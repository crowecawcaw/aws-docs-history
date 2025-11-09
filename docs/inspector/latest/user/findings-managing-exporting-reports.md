# Exporting Amazon Inspector findings reports

A findings report is a CSV or JSON file that provides a detailed snapshot of your findings.
You can export a findings report to AWS Security Hub, Amazon EventBridge, and Amazon Simple Storage Service (Amazon S3).
When you configure a findings report, you specify which findings to include in it.
By default, your findings report includes data for all of your active findings.
If you're the delegated administrator for an organization, your findings report includes data for all member accounts in the organization.
To customize a findings report, create and apply [a filter](findings-managing-filtering.md "findings-managing-filtering.md") to it.

When you export a findings report, Amazon Inspector encrypts your findings data with an AWS KMS key that you specify.
After Amazon Inspector encrypts your findings data, it stores your finding report in an Amazon S3 bucket that you specify.
Your AWS KMS key must be used in the same AWS Region as your Amazon S3 bucket.
Your AWS KMS key policy must allow Amazon Inspector to use it, and your Amazon S3 bucket policy must allow Amazon Inspector to add objects to it.
After you export your findings report, you can download it from your Amazon S3 bucket or transfer it to new location.
You can also use your Amazon S3 bucket as a repository for other exported findings reports.

This section describes how to export a findings report in the Amazon Inspector console.
The following tasks require that you verify your permissions, configure an Amazon S3 bucket, configure an AWS KMS key, and configure and export a findings report.

###### Note

If you export a findings report with the Amazon Inspector [CreateFindingsReport](../../v2/APIReference/API_CreateFindingsReport.md "../../v2/APIReference/API_CreateFindingsReport.md") API, you can only view your active findings.
If you want to view your suppressed or closed findings, you must specify `SUPPRESSED` or `CLOSED` as part of your [filter criteria](../../v2/APIReference/API_FilterCriteria.md "../../v2/APIReference/API_FilterCriteria.md").

###### Tasks

- [Step 1: Verify your permissions](#findings-managing-exporting-permissions "#findings-managing-exporting-permissions")
- [Step 2: Configure an S3
  bucket](#findings-managing-exporting-bucket-perms "#findings-managing-exporting-bucket-perms")
- [Step 3: Configure an
  AWS KMS key](#findings-managing-exporting-KMS "#findings-managing-exporting-KMS")
- [Step 4: Configure and export a
  findings report](#findings-managing-exporting-console "#findings-managing-exporting-console")
- [Troubleshoot
  errors](#findings-managing-access-error "#findings-managing-access-error")

## Step 1: Verify your permissions

###### Note

After you export a findings report for the first time, steps 1–3 are optional.
Following these steps is based on whether you want to use the same Amazon S3 bucket and AWS KMS key for other exported findings reports.
If you want to export a findings report programmatically after completing steps 1–3, use the [CreateFindingsReport](../../v2/APIReference/API_CreateFindingsReport.md "../../v2/APIReference/API_CreateFindingsReport.md") operation of the Amazon Inspector API.

Before you export a findings report from Amazon Inspector, verify that you have the
permissions that you need to both export findings reports and configure resources for
encrypting and storing the reports. To verify your permissions, use AWS Identity and Access Management (IAM) to
review the IAM policies that are attached to your IAM identity. Then compare the
information in those policies to the following list of actions that you must be allowed
to perform to export a findings report.

**Amazon Inspector**

For Amazon Inspector, verify that you're allowed to perform the following
actions:

- `inspector2:ListFindings`
- `inspector2:CreateFindingsReport`

These actions allow you to retrieve findings data for your account and to
export that data in findings reports.

If you plan to export large reports programmatically, you might also
verify that you're allowed to perform the following actions:
`inspector2:GetFindingsReportStatus`, to check the status of
reports, and `inspector2:CancelFindingsReport`, to cancel exports
that are in progress.

**AWS KMS**

For AWS KMS, verify that you're allowed to perform the following
actions:

- `kms:GetKeyPolicy`
- `kms:PutKeyPolicy`

These actions allow you to retrieve and update the key policy for the
AWS KMS key that you want Amazon Inspector to use to encrypt your report.

To use the Amazon Inspector console to export a report, also verify that you're
allowed to perform the following AWS KMS actions:

- `kms:DescribeKey`
- `kms:ListAliases`

These actions allow you to retrieve and display information about the
AWS KMS keys for your account. You can then choose one of these keys to
encrypt your report.

If you plan to create a new KMS key for encryption of your report, you
also need to be allowed to perform the `kms:CreateKey`
action.

**Amazon S3**

For Amazon S3, verify that you're allowed to perform the following
actions:

- `s3:CreateBucket`
- `s3:DeleteObject`
- `s3:PutBucketAcl`
- `s3:PutBucketPolicy`
- `s3:PutBucketPublicAccessBlock`
- `s3:PutObject`
- `s3:PutObjectAcl`

These actions allow you to create and configure the S3 bucket where you
want Amazon Inspector to store your report. They also allow you to add and delete
objects from the bucket.

If you plan to use the Amazon Inspector console to export your report, also
verify that you're allowed to perform the `s3:ListAllMyBuckets`
and `s3:GetBucketLocation` actions. These actions allow you to
retrieve and display information about the S3 buckets for your account. You
can then choose one of these buckets to store the report.

If you're not allowed to perform one or more of the required actions, ask your AWS
administrator for assistance before you proceed to the next step.

## Step 2: Configure an S3

bucket

After you verify your permissions, you're ready to configure the S3 bucket where you
want to store your findings report. It can be an existing bucket for your own account,
or an existing bucket that's owned by another AWS account and you're allowed to
access. If you want to store your report in a new bucket, create the bucket before you
proceed.

The S3 bucket must be in the same AWS Region as the findings data that you want to
export. For example, if you're using Amazon Inspector in the US East (N. Virginia) Region and you want to export
findings data for that Region, the bucket must also be in the US East (N. Virginia) Region.

In addition, the bucket's policy must allow Amazon Inspector to add objects to the bucket. This
topic explains how to update the bucket policy and it provides an example of the
statement to add to the policy. For detailed information about adding and updating
bucket policies, see [Using bucket policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md")
in the _Amazon Simple Storage Service User Guide_.

If you want to store your report in an S3 bucket that's owned by another account, work
with the bucket's owner to update the bucket's policy. Also obtain the URI for the
bucket. You'll need to enter this URI when you export your report.

###### To update the bucket policy

1. Sign in using your credentials, and then open the Amazon S3 console at [https://console.aws.amazon.com/s3](https://console.aws.amazon.com/s3 "https://console.aws.amazon.com/s3").
2. In the navigation pane, choose **Buckets**.
3. Choose the S3 bucket where you want to store the findings report.
4. Choose the **Permissions** tab.
5. In the **Bucket policy** section, choose
   **Edit**.
6. Copy the following example statement to your clipboard:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "allow-inspector",
 "Effect": "Allow",
 "Principal": {
 "Service": "inspector2.amazonaws.com"
 },
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl",
 "s3:AbortMultipartUpload"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:inspector2:`us-east-1`:`111122223333`:report/*"
 }
 }
 }
 ]
}`

```

7. In the **Bucket policy** editor on the Amazon S3 console, paste
   the preceding statement into the policy to add it to the policy.

When you add the statement, ensure that the syntax is valid. Bucket policies
use JSON format. This means that you need to add a comma before or after the
statement, depending on where you add the statement to the policy. If you add
the statement as the last statement, add a comma after the closing brace for the
preceding statement. If you add it as the first statement or between two
existing statements, add a comma after the closing brace for the
statement. 8. Update the statement with the correct values for your environment,
where:

    * `amzn-s3-demo-bucket` is the name of the
     bucket.
    * `111122223333` is the account ID
     for your AWS account.
    * `Region` is the AWS Region in which you're
     using Amazon Inspector and want to allow Amazon Inspector to add reports to the bucket. For
     example, `us-east-1` for the US East (N. Virginia) Region.

###### Note

If you're using Amazon Inspector in a manually enabled AWS Region, also add the
appropriate Region code to the value for the `Service` field.
This field specifies the Amazon Inspector service principal.

For example, if you're using Amazon Inspector in the Middle East (Bahrain) Region, which has the
Region code `me-south-1`, replace
`inspector2.amazonaws.com` with
`inspector2.me-south-1.amazonaws.com` in the
statement.

Note that the example statement defines conditions that use two IAM global
condition keys:

    * [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") – This condition allows Amazon Inspector to
     add reports to the bucket only for your account. It prevents Amazon Inspector from
     adding reports to the bucket for other accounts. More specifically, the
     condition specifies which account can use the bucket for the resources
     and actions specified by the `aws:SourceArn`
     condition.


    To store reports for additional accounts in the bucket, add the
     account ID for each additional account to this condition. For
     example:



    ```
    "aws:SourceAccount": [111122223333,444455556666,123456789012]
    ```
    * [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") – This condition restricts access to
     the bucket based on the source of the objects that are being added to
     the bucket. It prevents other AWS services from adding objects to the
     bucket. It also prevents Amazon Inspector from adding objects to the bucket while
     performing other actions for your account. More specifically, the
     condition allows Amazon Inspector to add objects to the bucket only if the objects
     are findings reports, and only if those reports are created by the
     account and in the Region specified in the condition.


    To allow Amazon Inspector to perform the specified actions for additional
     accounts, add Amazon Resource Names (ARNs) for each additional account
     to this condition. For example:



    ```
    "aws:SourceArn": [
        "arn:aws:inspector2:`Region`:`111122223333`:report/*",
        "arn:aws:inspector2:`Region`:`444455556666`:report/*",
        "arn:aws:inspector2:`Region`:`123456789012`:report/*"
    ]
    ```

    The accounts specified by the `aws:SourceAccount` and
     `aws:SourceArn` conditions should match.

Both conditions help prevent Amazon Inspector from being used as a [confused deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") during transactions with Amazon S3. Although we don’t
recommend it, you can remove these conditions from the bucket policy. 9. When you finish updating the bucket policy, choose **Save
changes**.

## Step 3: Configure an

AWS KMS key

After you verify your permissions and configure the S3 bucket, determine which
AWS KMS key you want Amazon Inspector to use to encrypt your findings report. The key must be a
customer managed, symmetric encryption KMS key. In addition, the key must be in the
same AWS Region as the S3 bucket that you configured to store the report.

The key can be an existing KMS key from your own account, or an existing KMS key
that another account owns. If you want to use a new KMS key, create the key before
proceeding. If you want to use an existing key that another account owns, obtain the
Amazon Resource Name (ARN) of the key. You'll need to enter this ARN when you export
your report from Amazon Inspector. For information about creating and reviewing the settings for
KMS keys, see [Managing keys](../../../kms/latest/developerguide/getting-started.md "../../../kms/latest/developerguide/getting-started.md") in
the _AWS Key Management Service Developer Guide_.

After you determine which KMS key you want to use, give Amazon Inspector permission to use the
key. Otherwise, Amazon Inspector won't be able to encrypt and export the report. To give Amazon Inspector
permission to use the key, update the key policy for the key. For detailed information
about key policies and managing access to KMS keys, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

###### Note

The following procedure is for updating an existing key to allow Amazon Inspector to use it.
If you don't have an existing key, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

###### To update the key policy

1. Sign in using your credentials, and then open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. In the navigation pane, choose **Customer managed
   keys**.
3. Choose the KMS key that you want to use to encrypt the report. The key must
   be a symmetric encryption (**SYMMETRIC_DEFAULT**) key.
4. On the **Key policy** tab, choose **Edit**.
   If you do not see a key policy with an **Edit** button, you
   must first select **Switch to policy view**.
5. Copy the following example statement to your clipboard:

```
{
    "Sid": "Allow Amazon Inspector to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": "inspector2.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey*"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "`111122223333`"
        },
        "ArnLike": {
            "aws:SourceArn": "arn:aws:inspector2:`Region`:`111122223333`:report/*"
        }
    }
}
```

6. In the **Key policy** editor on the AWS KMS console, paste the
   preceding statement into the key policy to add it to the policy.

When you add the statement, ensure that the syntax is valid. Key policies use
JSON format. This means that you need to add a comma before or after the
statement, depending on where you add the statement to the policy. If you add
the statement as the last statement, add a comma after the closing brace for the
preceding statement. If you add it as the first statement or between two
existing statements, add a comma after the closing brace for the
statement. 7. Update the statement with the correct values for your environment,
where:

    * `111122223333` is the account ID
     for your AWS account.
    * `Region` is the AWS Region in which you
     want to allow Amazon Inspector to encrypt reports with the key. For example,
     `us-east-1` for the US East (N. Virginia) Region.

###### Note

If you're using Amazon Inspector in a manually enabled AWS Region, also add the
appropriate Region code to the value for the `Service` field. For
example, if you're using Amazon Inspector in the Middle East (Bahrain) Region, replace
`inspector2.amazonaws.com` with
`inspector2.me-south-1.amazonaws.com`.

Like the example statement for the bucket policy in the preceding step, the
`Condition` fields in this example use two IAM global condition
keys:

    * [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") – This condition allows Amazon Inspector to
     perform the specified actions only for your account. More specifically,
     it determines which account can perform the specified actions for the
     resources and actions specified by the `aws:SourceArn`
     condition.


    To allow Amazon Inspector to perform the specified actions for additional
     accounts, add the account ID for each additional account to this
     condition. For example:



    ```
    "aws:SourceAccount": [111122223333,444455556666,123456789012]
    ```
    * [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") – This condition prevents other
     AWS services from performing the specified actions. It also prevents
     Amazon Inspector from using the key while performing other actions for your
     account. In other words, it allows Amazon Inspector to encrypt S3 objects with the
     key only if the objects are findings reports, and only if those reports
     are created by the account and in the Region specified in the
     condition.


    To allow Amazon Inspector to perform the specified actions for additional
     accounts, add ARNs for each additional account to this condition. For
     example:



    ```
    "aws:SourceArn": [
        "arn:aws:inspector2:us-east-1:111122223333:report/*",
        "arn:aws:inspector2:us-east-1:444455556666:report/*",
        "arn:aws:inspector2:us-east-1:123456789012:report/*"
    ]
    ```

    The accounts specified by the `aws:SourceAccount` and
     `aws:SourceArn` conditions should match.

These conditions help prevent Amazon Inspector from being used as a [confused deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") during transactions with AWS KMS. Although we don’t
recommend it, you can remove these conditions from the statement. 8. When you finish updating the key policy, choose **Save
changes**.

## Step 4: Configure and export a

findings report

###### Note

You only can export only one findings report a time.
If an export is currently in progress, you must wait until the export is complete before exporting another findings report.

After you verify your permissions and you configure resources to encrypt and store
your findings report, you're ready to configure and export the report.

###### To configure and export a findings report

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. In the navigation pane, under **Findings**, choose
   **All findings**.
3. (Optional) By using the filter bar above the **Findings**
   table, [add filter criteria](findings-managing-filtering.md "findings-managing-filtering.md")
   that specify which findings to include in the report. As you add criteria, Amazon Inspector
   updates the table to include only those findings that match the criteria. The
   table provides a preview of the data that your report will contain.

###### Note

We recommend that you add filter criteria. If you don't, the report will
include data for all of your findings in the current AWS Region that have
a status of **Active**. If you're the Amazon Inspector administrator
for an organization, this includes findings data for all the member accounts
in your organization.

If a report includes data for all or many findings, it can take a long
time to generate and export the report, and you can export only one report
at a time. 4. Choose **Export findings**. 5. In the **Export settings** section, for **Export file
type**, specify a file format for the report:

    * To create a JavaScript Object Notation (.json) file that contains the
     data, choose **JSON**.


    If you choose the **JSON** option, the report will
     include all the fields for each finding. For a list of possible JSON
     fields see the [Finding](../../v2/APIReference/API_Finding.md "../../v2/APIReference/API_Finding.md") data type in the Amazon Inspector API
     reference.
    * To create a comma-separated values (.csv) file that contains the data,
     choose **CSV**.


    If you choose the **CSV** option, the report will
     include only a subset of the fields for each finding, approximately 45
     fields that report key attributes of a finding. The fields include:
     *Finding Type, Title, Severity, Status,
     Description, First Seen, Last Seen, Fix Available, AWS account ID,
     Resource ID, Resource Tags*, and *Remediation*. These are in addition to fields that
     capture scoring details and reference URLs for each finding. The
     following is a sample of the CSV headers in a findings report:




    |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | AWS Account Id | Severity | Fix Available | Finding Type | Title | Description | Finding ARN | First Seen | Last Seen | Last Updated | Resource ID | Container Image Tags | Region | Platform | Resource Tags | Affected Packages | Package Installed Version | Fixed in Version | Package Remediation | File Path | Network Paths | Age (Days) | Remediation | Inspector Score | Inspector Score Vector | Status | Vulnerability Id | Vendor | Vendor Severity | Vendor Advisory | Vendor Advisory Published | NVD CVSS3 Score | NVD CVSS3 Vector | NVD CVSS2 Score | NVD CVSS2 Vector | Vendor CVSS3 Score | Vendor CVSS3 Vector | Vendor CVSS2 Score | Vendor CVSS2 Vector | Resource Type | Ami | Resource Public Ipv4 | Resource Private Ipv4 | Resource Ipv6 | Resource Vpc | Port Range | Exploit Available | Last Exploited At | Lambda Layers | Lambda Package Type | Lambda Last Updated At | Reference Urls |

6. Under **Export location**, for **S3 URI**,
   specify the S3 bucket where you want to store the report:
   - To store the report in a bucket that your account owns, choose
     **Browse S3**. Amazon Inspector displays a table of the S3
     buckets for your account. Select the row for the bucket that you want,
     and then choose **Choose**.

   ###### Tip

   To also specify an Amazon S3 path prefix for the report, append a slash
   (/) and the prefix to the value in the **S3 URI**
   box. Amazon Inspector then includes the prefix when it adds the report to the
   bucket, and Amazon S3 generates the path specified by the prefix.

   For example, if you want to use your AWS account ID as a prefix
   and your account ID is _111122223333_, append
   `/111122223333` to the value in
   the **S3 URI** box.

   A _prefix_ is similar to a
   directory path within an S3 bucket. It allows you to group similar
   objects together in a bucket, much like you might store similar
   files together in a folder on a file system. For more information,
   see [Organizing
   objects in the Amazon S3 console using folders](../../../AmazonS3/latest/userguide/using-folders.md "../../../AmazonS3/latest/userguide/using-folders.md") in the
   _Amazon Simple Storage Service User Guide_.
   - To store the report in a bucket that another account owns, enter the
     URI for the bucket—for example,
     `s3://DOC-EXAMPLE_BUCKET`, where _DOC-EXAMPLE_BUCKET_ is the name of the
     bucket. The bucket owner can find this information for you in the
     bucket's properties.

7. For **KMS key**, specify the AWS KMS key that you want
   to use to encrypt the report:
   - To use a key from your own account, choose the key from the list. The
     list displays customer managed, symmetric encryption KMS keys for your
     account.
   - To use a key that another account owns, enter the Amazon Resource Name
     (ARN) of the key. The key owner can find this information for you in the
     key's properties. For more information, see [Finding the key
     ID and key ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md") in the _AWS Key Management Service Developer Guide_.

8. Choose **Export**.

Amazon Inspector generates the findings report, encrypts it with the KMS key that you
specified, and adds it to the S3 bucket that you specified. Depending on the number of
findings that you chose to include in the report, this process can take several minutes
or hours. When the export is complete, Amazon Inspector displays a message indicating that your
findings report was exported successfully. Optionally choose **View
report** in the message to navigate to the report in Amazon S3.

Note that you can export only one report a time. If an export is currently in
progress, wait until that export is complete before you try to export another
report.

## Troubleshoot export errors

If an error occurs when you try to export a findings report, Amazon Inspector displays a message
describing the error. You can use the information in this topic as a guide to identify
possible causes and solutions for the error.

For example, verify that the S3 bucket is in the current AWS Region and the bucket's
policy allows Amazon Inspector to add objects to the bucket. Also verify that the AWS KMS key is
enabled in the current Region, and ensure that the key policy allows Amazon Inspector to use the
key.

After you address the error, try to export the report again.

### Cannot have multiple reports error

If you are attempting to create a report but Amazon Inspector is already generating a report,
you will receive an error stating **Reason: Cannot have multiple reports
in-progress**. This error occurs because Amazon Inspector can only generate one
report for an account at a time.

To resolve the error you can wait for the other report to finish or cancel it before requesting
a new report.

You can check the status of a report by using the [GetFindingsReportStatus](../../v2/APIReference/API_GetFindingsReportStatus.md "../../v2/APIReference/API_GetFindingsReportStatus.md") operation, this operation returns the report ID of any report that is currently being generated.

If you need to, you can use the report ID given by the `GetFindingsReportStatus`
operation to cancel a export that is currently in progress by using the [CancelFindingsReport](../../v2/APIReference/API_CancelFindingsReport.md "../../v2/APIReference/API_CancelFindingsReport.md") operation.
