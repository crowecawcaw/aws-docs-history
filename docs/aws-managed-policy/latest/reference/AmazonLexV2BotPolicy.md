

# AmazonLexV2BotPolicy
<a name="AmazonLexV2BotPolicy"></a>

**Description**: Provides Lex V2 bots access to call other AWS services on your behalf.

`AmazonLexV2BotPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonLexV2BotPolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AmazonLexV2BotPolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: January 13, 2021, 20:10 UTC 
+ **Edited time:** January 13, 2021, 20:10 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AmazonLexV2BotPolicy`

## Policy version
<a name="AmazonLexV2BotPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonLexV2BotPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "polly:SynthesizeSpeech"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AmazonLexV2BotPolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)