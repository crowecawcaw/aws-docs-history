

# AWSHealthImagingReadOnlyAccess
<a name="AWSHealthImagingReadOnlyAccess"></a>

**Description**: Provides read only access to AWS Health Imaging service.

`AWSHealthImagingReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSHealthImagingReadOnlyAccess-how-to-use"></a>

You can attach `AWSHealthImagingReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSHealthImagingReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: July 25, 2023, 23:40 UTC 
+ **Edited time:** August 01, 2023, 15:18 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSHealthImagingReadOnlyAccess`

## Policy version
<a name="AWSHealthImagingReadOnlyAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSHealthImagingReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "medical-imaging:GetDICOMImportJob",
        "medical-imaging:GetDatastore",
        "medical-imaging:GetImageFrame",
        "medical-imaging:GetImageSet",
        "medical-imaging:GetImageSetMetadata",
        "medical-imaging:ListDICOMImportJobs",
        "medical-imaging:ListDatastores",
        "medical-imaging:ListImageSetVersions",
        "medical-imaging:ListTagsForResource",
        "medical-imaging:SearchImageSets"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSHealthImagingReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)