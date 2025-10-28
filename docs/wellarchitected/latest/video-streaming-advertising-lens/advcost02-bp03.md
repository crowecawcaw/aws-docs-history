# ADVCOST02-BP03 Use provisioned resource allocation for campaigns with predictable capacity requirements, and use dynamic allocation for unexpected capacity needs

Provisioned capacity can provide the lowest cost per hour.
However, for unpredictable workloads dynamic allocation can
provide a lower overall cost of ownership.

## Implementation guidance

Provisioned capacity and on-demand capacity are two different
pricing models offered by various AWS services, including
[Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/ "https://aws.amazon.com/kinesis/data-streams/"),
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/"),
[AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/"), and
[Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/"). The differences between the two models are the
following:

- **Provisioned capacity:**
  With provisioned capacity, you reserve and pay for a
  specific amount of capacity in advance, regardless of
  whether you use it or not.
  - This model is suitable for workloads with predictable
    and consistent traffic patterns or when you have a
    baseline capacity requirement.
  - By provisioning capacity, you get dedicated resources
    and can achieve better performance and lower costs
    compared to on-demand capacity for sustained workloads.
  - Examples: DynamoDB provisioned throughput, Kinesis Data
    Streams provisioned capacity, Lambda provisioned
    concurrency, and Athena workgroup capacity.

- **On-demand capacity:** With
  on-demand capacity, you pay for the resources you consume on
  a per-use basis without any upfront commitment or
  reservation.
  - This model is suitable for workloads with unpredictable
    or bursty traffic patterns, where you don't have a
    consistent baseline requirement.
  - On-demand capacity provides flexibility and scalability,
    as you only pay for what you use, but it can be more
    expensive for sustained workloads compared to
    provisioned capacity.
  - Examples: DynamoDB on-demand capacity, Kinesis Data
    Streams on-demand capacity, Lambda on-demand
    concurrency, and Athena on-demand capacity.

- **[Serverless
  capacity](https://aws.amazon.com/serverless/ "https://aws.amazon.com/serverless/"):** AWS offers technologies for
  running code, managing data, and integrating applications,
  all without managing servers.
  - Serverless technologies feature automatic scaling,
    built-in high availability, and a pay-for-use billing
    model to increase agility and optimize costs.
  - These technologies also eliminate infrastructure
    management tasks like capacity provisioning and
    patching, so you can focus on writing code that serves
    your customers.
  - Examples: Amazon Aurora, Amazon Redshift, Amazon Neptune, Amazon OpenSearch Service, and Amazon
    Elasticache.

The choice between provisioned, on-demand, and serverless
capacity depends on your workload characteristics, cost
considerations, and performance requirements. Some general
guidelines for making this choice are the following:

- If you have a predictable and consistent workload with a
  known baseline capacity requirement, provisioned capacity
  can provide better performance and cost savings for
  sustained usage.
- If your workload is highly variable, unpredictable, or
  bursty, on-demand or serverless capacity can offer more
  flexibility and scalability, but it may be more expensive
  for sustained usage.
- For short-term or temporary workloads, on-demand or
  serverless capacity may be more cost-effective because you
  don't have to pay for unused provisioned capacity.
- For long-running or mission-critical workloads with
  consistent traffic, provisioned capacity can provide better
  performance and cost savings.

Analyze your workload patterns, performance requirements, and
cost considerations to determine the most suitable capacity
model for your use case. Additionally, many AWS services offer
auto scaling and capacity management features to help optimize
resource allocation and costs based on actual usage patterns.

## Resources

- [Choose
  the data stream capacity mode](../../../streams/latest/dev/how-do-i-size-a-stream.md "../../../streams/latest/dev/how-do-i-size-a-stream.md")
- [Pricing
  for Provisioned Capacity](https://aws.amazon.com/dynamodb/pricing/provisioned/ "https://aws.amazon.com/dynamodb/pricing/provisioned/")
- [Configuring
  provisioned concurrency for a function](../../../lambda/latest/dg/provisioned-concurrency.md "../../../lambda/latest/dg/provisioned-concurrency.md")
- [Serverless
  on AWS](https://aws.amazon.com/serverless/ "https://aws.amazon.com/serverless/")
