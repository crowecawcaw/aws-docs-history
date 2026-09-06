

# AmazonInspector2ManagedTelemetryPolicy
<a name="AmazonInspector2ManagedTelemetryPolicy"></a>

**Description**: Grants permissions to communicate with Inspector2 Telemetry Channel

`AmazonInspector2ManagedTelemetryPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonInspector2ManagedTelemetryPolicy-how-to-use"></a>

You can attach `AmazonInspector2ManagedTelemetryPolicy` to your users, groups, and roles.

## Policy details
<a name="AmazonInspector2ManagedTelemetryPolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: February 13, 2026, 17:12 UTC 
+ **Edited time:** February 13, 2026, 17:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonInspector2ManagedTelemetryPolicy`

## Policy version
<a name="AmazonInspector2ManagedTelemetryPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonInspector2ManagedTelemetryPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "PermissionsForInspector2Telemetry",
      "Effect" : "Allow",
      "Action" : [
        "inspector2-telemetry:StartSession",
        "inspector2-telemetry:StopSession",
        "inspector2-telemetry:SendTelemetry",
        "inspector2-telemetry:NotifyHeartbeat"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonInspector2ManagedTelemetryPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)