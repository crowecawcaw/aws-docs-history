

# AmazonManagedBlockchainConsoleFullAccess
<a name="AmazonManagedBlockchainConsoleFullAccess"></a>

**Description**: Provides full access to Amazon Managed Blockchain via the AWS Management Console

`AmazonManagedBlockchainConsoleFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonManagedBlockchainConsoleFullAccess-how-to-use"></a>

You can attach `AmazonManagedBlockchainConsoleFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonManagedBlockchainConsoleFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: April 29, 2019, 21:23 UTC 
+ **Edited time:** April 29, 2019, 21:23 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonManagedBlockchainConsoleFullAccess`

## Policy version
<a name="AmazonManagedBlockchainConsoleFullAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonManagedBlockchainConsoleFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "managedblockchain:*",
        "ec2:DescribeAvailabilityZones",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeSubnets",
        "ec2:DescribeVpcs",
        "ec2:CreateVpcEndpoint",
        "kms:ListAliases",
        "kms:DescribeKey"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonManagedBlockchainConsoleFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)