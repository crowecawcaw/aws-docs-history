# Set up IAM-based domains in Amazon SageMaker Unified Studio

Setting up an IAM-based domain in Amazon SageMaker Unified Studio requires an IAM roles used for domain
administration tasks. The setup process validates your IAM role configurations and guides
you through any necessary policy attachments. You can choose to create new execution IAM
role with default permissions or use existing roles that meet the service
requirements.

In addition, you must choose encryption settings before you can complete setup. The
setup typically completes in minutes and automatically provisions the required AWS
resources.

**Prepare the Login IAM role for your IAM-based
domain:**

1. Login to the IAM role (defined in [Overview of IAM-based domains](iam-based-domains-overview.md "iam-based-domains-overview.md")) with AWS IAM administrator privileges
   defined in the pre-requisites.
2. Navigate to the IAM console.
3. Choose **Add permission** followed by **Attach
   policy** and search for the managed policy
   `SageMakerStudioAdminIAMConsolePolicy`. Select it to add it to your
   existing role.
4. Do one of the following:
   - Add the following inline policy to your Login IAM role if you are choosing to use a new role as the Execution IAM role:

   ```

   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "CreateRoleStatement",
               "Effect": "Allow",
               "Action": [
                   "iam:CreatePolicy",
                   "iam:CreateRole"
               ],
               "Resource": [
                   "arn:aws:iam::*:policy/service-role/AmazonSageMaker*",
                   "arn:aws:iam::*:role/service-role/AmazonSageMaker*"
               ]
           },
           {
               "Sid": "AttachRolePolicyStatement",
               "Effect": "Allow",
               "Action": "iam:AttachRolePolicy",
               "Resource": "arn:aws:iam::*:role/service-role/AmazonSageMaker*",
               "Condition": {
                   "ArnLike": {
                       "iam:PolicyARN": [
                           "arn:aws:iam::aws:policy/SageMakerStudio*",
                           "arn:aws:iam::*:policy/service-role/AmazonSageMaker*"
                       ]
                   }
               }
           }
       ]
   }

   ```

   - Add the following inline policy to your Login IAM role if you are choosing to use an existing role as the Execution IAM role:

   ```

   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "IAMPassRoleStatement",
               "Effect": "Allow",
               "Action": "iam:PassRole",
               "Resource": [
                   "arn:aws:iam::*:role/<execution_role>"
               ],
               "Condition": {
                   "StringEquals": {
                       "iam:PassedToService": [
                           "datazone.amazonaws.com"
                       ]
                   }
               }
           }
       ]
   }

   ```

5. Add the following inline policy to your Login and Execution IAM roles to enable KMS key
   usage.

```

{
    "Version": "2012-10-17",
    "Statement": [
          {
             "Sid": "KMSDescribePermissions",
             "Effect": "Allow",
             "Action": "kms:DescribeKey",
             "Resource": [
               "<KmsKeyArn>"
             ]
         },
         {
             "Sid": "KMSPermissions",
             "Effect": "Allow",
             "Action": [
                 "kms:Decrypt",
                 "kms:GenerateDataKey"
             ],
             "Resource": [
               "<KmsKeyArn>"
             ],
             "Condition": {
                 "ForAnyValue:StringEquals": {
                     "kms:EncryptionContextKeys": "aws:datazone:domainId"
                 }
             }
         }
     ]
 }

```

**Prepare the Execution IAM role for your IAM-based
domain:**

Amazon SageMaker Unified Studio provides two methods to configure the Execution IAM role (defined in [Overview of IAM-based domains](iam-based-domains-overview.md "iam-based-domains-overview.md")), first
you can choose to create a new Execution IAM role for your IAM-based domain. Choosing this
option will create a new role with default permissions and policies to administer your
IAM-based domain. This auto-created role will contain the following permission
details:

1. Managed policy: Data access and permission will be defined by
   `SageMakerStudioAdminIAMPermissiveExecutionPolicy`. It will not have the
   data access of the login
2. Add the following trust policy to allow Amazon SageMaker Unified Studio and related services to
   assume this Execution IAM role.

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "datazone.amazonaws.com",
                    "sagemaker.amazonaws.com",
                    "glue.amazonaws.com",
                    "bedrock.amazonaws.com",
                    "scheduler.amazonaws.com",
                    "lakeformation.amazonaws.com",
                    "airflow-serverless.amazonaws.com",
                    "athena.amazonaws.com",
                    "redshift.amazonaws.com",
                    "emr-serverless.amazonaws.com"
                ]
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession",
                "sts:SetContext",
                "sts:SetSourceIdentity"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "<domain_account>"
                }
            }
        }
    ]
}

```

3. AWS Lake Formation administrator: This role will be assigned as an administrator
   to enable data discovery and access management.
   Alternatively, Amazon SageMaker Unified Studio can use an existing IAM role as the Execution IAM role for your
   IAM-based domain. Choosing this option will require additional permissions and policies to
   be added to your existing IAM role to administer your IAM-based domain

1. Login to the IAM role with AWS IAM administrator privileges defined in the
   pre-requisites.
1. Navigate to the IAM console.
1. Choose **Add permission** followed by **Attach
   policy** and search for the managed policy
   `SageMakerStudioAdminIAMDefaultExecutionPolicy`. Select it to add it to
   your existing role.
1. Add the following inline policy to allow this role to pass itself to other services.

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PassRoleSelf",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": [
                "arn:aws:iam::*:role/<role_name>"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "sagemaker.amazonaws.com",
                        "glue.amazonaws.com",
                        "lakeformation.amazonaws.com",
                        "bedrock.amazonaws.com",
                        "scheduler.amazonaws.com",
                        "airflow-serverless.amazonaws.com",
                        "athena.amazonaws.com",
                        "redshift.amazonaws.com",
                        "emr-serverless.amazonaws.com"
                    ]
                }
            }
        }
    ]
}

```

5. Add the following trust policy to allow Amazon SageMaker Unified Studio and related services to
   assume this Execution IAM role.

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "datazone.amazonaws.com",
                    "sagemaker.amazonaws.com",
                    "glue.amazonaws.com",
                    "bedrock.amazonaws.com",
                    "scheduler.amazonaws.com",
                    "lakeformation.amazonaws.com",
                    "airflow-serverless.amazonaws.com",
                    "athena.amazonaws.com",
                    "redshift.amazonaws.com",
                    "emr-serverless.amazonaws.com"
                ]
            },
            "Action": [
                "sts:AssumeRole",
                "sts:TagSession",
                "sts:SetContext",
                "sts:SetSourceIdentity"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "<domain_account>"
                }
            }
        }
    ]
}

```

6.  Recommended: Navigate to AWS Lake Formation and grant this role AWS Lake
    Formation administrator permission to enable data discovery and access management within
    the domain.
    **Create Your Domain:**

1.  Login to the AWS Management Console and choose the Login IAM role (defined in
    [Overview of IAM-based domains](iam-based-domains-overview.md "iam-based-domains-overview.md")) you created for the Administrator.
1.  Navigate to the Amazon SageMaker console and use the region selector to choose your
    desired AWS Region.
1.  Choose **Get started** from the Amazon SageMaker Unified Studio section.
1.  You should see a screen with the title **Set up
    Amazon SageMaker Unified Studio**.
1.  Choose and select the Execution IAM Role for the Admin
1.  **Setup S3 table integration with AWS analytics services**. This
    option is enabled by default, and will allow Amazon SageMaker Unified Studio to access table buckets,
    integrate the table buckets with AWS Analytics services using AWS Glue and AWS
    Lake Formation. [Learn more](../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-aws.md").
1.  In the **Data encryption** section, configure your encryption
    preferences:

        * Leave **Customize encryption settings (advanced)** unchecked to
         use AWS-managed encryption
        * Check **Customize encryption settings (advanced)** to specify a
         custom AWS KMS key

    If using custom encryption, see [Manage data encryption in
    IAM-based domains](manage-data-encryption-iam-based-domains.md "manage-data-encryption-iam-based-domains.md")

1.  Choose **Set up** to begin the domain creation process.
1.  Monitor the setup progress in the **Setting up Amazon SageMaker Unified Studio**
    dialog. The process typically takes 1-2 minutes to complete.
1.  Once the setup is completed, project will automatically be created using the same
    Execution role. Then you will be redirected to the Administrative pages for managing the
    domain. See [Access the Domain Administration
    Page](access-domain-administration-page.md "access-domain-administration-page.md") for details.
1.  You can also access the project associated with your Login IAM role by choosing on
    the first project. See **Navigating within Amazon SageMaker Unified Studio** for
    details.

###### Note

To add more IAM roles to the IAM based domain, you can create new projects using the
IAM role as the Login IAM role. See additional details to setup [Projects in IAM-based domains](projects-iam-based-domains.md "projects-iam-based-domains.md")
.

Amazon SageMaker Unified Studio also supports domains configured with AWS IAM Identity Center (IdC).
Additional details to setup an Identity Center based domain are available in [Identity Center-based domains](identity-center-based-domains.md "identity-center-based-domains.md").
