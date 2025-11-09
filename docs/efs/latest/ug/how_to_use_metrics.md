# Using CloudWatch metrics for Amazon EFS

The metrics reported by Amazon EFS provide information that you can analyze in
different ways. The following list shows some common uses for the metrics. These are
suggestions to get you started, not a comprehensive list.

| How do I?                                                                                  | Relevant metrics                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| How can I determine my throughput?                                                         | You can monitor the daily `Sum` statistic of the<br>`TotalIOBytes` metric to see your throughput.                                                                                                                                    |
| How can I determine the total amount of data transferred?                                  | You can monitor the daily `Sum` statistic of `MeteredIOBytes` to<br>see your total data transferred.                                                                                                                                 |
| How can I track the number of Amazon EC2 instances that are connected to a<br>file system? | You can monitor the `Sum` statistic of the `ClientConnections` metric.<br>To calculate the average `ClientConnections` for periods greater than<br>one minute, divide the sum by the number of minutes in the period.                |
| How can I see my burst credit balance?                                                     | You can see your balance by monitoring the<br>`BurstCreditBalance` metric for your file system. For more<br>information on bursting and burst credits, see [Bursting throughput](performance.md#bursting "performance.md#bursting"). |

## Monitoring throughput

performance

The CloudWatch metrics for throughput monitoring—`TotalIOBytes`,
`ReadIOBytes`, `WriteIOBytes`, and
`MetadataIOBytes`— represent the actual throughput that you are driving
on your file system. The metric `MeteredIOBytes` represents the calculation of
the overall metered throughput that you are driving. You can use the **Throughput
utilization (%)** graph in the Amazon EFS console **Monitoring**
section to monitor your throughput utilization. If you use custom CloudWatch dashboards or
another monitoring tool, you can create a [CloudWatch metric math expression](monitoring-metric-math.md#metric-math-throughput-utilization "monitoring-metric-math.md#metric-math-throughput-utilization") that
compares `MeteredIOBytes` to `PermittedThroughput`.

`PermittedThroughput` measures the amount of allowed throughput for the
file system. This value is based on one of the following methods:

- For file systems in Elastic throughput, this value reflects the
  maximum write throughput of the file system.
- For file systems using Provisioned throughput, if the amount of data
  stored in the EFS Standard storage class allows your file system to drive a
  higher throughput than you provisioned, this metric reflects the higher throughput
  instead of the provisioned amount.
- For file systems using Bursting throughput, this value is a function
  of the file system size and `BurstCreditBalance`. Monitor
  `BurstCreditBalance` to ensure that your file system is operating at its
  burst rate rather than its base rate. If the balance is consistently at or near zero,
  consider switching to Elastic throughput or Provisioned
  throughput to get additional throughput.

When the values for `MeteredIOBytes` and `PermittedThroughput`
are equal, your file system is consuming all available throughput. For file systems using
Provisioned throughput, you can provision additional throughput.
