# Creating migration projects in AWS Database Migration Service

Before you create a migration project in AWS DMS, make sure that you create the
following resources:

- Data providers that describe your source and target databases
- Secrets with database credentials stored in AWS Secrets Manager
- The AWS Identity and Access Management (IAM) role that provides access to Secrets Manager
- An instance profile that includes network and security settings

###### To create a migration project

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration projects** page
   opens.
3. Choose **Create migration project**. The following table describes the settings.

| Option                   | Action                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                 | Enter a name for your migration project. Make sure that<br>you use a unique name for your migration project so that you<br>can easily identify it.                                                                                                                                                                                                                                                                                    |
| **Instance profile**     | Choose your instance profile to use for your migration project.                                                                                                                                                                                                                                                                                                                                                                       |
| **Source**               | Choose **Browse**, and then choose your<br>source data provider.                                                                                                                                                                                                                                                                                                                                                                      |
| **Secret ID**            | Choose the Amazon Resource Name (ARN) of your secret in Secrets Manager that stores<br>your source database credentials.                                                                                                                                                                                                                                                                                                              |
| **IAM role**             | Choose an IAM role to provide access to your source database credentials<br>in Secrets Manager.                                                                                                                                                                                                                                                                                                                                       |
| **Target**               | Choose **Browse**, and then choose your<br>target data provider.                                                                                                                                                                                                                                                                                                                                                                      |
| **Secret ID**            | Choose the ARN of your secret in Secrets Manager that stores your target database<br>credentials.                                                                                                                                                                                                                                                                                                                                     |
| **IAM role**             | Choose an IAM role to provide access to your target database credentials<br>in Secrets Manager.                                                                                                                                                                                                                                                                                                                                       |
| **Transformation rules** | (Optional) If you create a migration project for DMS Schema Conversion, then choose<br>\*_Add transformation rule_<br>• to set up transformation rules.<br>Transformation rules make it possible for you to change the object names<br>according to the rule that you specify. For more information, see [Setting up<br>transformation rules](schema-conversion-transformation-rules.md "schema-conversion-transformation-rules.md"). |

4. Choose **Create migration project**.
   After AWS DMS creates your migration project, you can use this project in DMS Schema Conversion or homogeneous data migrations.
   To start working with your migration project, on the **Migration projects** page,
   choose your project from the list.
