# DRHCCOST02-BP01 Monitor and manage Outposts capacity and utilization effectively

Understand available edge capacity and its utilization.

**Desired outcome:** You are aware
of what capacity they have, and you scale as needed.

**Benefits of establishing this best
practice:** You can proactively make decisions to provide
the appropriate capacity and minimize unexpected cost.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Actively monitor and manage Outposts capacity and utilization.
AWS recommends
[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") to track usage and available
[Outposts
CloudWatch metrics](../../../outposts/latest/userguide/outposts-cloudwatch-metrics.md "../../../outposts/latest/userguide/outposts-cloudwatch-metrics.md") for Amazon EC2, Amazon EBS, Amazon S3,
and network resources, which helps organizations meet their
business objectives and proactively make scaling decisions.

Outposts capacity scales in fixed increments, with cost
increasing accordingly, and scaling actions can extend the
service term. You should plan for future generation Outposts, as
it is a managed service and AWS retrieves Outposts at the end of
the service period. You can
[extend
the existing term](https://aws.amazon.com/outposts/rack/faqs/#product-faqs "https://aws.amazon.com/outposts/rack/faqs/#product-faqs") or consider replacement Outposts to
adopt new services and features.

Maintaining appropriate spare capacity is crucial, as Outposts
has redundant components, and spare compute and storage capacity
ensure hardware failures do not affect workloads and minimize
sunk costs. AWS tools like
[AWS Compute Optimizer](../../../outposts/latest/userguide/outposts-optimizations.md "../../../outposts/latest/userguide/outposts-optimizations.md") can be used for rightsizing workloads
in Outposts while considering business objectives and
utilization goals.

Monitor the
[What's New with
AWS](https://aws.amazon.com/new/ "https://aws.amazon.com/new/") webpage to evaluate new services and offerings for
Outposts and Local Zones. Adopt services that can reduce the
cost profile of workloads and foster innovation.
