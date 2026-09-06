

# `AWSSupport-ValidateMWAADependencies`
<a name="automation-awssupport-validatemwaadependencies"></a>

 **Description** 

The `AWSSupport-ValidateMWAADependencies` runbook validates Amazon Managed Workflows for Apache Airflow (Amazon MWAA) environment Python dependencies. It does this by running the amazon-mwaa-docker-images test command on an Amazon EC2 instance. This validates that your Python packages work with your target Airflow version. It also packages wheel files for environments without public network access.

 **Use cases:** 
+ **Dependency Validation**: Verify that dependencies (requirements file) with default or custom constraints are compatible before upgrading or downgrading the Amazon MWAA environment to a specific Airflow version.
+ **Package Wheel Files**: Generate packaged wheel files in `plugins.zip` for environments that lack public network access.

**Important**  
This automation incurs additional AWS costs. The automation provisions a `t3.large` Amazon EC2 instance with a 50 GB `gp3` volume in your account via CloudFormation. This instance fetches the amazon-mwaa-docker-images repository, validates dependencies, and packages wheel files. The instance is automatically terminated after execution.

**Note**  
If unsupported Python modules are detected: For versioned modules, the specific version is updated or removed, and the test command reruns. For unversioned modules, the module is commented out, and the test command reruns. This process continues until all modules are supported or the maximum retry limit (20 attempts) is reached.
Wheel file packaging executes only when the requirements file contains a `--find-links` directive pointing to a plugin path and the `--no-index` flag.
Requirements file and custom constraints file must be stored in the Amazon S3 bucket specified in the input parameters. All generated files including the updated `requirements.txt` file, `plugins.zip` file (if applicable), logs and the report are uploaded to the same Amazon S3 bucket.
This runbook only supports Airflow version 2.9.2 and later. If validation for a previous version is required, use aws-mwaa-local-runner.

 **How does it work?** 

The runbook performs the following steps:
+ Checks if the target Amazon S3 bucket potentially grants read or write public access to its objects.
+ Validates the input parameters including IAM permissions, Amazon S3 bucket location and ownership, file existence, target Airflow version, and subnet public network access.
+ Retrieves the latest Amazon Linux 2023 AMI.
+ Creates a CloudFormation stack including an IAM role, an instance profile, a security group and an Amazon MWAA runner Amazon EC2 instance.
+ Waits for the Amazon EC2 instance to initialize.
+ Runs commands on the instance to validate the Amazon MWAA dependencies and download wheel files if required.
+ Cleans up the created resources by deleting the CloudFormation stack.
+ Generates the final report and uploads it to the Amazon S3 bucket.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ValidateMWAADependencies) 

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ cloudformation:CreateStack
+ cloudformation:DeleteStack
+ cloudformation:DescribeStacks
+ ec2:AuthorizeSecurityGroupEgress
+ ec2:CreateSecurityGroup
+ ec2:CreateTags
+ ec2:DeleteSecurityGroup
+ ec2:DescribeImages
+ ec2:DescribeInstances
+ ec2:DescribeInstanceStatus
+ ec2:DescribeRouteTables
+ ec2:DescribeSecurityGroups
+ ec2:DescribeSubnets
+ ec2:DescribeVpcs
+ ec2:ModifyInstanceAttribute
+ ec2:RevokeSecurityGroupEgress
+ ec2:RunInstances
+ ec2:TerminateInstances
+ iam:AddRoleToInstanceProfile
+ iam:AttachRolePolicy
+ iam:CreateInstanceProfile
+ iam:CreateRole
+ iam:DeleteInstanceProfile
+ iam:DeleteRole
+ iam:DeleteRolePolicy
+ iam:DetachRolePolicy
+ iam:GetInstanceProfile
+ iam:GetRole
+ iam:GetRolePolicy
+ iam:PassRole
+ iam:PutRolePolicy
+ iam:RemoveRoleFromInstanceProfile
+ iam:SimulatePrincipalPolicy
+ iam:TagRole
+ s3:GetAccountPublicAccessBlock
+ s3:GetBucketAcl
+ s3:GetBucketLocation
+ s3:GetBucketPolicyStatus
+ s3:GetBucketPublicAccessBlock
+ s3:GetEncryptionConfiguration
+ s3:GetObject
+ s3:ListBucket
+ s3:PutObject
+ ssm:DescribeInstanceInformation
+ ssm:GetAutomationExecution
+ ssm:GetCommandInvocation
+ ssm:GetParameter
+ ssm:ListCommandInvocations
+ ssm:ListCommands
+ ssm:SendCommand
+ ssm:StartAutomationExecution
+ sts:GetCallerIdentity

Example Policy: 

```
        {
            "Version": "2012-10-17"		 	 	 ,
            "Statement": [
                {
                    "Sid": "ReadOnlyPermissions",
                    "Effect": "Allow",
                    "Action": [
                        "ec2:DescribeInstances",
                        "ec2:DescribeInstanceStatus",
                        "ec2:DescribeImages",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "ec2:DescribeRouteTables",
                        "ec2:DescribeSecurityGroups",
                        "iam:SimulatePrincipalPolicy",
                        "iam:GetRolePolicy",
                        "s3:GetAccountPublicAccessBlock",
                        "ssm:GetParameter"
                    ],
                    "Resource": "*"
                },
                {
                    "Sid": "CloudFormationPermissions",
                    "Effect": "Allow",
                    "Action": [
                        "cloudformation:CreateStack",
                        "cloudformation:DeleteStack",
                        "cloudformation:DescribeStacks"
                    ],
                    "Resource": "arn:<aws|aws-cn|aws-us-gov>:cloudformation:*:*:stack/MWAA-Runner-*"
                },
                {
                    "Sid": "MWAARunnerInstancesEC2Permissions",
                    "Effect": "Allow",
                    "Action": [
                        "ec2:TerminateInstances",
                        "ec2:ModifyInstanceAttribute"
                    ],
                    "Resource": "*",
                    "Condition": {
                        "StringLike": {
                            "ec2:ResourceTag/Name": "mwaa-runner-*"
                        }
                    }
                },
                {
                    "Sid": "EC2CreateTagsOnMWAARunnerResources",
                    "Effect": "Allow",
                    "Action": "ec2:CreateTags",
                    "Resource": "*",
                    "Condition": {
                        "StringLike": {
                            "aws:RequestTag/Name": "mwaa-runner-*"
                        }
                    }
                },
                {
                    "Sid": "EC2CreateTagsOnStackCreation",
                    "Effect": "Allow",
                    "Action": "ec2:CreateTags",
                    "Resource": "*",
                    "Condition": {
                        "StringEquals": {
                            "ec2:CreateAction": "RunInstances"
                        }
                    }
                },
                {
                    "Sid": "MWAAInstanceRoleIAMPermissions",
                    "Effect": "Allow",
                    "Action": [
                        "iam:AttachRolePolicy",
                        "iam:CreateRole",
                        "iam:DeleteRole",
                        "iam:DetachRolePolicy",
                        "iam:GetRole",
                        "iam:PutRolePolicy",
                        "iam:DeleteRolePolicy",
                        "iam:GetRolePolicy",
                        "iam:TagRole"
                    ],
                    "Resource": "arn:<aws|aws-cn|aws-us-gov>:iam::*:role/mwaa-instance-role-*"
                },
                {
                    "Sid": "MWAAInstanceProfileIAMPermissions",
                    "Effect": "Allow",
                    "Action": [
                        "iam:CreateInstanceProfile",
                        "iam:DeleteInstanceProfile",
                        "iam:GetInstanceProfile",
                        "iam:AddRoleToInstanceProfile",
                        "iam:RemoveRoleFromInstanceProfile"
                    ],
                    "Resource": "arn:<aws|aws-cn|aws-us-gov>:iam::*:instance-profile/mwaa-instance-profile-*"
                },
                {
                    "Sid": "S3AccessPermissions",
                    "Effect": "Allow",
                    "Action": [
                        "s3:GetBucketAcl",
                        "s3:GetBucketLocation",
                        "s3:GetBucketPolicyStatus",
                        "s3:GetBucketPublicAccessBlock",
                        "s3:GetEncryptionConfiguration",
                        "s3:GetObject",
                        "s3:ListBucket",
                        "s3:PutObject"
                    ],
                    "Resource": [
                        "arn:<aws|aws-cn|aws-us-gov>:s3:::<S3BucketName>",
                        "arn:<aws|aws-cn|aws-us-gov>:s3:::<S3BucketName>/*"
                    ]
                },
                {
                    "Sid": "SSMAutomationExecution",
                    "Effect": "Allow",
                    "Action": [
                        "ssm:GetAutomationExecution",
                        "ssm:StartAutomationExecution"
                    ],
                    "Resource": [
                        "arn:<aws|aws-cn|aws-us-gov>:ssm:*:*:automation-definition/AWSSupport-ValidateMWAADependencies:*",
                        "arn:<aws|aws-cn|aws-us-gov>:ssm:*:*:automation-execution/*"
                    ]
                },
                {
                    "Sid": "OtherMutationPermissions",
                    "Effect": "Allow",
                    "Action": [
                        "ec2:CreateSecurityGroup",
                        "ec2:DeleteSecurityGroup",
                        "ec2:AuthorizeSecurityGroupEgress",
                        "ec2:RevokeSecurityGroupEgress",
                        "ec2:RunInstances",
                        "s3:GetAccountPublicAccessBlock",
                        "ssm:GetCommandInvocation",
                        "ssm:ListCommands",
                        "ssm:ListCommandInvocations",
                        "ssm:DescribeInstanceInformation",
                        "ssm:SendCommand",
                        "sts:GetCallerIdentity"
                    ],
                    "Resource": "*"
                },
                {
                    "Sid": "PassRolePermission",
                    "Effect": "Allow",
                    "Action": "iam:PassRole",
                    "Resource": "arn:<aws|aws-cn|aws-us-gov>:iam::*:role/mwaa-instance-role-*",
                    "Condition": {
                        "StringEquals": {
                            "iam:PassedToService": "ec2.amazonaws.com"
                        }
                    }
                }
            ]
        }
```

 **Instructions** 

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-ValidateMWAADependencies`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ValidateMWAADependencies/description) in Systems Manager under the Documents section.

1. Choose **Execute automation**. Ensure your IAM role has the required permissions listed in the preceding permissions section before executing.

1. For the input parameters, enter the following:
   + **S3BucketName (Required):**

     Enter the name of the Amazon S3 bucket in your account where you want to upload the troubleshooting logs. Make sure the bucket policy does not grant unnecessary read/write permissions to parties that do not need access to the collected logs.
   + **RequirementsFilePath (Required):**

     The Amazon S3 object key of the requirements file in the Amazon S3 bucket. Must end with the `.txt` extension.
   + **ConstraintsFilePath (Optional):**

     The Amazon S3 object key of the custom constraints file in the Amazon S3 bucket. Must end with the `.txt` extension if provided.
   + **TargetAirflowVersion (Required):**

     The Airflow version to use for validating the dependencies. Target version must be supported by Amazon MWAA. Format: `X.Y.Z` (e.g., `2.9.2`).
   + **SubnetId (Required):**

     The subnet that has public network access to launch the Amazon MWAA runner Amazon EC2 instance. Format: `subnet-xxxxxxxxx`.
   + **AutomationAssumeRole (Optional):**

     The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
   + **AcknowledgeIAMPolicyWarnings (Required):**

     This runbook pre-checks whether your IAM role has the required permissions using SimulatePrincipalPolicy. This check may produce inaccurate results if your policy uses Conditions or resource-level restrictions. Select `YES` to acknowledge this and proceed.

1. Choose **Execute**.

1. The automation initiates.

1. The document performs the following steps:
   + **`GetBucketPublicStatus`**:

     Checks if the target Amazon S3 bucket potentially grants read or write public access to its objects.
   + **`ValidateInput`**:

     Validates the input parameters including IAM permissions, Amazon S3 bucket location and ownership, file existence, target Airflow version, and subnet public network access.
   + **`BranchOnValidationResult`**:

     Branches the workflow based on whether the input parameters are valid.
   + **`GetLatestAMI`**:

     Retrieves the latest AMI for Amazon Linux 2023 image.
   + **`CreateMWAARunnerStack`**:

     Creates a CloudFormation stack including an IAM role, an instance profile, a security group and an Amazon MWAA runner Amazon EC2 instance.
   + **`GetInstanceId`**:

     Retrieves the Amazon EC2 instance ID from the CloudFormation stack output.
   + **`WaitForInstanceInitialization`**:

     Checks the Amazon EC2 instance status and waits for the initialization.
   + **`RunCommands`**:

     Runs commands on the instance to validate the Amazon MWAA dependencies and download wheel files if required.
   + **`Cleanup`**:

     Cleans up the created resources by deleting the CloudFormation stack.
   + **`GenerateReport`**:

     Generates the final report based on previous steps' output and uploads the report to the Amazon S3 bucket.

1. After the automation completes, review the Outputs section for detailed execution results.

**References**

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ValidateMWAADependencies/description)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/)