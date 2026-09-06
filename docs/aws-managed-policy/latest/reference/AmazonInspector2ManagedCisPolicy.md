

# AmazonInspector2ManagedCisPolicy
<a name="AmazonInspector2ManagedCisPolicy"></a>

**Description**: This is a managed policy that customer should attach to their roles to communicate with inspector service for CIS scans

`AmazonInspector2ManagedCisPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonInspector2ManagedCisPolicy-how-to-use"></a>

You can attach `AmazonInspector2ManagedCisPolicy` to your users, groups, and roles.

## Policy details
<a name="AmazonInspector2ManagedCisPolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: January 24, 2024, 16:31 UTC 
+ **Edited time:** January 24, 2024, 16:31 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonInspector2ManagedCisPolicy`

## Policy version
<a name="AmazonInspector2ManagedCisPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonInspector2ManagedCisPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "PermissionsForCISScans",
      "Effect" : "Allow",
      "Action" : [
        "inspector2:StartCisSession",
        "inspector2:StopCisSession",
        "inspector2:SendCisSessionTelemetry",
        "inspector2:SendCisSessionHealth"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonInspector2ManagedCisPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)