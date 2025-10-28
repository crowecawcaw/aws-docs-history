# ADVREL01-BP03 Architect for variable demand

Architect to elastically launch resources for variable demand,
including the most challenging peak events, like flash crowds or
thundering herds.

## Implementation guidance

Depending on the advertising channel, such as retail stores,
video streaming, or audio apps, loads will peak at different
times in different locations. Know your historical load
statistics, and adjust load testing scenarios based on
historical peaks to determine how the workload performs in
unexpected situations and peak demand. With
[Amazon CloudWatch Real-User Monitoring (RUM)](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md"), you can collect
and view client-side data about your web application performance
from actual user sessions in near real-time.
[CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
Synthetics are configurable scripts that run on a schedule to
monitor your endpoints and APIs.

If this a new workload without historical data, load testing is
part of this process. Until enough historical data is obtained,
use [Auto
Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/") groups and Elastic Load Balancers (ELB) to meet
compute demands and send requests to healthy hosts. Networking
demands must also be considered and capacity planned to prevent
congestion. For critical workloads, consider private AWS Direct Connect networking to connect to partners or on-premise
infrastructure to provide sufficient capacity and more stable
latency.

## Resources

- [Predictive
  scaling for Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.md")
- [Guidance
  for AdTech Private Network on AWS](https://aws.amazon.com/solutions/guidance/adtech-private-network-on-aws/ "https://aws.amazon.com/solutions/guidance/adtech-private-network-on-aws/")
