

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



<table>
<thead>
  <tr><th>Option</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><b>Name</b></td><td>Enter a name for your migration project. Make sure that you use a unique name for your migration project so that you can easily identify it.</td></tr>
  <tr><td><b>Instance profile</b></td><td>Choose your instance profile to use for your migration project.</td></tr>
  <tr><td><b>Source</b></td><td>Choose <b>Browse</b>, and then choose your source data provider.</td></tr>
  <tr><td><b>Secret ID</b></td><td>Choose the Amazon Resource Name (ARN) of your secret in Secrets Manager that stores your source database credentials.</td></tr>
  <tr><td><b>IAM role</b></td><td>Choose an IAM role to provide access to your source database credentials in Secrets Manager.</td></tr>
  <tr><td><b>Target</b></td><td>Choose <b>Browse</b>, and then choose your target data provider.</td></tr>
  <tr><td><b>Secret ID</b></td><td>Choose the ARN of your secret in Secrets Manager that stores your target database credentials.</td></tr>
  <tr><td><b>IAM role</b></td><td>Choose an IAM role to provide access to your target database credentials in Secrets Manager.</td></tr>
  <tr><td><b>Transformation rules</b></td><td>(Optional) If you create a migration project for DMS Schema Conversion, then choose <b>Add transformation rule</b> to set up transformation rules. Transformation rules make it possible for you to change the object names according to the rule that you specify. For more information, see <a href="sc-transformation-rules.md">Transformation rules</a>. </td></tr>
</tbody>
</table>


1. Choose **Create migration project**.

After AWS DMS creates your migration project, you can use this project in DMS Schema Conversion or homogeneous data migrations. To start working with your migration project, on the **Migration projects** page, choose your project from the list.