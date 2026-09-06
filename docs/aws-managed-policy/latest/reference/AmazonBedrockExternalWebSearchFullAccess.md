

# AmazonBedrockExternalWebSearchFullAccess
<a name="AmazonBedrockExternalWebSearchFullAccess"></a>

**Description**: Provides full access to Amazon Bedrock Web Search, including retrieval of content from external websites outside the AWS network boundary.

`AmazonBedrockExternalWebSearchFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonBedrockExternalWebSearchFullAccess-how-to-use"></a>

You can attach `AmazonBedrockExternalWebSearchFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonBedrockExternalWebSearchFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: August 03, 2026, 16:57 UTC 
+ **Edited time:** August 03, 2026, 16:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonBedrockExternalWebSearchFullAccess`

## Policy version
<a name="AmazonBedrockExternalWebSearchFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonBedrockExternalWebSearchFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AmazonBedrockExternalWebSearchFullAccess",
      "Effect" : "Allow",
      "Action" : [
        "bedrock-websearch:InvokeSearch",
        "bedrock-websearch:InvokeFetch",
        "bedrock-websearch:ExternalWebAccess"
      ],
      "Resource" : "arn:aws:bedrock-websearch:*:*:*"
    }
  ]
}
```

## Learn more
<a name="AmazonBedrockExternalWebSearchFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)