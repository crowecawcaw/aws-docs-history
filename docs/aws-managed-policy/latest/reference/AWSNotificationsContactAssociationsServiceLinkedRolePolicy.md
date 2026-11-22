

# AWSNotificationsContactAssociationsServiceLinkedRolePolicy

**Description**: Grants the AWS User Notifications service permissions to manage account contact associations.

`AWSNotificationsContactAssociationsServiceLinkedRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSNotificationsContactAssociationsServiceLinkedRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSNotificationsContactAssociationsServiceLinkedRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 10, 2026, 23:17 UTC 
+ **Edited time:** November 10, 2026, 23:17 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSNotificationsContactAssociationsServiceLinkedRolePolicy`

## Policy version
<a name="AWSNotificationsContactAssociationsServiceLinkedRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSNotificationsContactAssociationsServiceLinkedRolePolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ManageContactAssociations",
      "Effect" : "Allow",
      "Action" : [
        "notifications:AssociateManagedNotificationAccountContact",
        "notifications:DisassociateManagedNotificationAccountContact",
        "notifications:ListManagedNotificationChannelAssociations"
      ],
      "Resource" : "arn:aws:notifications::*:managed-notification-configuration/category/AWS-BCM/sub-category/SLA-Budgets",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSNotificationsContactAssociationsServiceLinkedRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)