# ADVSUS02-BP01 Break down system components to determine which are business critical and compare the trade-offs

When aligning SLAs with sustainability goals for advertising
workloads, break down system components to identify
business-critical elements, and evaluate trade-offs to balance
SLAs with environmental objectives while minimizing waste.

## Implementation guidance

- Categorize workloads by business impact, customer impact,
  and latency, monitor performance, and set SLA requirements
  accordingly to optimize resource allocation.
- For batch workloads like privacy-enhanced data
  collaboration, consider scheduling them to run during
  periods when the carbon footprint is lower, such as time of
  the day or week when more renewable energy is available or
  when demand is lower.
- For time-sensitive and business-critical workloads like
  real-time bidding, prioritize meeting SLA requirements, even
  if it means running during peak demand periods with a higher
  carbon footprint.

## Key AWS services

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/") (Automatically scales resources)
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/") (Recommends optimal compute
  resources)
- [AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/ "https://aws.amazon.com/solutions/implementations/instance-scheduler/") (Schedules starting/stopping
  instances)
- [AWS Spot
  Instances](https://aws.amazon.com/ec2/spot/ "https://aws.amazon.com/ec2/spot/") (Discounted spare compute capacity)
- [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/") (Energy-efficient ARM processors)
