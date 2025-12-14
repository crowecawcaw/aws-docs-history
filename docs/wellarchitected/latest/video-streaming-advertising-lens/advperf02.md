# Compute and hardware

The optimal compute choice for a particular workload can vary
based on application design, usage patterns, and configuration
settings. Architectures may use different compute choices for
various components and allow different features to improve
performance. Selecting a fitting compute choice for an
architecture can improve performance efficiency. 

| ADVPERF02:  How do you select and configure compute resources to optimize ISV compatibility, scaling, latency, and costs for ad workloads? |
| ------------------------------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                            |

There are many compute choices to be considered for advertising
workloads, with popular adtech ISV products, cloud native and
machine learning needs, addressing low latency, burst traffic,
and scaling design principles.

###### Best practices

- [ADVPERF02-BP01 Evaluate compute benchmarks and compute options certified by the ISVs if applicable](advperf02-bp01.md "advperf02-bp01.md")
- [ADVPERF02-BP02 Consider containerization for scalability, low latency, and cost optimization](advperf02-bp02.md "advperf02-bp02.md")
- [ADVPERF02-BP03 Consider using low latency scaling tools like Karpenter to improve startup and scaling time](advperf02-bp03.md "advperf02-bp03.md")
- [ADVPERF02-BP04 Use a specialized instance family and features](advperf02-bp04.md "advperf02-bp04.md")
- [ADVPERF02-BP05 Evaluate ARM architecture for performance considerations by using AWS Graviton](advperf02-bp05.md "advperf02-bp05.md")
