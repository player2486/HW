import cmath

def dft(f_n):
    """
    執行離散傅立葉正轉換 (DFT)。
    
    參數:
        f_n (list/tuple): 輸入的離散序列 (時域信號)。
        
    回傳:
        list: 轉換後的頻域序列 X_k (複數)。
    """
    N = len(f_n)
    X_k = []
    
    for k in range(N):
        sum_of_terms = 0 + 0j 
        
        for n in range(N):
            exponent = (-2j * cmath.pi * k * n) / N
            W_kn = cmath.exp(exponent)
            
            sum_of_terms += f_n[n] * W_kn
            
        X_k.append(sum_of_terms)
        
    return X_k

def idft(X_k):
    """
    執行逆離散傅立葉轉換 (IDFT)。
    
    參數:
        X_k (list): 輸入的頻域序列 (複數)。
        
    回傳:
        list: 逆轉換後的時域序列 (複數)。
    """
    N = len(X_k)
    f_n_restored = []
    
    for n in range(N):
        sum_of_terms = 0 + 0j 
        
        for k in range(N):
            exponent = (2j * cmath.pi * k * n) / N
            W_kn_inverse = cmath.exp(exponent)
            
            sum_of_terms += X_k[k] * W_kn_inverse
            
        f_n = sum_of_terms / N
        f_n_restored.append(f_n)
        
    return f_n_restored

def simplify_result(complex_list, tolerance=1e-9):
    """將結果中的極小虛部四捨五入為 0，並只取實部。"""
    real_list = []
    for z in complex_list:
        if abs(z.imag) < tolerance:
            real_list.append(z.real)
        else:
            real_list.append(z) 
    return real_list

f = [1.0, 2.0, 3.0, 4.0]

print(f"--- 原始函數 f ---")
print(f"f = {f}")

F = dft(f)

print("\n--- 正轉換 F(ω) ---")
print(f"F = {[round(c.real, 4) + round(c.imag, 4) * 1j for c in F]}")

f_restored_complex = idft(F)

print("\n--- 逆轉換 f_restored (複雜結果) ---")
print(f"f_restored = {[round(c.real, 9) + round(c.imag, 9) * 1j for c in f_restored_complex]}")

f_restored = simplify_result(f_restored_complex)

print("\n--- 驗證與簡化 (去除極小虛部) ---")
print(f"f_restored (簡化後) = {[round(x, 4) for x in f_restored]}")

is_close = all(abs(f[i] - f_restored[i]) < 1e-9 for i in range(len(f)))

print(f"\n驗證結果：原始 f 和還原後的 f_restored 是否相同 (誤差容忍度 1e-9)? **{is_close}**")