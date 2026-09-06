

# ResourceGroupsandTagEditorFullAccess
<a name="ResourceGroupsandTagEditorFullAccess"></a>

**Description**: Provides full access to Resource Groups and Tag Editor.

`ResourceGroupsandTagEditorFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="ResourceGroupsandTagEditorFullAccess-how-to-use"></a>

You can attach `ResourceGroupsandTagEditorFullAccess` to your users, groups, and roles.

## Policy details
<a name="ResourceGroupsandTagEditorFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: February 06, 2015, 18:39 UTC 
+ **Edited time:** August 10, 2023, 13:29 UTC
+ **ARN**: `arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess`

## Policy version
<a name="ResourceGroupsandTagEditorFullAccess-version"></a>

**Policy version:** v6 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="ResourceGroupsandTagEditorFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "tag:getResources",
        "tag:getTagKeys",
        "tag:getTagValues",
        "tag:TagResources",
        "tag:UntagResources",
        "resource-groups:*",
        "cloudformation:DescribeStacks",
        "cloudformation:ListStackResources",
        "cloudformation:ListStacks"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="ResourceGroupsandTagEditorFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)