# ADVREL05-BP02 Create disaster recovery (DR) runbooks, and regularly test documented backup and restoration processes

Processes for backup, restoration, and failover of data should be
documented and regularly tested to validate efficacy and
understanding.

## Implementation guidance

Advertising workloads are designed for low latency when
accessing information. An unsuccessful or slow data restoration
could result in negative impact to the workload. To mitigate the
impact from data unavailability during a disaster, implement
data backup mechanisms which can quickly make necessary data
available. By documenting processes, incident response teams can
address impactful events, while validation ensures that the
processes will work when needed, and that team members are
comfortable, and confident, in performing disaster response
activities quickly.

## Key AWS services

- [AWS Elastic Disaster Recovery (DRS)](https://aws.amazon.com/disaster-recovery/ "https://aws.amazon.com/disaster-recovery/") is a
  service that can help design a DR solution, map applications
  and networks, and build and test a DR runbook
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") can be used to continuously monitor
  and record resource configurations
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") can detect drift in stacks
  that have been deployed

## Resources

- [Disaster
  recovery options in the cloud](../../../whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.md "../../../whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.md")
- [Orchestrate
  disaster recovery automation using Amazon Application Recovery Controller (ARC) and AWS Step Functions](https://aws.amazon.com/blogs/networking-and-content-delivery/orchestrate-disaster-recovery-automation-using-amazon-route-53-arc-and-aws-step-functions/ "https://aws.amazon.com/blogs/networking-and-content-delivery/orchestrate-disaster-recovery-automation-using-amazon-route-53-arc-and-aws-step-functions/")
- [Testing
  disaster recovery](../../../whitepapers/latest/disaster-recovery-workloads-on-aws/testing-disaster-recovery.md "../../../whitepapers/latest/disaster-recovery-workloads-on-aws/testing-disaster-recovery.md")
