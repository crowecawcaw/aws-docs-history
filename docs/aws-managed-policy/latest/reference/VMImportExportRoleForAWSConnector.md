

# VMImportExportRoleForAWSConnector
<a name="VMImportExportRoleForAWSConnector"></a>

**Description**: Default policy for the VM Import/Export service role, for customers using the AWS Connector. The VM Import/Export service assumes a role with this policy to fulfill virtual machine migration requests from the AWS Connector virtual appliance. (Note that the AWS Connector uses the "AWSConnector" managed policy to issue requests on the customer's behalf to the VM Import/Export service.) Provides the ability to create AMIs and EBS snapshots, modify EBS snapshot attributes, make "Describe\*" calls on EC2 objects, and read from S3 buckets starting with 'import-to-ec2-'.

`VMImportExportRoleForAWSConnector` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="VMImportExportRoleForAWSConnector-how-to-use"></a>

You can attach `VMImportExportRoleForAWSConnector` to your users, groups, and roles.

## Policy details
<a name="VMImportExportRoleForAWSConnector-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: September 03, 2015, 20:48 UTC 
+ **Edited time:** September 03, 2015, 20:48 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/VMImportExportRoleForAWSConnector`

## Policy version
<a name="VMImportExportRoleForAWSConnector-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="VMImportExportRoleForAWSConnector-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:ListBucket",
        "s3:GetBucketLocation",
        "s3:GetObject"
      ],
      "Resource" : [
        "arn:aws:s3:::import-to-ec2-*"
      ]
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "ec2:ModifySnapshotAttribute",
        "ec2:CopySnapshot",
        "ec2:RegisterImage",
        "ec2:Describe*"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="VMImportExportRoleForAWSConnector-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)