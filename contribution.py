class contribution:
    def __init__(self,limit,income,match=7):
        self._limit=.0+max(0,limit)
        self._income=.0+max(0,income)
        self._mm=100*self._limit/self._income
        self._match = min(max(0,int(match)), int(0.5+self._mm))

    def check(self,nm):
        return max(1,int(nm))

    def check2(self,nm,x):
        nm=self.check(nm)
        x=min(nm,max(0,int(x)))
        return nm,x

    def contribute_value(self,nm,x):
        nm,x=self.check2(nm,x)
        return self._match+max(0,int(0.5+self._mm-self._match)*nm/x) # no reduce

    def all_contributions(self,nm):
        nm=self.check(nm)
        for i in range(nm):
            yield (i+1,self.contribute_value(nm,i+1))

    def all_contribution_values(self,nm):
        nm=self.check(nm)
        return (j for i,j in self.all_contributions(nm))

    def round(self,a):
        return int(0.5+100*a)/100.0

    def contribute_amount(self,nm,c):
        nm=self.check(nm)
        c=max(0,c)
        return self.round(self._income/nm*c/100)

    def append_amount(self,l,a,s):
        if self._limit-s>a:
            l.append(a)
            s+=a
        else:
            l.append(self.round(self._limit-s))
            s=self._limit
        return s

    def all_contribution_amounts(self,nm,x):
        nm,x=self.check2(nm,x)
        result=[]
        s=0
        c=self.contribute_value(nm,x)
        a1=self.contribute_amount(nm,c)
        for i in range(x):
            s=self.append_amount(result,a1,s)
        a2=self.contribute_amount(nm,self._match)
        for i in range(x,nm):
            s=self.append_amount(result,a2,s)
        return result

    def contribute_percentage(self,nm,r):
        nm=self.check(nm)
        r=.0+max(0,r)
        return int(0.5+r*100/(self._income/nm))

    def residuals(self,nm,x):
        nm,x=self.check2(nm,x)
        r=0
        return self._limit-sum(self.all_contribution_amounts(nm,x))

