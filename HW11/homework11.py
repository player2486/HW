import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    """
    求解常係數齊次線性常微分方程 (ODE) 的通解。

    方程的一般形式為: a_n * y^(n) + a_{n-1} * y^(n-1) + ... + a_1 * y' + a_0 * y = 0
    其中 coefficients = [a_n, a_{n-1}, ..., a_0]。

    Args:
        coefficients (list or np.ndarray): ODE 的係數列表，從最高階項到零階項。

    Returns:
        str: ODE 的通解形式，例如 "y(x) = C_1e^(r1*x) + C_2e^(r2*x) + ... "。
    """
    if not coefficients or len(coefficients) == 0:
        return "係數列表不能為空。"

    # 1. 求解特徵方程的根 (Characteristic Equation Roots)
    # 使用 numpy.roots 求解特徵多項式的根
    # [a_n, a_{n-1}, ..., a_0] 經過 roots 得到 n 個複數根
    roots = np.roots(coefficients)
    
    # 設置容忍度，用於判斷數值誤差。
    # 例如，判斷一個數是否接近於零 (虛部或實部)。
    TOLERANCE = 1e-9

    # 2. 處理根的類型並計算每個根的重數 (Count Multiplicity)
    # 將根根據實部和虛部分類，並計算它們的重數。
    root_multiplicity = {} # 儲存 {根 (實數或複數元組): 重數}
    
    # 用於標記已處理的根，避免重複計算共軛根。
    processed_roots = set() 
    
    # 對每個根進行迭代處理
    for root in roots:
        # 由於 roots 輸出的是複數，我們將其分成實部 alpha 和虛部 beta
        alpha = root.real
        beta = root.imag

        # 數值穩定性處理：如果虛部或實部非常接近零，則視為零。
        if abs(beta) < TOLERANCE:
            beta = 0.0
        if abs(alpha) < TOLERANCE:
            alpha = 0.0

        # 將實數根和複數根進行標準化表示
        if beta == 0.0:
            # 實數根
            r_key = alpha
            
            # 處理複數根的對稱性 (共軛對)
            if r_key in processed_roots:
                continue
            
            # 計算實數根的重數
            # 由於 roots 函數可能產生微小差異的根，我們使用容忍度來判斷它們是否相同。
            count = sum(1 for r in roots if abs(r.real - alpha) < TOLERANCE and abs(r.imag) < TOLERANCE)
            root_multiplicity[r_key] = count
            processed_roots.add(r_key)
            
        else:
            # 複數共軛根：alpha + i*beta 和 alpha - i*beta
            # 僅需處理其中一個 (例如 alpha + i*beta)，另一個會自動產生。
            # 我們使用 (alpha, abs(beta)) 作為 key，因為 beta 已經是非零的
            
            # 為了避免在 roots 列表中重複處理 (a+bi) 和 (a-bi)，
            # 我們只處理 beta > 0 的部分，並將其標準化。
            if beta < 0:
                continue # 跳過負虛部 (alpha - i*beta)
            
            # 標準化 key 為 (alpha, beta)，其中 beta > 0
            r_key = (alpha, beta)
            
            # 判斷是否已經處理過 (例如，避免重複處理高階複數重根)
            if r_key in processed_roots:
                continue
            
            # 計算複數共軛對 (alpha + i*beta 和 alpha - i*beta) 的重數 m
            # 在特徵方程中，複數根總是以共軛對的形式出現。
            # 這裡的 'count' 是指 (alpha + i*beta) 這個根的重數 m。
            # 由於 roots 列表中的根是亂序的，我們需要計算 alpha + i*beta 的個數。
            count = sum(1 for r in roots if abs(r.real - alpha) < TOLERANCE and abs(r.imag - beta) < TOLERANCE)

            # 將複數根的標準化形式 (alpha, beta) 和它的重數 m 儲存
            root_multiplicity[r_key] = count
            
            # 將共軛對標記為已處理
            processed_roots.add(r_key)


    # 3. 構造通解 (Construct General Solution)
    solution_terms = []
    constant_index = 1 # 用於 C_1, C_2, ...
    
    # 根據分類好的根和重數來構造通解
    for root_key, multiplicity in root_multiplicity.items():
        # 實數根
        if isinstance(root_key, float):
            r = root_key
            # 通解形式: C_1*e^(rx) + C_2*x*e^(rx) + ... + C_m*x^(m-1)*e^(rx)
            for k in range(multiplicity):
                term = f"C_{constant_index}"
                if k > 0:
                    term += f"x^{k}" if k > 1 else "x" # 加上 x^(k-1)
                term += f"e^({r}x)"
                solution_terms.append(term)
                constant_index += 1
                
        # 複數共軛根 (alpha + i*beta, alpha - i*beta)
        elif isinstance(root_key, tuple) and len(root_key) == 2:
            alpha, beta = root_key
            
            # 通解形式: e^(αx) * [ (C_1 + C_2x + ...)cos(βx) + (C_m+1 + C_m+2x + ...)sin(βx) ]
            # 這裡 multiplicity = m，表示 alpha + i*beta (和 alpha - i*beta) 都是 m 重根
            
            # 構造 (C_1 + C_2x + ... + C_m*x^(m-1)) * cos(βx)
            cos_terms = []
            for k in range(multiplicity):
                cos_term = f"C_{constant_index}"
                if k > 0:
                    cos_term += f"x^{k}" if k > 1 else "x"
                cos_terms.append(cos_term)
                constant_index += 1
                
            # 構造 (C_m+1 + C_m+2x + ... + C_2m*x^(m-1)) * sin(βx)
            sin_terms = []
            for k in range(multiplicity):
                sin_term = f"C_{constant_index}"
                if k > 0:
                    sin_term += f"x^{k}" if k > 1 else "x"
                sin_terms.append(sin_term)
                constant_index += 1
            
            # 將兩組項合併為一個解的項
            # 格式: e^(αx)[(C_a + ...)cos(βx) + (C_b + ...)sin(βx)]
            
            # 處理 alpha = 0 的情況，e^(0x) = 1，可省略
            exp_term = f"e^({alpha}x)" if alpha != 0.0 else ""
            
            # 將 cos 和 sin 裡面的 C_i*x^k 合併
            cos_part = " + ".join(cos_terms)
            sin_part = " + ".join(sin_terms)
            
            # 組合 cos 和 sin 部分
            if exp_term:
                full_term = f"{exp_term}[({cos_part})cos({beta}x) + ({sin_part})sin({beta}x)]"
            else:
                full_term = f"({cos_part})cos({beta}x) + ({sin_part})sin({beta}x)"
                
            solution_terms.append(full_term)
            
    # 4. 輸出最終通解
    if not solution_terms:
        return "y(x) = 0 (可能係數錯誤或只有零解)"
    
    return "y(x) = " + " + ".join(solution_terms)

# 以下是測試主程式 (使用提供的程式碼)

# 範例測試 (1): 實數單根: y'' - 3y' + 2y = 0  特徵方程: lambda^2 - 3lambda + 2 = 0, 根: 1, 2
# 預期解: C_1e^(1x) + C_2e^(2x)
print("--- 實數單根範例 ---")
coeffs1 = [1, -3, 2]
print(f"方程係數: {coeffs1}")
print(solve_ode_general(coeffs1))

# 範例測試 (2): 實數重根: y'' - 4y' + 4y = 0  特徵方程: lambda^2 - 4lambda + 4 = 0, 根: 2, 2
# 預期解: C_1e^(2x) + C_2xe^(2x)
print("\n--- 實數重根範例 ---")
coeffs2 = [1, -4, 4]
print(f"方程係數: {coeffs2}")
print(solve_ode_general(coeffs2))

# 範例測試 (3): 複數共軛根: y'' + 4y = 0  特徵方程: lambda^2 + 4 = 0, 根: 2i, -2i (alpha=0, beta=2)
# 預期解: C_1cos(2x) + C_2sin(2x)
print("\n--- 複數共軛根範例 ---")
coeffs3 = [1, 0, 4]
print(f"方程係數: {coeffs3}")
print(solve_ode_general(coeffs3))

# 範例測試 (4): 複數重根 (二重): (D^2 + 1)^2 y = 0  特徵方程: (lambda^2 + 1)^2 = 0, 根: i, i, -i, -i (alpha=0, beta=1, m=2)
# 預期解: C_1cos(1x) + C_2sin(1x) + C_3xcos(1x) + C_4xsin(1x)
print("\n--- 複數重根範例 ---")
coeffs4 = [1, 0, 2, 0, 1]
print(f"方程係數: {coeffs4}")
print(solve_ode_general(coeffs4))

# 範例測試 (5): 高階重根: y''' - 6y'' + 12y' - 8y = 0  特徵方程: (lambda - 2)^3 = 0, 根: 2, 2, 2
# 預期解: C_1e^(2x) + C_2xe^(2x) + C_3x^2e^(2x)
print("\n--- 高階重根範例 ---")
coeffs5 = [1, -6, 12, -8]
print(f"方程係數: {coeffs5}")
print(solve_ode_general(coeffs5))