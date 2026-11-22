

# AWSPartnerCentralMarketingServiceRolePolicy

**Description**: Allows Partner Central Marketing to act in Partner Central on behalf of your marketing campaigns, including creating engagements in Partner Central Selling (partnercentral:CreateEngagement) in your own account from leads your campaigns capture.

`AWSPartnerCentralMarketingServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSPartnerCentralMarketingServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSPartnerCentralMarketingServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 17, 2026, 18:47 UTC 
+ **Edited time:** November 17, 2026, 18:47 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSPartnerCentralMarketingServiceRolePolicy`

## Policy version
<a name="AWSPartnerCentralMarketingServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSPartnerCentralMarketingServiceRolePolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "CreateEngagementFromCampaignLeads",
      "Effect" : "Allow",
      "Action" : [
        "partnercentral:CreateEngagement"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "partnercentral:Catalog" : [
            "AWS",
            "Sandbox"
          ],
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSPartnerCentralMarketingServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)