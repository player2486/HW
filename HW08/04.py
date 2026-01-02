import numpy as np

def cross_entropy(P, Q):
    """計算機率分佈 P 和 Q 的交叉熵 (H(P, Q))，使用 log2。"""
    P = np.array(P)
    Q = np.array(Q)
    
    Q = np.where(Q < 1e-9, 1e-9, Q)
    
    non_zero_P_indices = P > 1e-9
    
    return -np.sum(P[non_zero_P_indices] * np.log2(Q[non_zero_P_indices]))

P_same = [0.1, 0.2, 0.7]   
Q_diff = [0.2, 0.3, 0.5]    

CE_P_P = cross_entropy(P_same, P_same) 