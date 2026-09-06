

# Setting up database authentication and resource access manually
<a name="limitless-load.manual"></a>

The manual process for setting up database authentication and resource access has the following steps:

1. [Creating the customer-managed AWS KMS key](#limitless-load.auth.create-kms)

1. [Adding the IAM role permission policies](#limitless-load.auth.iam-policy)

1. [Creating the database secrets](#limitless-load.auth.secrets)

1. [Creating the IAM role](#limitless-load.auth.iam-role)

1. [Updating the customer-managed AWS KMS key](#limitless-load.auth.update-kms)

This process is optional, and performs the same tasks as in [Setting up database authentication and resource access using a script](limitless-load.script.md). We recommend using the script.

## Creating the customer-managed AWS KMS key
<a name="limitless-load.auth.create-kms"></a>

Follow the procedures in [Creating symmetric encryption keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) to create a customer-managed KMS key. You can also use an existing key if it meets these requirements.

**To create a customer-managed KMS key**

1. Sign in to the AWS Management Console and open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. Navigate to the **Customer managed keys** page.

1. Choose **Create key**.

1. On the **Configure key** page:

   1. For **Key type**, select **Symmetric**.

   1. For **Key usage**, select **Encrypt and decrypt**.

   1. Choose **Next**.

1. On the **Add labels** page, enter an **Alias** such as **limitless**, then choose **Next**.

1. On the **Define key administrative permissions** page, make sure that the **Allow key administrators to delete this key** check box is selected, then choose **Next**.

1. On the **Define key usage permissions** page, choose **Next**.

1. On the **Review** page, choose **Finish**.

   You update the key policy later.

Record the Amazon Resource Names (ARN) of the KMS key to use in [Adding the IAM role permission policies](#limitless-load.auth.iam-policy).

For information on using the AWS CLI to create the customer-managed KMS key, see [create-key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-key.html) and [create-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-alias.html).

## Creating the database secrets
<a name="limitless-load.auth.secrets"></a>

To allow the data loading utility to access the source and destination database tables, you create two secrets in AWS Secrets Manager: one for the source database and one for the destination database. These secrets store the usernames and passwords for accessing the source and destination databases.

Follow the procedures in [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) to create the key-value pair secrets.

**To create the database secrets**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page:

   1. For **Secret type**, select **Other type of secret**.

   1. For **Key/value pairs**, choose the **Plaintext** tab.

   1. Enter the following JSON code, where `{{sourcedbreader}}` and `{{sourcedbpassword}}` are the credentials for the source database user from [Create the source database credentials](limitless-load.utility.md#limitless-load.users.source).

      ```
      {
          "username":"{{sourcedbreader}}",
          "password":"{{sourcedbpassword}}"
      }
      ```

   1. For **Encryption key**, choose the KMS key that you created in [Creating the customer-managed AWS KMS key](#limitless-load.auth.create-kms), for example `limitless`.

   1. Choose **Next**.

1. On the **Configure secret** page, enter a **Secret name**, such as **source\_DB\_secret**, then choose **Next**.

1. On the **Configure rotation - *optional*** page, choose **Next**.

1. On the **Review** page, choose **Store**.

1. Repeat the procedure for the destination database secret:

   1. Enter the following JSON code, where `{{destinationdbwriter}}` and `{{destinationdbpassword}}` are the credentials for the destination database user from [Create the destination database credentials](limitless-load.utility.md#limitless-load.users.destination).

      ```
      {
          "username":"{{destinationdbwriter}}",
          "password":"{{destinationdbpassword}}"
      }
      ```

   1. Enter a **Secret name**, such as **destination\_DB\_secret**.

Record the ARNs of the secrets to use in [Adding the IAM role permission policies](#limitless-load.auth.iam-policy).

## Creating the IAM role
<a name="limitless-load.auth.iam-role"></a>

Data loading requires you to provide access to AWS resources. To provide access, you create the `aurora-data-loader` IAM role by following the procedures in [Creating a role to delegate permissions to an IAM user.](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html)

**To create the IAM role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Navigate to the **Roles** page.

1. Choose **Create role**.

1. On the **Select trusted entity** page:

   1. For **Trusted entity type**, select **Custom trust policy**.

   1. Enter the following JSON code for the custom trust policy:

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "Service": [
                          "rds.amazonaws.com"
                      ]
                  },
                  "Action": "sts:AssumeRole"
              }
          ]
      }
      ```

------

   1. Choose **Next**.

1. On the **Add permissions** page, choose **Next**.

1. On the **Name, review, and create** page:

   1. For **Role name**, enter **aurora-data-loader** or another name that you prefer.

   1. Choose **Add tag**, and enter the following tag:
      + **Key**: **assumer**
      + **Value**: **aurora\_limitless\_table\_data\_load**
**Important**  
The Aurora PostgreSQL Limitless Database can only assume an IAM role that has this tag.

   1. Choose **Create role**.

## Updating the customer-managed AWS KMS key
<a name="limitless-load.auth.update-kms"></a>

Follow the procedures in [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html) to add the IAM role `aurora-data-loader` to the default key policy.

**To add the IAM role to the key policy**

1. Sign in to the AWS Management Console and open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. Navigate to the **Customer managed keys** page.

1. Choose the KMS key that you created in [Creating the customer-managed AWS KMS key](#limitless-load.auth.create-kms), for example `limitless`.

1. On the **Key policy** tab, for **Key users**, choose **Add**.

1. In the **Add key users** window, select the name of the IAM role that you created in [Creating the IAM role](#limitless-load.auth.iam-role), for example **aurora-data-loader**.

1. Choose **Add**.

## Adding the IAM role permission policies
<a name="limitless-load.auth.iam-policy"></a>

You must add permission policies to the IAM role that you created. This allows the Aurora PostgreSQL Limitless Database data loading utility to access related AWS resources for building network connections and retrieving the source and destination DB credential secrets.

For more information, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html#roles-modify_gen-policy).

**To add the permission policies**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Navigate to the **Roles** page.

1. Choose the IAM role that you created in [Creating the IAM role](#limitless-load.auth.iam-role), for example **aurora-data-loader**.

1. On the **Permissions** tab, for **Permissions policies** choose **Add permissions**, then **Create inline policy**.

1. On the **Specify permissions** page, choose the **JSON** editor.

1. Copy and paste the following template into the JSON editor, replacing the placeholders with the ARNs for your database secrets and KMS key.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "Ec2Permission",
               "Effect": "Allow",
               "Action": [
                   "ec2:DescribeNetworkInterfaces",
                   "ec2:CreateNetworkInterface",
                   "ec2:DeleteNetworkInterface",
                   "ec2:CreateNetworkInterfacePermission",
                   "ec2:DeleteNetworkInterfacePermission",
                   "ec2:DescribeNetworkInterfacePermissions",
                   "ec2:ModifyNetworkInterfaceAttribute",
                   "ec2:DescribeNetworkInterfaceAttribute",
                   "ec2:DescribeAvailabilityZones",
                   "ec2:DescribeRegions",
                   "ec2:DescribeVpcs",
                   "ec2:DescribeSubnets",
                   "ec2:DescribeSecurityGroups",
                   "ec2:DescribeNetworkAcls"
               ],
               "Resource": "*"
           },
           {
               "Sid": "SecretsManagerPermissions",
               "Effect": "Allow",
               "Action": [
                   "secretsmanager:GetSecretValue",
                   "secretsmanager:DescribeSecret"
               ],
               "Resource": [
                   "arn:aws:secretsmanager:us-east-1:{{123456789012}}:secret:{{source_DB_secret-ABC123}}",
                   "arn:aws:secretsmanager:us-east-1:{{123456789012}}:secret:{{destination_DB_secret-456DEF}}"
               ]
           },        {
               "Sid": "KmsPermissions",
               "Effect": "Allow",
               "Action": [
                   "kms:Decrypt",
                   "kms:DescribeKey",
                   "kms:GenerateDataKey"
               ],
               "Resource": "arn:aws:kms:us-east-1:{{123456789012}}:key/{{aa11bb22-####-####-####-fedcba123456}}"
           },
           {
               "Sid": "RdsPermissions",
               "Effect": "Allow",
               "Action": [
                   "rds:DescribeDBClusters",
                   "rds:DescribeDBInstances"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Check for errors and correct them.

1. Choose **Next**.

1. On the **Review and create** page, enter a **Policy name** such as **data\_loading\_policy**, then choose **Create policy**.