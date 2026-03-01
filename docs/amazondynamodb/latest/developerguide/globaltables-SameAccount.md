# DynamoDB same-account global table

Same-account global tables automatically replicate your DynamoDB table data across AWS Regions within a
single AWS account. Same-account global tables provide the simplest model for running multi-Region applications
because all replicas share the same account boundary, ownership, and permissions model. When you choose the AWS Regions
for your replica tables, global tables handle all replication automatically. Global tables are available in all Regions
where DynamoDB is available.

Same-account global tables provide the following benefits:

- Replicate DynamoDB table data automatically across your choice of AWS Regions to locate data closer to your users
- Enable higher application availability during regional isolation or degradation
- Use built-in conflict resolution so you can focus on your application's business logic
- When creating a same-account global table, you can choose either [Multi-Region eventual consistency (MREC)](V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes.mrec "V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes.mrec") or
  [Multi-Region strong consistency (MRSC)](V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes.mrsc "V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes.mrsc")

###### Topics

- [How DynamoDB global tables work](V2globaltables_HowItWorks.md "V2globaltables_HowItWorks.md")
- [Tutorials: Creating global tables](V2globaltables.md "V2globaltables.md")
- [DynamoDB global tables security](globaltables-security.md "globaltables-security.md")
