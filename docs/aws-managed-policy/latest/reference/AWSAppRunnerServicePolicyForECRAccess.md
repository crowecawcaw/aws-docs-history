

# AWSAppRunnerServicePolicyForECRAccess
<a name="AWSAppRunnerServicePolicyForECRAccess"></a>

**Description**: AWS App Runner service policy that grants read permissions to Amazon ECR resources in the customer's account. Use it in a role that is passed to App Runner when creating or updating an App Runner service.

`AWSAppRunnerServicePolicyForECRAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSAppRunnerServicePolicyForECRAccess-how-to-use"></a>

You can attach `AWSAppRunnerServicePolicyForECRAccess` to your users, groups, and roles.

## Policy details
<a name="AWSAppRunnerServicePolicyForECRAccess-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: May 14, 2021, 19:17 UTC 
+ **Edited time:** May 14, 2021, 19:17 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSAppRunnerServicePolicyForECRAccess`

## Policy version
<a name="AWSAppRunnerServicePolicyForECRAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSAppRunnerServicePolicyForECRAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecr:DescribeImages",
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSAppRunnerServicePolicyForECRAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)