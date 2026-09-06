

# Use AWS KMS Permissions for Amazon SageMaker Partner AI Apps
<a name="partner-apps-kms"></a>

You can protect your data at rest using encryption for Amazon SageMaker Partner AI Apps. By default, it uses server-side encryption with a SageMaker owned key. SageMaker also supports an option for server-side encryption with a customer managed KMS key.

## Server-side encryption with SageMaker managed keys (Default)
<a name="partner-apps-managed-key"></a>

Partner AI Apps encrypt all your data at rest using an AWS managed key by default.

## Server-side encryption with customer managed KMS keys (Optional)
<a name="partner-apps-customer-managed-key"></a>

Partner AI Apps support the use of a symmetric customer managed key that you create, own, and manage to replace the existing AWS owned encryption. Because you have full control of this layer of encryption, you can perform such tasks as:
+ Establishing and maintaining key policies
+ Establishing and maintaining IAM policies and grants
+ Enabling and disabling key policies
+ Rotating key cryptographic material
+ Adding tags
+ Creating key aliases
+ Scheduling keys for deletion

For more information, see [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the *AWS Key Management Service Developer Guide*.

## How Partner AI Apps use grants in AWS KMS
<a name="partner-apps-grants-cmk"></a>

Partner AI Apps require a grant to use your customer managed key. When you create an application encrypted with a customer managed key, Partner AI Apps creates a grant on your behalf by sending a CreateGrant request to AWS KMS. Grants in AWS KMS are used to give Partner AI Apps access to a KMS key in a customer account.

You can revoke access to the grant, or remove the service's access to the customer managed key at any time. If you do, Partner AI App won't be able to access any of the data encrypted by the customer managed key, which affects operations that are dependent on that data. The application will not operate properly and will become irrecoverable.

## Create a customer managed key
<a name="partner-apps-create-cmk"></a>

You can create a symmetric customer managed key by using the AWS Management Console or the AWS KMS APIs.

**To create a symmetric customer managed key**

Follow the steps for [Creating symmetric encryption KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *AWS Key Management Service Developer Guide*.

**Key policy**

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy. For more information, see [Determining access to AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/determining-access.html) in the *AWS Key Management Service Developer Guide*.

To use your customer managed key with your Partner AI App resources, the following API operations must be permitted in the key policy. The principal for these operations depends on whether the role is used to create or use the application. 
+ Creating the application:
  + `[kms:CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html)`
  + [`kms:DescribeKey`](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) 
+ Using the application:
  + [`kms:Decrypt`](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) 
  + [`kms:GenerateDataKey`](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html)

The following are policy statement examples you can add for Partner AI Apps based on whether the persona is an administrator or user. For more information about specifying permissions in a policy, see [AWS KMS permissions](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) in the *AWS Key Management Service Developer Guide*. For more information about troubleshooting, see [Troubleshooting key access](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html) in the *AWS Key Management Service Developer Guide*.

**Administrator**

The following policy statement is used for the administrator who is creating Partner AI Apps.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "example-key-policy",
    "Statement": [
        {
            "Sid": "Allow use of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/{{<admin-role>}}"
            },
            "Action": [
                "kms:CreateGrant",
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "sagemaker.{{us-east-1}}.amazonaws.com"
                }
            }
        }
    ]
}
```

------

**User**

The following policy statement is for the user of the Partner AI Apps.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Id":"example-key-policy",
  "Statement":[
    {
      "Effect":"Allow",
      "Principal":{
        "AWS":"arn:aws:iam::{{111122223333}}:role/{{user-role}}"
      },
      "Action":[
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource":"*",
      "Condition":{
        "StringEquals":{
          "kms:ViaService":"sagemaker.{{us-east-1}}.amazonaws.com"
        }
      }
    }
  ]
}
```

------