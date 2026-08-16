# AmazonODBAutonomousVmClusterAdmin

**Description**: Provides administrative access to manage Autonomous VM cluster resources in Oracle Database@AWS

`AmazonODBAutonomousVmClusterAdmin` is an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

## Using this policy

You can attach `AmazonODBAutonomousVmClusterAdmin` to your users, groups, and roles.

## Policy details

- **Type**: Job function policy
- **Creation time**: August 07, 2026, 01:12 UTC
- **Edited time:** August 07, 2026, 01:12 UTC
- **ARN**:
  `arn:aws:iam::aws:policy/job-function/AmazonODBAutonomousVmClusterAdmin`

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
      "Sid" : "AllowODBActions",
      "Effect" : "Allow",
      "Action" : [
        "odb:GetOciOnboardingStatus",
        "odb:InitializeService",
        "odb:GetCloudExadataInfrastructure",
        "odb:GetCloudExadataInfrastructureUnallocatedResources",
        "odb:ListCloudExadataInfrastructures",
        "odb:CreateCloudAutonomousVmCluster",
        "odb:GetCloudAutonomousVmCluster",
        "odb:DeleteCloudAutonomousVmCluster",
        "odb:ListCloudAutonomousVmClusters",
        "odb:ListDbServers",
        "odb:GetOdbNetwork",
        "odb:ListOdbNetworks",
        "odb:ListAutonomousVirtualMachines",
        "odb:ListDbSystemShapes",
        "odb:ListGiVersions",
        "odb:ListSystemVersions",
        "odb:ListTagsForResource"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AllowEC2Actions",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeAvailabilityZones"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AllowTaggingActions",
      "Effect" : "Allow",
      "Action" : [
        "odb:TagResource",
        "odb:UntagResource"
      ],
      "Resource" : [
        "arn:aws:odb:*:*:cloud-autonomous-vm-cluster/*"
      ]
    },
    {
      "Sid" : "AllowOutboundIntegrationActions",
      "Effect" : "Allow",
      "Action" : [
        "odb:CreateOutboundIntegration"
      ],
      "Resource" : [
        "arn:aws:odb:*:*:cloud-autonomous-vm-cluster/*"
      ]
    }
  ]
}
```

## Learn more

- [Create a permission set using AWS managed policies in IAM Identity Center](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md")
- [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")
- [Understand versioning for IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-versioning.md "../../../IAM/latest/UserGuide/access_policies_managed-versioning.md")
- [Get started with AWS managed policies and move toward least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies")
