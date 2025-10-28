# Using Amazon S3 Access Grants with EMR Serverless

## S3 Access Grants overview for EMR Serverless

With Amazon EMR releases 6.15.0 and higher, Amazon S3 Access Grants provide a scalable access control
solution for augmenting access to your Amazon S3 data from EMR Serverless. If you
have a complex or large permission configuration for your S3 data, use Access Grants
to scale S3 data permissions for users, roles, and applications.

Use S3 Access Grants to augment access to Amazon S3 data beyond the permissions granted by the runtime
role or the IAM roles that are attached to the identities with access to your
EMR Serverless application.

For more information, refer to [Managing access with S3 Access Grants for
Amazon EMR](../ManagementGuide/emr-access-grants.md "../ManagementGuide/emr-access-grants.md") in the _Amazon EMR Management Guide_ and [Managing access with S3 Access Grants](../../../AmazonS3/latest/userguide/access-grants.md "../../../AmazonS3/latest/userguide/access-grants.md") in
the _Amazon Simple Storage Service User Guide_.

This section describes how to launch an EMR Serverless application that uses S3 Access Grants to
provide access to data in Amazon S3. For steps to use S3 Access Grants with other Amazon EMR deployments, see the
following documentation:

- [Using S3 Access Grants with Amazon EMR](../ManagementGuide/emr-access-grants.md "../ManagementGuide/emr-access-grants.md")
- [Using S3 Access Grants with
  Amazon EMR on EKS](../EMR-on-EKS-DevelopmentGuide/access-grants.md "../EMR-on-EKS-DevelopmentGuide/access-grants.md")

## Launch an EMR Serverless application with S3 Access Grants

for data management

You can enable S3 Access Grants on EMR Serverless and launch a Spark application. When your
application makes a request for S3 data, Amazon S3 provides temporary credentials that are scoped
to the specific bucket, prefix, or object.

1. Set up a job execution role for your EMR Serverless application. Include the required
   IAM permissions that you must run Spark jobs and use S3 Access Grants,
   `s3:GetDataAccess` and
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

If you specify IAM roles for job execution that have additional permissions to
access S3 directly, then users can access the data permitted by the role
even if they don't have permission from S3 Access Grants. 2. Launch your EMR Serverless application with an Amazon EMR release label of 6.15.0 or
higher and the `spark-defaults` classification, as the following example shows.
Replace the values in `red text` with the
appropriate values for your usage scenario.

```
aws emr-serverless start-job-run \
  --application-id `application-id` \
  --execution-role-arn `job-role-arn` \
  --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://`us-east-1`.elasticmapreduce/emr-containers/samples/wordcount/scripts/wordcount.py",
            "entryPointArguments": ["s3://`amzn-s3-demo-destination-bucket1`/wordcount_output"],
            "sparkSubmitParameters": "--conf spark.executor.cores=1 --conf spark.executor.memory=4g --conf spark.driver.cores=1 --conf spark.driver.memory=4g --conf spark.executor.instances=1"
        }
    }' \
  --configuration-overrides '{
    "applicationConfiguration": [{
        "classification": "spark-defaults",
        "properties": {
          "spark.hadoop.fs.s3.s3AccessGrants.enabled": "true",
          "spark.hadoop.fs.s3.s3AccessGrants.fallbackToIAM": "false"
         }
      }]
}'
```

## S3 Access Grants considerations with

EMR Serverless

For important support, compatibility, and behavioral information when you use Amazon S3 Access Grants
with EMR Serverless, refer to [S3 Access Grants considerations
with Amazon EMR](../ManagementGuide/emr-access-grants.md#emr-access-grants-considerations "../ManagementGuide/emr-access-grants.md#emr-access-grants-considerations") in the _Amazon EMR Management Guide_.
