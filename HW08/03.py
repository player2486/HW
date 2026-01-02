import numpy as np
import math

def entropy(P):
    """計算機率分佈 P 的熵 (H(P))，使用 log2。"""
    P = np.array(P)
    P = P[P > 1e-9]
    return -np.sum(P * np.log2(P))

def cross_entropy(P, Q):
    """計算機率分佈 P 和 Q 的交叉熵 (H(P, Q))，使用 log2。"""
    P = np.array(P)
    Q = np.array(Q)
    
    Q = np.where(Q < 1e-9, 1e-9, Q)
    
    non_zero_P_indices = P > 1e-9
    
    return -np.sum(P[non_zero_P_indices] * np.log2(Q[non_zero_P_indices]))

def kl_divergence(P, Q):
    """計算 P 相對於 Q 的 KL 散度 (D_KL(P || Q))，使用 log2。"""
    P = np.array(P)
    Q = np.array(Q)
    
    non_zero_P_indices = P > 1e-9
    
    Q = np.where(Q < 1e-9, 1e-9, Q)

    return np.sum(P[non_zero_P_indices] * np.log2(P[non_zero_P_indices] / Q[non_zero_P_indices]))

def mutual_information(P_XY):
    """計算隨機變數 X 和 Y 的互資訊 (I(X; Y))。
    P_XY 是一個聯合機率分佈的矩陣。"""
    P_XY = np.array(P_XY)
    
    P_X = np.sum(P_XY, axis=1) 
    P_Y = np.sum(P_XY, axis=0) 
    
    H_X = entropy(P_X)
    H_Y = entropy(P_Y)
    
    H_XY = entropy(P_XY.flatten())
    
    I_XY = H_X + H_Y - H_XY
    return I_XY, H_X, H_Y, H_XY

# --- 範例計算 ---
P = [0.5, 0.5]
Q = [0.8, 0.2] 
P_XY_example = [ 
    [0.2, 0.3], 
    [0.1, 0.4] 
]

print("\n3. 資訊理論量計算範例:")
print(f"   - 分佈 P: {P}, Q: {Q}")
print(f"   - 熵 H(P): {entropy(P):.4f} bits")
print(f"   - 交叉熵 H(P, P): {cross_entropy(P, P):.4f} bits")
print(f"   - 交叉熵 H(P, Q): {cross_entropy(P, Q):.4f} bits")
print(f"   - KL 散度 D_KL(P || Q): {kl_divergence(P, Q):.4f} bits")

I_XY, H_X, H_Y, H_XY = mutual_information(P_XY_example)
print(f"   - 聯合機率 P(X, Y):\n{np.array(P_XY_example)}")
print(f"   - 互資訊 I(X; Y): {I_XY:.4f} bits (H(X)={H_X:.4f}, H(Y)={H_Y:.4f}, H(X,Y)={H_XY:.4f})")