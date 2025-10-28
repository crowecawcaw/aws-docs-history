# Use AMS SSP to provision AWS Glue in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Glue capabilities directly in your AMS managed account. AWS Glue is a fully managed extract, transform, and load (ETL) service that helps you to prepare and
load your data for analytics. You can create and run an ETL job with a few clicks in the AWS Management Console.
You point AWS Glue to your data stored on AWS, and AWS Glue discovers your data and stores the associated
metadata (e.g. table definition and schema) in the AWS Glue Data Catalog. Once cataloged, your data is
immediately searchable, queryable, and available for ETL actions. To learn more, see
[AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/").

## AWS Glue in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request AWS Glue to be set up in my AMS account?**

Request access to AWS Glue by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM roles to your account:

- `customer_glue_console_role`
- `customer_glue_service_role`

The preceding roles include the following attached policies:

- `customer_glue_secrets_manager_policy`
- `customer_glue_deny_policy`

After the roles are provisioned in your
account, you must onboard them in your federation solution.

For access to Crawlers, Jobs, and Development endpoints (roles needed for
specific use cases), submit an RFC with the Deployment | Advanced stack
components | Identity and Access Management (IAM) | Create entity or policy
(ct-3dpd8mdd9jn1r).

**Q: What are the restrictions to using AWS Glue in my AMS account?**

There are no restrictions. Full functionality of AWS Glue is available in your AMS account. For an interactive environment where you can author and test ETL scripts, use Notebooks on AWS Glue Studio. AWS Glue Interactive Sessions and Job Notebooks are serverless features of AWS Glue that you can use in AWS Glue and that make use of the AWS Glue service role.

**AWS Glue prior to 2.0:** AWS Glue Notebooks are a non-managed resource that
launches Amazon EC2 instances in an account. It's a best practice to launch your
own Amazon EC2 instances and install the software necessary to support a notebook
environment and development. For more information, see
[Tutorial: Set Up a Local Apache Zeppelin Notebook to Test and Debug ETL Scripts](../../../glue/latest/dg/dev-endpoint-tutorial-local-notebook.md "../../../glue/latest/dg/dev-endpoint-tutorial-local-notebook.md") and
[Using Development Endpoints for Developing Scripts](../../../glue/latest/dg/dev-endpoint.md "../../../glue/latest/dg/dev-endpoint.md").

**Q: What are the prerequisites or dependencies to using AWS Glue in my AMS account?**

AWS Glue has a dependency on Amazon S3, CloudWatch, and CloudWatch Logs.
Transitive dependencies vary based on data sources, and other AWS Glue service
features may be interacting with (example: Amazon Redshift, Amazon RDS, Athena).
