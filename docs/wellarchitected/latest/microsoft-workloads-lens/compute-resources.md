# Compute resources

Optimizing compute resources for Microsoft workloads running on
Windows servers requires careful selection of EC2 instance families
and features that align with workload requirements. This includes
choosing appropriate instance types for different use cases,
leveraging performance-enhancing features like EC2 Fast Launch and
EBS optimizations, and utilizing instance store storage for
high-performance scenarios. By understanding the performance
characteristics of different compute options, organizations can
maximize the efficiency of their Windows-based applications while
maintaining cost-effectiveness.

| MSFTPERF02: How do you select the appropriate compute<br>resources and features for your Microsoft workloads running<br>on Windows servers? |
| ------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                             |

Amazon EC2 provides scalability, flexibility, and cost efficiency
resources that can apply to Windows EC2 instances. Appropriate
instance families and EC2 features can be used by your Windows
machines to bring the performance efficiency needed by your
workload.

###### Best practices

- [MSFTPERF02-BP01 Choose the Amazon EC2 instance families that
  best fit the Microsoft workload](msftperf02-bp01.md "msftperf02-bp01.md")
- [MSFTPERF02-BP02 Consider the use for EC2 Fast Launch to
  accelerate launching your Microsoft workload instances](msftperf02-bp02.md "msftperf02-bp02.md")
- [MSFTPERF02-BP03 Consider using Amazon EBS fast snapshot
  restore](msftperf02-bp03.md "msftperf02-bp03.md")
- [MSFTPERF02-BP04 Consider using Amazon EBS Provisioned Rate for
  Volume Initialization](msftperf02-bp04.md "msftperf02-bp04.md")
