

# AWSPartnerCentralAccountManagementServiceRolePolicy
<a name="AWSPartnerCentralAccountManagementServiceRolePolicy"></a>

**Description**: Allows AWS Partner Central to access and manage your partner account resources, including partner account details and business plans, on your behalf.

`AWSPartnerCentralAccountManagementServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSPartnerCentralAccountManagementServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSPartnerCentralAccountManagementServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 04, 2026, 23:07 UTC 
+ **Edited time:** November 04, 2026, 23:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSPartnerCentralAccountManagementServiceRolePolicy`

## Policy version
<a name="AWSPartnerCentralAccountManagementServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSPartnerCentralAccountManagementServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "PartnerBusinessPlanWriteAccess",
      "Effect" : "Allow",
      "Action" : [
        "partnercentral:CreateBusinessPlan",
        "partnercentral:UpdateBusinessPlan",
        "partnercentral:CancelBusinessPlan",
        "partnercentral:CreateBusinessPlanItem",
        "partnercentral:UpdateBusinessPlanItem",
        "partnercentral:DeleteBusinessPlanItem",
        "partnercentral:StartBusinessPlanSubmissionTask",
        "partnercentral:CancelBusinessPlanSubmissionTask",
        "partnercentral:StartBusinessPlanAttachmentImportTask",
        "partnercentral:DeleteBusinessPlanAttachment"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "partnercentral:AllowAwsEngagement" : "ENABLED",
          "partnercentral:Catalog" : "AWS"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSPartnerCentralAccountManagementServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)