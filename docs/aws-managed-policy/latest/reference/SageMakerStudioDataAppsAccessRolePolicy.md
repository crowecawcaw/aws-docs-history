

# SageMakerStudioDataAppsAccessRolePolicy
<a name="SageMakerStudioDataAppsAccessRolePolicy"></a>

**Description**: Amazon SageMaker Studio uses this policy to access data apps shared with a user in the Amazon SageMaker Studio domain.

`SageMakerStudioDataAppsAccessRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="SageMakerStudioDataAppsAccessRolePolicy-how-to-use"></a>

You can attach `SageMakerStudioDataAppsAccessRolePolicy` to your users, groups, and roles.

## Policy details
<a name="SageMakerStudioDataAppsAccessRolePolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: October 13, 2026, 21:57 UTC 
+ **Edited time:** October 13, 2026, 21:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/SageMakerStudioDataAppsAccessRolePolicy`

## Policy version
<a name="SageMakerStudioDataAppsAccessRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="SageMakerStudioDataAppsAccessRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "DataZonePermissions",
      "Effect" : "Allow",
      "Action" : [
        "datazone:CreateSubscriptionRequest",
        "datazone:GetListing",
        "datazone:GetSubscription",
        "datazone:ListGroupsForUser",
        "datazone:ListProjects",
        "datazone:ListSharedDataApps",
        "datazone:ListSubscriptionGrants",
        "datazone:ListSubscriptions",
        "datazone:SearchListings"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "S3ControlReadPermissions",
      "Effect" : "Allow",
      "Action" : [
        "s3:GetDataAccess",
        "s3:ListCallerAccessGrants"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="SageMakerStudioDataAppsAccessRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)