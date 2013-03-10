from contribution import contribution

class ccontribution:
    def __init__(self, limit,income,nm=12,match=7):
        self._c= contribution(limit,income,match)
        self._nm=self._c.check(nm)

    def all_contribution_values(self):
        return self._c.all_contribution_values(self._nm)

    def residuals(self,x):
        return self._c.residuals(self._nm,x)

    def contribute_percentage(self,r):
        return self._c.contribute_percentage(self._nm,r)


    def all_contribution_amounts(self,x):
        return self._c.all_contribution_amounts(self._nm,x)

    def report(self,x):
        amounts=self.all_contribution_amounts(x)
        print x,amounts,
        r=self.residuals(x)
        if self._c.round(r)>0:
            print "{0:.2f} {1:.0%}".format(r,self.contribute_percentage(r)) # year end
        else:
            print

    def all_reports(self):
        t=tuple(self._c.all_contributions(self._nm))
        print zip(*t)[1] # minimum
        for i,j in t:
            if j>100:
                continue
            self.report(i)

