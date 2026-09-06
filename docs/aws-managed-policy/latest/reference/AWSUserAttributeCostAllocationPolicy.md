

# AWSUserAttributeCostAllocationPolicy
<a name="AWSUserAttributeCostAllocationPolicy"></a>

**Description**: Provides read-only access to user attributes from AWS IAM Identity Center for the user attributes that the customer has opted in to.

`AWSUserAttributeCostAllocationPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSUserAttributeCostAllocationPolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSUserAttributeCostAllocationPolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: December 15, 2025, 16:34 UTC 
+ **Edited time:** December 15, 2025, 16:34 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSUserAttributeCostAllocationPolicy`

## Policy version
<a name="AWSUserAttributeCostAllocationPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSUserAttributeCostAllocationPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "iam:GetRole",
      "Resource" : "arn:aws:iam::*:role/aws-service-role/user-attribute-cost-allocation-data.amazonaws.com/AWSServiceRoleForUserAttributeCostAllocation"
    }
  ]
}
```

## Learn more
<a name="AWSUserAttributeCostAllocationPolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)