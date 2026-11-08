

# AIDevOpsOrganizationsAccessPolicy
<a name="AIDevOpsOrganizationsAccessPolicy"></a>

**Description**: Provides permissions required by the AWS DevOps Agent to read your organization's structure and to manage the CloudFormation StackSets it creates to deploy roles to your member accounts.

`AIDevOpsOrganizationsAccessPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AIDevOpsOrganizationsAccessPolicy-how-to-use"></a>

You can attach `AIDevOpsOrganizationsAccessPolicy` to your users, groups, and roles.

## Policy details
<a name="AIDevOpsOrganizationsAccessPolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 06, 2026, 22:07 UTC 
+ **Edited time:** November 06, 2026, 22:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AIDevOpsOrganizationsAccessPolicy`

## Policy version
<a name="AIDevOpsOrganizationsAccessPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AIDevOpsOrganizationsAccessPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "OrgSourceStackSets",
      "Effect" : "Allow",
      "Action" : [
        "cloudformation:CreateStackSet",
        "cloudformation:DescribeStackSet",
        "cloudformation:UpdateStackSet",
        "cloudformation:DeleteStackSet",
        "cloudformation:CreateStackInstances",
        "cloudformation:DeleteStackInstances",
        "cloudformation:ListStackInstances",
        "cloudformation:DescribeStackSetOperation",
        "cloudformation:ListStackSetOperations",
        "cloudformation:ListStackSetOperationResults"
      ],
      "Resource" : [
        "arn:aws:cloudformation:*:*:stackset/AIDevOpsOrgSource-*",
        "arn:aws:cloudformation:*:*:stackset-target/AIDevOpsOrgSource-*/*",
        "arn:aws:cloudformation:*:*:type/resource/AWS-IAM-Role",
        "arn:aws:cloudformation:*:*:type/resource/AWS-CloudFormation-WaitConditionHandle"
      ]
    },
    {
      "Sid" : "OrgReads",
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribeOrganization",
        "organizations:DescribeAccount",
        "organizations:DescribeOrganizationalUnit",
        "organizations:ListParents",
        "organizations:ListChildren",
        "organizations:ListRoots",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:ListDelegatedServicesForAccount",
        "organizations:ListDelegatedAdministrators"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AIDevOpsOrganizationsAccessPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)