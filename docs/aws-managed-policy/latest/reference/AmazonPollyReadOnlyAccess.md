

# AmazonPollyReadOnlyAccess
<a name="AmazonPollyReadOnlyAccess"></a>

**Description**: Grants read-only access to Amazon Polly resources.

`AmazonPollyReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonPollyReadOnlyAccess-how-to-use"></a>

You can attach `AmazonPollyReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonPollyReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 30, 2016, 18:59 UTC 
+ **Edited time:** April 01, 2026, 08:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonPollyReadOnlyAccess`

## Policy version
<a name="AmazonPollyReadOnlyAccess-version"></a>

**Policy version:** v3 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonPollyReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "polly:DescribeVoices",
        "polly:GetLexicon",
        "polly:GetSpeechSynthesisTask",
        "polly:ListLexicons",
        "polly:ListSpeechSynthesisTasks",
        "polly:SynthesizeSpeech",
        "polly:StartSpeechSynthesisStream"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AmazonPollyReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)