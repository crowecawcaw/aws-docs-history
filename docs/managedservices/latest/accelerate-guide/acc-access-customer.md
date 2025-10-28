# Permissions to use AMS features

To allow your users to read and configure AMS Accelerate capabilities, like accessing
the AMS Console or configuring backups, you must grant explicit permissions to their IAM
roles to perform those actions. The following AWS CloudFormation template contains the policies required
to read and configure services associated with AMS so you can assign them to your IAM
roles. They are designed to closely align with common job responsibilities in the IT industry,
where Administrator or Read-Only permissions are required; however, if you need to
grant different permissions to users, you can edit the policy to include or exclude specific
permissions. You can also create your own custom policy.

The template provides two policies. The `AMSAccelerateAdminAccess` policy is meant to be used for setting up and operating
the AMS Accelerate components. This policy is typically assumed by an IT admin and grants permissions to configure AMS
features such as patching and backups. The `AMSAccelerateReadOnly` grants minimum required permissions for viewing AMS Accelerate-related resources.

```
AWSTemplateFormatVersion: 2010-09-09
Description: AMSAccelerateCustomerAccessPolicies

Resources:
  AMSAccelerateAdminAccess:
    Type: 'AWS::IAM::ManagedPolicy'
    Properties:
      ManagedPolicyName: AMSAccelerateAdminAccess
      Path: /
      PolicyDocument:
        Fn::Sub:
        - |
          {
            "Version": "2012-10-17",
            "Statement": [
              {
                 "Sid": "AmsSelfServiceReport",
                 "Effect": "Allow",
                 "Action": "amsssrv:*",
                 "Resource": "*"
              },
              {
                "Sid": "AmsBackupPolicy",
                "Effect": "Allow",
                "Action": "iam:PassRole",
                "Resource": "arn:aws:iam::${`AWS::AccountId`}:role/ams-backup-iam-role"
              },
              {
                "Sid": "AmsChangeRecordKMSPolicy",
                "Effect": "Allow",
                "Action": [
                  "kms:Encrypt",
                  "kms:Decrypt",
                  "kms:GenerateDataKey"
                ],
                "Resource": [
                  "arn:aws:kms:${`AWS::Region`}:${`AWS::AccountId`}:key/*"
                ],
                "Condition": {
                  "ForAnyValue:StringLike": {
                    "kms:ResourceAliases": "alias/AMSCloudTrailLogManagement"
                  }
                }
              },
              {
                "Sid": "AmsChangeRecordAthenaReadPolicy",
                "Effect": "Allow",
                "Action": [
                  "athena:BatchGetNamedQuery",
                  "athena:Get*",
                  "athena:List*",
                  "athena:StartQueryExecution",
                  "athena:UpdateWorkGroup",
                  "glue:GetDatabase*",
                  "glue:GetTable*",
                  "s3:GetAccountPublicAccessBlock",
                  "s3:ListAccessPoints",
                  "s3:ListAllMyBuckets"
                ],
                "Resource": "*"
              },
              {
                "Sid": "AmsChangeRecordS3ReadPolicy",
                "Effect": "Allow",
                "Action": [
                  "s3:Get*",
                  "s3:List*"
                ],
                "Resource": [
                  "arn:aws:s3:::ams-a${`AWS::AccountId`}-athena-results-${`AWS::Region`}",
                  "arn:aws:s3:::ams-a${`AWS::AccountId`}-athena-results-${`AWS::Region`}/*",
                  "arn:aws:s3:::ams-a${`AWS::AccountId`}-cloudtrail-${`AWS::Region`}",
                  "arn:aws:s3:::ams-a${`AWS::AccountId`}-cloudtrail-${`AWS::Region`}/*"
                ]
              },
              {
                "Sid": "AmsChangeRecordS3WritePolicy",
                "Effect": "Allow",
                "Action": [
                  "s3:PutObject",
                  "s3:PutObjectLegalHold",
                  "s3:PutObjectRetention"

                ],
                "Resource": [
                  "arn:aws:s3:::ams-a${`AWS::AccountId`}-athena-results-${`AWS::Region`}/*"
                ]
              },
              {
                "Sid": "MaciePolicy",
                "Effect": "Allow",
                "Action": [
                  "macie2:GetFindingStatistics"
                ],
                "Resource": "*"
              },
              {
                "Sid": "GuardDutyPolicy",
                "Effect": "Allow",
                "Action": [
                  "guardduty:GetFindingsStatistics",
                  "guardduty:ListDetectors"
                ],
                "Resource": "*"
              },
              {
                "Sid": "SupportPolicy",
                "Effect": "Allow",
                "Action": "support:*",
                "Resource": "*"
              },
              {
                "Sid": "ConfigPolicy",
                "Effect": "Allow",
                "Action": [
                  "config:Get*",
                  "config:Describe*",
                  "config:Deliver*",
                  "config:List*",
                  "config:StartConfigRulesEvaluation"
                ],
                "Resource": "*"
              },
              {
                "Sid": "AppConfigReadPolicy",
                "Effect": "Allow",
                "Action": [
                  "appconfig:List*",
                  "appconfig:Get*"
                ],
                "Resource": "*"
              },
              {
                "Sid": "AppConfigPolicy",
                "Effect": "Allow",
                "Action": [
                  "appconfig:StartDeployment",
                  "appconfig:StopDeployment",
                  "appconfig:CreateHostedConfigurationVersion",
                  "appconfig:ValidateConfiguration"
                ],
                "Resource": [
                  "arn:aws:appconfig:*:${`AWS::AccountId`}:application/${`AMSAlarmManagerConfigurationApplicationId`}",
                  "arn:aws:appconfig:*:${`AWS::AccountId`}:application/${`AMSAlarmManagerConfigurationApplicationId`}/configurationprofile/${`AMSAlarmManagerConfigurationCustomerManagedAlarmsProfileID`}",
                  "arn:aws:appconfig:*:${`AWS::AccountId`}:application/${`AMSAlarmManagerConfigurationApplicationId`}/environment/*",
                  "arn:aws:appconfig:*:${`AWS::AccountId`}:application/${`AMSResourceTaggerConfigurationApplicationId`}",
                  "arn:aws:appconfig:*:${`AWS::AccountId`}:application/${`AMSResourceTaggerConfigurationApplicationId`}/configurationprofile/${`AMSResourceTaggerConfigurationCustomerManagedTagsProfileID`}",
                  "arn:aws:appconfig:*:${`AWS::AccountId`}:application/${`AMSResourceTaggerConfigurationApplicationId`}/environment/*",
                  "arn:aws:appconfig:*:${`AWS::AccountId`}:deploymentstrategy/*"
                ]
              },
              {
                "Sid": "CloudFormationStacksPolicy",
                "Effect": "Allow",
                "Action": [
                  "cloudformation:DescribeStacks"
                ],
                "Resource": "*"
              },
              {
                "Sid": "EC2Policy",
                "Action": [
                  "ec2:DescribeInstances"
                ],
                "Effect": "Allow",
                "Resource": "*"
              },
              {
                "Sid": "SSMPolicy",
                "Effect": "Allow",
                "Action": [
                  "ssm:AddTagsToResource",
                  "ssm:CancelCommand",
                  "ssm:CancelMaintenanceWindowExecution",
                  "ssm:CreateAssociation",
                  "ssm:CreateAssociationBatch",
                  "ssm:CreateMaintenanceWindow",
                  "ssm:CreateOpsItem",
                  "ssm:CreatePatchBaseline",
                  "ssm:DeleteAssociation",
                  "ssm:DeleteMaintenanceWindow",
                  "ssm:DeletePatchBaseline",
                  "ssm:DeregisterPatchBaselineForPatchGroup",
                  "ssm:DeregisterTargetFromMaintenanceWindow",
                  "ssm:DeregisterTaskFromMaintenanceWindow",
                  "ssm:Describe*",
                  "ssm:Get*",
                  "ssm:List*",
                  "ssm:PutConfigurePackageResult",
                  "ssm:RegisterDefaultPatchBaseline",
                  "ssm:RegisterPatchBaselineForPatchGroup",
                  "ssm:RegisterTargetWithMaintenanceWindow",
                  "ssm:RegisterTaskWithMaintenanceWindow",
                  "ssm:RemoveTagsFromResource",
                  "ssm:SendCommand",
                  "ssm:StartAssociationsOnce",
                  "ssm:StartAutomationExecution",
                  "ssm:StartSession",
                  "ssm:StopAutomationExecution",
                  "ssm:TerminateSession",
                  "ssm:UpdateAssociation",
                  "ssm:UpdateAssociationStatus",
                  "ssm:UpdateMaintenanceWindow",
                  "ssm:UpdateMaintenanceWindowTarget",
                  "ssm:UpdateMaintenanceWindowTask",
                  "ssm:UpdateOpsItem",
                  "ssm:UpdatePatchBaseline"
                ],
                "Resource": "*"
              },
              {
                "Sid": "AmsPatchRestrictAMSResources",
                "Effect": "Deny",
                "Action": [
                  "ssm:DeletePatchBaseline",
                  "ssm:UpdatePatchBaseline"
                ],
                "Resource": [
                  "arn:aws:ssm:${`AWS::Region`}:${`AWS::AccountId`}:patchbaseline/*"
                ],
                "Condition": {
                  "StringLike": {
                    "aws:ResourceTag/ams:resourceOwner": "*"
                  }
                }
              },
              {
                "Sid": "AmsPatchRestrictAmsTags",
                "Effect": "Deny",
                "Action": [
                  "ssm:AddTagsToResource",
                  "ssm:RemoveTagsFromResource"
                ],
                "Resource": "*",
                "Condition": {
                  "ForAnyValue:StringLike": {
                    "aws:TagKeys": [
                      "AMS*",
                      "Ams*",
                      "ams*"
                    ]
                  }
                }
              },
              {
                "Sid": "TagReadPolicy",
                "Effect": "Allow",
                "Action": [
                  "tag:GetResources",
                  "tag:GetTagKeys"
                ],
                "Resource": "*"
              },
              {
                "Sid": "CloudtrailReadPolicy",
                "Effect": "Allow",
                "Action": [
                  "cloudtrail:DescribeTrails",
                  "cloudtrail:GetTrailStatus",
                  "cloudtrail:LookupEvents"
                ],
                "Resource": "*"
              },
              {
                "Sid": "EventBridgePolicy",
                "Effect": "Allow",
                "Action": [
                  "events:Describe*",
                  "events:List*",
                  "events:TestEventPattern"
                ],
                "Resource": "*"
              },
              {
                "Sid": "IAMReadOnlyPolicy",
                "Action": [
                    "iam:ListRoles",
                    "iam:GetRole"
                ],
                "Effect": "Allow",
                "Resource": "*"
              },
              {
                "Sid": "AmsResourceSchedulerPassRolePolicy",
                "Effect": "Allow",
                "Action": "iam:PassRole",
                "Resource": "arn:aws:iam::${AWS::AccountId}:role/ams_resource_scheduler_ssm_automation_role",
                "Condition": {
                    "StringEquals": {
                        "iam:PassedToService": "ssm.amazonaws.com"
                    }
                }
              }
            ]
          }
        - AMSAlarmManagerConfigurationApplicationId: !ImportValue "AMS-Alarm-Manager-Configuration-ApplicationId"
          AMSAlarmManagerConfigurationCustomerManagedAlarmsProfileID: !ImportValue "AMS-Alarm-Manager-Configuration-CustomerManagedAlarms-ProfileID"
          AMSResourceTaggerConfigurationApplicationId: !ImportValue "AMS-ResourceTagger-Configuration-ApplicationId"
          AMSResourceTaggerConfigurationCustomerManagedTagsProfileID: !ImportValue "AMS-ResourceTagger-Configuration-CustomerManagedTags-ProfileID"

  AMSAccelerateReadOnly:
    Type: 'AWS::IAM::ManagedPolicy'
    Properties:
      ManagedPolicyName: AMSAccelerateReadOnly
      Path: /
      PolicyDocument: !Sub |
        {
          "Version": "2012-10-17",
          "Statement": [
          {
                 "Sid": "AmsSelfServiceReport",
                 "Effect": "Allow",
                 "Action": "amsssrv:*",
                 "Resource": "*"
               },
            {
               "Sid": "AmsBackupPolicy",
               "Effect": "Allow",
               "Action": [
                 "backup:Describe*",
                 "backup:Get*",
                 "backup:List*"
               ],
               "Resource": "*"
            },
            {
                "Action": [
                    "rds:DescribeDBSnapshots",
                    "rds:ListTagsForResource",
                    "rds:DescribeDBInstances",
                    "rds:describeDBSnapshots",
                    "rds:describeDBEngineVersions",
                    "rds:describeOptionGroups",
                    "rds:describeOrderableDBInstanceOptions",
                    "rds:describeDBSubnetGroups",
                    "rds:DescribeDBClusterSnapshots",
                    "rds:DescribeDBClusters",
                    "rds:DescribeDBParameterGroups",
                    "rds:DescribeDBClusterParameterGroups",
                    "rds:DescribeDBInstanceAutomatedBackups"
                ],
                "Effect": "Allow",
                "Resource": "*"
            },
            {
                "Action": [
                    "dynamodb:ListBackups",
                    "dynamodb:ListTables"
                ],
                "Effect": "Allow",
                "Resource": "*"
            },
            {
                "Action": [
                    "elasticfilesystem:DescribeFilesystems"
                ],
                "Resource": "arn:aws:elasticfilesystem:*:*:file-system/*",
                "Effect": "Allow"
            },
            {
                "Action": [
                    "ec2:DescribeSnapshots",
                    "ec2:DescribeVolumes",
                    "ec2:describeAvailabilityZones",
                    "ec2:DescribeVpcs",
                    "ec2:DescribeAccountAttributes",
                    "ec2:DescribeSecurityGroups",
                    "ec2:DescribeImages",
                    "ec2:DescribeSubnets",
                    "ec2:DescribePlacementGroups",
                    "ec2:DescribeInstances",
                    "ec2:DescribeInstanceTypes"
                ],
                "Effect": "Allow",
                "Resource": "*"
            },
            {
                "Action": [
                    "tag:GetTagKeys",
                    "tag:GetTagValues",
                    "tag:GetResources"
                ],
                "Effect": "Allow",
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "storagegateway:DescribeCachediSCSIVolumes",
                    "storagegateway:DescribeStorediSCSIVolumes"
                ],
                "Resource": "arn:aws:storagegateway:*:*:gateway/*/volume/*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "storagegateway:ListGateways"
                ],
                "Resource": "arn:aws:storagegateway:*:*:*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "storagegateway:DescribeGatewayInformation",
                    "storagegateway:ListVolumes",
                    "storagegateway:ListLocalDisks"
                ],
                "Resource": "arn:aws:storagegateway:*:*:gateway/*"
            },
            {
                "Action": [
                    "iam:ListRoles",
                    "iam:GetRole"
                ],
                "Effect": "Allow",
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": "organizations:DescribeOrganization",
                "Resource": "*"
            },
            {
                "Action": "fsx:DescribeBackups",
                "Effect": "Allow",
                "Resource": "arn:aws:fsx:*:*:backup/*"
            },
            {
                "Action": "fsx:DescribeFileSystems",
                "Effect": "Allow",
                "Resource": "arn:aws:fsx:*:*:file-system/*"
            },
            {
                "Action": "ds:DescribeDirectories",
                "Effect": "Allow",
                "Resource": "*"
            },
            {
              "Sid": "AmsChangeRecordKMSPolicy",
              "Effect": "Allow",
              "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKey"
              ],
              "Resource": [
                "arn:aws:kms:${`AWS::Region`}:${`AWS::AccountId`}:key/*"
              ],
              "Condition": {
                "ForAnyValue:StringLike": {
                  "kms:ResourceAliases": "alias/AMSCloudTrailLogManagement"
                }
              }
            },
            {
              "Sid": "AmsChangeRecordAthenaReadPolicy",
              "Effect": "Allow",
              "Action": [
                "athena:BatchGetNamedQuery",
                "athena:Get*",
                "athena:List*",
                "athena:StartQueryExecution",
                "athena:UpdateWorkGroup",
                "glue:GetDatabase*",
                "glue:GetTable*",
                "s3:GetAccountPublicAccessBlock",
                "s3:ListAccessPoints",
                "s3:ListAllMyBuckets"
              ],
              "Resource": "*"
            },
            {
              "Sid": "AmsChangeRecordS3ReadPolicy",
              "Effect": "Allow",
              "Action": [
                "s3:Get*",
                "s3:List*"
              ],
              "Resource": [
                "arn:aws:s3:::ams-a${`AWS::AccountId`}-athena-results-${`AWS::Region`}",
                "arn:aws:s3:::ams-a${`AWS::AccountId`}-athena-results-${`AWS::Region`}/*",
                "arn:aws:s3:::ams-a${`AWS::AccountId`}-cloudtrail-${`AWS::Region`}",
                "arn:aws:s3:::ams-a${`AWS::AccountId`}-cloudtrail-${`AWS::Region`}/*"
              ]
            },
            {
              "Sid": "AmsChangeRecordS3WritePolicy",
              "Effect": "Allow",
              "Action": [
                "s3:PutObject",
                "s3:PutObjectLegalHold",
                "s3:PutObjectRetention"
              ],
              "Resource": [
                "arn:aws:s3:::ams-a${`AWS::AccountId`}-athena-results-${`AWS::Region`}/*"
              ]
            },
            {
              "Sid": "MaciePolicy",
              "Effect": "Allow",
              "Action": [
                "macie2:GetFindingStatistics"
              ],
              "Resource": "*"
            },
            {
              "Sid": "GuardDutyReadPolicy",
              "Effect": "Allow",
              "Action": [
                "guardduty:GetFindingsStatistics",
                "guardduty:ListDetectors"
              ],
              "Resource": "*"
            },
            {
              "Sid": "SupportReadPolicy",
              "Effect": "Allow",
              "Action": "support:Describe*",
              "Resource": "*"
            },
            {
              "Sid": "ConfigReadPolicy",
              "Effect": "Allow",
              "Action": [
                "config:Get*",
                "config:Describe*",
                "config:List*"
              ],
              "Resource": "*"
            },
            {
              "Sid": "AppConfigReadPolicy",
              "Effect": "Allow",
              "Action": [
                "appconfig:List*",
                "appconfig:Get*"
              ],
              "Resource": "*"
            },
            {
              "Sid": "CloudFormationReadPolicy",
              "Effect": "Allow",
              "Action": [
                "cloudformation:DescribeStacks"
              ],
              "Resource": "*"
            },
            {
              "Sid": "EC2ReadPolicy",
              "Effect": "Allow",
              "Action": [
                "ec2:DescribeInstances"
              ],
              "Resource": "*"
            },
            {
              "Sid": "SSMReadPolicy",
              "Effect": "Allow",
              "Action": [
                "ssm:Describe*",
                "ssm:Get*",
                "ssm:List*"
              ],
              "Resource": "*"
            },
            {
              "Sid": "TagReadPolicy",
              "Effect": "Allow",
              "Action": [
                "tag:GetResources",
                "tag:GetTagKeys"
              ],
              "Resource": "*"
            },
            {
              "Sid": "CloudtrailReadPolicy",
              "Effect": "Allow",
              "Action": [
                "cloudtrail:DescribeTrails",
                "cloudtrail:GetTrailStatus",
                "cloudtrail:LookupEvents"
              ],
              "Resource": "*"
            },
            {
              "Sid": "EventBridgePolicy",
              "Effect": "Allow",
              "Action": [
                "events:Describe*",
                "events:List*",
                "events:TestEventPattern"
              ],
              "Resource": "*"
            }
          ]
        }
```
