import ccontribution

if __name__=="__main__":
    salary=70000
    exclusion=salary/10
    limit=17500-exclusion # exclude expected bonus contribution and all contributions so far
    c=ccontribution.ccontribution(limit,salary,24)
    c.all_reports()

