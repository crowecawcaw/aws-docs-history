

# AWSPartnerCentralChannelHandshakeApprovalManagement
<a name="AWSPartnerCentralChannelHandshakeApprovalManagement"></a>

**Description**: Provides necessary access for channel handshake approval management activities.

`AWSPartnerCentralChannelHandshakeApprovalManagement` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSPartnerCentralChannelHandshakeApprovalManagement-how-to-use"></a>

You can attach `AWSPartnerCentralChannelHandshakeApprovalManagement` to your users, groups, and roles.

## Policy details
<a name="AWSPartnerCentralChannelHandshakeApprovalManagement-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 19, 2025, 16:34 UTC 
+ **Edited time:** February 12, 2026, 17:59 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSPartnerCentralChannelHandshakeApprovalManagement`

## Policy version
<a name="AWSPartnerCentralChannelHandshakeApprovalManagement-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSPartnerCentralChannelHandshakeApprovalManagement-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ChannelHandshakeManagement",
      "Effect" : "Allow",
      "Action" : [
        "partnercentral:ListChannelHandshakes",
        "partnercentral:AcceptChannelHandshake",
        "partnercentral:RejectChannelHandshake"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "partnercentral:Catalog" : [
            "AWS",
            "Sandbox"
          ]
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSPartnerCentralChannelHandshakeApprovalManagement-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)