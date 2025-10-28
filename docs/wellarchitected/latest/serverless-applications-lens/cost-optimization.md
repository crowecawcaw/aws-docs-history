# Cost optimization pillar

The cost optimization pillar includes the continual process of refinement and improvement of
a system over its entire lifecycle. From the initial design of your first proof of concept to
the ongoing operation of production workloads, adopting the practices in this document will
enable you to build and operate cost-aware systems that achieve business outcomes and minimize
costs, thus allowing your business to maximize its return on investment.

There are four best practice areas for cost optimization in the cloud:

- [Cost-effective resources](cost-effective-resources.md "cost-effective-resources.md")
- [Matching supply and demand](matching-supply-and-demand.md "matching-supply-and-demand.md")
- [Expenditure and usage awareness](expenditure-and-usage-awareness.md "expenditure-and-usage-awareness.md")
- [Optimizing over time](optimizing-over-time.md "optimizing-over-time.md")
  As with the other pillars, there are tradeoffs to consider. For example, do you want to
  optimize for speed to market or for cost? In some cases, it’s best to optimize for speed — going
  to market quickly, shipping new features, or simply meeting a deadline rather than investing in
  upfront cost optimization.

Design decisions are sometimes guided by haste as opposed to empirical data, as the
temptation always exists to overcompensate _just in case_
rather than spend time benchmarking for the most cost-optimal deployment.

This often leads to drastically over-provisioned and under-optimized deployments. The
following sections provide techniques and strategic guidance for the initial and ongoing cost
optimization of your deployment.

Generally, serverless architectures tend to reduce costs because some of the services, such
as AWS Lambda, don’t cost anything while they’re idle. However, following certain best practices
and making tradeoffs will help you reduce the cost of these solutions even more.
