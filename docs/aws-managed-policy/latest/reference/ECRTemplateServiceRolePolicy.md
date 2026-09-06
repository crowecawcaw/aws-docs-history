

# ECRTemplateServiceRolePolicy
<a name="ECRTemplateServiceRolePolicy"></a>

**Description**: Allows actions to be performed when using AWS ECR repository creation templates

`ECRTemplateServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="ECRTemplateServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="ECRTemplateServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: June 19, 2024, 23:11 UTC 
+ **Edited time:** June 19, 2024, 23:11 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/ECRTemplateServiceRolePolicy`

## Policy version
<a name="ECRTemplateServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="ECRTemplateServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "CreateRepositoryWithTemplate",
      "Effect" : "Allow",
      "Action" : [
        "ecr:CreateRepository"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="ECRTemplateServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)