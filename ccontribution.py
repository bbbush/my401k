from contribution import contribution

class ccontribution:
    def __init__(self, limit,income,nm=12,match=7):
        self._c= contribution(limit,income,match)
        self._nm=self._c.check(nm)

    def residuals_percentage(self,r):
        r=.0+max(0,r)
        return round(0.5+100*(r/(self._c._income/self._nm)))/100

    def all_contribution_amounts(self,x):
        return self._c.all_contribution_amounts(self._nm,x)

    def report(self,x):
        amounts=self.all_contribution_amounts(x)
        print x,amounts,
        r=self._c.round(self._c._limit-sum(amounts))
        if r>0:
            print "{0:.2f} {1:.0%}".format(r,self.residuals_percentage(r)) # year end
        else:
            print

    def all_reports(self):
        t=tuple(self._c.all_contributions(self._nm))
        print zip(*t)[1] # minimum
        for i,j in t:
            if j>100:
                continue
            self.report(i)

