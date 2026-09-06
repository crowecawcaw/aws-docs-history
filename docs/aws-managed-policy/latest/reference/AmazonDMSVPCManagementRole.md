

# AmazonDMSVPCManagementRole
<a name="AmazonDMSVPCManagementRole"></a>

**Description**: Provides access to manage VPC settings for AWS managed customer configurations

`AmazonDMSVPCManagementRole` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonDMSVPCManagementRole-how-to-use"></a>

You can attach `AmazonDMSVPCManagementRole` to your users, groups, and roles.

## Policy details
<a name="AmazonDMSVPCManagementRole-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: November 18, 2015, 16:33 UTC 
+ **Edited time:** July 25, 2024, 15:19 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole`

## Policy version
<a name="AmazonDMSVPCManagementRole-version"></a>

**Policy version:** v4 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonDMSVPCManagementRole-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "Statement1",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateNetworkInterface",
        "ec2:DeleteNetworkInterface",
        "ec2:DescribeAvailabilityZones",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeInternetGateways",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeSubnets",
        "ec2:DescribeVpcs",
        "ec2:ModifyNetworkInterfaceAttribute"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonDMSVPCManagementRole-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)