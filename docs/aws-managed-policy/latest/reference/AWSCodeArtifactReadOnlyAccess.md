

# AWSCodeArtifactReadOnlyAccess
<a name="AWSCodeArtifactReadOnlyAccess"></a>

**Description**: Provides read only access to AWS CodeArtifact via the AWS Management Console.

`AWSCodeArtifactReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCodeArtifactReadOnlyAccess-how-to-use"></a>

You can attach `AWSCodeArtifactReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSCodeArtifactReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 25, 2020, 21:23 UTC 
+ **Edited time:** June 25, 2020, 21:23 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSCodeArtifactReadOnlyAccess`

## Policy version
<a name="AWSCodeArtifactReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCodeArtifactReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "codeartifact:Describe*",
        "codeartifact:Get*",
        "codeartifact:List*",
        "codeartifact:ReadFromRepository"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : "sts:GetServiceBearerToken",
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "sts:AWSServiceName" : "codeartifact.amazonaws.com"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSCodeArtifactReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)