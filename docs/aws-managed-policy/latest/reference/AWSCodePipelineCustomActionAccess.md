

# AWSCodePipelineCustomActionAccess
<a name="AWSCodePipelineCustomActionAccess"></a>

**Description**: Provides access for custom actions to poll for jobs details (including temporary credentials) and report status updates to AWS CodePipeline.

`AWSCodePipelineCustomActionAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCodePipelineCustomActionAccess-how-to-use"></a>

You can attach `AWSCodePipelineCustomActionAccess` to your users, groups, and roles.

## Policy details
<a name="AWSCodePipelineCustomActionAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 09, 2015, 17:02 UTC 
+ **Edited time:** July 09, 2015, 17:02 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSCodePipelineCustomActionAccess`

## Policy version
<a name="AWSCodePipelineCustomActionAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCodePipelineCustomActionAccess-json"></a>

```
{
  "Statement" : [
    {
      "Action" : [
        "codepipeline:AcknowledgeJob",
        "codepipeline:GetJobDetails",
        "codepipeline:PollForJobs",
        "codepipeline:PutJobFailureResult",
        "codepipeline:PutJobSuccessResult"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ],
  "Version" : "2012-10-17"
}
```

## Learn more
<a name="AWSCodePipelineCustomActionAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)