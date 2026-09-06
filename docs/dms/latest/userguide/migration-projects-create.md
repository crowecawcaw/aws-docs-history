

# Creating migration projects in AWS Database Migration Service
<a name="migration-projects-create"></a>

Before you create a migration project in AWS DMS, make sure that you create the following resources:
+ Data providers that describe your source and target databases
+ Secrets with database credentials stored in AWS Secrets Manager
+ The AWS Identity and Access Management (IAM) role that provides access to Secrets Manager
+ An instance profile that includes network and security settings

**To create a migration project**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. Choose **Migration projects**. The **Migration projects** page opens.

1. Choose **Create migration project**. The following table describes the settings.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/migration-projects-create.html)

1. Choose **Create migration project**.

After AWS DMS creates your migration project, you can use this project in DMS Schema Conversion or homogeneous data migrations. To start working with your migration project, on the **Migration projects** page, choose your project from the list.