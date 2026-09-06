

# Encrypt build outputs using a customer managed key
<a name="setting-up-kms"></a>

If you follow the steps in [Getting started using the console](getting-started-overview.md#getting-started) to access AWS CodeBuild for the first time, you most likely do not need the information in this topic. However, as you continue using CodeBuild, you might want to do things such as encrypt build artifacts.

For AWS CodeBuild to encrypt its build output artifacts, it needs access to a KMS key. By default, CodeBuild uses the AWS managed key for Amazon S3 in your AWS account.

If you do not want to use the AWS managed key, you must create and configure a customer managed key yourself. This section describes how to do this with the IAM console.

For information about customer managed keys, see [AWS Key Management Service Concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) and [Creating Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS KMS Developer Guide*.

To configure a customer managed key for use by CodeBuild, follow the instructions in the "How to Modify a Key Policy" section of [Modifying a Key Policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html) in the *AWS KMS Developer Guide*. Then add the following statements (between {{\#\#\# BEGIN ADDING STATEMENTS HERE \#\#\#}} and {{\#\#\# END ADDING STATEMENTS HERE \#\#\#}}) to the key policy. Ellipses (`...`) are used for brevity and to help you locate where to add the statements. Do not remove any statements, and do not type these ellipses into the key policy.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "s3.us-east-1.amazonaws.com",
          "kms:CallerAccount": "{{111122223333}}"
        }
      }
    },
    {
      "Effect": "Allow", 
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
      ],
      "Resource": "*"
    }
  ]
}
```

------
+ {{region-ID}} represents the ID of the AWS region where the Amazon S3 buckets associated with CodeBuild are located (for example, `us-east-1`).
+ {{account-ID}} represents the ID of the of the AWS account that owns the customer managed key.
+ {{CodeBuild-service-role}} represents the name of the CodeBuild service role you created or identified earlier in this topic.

**Note**  
To create or configure a customer managed key through the IAM console, you must first sign in to the AWS Management Console by using one of the following:  
Your AWS root account. This is not recommended. For more information, see [The Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) in the *user Guide*.
An administrator user in your AWS account. For more information, see [Creating Your First AWS account root user and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *user Guide*.
A user in your AWS account with permission to create or modify the customer managed key. For more information, see [Permissions Required to Use the AWS KMS Console](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html#console-permissions) in the *AWS KMS Developer Guide*.