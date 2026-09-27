

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Authorizing use of an AWS KMS customer managed key with Amazon Redshift (Provisioned) and Amazon Redshift Serverless
<a name="authorizing-kms-customer-managed-key"></a>

Amazon Redshift integrates with AWS Key Management Service (AWS KMS) to encrypt your data at rest. When you use a customer managed key, you have full control over the key policy, key rotation, and enabling or disabling the key. For more information about customer managed keys, see [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the *AWS Key Management Service Developer Guide*.

When Amazon Redshift uses a customer managed key in cryptographic operations, it acts on behalf of the user who is creating or modifying the Amazon Redshift provisioned cluster or Amazon Redshift Serverless resource.

## Required permissions
<a name="authorizing-kms-cmk-required-permissions"></a>

To create and use an Amazon Redshift provisioned cluster or an Amazon Redshift Serverless resource that is encrypted with a customer managed key, a user must have permission to call the following operations on the customer managed key:
+ `kms:CreateGrant`
+ `kms:GenerateDataKey`
+ `kms:Encrypt`
+ `kms:Decrypt`
+ `kms:DescribeKey`

The owner or administrator of the customer managed key can add these permissions for specific users in the key policy of the customer managed key, or in an IAM policy if the key policy allows it.

Amazon Redshift accesses the customer managed key through AWS KMS grants. Make sure that your key policy doesn't prevent Amazon Redshift from creating or using grants on the key. For example, explicit Deny statements, or restrictive conditions on Allow statements, can block grant creation and cause operations to fail.

As a security best practice, we recommend that you provide only the permissions that are required for your use case. For example, you can scope down the `kms:CreateGrant` permission by using a condition key such as `kms:GrantIsForAWSResource`.

For more information about controlling access to AWS KMS keys, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) and [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) in the *AWS Key Management Service Developer Guide*.