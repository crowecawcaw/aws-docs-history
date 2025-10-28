# Use AMS SSP to provision AWS Lake Formation in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Lake Formation capabilities directly in your AMS managed account. AWS Lake Formation is a service that makes it easy to set up a secure data lake in days.
A data lake is a centralized, curated, and secured repository that stores all your
data, both in its original form and prepared for analysis. A data lake enables
you to break down data silos and combine different types of analytics to gain
insights and guide better business decisions.

Creating a data lake with Lake Formation is as simple as defining data sources and what
data access and security policies you want to apply. Lake Formation then helps you collect and
catalog data from databases and object storage, move the data into your
new Amazon S3 data lake, clean and classify your data using machine learning
algorithms, and secure access to your sensitive data. Your users can access a
centralized data catalog (for details, see
[AWS Glue FAQ](https://aws.amazon.com/glue/faqs/#AWS_Glue_Data_Catalog/ "https://aws.amazon.com/glue/faqs/#AWS_Glue_Data_Catalog/"))
that describes available data sets and their appropriate usage. Your users then
leverage these data sets with their choice of analytics and machine learning services,
like [Amazon Redshift](https://aws.amazon.com/redshift/ "https://aws.amazon.com/redshift/"),
[Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/"), and (in beta)
[Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/") for Apache Spark. Lake Formation builds on the capabilities available in
[AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/").

To learn more, see [AWS Lake Formation](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/").

## Lake Formation in AWS Managed Services FAQ

**Q: How do I request access to AWS Lake Formation in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account: `customer_lakeformation_data_analyst_role`. After it's provisioned in your account, you must onboard the roles in your federation solution.

Additionally, the following two roles are optional:

- `customer_lakeformation_admin_role`
- `customer_lakeformation_workflow_role`

For admin permissions, you can choose to onboard the role `customer_lakeformation_admin_role` as part of the same SSPS change type (ct-3qe6io8t6jtny).

If you want to create Blueprints in the AWS Lake Formation Console, you need to submit a Management | Other | Other RFC (ct-1e1xtak34nx76) to deploy the `customer_lakeformation_workflow_role`. In the RFC, you must provide the S3 bucket name if the bucket is a source when Blueprints are created. S3 bucket is applicable if the Blueprint type is AWS CloudTrail, Classic Load Balancer Logs or Application Load Balancer Logs.

**Q: What are the restrictions to using AWS Lake Formation in my AMS account?**

Full functionality of Lake Formation is available in AMS.

**Q: What are the prerequisites or dependencies to using AWS Lake Formation in my AMS account?**

Lake Formation integrates with the AWS Glue service, therefore AWS Glue users can access only the
databases and tables on which they have Lake Formation permissions. Additionally
AWS Athena and Amazon Redshift users can only query the AWS Glue databases and tables on which
they have Lake Formation permissions.
