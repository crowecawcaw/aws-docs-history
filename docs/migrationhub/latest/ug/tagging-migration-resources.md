AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Tagging migration resources in

AWS Application Migration Service

Migrated resources (Amazon EC2 instances or Amazon Machine Images (AMIs)) reported to Migration Hub by
migration tools like AWS Application Migration Service are automatically tagged with Application Discovery Service server IDs.

If you turn on cost allocation tagging, you can view the cost of the AWS resources that
are tagged by Migration Hub in the AWS Cost Explorer Service. Resource tagging by Migration Hub can’t
be turned off. This tagging is implemented automatically and doesn't count against your
limit of 50 tags per resource.

These resources have the
`aws:migrationhub:`source-id``tag, and the
`source-id`matches the`server.configurationId` server asset
field from Application Discovery Service. For more information, see the following topics:

- [Querying Discovered Configuration Items](../../../application-discovery/latest/userguide/discovery-api-queries.md "../../../application-discovery/latest/userguide/discovery-api-queries.md") in the
  _Application Discovery Service User Guide_.
- [Using Cost
  Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.
