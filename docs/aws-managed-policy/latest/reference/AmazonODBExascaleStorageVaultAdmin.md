

# AmazonODBExascaleStorageVaultAdmin
<a name="AmazonODBExascaleStorageVaultAdmin"></a>

**Description**: Provides administrative access to manage Exascale storage vault resources in Oracle Database@AWS.

`AmazonODBExascaleStorageVaultAdmin` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonODBExascaleStorageVaultAdmin-how-to-use"></a>

You can attach `AmazonODBExascaleStorageVaultAdmin` to your users, groups, and roles.

## Policy details
<a name="AmazonODBExascaleStorageVaultAdmin-details"></a>
+ **Type**: Job function policy 
+ **Creation time**: September 04, 2026, 21:37 UTC 
+ **Edited time:** September 04, 2026, 21:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/job-function/AmazonODBExascaleStorageVaultAdmin`

## Policy version
<a name="AmazonODBExascaleStorageVaultAdmin-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonODBExascaleStorageVaultAdmin-json"></a>

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
        "odb:CreateExascaleDbStorageVault",
        "odb:GetExascaleDbStorageVault",
        "odb:UpdateExascaleDbStorageVault",
        "odb:DeleteExascaleDbStorageVault",
        "odb:ListExascaleDbStorageVaults",
        "odb:ListExadbVmClusters",
        "odb:GetDbServer",
        "odb:ListDbServers",
        "odb:ListDbSystemShapes",
        "odb:ListFlexComponents",
        "odb:PutResourcePolicy",
        "odb:GetResourcePolicy",
        "odb:DeleteResourcePolicy",
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
      "Sid" : "AllowSLRActions",
      "Effect" : "Allow",
      "Action" : [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : [
            "odb.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid" : "AllowTaggingActions",
      "Effect" : "Allow",
      "Action" : [
        "odb:TagResource",
        "odb:UntagResource"
      ],
      "Resource" : [
        "arn:aws:odb:*:*:exascale-db-storage-vault/*"
      ]
    }
  ]
}
```

## Learn more
<a name="AmazonODBExascaleStorageVaultAdmin-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)