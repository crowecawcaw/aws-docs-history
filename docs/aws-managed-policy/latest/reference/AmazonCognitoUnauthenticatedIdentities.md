

# AmazonCognitoUnauthenticatedIdentities
<a name="AmazonCognitoUnauthenticatedIdentities"></a>

**Description**: This policy defines the set of permissions allowed for unauthenticated identities for Cognito Identity Pools. This does not need to be attached to your unauth role, as Cognito Identity Service will automatically include it as a scoped down policy when creating credentials. The privileges to temporarily access other AWS resources through the enhanced flow will now be defined by the intersection of the role associated with the identity of the unauthenticated user provided by a service, and the privileges given in this managed policy that is owned by Cognito.

`AmazonCognitoUnauthenticatedIdentities` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonCognitoUnauthenticatedIdentities-how-to-use"></a>

You can attach `AmazonCognitoUnauthenticatedIdentities` to your users, groups, and roles.

## Policy details
<a name="AmazonCognitoUnauthenticatedIdentities-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: February 01, 2023, 22:36 UTC 
+ **Edited time:** February 01, 2023, 22:36 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonCognitoUnauthenticatedIdentities`

## Policy version
<a name="AmazonCognitoUnauthenticatedIdentities-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonCognitoUnauthenticatedIdentities-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "rum:PutRumEvents",
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonCognitoUnauthenticatedIdentities-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)