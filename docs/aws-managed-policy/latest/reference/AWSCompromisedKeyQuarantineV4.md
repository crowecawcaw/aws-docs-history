

# AWSCompromisedKeyQuarantineV4
<a name="AWSCompromisedKeyQuarantineV4"></a>

**Description**: Denies access to certain actions, applied by AWS in the event that an IAM user's credentials have been compromised or exposed publicly. The policy aims to limit the potential damage that may be caused by fraud-related activity leading to unauthorized charges. Do NOT remove this policy. Instead, please follow the instructions specified in the support case created for you regarding this event. AWSCompromisedKeyQuarantineV4 is an AWS managed policy.

`AWSCompromisedKeyQuarantineV4` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCompromisedKeyQuarantineV4-how-to-use"></a>

You can attach `AWSCompromisedKeyQuarantineV4` to your users, groups, and roles.

## Policy details
<a name="AWSCompromisedKeyQuarantineV4-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 06, 2026, 00:37 UTC 
+ **Edited time:** November 06, 2026, 00:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSCompromisedKeyQuarantineV4`

## Policy version
<a name="AWSCompromisedKeyQuarantineV4-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCompromisedKeyQuarantineV4-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Deny",
      "Action" : [
        "cloudtrail:LookupEvents",
        "ec2:RequestSpotInstances",
        "ec2:RunInstances",
        "ec2:StartInstances",
        "ec2:PurchaseReservedInstancesOffering",
        "ec2:AcceptReservedInstancesExchangeQuote",
        "ec2:CreateReservedInstancesListing",
        "iam:AddUserToGroup",
        "iam:AttachGroupPolicy",
        "iam:AttachRolePolicy",
        "iam:AttachUserPolicy",
        "iam:ChangePassword",
        "iam:CreateAccessKey",
        "iam:CreateInstanceProfile",
        "iam:CreateLoginProfile",
        "iam:CreatePolicyVersion",
        "iam:CreateRole",
        "iam:CreateUser",
        "iam:DetachUserPolicy",
        "iam:PassRole",
        "iam:PutGroupPolicy",
        "iam:PutRolePolicy",
        "iam:PutUserPermissionsBoundary",
        "iam:PutUserPolicy",
        "iam:SetDefaultPolicyVersion",
        "iam:UpdateAccessKey",
        "iam:UpdateAccountPasswordPolicy",
        "iam:UpdateAssumeRolePolicy",
        "iam:UpdateLoginProfile",
        "iam:UpdateUser",
        "iam:DeleteRole",
        "iam:DeleteAccessKey",
        "iam:ListUsers",
        "lambda:AddLayerVersionPermission",
        "lambda:AddPermission",
        "lambda:CreateFunction",
        "lambda:GetPolicy",
        "lambda:ListTags",
        "lambda:PutProvisionedConcurrencyConfig",
        "lambda:TagResource",
        "lambda:UntagResource",
        "lambda:UpdateFunctionCode",
        "lambda:GetEventSourceMapping",
        "lightsail:Create*",
        "lightsail:Delete*",
        "lightsail:DownloadDefaultKeyPair",
        "lightsail:GetInstanceAccessDetails",
        "lightsail:Start*",
        "lightsail:Update*",
        "organizations:CreateAccount",
        "organizations:CreateOrganization",
        "organizations:InviteAccountToOrganization",
        "organizations:LeaveOrganization",
        "organizations:AcceptHandshake",
        "s3:DeleteBucket",
        "s3:DeleteObject",
        "s3:DeleteObjectVersion",
        "s3:PutLifecycleConfiguration",
        "s3:PutBucketAcl",
        "s3:PutBucketOwnershipControls",
        "s3:DeleteBucketPolicy",
        "s3:ObjectOwnerOverrideToBucketOwner",
        "s3:PutAccountPublicAccessBlock",
        "s3:PutBucketPolicy",
        "s3:ListAllMyBuckets",
        "s3:CreateBucket",
        "s3:PutBucketCors",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:PutEncryptionConfiguration",
        "savingsplans:CreateSavingsPlan",
        "ecs:CreateService",
        "ecs:CreateCluster",
        "ecs:RegisterTaskDefinition",
        "ecr:GetAuthorizationToken",
        "bedrock:CreateModelInvocationJob",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:CreateFoundationModelAgreement",
        "bedrock:PutFoundationModelEntitlement",
        "bedrock:InvokeModel",
        "sagemaker:CreateEndpointConfig",
        "sagemaker:CreateProcessingJob",
        "sts:GetSessionToken",
        "sts:GetFederationToken",
        "amplify:CreateDeployment",
        "amplify:CreateBackendEnvironment",
        "codebuild:CreateProject",
        "glue:CreateJob",
        "sns:GetSMSAttributes",
        "mediapackagev2:CreateChannel",
        "logs:PutLogEvents",
        "xray:CallWithBearerToken",
        "ssm:SendCommand",
        "ssm:StartSession",
        "autoscaling:CreateAutoScalingGroup",
        "autoscaling:UpdateAutoScalingGroup",
        "autoscaling:SetDesiredCapacity",
        "secretsmanager:GetSecretValue",
        "ssm:GetParameter*",
        "kms:CreateKey",
        "kms:CreateAlias",
        "kms:CreateCustomKeyStore",
        "kms:Enable*",
        "kms:Put*",
        "kms:Update*",
        "kms:Revoke*",
        "kms:Disable*",
        "kms:Delete*",
        "kms:TagResource",
        "kms:UntagResource",
        "kms:Replicate*",
        "kms:Connect*",
        "kms:Cancel*",
        "kms:Retire*",
        "kms:Schedule*",
        "kms:Rotate*",
        "dynamodb:CreateTable",
        "lambda:InvokeFunction",
        "ses:Send*",
        "ses:Create*",
        "ses:Get*",
        "ses:List*",
        "ses:Delete*",
        "ses:Put*",
        "ses:Update*",
        "ses:TagResource",
        "ses:UntagResource",
        "ses:Set*",
        "ses:Describe*",
        "sns:Publish",
        "cloudtrail:StopLogging",
        "cloudtrail:DeleteTrail",
        "s3:PutBucketVersioning",
        "s3:PutBucketObjectLockConfiguration",
        "s3:PutObjectRetention",
        "s3:PutObjectLegalHold",
        "backup:DeleteRecoveryPoint",
        "backup:DeleteBackupVault",
        "rds:DeleteDBSnapshot",
        "cloudformation:DeleteStack",
        "iam:CreateServiceSpecificCredential",
        "iam:ResetServiceSpecificCredential",
        "sts:AssumeRole",
        "ecs:RunTask",
        "ecs:UpdateService",
        "apprunner:CreateService",
        "apprunner:UpdateService",
        "apprunner:StartDeployment",
        "apprunner:ResumeService",
        "apprunner:TagResource",
        "apprunner:UntagResource",
        "sagemaker:CreateTrainingJob",
        "sagemaker:CreateEndpoint",
        "bedrock-mantle:CreateInference",
        "aws-marketplace:Subscribe",
        "aws-marketplace:AcceptAgreementApprovalRequest",
        "apprunner:DeleteService",
        "ecs:ExecuteCommand",
        "ecs:StartTask",
        "ecs:CreateTaskSet",
        "ecs:UpdateTaskSet",
        "ecs:UpdateServicePrimaryTaskSet",
        "ecs:CreateExpressGatewayService",
        "ecs:UpdateExpressGatewayService",
        "ecs:RegisterDaemonTaskDefinition",
        "ecs:CreateDaemon",
        "ecs:UpdateDaemon",
        "application-autoscaling:RegisterScalableTarget",
        "application-autoscaling:PutScalingPolicy",
        "sagemaker:CreateNotebookInstance",
        "sagemaker:CreateTransformJob",
        "autoscaling:DeleteAutoScalingGroup",
        "ec2:CreateLaunchTemplateVersion",
        "ec2:ModifyLaunchTemplate",
        "sagemaker:CreateCluster",
        "secretsmanager:PutResourcePolicy",
        "sagemaker:CreateHyperParameterTuningJob",
        "sagemaker:CreateCompilationJob",
        "sagemaker:CreateOptimizationJob",
        "sagemaker:CreateApp",
        "sagemaker:CreateMlflowTrackingServer",
        "sagemaker:CreatePartnerApp",
        "sagemaker:CreateJob",
        "ssm:ResumeSession",
        "lambda:InvokeFunctionUrl",
        "lambda:InvokeAsync",
        "ssm:PutParameter",
        "ssm:DescribeParameters",
        "ssm:DeleteParameter",
        "ssm:DeleteParameters",
        "ssm:PutResourcePolicy",
        "secretsmanager:TagResource",
        "secretsmanager:UntagResource",
        "bedrock-mantle:CallWithBearerToken",
        "bedrock:CallWithBearerToken",
        "lambda:CreateFunctionUrlConfig",
        "lambda:UpdateFunctionUrlConfig",
        "lambda:CreateEventSourceMapping",
        "lambda:UpdateEventSourceMapping",
        "lambda:InvokeWebFunctionEndpoint",
        "lambda:CreateWebFunction",
        "lambda:CreateWebFunctionRevision",
        "lambda:CreateWebFunctionEndpoint",
        "lambda:UpdateWebFunctionEndpoint"
      ],
      "Resource" : [
        "*"
      ]
    },
    {
      "Effect" : "Deny",
      "Action" : [
        "kms:CreateGrant"
      ],
      "Resource" : "*",
      "Condition" : {
        "Null" : {
          "kms:ViaService" : "true"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSCompromisedKeyQuarantineV4-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)