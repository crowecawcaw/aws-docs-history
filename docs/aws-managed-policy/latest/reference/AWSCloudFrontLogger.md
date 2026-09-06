

# AWSCloudFrontLogger
<a name="AWSCloudFrontLogger"></a>

**Description**: Grants CloudFront Logger write permissions to CloudWatch Logs. 

`AWSCloudFrontLogger` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSCloudFrontLogger-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSCloudFrontLogger-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: June 12, 2018, 20:15 UTC 
+ **Edited time:** November 22, 2019, 19:33 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSCloudFrontLogger`

## Policy version
<a name="AWSCloudFrontLogger-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSCloudFrontLogger-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource" : "arn:aws:logs:*:*:log-group:/aws/cloudfront/*"
    }
  ]
}
```

## Learn more
<a name="AWSCloudFrontLogger-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)