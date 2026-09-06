

# Getting started with Amazon EMR Serverless
<a name="getting-started"></a>

This tutorial helps you get started with EMR Serverless when you deploy a sample Spark or Hive workload. You'll create, run, and debug your own application. We show default options in most parts of this tutorial.

Before you launch an EMR Serverless application, complete the following tasks.

**Topics**
+ [Grant permissions to use EMR Serverless](#gs-permissions)
+ [Prepare storage for EMR Serverless](#gs-prepare-storage)
+ [Create an EMR Studio to run interactive workloads](#gs-interactive)
+ [Create a job runtime role](#gs-runtime-role)
+ [Getting started with EMR Serverless from the console](gs-console.md)
+ [Getting started from the AWS CLI](gs-cli.md)

## Grant permissions to use EMR Serverless
<a name="gs-permissions"></a>

To use EMR Serverless, you need a user or IAM role with an attached policy that grants permissions for EMR Serverless. To create a user and attach the appropriate policy to that user, follow the instructions in [Grant permissions](setting-up.md#setting-up-iam).

## Prepare storage for EMR Serverless
<a name="gs-prepare-storage"></a>

In this tutorial, you'll use an S3 bucket to store output files and logs from the sample Spark or Hive workload that you'll run using an EMR Serverless application. To create a bucket, follow the instructions in [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html) in the *Amazon Simple Storage Service Console User Guide*. Replace any further reference to `{{amzn-s3-demo-bucket}}` with the name of the newly created bucket. 

## Create an EMR Studio to run interactive workloads
<a name="gs-interactive"></a>

If you want to use EMR Serverless to execute interactive queries through notebooks that are hosted in EMR Studio, you need to specify an S3 bucket and the [minimum service role for EMR Serverless](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-service-role.html#emr-studio-service-role-serverless) to create a Workspace. For steps to get set up, see [Set up an EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-set-up.html) in the *Amazon EMR Management Guide*. For more information on interactive workloads, see [Run interactive workloads with EMR Serverless through EMR Studio](interactive-workloads.md).

## Create a job runtime role
<a name="gs-runtime-role"></a>

Job runs in EMR Serverless use a runtime role that provides granular permissions to specific AWS services and resources at runtime. In this tutorial, a public S3 bucket hosts the data and scripts. The bucket `{{amzn-s3-demo-bucket}}` stores the output. 

To set up a job runtime role, first create a runtime role with a trust policy so that EMR Serverless can use the new role. Next, attach the required S3 access policy to that role. The following steps guide you through the process.

------
#### [ Console ]

1. Navigate to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Policies**.

1. Choose **Create Policy**.

1. The **Create policy** page opens on a new tab. Select the **Policy editor **as Json and Paste the policy JSON below.
**Important**  
Replace `{{amzn-s3-demo-bucket}}` in the policy below with the actual bucket name created in [Prepare storage for EMR Serverless](#gs-prepare-storage). This is a basic policy for S3 access. For more job runtime role examples, see [Job runtime roles for Amazon EMR Serverless](security-iam-runtime-role.md).

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "ReadAccessForEMRSamples",
         "Effect": "Allow",
         "Action": [
           "s3:GetObject",
           "s3:ListBucket"
         ],
         "Resource": [
           "arn:aws:s3:::*.elasticmapreduce",
           "arn:aws:s3:::*.elasticmapreduce/*"
         ]
       },
       {
         "Sid": "FullAccessToOutputBucket",
         "Effect": "Allow",
         "Action": [
           "s3:PutObject",
           "s3:GetObject",
           "s3:ListBucket",
           "s3:DeleteObject"
         ],
         "Resource": [
           "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
           "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
         ]
       },
       {
         "Sid": "GlueCreateAndReadDataCatalog",
         "Effect": "Allow",
         "Action": [
           "glue:GetDatabase",
           "glue:CreateDatabase",
           "glue:GetDataBases",
           "glue:CreateTable",
           "glue:GetTable",
           "glue:UpdateTable",
           "glue:DeleteTable",
           "glue:GetTables",
           "glue:GetPartition",
           "glue:GetPartitions",
           "glue:CreatePartition",
           "glue:BatchCreatePartition",
           "glue:GetUserDefinedFunctions"
         ],
         "Resource": [
           "*"
         ]
       }
     ]
   }
   ```

------

1. Choose **Next** to enter a name for your policy, such as `EMRServerlessS3AndGlueAccessPolicy` and **Create policy** 

1. In the left navigation pane of IAM console , choose **Roles**.

1. Choose **Create role**.

1. For role type, choose **Custom trust policy** and paste the following trust policy. This allows jobs submitted to your Amazon EMR Serverless applications to access other AWS services on your behalf.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "AllowSTSAssumerole",
         "Effect": "Allow",
         "Principal": {
           "Service": "emr-serverless.amazonaws.com"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{123456789012}}"
           }
         }
       }
     ]
   }
   ```

------

1. Choose **Next** to navigate to the **Add permissions** page, then choose **EMRServerlessS3AndGlueAccessPolicy**.

1. In the **Name, review, and create** page, for **Role name**, enter a name for your role, for example, `EMRServerlessS3RuntimeRole`. To create this IAM role, choose **Create role**.

------
#### [ CLI ]

1. Create a file named `emr-serverless-trust-policy.json` that contains the trust policy to use for the IAM role. The file should contain the following policy.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "EMRServerlessTrustPolicy",
         "Effect": "Allow",
         "Principal": {
           "Service": "emr-serverless.amazonaws.com"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{123456789012}}"
           }
         }
       }
     ]
   }
   ```

------

1. Create an IAM role named `EMRServerlessS3RuntimeRole`. Use the trust policy that you created in the previous step.

   ```
   aws iam create-role \
       --role-name EMRServerlessS3RuntimeRole \
       --assume-role-policy-document file://emr-serverless-trust-policy.json
   ```

   Note the ARN in the output. You use the ARN of the new role during job submission, referred to after this as the `{{job-role-arn}}`.

1. Create a file named `emr-sample-access-policy.json` that defines the IAM policy for your workload. This provides read access to the script and data stored in public S3 buckets and read-write access to `{{amzn-s3-demo-bucket}}`. 
**Important**  
Replace `{{amzn-s3-demo-bucket}}` in the policy below with the actual bucket name created in [Prepare storage for EMR Serverless](#gs-prepare-storage).. This is a basic policy for AWS Glue and S3 access. For more job runtime role examples, see [Job runtime roles for Amazon EMR Serverless](security-iam-runtime-role.md).

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "ReadAccessForEMRSamples",
         "Effect": "Allow",
         "Action": [
           "s3:GetObject",
           "s3:ListBucket"
         ],
         "Resource": [
           "arn:aws:s3:::*.elasticmapreduce",
           "arn:aws:s3:::*.elasticmapreduce/*"
         ]
       },
       {
         "Sid": "FullAccessToOutputBucket",
         "Effect": "Allow",
         "Action": [
           "s3:PutObject",
           "s3:GetObject",
           "s3:ListBucket",
           "s3:DeleteObject"
         ],
         "Resource": [
           "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
           "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
         ]
       },
       {
         "Sid": "GlueCreateAndReadDataCatalog",
         "Effect": "Allow",
         "Action": [
           "glue:GetDatabase",
           "glue:CreateDatabase",
           "glue:GetDataBases",
           "glue:CreateTable",
           "glue:GetTable",
           "glue:UpdateTable",
           "glue:DeleteTable",
           "glue:GetTables",
           "glue:GetPartition",
           "glue:GetPartitions",
           "glue:CreatePartition",
           "glue:BatchCreatePartition",
           "glue:GetUserDefinedFunctions"
         ],
         "Resource": [
           "*"
         ]
       }
     ]
   }
   ```

------

1. Create an IAM policy named `EMRServerlessS3AndGlueAccessPolicy` with the policy file that you created in **Step 3**. Take note of the ARN in the output, as you will use the ARN of the new policy in the next step. 

   ```
   aws iam create-policy \
       --policy-name EMRServerlessS3AndGlueAccessPolicy \
       --policy-document file://emr-sample-access-policy.json
   ```

   Note the new policy's ARN in the output. You'll substitute it for `{{policy-arn}}` in the next step.

1. Attach the IAM policy `EMRServerlessS3AndGlueAccessPolicy` to the job runtime role `EMRServerlessS3RuntimeRole`.

   ```
   aws iam attach-role-policy \
       --role-name EMRServerlessS3RuntimeRole \
       --policy-arn {{policy-arn}}
   ```

------