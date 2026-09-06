

# DeclarativePoliciesEC2Report
<a name="DeclarativePoliciesEC2Report"></a>

**Description**: Provides access to read-only APIs needed to run EC2 Declarative Policies Account Status Report.

`DeclarativePoliciesEC2Report` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="DeclarativePoliciesEC2Report-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="DeclarativePoliciesEC2Report-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 30, 2024, 13:21 UTC 
+ **Edited time:** July 03, 2026, 10:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/DeclarativePoliciesEC2Report`

## Policy version
<a name="DeclarativePoliciesEC2Report-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="DeclarativePoliciesEC2Report-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "DeclarativePoliciesEC2Report",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeRegions",
        "ec2:GetSerialConsoleAccessStatus",
        "ec2:GetInstanceMetadataDefaults",
        "ec2:GetImageBlockPublicAccessState",
        "ec2:GetSnapshotBlockPublicAccessState",
        "ec2:GetAllowedImagesSettings",
        "ec2:DescribeVpcBlockPublicAccessOptions",
        "ec2:DescribeAccountVpcEncryptionControl"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="DeclarativePoliciesEC2Report-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)