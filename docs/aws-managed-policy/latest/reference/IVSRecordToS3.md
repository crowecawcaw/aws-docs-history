

# IVSRecordToS3
<a name="IVSRecordToS3"></a>

**Description**: Service Linked Role to perform S3 PutObject to recording IVS live streams

`IVSRecordToS3` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="IVSRecordToS3-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="IVSRecordToS3-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: December 05, 2020, 00:10 UTC 
+ **Edited time:** December 05, 2020, 00:10 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/IVSRecordToS3`

## Policy version
<a name="IVSRecordToS3-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="IVSRecordToS3-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:PutObject"
      ],
      "Resource" : [
        "arn:aws:s3:::AWSIVS_*/ivs/*"
      ]
    }
  ]
}
```

## Learn more
<a name="IVSRecordToS3-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)