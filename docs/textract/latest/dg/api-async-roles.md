

# Configuring Amazon Textract Core for asynchronous operations

The following procedures show you how to configure Amazon Textract Core to use with an Amazon SNS topic and an Amazon SQS queue.

**Note**  
If you're using these instructions to set up the [Detecting or analyzing text in a multipage document](async-analyzing-with-sqs.md) example, you don't need to do steps 3 – 6. The example includes code to create and configure the Amazon SNS topic and Amazon SQS queue.

**To configure Amazon Textract Core**

1. Set up an AWS account to access Amazon Textract Core. For more information, see [Step 1: Set up an AWS account and create a user](setting-up.md).

   Ensure that the user has at least the following permissions:
   + AmazonTextractFullAccess
   + AmazonS3ReadOnlyAccess
   + AmazonSNSFullAccess
   + AmazonSQSFullAccess

   Additionally, ensure that the user has permission to pass IAM roles to Amazon Textract Core. This is done through an IAM PassRole policy. A simple example of such a policy is below:

------
#### [ JSON ]

****  

   ```json
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "iam:PassRole",
               "Resource": "*",
               "Condition": {
                   "StringEquals": {"iam:PassedToService": "textract.amazonaws.com"}
               }
           }
       ]
   }
   ```

------

1. Install and configure the required AWS SDK. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md). 

1. [Create an Amazon SNS standard topic](https://docs.aws.amazon.com/sns/latest/dg/sns-tutorial-create-topic.html). Prepend the topic name with *AmazonTextract*. Note the topic Amazon Resource Name (ARN). Ensure that the topic is in the same AWS Region as the AWS endpoint that you're using with your AWS account.

1. [Create an Amazon SQS standard queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-create-queue.html) by using the [Amazon SQS console](https://console.aws.amazon.com/sqs/). Note the queue ARN.

1. [Subscribe the queue to the topic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-subscribe-queue-sns-topic.html) you created in step 3.

1. [Give permission to the Amazon SNS topic to send messages to the Amazon SQS queue](https://docs.aws.amazon.com/sns/latest/dg/subscribe-sqs-queue-to-sns-topic.html).

1. Create an IAM service role to give Amazon Textract Core access to your Amazon SNS topics. Note the ARN of the service role. For more information, see [Giving Amazon Textract Core access to your Amazon SNS topic](#api-async-roles-all-topics).

1. [Add the following inline policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#embed-inline-policy-console) to the IAM user that you created in step 1. Give the inline policy a name.

1. You can now run the examples in [Detecting or analyzing text in a multipage document](async-analyzing-with-sqs.md).

## Giving Amazon Textract Core access to your Amazon SNS topic
<a name="api-async-roles-all-topics"></a>

Amazon Textract Core needs permission to send a message to your Amazon SNS topic when an asynchronous operation is complete. You use an IAM service role to give Amazon Textract Core access to the Amazon SNS topic. 

 When you create the Amazon SNS topic, you must prepend the topic name with **AmazonTextract**, for example: **AmazonTextractMyTopicName**. 

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/home#/roles).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. For **Select type of trusted entity**, choose **AWS service**. 

1. For **Choose the service that will use this role**, choose **Textract**.

1. Choose **Next: Permissions**.

1. Verify that the **AmazonTextractServiceRole** policy has been included in the list of attached policies. To display the policy in the list, enter part of the policy name in the **Filter policies**.

1. Choose **Next: Tags**.

1. You don't need to add tags, so choose **Next: Review**.

1. In the **Review** section, for **Role name**, enter a name for the role (for example, `TextractRole`). In **Role description**, update the description for the role, and then choose **Create role**.

1. Choose the new role to open the role's details page.

1. In the **Summary**, copy the **Role ARN** value and save it.

1. Choose **Trust relationships**.

1. Choose **Edit trust relationship**, and edit the trust policy. Ensure that your trust policy includes conditions that limit the scope of permissions to just the required resources, as this will help prevent the confused deputy problem. For more details about this potential security issue, see [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md). In the example below, replace the {{red}} text with your AWS account ID.

------
#### [ JSON ]

****  

   ```json
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": {
       "Sid": "ConfusedDeputyPreventionExamplePolicy",
       "Effect": "Allow",
       "Principal": {
         "Service": "textract.amazonaws.com"
       },
       "Action": "sts:AssumeRole",
       "Condition": {
         "ArnLike": {
           "aws:SourceArn":"arn:aws:textract:*:{{123456789012}}:*"
         },
         "StringEquals": {
           "aws:SourceAccount": "{{123456789012}}"
         }
       }
     }
   }
   ```

------

1. Choose **Update Trust Policy**.

## Permissions for output configuration
<a name="async-output-config"></a>

You can have Amazon Textract Core send the results of asynchronous analysis operations to a designated Amazon S3 bucket by using the `OutputConfig` feature of asynchronous API operations. If you are using the `OutputConfig` option for an asynchronous analysis operation to customize where the output of your operations is sent, additional configuration is required. You must let Amazon Textract Core decrypt your uploads and provide permissions for certain Amazon S3 operations.

**To allow decryption of S3 bucket uploads**

You will need to provide the appropriate users with the correct Amazon S3 permissions.

1. Navigate to the **Users** section of the [IAM console](https://console.aws.amazon.com/iam/home#/users).

1. Select the user you created in **Step 1** of the **To configure Amazon Textract Core** section above.

1. Choose **Add inline policy** for your user.

1. Attach a JSON policy that includes the `s3:GetObject`, `s3:PutObject`, `s3:ListMultipartUploadParts`, `s3:ListBucketMultipartUploads`, and `s3:AbortMultipartUpload` operations. Your JSON may look like the following:

------
#### [ JSON ]

****  

   ```json
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "s3:Get*",
                   "s3:List*",
                   "s3:PutObject",
                   "s3:GetObject",
                   "s3-object-lambda:Get*",
                   "s3-object-lambda:List*",
                   "s3:ListMultipartUploadParts",
                   "s3:ListBucketMultipartUploads",
                   "s3:AbortMultipartUpload"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

**To provide AWS KMS key permissions**  
You must [add](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html#key-policy-modifying-how-to-console-policy-view) permissions to your AWS Key Management Service key that will allow your service role to decrypt your uploads. The service role will need permission for `kms:GenerateDataKey` and `kms:Decrypt` actions. Ensure that the service role you created in **Step 7** in the **To configure Amazon Textract Core** section has a permissions policy that looks like the following example. 

In the following example, replace `ARN from Step 7` with the ARN of your service role:

```
{
    "Sid": "Decrypt only",
    "Effect": "Allow",
    "Principal": {
        "AWS": "{{ARN from Step 7}}"
    },
    "Action": [
        "kms:Decrypt",
        "kms:ReEncrypt",
        "kms:GenerateDataKey",
        "kms:DescribeKey"
    ],
    "Resource": "*"
}
```