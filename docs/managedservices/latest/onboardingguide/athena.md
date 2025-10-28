# Use AMS SSP to provision Amazon Athena in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Athena (Athena)
capabilities directly in your AMS managed account. Athena is an interactive query
service that helps you to analyze data in Amazon S3 using standard SQL. Athena is serverless,
so there is no infrastructure to manage, and you pay only for the queries that you run.
You point to your data in Amazon S3, define the schema, and start querying using standard
SQL. Most results are delivered within seconds. With Athena, there’s no need for complex
extract-transform-load (ETL) jobs to prepare your data for analysis. This makes it
straight-forward for anyone with SQL skills to quickly analyze large-scale datasets. To
learn more, see [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/").

## FAQ: Athena in AMS

**Q: How do I request access to Amazon Athena in my AMS account?**

Request access to Athena by submitting an RFC with the Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account:
`customer_athena_console_role`. After it's provisioned in
your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon Athena in my AMS account?**

There are no restrictions. Full functionality of Amazon Athena is available in your AMS account.

**Q: What are the prerequisites or dependencies to using Amazon Athena in my AMS account?**

Athena has a major dependency on the AWS Glue service, as it uses the data
catalog/metastore created with AWS Glue. Therefore, AWS Glue permissions are included in the successful Athena RFC.

The role `customer_athena_console_role` has a prerequisite for an Amazon S3 bucket. To create a new bucket, use the automated CT `ct-1a68ck03fn98r` (Deployment | Advanced stack components | S3 storage | Create). When you use this automated CT to create an S3 bucket for Athena, the bucket name must begin with prefix `athena-query-results-*`.
