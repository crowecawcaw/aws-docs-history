# Curated SCPs and Config Rules

Curated SCPs and Config Rules for AMS Advanced.

- **Service control policies (SCPs)**: The provided SCPs are in addition to default AMS ones.

You can use these library controls in tandem with the default ones to meet specific security requirements.

- **Config Rules**: As a baseline measure, AMS recommends applying Conformance Packs (see
  [Conformance Packs](../../../config/latest/developerguide/conformance-packs.md "../../../config/latest/developerguide/conformance-packs.md") in the AWS Config guide)
  in addition to the default AMS config rules (see AMS Artifacts for default rules). The Conformance Packs cover a majority of compliance
  requirements and AWS regularly updates them.

The rules listed here can be used to cover use-case specific gaps that aren’t covered by Conformance Packs

###### Note

As AMS default rules and conformance packs get updated over time, you might see duplicates of these rules.

AMS recommends doing periodic clean-up of duplicate Config Rules in general.

For AMS Advanced, Config Rules should not use auto-remediations (see
[Remediating Noncompliant AWS Resources by AWS Config Rules](../../../config/latest/developerguide/remediation.md "../../../config/latest/developerguide/remediation.md"))
in order to avoid out-of-band changes.

## SCP-AMS-001: Restrict EBS creation

Prevent the creation of EBS volumes if you don’t have encryption enabled.

```
{
      "Condition": {
        "Bool": {
          "ec2:Encrypted": "false"
        }
      },
      "Action": "ec2:CreateVolume",
      "Resource": "*",
      "Effect": "Deny"
    }
```

## SCP-AMS-002: Restrict EC2 launch

Prevent the launch of an EC2 instance if the EBS volume is unencrypted.
This includes denying an EC2 launch from unencrypted AMIs because this SCP also applies to root volumes.

```
{
      "Condition": {
        "Bool": {
          "ec2:Encrypted": "false"
        }
      },
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*:*:volume/*",
      "Effect": "Deny"
    }
```

## SCP-ADV-001: Restrict RFC submissions

Restrict default AMS roles from submitting specific automated RFCs like **Create VPC** or
**Delete VPC**. This is helpful if you want to apply more granular permissions to your federated roles.

For example, you might want the default `AWSManagedServicesChangeManagement Role` to be able to submit most of the
available RFCs except the ones that allow for the creation and deletion of a VPC, creation of additional subnets, offboarding of an
application account, updating or deleting SAML identity providers:

## SCP-AMS-003: Restrict EC2 or RDS creation in AMS

Prevent creation of Amazon EC2 and RDS instances that don't have specific tags, while allowing the AMS default
`AMS Backup IAM` role to do so. This is needed for disaster recover or DR.

```
{
    "Sid": "DenyRunInstanceWithNoOrganizationTag",
    "Effect": "Deny",
    "Action": [
        "ec2:RunInstances",
        "rds:CreateDBInstance"
    ],
    "Resource": [
        "arn:aws:ec2:*:*:instance/*",
        "arn:aws:ec2:*:*:volume/*",
        "arn:aws:rds:*:*:db:*"
    ],
    "Condition": {
        "Null": {
            "aws:RequestTag/organization": "true"
        },
        "StringNotLike": {
            "aws:PrincipalArn": [
                "arn:aws:iam::<Account_Number>:role/ams-backup-iam-role"
            ]
        }
    }
}
```

## SCP-AMS-004: Restrict S3 uploads

Prevent uploads of unencrypted S3 objects.

```
{
            "Sid": "DenyUnencryptedS3Uploads",
            "Effect": "Deny",
            "Action": "s3:PutObject",
            "Resource": "*",
            "Condition": {
                "StringNotLike": {
                    "s3:x-amz-server-side-encryption": ["aws:kms", "AES256"]
                },
                "Null": {
                    "s3:x-amz-server-side-encryption": "false"
                }
            }
        }
    ]
}
```

## SCP-AMS-005: Restrict API and console access

Prevent AWS Console and API access for requests coming from known bad IP addresses as determined customer InfoSec.

## SCP-AMS-006: Prevent IAM entity from removing member account from the organization

Prevent an AWS Identity and Access Management entity from removing member accounts from the organization.

```
{
  "Effect": "Deny",
  "Action": ["organizations:LeaveOrganization"],
  "Resource": ["*"]
}
```

## SCP-AMS-007: Prevent sharing resources to accounts outside your organization

Prevent sharing resources with external accounts outside your AWS organization

```

  {
    "Effect": "Deny",
    "Action": [
      "ram:*"
    ],
    "Resource": [
      "*"
    ],
    "Condition": {
      "Bool": {
        "ram:AllowsExternalPrincipals": "true"
      }
    }
  },
  {
    "Effect": "Deny",
    "Action": [
      "ram:CreateResourceShare",
      "ram:UpdateResourceShare"
    ],
    "Resource": "*",
    "Condition": {
      "Bool": {
        "ram:RequestedAllowsExternalPrincipals": "true"
      }
    }
  }

```

## SCP-AMS-008: Prevent sharing with organizations or organizational units (OUs)

Prevent sharing resources with an account and/or OU that's in an organization.

```
{
  "Effect": "Deny",
  "Action": [
    "ram:CreateResourceShare",
    "ram:AssociateResourceShare"
  ],
  "Resource": "*",
  "Condition": {
    "ForAnyValue:StringLike": {
      "ram:Principal": [
        "arn:aws:organizations::*:account/o-${OrganizationId}/${AccountId}",
        "arn:aws:organizations::*:ou/o-${OrganizationId}/ou-${OrganizationalUnitId}"
      ]
    }
  }
}
```

## SCP-AMS-009: Prevent users from accepting resource share invitations

Prevent member accounts from accepting invitations from AWS RAM to join resource shares. This API doesn't support any conditions and prevents shares only from external accounts.

```
{
  "Effect": "Deny",
  "Action": ["ram:AcceptResourceShareInvitation"],
  "Resource": ["*"]
}
```

## SCP-AMS-010: Prevent account Region enable and disable actions

Prevent enabling or disabling any new AWS Regions for your AWS accounts.

```
{
  "Effect": "Deny",
  "Action": [
    "account:EnableRegion",
    "account:DisableRegion"
  ],
  "Resource": "*"
}
```

## SCP-AMS-011: Prevent billing modification actions

Prevent modifications to billing and payment configuration.

```
{
  "Effect": "Deny",
  "Action": [
    "aws-portal:ModifyBilling",
    "aws-portal:ModifyAccount",
    "aws-portal:ModifyPaymentMethods"
  ],
  "Resource": "*"
}
```

## SCP-AMS-012: Prevent deletion or modification to specific CloudTrails

Prevent modifications to specific AWS CloudTrail trails.

```
{
  "Effect": "Deny",
  "Action": [
    "cloudtrail:DeleteEventDataStore",
    "cloudtrail:DeleteTrail",
    "cloudtrail:PutEventSelectors",
    "cloudtrail:PutInsightSelectors",
    "cloudtrail:UpdateEventDataStore",
    "cloudtrail:UpdateTrail",
    "cloudtrail:StopLogging"
  ],
  "Resource": [
    "arn:${Partition}:cloudtrail:${Region}:${Account}:trail/${TrailName}"
  ]
}
```

## SCP-AMS-013: Prevent disabling default EBS encryption

Prevent disabling of default Amazon EBS encryption.

```
{
  "Effect": "Deny",
  "Action": [
    "ec2:DisableEbsEncryptionByDefault"
  ],
  "Resource": "*"
}
```

## SCP-AMS-014: Prevent creating default VPC and subnet

Prevent the creation of a default Amazon VPC and subnets.

```
{
  "Effect": "Deny",
  "Action": [
    "ec2:CreateDefaultSubnet",
    "ec2:CreateDefaultVpc"
  ],
  "Resource": "*"
}
```

## SCP-AMS-015: Prevent disabling and modifying GuardDuty

Prevent Amazon GuardDuty from being modified or disabled.

```
{
  "Effect": "Deny",
  "Action": [
    "guardduty:AcceptInvitation",
    "guardduty:ArchiveFindings",
    "guardduty:CreateDetector",
    "guardduty:CreateFilter",
    "guardduty:CreateIPSet",
    "guardduty:CreateMembers",
    "guardduty:CreatePublishingDestination",
    "guardduty:CreateSampleFindings",
    "guardduty:CreateThreatIntelSet",
    "guardduty:DeclineInvitations",
    "guardduty:DeleteDetector",
    "guardduty:DeleteFilter",
    "guardduty:DeleteInvitations",
    "guardduty:DeleteIPSet",
    "guardduty:DeleteMembers",
    "guardduty:DeletePublishingDestination",
    "guardduty:DeleteThreatIntelSet",
    "guardduty:DisableOrganizationAdminAccount",
    "guardduty:DisassociateFromMasterAccount",
    "guardduty:DisassociateMembers",
    "guardduty:InviteMembers",
    "guardduty:StartMonitoringMembers",
    "guardduty:StopMonitoringMembers",
    "guardduty:TagResource",
    "guardduty:UnarchiveFindings",
    "guardduty:UntagResource",
    "guardduty:UpdateDetector",
    "guardduty:UpdateFilter",
    "guardduty:UpdateFindingsFeedback",
    "guardduty:UpdateIPSet",
    "guardduty:UpdateMalwareScanSettings",
    "guardduty:UpdateMemberDetectors",
    "guardduty:UpdateOrganizationConfiguration",
    "guardduty:UpdatePublishingDestination",
    "guardduty:UpdateThreatIntelSet"
  ],
  "Resource": "*"
}
```

## SCP-AMS-016: Prevent root user activity

Prevent the root user from performing any action.

```
{
  "Action": "*",
  "Resource": "*",
  "Effect": "Deny",
  "Condition": {
    "StringLike": {
      "aws:PrincipalArn": [
        "arn:aws:iam::*:root"
      ]
    }
  }
}
```

## SCP-AMS-017: Prevent creating access keys for the root user

Prevent the creation of access keys for the root user.

```
{
  "Effect": "Deny",
  "Action": "iam:CreateAccessKey",
  "Resource": "arn:aws:iam::*:root"
}
```

## SCP-AMS-018: Prevent disabling S3 account public access block

Prevent disabling an Amazon S3 account public access block. This prevents any bucket in the account from becoming public.

```
{
  "Effect": "Deny",
  "Action": "s3:PutAccountPublicAccessBlock",
  "Resource": "*"
}
```

## SCP-AMS-019: Prevent disabling AWS Config or modifying Config rules

Prevent disabling or modifying AWS Config rules.

```
{
  "Effect": "Deny",
  "Action": [
    "config:DeleteConfigRule",
    "config:DeleteConfigurationRecorder",
    "config:DeleteDeliveryChannel",
    "config:DeleteEvaluationResults",
    "config:StopConfigurationRecorder"
  ],
  "Resource": "*"
}
```

## SCP-AMS-020: Prevent all IAM actions

Prevent all IAM actions.

```
{
  "Effect": "Deny",
  "Action": [
    "iam:*"
  ],
  "Resource": "*"
}
```

## SCP-AMS-021: Prevent deleting CloudWatch Logs groups and streams

Prevent deleting Amazon CloudWatch Logs groups and streams.

```
{
  "Effect": "Deny",
  "Action": [
    "logs:DeleteLogGroup",
    "logs:DeleteLogStream"
  ],
  "Resource": "*"
}
```

## SCP-AMS-022: Prevent Glacier deletion

Prevent Amazon Glacier deletion.

```
{
  "Effect": "Deny",
  "Action": [
    "glacier:DeleteArchive",
    "glacier:DeleteVault"
  ],
  "Resource": "*"
}
```

## SCP-AMS-023: Prevent deletion of IAM Access Analyzer

Prevent the deletion of IAM Access Analyzer.

```
{
  "Action": [
    "access-analyzer:DeleteAnalyzer"
  ],
  "Resource": "*",
  "Effect": "Deny"
}
```

## SCP-AMS-024: Prevent modifications to Security Hub

Prevent the deletion of AWS Security Hub.

```
{
  "Action": [
    "securityhub:DeleteInvitations",
    "securityhub:DisableSecurityHub",
    "securityhub:DisassociateFromMasterAccount",
    "securityhub:DeleteMembers",
    "securityhub:DisassociateMembers"
  ],
  "Resource": "*",
  "Effect": "Deny"
}
```

## SCP-AMS-025: Prevent deletion under Directory Service

Prevent the deletion of resources under AWS Directory Service.

```
{
  "Action": [
    "ds:DeleteDirectory",
    "ds:DeleteLogSubscription",
    "ds:DeleteSnapshot",
    "ds:DeleteTrust",
    "ds:DeregisterCertificate",
    "ds:DeregisterEventTopic",
    "ds:DisableLDAPS",
    "ds:DisableRadius",
    "ds:DisableSso",
    "ds:UnshareDirectory"
  ],
  "Resource": "*",
  "Effect": "Deny"
}
```

## SCP-AMS-026: Prevent use of denylisted service

Prevent the use of denylisted services.

###### Note

Replace `service1` and `service2` with your service names. Example `access-analyzer` or `IAM`.

```
{
  "Effect": "Deny",
  "Resource": "*",
  "Action": ["`service1`:*", "`service2`:*"]
}
```

## SCP-AMS-027: Prevent use of denylisted service in specific Regions

Prevent the use of denylisted services in specific AWS Regions.

###### Note

Replace `service1` and `service2` with your service names. Example `access-analyzer` or `IAM`.

Replace `region1` and `region2` with your service names. Example `us-west-2` or `use-east-1`.

```
{
  "Effect": "Deny",
  "Resource": "*",
  "Action": ["`service1`:*", "`service2`:*"],
  "Condition": {
    "StringEquals": {
      "aws:RequestedRegion": [
        "`region1`",
        "`region2`"
      ]
    }
  }
}
```

## SCP-AMS-028: Prevent tags from being modified except by authorized principals

Prevent tag modifications by any user except the authorized principals. Use authorization tags to authorize principals. Authorization tags must be associated with resources and with principals. A user/role is only considered authorized if the tag on both the resource and the principal match. For more information, see the following resources:

- [Securing resource tags used for authorization using a service control policy in AWS Organizations](https://aws.amazon.com/blogs/security/securing-resource-tags-used-for-authorization-using-service-control-policy-in-aws-organizations/ "https://aws.amazon.com/blogs/security/securing-resource-tags-used-for-authorization-using-service-control-policy-in-aws-organizations/")
- [Prevent tags from being modified except by authorized principals](../../../organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.md#example-require-restrict-tag-mods-to-admin "../../../organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.md#example-require-restrict-tag-mods-to-admin")

```
{
  "Effect": "Deny",
  "Action": [
    "ec2:CreateTags",
    "ec2:DeleteTags"
  ],
  "Resource": [
    "*"
  ],
  "Condition": {
    "StringNotEquals": {
      "ec2:ResourceTag/access-project": "${aws:PrincipalTag/access-project}",
      "aws:PrincipalArn": "arn:aws:iam::{`ACCOUNT_ID`}:{`RESOURCE_TYPE`}/{`RESOURCE_NAME`}"
    },
    "Null": {
      "ec2:ResourceTag/access-project": false
    }
  }
},
{
  "Effect": "Deny",
  "Action": [
    "ec2:CreateTags",
    "ec2:DeleteTags"
  ],
  "Resource": [
    "*"
  ],
  "Condition": {
    "StringNotEquals": {
      "aws:RequestTag/access-project": "${aws:PrincipalTag/access-project}",
      "aws:PrincipalArn": "arn:aws:iam::{`ACCOUNT_ID`}:{`RESOURCE_TYPE`}/{`RESOURCE_NAME`}"
    },
    "ForAnyValue:StringEquals": {
      "aws:TagKeys": [
        "access-project"
      ]
    }
  }
},
{
  "Effect": "Deny",
  "Action": [
    "ec2:CreateTags",
    "ec2:DeleteTags"
  ],
  "Resource": [
    "*"
  ],
  "Condition": {
    "StringNotEquals": {
      "aws:PrincipalArn": "arn:aws:iam::{`ACCOUNT_ID`}:{`RESOURCE_TYPE`}/{`RESOURCE_NAME`}"
    },
    "Null": {
      "aws:PrincipalTag/access-project": true
    }
  }
}
```

## SCP-AMS-029: Prevent users from deleting Amazon VPC Flow Logs

Prevent the deletion of Amazon VPC Flow Logs.

```
{
  "Action": [
    "ec2:DeleteFlowLogs",
    "logs:DeleteLogGroup",
    "logs:DeleteLogStream",
    "s3:DeleteBucket",
    "s3:DeleteObject",
    "s3:DeleteObjectVersion",
    "s3:PutLifecycleConfiguration",
    "firehose:DeleteDeliveryStream"
  ],
  "Resource": "*",
  "Effect": "Deny"
}
```

## SCP-AMS-030: Prevent sharing VPC subnet with account other than network account

Prevent sharing Amazon VPC subnets with accounts other than the network account.

###### Note

Replace `NETWORK_ACCOUNT_ID` with your network account ID.

```
{
  "Effect": "Deny",
  "Action": [
    "ram:AssociateResourceShare",
    "ram:CreateResourceShare"
  ],
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "ram:Principal": "`NETWORK_ACCOUNT_ID`"
    },
    "StringEquals": {
      "ram:RequestedResourceType": "ec2:Subnet"
    }
  }
}
```

## SCP-AMS-031: Prevent launching instances with prohibited instance types

Prevent launcing prohibited Amazon EC2 instance types.

###### Note

Replace `instance_type1` and `instance_type2` with the instance types that you want to restrict, such as `t2.micro` or a wildcard string such as `*.nano`.

```
{
  "Effect": "Deny",
  "Action": "ec2:RunInstances",
  "Resource": [
    "arn:aws:ec2:*:*:instance/*"
  ],
  "Condition": {
    "ForAnyValue:StringLike": {
      "ec2:InstanceType": [
        "`instance_type1`",
        "`instance_type2`"
      ]
    }
  }
}
```

## SCP-AMS-032: Prevent launching instances without IMDSv2

Prevent Amazon EC2 instances without IMDSv2.

```
[
  {
    "Effect": "Deny",
    "Action": "ec2:RunInstances",
    "Resource": "arn:aws:ec2:*:*:instance/*",
    "Condition": {
      "StringNotEquals": {
        "ec2:MetadataHttpTokens": "required"
      }
    }
  },
  {
    "Effect": "Deny",
    "Action": "ec2:RunInstances",
    "Resource": "arn:aws:ec2:*:*:instance/*",
    "Condition": {
      "NumericGreaterThan": {
        "ec2:MetadataHttpPutResponseHopLimit": "3"
      }
    }
  },
  {
    "Effect": "Deny",
    "Action": "*",
    "Resource": "*",
    "Condition": {
      "NumericLessThan": {
        "ec2:RoleDelivery": "2.0"
      }
    }
  },
  {
    "Effect": "Deny",
    "Action": "ec2:ModifyInstanceMetadataOptions",
    "Resource": "*"
  }
]
```

## SCP-AMS-033: Prevent modifications to specific IAM role

Prevent modifications to specified IAM roles.

```
{
  "Action": [
    "iam:AttachRolePolicy",
    "iam:DeleteRole",
    "iam:DeleteRolePermissionsBoundary",
    "iam:DeleteRolePolicy",
    "iam:DetachRolePolicy",
    "iam:PutRolePermissionsBoundary",
    "iam:PutRolePolicy",
    "iam:TagRole",
    "iam:UntagRole",
    "iam:UpdateAssumeRolePolicy",
    "iam:UpdateRole",
    "iam:UpdateRoleDescription"
  ],
  "Resource": [
     "arn:aws:iam::{`ACCOUNT_ID`}:role/{`RESOURCE_NAME`}"
  ],
  "Effect": "Deny"
}
```

## SCP-AMS-034: Prevent AssumeRolePolicy modification on specific IAM roles

Prevent modifications to the AssumeRolePolicy for specified IAM roles.

```
{
  "Action": [
    "iam:UpdateAssumeRolePolicy"
  ],
  "Resource": [
     "arn:aws:iam::{`ACCOUNT_ID`}:role/{`RESOURCE_NAME`}"
  ],
  "Effect": "Deny"
}
```

## ConfigRule: Required tags

Check whether EC2 instances have custom tags that you have required.
In addition to InfoSec, this is also useful for your Cost Management

```
ConfigRuleName: required-tags
      Description: >-
        A Config rule that checks whether EC2 instances have the required tags.
      Scope:
        ComplianceResourceTypes:
          - 'AWS::EC2::Instance'
      InputParameters:
        tag1Key: COST_CENTER
        tag2Key: APP_ID
      Source:
        Owner: AWS
        SourceIdentifier: REQUIRED_TAGS
```

## ConfigRule: Access key rotated

Check that access keys are being rotated within the specified time period. This is usually set to be 90 days per typical compliance requirements.

```
ConfigRuleName: access-keys-rotated
      Description: >-
        A config rule that checks whether the active access keys are rotated
        within the number of days specified in maxAccessKeyAge. The rule is
        NON_COMPLIANT if the access keys have not been rotated for more than
        maxAccessKeyAge number of days.
      InputParameters:
        maxAccessKeyAge: '90'
      Source:
        Owner: AWS
        SourceIdentifier: ACCESS_KEYS_ROTATED
      MaximumExecutionFrequency: TwentyFour_Hours
```

## ConfigRule: IAM root access key in AMS

Check that a root access key is not present on an account. For AMS Advanced accounts, this is expected to be compliant out-of-the-box.

```
ConfigRuleName: iam-root-access-key-check
      Description: >-
        A config rule that checks whether the root user access key is available. The rule is COMPLIANT if the user access key does not exist.
      Source:
        Owner: AWS
        SourceIdentifier: IAM_ROOT_ACCESS_KEY_CHECK
      MaximumExecutionFrequency: TwentyFour_Hours
```

## ConfigRule: SSM managed EC2

Check that your EC2s are being managed by SSM Systems Manager.

```
ConfigRuleName: ec2-instance-managed-by-systems-manager
      Description: >-
        A Config rule that checks whether the EC2 instances in the
        account are managed by AWS Systems Manager.
      Scope:
        ComplianceResourceTypes:
          - 'AWS::EC2::Instance'
          - 'AWS::SSM::ManagedInstanceInventory'
      Source:
        Owner: AWS
        SourceIdentifier: EC2_INSTANCE_MANAGED_BY_SSM
```

## ConfigRule: Unused IAM user in AMS

Check for IAM user credentials that have not been used for a specified duration. Like the key-rotation check, this usually
defaults to 90 days per typical compliance requirements.

```
ConfigRuleName: iam-user-unused-credentials-check
      Description: >-
        A config rule that checks whether IAM users have passwords
        or active access keys that have not been used within the
        specified number of days provided.
      InputParameters:
        maxCredentialUsageAge: '90'
      Source:
        Owner: AWS
        SourceIdentifier: IAM_USER_UNUSED_CREDENTIALS_CHECK
      MaximumExecutionFrequency: TwentyFour_Hours
```

## ConfigRule: S3 bucket logging

Check that logging has been enabled for S3 buckets in the account.

```
ConfigRuleName: s3-bucket-logging-enabled
      Description: >-
        A Config rule that checks whether logging is enabled for S3 buckets.
      Scope:
        ComplianceResourceTypes:
          - 'AWS::S3::Bucket'
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_LOGGING_ENABLED
```

## ConfigRule: S3 bucket versioning

Check that versioning and MFA-delete (optional) is enabled on all S3 buckets

```
ConfigRuleName: s3-bucket-versioning-enabled
      Description: >-
        A Config rule that checks whether versioning is enabled for S3
        buckets. Optionally, the rule checks if MFA delete is enabled for S3 buckets.
      Scope:
        ComplianceResourceTypes:
          - 'AWS::S3::Bucket'
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_VERSIONING_ENABLED
```

## ConfigRule: S3 public access

Check that public access settings (Public ACL, Public Policy, Public Buckets) are restricted across the account

```
ConfigRuleName: s3-account-level-public-access-blocks
      Description: >-
        A Config rule that checks whether the required public access block
        settings are configured from account level. The rule is only
        NON_COMPLIANT when the fields set below do not match the corresponding
        fields in the configuration item.
      Scope:
        ComplianceResourceTypes:
          - 'AWS::S3::AccountPublicAccessBlock'
      InputParameters:
        IgnorePublicAcls: 'True'
        BlockPublicPolicy: 'True'
        BlockPublicAcls: 'True'
        RestrictPublicBuckets: 'True'
      Source:
        Owner: AWS
        SourceIdentifier: S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS
```

## ConfigRule: Non-archived GuardDuty findings

Check for any non-archived GuardDuty findings that are older than the
specified duration. The default duration is 30 days for low-sev, 7 days for medium-sev and 1 day for high-sev findings.

```
ConfigRuleName: guardduty-non-archived-findings
      Description: >-
        A Config rule that checks whether the Amazon GuardDuty has findings that
        are non archived. The rule is NON_COMPLIANT if GuardDuty has non
        archived low/medium/high severity findings older than the specified number.
      InputParameters:
        daysLowSev: '30'
        daysMediumSev: '7'
        daysHighSev: '1'
      Source:
        Owner: AWS
        SourceIdentifier: GUARDDUTY_NON_ARCHIVED_FINDINGS
      MaximumExecutionFrequency: TwentyFour_Hours
```

## ConfigRule: CMK deletion

Check for any AWS Key Management Service custom master keys (CMKs) that are scheduled (aka pending) for deletion.
This is crucial as unawareness around CMK deletion can lead to data being unrecoverable

```
ConfigRuleName: kms-cmk-not-scheduled-for-deletion
      Description: >-
        A config rule that checks whether customer master keys (CMKs) are not
        scheduled for deletion in AWS Key Management Service (AWS KMS). The rule is
        NON_COMPLIANT if CMKs are scheduled for deletion.
      Source:
        Owner: AWS
        SourceIdentifier: KMS_CMK_NOT_SCHEDULED_FOR_DELETION
      MaximumExecutionFrequency: TwentyFour_Hours
```

## ConfigRule: CMK rotation

Check that auto-rotation is enabled for every CMK in the account

```
ConfigRuleName: cmk-backing-key-rotation-enabled
      Description: >-
        A config rule that checks that key rotation is enabled for each customer
        master key (CMK). The rule is COMPLIANT, if the key rotation is enabled
        for specific key object. The rule is not applicable to CMKs that have
        imported key material.
      Source:
        Owner: AWS
        SourceIdentifier: CMK_BACKING_KEY_ROTATION_ENABLED
      MaximumExecutionFrequency: TwentyFour_Hours
```
