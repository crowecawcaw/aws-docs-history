# ADVREL07-BP01 Design your advertising workloads to withstand failures of individual components, such as compute instances, queues, databases, and caches

Build building resilient advertising systems by identifying
critical components, and implement fault tolerance through
cell-based architectures and distributed resources across
Availability Zones.

## Implementation guidance

Determine which components of your workload are in a critical
path to maintain operations for real-time bidding, ad serving,
and other crucial functions. Identify AWS services that provide
built-in fault tolerance mechanisms which are within your
workload's response time, RTO, and RPO targets. Use cell-based
architectures, with resources spread across multiple
availability zones, to reduce the scope of a disruptive event.
Where consistent communications are necessary, implement static
stability mechanisms to reduce the dependency on control plane
actions.

## Key AWS services

- [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/ "https://aws.amazon.com/sqs/")
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/ "https://aws.amazon.com/elasticache/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/")
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/")
- [AWS Availability Zones and Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/")
- [AWS ELB](https://aws.amazon.com/elasticloadbalancing/ "https://aws.amazon.com/elasticloadbalancing/")
- [Monitoring
  and Alerting](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")

## Resources

- [Reducing
  the Scope of Impact with Cell-Based Architecture](../reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.md "../reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.md")
- [Static
  stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/ "https://aws.amazon.com/builders-library/static-stability-using-availability-zones/")
- [Control
  planes and data planes](../../../whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.md")
