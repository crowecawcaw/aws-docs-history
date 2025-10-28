# Use AMS SSP to provision Amazon DynamoDB in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon DynamoDB (DynamoDB) capabilities directly in your AMS managed account. Amazon DynamoDB is a key value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multi-region, multi-active database with built-in security, backup and restore,
and in-memory caching for internet scale applications.
To learn more, see [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/").

Amazon DynamoDB Accelerator (DAX) is a write-through caching service that is designed to simplify the process of adding a cache to
DynamoDB tables. DAX is intended for applications that require high-performance reads.

## DynamoDB in AWS Managed Services FAQ

**Q: How do I request access to DynamoDB and DAX in my AMS account?**

Request access to DynamoDB and DAX by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM roles and policies to your account:

- DynamoDB role name: `customer_dynamodb_role`

DAX service role name: `customer_dax_service_role`

- DynamoDB policy name: `customer_dynamodb_policy`

DAX service policy: `customer_dax_service_policy`

Once provisioned in your account, you must onboard the `customer_dynamodb_role` in your federation solution.

**Q: What are the restrictions to using DynamoDB in my AMS account?**

All DynamoDB functionality are supported including DynamoDB Accelerator (DAX).

When creating alarms for any given table, the alarm name must be prefixed with "customer\*"; for example,
`customer-employee-table-high-put-latency`.

When creating an Amazon SNS topic for DynamoDB, it must be named: `dynamodb`.

To delete the Amazon SNS topic created by DynamoDB, submit a Management | Other |
Other | Update change type RFC.

**Q: What are the prerequisites or dependencies to using DynamoDB in my AMS account?**

There are no prerequisites or dependencies to use DynamoDB in your AMS account.
