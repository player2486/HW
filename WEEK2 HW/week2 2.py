import random

class FiniteFieldAdditiveGroup:
    def __init__(self, p):
        self.p = p
        self._identity = 0  # 加法單位元為 0
    
    @property
    def identity(self):
        return self._identity

    def operation(self, a, b):
        if not (self.include(a) and self.include(b)):
            raise TypeError("輸入必須是有限體元素 (int)")
        
        return (a + b) % self.p

    def inverse(self, val):
        if not self.include(val):
            raise TypeError("輸入必須是有限體元素 (int)")
        
        return (-val) % self.p

    def include(self, element):
        return isinstance(element, int) and 0 <= element < self.p

    def random_generate(self):
        return random.randint(0, self.p - 1)


# --- 測試 ---
G = FiniteFieldAdditiveGroup(5)  # 𝔽5
a, b = 3, 4
print("a =", a, "b =", b)
print("a + b =", G.operation(a, b))
print("a 的逆元 =", G.inverse(a))
print("單位元 =", G.identity)
print("隨機元素 =", G.random_generate())
