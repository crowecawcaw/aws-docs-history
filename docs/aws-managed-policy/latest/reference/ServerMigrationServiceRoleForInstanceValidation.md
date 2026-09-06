

# ServerMigrationServiceRoleForInstanceValidation
<a name="ServerMigrationServiceRoleForInstanceValidation"></a>

**Description**: Permissions to allow the AWS SMS to run used data validation script and send script success/failure back to SMS

`ServerMigrationServiceRoleForInstanceValidation` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="ServerMigrationServiceRoleForInstanceValidation-how-to-use"></a>

You can attach `ServerMigrationServiceRoleForInstanceValidation` to your users, groups, and roles.

## Policy details
<a name="ServerMigrationServiceRoleForInstanceValidation-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: July 20, 2020, 22:25 UTC 
+ **Edited time:** July 20, 2020, 22:25 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/ServerMigrationServiceRoleForInstanceValidation`

## Policy version
<a name="ServerMigrationServiceRoleForInstanceValidation-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="ServerMigrationServiceRoleForInstanceValidation-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "s3:GetObject",
      "Resource" : "arn:aws:s3:::sms-app-*/*"
    },
    {
      "Effect" : "Allow",
      "Action" : "sms:NotifyAppValidationOutput",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="ServerMigrationServiceRoleForInstanceValidation-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)