

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Prerequisites to use AWS Microservice Extractor for .NET
<a name="microservice-extractor-prerequisites"></a>

**Topics**
+ [Prerequisites for analysis and extraction](#microservice-extractor-prerequisites-analysis-extraction)
+ [Required IAM policies](#microservice-extractor-iam)

## Prerequisites for analysis and extraction of monolithic application
<a name="microservice-extractor-prerequisites-analysis-extraction"></a>

To use Microservice Extractor to analyze and extract a monolithic application to deploy into smaller services, you must have the following:
+ A valid AWS CLI profile to publish metrics. For information about how to configure an AWS CLI profile, see [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles).
+ A monolithic application that must be one of the following:
  + A .NET Framework ASP.NET web service application hosted on IIS with the .NET Framework developer pack installed.
  + A .NET Core ASP.NET web service application with the developer pack installed.
+ The ability to build the application solution with [MSBuild](https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild).
+ One of the following operating systems for analyzing the application and creating the visualization:
  + Windows 10 or later
  + Windows Server 2016 or later
+ For the application analysis, you must have:
  + .NET Framework version 4 or later, or .NET Core version 3.1 or later compatibility with source code solution.
  + 10 GB minimum of free disk space, in addition to the size of your application.
  + 8 GB minimum of available memory.
  + Compute power equivalent to or greater than that of an Intel Core i3 3-GHz processor.
+ For the extraction, you must have:
  + .NET Framework version 4.5 or later, or .NET Core version 3.1 or later compatibility with source code solution.
  + 20 GB minimum of free disk space, in addition to twice the size of your application.

## Required AWS Identity and Access Management policies
<a name="microservice-extractor-iam"></a>

To perform certain operations using AWS Microservice Extractor for .NET, your user must have the necessary permissions. This section includes the policies that your user must have, and also instructions for granting permissions to the user.

You must use a valid AWS CLI profile to use the assessment tool and run the commands to complete an extraction. For information about how to configure your AWS CLI profile, see [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles).

### How to provide access to your user
<a name="microservice-extractor-iam-how-to-attach-policy"></a>

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

### Permissions to use the AWS Microservice Extractor for .NET assessment tool
<a name="microservice-extractor-iam-assessment"></a>

To use the AWS Microservice Extractor for .NET assessment tool, you must create an IAM policy that includes the following permissions. To view the type of application data collected by Microservice Extractor, see [Information collected](microservice-extractor-information-collected.md).

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ApplicationTransformationAccess",
            "Effect": "Allow",
            "Action": [
                "application-transformation:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "KMSPermissions",
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey",
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:CreateGrant",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:::*",
            "Condition": {
                "ForAnyValue:StringLike": {
                    "kms:ResourceAliases": "alias/application-transformation*"
                }
            }
        },
        {
            "Sid": "S3Access",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:CreateBucket",
                "s3:ListBucket",
                "s3:PutBucketOwnershipControls",
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        }
    ]
}
```