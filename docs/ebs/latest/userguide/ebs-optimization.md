# Amazon EBS optimization

An Amazon EBS–optimized instance uses an optimized configuration stack and provides
additional, dedicated capacity for Amazon EBS I/O. This optimization provides the best
performance for your EBS volumes by minimizing contention between Amazon EBS I/O and other
traffic from your instance.

EBS–optimized instances deliver dedicated bandwidth to Amazon EBS. When attached to an
EBS–optimized instance:

- `io2` Block Express volumes are designed to deliver an average
  latency of under 500 microseconds for 16KiB I/O operations. `io2` Block Express volumes also deliver
  better outlier latency compared to General Purpose volumes, reducing the frequency of I/Os
  exceeding 800 microseconds by over 10 times. `io1` and `io2` volumes are designed to deliver at least 90% of their provisioned
  IOPS performance 99.9% of the time in a given year.
- `gp2` and `gp3` volumes are designed to deliver at least 90% of their provisioned IOPS
  performance 99% of the time in a given year.
- `st1` and `sc1` volumes deliver at least 90% of their expected throughput
  performance 99% of the time in a given year.
  Non-compliant periods are approximately uniformly distributed, targeting 99% of
  expected total throughput each hour. For more information, see [Amazon EBS volume types](ebs-volume-types.md "ebs-volume-types.md").

The I/O size of your workload will impact the observed average latency as latency increases
with larger I/O size. For example, `io2` Block Express volumes are designed to deliver an average
latency of under 500 microseconds for 16KiB I/O operations.

For more information, see [Amazon EBS–optimized instances](../../../AWSEC2/latest/UserGuide/ebs-optimized.md "../../../AWSEC2/latest/UserGuide/ebs-optimized.md")
in the _Amazon EC2 User Guide_.
