Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Create an S3 event integration to automatically copy files from Amazon S3 buckets

###### Note

The preview release for auto-copy has ended. Consequently, preview clusters will be automatically removed 30 days after the end of the preview period.
If you plan to continue using auto-copy, we recommend re-creating your existing auto-copy jobs on another Amazon Redshift cluster.
Upgrading a preview cluster to the latest Amazon Redshift version is not supported.

You can use an auto-copy job to load data into your Amazon Redshift tables from files that are stored in Amazon S3.
Amazon Redshift detects when new Amazon S3 files are added to the path specified in your COPY command.
A COPY command is then automatically run without you having to create an external data ingestion pipeline.
Amazon Redshift keeps track of which files have been loaded. Amazon Redshift determines the number of files batched together per COPY command.
You can see the resulting COPY commands in system views.

The first step to create an automatic COPY JOB is to create an S3 event integration.

When a new file appears in the Amazon S3 source bucket, Amazon Redshift then manages loading the files into your database using the COPY command.

## Prerequisites to creating an S3 event integration

To set up your s3 event integration, confirm the following prerequisites are completed.

- Your Amazon S3 bucket must have a bucket policy that allows several Amazon S3 permissions.
  For example, the following example policy allows permissions for the resource bucket `amzn-s3-demo-bucket` that is hosted in `us-east-1`.
  Both the Amazon S3 bucket and the integration are in the same AWS Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Auto-Copy-Policy-01",
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": [
 "s3:GetBucketNotification",
 "s3:PutBucketNotification",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`:*",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:redshift:`us-east-1`:`111122223333`:integration:*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

- Your target Amazon Redshift provisioned cluster or Redshift Serverless namespace must have permission to the bucket. Confirm an IAM role that is associated with your cluster or serverless namesspace has a IAM policy
  that allows the proper permissions.
  The policy must allow both `s3:GetObject` for a bucket resource such as `amzn-s3-demo-bucket`
  and `s3:ListBucket` for a bucket resource and its contents such as ``amzn-s3-demo-bucket`/\*`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AutoCopyReadId",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

Add your policy to an IAM role that has a trust relationship for the role is as follows.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "redshift.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

If your target data warehouse is a provisioned cluster, you can associate an IAM role to your provisioned cluster using the Amazon Redshift console,
**Cluster permissions** tab in your cluster details.
For information about how to associate a role to your provisioned cluster, see
[Associating IAM roles with clusters](../mgmt/copy-unload-iam-role-associating-with-clusters.md "../mgmt/copy-unload-iam-role-associating-with-clusters.md") in the _Amazon Redshift Management Guide_.

If your target data warehouse is Redshift Serverless, you can associate an IAM role to your serverless namespace using the Redshift Serverless console,
**Security and encryption** tab in your namespace details.
For information about how to associate a role to your serverless namespace, see
[Granting permissions to Amazon Redshift Serverless](../mgmt/serverless-security-other-services.md "../mgmt/serverless-security-other-services.md") in the _Amazon Redshift Management Guide_.

- Your Amazon Redshift data warehouse must also have a resource policy that allows the Amazon S3 bucket.
  If you use the Amazon Redshift console, when you create the s3 event integration, Amazon Redshift provides the option **Fix it for me** to add this policy to your Amazon Redshift data warehouse.
  To update a resource policy yourself, you can use the [put-resource-policy](../../../cli/latest/reference/redshift/put-resource-policy.md "../../../cli/latest/reference/redshift/put-resource-policy.md")
  AWS CLI command. For example, to attach a resource policy to your Amazon Redshift provisioned cluster for an S3 event integration with an Amazon S3 bucket, run an AWS CLI command similar to the following.
  The following example shows a policy for a provisioned cluster namespace in the `us-east-1` AWS Region for user account `123456789012`.
  The bucket is named `amzn-s3-demo-bucket`.

```
aws redshift put-resource-policy \
--policy file://rs-rp.json \
--resource-arn "arn:aws:redshift: `us-east-1`:`123456789012`:namespace/cc4ffe56-ad2c-4fd1-a5a2-f29124a56433"
```

Where `rs-rp.json` contains:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "redshift:AuthorizeInboundIntegration",
 "Resource": "arn:aws:redshift:`us-east-1`:`123456789012`:namespace:cc4ffe56-ad2c-4fd1-a5a2-f29124a56433",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "aws:SourceAccount": `111122223333`
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/myRedshiftRole"
 },
 "Action": "redshift:CreateInboundIntegration",
 "Resource": "arn:aws:redshift:`us-east-1`:`123456789012`:namespace:cc4ffe56-ad2c-4fd1-a5a2-f29124a56433",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "aws:SourceAccount": `111122223333`
 }
 }
 }
 ]
}`

```

To attach a resource policy to your Redshift Serverless namespace for an S3 event integration with an Amazon S3 bucket, run a AWS CLI command similar to the following.
The following example shows a policy for a serverless namespace in the `us-east-1` AWS Region for user account `123456789012`.
The bucket is named `amzn-s3-demo-bucket`.

```
aws redshift put-resource-policy \
--policy file://rs-rp.json \
--resource-arn "arn:aws:redshift-serverless:`us-east-1`:`123456789012`:namespace/namespace-1"
```

Where `rs-rp.json` contains:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "redshift:AuthorizeInboundIntegration",
 "Resource": "arn:aws:redshift-serverless:`us-east-1`:`123456789012`:namespace/namespace-1",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "aws:SourceAccount": `111122223333`

 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:user/myUser"
 },
 "Action": "redshift:CreateInboundIntegration",
 "Resource": "arn:aws:redshift-serverless:`us-east-1`:`123456789012`:namespace/namespace-1",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "aws:SourceAccount": `111122223333`
 }
 }
 }
 ]
}`

```

## Create an S3 event integration

To set up your copy job, you first define an S3 event integration.

Amazon Redshift console

###### To create an Amazon S3 event integration on the Amazon Redshift console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. In the left navigation pane, choose **S3 event integrations**.
3. Choose **Create Amazon S3 event integration** to open the wizard to create and S3 event integration to use with auto-copy.
   Your source Amazon S3 bucket and target Amazon Redshift data warehouse must be in the same AWS Region.
   Specify the following information when going through the steps to create an integration:
   - **Integration name** – Is a unique identifier across all integrations owned by your AWS account in the current AWS Region.
   - **Description** – Is text that describes the Amazon S3 event integration for later reference.
   - **Source S3 bucket** – Is the Amazon S3 bucket in the current AWS account and AWS Region which is the source of ingesting data into Amazon Redshift.
   - **Amazon Redshift data warehouse** – Is the target Amazon Redshift provisioned cluster or Redshift Serverless workgroup that receives the data from the integration.

   If your target Amazon Redshift is in the same account, you are able to select the target.
   If the target is in a different account, you specify the **Amazon Redshift data warehouse ARN**.
   The target must have a resource policy with authorized principals and integration source.
   If you do not have the correct resource policies on the target and your target is in the same account, you can select the **Fix it for me** option
   to automatically apply the resource policies during the create integration process.
   If your target is in a different AWS account, you need to apply the resource policy on the Amazon Redshift warehouse manually.

4. Enter up to 50 tag **Keys** and with an optional **Value** – To provide additional metadata about the integration.
5. A review page is shown where you can choose **Create S3 event integration**.

AWS CLI
To create an Amazon S3 event integration using the AWS CLI, use the `create-integration` command with the following options:

- `integration-name` – Specify a name for the integration.
- `source-arn` – Specify the ARN of the Amazon S3 source bucket.
- `target-arn` – Specify the namespace ARN of the Amazon Redshift provisioned cluster or Redshift Serverless workgroup target.

The following example creates an integration by providing the integration name, source ARN, and target ARN. The integration is not encrypted.

```
`aws redshift create-integration \
--integration-name s3-integration \
--source-arn arn:aws:s3:us-east-1::s3-example-bucket \
--target-arn arn:aws:redshift:us-east-1:123456789012:namespace:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`
          `{
 "IntegrationArn": "arn:aws:redshift:us-east-1:123456789012:integration:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "IntegrationName": "s3-integration",
 "SourceArn": "arn:aws:s3:::s3-example-bucket",
 "SourceType": "s3-event-notifications",
 "TargetArn": "arn:aws:redshift:us-east-1:123456789012:namespace:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
 "Status": "creating",
 "Errors": [],
 "CreateTime": "2024-10-09T19:08:52.758000+00:00",
 "Tags": []
}`

```

You can also use the following AWS CLI commands to manage your S3 event integration.

- `delete-integration` – Specify an integration ARN to delete an S3 event integration.
- `modify-integration` – Specify an integration ARN to change the name or description (or both) of an S3 event integration.
- `describe-integrations` – Specify an integration ARN to view properties of an S3 event integration.

See the
[_Amazon Redshift CLI Guide_](../../../cli/latest/reference/redshift.md "../../../cli/latest/reference/redshift.md")
for more information about these commands.

Amazon Redshift then creates an S3 event integration with its associated source and target, status, and information about the status of an associated auto-copy job.
You can view information about an S3 event integration on the Amazon Redshift console by choosing **S3 event integrations**,
and choosing the integration to show its details. Integrations are separated by those created **In my account** and **From other accounts**.
The **In my account** list shows integrations where the source and target are in the same account. The **From other accounts** list shows integrations where
the source is owned by another account.

If you delete an S3 event integration, the corresponding COPY JOB status changes from `1` (active) to `0` (inactive/pending).
However, the corresponding COPY JOB is not automatically dropped. If later you try to create a COPY JOB with the same name, there might be a conflict.

## Create and monitor a COPY JOB

After the integration is created, on the **S3 event integration details** page for the integration you created,
choose **Create autocopy job** to go to Amazon Redshift query editor v2 where you can create the auto-copy job for the integration.
Amazon Redshift matches the bucket in the FROM clause in the COPY JOB CREATE statement to the bucket used in S3 event integration.
For information about how to use Amazon Redshift query editor v2, see
[Querying a database using the Amazon Redshift query editor v2](../mgmt/query-editor-v2.md "../mgmt/query-editor-v2.md") in the _Amazon Redshift Management Guide_.
For example, run the following COPY command in query editor v2 to create an automatic COPY JOB that matches
the Amazon S3 bucket `s3://amzn-s3-demo-bucket/staging-folder` to an Amazon S3 event integration.

```
COPY public.target_table
FROM 's3://amzn-s3-demo-bucket/staging-folder'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyLoadRoleName'
JOB CREATE my_copy_job_name
AUTO ON;

```

You define a COPY JOB one time. The same parameters are used for future runs.

To define and manage a COPY JOB, you must have permission.
For information about granting and revoking permission on a COPY JOB, see
[GRANT](r_GRANT.md "r_GRANT.md") and [REVOKE](r_REVOKE.md "r_REVOKE.md").
For more information about granting and revoking scoped permissions for a COPY JOB, see
[Granting scoped permissions](r_GRANT.md#grant-scoped-syntax "r_GRANT.md#grant-scoped-syntax") and
[Revoking scoped permissions](r_REVOKE.md#revoke-scoped-permissions "r_REVOKE.md#revoke-scoped-permissions").

You manage the load operations using options to CREATE, LIST, SHOW, DROP, ALTER, and RUN jobs.
For more information, see
[COPY JOB](r_COPY-JOB.md "r_COPY-JOB.md").

You can query system views to see the COPY JOB status and progress. Views are provided as follows:

- [SYS_COPY_JOB](SYS_COPY_JOB.md "SYS_COPY_JOB.md") – contains a row for each currently defined COPY JOB.
- [SYS_COPY_JOB_DETAIL](SYS_COPY_JOB_DETAIL.md "SYS_COPY_JOB_DETAIL.md") – contains details on pending, error, and ingested files for each COPY JOB.
- [SYS_COPY_JOB_INFO](SYS_COPY_JOB_INFO.md "SYS_COPY_JOB_INFO.md") – contains messages logged about a COPY JOB.
- [SYS_LOAD_HISTORY](SYS_LOAD_HISTORY.md "SYS_LOAD_HISTORY.md") – contains details of COPY commands.
- [SYS_LOAD_ERROR_DETAIL](SYS_LOAD_ERROR_DETAIL.md "SYS_LOAD_ERROR_DETAIL.md") – contains details of COPY command errors.
- [SVV_COPY_JOB_INTEGRATIONS](SVV_COPY_JOB_INTEGRATIONS.md "SVV_COPY_JOB_INTEGRATIONS.md") – contains details of S3 event integrations.
- [STL_LOAD_ERRORS](r_STL_LOAD_ERRORS.md "r_STL_LOAD_ERRORS.md") – contains errors from COPY commands.
- [STL_LOAD_COMMITS](r_STL_LOAD_COMMITS.md "r_STL_LOAD_COMMITS.md") – contains information used to troubleshoot a COPY command data load.

For information about troubleshooting S3 event integration errors, see
[Troubleshooting S3 event integration and COPY JOB errors](s3-integration-troubleshooting.md "s3-integration-troubleshooting.md").

To get the list of files loaded by a COPY JOB, run the following SQL, but first replace `<job_id>`:

```
SELECT job_id, job_name, data_source, copy_query, filename, status, curtime
FROM sys_copy_job copyjob
JOIN stl_load_commits loadcommit
ON copyjob.job_id = loadcommit.copy_job_id
WHERE job_id = `<job_id>`;
```

## Considerations when creating S3 event integration for auto-copy

Consider the following when using auto-copy.

- You can create a maximum of 200 COPY JOBS for each cluster or workgroup in an AWS account.
- You can create a maximum of 50 S3 event integrations for each Amazon Redshift target.
- You can't create an S3 event integration with a source Amazon S3 bucket which has a period (.) in the bucket name.
- You can only create one S3 event integration between the same source and target.
  That is, there can only be one S3 event integration between an Amazon S3 bucket and a Amazon Redshift data warehouse at a time.
- You can't have any existing event notifications for event type `S3_OBJECT_CREATED` that are defined on the source Amazon S3 bucket.
  However, after an S3 event integration is created, you can update the Amazon S3 bucket event notification with a
  prefix/suffix with a narrower scope. In this way, you can also configure `S3_OBJECT_CREATED` for another prefix/suffix to other targets and avoid
  a conflict with S3 event integration.
  If you experience problems that auto-copy was not running as expected, prepare the AWS CloudTrail log of the `s3:PutBucketNotificationConfiguration`
  action on your S3 bucket for the time frame in question when you contact AWS Support.

## Supported Regions

The following Regions are available for auto-copy.

| Region                     | Auto-copy     |
| -------------------------- | ------------- |
| Africa (Cape Town)         | Available     |
| Asia Pacific (Hong Kong)   | Available     |
| Asia Pacific (Taipei)      | Available     |
| Asia Pacific (Tokyo)       | Available     |
| Asia Pacific (Seoul)       | Available     |
| Asia Pacific (Osaka)       | Available     |
| Asia Pacific (Mumbai)      | Available     |
| Asia Pacific (Hyderabad)   | Available     |
| Asia Pacific (Singapore)   | Available     |
| Asia Pacific (Sydney)      | Available     |
| Asia Pacific (Jakarta)     | Available     |
| Asia Pacific (Melbourne)   | Available     |
| Asia Pacific (Malaysia)    | Available     |
| Asia Pacific (New Zealand) | Not available |
| Asia Pacific (Thailand)    | Available     |
| Canada (Central)           | Available     |
| Canada West (Calgary)      | Available     |
| China (Beijing)            | Available     |
| China (Ningxia)            | Available     |
| Europe (Frankfurt)         | Available     |
| Europe (Zurich)            | Available     |
| Europe (Stockholm)         | Available     |
| Europe (Milan)             | Available     |
| Europe (Spain)             | Available     |
| Europe (Ireland)           | Available     |
| Europe (London)            | Available     |
| Europe (Paris)             | Available     |
| Israel (Tel Aviv)          | Available     |
| Middle East (UAE)          | Available     |
| Middle East (Bahrain)      | Available     |
| Mexico (Central)           | Available     |
| South America (São Paulo)  | Available     |
| US East (N. Virginia)      | Available     |
| US East (Ohio)             | Available     |
| US West (N. California)    | Available     |
| US West (Oregon)           | Available     |
| AWS GovCloud (US-East)     | Available     |
| AWS GovCloud (US-West)     | Available     |
