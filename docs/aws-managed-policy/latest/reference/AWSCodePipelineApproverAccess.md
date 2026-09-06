

# AWSCodePipelineApproverAccess
<a name="AWSCodePipelineApproverAccess"></a>

**Description**: Provides access to view and approve manual changes for all pipelines

`AWSCodePipelineApproverAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCodePipelineApproverAccess-how-to-use"></a>

You can attach `AWSCodePipelineApproverAccess` to your users, groups, and roles.

## Policy details
<a name="AWSCodePipelineApproverAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 28, 2016, 18:59 UTC 
+ **Edited time:** August 02, 2017, 17:24 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSCodePipelineApproverAccess`

## Policy version
<a name="AWSCodePipelineApproverAccess-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCodePipelineApproverAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "codepipeline:GetPipeline",
        "codepipeline:GetPipelineState",
        "codepipeline:GetPipelineExecution",
        "codepipeline:ListPipelineExecutions",
        "codepipeline:ListPipelines",
        "codepipeline:PutApprovalResult"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSCodePipelineApproverAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)