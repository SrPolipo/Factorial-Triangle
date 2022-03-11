class coeff:
    def __init__(self,arg):
        if type(arg) == list:
            self.id = arg
            return None
        if type(arg) == int:
            self.id = [1,-arg]
            return None
    def __repr__(self):
        c1 = self.id
        l = len(c1)
        s = [f"{c1[i]}x^{l-1-i}" if c1[i] != 1 else f"x^{l-1-i}" for i in range(l-2)] + [f"{c1[l-2]}x" if c1[l-2] != 1 else "x"] + [str(c1[l-1])]
        return " + ".join(s)
    def __add__(self,c2):
        c1 = self.id
        if type(c2) == coeff:
            c2 = c2.id
        l1 = len(c1)
        l2 = len(c2)
        if l1 >= l2:
            c2 = [0]*(l1-l2) + c2
            m = l1
        if l2 > l1:
            c1 = [0]*(l2-l1)+ c1
            m = l2
        return coeff([c1[i] + c2[i] for i in range(m)])
    def __mul__(self, c2):
        c1 = self.id
        if type(c2) == coeff:
            c2 = c2.id
        meta = []
        for i,elem in enumerate(c1):
            meta.append(coeff([elem * k for k in c2]+ [0]*(len(c1) - i - 1)))
        s = meta[0]
        for i in meta[1:]:
            s+= i
        return s



x=coeff(0)
for i in range(1,10):
    print(x)
    x = x*coeff(i)
