

# AWSCloudWatchAlarms\_ActionSSMIncidentsServiceRolePolicy
<a name="AWSCloudWatchAlarms_ActionSSMIncidentsServiceRolePolicy"></a>

**Description**: This policy is used by the service-linked role named AWSServiceRoleForCloudWatchAlarms\_ActionSSMIncidents. CloudWatch uses this service-linked role to perform AWS System Manager Incident Manager actions when a CloudWatch alarm goes in to ALARM state. This policy grants permission to start incidents on your behalf.

`AWSCloudWatchAlarms_ActionSSMIncidentsServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCloudWatchAlarms_ActionSSMIncidentsServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSCloudWatchAlarms_ActionSSMIncidentsServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: April 27, 2021, 13:30 UTC 
+ **Edited time:** April 27, 2021, 13:30 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSCloudWatchAlarms_ActionSSMIncidentsServiceRolePolicy`

## Policy version
<a name="AWSCloudWatchAlarms_ActionSSMIncidentsServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCloudWatchAlarms_ActionSSMIncidentsServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "StartIncidentPermissions",
      "Effect" : "Allow",
      "Action" : "ssm-incidents:StartIncident",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSCloudWatchAlarms_ActionSSMIncidentsServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)