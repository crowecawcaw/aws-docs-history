

# AmazonLexRunBotsOnly
<a name="AmazonLexRunBotsOnly"></a>

**Description**: Provides access to Amazon Lex conversational APIs.

`AmazonLexRunBotsOnly` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonLexRunBotsOnly-how-to-use"></a>

You can attach `AmazonLexRunBotsOnly` to your users, groups, and roles.

## Policy details
<a name="AmazonLexRunBotsOnly-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: April 11, 2017, 23:06 UTC 
+ **Edited time:** August 18, 2021, 00:15 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonLexRunBotsOnly`

## Policy version
<a name="AmazonLexRunBotsOnly-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonLexRunBotsOnly-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "lex:PostContent",
        "lex:PostText",
        "lex:PutSession",
        "lex:GetSession",
        "lex:DeleteSession",
        "lex:RecognizeText",
        "lex:RecognizeUtterance",
        "lex:StartConversation"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonLexRunBotsOnly-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)