# AWS Resource Groups in AWS GovCloud (US)

In AWS, a resource is an entity that you can work with. Examples include an Amazon EC2 instance, an AWS CloudFormation stack, or an Amazon S3 bucket. If you work with multiple resources, you might find it useful to manage them as a group rather than move from one AWS service to another for each task. AWS Resource Groups make it easier to manage and automate tasks on large numbers of resources at one time. You can use resource groups to organize your AWS resources. A resource group is a collection of AWS resources that are all in the same AWS region, and that match criteria provided in a query. In Resource Groups, there are two types of queries on which you can build a group: tag-based and AWS CloudFormation stack-based queries. Resource Groups feature permissions are at the account level. In Resource Groups, the only available resource is a group. Groups have unique Amazon Resource Names (ARNs) associated with them.

## How AWS Resource Groups differs for AWS GovCloud (US)

The following list details the differences for using this service in the AWS GovCloud (US-West) Region compared to other AWS Regions:

- [Group lifecycle events](../../../ARG/latest/userguide/monitor-groups.md "../../../ARG/latest/userguide/monitor-groups.md") are not supported.

## Documentation for AWS Resource Groups

[AWS Resource Groups documentation](../../../ARG.md "../../../ARG.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Name
