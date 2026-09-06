

# Set up cross-account support for Amazon SageMaker Model Cards
<a name="model-cards-xaccount"></a>

Use cross-account support in Amazon SageMaker Model Cards to share model cards between AWS accounts. The account where the model cards are created is the *model card account*. Users in the model card account share them with the *shared accounts*. The users in a shared account can update the model cards or create PDFs of them.

Users in the model card account share their model cards through AWS Resource Access Manager (AWS RAM). AWS RAM helps you share resources across AWS accounts. For an introduction to AWS RAM, see [What is AWS Resource Access Manager?](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)

The following is the process to share model cards:

1. A user in the model card account sets up the cross-account model card sharing using AWS Resource Access Manager.

1. If the model cards are encrypted with AWS KMS keys, the user setting up model sharing must also provide users in the shared account with AWS KMS permissions.

1. A user in the shared account accepts the invite to the resource share.

1. A user in the shared account provides the other users with permissions to access the model cards.

If you're a user in the model card account, see the following sections:
+ [Set up cross-account model card sharing](#model-cards-xaccount-set-up)
+ [Set up AWS KMS permissions for the shared account](#model-cards-xaccount-kms)
+ [Get responses to your resource share invitation](#model-cards-xaccount-set-up-responses)

If you're a user in the shared account, see [Set up IAM user permissions in the shared account](#model-cards-xaccount-shared-account-permissions) about setting up permissions for yourself and the other users in the account.

## Set up cross-account model card sharing
<a name="model-cards-xaccount-set-up"></a>

Use AWS Resource Access Manager (AWS RAM) to grant users in your AWS account access to view or update model cards created in a different AWS account.

To set up model card sharing, you must create a resource share. A resource share specifies:
+ The resources being shared
+ Who or what has access to the resources
+ Managed permissions for the resources

For more information about resource shares, see [Terms and concepts for AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-terms-and-concepts.html). We recommend taking the time to understand AWS RAM conceptually before you go through the process of creating a resource share.

**Important**  
You must have permissions to create a resource share. For more information about permissions, see [How AWS RAM works with IAM](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-policies.html).

For procedures to create a resource share and additional information about them, see [Create a resource share](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-create).

When you go through the procedure of creating a resource share, you specify `sagemaker:ModelCard` as the resource type. You must also specify the Amazon Resource Number (ARN) of the AWS RAM resource-based policy. You can specify either the default policy or the policy that has additional permissions to create a PDF of the model card.

With the default `AWSRAMPermissionSageMakerModelCards` resource-based policy, the users in the shared account have permissions to do the following operations:
+  [DescribeModelCard](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelCard.html)
+ [ListModelCardVersions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelCardVersions.html)
+ [UpdateModelCard](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateModelCard.html)

With the `AWSRAMPermissionSageMakerModelCardsAllowExport` resource-based policy, the users in the shared account have permissions to do all of the preceding actions. They also have permissions to create a model card export job and describe it through the following operations:
+ [CreateModelCardExportJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelCardExportJob.html)
+ [DescribeModelCardExportJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelCardExportJob.html)

The users in the shared account can create an export job to generate a PDF of a model card. They can also describe an export job that has been created to find the PDF's Amazon S3 URI.

Model cards and export jobs are resources. The model card account owns the export jobs created by a user in the shared account. For example, a user in account A shares model card X with shared account B. A user in account B creates export job Y for model card X that stores the output in an Amazon S3 location that the user in account B specifies. Even though account B created export job Y, it belongs to account A.

Each AWS account has resource quotas. For information about quotas related to model cards, see [Amazon SageMaker AI endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html#limits_sagemaker).

### Set up AWS KMS permissions for the shared account
<a name="model-cards-xaccount-kms"></a>

If the model cards that you're sharing have been encrypted with AWS Key Management Service keys, you also need to share the access to the keys with the shared account. Otherwise, the users in the shared account can't view, update, or export the model cards. For an overview of AWS KMS, see [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).

To provide AWS KMS permissions to users in the shared account, update your key policy with the following statement:

```
{
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam::{{shared-account-id}}::role/{{example-IAM-role}}"
        ]
    },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt",
    ]
    "Resource": "arn:aws:kms:{{AWS-Region-of-model-card-account}}:{{model-card-account-id}}:key/{{AWS KMS-key-id}}"
    "Condition": {
        "Bool": {"kms:GrantIsForAWSResource": true },
        "StringEquals": {
            "kms:ViaService": [
                "sagemaker.{{AWS-Region}}.amazonaws.com", 
                "s3.{{AWS-Region}}.amazonaws.com"
            ],
        },
        "StringLike": {
          "kms:EncryptionContext:aws:sagemaker:model-card-arn": "arn:aws:sagemaker:{{AWS-Region}}:{{model-card-account-id}}:model-card/{{model-card-name}}"
        }
    }    
}
```

The preceding statement provides users in the shared account with `kms:Decrypt` and `kms:GenerateDataKey` permissions. With `kms:Decrypt`, users can decrypt the model cards. With `kms:GenerateDataKey`, users can encrypt the model cards that they update or the PDFs that they create.

### Get responses to your resource share invitation
<a name="model-cards-xaccount-set-up-responses"></a>

After you've created a resource share, the shared accounts that you've specified in the resource share receive an invitation to join it. They must accept the invite to access the resources.

For information about accepting a resource share invite, see [Using shared AWS resources ](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-shared.html)in the *AWS Resource Access Manager User Guide*.

### Set up IAM user permissions in the shared account
<a name="model-cards-xaccount-shared-account-permissions"></a>

The following information assumes that you've accepted the resource share invitation from the model card account. For more information about accepting a resource share invitation, see [Using shared AWS resources ](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-shared.html).

You and the other users in your account use an IAM role to access the model cards shared from the model card account. Use the following template to change the policy of the IAM role. You can modify the template for your own use case.

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
                "sagemaker:DescribeModelCard",
                "sagemaker:UpdateModelCard",
                "sagemaker:CreateModelCardExportJob",
                "sagemaker:ListModelCardVersions",
                "sagemaker:DescribeModelCardExportJob"
            ],
            "Resource": [
                "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:model-card/{{example-model-card-name-0}}",
                "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:model-card/{{example-model-card-name-1}}/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket-storing-the-pdf-of-the-model-card}}/{{model-card-name}}/*"
        }
    ]
}
```

------

To access model cards encrypted using AWS KMS, you must provide users in your account with the following AWS KMS permissions.

```
{
     "Effect": "Allow",
     "Action": [
         "kms:GenerateDataKey",
         "kms:Decrypt",
     ],
     "Resource": "arn:aws:kms:{{AWS-Region}}:{{AWS-account-id-where-the-model-card-is-created}}:key/{{AWS Key Management Service-key-id}}"
}
```