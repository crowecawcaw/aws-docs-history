# Use advanced configuration

Advanced configuration allows you to customize your instance by setting your own parameters. To create an AWS Supply Chain instance
using an advanced configuration of preset parameters, follow these steps.

1. Select **Edit in advanced setup**.

![Interface for creating AWS Supply Chain application with options to create or edit in advanced setup.](/images/aws-supply-chain/latest/adminguide/images/create-instance.png)

The **Instance properties** page will appear.

![Instance properties form with fields for AWS region, instance name, description, and KMS key.](images/instance-properties.png) 2. Enter the following on the **Instance properties** page:

    * **Name** – Enter an instance name.
    * **Description**  – Enter a description of your AWS Supply Chain instance (e.g., production instance, test instance, etc.).
    * **AWS KMS Key (Optional)** – You can either choose to use the default AWS KMS Key (recommended) or provide your own AWS KMS Key. See [Using a custom AWS KMS key](#using-custom-keys "#using-custom-keys") for more information.
    * **Instance tags**  – You can add tags to your instance that can be used for identification. For example, you can add a tag to define the type of instance you are creating (e.g., production, test, UAT, etc.).


    ###### Note

    If you plan to use an S/4 Hana data connection, make sure that the AWS KMS key that you provided has the `aws-supply-chain-access` tag with an associated **Value** of `true`.

3. Select **Create instance**.
4. (Optional) Once your AWS Supply Chain instance is created and if you chose to use your own AWS KMS Key under **AWS KMS Key**, update your KMS policy to
   allow AWS Supply Chain to access your AWS KMS key.

###### Note

Replace `YourAccountNumber` and `YourInstanceID`
with your AWS account and AWS Supply Chain Instance ID.

```
 `{

 "Sid": "Allow AWS Supply Chain to access the AWS KMS Key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`YourAccountNumber`:role/service-role/scn-instance-role-`YourInstanceID`"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*"
}`

```

## Using a custom AWS KMS key

You can use your own AWS KMS key when creating instances. If you want to manage your own key, but do not wish to use an existing key you can create a new key.

###### Note

Using an AWS owned key is the recommended default setting for AWS Supply Chain instances.

###### Using an existing AWS KMS key

1. Choose **Customize encryption settings**.
2. Go to **Choose an AWS KMS Key**.
3. Enter your key in the provided field.
4. Select **Update**.

###### Creating an AWS KMS key

1. Select **Create**.
2. Follow the steps in [Create a KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").
3. Update the new key with the following permissions.
   - Define key administrative permissions: Leave unchecked
   - Define key usage permissions: Leave unchecked
   - Update key policy: Edit key policy and replace with:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "Enable IAM User Permissions",
    "Effect": "Allow",
    "Principal": {
    "AWS": "arn:aws:iam::`111122223333`:root"
    },
    "Action": "kms:*",
    "Resource": "*"
    },
    {
    "Sid": "Allow access through SecretManager for all principals in the account that are authorized to use SecretManager",
    "Effect": "Allow",
    "Principal": {
    "AWS": "*"
    },
    "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:CreateGrant",
    "kms:DescribeKey",
    "kms:GenerateDataKeyWithoutPlaintext",
    "kms:ReEncryptFrom",
    "kms:ReEncryptTo"
    ],
    "Resource": "*",
    "Condition": {
    "StringEquals": {
    "kms:ViaService": "secretsmanager.us-east-1.amazonaws.com",
    "kms:CallerAccount": "YourAccountNumber"
    }
    }
    },
    {
    "Sid": "Allow AWS Supply Chain to access the AWS KMS Key",
    "Effect": "Allow",
    "Principal": {
    "Service": "scn.Region.amazonaws.com"
    },
    "Action": [
    "kms:Encrypt",
    "kms:GenerateDataKeyWithoutPlaintext",
    "kms:ReEncryptFrom",
    "kms:ReEncryptTo",
    "kms:Decrypt",
    "kms:GenerateDataKey",
    "kms:DescribeKey",
    "kms:CreateGrant",
    "kms:RetireGrant"
    ],
    "Resource": "*"
    }
    ]
   }`

   ```
