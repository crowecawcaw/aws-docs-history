

# Prerequisites

Before you can publish your model package or algorithm in AWS Marketplace, you must have the following:
+  An AWS account that is registered as an AWS Marketplace seller in AWS Partner Central. For more information, see [Registration process](registration-process.md).
+ A completed seller public profile. For more information, see [Step 1: Register and create your seller profile](create-public-profile.md).
+  For publishing paid products, you must complete the tax interview and bank forms. This is not required for publishing free products. For more information, see [Seller registration process](https://docs.aws.amazon.com/marketplace/latest/userguide/registration-process.html). 
+ Permissions to manage products in AWS Partner Central, and permissions to describe your Amazon SageMaker AI resources. For more information, see [Required permissions](#ml-permissions-required).

## Required permissions
<a name="ml-permissions-required"></a>

To publish an Amazon SageMaker AI product, you need two sets of permissions:
+ The AWS Identity and Access Management (IAM) user or role that you sign in with needs permission to describe your model package or algorithm. The **Add version** wizard uses this identity to read your resource from SageMaker AI when you enter its ARN.
+ An IAM access role that has a trust relationship with the AWS Marketplace service principal. AWS Marketplace uses this role to access your SageMaker AI resource for validation and replication. You enter its ARN when you add a version.

**To set sign-in permissions**
+  Add the following permissions to the IAM role: 

  1. **sagemaker:DescribeModelPackage** — For listing a model package 

  1.  **sagemaker:DescribeAlgorithm** — For listing an algorithm 

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
                     "sagemaker:DescribeModelPackage", 
                     "sagemaker:DescribeAlgorithm"
                 ],
                 "Resource": "*"  
            }
         ] 
     }
     ```

------

**To set up the IAM access role**

1. Follow the steps to create a role with a custom trust policy. For more information, see [Creating an IAM role using a custom trust policy (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html).

1. Enter the following for the custom trust policy statement:

------
#### [ JSON ]

****  

   ```json
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "Statement1",
               "Effect": "Allow",
               "Principal": {
                   "Service": "assets.marketplace.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

1. Enter the following permissions policy:

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
                   "sagemaker:DescribeModelPackage", 
                   "sagemaker:DescribeAlgorithm"
               ],
               "Resource": "*"  
          }
       ] 
   }
   ```

------

1. When you add a version, enter the role ARN in **IAM access role ARN**.

   The ARN must use the format `arn:aws:iam::<account-id>:role/<role-name>`, with no role path. Otherwise, AWS Partner Central shows the message *Enter a valid IAM access role ARN.*

 For the AWS Marketplace permissions needed, or for managing your seller account, see [Policies and permissions for AWS Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html). 

## Required assets
<a name="ml-required-assets"></a>

Before creating a machine learning product listing, ensure that you have the following required assets:
+ **Amazon Resource Name (ARN)** — Provide the ARN of the model package or algorithm resource in the AWS Region that you are publishing from (see [Supported AWS Regions for publishing](ml-service-restrictions-and-limits.md#ml-supported-aws-regions-for-publishing)). 
  +  An ARN for a model package has this form: `arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>` 

     To find your model package ARN, see [My marketplace model packages](https://console.aws.amazon.com/sagemaker/home#/model-packages/my-resources). 
  +  An ARN for an algorithm has this form: `arn:aws:sagemaker:<region>:<account-id>:algorithm/<algorithm-name>` 

     To find your algorithm resource ARN, see [My algorithms](https://console.aws.amazon.com/sagemaker/home#/algorithms/my-resources). 
+ [Requirements for usage information](ml-listing-requirements-and-best-practices.md#ml-requirements-for-usage-information) — Provide details about inputs, outputs, and code examples. 
+  [Requirements for inputs and outputs](ml-listing-requirements-and-best-practices.md#ml-requirements-for-inputs-and-outputs) — Provide a URL or text for each input and output data sample. 
+ [Requirements for Jupyter notebook](ml-listing-requirements-and-best-practices.md#ml-requirements-for-jupyter-notebook) — Demonstrate complete product usage. 