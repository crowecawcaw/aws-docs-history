

# AmazonHealthLakeReadOnlyAccess
<a name="AmazonHealthLakeReadOnlyAccess"></a>

**Description**: Provides read only access to Amazon HealthLake service.

`AmazonHealthLakeReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonHealthLakeReadOnlyAccess-how-to-use"></a>

You can attach `AmazonHealthLakeReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonHealthLakeReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: February 17, 2021, 02:43 UTC 
+ **Edited time:** August 04, 2026, 21:12 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonHealthLakeReadOnlyAccess`

## Policy version
<a name="AmazonHealthLakeReadOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonHealthLakeReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "healthlake:ListFHIRDatastores",
        "healthlake:DescribeFHIRDatastore",
        "healthlake:DescribeFHIRImportJob",
        "healthlake:DescribeFHIRExportJob",
        "healthlake:GetCapabilities",
        "healthlake:ReadResource",
        "healthlake:SearchWithGet",
        "healthlake:SearchWithPost",
        "healthlake:GetDataTransformationProfile",
        "healthlake:ListDataTransformationProfiles",
        "healthlake:ListDataTransformationProfileVersions",
        "healthlake:DescribeDataTransformationJob",
        "healthlake:ListDataTransformationJobs",
        "healthlake:ValidateSource"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonHealthLakeReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)