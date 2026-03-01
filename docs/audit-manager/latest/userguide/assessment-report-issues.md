# Troubleshooting assessment report issues

You can use the information on this page to resolve common assessment report issues in
Audit Manager.

###### Topics

- [My assessment report failed to generate](#assessment-report-checklist "#assessment-report-checklist")
- [I followed the checklist above, and my assessment report still failed to generate](#assessment-report-failed "#assessment-report-failed")
- [I get an access denied error when I try to generate a report](#assessment-report-access-denied-error "#assessment-report-access-denied-error")
- [I’m unable to unzip the assessment report](#cannot-unzip-assessment-report "#cannot-unzip-assessment-report")
- [When I choose an evidence name in a report, I’m not redirected to the evidence details](#cannot-open-evidence-detail-links "#cannot-open-evidence-detail-links")
- [My assessment report generation is stuck in In progress status, and I'm not sure how this impacts my billing](#assessment-report-billing "#assessment-report-billing")
- [Additional resources](#assessment-report-see-also "#assessment-report-see-also")

## My assessment report failed to generate

Your assessment report might have failed to generate for a number of reasons. You
can start to troubleshoot this issue by checking the most frequent causes. Use the
following checklist to get started.

1. Check if any of your AWS Region information doesn't match up:
   1. **Does the AWS Region of your customer managed key
      match the AWS Region of your assessment?**

   If you provided your own KMS key for Audit Manager data encryption, the
   key must be in the same AWS Region as your assessment. To resolve
   this issue, change the KMS key to one that’s in the same Region as
   your assessment. For instructions on how to change the KMS key,
   see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md"). 2. **Does the AWS Region of your customer managed key
   match the AWS Region of your S3 bucket?**

   If you provided your own KMS key for Audit Manager data encryption, the
   key must be in the same AWS Region as the S3 bucket that you use
   as your assessment report destination. To resolve this issue, you
   can change either the KMS key or the S3 bucket so that they’re
   both in the same Region as your assessment. For instructions on how
   to change the KMS key, see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md"). For instructions on how to
   change the S3 bucket, see [Configuring your default assessment report destination](settings-destination.md "settings-destination.md").

2. Check the permissions of the S3 bucket that you’re using as the assessment
   report destination:
   1. **Does the IAM entity that’s generating the
      assessment report have the necessary permissions for the S3
      bucket?**

   The IAM entity must have the required S3 bucket permissions to
   publish reports in that bucket. We provide an [example policy](security_iam_id-based-policy-examples.md#full-administrator-access-assessment-report-destination "security_iam_id-based-policy-examples.md#full-administrator-access-assessment-report-destination") that you can use. 2. **Does the S3 bucket have a bucket policy that
   requires server-side encryption (SSE) using [SSE-KMS](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md#require-sse-kms "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md#require-sse-kms")?**

   If yes, the KMS key that's used in that bucket policy must match
   the KMS key that's specified in your Audit Manager data encryption
   settings. If you didn't configure a KMS key in your Audit Manager settings,
   and your S3 bucket policy requires SSE, ensure that the bucket
   policy allows [SSE-S3](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md"). For instructions on how to change the
   KMS key, see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md"). For instructions on how to
   change the S3 bucket, see [Configuring your default assessment report destination](settings-destination.md "settings-destination.md").

If you’re still unable to successfully generate an assessment report, review the
following issues on this page.

## I followed the checklist above, and my assessment report still failed to generate

Audit Manager limits how much evidence you can add to an assessment report. The limit is
based on the AWS Region of your assessment, the Region of the S3 bucket that's
used as your assessment report destination, and whether your assessment uses a
customer managed AWS KMS key.

1. The limit is 22,000 for same-Region reports (where the S3 bucket and
   assessment are in the same AWS Region)
2. The limit is 3,500 for cross-Region reports (where the S3 bucket and
   assessment are in different AWS Regions)
3. The limit is 3,500 if the assessment uses a customer managed
   KMS key

If you try to generate a report that contains more evidence than this, the
operation might fail.

As a workaround, you can generate multiple assessment reports rather than one
larger assessment report. By doing this, you can export evidence from your
assessment into more manageable-sized batches.

## I get an _access denied_ error when I try to generate a report

You will get an `access denied` error if your assessment was created by
a delegated administrator account that the KMS key that's specified in your Audit Manager
settings doesn't belong to. To avoid this error, when you designate a delegated
administrator for Audit Manager, make sure that the delegated administrator account has
access on the KMS key that you provided when setting up Audit Manager.

You might also receive an `access denied` error if you don't have write
permissions for the S3 bucket that you're using as your assessment report
destination.

If you get an `access denied` error, make sure that you meet the
following requirements:

- Your KMS key in your Audit Manager settings gives permissions to the delegated
  administrator. You can configure this by following the instructions in
  [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the
  _AWS Key Management Service Developer Guide._ For
  instructions on how to review and change your encryption settings in Audit Manager,
  see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md").
- You have a permissions policy that grants you write access for the S3
  bucket that you're using as the assessment report destination. More
  specifically, your permissions policy contains an `s3:PutObject`
  action, specifies the ARN of the S3 bucket, and includes the KMS key
  that's used to encrypt your assessment reports. For an example policy that
  you can use, see [Example 2 (Assessment report destination permissions)](security_iam_id-based-policy-examples.md#full-administrator-access-assessment-report-destination "security_iam_id-based-policy-examples.md#full-administrator-access-assessment-report-destination").

###### Note

If you change your Audit Manager data encryption settings, these changes apply to the
new assessments that you create moving forward. This includes any assessment
reports that you create from your new assessments.

The changes don't apply to existing assessments that you created before you
changed your encryption settings. This includes new assessment reports that you
create from existing assessments, in addition to existing assessment reports.
Existing assessments—and all their assessment reports—continue to use the old
KMS key. If the IAM identity that’s generating the assessment report doesn’t
have permissions to use the old KMS key, you can grant permissions at the key
policy level.

## I’m unable to unzip the assessment report

If you can't unzip the assessment report on Windows, it's likely that Windows
Explorer can't extract it because its file path has several nested folders or long
names. This is because, under the Windows file naming system, the folder path, file
name, and file extension can’t exceed 259 characters. Otherwise, this results in a
`Destination Path Too Long` error.

To resolve this issue, try moving the zip file to the parent folder of its current
location. You can then try again to unzip it from there. Alternatively, you can also
try shortening the name of the zip file or extracting it to a different location
that has a shorter file path.

## When I choose an evidence name in a report, I’m not redirected to the evidence details

This issue might happen if you’re interacting with the assessment report in a
browser, or using the default PDF reader that’s installed on your operating system.
Some browser and system default PDF readers don’t allow the opening of relative
links. This means that, although hyperlinks might work within the assessment report
summary PDF (such as hyperlinked control names in the table of contents), hyperlinks
are ignored when you attempt to navigate away from the assessment summary PDF to a
separate evidence detail PDF.

If you encounter this issue, we recommend that you use a dedicated PDF reader to
interact with your assessment reports. For a reliable experience, we recommend that
you install and use Adobe Acrobat Reader, which you can download at the [Adobe website](https://get.adobe.com/reader/ "https://get.adobe.com/reader/"). Other PDF readers are
also available, but Adobe Acrobat Reader has been proven to work consistently and
reliably with Audit Manager assessment reports.

## My assessment report generation is stuck in _In progress_ status, and I'm not sure how this impacts my billing

Assessment report generation has no impact on billing. You're only billed based on
the evidence that your assessments collect. For more information about pricing, see
[AWS Audit Manager
Pricing](https://aws.amazon.com/audit-manager/pricing/ "https://aws.amazon.com/audit-manager/pricing/").

## Additional resources

The following pages contain troubleshooting guidance about generating an
assessment report from evidence finder:

- [I can’t generate multiple assessment reports from my search results](evidence-finder-issues.md#cannot-generate-multiple-reports-from-search-results "evidence-finder-issues.md#cannot-generate-multiple-reports-from-search-results")
- [I can't include specific evidence from my search results](evidence-finder-issues.md#cannot-add-individual-evidence "evidence-finder-issues.md#cannot-add-individual-evidence")
- [Not all of my evidence finder results are included in the assessment report](evidence-finder-issues.md#not-all-results-present-in-report "evidence-finder-issues.md#not-all-results-present-in-report")
- [I want to generate an assessment report from my search results, but my query statement is failing](evidence-finder-issues.md#querystatement-exceptions "evidence-finder-issues.md#querystatement-exceptions")
