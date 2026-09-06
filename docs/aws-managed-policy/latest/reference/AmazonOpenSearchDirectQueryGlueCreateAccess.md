

# AmazonOpenSearchDirectQueryGlueCreateAccess
<a name="AmazonOpenSearchDirectQueryGlueCreateAccess"></a>

**Description**: Allows OpenSearch DirectQuery Service to access AWS Glue APIs for creating resources on your behalf.

`AmazonOpenSearchDirectQueryGlueCreateAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonOpenSearchDirectQueryGlueCreateAccess-how-to-use"></a>

You can attach `AmazonOpenSearchDirectQueryGlueCreateAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonOpenSearchDirectQueryGlueCreateAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: May 06, 2024, 12:24 UTC 
+ **Edited time:** May 06, 2024, 12:24 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonOpenSearchDirectQueryGlueCreateAccess`

## Policy version
<a name="AmazonOpenSearchDirectQueryGlueCreateAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonOpenSearchDirectQueryGlueCreateAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AmazonOpenSearchDirectQueryGlueCreateAccess",
      "Effect" : "Allow",
      "Action" : [
        "glue:CreateDatabase",
        "glue:CreatePartition",
        "glue:CreateTable",
        "glue:BatchCreatePartition"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonOpenSearchDirectQueryGlueCreateAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)