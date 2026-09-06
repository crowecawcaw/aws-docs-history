

# Generating an organization-wide compliance report
<a name="enforcement-report"></a>

At any time, you can generate a report that lists all tagged resources in the AWS accounts across your organization. The report shows whether each resource is compliant with the effective tag policy. Note that it can take up to 48 hours for changes you make to a tag policy or resources to be reflected in the organization-wide compliance report. For example, if you have a tag policy that defines a new standardized tag for a resource type, resources of that type that don't have this tag are shown as compliant in the report for up to 48 hours.

You can generate the report from your organization's management account in the `us-east-1` Region, provided that it has access to an Amazon S3 bucket. The bucket must have an attached bucket policy as shown in [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS Resources User Guide*. To generate the report, run the following command:

```
$ aws resourcegroupstaggingapi start-report-creation --s3-bucket amzn-s3-demo-bucket --region us-east-1
```

Replace `amzn-s3-demo-bucket` with the name of your S3 bucket. The bucket must be in the `us-east-1` Region with the bucket policy described in the preceding link.

You can generate one report at a time.

This report can take some time to complete. You can check the status by running the following command:

```
$ aws resourcegroupstaggingapi describe-report-creation --region us-east-1
{
    "Status": "SUCCEEDED"
}
```

After the above command returns `SUCCEEDED`, you can open the report from the Amazon S3 bucket.