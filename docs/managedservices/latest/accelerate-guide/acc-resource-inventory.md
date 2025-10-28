# Resource inventory for Accelerate

All the resources that AMS Accelerate deploys to your AWS account or accounts are listed in
the [`resource_inventory.zip`](samples/resource_inventory3.md "samples/resource_inventory3.md") file resource_inventory.xlsx spreadsheet (compressed).

###### Note

In the _Resource Name_ column, the prefix _CFN:_
indicates a CloudFormation logical ID instead of a resource name. These are shown for unnamed
resources, for example, for S3 bucket policies.

AMS deploys a set of services as described in the [Service description](acc-sd.md "acc-sd.md"). The cost of deploying them is low when deployed to an empty account,
but the cost increases as utilization grows. For example, logs are created and config rules are invoked as resources change.

When multiple changes are made to the config rules, multiple config compliance invocation
can be triggered, leading to higher costs. The same possibility applies for Amazon CloudWatch used for
monitoring instances—the more granular your monitoring, the higher the cost of the service.
AWS Backup is another example. If you have multiple backups stored, or if you have higher retention
periods, you are using more storage and the cost is higher.

These numbers are hard to predict. During your monthly business review with your cloud
service delivery manager (CSDM), keep track of the changes and work to identify areas of
opportunity for cost reduction.
