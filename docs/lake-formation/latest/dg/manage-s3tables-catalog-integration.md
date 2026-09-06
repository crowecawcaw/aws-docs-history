

# Changing access controls for S3 Tables integration
<a name="manage-s3tables-catalog-integration"></a>

After you have integrated Amazon S3 Tables with the AWS Glue Data Catalog, you can change how access to your catalog resources is controlled. This section how to change access control depending on your current and desired access control model. Enabling Lake Formation allows you to use fine-grained permissions such as column-level and row-level security through Lake Formation grants, and allows Lake Formation to vend temporary credentials on behalf of principals through a registered role. Changing access control from AWS Lake Formation to IAM returns access control to standard IAM policies, which may be appropriate if your workloads do not require fine-grained access and you prefer to manage permissions entirely through IAM. Both migration paths involve updating the Data Catalog defaults, adjusting resource registrations with Lake Formation, and coordinating permission grants to avoid access disruptions during the transition.

**Topics**
+ [Enable Lake Formation with S3 Tables integration with Data Catalog](change-access-iam-to-lf.md)
+ [Change access control from AWS Lake Formation to IAM](change-access-lf-to-iam.md)