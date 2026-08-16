# AWSTransformLandingZoneAgentPolicy

**Description**: Grants permissions for AWS Transform to set up AWS landing zones including account provisioning, organizational governance, and Control Tower configuration

`AWSTransformLandingZoneAgentPolicy` is an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

## Using this policy

You can attach `AWSTransformLandingZoneAgentPolicy` to your users, groups, and roles.

## Policy details

- **Type**: AWS managed policy
- **Creation time**: August 06, 2026, 15:12 UTC
- **Edited time:** August 06, 2026, 15:12 UTC
- **ARN**:
  `arn:aws:iam::aws:policy/AWSTransformLandingZoneAgentPolicy`

## Policy version

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a
request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "S3LandingZoneBucketAndObjectOperations",
      "Effect" : "Allow",
      "Action" : [
        "s3:AbortMultipartUpload",
        "s3:CreateBucket",
        "s3:DeleteObject",
        "s3:GetBucketLocation",
        "s3:GetBucketPublicAccessBlock",
        "s3:GetBucketTagging",
        "s3:GetObject",
        "s3:GetObjectAttributes",
        "s3:GetObjectVersion",
        "s3:ListBucket",
        "s3:ListBucketMultipartUploads",
        "s3:ListMultipartUploadParts",
        "s3:PutBucketTagging",
        "s3:PutEncryptionConfiguration",
        "s3:PutObject"
      ],
      "Resource" : "arn:aws:s3:::transform-vmware-landing-zone-*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "CfnLandingZoneStackCreate",
      "Effect" : "Allow",
      "Action" : [
        "cloudformation:CreateStack",
        "cloudformation:TagResource"
      ],
      "Resource" : "arn:aws:cloudformation:*:*:stack/AtxLz*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/CreatedBy" : "AWSTransform",
          "aws:RequestedRegion" : "${aws:PrincipalTag/TargetRegion}",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "CfnLandingZoneStackUpdate",
      "Effect" : "Allow",
      "Action" : [
        "cloudformation:UpdateStack"
      ],
      "Resource" : "arn:aws:cloudformation:*:*:stack/AtxLz*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/CreatedBy" : "AWSTransform",
          "aws:RequestedRegion" : "${aws:PrincipalTag/TargetRegion}",
          "aws:ResourceTag/CreatedBy" : "AWSTransform",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "CfnLandingZoneStackOperationsAndChangeSets",
      "Effect" : "Allow",
      "Action" : [
        "cloudformation:CreateChangeSet",
        "cloudformation:DescribeChangeSet",
        "cloudformation:DescribeStackEvents",
        "cloudformation:DescribeStacks",
        "cloudformation:ExecuteChangeSet",
        "cloudformation:GetTemplate",
        "cloudformation:ListChangeSets"
      ],
      "Resource" : "arn:aws:cloudformation:*:*:stack/AtxLz*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestedRegion" : "${aws:PrincipalTag/TargetRegion}",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ControlTowerAndOrganizationsOperationsReadOnly",
      "Effect" : "Allow",
      "Action" : [
        "controltower:GetBaselineOperation",
        "controltower:GetControlOperation",
        "controltower:ListBaselines",
        "controltower:ListEnabledBaselines",
        "controltower:ListEnabledControls",
        "controltower:ListLandingZones",
        "organizations:DescribeCreateAccountStatus",
        "organizations:DescribeOrganization",
        "organizations:ListPolicies",
        "organizations:ListRoots"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "ControlTowerResourceOperationsReadOnly",
      "Effect" : "Allow",
      "Action" : [
        "controltower:GetEnabledBaseline",
        "controltower:GetEnabledControl",
        "controltower:GetLandingZone",
        "controltower:ListTagsForResource"
      ],
      "Resource" : [
        "arn:aws:controltower:*:*:enabledbaseline/*",
        "arn:aws:controltower:*:*:enabledcontrol/*",
        "arn:aws:controltower:*:*:landingzone/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:RequestedRegion" : "${aws:PrincipalTag/TargetRegion}",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ControlTowerBaselineOperationsReadOnly",
      "Effect" : "Allow",
      "Action" : [
        "controltower:GetBaseline"
      ],
      "Resource" : "arn:aws:controltower:*::baseline/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestedRegion" : "${aws:PrincipalTag/TargetRegion}"
        }
      }
    },
    {
      "Sid" : "ControlTowerEnableControlWithRequestTag",
      "Effect" : "Allow",
      "Action" : [
        "controltower:EnableControl"
      ],
      "Resource" : "arn:aws:controltower:*:*:enabledcontrol/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/ATWorkspace" : "${aws:PrincipalTag/WorkspaceId}",
          "aws:RequestTag/CreatedBy" : "AWSTransform",
          "aws:RequestedRegion" : "${aws:PrincipalTag/TargetRegion}",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ControlTowerEnableBaselineAndOrganizationsAccountCreate",
      "Effect" : "Allow",
      "Action" : [
        "controltower:EnableBaseline",
        "controltower:TagResource",
        "organizations:CreateAccount"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/ATWorkspace" : "${aws:PrincipalTag/WorkspaceId}",
          "aws:RequestTag/CreatedBy" : "AWSTransform"
        }
      }
    },
    {
      "Sid" : "OrganizationsTagAndCreateOrganizationalUnit",
      "Effect" : "Allow",
      "Action" : [
        "organizations:CreateOrganizationalUnit",
        "organizations:TagResource"
      ],
      "Resource" : [
        "arn:aws:organizations::*:account/o-*/*",
        "arn:aws:organizations::*:ou/o-*/*",
        "arn:aws:organizations::*:policy/o-*/*",
        "arn:aws:organizations::*:root/o-*/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/ATWorkspace" : "${aws:PrincipalTag/WorkspaceId}",
          "aws:RequestTag/CreatedBy" : "AWSTransform",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "OrganizationsResourceDescribeReadOnly",
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribeAccount",
        "organizations:DescribeOrganizationalUnit",
        "organizations:DescribePolicy"
      ],
      "Resource" : [
        "arn:aws:organizations::*:account/*",
        "arn:aws:organizations::*:ou/*",
        "arn:aws:organizations::*:policy/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "OrganizationsPolicyUpdateViaControlTower",
      "Effect" : "Allow",
      "Action" : [
        "organizations:UpdatePolicy"
      ],
      "Resource" : "arn:aws:organizations::*:policy/*",
      "Condition" : {
        "ForAnyValue:StringEquals" : {
          "aws:CalledVia" : "controltower.amazonaws.com"
        },
        "StringEquals" : {
          "organizations:PolicyType" : "SERVICE_CONTROL_POLICY",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "OrganizationsHierarchyOperationsReadOnly",
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListAccountsForParent",
        "organizations:ListOrganizationalUnitsForParent",
        "organizations:ListParents"
      ],
      "Resource" : [
        "arn:aws:organizations::*:account/*",
        "arn:aws:organizations::*:ou/*",
        "arn:aws:organizations::*:root/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "OrganizationsMoveAccountWithResourceTag",
      "Effect" : "Allow",
      "Action" : [
        "organizations:MoveAccount"
      ],
      "Resource" : [
        "arn:aws:organizations::*:account/*",
        "arn:aws:organizations::*:ou/*",
        "arn:aws:organizations::*:root/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/ATWorkspace" : "${aws:PrincipalTag/WorkspaceId}",
          "aws:ResourceTag/CreatedBy" : "AWSTransform",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "OrganizationsListTagsForResource",
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListTagsForResource"
      ],
      "Resource" : [
        "arn:aws:organizations::*:account/o-*/*",
        "arn:aws:organizations::*:ou/o-*/*",
        "arn:aws:organizations::*:policy/o-*/*",
        "arn:aws:organizations::*:root/o-*/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "OrganizationsServiceControlPolicyCreateViaControlTower",
      "Effect" : "Allow",
      "Action" : [
        "organizations:CreatePolicy"
      ],
      "Resource" : "*",
      "Condition" : {
        "ForAnyValue:StringEquals" : {
          "aws:CalledVia" : "controltower.amazonaws.com"
        },
        "StringEquals" : {
          "organizations:PolicyType" : "SERVICE_CONTROL_POLICY"
        }
      }
    },
    {
      "Sid" : "OrganizationsServiceControlPolicyAttachViaControlTower",
      "Effect" : "Allow",
      "Action" : [
        "organizations:AttachPolicy"
      ],
      "Resource" : [
        "arn:aws:organizations::*:account/o-*/*",
        "arn:aws:organizations::*:ou/o-*/*",
        "arn:aws:organizations::*:policy/o-*/*",
        "arn:aws:organizations::*:root/o-*/*"
      ],
      "Condition" : {
        "ForAnyValue:StringEquals" : {
          "aws:CalledVia" : "controltower.amazonaws.com"
        },
        "StringEquals" : {
          "organizations:PolicyType" : "SERVICE_CONTROL_POLICY",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ServiceCatalogProvisioningArtifactOperations",
      "Effect" : "Allow",
      "Action" : [
        "servicecatalog:CreateProvisioningArtifact",
        "servicecatalog:DeleteProvisioningArtifact",
        "servicecatalog:ListProvisioningArtifacts",
        "servicecatalog:UpdateProvisioningArtifact"
      ],
      "Resource" : "arn:aws:catalog:*:*:product/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestedRegion" : "${aws:PrincipalTag/TargetRegion}",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Learn more

- [Create a permission set using AWS managed policies in IAM Identity Center](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md")
- [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")
- [Understand versioning for IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-versioning.md "../../../IAM/latest/UserGuide/access_policies_managed-versioning.md")
- [Get started with AWS managed policies and move toward least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies")
