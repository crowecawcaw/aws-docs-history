# Securing storage location credentials with Secrets Manager

###### Note

Secrets Manager integration is available for object storage and Microsoft Azure Blob Storage.

DataSync uses [locations](how-datasync-transfer-works.md#sync-locations "how-datasync-transfer-works.md#sync-locations") to access your storage resources located on premises, in other
clouds, or in AWS. Some location types require you to provide credentials, such as an
access key and secret key or a user name and password, to authenticate with your storage
system. When you create a DataSync location that requires credentials for authentication, you
can use AWS Secrets Manager (Secrets Manager) to store the secret for your credentials. The following options are
available:

- Store the secret in Secrets Manager using a service-managed secret encrypted with a
  default key.
- Store the secret in Secrets Manager using a service-managed secret encrypted with an
  AWS KMS key that you manage.
- Store the secret in Secrets Manager using a secret and key that you create and manage.
  DataSync accesses this secret using an IAM role that you provide.
  In all cases, the Secrets Manager secret is stored in your account, allowing you to update the
  secret as needed, independent of the DataSync service. Secrets created and managed by DataSync have the
  prefix `aws-datasync`.

You are charged for the use of secrets only when you create secrets outside of DataSync or make API calls to service-managed secrets from services other than DataSync.

## Using a service-managed secret encrypted

with a default key

When you create your DataSync location, you simply provide the secret string. DataSync
creates a secret resource in Secrets Manager to store the secret you provide, and encrypts the
secret with the default Secrets Manager KMS key for your account. You can change the secret
value directly in Secrets Manager, or by updating the location using the DataSync console, AWS CLI, or
SDK. When you delete the location resource or update it to use a custom secret, DataSync
deletes the secret resource automatically.

###### Note

To create, modify, and delete secret resources in Secrets Manager, DataSync must have the
appropriate permissions. For more information, see [AWS managed policies for DataSync](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess").

## Using a service-managed secret encrypted

with a custom AWS KMS key

When you create your DataSync location, you provide the secret and the ARN of your AWS KMS
key. DataSync automatically creates a secret resource in Secrets Manager to store the secret you
provide, and encrypts it using your AWS KMS key. You can change the secret value directly
in Secrets Manager, or by updating the location using the DataSync console, AWS CLI, or SDK. When you
delete the location resource or update it to use a custom secret, DataSync deletes the
secret resource automatically.

###### Note

Your AWS KMS key must use symmetric encryption with the `ENCRYPT_DECRYPT`
key type. For more information, see [Choosing a AWS Key Management Service
key](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_.

To create, modify, and delete secret resources in Secrets Manager, DataSync must have the
appropriate permissions. For more information, see [AWS managed policy: AWSDataSyncFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncfullaccess").

In addition to using the correct DataSync managed policy, you also need the following
permissions:

```
{
    "Sid": "DataSyncKmsPermissions",
    "Effect": "Allow",
    "Action": [
        "kms:Encrypt",
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "`your-kms-key-arn`",
    "Condition": {
        "StringLike": {
            "kms:ViaService": "secretsmanager.*.amazonaws.com"
        }
    }
}
```

Replace `your-kms-key-arn` with your KMS key ARN.

To retrieve and decrypt the secret value, DataSync uses a Service Linked Role (SLR) to
access your AWS KMS key. To make sure DataSync can use your KMS key, add the following to
the key’s policy statement:

```
{
    "Sid": "Allow DataSync to use the key for decryption",
    "Effect": "Allow",
    "Principal": {
            "AWS": "arn:aws:iam::`111122223333`:role/aws-service-role/datasync.amazonaws.com/AWSServiceRoleForDataSync"
    },
    "Action": "kms:Decrypt",
    "Resource": "*"
}
```

Replace `111122223333` with your AWS account ID.

## Using a secret that you manage

Before you create your DataSync location, [create a secret in
Secrets Manager](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md"). The value for the secret must only contain the secret string
itself in plain text. When you create your DataSync location, you provide the ARN of your
secret and an IAM role that DataSync uses to access both your secret and the AWS KMS key
used to encrypt your secret. To create an IAM role with the appropriate permissions,
do the following:

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, under **Access management**,
   choose **Roles**, and then choose **Create
   role**.
3. On the **Select trusted entity** page, for **Trusted
   entity type**, choose **AWS service**.
4. For **Use case**, choose **DataSync** from the
   drop-down list. Choose **Next**.
5. On the **Add permissions** page, choose
   **Next**. Enter a name for your role, and then choose
   **Create role**.
6. On the **Roles** page, search for the role that you just
   created and choose its name.
7. On the **Details** page for the role, choose the
   **Permissions** tab. Choose **Add
   permissions**, and then **Create inline
   policy**.
8. Choose the **JSON** tab and add the following permissions
   into the policy editor:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret"
 ],
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`your-secret-name`"
 }
 ]
}`

```

Replace `your-secret-name` with the name of your Secrets Manager
secret. 9. Choose **Next**. Enter a name for your policy, and then
choose **Create policy**. 10. (Recommended) To prevent the [cross-service confused deputy problem](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md"), do the following:

    1. On the **Details** page for the role, choose the
     **Trust relationships** tab. Choose **Edit
     trust policy**.
    2. Update the trust policy by using the following example, which includes
     the `aws:SourceArn` and `aws:SourceAccount` global
     condition context keys:



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Principal": {
     "Service": "datasync.amazonaws.com"
     },
     "Action": "sts:AssumeRole",
     "Condition": {
     "StringEquals": {
     "aws:SourceAccount": "`111122223333`"
     },
     "ArnLike": {
     "aws:SourceArn": "arn:aws:datasync:`us-east-1`:`111122223333`:*"
     }
     }
     }
     ]
    }`

    ```
    3. Choose **Update policy**.

You can specify this role when creating your location. If your secret uses a
customer-managed AWS KMS key for encryption, then you will also need to update the key’s
policy to allow access from the role you created in the previous procedure. To update
the policy, add the following to your AWS KMS key’s policy statement:

```
{
    "Sid": "Allow DataSync use of the key",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam:`111122223333`:role/`your-role-name`”
    },
    "Action": "kms:Decrypt",
    "Resource": "*"
}
```

Replace `111122223333` with your AWS account ID, and
`your-role-name` with the name of the IAM role you
created in the previous procedure.

###### Note

When you store secrets in Secrets Manager, your AWS account incurs charges. For
information about pricing, see [AWS Secrets Manager
Pricing](https://aws.amazon.com/secrets-manager/pricing/ "https://aws.amazon.com/secrets-manager/pricing/").
