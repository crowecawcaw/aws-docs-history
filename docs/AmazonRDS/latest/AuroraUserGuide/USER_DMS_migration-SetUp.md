

# Setting up data migration for EC2 database
<a name="USER_DMS_migration-SetUp"></a>

To begin migrating data from your EC2 source database, you must create an equivalent Aurora database. For instructions on creating your database, see [Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md) .

After creating your target database, use the following steps to set up the data migration:

**Set up data migration project**

1. Select the target database on the **Databases** page in the RDS console.

1. Choose the **Actions** dropdown and select the **Migrate data from EC2 database** option. To see the supported target databases, see [Limitations](USER_DMS_migration.md#USER_DMS_migration-Limitations).

1. Under the **Select source EC2 database** section:

   1. Check the **Engine type** and make sure it is the same as your source database.

      Also, check if the engine versions are compatible.

   1. For **EC2 instance**, choose the EC2 instance where your source database resides.

   1. For **Port**, enter the port on which your source database allows traffic.

   1. For **Secret**, choose **Create and use a new secret** if you don't have an existing secret. Enter the **Username** and **Password** for your source database. Also choose the KMS key with which to encrypt your secret.

      If you have an existing secret, select **Use an existing secret** and then choose secret from the dropdown.

   1. For **IAM role for secret**, if you have an existing IAM role, select **Use an existing IAM role** and choose an IAM role from the dropdown that can access the secret ID from the previous step.

      If you don't have existing IAM role, choose **Create and use new IAM role**. Enter the new name for your role for **IAM role name. You can see the permissions associated with this role in the link below.**

1. Under the **View target RDS database** section:

   1. Confirm the settings of your target database in the section.

   1. For **Secret**, choose **Create and use a new secret** if you don't have an existing secret that holds your target database credentials.

      If you have an existing secret, select the secret from the dropdown.

   1. For **IAM role for secret**, select an IAM role that can access the secret from the previous step. You can also create a new IAM role if you don't have existing IAM role.

      If the dropdown doesn't populate the IAM roles, specify the **IAM role ARN** in the format `arn:aws:iam:{{account_id}}:role/{{roleName}}`.

1. Under the **Configure data migration** section:

   1. Select the type of data migration by selecting between **Full load**, **Full load and change data capture (CDC)**, or **Change data capture (CDC)**. For more information about these options, see [Overview](USER_DMS_migration.md#USER_DMS_migration-overview).

      You can't modify the migration type afer the migration starts. 

   1. For **IAM role for data migration**, if you have an existing IAM role, select **Use an existing IAM role** and choose an IAM role from the dropdown that grants DMS the permissions to create the resources required for the migration. If you don't have existing IAM role, choose **Create and use new IAM role**.
**Note**  
If role manager is enabled in your account, Amazon RDS attaches the roles for you, and the role options described here (for source secret, target secret, and data migration) are replaced by a **Customize** option. To use a different role, choose **Customize**. For more information, see [IAM role creation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*.

1. Confirm that the **View migration settings** tab shows the required settings for your data migration to be set up successfully.

1. Select **Migrate** to complete the migration set up.

After completing these steps, you can see the resources being set up for the data migration by choosing **View details** in the progress banner in the console. Once the required resources are set up, the migration automatically starts. If you create 

To migrate multiple databases into the target database, start this process again with details about the new EC2 database.