

# AWSStepFunctionsReadOnlyAccess
<a name="AWSStepFunctionsReadOnlyAccess"></a>

**Description**: An access policy for providing a user/role/etc read only access to the AWS StepFunctions service.

`AWSStepFunctionsReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSStepFunctionsReadOnlyAccess-how-to-use"></a>

You can attach `AWSStepFunctionsReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSStepFunctionsReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: January 11, 2017, 21:46 UTC 
+ **Edited time:** April 26, 2024, 18:53 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSStepFunctionsReadOnlyAccess`

## Policy version
<a name="AWSStepFunctionsReadOnlyAccess-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSStepFunctionsReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ReadOnlyAccess",
      "Effect" : "Allow",
      "Action" : [
        "states:ListStateMachines",
        "states:ListActivities",
        "states:DescribeStateMachine",
        "states:DescribeStateMachineForExecution",
        "states:ListExecutions",
        "states:DescribeExecution",
        "states:GetExecutionHistory",
        "states:DescribeActivity",
        "states:ListTagsForResource",
        "states:DescribeMapRun",
        "states:ListMapRuns",
        "states:DescribeStateMachineAlias",
        "states:ListStateMachineAliases",
        "states:ListStateMachineVersions",
        "states:ValidateStateMachineDefinition"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSStepFunctionsReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)