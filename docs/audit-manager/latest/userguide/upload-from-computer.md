# Uploading manual evidence files from your browser

You can manually upload evidence files from your browser into your Audit Manager assessment. This
enables you to supplement the automatically collected evidence with additional supporting
materials.

## Prerequisites

- The maximum supported size for a single manual evidence file is 100 MB.
- You must use one of the [Supported file formats for manual
  evidence](supported-manual-evidence-files.md "supported-manual-evidence-files.md").
- Each AWS account can manually upload up to 100 evidence files to a control each day.
  Exceeding this daily quota causes any additional manual uploads to fail for that control. If
  you need to upload a large amount of manual evidence to a single control, upload your
  evidence in batches across several days.
- When a control is _inactive_, you can't add manual
  evidence to that control. To add manual evidence, you must first [change the
  control status](change-assessment-control-status.md "change-assessment-control-status.md") to either _under review_ or
  _reviewed_.
- Make sure your IAM identity has appropriate permissions to manage an assessment in
  AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
  AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

You can upload a file using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface
(AWS CLI).

AWS console

###### Important

We strongly recommend that you never upload any sensitive or personally identifiable
information (PII) as manual evidence. This includes, but is not limited to, Social Security
numbers, addresses, phone numbers, or any other information that could be used to identify
an individual.

###### To upload a file from your browser on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Assessments** and then choose
   an assessment.
3. On the **Controls** tab, scroll down to **Control
   sets** and then choose a control.
4. From the **Evidence folders** tab, choose **Add manual
   evidence**.
5. Choose **Upload file from browser**.
6. Choose the file that you want to upload.
7. Choose **Upload**.

AWS CLI

###### Important

We strongly recommend that you never upload any sensitive or personally identifiable
information (PII) as manual evidence. This includes, but is not limited to, Social Security
numbers, addresses, phone numbers, or any other information that could be used to identify
an individual.

In the following procedure, replace the `placeholder text`
with your own information.

###### To upload a file from your browser in the AWS CLI

1. Run the `list-assessments` command to see a list of your assessments.

```
aws auditmanager list-assessments
```

In the response, find the assessment that you want to upload evidence to and take
note of the assessment ID. 2. Run the `get-assessment` command and specify the assessment ID from step one.

```
aws auditmanager get-assessment --assessment-id `1a2b3c4d-5e6f-7g8h-9i0j-0k1l2m3n4o5p`
```

In the response, find the control set and the control that you want to upload
evidence to, and take note of their IDs. 3. Run the `get-evidence-file-upload-url` command and specify the file that you want
to upload.

```
aws auditmanager get-evidence-file-upload-url --file-name `fileName.extension`
```

In the response, take note of the presigned URL and the
`evidenceFileName`. 4. Use the presigned URL from step three to upload the file from your browser. This
action uploads your file to Amazon S3, where it's saved as an object that can be attached to an
assessment control. In the following step, you'll reference the newly-created object by
using the `evidenceFileName` parameter.

###### Note

When you upload a file using a presigned URL, Audit Manager protects and stores your data by
using server side encryption with AWS Key Management Service. To support this, you must use the
`x-amz-server-side-encryption` header in your request when you use the
presigned URL to upload your file.

If you're using a customer managed AWS KMS key in your Audit Manager [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md") settings, make sure that you also
include the `x-amz-server-side-encryption-aws-kms-key-id` header in your
request. If the `x-amz-server-side-encryption-aws-kms-key-id` header isn't
present in the request, Amazon S3 assumes that you want to use the AWS managed key.

For more information, see [Protecting data using
server-side encryption with AWS Key Management Service keys (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md") in the _Amazon Simple Storage Service User Guide_. 5. Run the `batch-import-evidence-to-assessment-control` command with the following
parameters:

    * `--assessment-id` – Use the assessment ID from step one.
    * `--control-set-id` – Use the control set ID from step two.
    * `--control-id` – Use the control ID from step two.
    * `--manual-evidence` – Use `evidenceFileName` as the
     manual evidence type and specify the evidence file name from step three.

```
aws auditmanager batch-import-evidence-to-assessment-control --assessment-id `1a2b3c4d-5e6f-7g8h-9i0j-0k1l2m3n4o5p` --control-set-id `ControlSet` --control-id `a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6` --manual-evidence evidenceFileName=`fileName.extension`
```

Audit Manager API

###### Important

We strongly recommend that you never upload any sensitive or personally identifiable
information (PII) as manual evidence. This includes, but is not limited to, Social Security
numbers, addresses, phone numbers, or any other information that could be used to identify
an individual.

###### To upload a file from your browser using the API

1. Call the `ListAssessments` operation. In the response, find the assessment that you
   want to upload evidence to and take note of the assessment ID.
2. Call the `GetAssessment` operation and specify the `assessmentId` from
   step one. In the response, find the control set and the control that you want to upload
   evidence to, and take note of their IDs.
3. Call the `GetEvidenceFileUploadUrl` operation and specify the `fileName`
   that you want to upload. In the response, take note of the presigned URL and the
   `evidenceFileName`.
4. Use the presigned URL from step three to upload the file from your browser. This
   action uploads your file to Amazon S3, where it's saved as an object that can be attached to an
   assessment control. In the following step, you'll reference the newly-created object by
   using the `evidenceFileName` parameter.

###### Note

When you upload a file using a presigned URL, Audit Manager protects and stores your data by
using server side encryption with AWS Key Management Service. To support this, you must use the
`x-amz-server-side-encryption` header in your request when you use the
presigned URL to upload your file.

If you're using a customer managed AWS KMS key in your Audit Manager [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md") settings, make sure that you also
include the `x-amz-server-side-encryption-aws-kms-key-id` header in your
request. If the `x-amz-server-side-encryption-aws-kms-key-id` header isn't
present in the request, Amazon S3 assumes that you want to use the AWS managed key.

For more information, see [Protecting data using
server-side encryption with AWS Key Management Service keys (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md") in the _Amazon Simple Storage Service User Guide_. 5. Call the `BatchImportEvidenceToAssessmentControl` operation with the following
parameters:

    * `assessmentId` – Use the assessment ID from step one.
    * `controlSetId` – Use the control set ID from step two.
    * `controlId` – Use the control ID from step two.
    * `manualEvidence` – Use `evidenceFileName` as the
     manual evidence type and specify the evidence file name from step three.

For more information, choose any of the links in the previous procedure to read more in
the _AWS Audit Manager API Reference_. This includes information
about how to use these operations and parameters in one of the language-specific AWS
SDKs.

## Next steps

After you've collected and reviewed the evidence for your assessment, you can generate an
assessment report. For more information, see [Preparing an assessment report in AWS Audit Manager](generate-assessment-report.md "generate-assessment-report.md").

## Additional resources

To learn which file formats you can use, see [Supported file formats for manual
evidence](supported-manual-evidence-files.md "supported-manual-evidence-files.md").
