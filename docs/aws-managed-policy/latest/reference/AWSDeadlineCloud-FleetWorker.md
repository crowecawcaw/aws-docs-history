

# AWSDeadlineCloud-FleetWorker
<a name="AWSDeadlineCloud-FleetWorker"></a>

**Description**: Provides AWS Deadline Cloud workers with access to run tasks on a farm.

`AWSDeadlineCloud-FleetWorker` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSDeadlineCloud-FleetWorker-how-to-use"></a>

You can attach `AWSDeadlineCloud-FleetWorker` to your users, groups, and roles.

## Policy details
<a name="AWSDeadlineCloud-FleetWorker-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: April 01, 2024, 17:21 UTC 
+ **Edited time:** April 01, 2024, 17:21 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSDeadlineCloud-FleetWorker`

## Policy version
<a name="AWSDeadlineCloud-FleetWorker-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSDeadlineCloud-FleetWorker-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "RunTasksPermissions",
      "Effect" : "Allow",
      "Action" : [
        "deadline:AssumeFleetRoleForWorker",
        "deadline:UpdateWorker",
        "deadline:UpdateWorkerSchedule",
        "deadline:BatchGetJobEntity",
        "deadline:AssumeQueueRoleForWorker"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:PrincipalAccount" : "${aws:ResourceAccount}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSDeadlineCloud-FleetWorker-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)