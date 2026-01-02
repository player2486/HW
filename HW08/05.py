import numpy as np

G = np.array([
    [1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0],  
    [0, 1, 1, 0, 0, 1, 0], 
    [1, 1, 1, 0, 0, 0, 1]  
], dtype=int)

H = np.array([
    [0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 1], 
    [1, 0, 1, 0, 1, 0, 1] 
], dtype=int)

def hamming_encode(data_bits):
    """
    7-4 漢明碼編碼
    data_bits: 長度為 4 的 numpy array (d4, d3, d2, d1)
    """
    data_bits = np.array(data_bits, dtype=int)
    if data_bits.shape != (4,):
        raise ValueError("資料位元必須是長度為 4 的向量")
        
    codeword = np.dot(data_bits, G) % 2
    return codeword

def hamming_decode(received_codeword):
    """
    7-4 漢明碼解碼和糾錯 (糾正一位錯誤)
    received_codeword: 長度為 7 的 numpy array (r7, r6, r5, r4, r3, r2, r1)
    """
    received_codeword = np.array(received_codeword, dtype=int)
    if received_codeword.shape != (7,):
        raise ValueError("接收碼字必須是長度為 7 的向量")

    syndrome = np.dot(received_codeword, H.T) % 2 

    error_pos = syndrome[0] * 4 + syndrome[1] * 2 + syndrome[2] * 1
    
    corrected_codeword = np.copy(received_codeword)
    if error_pos != 0:
        print(f"   - 檢測到第 {error_pos} 位元有錯誤 (從右邊數，1-based)")
        corrected_codeword[7 - error_pos] = 1 - corrected_codeword[7 - error_pos]
    else:
        print("   - 未檢測到錯誤")
        
    data_bits = [
        corrected_codeword[0],
        corrected_codeword[1], 
        corrected_codeword[2], 
        corrected_codeword[4] 
    ]
    
    return corrected_codeword, np.array(data_bits)

data_in = [1, 0, 1, 0] 
codeword = hamming_encode(data_in)

error_pos_idx = 2
received = np.copy(codeword)
received[error_pos_idx] = 1 - received[error_pos_idx]

print("\n5. 7-4 漢明碼編碼與解碼範例:")
print(f"   - 原始資料: {data_in}")
print(f"   - 編碼結果 (Codeword): {codeword}")
print(f"   - 接收碼字 (第 {7 - error_pos_idx} 位元錯誤): {received}")

corrected, data_out = hamming_decode(received)

print(f"   - 糾錯後碼字: {corrected}")
print(f"   - 解碼資料: {data_out}")
print(f"   - 解碼是否成功: {np.array_equal(data_in, data_out)}")