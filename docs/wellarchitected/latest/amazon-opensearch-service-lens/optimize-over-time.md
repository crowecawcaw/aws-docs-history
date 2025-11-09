# Optimize over time

You can optimize cost over time by reviewing new instance types and
implementing them in your workload. As AWS releases new instances
and features, it is a best practice to review your existing
architectural decisions to verify that they remain cost effective.
As your requirements change, be aggressive in decommissioning
resources, components, and workloads that you no longer require.

Consider the following best practices to help you optimize over
time. While optimizing your workloads over time and improving your
CFM culture in your organization, evaluate the cost of effort for
operations in the cloud, review your time-consuming cloud
operations, and automate them to reduce human efforts and cost by
adopting related AWS services, third-party products, or custom tools
(like AWS CLI or AWS SDKs)

| AOSCOST04: How can regular monitoring and<br>tracking of costs help achieving cost optimization? |
| ------------------------------------------------------------------------------------------------ |
|                                                                                                  |

Actively monitoring the usage and cost of Amazon OpenSearch Service
is crucial for cost optimization because it allows you to identify
inefficiencies, optimize resource allocation, budget management and
plan for growth. You can use service metrics to monitor actively the
performance metrics and costs of OpenSearch Service.

| AOSCOST05: How do estimate your OpenSearch Service cost? |
| -------------------------------------------------------- |
|                                                          |

It is important to estimate costs for the services you use. We
recommend using AWS Pricing Calculator to estimate costs.

###### Best practices

- [AOSCOST04-BP01 Apply cost allocation tags to your OpenSearch
  resources for detailed cost tracking and analysis](aoscost04-bp01.md "aoscost04-bp01.md")
- [AOSCOST05-BP01 Assess the pricing for instances and storage in
  Amazon OpenSearch Service](aoscost05-bp01.md "aoscost05-bp01.md")
- [AOSCOST05-BP02 Examine the costs associated with Amazon S3
  storage for manually creating snapshots of your OpenSearch Service
  domain](aoscost05-bp02.md "aoscost05-bp02.md")
