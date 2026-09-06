

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Tagging migration resources in AWS Application Migration Service
<a name="tagging-migration-resources"></a>

Migrated resources (Amazon EC2 instances or Amazon Machine Images (AMIs)) reported to Migration Hub by migration tools like AWS Application Migration Service are automatically tagged with Application Discovery Service server IDs. 

If you turn on cost allocation tagging, you can view the cost of the AWS resources that are tagged by Migration Hub in the AWS Cost Explorer Service. Resource tagging by Migration Hub can’t be turned off. This tagging is implemented automatically and doesn't count against your limit of 50 tags per resource.

These resources have the `aws:migrationhub:{{source-id}}` tag, and the `source-id` matches the `server.configurationId` server asset field from Application Discovery Service. For more information, see the following topics:
+ [Querying Discovered Configuration Items](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html) in the *Application Discovery Service User Guide*.
+ [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.