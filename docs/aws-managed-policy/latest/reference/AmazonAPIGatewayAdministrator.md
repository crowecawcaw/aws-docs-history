

# AmazonAPIGatewayAdministrator
<a name="AmazonAPIGatewayAdministrator"></a>

**Description**: Provides full access to create/edit/delete APIs in Amazon API Gateway via the AWS Management Console.

`AmazonAPIGatewayAdministrator` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonAPIGatewayAdministrator-how-to-use"></a>

You can attach `AmazonAPIGatewayAdministrator` to your users, groups, and roles.

## Policy details
<a name="AmazonAPIGatewayAdministrator-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 09, 2015, 17:34 UTC 
+ **Edited time:** July 09, 2015, 17:34 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonAPIGatewayAdministrator`

## Policy version
<a name="AmazonAPIGatewayAdministrator-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonAPIGatewayAdministrator-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "apigateway:*"
      ],
      "Resource" : "arn:aws:apigateway:*::/*"
    }
  ]
}
```

## Learn more
<a name="AmazonAPIGatewayAdministrator-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)