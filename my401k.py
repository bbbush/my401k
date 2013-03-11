import ccontribution

if __name__=="__main__":
    nm=24
    rnm=18
    salary=72000.0 # updated
    exclusion=10000 # data from ADP
    limit=17500-exclusion # exclude expected bonus contribution and all contributions so far
    c=ccontribution.ccontribution(limit,salary*rnm/nm,rnm)
    c.all_reports()

