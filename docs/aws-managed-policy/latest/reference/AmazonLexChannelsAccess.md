

# AmazonLexChannelsAccess
<a name="AmazonLexChannelsAccess"></a>

**Description**: This policy allows customers to call Lex runtime from channels

`AmazonLexChannelsAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonLexChannelsAccess-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AmazonLexChannelsAccess-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: January 13, 2021, 20:12 UTC 
+ **Edited time:** January 13, 2021, 20:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AmazonLexChannelsAccess`

## Policy version
<a name="AmazonLexChannelsAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonLexChannelsAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Action" : [
        "lex:ListBots"
      ],
      "Effect" : "Allow",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonLexChannelsAccess-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)