import numpy as np

# 5. 7-4 漢明碼的編碼與解碼

# 7-4 漢明碼的生成矩陣 G (4x7)
# G 的每一行是一個基向量，將資料位元映射到碼字
# 碼字 C = D * G (這裡 D 是行向量)
G = np.array([
    [1, 1, 0, 1, 0, 0, 0],  # d4 -> c7, c6, c4
    [1, 0, 1, 0, 1, 0, 0],  # d3 -> c7, c5, c2
    [0, 1, 1, 0, 0, 1, 0],  # d2 -> c6, c5, c1
    [1, 1, 1, 0, 0, 0, 1]   # d1 -> c7, c6, c5
], dtype=int)

# 7-4 漢明碼的校驗矩陣 H (3x7)
# 伴隨式 S = R * H^T (這裡 R 是行向量)
# H 的列向量是 7 個非零 3 位元向量的二進制表示 (1, 2, 3, 4, 5, 6, 7)
H = np.array([
    [0, 0, 0, 1, 1, 1, 1],  # c4
    [0, 1, 1, 0, 0, 1, 1],  # c2
    [1, 0, 1, 0, 1, 0, 1]   # c1
], dtype=int)

def hamming_encode(data_bits):
    """
    7-4 漢明碼編碼
    data_bits: 長度為 4 的 numpy array (d4, d3, d2, d1)
    """
    data_bits = np.array(data_bits, dtype=int)
    if data_bits.shape != (4,):
        raise ValueError("資料位元必須是長度為 4 的向量")
        
    # C = D * G mod 2
    # C = [c7, c6, c5, c4, c3, c2, c1]
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

    # 1. 計算伴隨式 S (Syndrome)
    # S = R * H^T mod 2
    # H^T 是 7x3 矩陣
    syndrome = np.dot(received_codeword, H.T) % 2 # S = [s4, s2, s1]

    # 將伴隨式轉為十進制，作為錯誤位元的位置 (0 代表無錯誤)
    # [s4, s2, s1] 
    error_pos = syndrome[0] * 4 + syndrome[1] * 2 + syndrome[2] * 1
    
    # 2. 糾錯
    corrected_codeword = np.copy(received_codeword)
    if error_pos != 0:
        print(f"   - 檢測到第 {error_pos} 位元有錯誤 (從右邊數，1-based)")
        # 反轉錯誤位元 (error_pos - 1 是 0-based 索引)
        corrected_codeword[7 - error_pos] = 1 - corrected_codeword[7 - error_pos]
    else:
        print("   - 未檢測到錯誤")
        
    # 3. 提取資料位元
    # (c7, c6, c5, c3) 對應 (d4, d3, d2, d1)
    # 碼字索引 (0-based): 0, 1, 2, 4
    # 資料索引 (0-based): 0, 1, 2, 3
    data_bits = [
        corrected_codeword[0],  # d4 = c7
        corrected_codeword[1],  # d3 = c6
        corrected_codeword[2],  # d2 = c5
        corrected_codeword[4]   # d1 = c3
    ]
    
    return corrected_codeword, np.array(data_bits)

# --- 範例測試 ---
data_in = [1, 0, 1, 0] # (d4, d3, d2, d1)
codeword = hamming_encode(data_in)

# 模擬傳輸錯誤 (假設第 5 位元 c5 發生錯誤，即索引 2)
# 碼字: [c7, c6, c5, c4, c3, c2, c1]
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