

# AWSPartnerProServeToolsFullAccess
<a name="AWSPartnerProServeToolsFullAccess"></a>

**Description**: Provides full access to ProServe tools.

`AWSPartnerProServeToolsFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSPartnerProServeToolsFullAccess-how-to-use"></a>

You can attach `AWSPartnerProServeToolsFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSPartnerProServeToolsFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: March 23, 2026, 21:57 UTC 
+ **Edited time:** March 23, 2026, 21:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSPartnerProServeToolsFullAccess`

## Policy version
<a name="AWSPartnerProServeToolsFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSPartnerProServeToolsFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowProServeToolsFullAccess",
      "Effect" : "Allow",
      "Action" : "partnercentral-account-management:AccessProServeTools",
      "Resource" : "*",
      "Condition" : {
        "ForAllValues:StringEquals" : {
          "partnercentral-account-management:ProServeRole" : [
            "AssessmentIndividualContributor",
            "AssessmentOrganizationReader",
            "AssessmentOrganizationContributor",
            "OrganizationAdmin"
          ]
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSPartnerProServeToolsFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)