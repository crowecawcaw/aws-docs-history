

# AmazonBedrockWebSearchReadOnly
<a name="AmazonBedrockWebSearchReadOnly"></a>

**Description**: Provides read-only access to Amazon Bedrock Web Search. Data remains within the AWS network boundary.

`AmazonBedrockWebSearchReadOnly` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonBedrockWebSearchReadOnly-how-to-use"></a>

You can attach `AmazonBedrockWebSearchReadOnly` to your users, groups, and roles.

## Policy details
<a name="AmazonBedrockWebSearchReadOnly-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: August 03, 2026, 16:57 UTC 
+ **Edited time:** August 03, 2026, 16:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonBedrockWebSearchReadOnly`

## Policy version
<a name="AmazonBedrockWebSearchReadOnly-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonBedrockWebSearchReadOnly-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AmazonBedrockWebSearchReadOnly",
      "Effect" : "Allow",
      "Action" : [
        "bedrock-websearch:InvokeSearch",
        "bedrock-websearch:InvokeFetch"
      ],
      "Resource" : "arn:aws:bedrock-websearch:*:*:*"
    }
  ]
}
```

## Learn more
<a name="AmazonBedrockWebSearchReadOnly-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)