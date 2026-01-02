**HW1**  
原創  
方法：  
用前向差分法計算導數 df(f, x)  
用黎曼和計算定積分 integral(f, a, b)  
對積分函數 F(x)=∫₀ˣ f(t) dt 做數值微分，檢驗 F'(x) ≈ f(x)

**HW2**  
原創  
方法：  
計算判別式 D = b² − 4ac  
使用二次公式求根：  
r1 = (-b + √D) / (2a)  
r2 = (-b - √D) / (2a)  
印出 ax² + bx + c 代入根的結果，確認是否接近 0  
回傳兩個根 (r1, r2)

**HW3**  
AI資料遺失  
標準化三次方程：  
ax³ + bx² + cx + d = 0 ⇒ x³ + px + q = 0  
p = (3*a*c - b²)/(3*a²)  
q = (2*b³ - 9*a*b*c + 27*a²*d)/(27*a³)  
判別式與立方根：  
Δ = (q/2)² + (p/3)³  
u = (-q/2 + Δ^(1/2))^(1/3)  
v = (-q/2 - Δ^(1/2))^(1/3)  
三個根公式：  
t1 = u + v  
t2 = ω*u + ω²*v  
t3 = ω²*u + ω*v  
ω = e^(2πi/3)  
反變換：x = t − b/(3a)

**HW4**  
AI資料遺失  
多項式值與導數計算：  
poly_val(coef, x) → 用 Horner 法計算 P(x)  
poly_derivative(coef) → 計算 P'(x)  
牛頓法求根：初值 x 隨機複數  
x_new = x - P(x)/P'(x)  
收斂條件：|P(x)| < tol  
多項式降階 (deflation)：P(x) = (x−r)Q(x)，對 Q(x) 繼續找根，最後剩一階直接解出最後根

**HW5**  
GPT [連結](https://chatgpt.com/share/695771f7-5f74-8011-8ea8-5b97ad960546)

**HW6**  
GPT [連結](https://chatgpt.com/share/6957d189-3888-8011-8326-2d6c8e263add)  
點(Point)：平面上的座標 (x, y)  
線(Line)：  
斜率 m = (y2 - y1)/(x2 - x1)  
截距 b = y1 - m*x1  
交點透過解聯立方程求解  
垂線斜率互為負倒數 m⊥ = -1/m  
圓(Circle)：(x−h)² + (y−k)² = r²  
直線交圓 → 將線方程帶入圓方程解二次方程  
圓交圓 → 使用距離公式與圓方程  
三角形(Triangle)：邊長用距離公式  
畢氏定理 a² + b² = c²  
平移/縮放/旋轉公式

**HW7**  
Gemini [連結](https://gemini.google.com/share/55f6bd481b17)  
GPT [連結](https://chatgpt.com/share/6957c249-f66c-8011-a2a4-0c372d01d58a)

**HW8**  
GPT [連結](https://chatgpt.com/share/6957c5ab-fd94-8011-ab7a-fecb889d3e39)  
機率計算、對數計算、資訊理論量（熵、交叉熵、KL 散度、互資訊）、交叉熵不等式驗證、漢明碼編碼與解碼、夏農信道容量

**HW9**  
GPT [連結](https://chatgpt.com/share/6957cad3-8c1c-8011-96b6-85ac30a9d4f9)  
遞迴計算行列式（Laplace 展開法）  
LU 分解後計算行列式  
驗證 LU / 特徵值分解 / SVD  
用特徵值分解做 SVD  
PCA 主成份分析

**HW10**  
Gemini [連結](https://gemini.google.com/share/e2f95998218f)  
DFT/IDFT 定義與算式  
程式碼實現核心  
驗證互為反函式

**HW11**  
GPT [連結](https://chatgpt.com/share/6957ce10-e200-8011-8228-e66a29de9ce6)  
常係數齊次微分方程：  
a_n y^(n) + a_{n-1} y^(n-1) + … + a_1 y' + a_0 y = 0  
假設解 y = e^(λx)  
代入微分方程得到特徵方程：  
a_n λ^n + a_{n-1} λ^(n-1) + … + a_1 λ + a_0 = 0
