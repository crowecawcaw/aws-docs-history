# Choosing Metric Statistics and Periods

While CloudWatch will allow you to choose any statistic and period for each metric, not all
combinations will be useful. For example, the Average, Minimum, and Maximum statistics
for CPUUtilization are useful, but the Sum statistic is not.

All MemoryDB samples are published for a 60 second duration for each individual node. For any 60 second period, a node metric will only contain a single
sample.
