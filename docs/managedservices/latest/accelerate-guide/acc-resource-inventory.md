# Resource inventory for Accelerate

All the resources that deploys to your AWS account or accounts are listed in the [`resource_inventory.zip`](samples/resource_inventory3.zip.md "samples/resource_inventory3.zip.md") file (Excel spreadsheet).

###### Note

In the _Resource Name_ column, the prefix _CFN:_
indicates a CloudFormation logical ID instead of a resource name. These are shown for unnamed
resources, for example, for S3 bucket policies.

AMS deploys a set of services as described in the [Service description](acc-sd.md "acc-sd.md"). Deploying them to an empty account costs little,
but the cost increases as utilization grows. For example, the system creates logs and invokes config rules as resources change.

When multiple changes occur to the config rules, multiple config compliance invocations
can be triggered, leading to higher costs. The same possibility applies for Amazon CloudWatch used for
monitoring instances—the more granular your monitoring, the higher the cost of the service.
AWS Backup is another example. If you have multiple backups stored, or if you have higher retention
periods, you are using more storage and the cost is higher.

These numbers are hard to predict. During your monthly business review with your cloud
service delivery manager (CSDM), keep track of the changes and work to identify areas of
opportunity for cost reduction.
