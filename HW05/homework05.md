問題
什麼是有限體？

AI 答
有限體（Finite Field，又稱 Galois Field）是一種元素個數有限的代數結構，記作 GF(pⁿ)，其中 p 為質數、n 為正整數。
有限體同時具備以下性質：
加法形成一個交換群（Abelian Group）
有加法單位元（0）
每個元素都有加法反元素
加法滿足封閉性、結合律、交換律
乘法在去除 0 後形成一個交換群
乘法單位元（1）
每個非零元素都有乘法反元素
加法與乘法之間滿足分配律
a × (b + c) = a × b + a × c
最簡單的有限體是 GF(p)，其中 p 為質數，其元素為 {0, 1, 2, ..., p-1}，運算皆在 mod p 下進行。

一、有限體元素類別（運算子重載）
class FiniteFieldElement:
    def __init__(self, value, p):
        if p <= 1:
            raise ValueError("p must be a prime")
        self.p = p
        self.value = value % p

    def __repr__(self):
        return f"GF({self.p})[{self.value}]"

    def __eq__(self, other):
        return isinstance(other, FiniteFieldElement) and \
               self.p == other.p and self.value == other.value

    # 加法
    def __add__(self, other):
        self._check(other)
        return FiniteFieldElement(self.value + other.value, self.p)

    def __neg__(self):
        return FiniteFieldElement(-self.value, self.p)

    def __sub__(self, other):
        return self + (-other)

    # 乘法
    def __mul__(self, other):
        self._check(other)
        return FiniteFieldElement(self.value * other.value, self.p)

    # 乘法反元素（用費馬小定理）
    def inv(self):
        if self.value == 0:
            raise ZeroDivisionError("0 has no multiplicative inverse")
        return FiniteFieldElement(pow(self.value, self.p - 2, self.p), self.p)

    def __truediv__(self, other):
        return self * other.inv()

    def _check(self, other):
        if not isinstance(other, FiniteFieldElement) or self.p != other.p:
            raise TypeError("Operands must be in the same finite field")

二、加法群（對應 RationalAddGroup）
class FiniteFieldAddGroup:
    def __init__(self, p):
        self.p = p
        self.elements = [FiniteFieldElement(i, p) for i in range(p)]

    def op(self, a, b):
        return a + b

    def identity(self):
        return FiniteFieldElement(0, self.p)

    def inverse(self, a):
        return -a


→ 可通過 group_axioms.py 的加法群檢驗

三、乘法群（排除 0，對應 RationalMulGroup）
class FiniteFieldMulGroup:
    def __init__(self, p):
        self.p = p
        self.elements = [FiniteFieldElement(i, p) for i in range(1, p)]

    def op(self, a, b):
        return a * b

    def identity(self):
        return FiniteFieldElement(1, self.p)

    def inverse(self, a):
        return a.inv()


→ 非零元素形成群

四、分配律（field_axioms.py 對應）
def check_distributivity(field_elements):
    for a in field_elements:
        for b in field_elements:
            for c in field_elements:
                if a * (b + c) != a * b + a * c:
                    return False
    return True

五、有限體類別（整合）
class FiniteField:
    def __init__(self, p):
        self.p = p
        self.elements = [FiniteFieldElement(i, p) for i in range(p)]
        self.add_group = FiniteFieldAddGroup(p)
        self.mul_group = FiniteFieldMulGroup(p)

六、使用示範（像整數一樣）
F = FiniteField(7)

a = FiniteFieldElement(3, 7)
b = FiniteFieldElement(5, 7)

print(a + b)      # GF(7)[1]
print(a * b)      # GF(7)[1]
print(a - b)      # GF(7)[5]
print(a / b)      # GF(7)[2]

print(check_distributivity(F.elements))  # True

七、我的理解與反思
透過 AI 問答，我先理解「有限體」並不是抽象名詞，而是一個同時具備加法群、乘法群（非零）與分配律的結構。
老師提供的 field_rational.py、group_axioms.py 與 field_axioms.py，實際上就是把代數定義轉成「可被程式驗證的公理」。
這次作業讓我理解到：
數學中的「群、體、公理」可以直接對應成程式介面
group_axioms.py 就像自動證明工具
運算子重載讓抽象結構變得像內建型別一樣好用
這也讓我更清楚 抽象代數與軟體設計 之間的連結。