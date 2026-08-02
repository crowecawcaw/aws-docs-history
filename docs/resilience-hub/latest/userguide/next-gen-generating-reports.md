# Generating compliance and resilience posture reports

**Prerequisites**

Before you can generate a report, your service must have:

- A **report output configuration** specifying the Amazon S3
  bucket where reports are delivered.
- An **invoker role** that trusts the the next generation of Resilience Hub service
  and has permission to write to the configured Amazon S3 bucket.
- At least one **completed assessment** with a status of
  `SUCCESS`.
  You can configure report outputs when creating or updating a service:

```
aws resiliencehubv2 update-service \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/my-service:abc123" \
  --report-configuration '{"reportOutputs": [{"s3": {"bucketPath": "my-report-bucket", "bucketOwner": "123456789012"}}]}'
```

The invoker role must have a permissions policy that grants
`s3:PutObject` on the target bucket. The following example shows the minimum
required policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::my-report-bucket/*"
    }
  ]
}
```

###### Note

If your bucket uses a prefix in the `bucketPath` (for example,
`my-report-bucket/reports`), scope the resource accordingly (for example,
`arn:aws:s3:::my-report-bucket/reports/*`).

###### Note

If your Amazon S3 bucket is configured with SSE-KMS encryption, the invoker role also needs
`kms:GenerateDataKey` and `kms:Encrypt` permissions on the
bucket's KMS key.

**Generating a failure mode assessment report**

To generate a report after running an assessment:

1. Navigate to your service.
2. Choose the **Assessment** tab.
3. Choose **Generate report**.
   **Test run reports**

Test reports are auto-generated after each test run completes if a report destination is
configured. No additional steps are needed. For details on what's included, see [Test runs and report](next-gen-resilience-testing-runs-and-report.md "next-gen-resilience-testing-runs-and-report.md").

**Viewing reports**

In the left-hand navigation, choose **Reports**. The reports
page shows all generated reports (failure mode assessments and test runs) that you have access
to.
