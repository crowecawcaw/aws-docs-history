

# AWSAppMeshEnvoyAccess
<a name="AWSAppMeshEnvoyAccess"></a>

**Description**: App Mesh Envoy policy for accessing Virtual Node configuration.

`AWSAppMeshEnvoyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSAppMeshEnvoyAccess-how-to-use"></a>

You can attach `AWSAppMeshEnvoyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSAppMeshEnvoyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 03, 2019, 21:29 UTC 
+ **Edited time:** July 03, 2019, 21:29 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSAppMeshEnvoyAccess`

## Policy version
<a name="AWSAppMeshEnvoyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSAppMeshEnvoyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "appmesh:StreamAggregatedResources"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSAppMeshEnvoyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)