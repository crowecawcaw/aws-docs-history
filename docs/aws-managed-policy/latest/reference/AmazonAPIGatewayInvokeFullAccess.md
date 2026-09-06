

# AmazonAPIGatewayInvokeFullAccess
<a name="AmazonAPIGatewayInvokeFullAccess"></a>

**Description**: Provides full access to invoke APIs in Amazon API Gateway.

`AmazonAPIGatewayInvokeFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonAPIGatewayInvokeFullAccess-how-to-use"></a>

You can attach `AmazonAPIGatewayInvokeFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonAPIGatewayInvokeFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 09, 2015, 17:36 UTC 
+ **Edited time:** December 18, 2018, 18:25 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonAPIGatewayInvokeFullAccess`

## Policy version
<a name="AmazonAPIGatewayInvokeFullAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonAPIGatewayInvokeFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "execute-api:Invoke",
        "execute-api:ManageConnections"
      ],
      "Resource" : "arn:aws:execute-api:*:*:*"
    }
  ]
}
```

## Learn more
<a name="AmazonAPIGatewayInvokeFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)