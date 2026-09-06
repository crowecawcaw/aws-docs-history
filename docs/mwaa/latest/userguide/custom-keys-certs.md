

# Using customer-managed keys for encryption
<a name="custom-keys-certs"></a>

You can optionally provide a [Customer-managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) for data encryption on your environment. You must create the customer-managed KMS key in the same Region as your Amazon MWAA environment instance and your Amazon S3 bucket where you store resources for your workflows. If the customer-managed KMS key that you specify is in a different account from the one you use to configure an environment, you must specify the key using its ARN for cross-account access. For more information about creating keys, refer to [Creating Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.

## What's supported
<a name="custom-keys-grants-support"></a>


| AWS KMS feature | Supported | 
| --- | --- | 
| An [AWS KMS key ID or ARN](https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-id-arn.html). | Yes | 
| An [AWS KMS key alias](https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html). | No | 
| An [AWS KMS multi-region key](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html). | No | 

## Using Grants for Encryption
<a name="custom-keys-grants-provide"></a>

This topic describes the grants Amazon MWAA attaches to a customer-managed KMS key on your behalf to encrypt and decrypt your data.

### How it works
<a name="custom-keys-certs-grants"></a>

There are two resource-based access control mechanisms supported by AWS KMS for customer-managed KMS key: a [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) and [grant](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html).

A key policy is used when the permission is mostly static and used in synchronous service mode. A grant is used when more dynamic and granular permissions are required, such as when a service needs to define different access permissions for itself or other accounts.

Amazon MWAA uses and attaches four grant policies to your customer-managed KMS key. This is due to the granular permissions required for an environment to encrypt data at rest from CloudWatch Logs, Amazon SQS queue, Aurora PostgreSQL database database, Secrets Manager secrets, Amazon S3 bucket and DynamoDB tables.

When you create an Amazon MWAA environment and specify a customer-managed KMS key, Amazon MWAA attaches the grant policies to your customer-managed KMS key. These policies allow Amazon MWAA in `airflow.{{us-east-1}}.amazonaws.com` to use your customer-managed KMS key to encrypt resources on your behalf that are owned by Amazon MWAA.

Amazon MWAA creates, and attaches, additional grants to a specified KMS key on your behalf. This includes policies to retire a grant if you delete your environment, to use your customer-managed KMS key for Client-Side Encryption (CSE), and for the AWS Fargate execution role that needs to access secrets protected by your customer-managed key in Secrets Manager.

## Grant policies
<a name="custom-keys-certs-grant-policies"></a>

Amazon MWAA adds the following [resource based policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) grants on your behalf to a customer-managed KMS key. These policies allow the grantee and the principal (Amazon MWAA) to perform actions defined in the policy.

### Grant 1: used to create data plane resources
<a name="custom-keys-certs-grant-policies-1"></a>

```
{
  "Name": "mwaa-grant-for-env-mgmt-role-{{environment name}}",
  "GranteePrincipal": "airflow.{{us-east-1}}.amazonaws.com",
  "RetiringPrincipal": "airflow.{{us-east-1}}.amazonaws.com",
  "Operations": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:CreateGrant",
    "kms:DescribeKey",
    "kms:RetireGrant"
  ]
}
```

### Grant 2: used for `ControllerLambdaExecutionRole` access
<a name="custom-keys-certs-grant-policies-2"></a>

```
{
  "Name": "mwaa-grant-for-lambda-exec-{{environment name}}",
  "GranteePrincipal": "airflow.{{us-east-1}}.amazonaws.com",
  "RetiringPrincipal": "airflow.{{us-east-1}}.amazonaws.com",
  "Operations": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:DescribeKey",
    "kms:RetireGrant"
  ]
}
```

### Grant 3: used for `CfnManagementLambdaExecutionRole` access
<a name="custom-keys-certs-grant-policies-3"></a>

```
{
  "Name": " mwaa-grant-for-cfn-mgmt-{{environment name}}",
  "GranteePrincipal": "airflow.{{us-east-1}}.amazonaws.com",
  "RetiringPrincipal": "airflow.{{us-east-1}}.amazonaws.com",
  "Operations": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:DescribeKey"
  ]
}
```

### Grant 4: used for Fargate execution role to access backend secrets
<a name="custom-keys-certs-grant-policies-4"></a>

```
{
  "Name": "mwaa-fargate-access-for-{{environment name}}",
  "GranteePrincipal": "airflow.{{us-east-1}}.amazonaws.com",
  "RetiringPrincipal": "airflow.{{us-east-1}}.amazonaws.com",
  "Operations": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:DescribeKey",
    "kms:RetireGrant"
  ]
}
```

## Attaching key policies to a customer-managed key
<a name="custom-keys-certs-grant-policies-attach"></a>

If you choose to use your own customer-managed KMS key with Amazon MWAA, you must attach the following policy to the key to allow Amazon MWAA to use it to encrypt your data.

If the customer-managed KMS key you used for your Amazon MWAA environment is not already configured to work with CloudWatch, you must update the [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) to allow for encrypted CloudWatch Logs. For more information, refer to the [Encrypt log data in CloudWatch using AWS Key Management Service service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html).

The following example represents a key policy for CloudWatch Logs. Substitute the sample values provided for the region.

```
{
  "Effect": "Allow",
  "Principal": {
    "Service": "logs.us-east-1.amazonaws.com"
  },
  "Action": [
    "kms:Encrypt*",
    "kms:Decrypt*",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:Describe*"
  ],
  "Resource": "*",
  "Condition": {
    "ArnLike": {
      "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:us-east-1:*:*"
    }
  }
}
```