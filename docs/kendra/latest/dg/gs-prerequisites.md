

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Prerequisites
<a name="gs-prerequisites"></a>

The following steps are prequisites for the getting started exercises. The steps show you how to set up your account, create an IAM role that gives Amazon Kendra permission to make calls on your behalf, and index documents from an Amazon S3 bucket. An S3 bucket is used as an example, but you can use other data sources that Amazon Kendra supports. See [Data sources](https://docs.aws.amazon.com/kendra/latest/dg/hiw-data-source.html).

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.
+ If you are using an S3 bucket containing documents to test Amazon Kendra, create an S3 bucket in the same region that you are using Amazon Kendra. For instructions, see [Creating and Configuring an S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-configure-bucket.html) in the *Amazon Simple Storage Service User Guide*.

  Upload your documents to your S3 bucket. For instructions, see [Uploading, Downloading, and Managing Objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-download-objects.html) in the *Amazon Simple Storage Service User Guide*.

  If you are using another data source, you must have an active site and credentials to connect to the data source.

If you are using the console to get started, start with [Getting started with the Amazon Kendra console](gs-console.md).

## Amazon Kendra resources: AWS CLI, SDK, console
<a name="gs-prereq-cli-sdk"></a>

There are certain permissions required if you use CLI, SDK, or the console.

To use Amazon Kendra for the CLI, SDK, or console you must have permissions to allow Amazon Kendra to create and manage resources on your behalf. Depending on your use case, these permissions include access to the Amazon Kendra API itself, AWS KMS keys if you want to encrypt your data through a custom CMK, Identity Center directory if you want to integrate with AWS IAM Identity Center or [create a Search Experience](https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html). For a full list of permissions for different use cases, see [IAM roles](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html).

First, you must attach the below permissions to your IAM user.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "Stmt1644430853544",
      "Action": [
        "kms:CreateGrant",
        "kms:DescribeKey"
      ],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Sid": "Stmt1644430878150",
      "Action": "kendra:*",
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Sid": "Stmt1644430973706",
      "Action": [
        "sso:AssociateProfile",
        "sso:CreateManagedApplicationInstance",
        "sso:DeleteManagedApplicationInstance",
        "sso:DisassociateProfile",
        "sso:GetManagedApplicationInstance",
        "sso:GetProfile",
        "sso:ListDirectoryAssociations",
        "sso:ListProfileAssociations",
        "sso:ListProfiles"
      ],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Sid": "Stmt1644430999558",
      "Action": [
        "sso-directory:DescribeGroup",
        "sso-directory:DescribeGroups",
        "sso-directory:DescribeUser",
        "sso-directory:DescribeUsers"
      ],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Sid": "Stmt1644431025960",
      "Action": [
        "identitystore:DescribeGroup",
        "identitystore:DescribeUser",
        "identitystore:ListGroups",
        "identitystore:ListUsers"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

------

Second, if you use the CLI or SDK, you must also create an IAM role and policy to access Amazon CloudWatch Logs. If you are using the console, you don't need to create an IAM role and policy for this. You create this as part of the console procedure.

**To create an IAM role and policy for the AWS CLI and SDK that allows Amazon Kendra to access your Amazon CloudWatch Logs.**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. From the left menu, choose **Policies** and then choose **Create policy**.

1. Choose **JSON** and then replace the default policy with the following:

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
                   "cloudwatch:PutMetricData"
               ],
               "Resource": "*",
               "Condition": {
                   "StringEquals": {
                       "cloudwatch:namespace": "AWS/Kendra"
                   }
               }
           },
           {
               "Effect": "Allow",
               "Action": [
                   "logs:DescribeLogGroups"
               ],
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "logs:CreateLogGroup"
               ],
               "Resource": [
                   "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/kendra/*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "logs:DescribeLogStreams",
                   "logs:CreateLogStream",
                   "logs:PutLogEvents"
               ],
               "Resource": [
                   "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/kendra/*:log-stream:*"
               ]
           }
       ]
   }
   ```

------

1. Choose **Review policy**.

1. Name the policy "KendraPolicyForGettingStartedIndex" and then choose **Create policy**.

1. From the left menu, choose **Roles** and then choose **Create role**.

1. Choose **Another AWS account** and then type your account ID in **Account ID**. Choose **Next: Permissions**.

1. Choose the policy that you created above and then choose **Next: Tags**

1. Don't add any tags. Choose **Next: Review**.

1. Name the role "KendraRoleForGettingStartedIndex" and then choose **Create role**.

1. Find the role that you just created. Choose the role name to open the summary. Choose **Trust relationships** and then choose **Edit trust relationship**.

1. Replace the existing trust relationship with the following:

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
             "Service": "kendra.amazonaws.com"
           },
           "Action": "sts:AssumeRole"
         }
       ]
   }
   ```

------

1. Choose **Update trust policy**.

Third, if you use an Amazon S3 to store your documents or you are using S3 to test Amazon Kendra, you also must create an IAM role and policy to access your bucket. If you are using another data source, see [IAM roles for data sources](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html#iam-roles-ds).

**To create an IAM role and policy that allows Amazon Kendra to access and index your Amazon S3 bucket.**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. From the left menu, choose **Policies** and then choose **Create policy**.

1. Choose **JSON** and then replace the default policy with the following:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Action": [
                   "s3:GetObject"
               ],
               "Resource": [
                   "arn:aws:s3:::{{bucket name}}/*"
               ],
               "Effect": "Allow"
           },
           {
               "Action": [
                   "s3:ListBucket"
               ],
               "Resource": [
                   "arn:aws:s3:::{{bucket name}}"
               ],
               "Effect": "Allow"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "kendra:BatchPutDocument",
                   "kendra:BatchDeleteDocument"
               ],
               "Resource": "arn:aws:kendra:{{us-east-1}}:{{123456789012}}:index/*"
           }
       ]
   }
   ```

------

1. Choose **Review policy**.

1. Name the policy "KendraPolicyForGettingStartedDataSource" and then choose **Create policy**.

1. From the left menu, choose **Roles** and then choose **Create role**.

1. Choose **Another AWS account** and then type your account ID in **Account ID**. Choose **Next: Permissions**.

1. Choose the policy that you created above and then choose **Next: Tags**

1. Don't add any tags. Choose **Next: Review**.

1. Name the role "KendraRoleForGettingStartedDataSource" and then choose **Create role**.

1. Find the role that you just created. Choose the role name to open the summary. Choose **Trust relationships** and then choose **Edit trust relationship**.

1. Replace the existing trust relationship with the following:

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
             "Service": "kendra.amazonaws.com"
           },
           "Action": "sts:AssumeRole"
         }
       ]
   }
   ```

------

1. Choose **Update trust policy**.

Depending on how you want to use the Amazon Kendra API, do one of the following.
+ [Getting started (AWS CLI)](gs-cli.md)
+ [Getting started (AWS SDK for Java)](gs-java.md)
+ [Getting started (AWS SDK for Python (Boto3))](gs-python.md)