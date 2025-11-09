# Evolve

| SaaS OPS 2: How are you capturing and surfacing metric data that can be used<br>to analyze the usage and consumption trends of individual tenants? |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                    |

To continually evolve your SaaS operations experience, you’ll
need to have access to a rich collection of operational data
that can be used to analyze your multi-tenant SaaS
environment. This often means instrumenting and publishing a
much richer collection of tenant metrics from your application
that can accurately capture the activity and consumption
patterns of the tenants that are exercising your environment.

SaaS metrics go beyond the fundamental of infrastructure
consumption (CPU, memory, etc.), identifying specific
operational usage patterns that are fundamental to
understanding the operation of multi-tenant loads in your
environment. Analysis of this data will allow SaaS
organizations to assess trends that are happening across their
system and identify opportunities to introduce policies or
changes to the underlying architecture that will continually
improve the reliability, scalability, cost efficiency, and
overall agility of a SaaS offering.

There are two distinct elements of capturing and surfacing
metric data. First, your application must publish the metric
data that can provide useful operational insights into your
SaaS environment. You’ll need to identify key points in your
application where you’ll want to capture and publish these
metrics.

The other piece of the puzzle here is the ingestion,
aggregation, and surfacing of this data. There is a wide
spectrum of tools that you can choose here from AWS or one of
the AWS Partner Network (APN) Partners. Ultimately, the
ingestion component of this becomes more of a data warehouse
and business intelligence question. The SaaS architecture
scenarios listed previously in this document includes a Tenant
Insights scenario. This scenario outlines an architecture for
ingesting metric data. That architecture represents one of the
patterns you can apply to address this need.

While our focus here is on the operational view of these
tenant metrics, you can imagine that these metrics have usage
in multiple contexts across a SaaS business. The operational
requirement is for your architecture to ensure that the
organization is actively collecting and analyzing tenant
activity and consumption trends to identify opportunities to
evolve your SaaS system. This fits with the broader theme of
building the foundational tooling that can be used to assess
the continually shifting mix of tenants and tenant workloads.
