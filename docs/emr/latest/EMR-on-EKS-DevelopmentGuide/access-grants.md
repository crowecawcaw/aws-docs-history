# Using Amazon S3 Access Grants with Amazon EMR on EKS

## S3 Access Grants overview for Amazon EMR on EKS

With Amazon EMR releases 6.15.0 and higher, Amazon S3 Access Grants provide a scalable access control
solution that you can use to augment access to your Amazon S3 data from Amazon EMR on EKS. If you have a
complex or large permission configuration for your S3 data, you can use Access Grants to scale
S3 data permissions for users, roles, and applications.

Use S3 Access Grants to augment access to Amazon S3 data beyond the permissions granted by the runtime
role or the IAM roles that are attached to the identities with access to your Amazon EMR on EKS
cluster.

For more information, see [Managing access with S3 Access Grants for
Amazon EMR](../ManagementGuide/emr-access-grants.md "../ManagementGuide/emr-access-grants.md") in the _Amazon EMR Management Guide_ and [Managing access with S3 Access Grants](../../../AmazonS3/latest/userguide/access-grants.md "../../../AmazonS3/latest/userguide/access-grants.md") in
the _Amazon Simple Storage Service User Guide_.

This page describes the requirements to run a Spark job in Amazon EMR on EKS with S3 Access Grants
integration. With Amazon EMR on EKS, S3 Access Grants requires an additional IAM policy statement in the
execution role for your job, and an additional override configuration for the
`StartJobRun` API. For steps to set up S3 Access Grants with other Amazon EMR deployments, see
the following documentation:

- [Using S3 Access Grants with Amazon EMR](../ManagementGuide/emr-access-grants.md "../ManagementGuide/emr-access-grants.md")
- [Using S3 Access Grants with
  EMR Serverless](../EMR-Serverless-UserGuide/access-grants.md "../EMR-Serverless-UserGuide/access-grants.md")

## Launch an Amazon EMR on EKS cluster with S3 Access Grants for data

management

You can enable S3 Access Grants on Amazon EMR on EKS and launch a Spark job. When your application makes a
request for S3 data, Amazon S3 provides temporary credentials that are scoped to the specific
bucket, prefix, or object.

1. Set up a job execution role for your Amazon EMR on EKS cluster. Include the required IAM
   permissions that you need to run Spark jobs, `s3:GetDataAccess` and
   `s3:GetAccessGrantsInstanceForPrefix`:

```
{
    "Effect": "Allow",
    "Action": [
    "s3:GetDataAccess",
    "s3:GetAccessGrantsInstanceForPrefix"
    ],
    "Resource": [     //LIST ALL INSTANCE ARNS THAT THE ROLE IS ALLOWED TO QUERY
         "arn:`aws_partition`:s3:`Region`:`account-id1`:access-grants/default",
         "arn:`aws_partition`:s3:`Region`:`account-id2`:access-grants/default"
    ]
}
```

###### Note

If you specify IAM roles that for job execution that have any additional
permissions to access S3 directly, then users might be able to access data regardless of
the permissions that you define in S3 Access Grants 2. Submit a job to your Amazon EMR on EKS cluster with an Amazon EMR release label of 6.15 or higher
and the `emrfs-site` classification, as the following example shows. Replace
the values in `red text` with the appropriate values
for your usage scenario.

```
{
  "name": "`myjob`",
  "virtualClusterId": "`123456`",
  "executionRoleArn": "`iam_role_name_for_job_execution`",
  "releaseLabel": "`emr-7.9.0-latest`",
  "jobDriver": {
    "sparkSubmitJobDriver": {
      "entryPoint": "`entryPoint_location`",
      "entryPointArguments": ["`argument1`", "`argument2`"],
       "sparkSubmitParameters": "--class `main_class`"
    }
  },
  "configurationOverrides": {
    "applicationConfiguration": [
      {
        "classification": "emrfs-site",
        "properties": {
          "fs.s3.s3AccessGrants.enabled": "true",
          "fs.s3.s3AccessGrants.fallbackToIAM": "false"
         }
      }
    ],
  }
}
```

## S3 Access Grants considerations with Amazon EMR on EKS

For important support, compatibility, and behavioral information when you use Amazon S3 Access Grants
with Amazon EMR on EKS, see [S3 Access Grants considerations
with Amazon EMR](../ManagementGuide/emr-access-grants-considerations.md "../ManagementGuide/emr-access-grants-considerations.md") in the _Amazon EMR Management Guide_.
