# Global tables - multi-active, multi-Region

replication

_Amazon DynamoDB global tables_ is a fully managed,
multi-Region, and multi-active database feature that provides easy to use data replication
and fast local read and write performance for globally scaled applications.

Global tables automatically replicate your DynamoDB table data across AWS Regions without
requiring you to build and maintain your own replication solution. When you choose the
AWS Regions for your table replicas, global tables handle all replication automatically.
Global tables are available in all Regions where DynamoDB is available.

Global tables provide the following benefits:

- Replicate DynamoDB table data automatically across your choice of AWS Regions to
  locate data closer to your users
- Enable higher application availability during regional isolation or
  degradation
- Eliminate update conflict resolution so you can focus on your application's
  business logic
  Global tables are ideal for applications requiring business continuity and high
  availability through multi-Region deployment. Any global table replica can serve reads and
  writes. Applications can achieve high resilience with a low or zero Recovery Point Objective
  (RPO) by shifting traffic to a different Region if application processing is interrupted in
  a Region.

You can configure a global table using the AWS Management Console. Global tables use
existing DynamoDB APIs to read and write data to your tables, so no application changes are
required. You pay only for the resources you provision or use, with no upfront costs or
commitments. To get started with global tables, see [Tutorials: Creating global tables](V2globaltables.md "V2globaltables.md").

###### Topics

- [How DynamoDB global tables work](V2globaltables_HowItWorks.md "V2globaltables_HowItWorks.md")
- [Tutorials: Creating global tables](V2globaltables.md "V2globaltables.md")
- [DynamoDB global tables security](globaltables-security.md "globaltables-security.md")
- [Understanding Amazon DynamoDB billing for global
  tables](global-tables-billing.md "global-tables-billing.md")
- [DynamoDB global tables versions](V2globaltables_versions.md "V2globaltables_versions.md")
- [Best practices for global tables](globaltables-bestpractices.md "globaltables-bestpractices.md")
