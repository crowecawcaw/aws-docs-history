# Importing manual evidence files from Amazon S3

You can manually import evidence files from an Amazon S3 bucket into your assessment. This
enables you to supplement the automatically collected evidence with additional supporting
materials.

## Prerequisites

- The maximum supported size for a single manual evidence file is 100 MB.
- You must use one of the [Supported file formats for manual evidence](supported-manual-evidence-files.md "supported-manual-evidence-files.md").
- Each AWS account can manually upload up to 100 evidence files to a control each day.
  Exceeding this daily quota causes any additional manual uploads to fail for that control. If
  you need to upload a large amount of manual evidence to a single control, upload your
  evidence in batches across several days.
- When a control is _inactive_, you can't add manual
  evidence to that control. To add manual evidence, you must first [change the
  control status](change-assessment-control-status.md "change-assessment-control-status.md") to either _under review_ or
  _reviewed_.
- Make sure your IAM identity has appropriate permissions to manage an assessment in
  AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

You can import a file using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface
(AWS CLI).

AWS console

###### Important

We strongly recommend that you never import any sensitive or personally identifiable
information (PII) as manual evidence. This includes, but is not limited to, Social Security
numbers, addresses, phone numbers, or any other information that could be used to identify
an individual.

###### To import a file from S3 on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Assessments** and then choose
   an assessment.
3. Choose the **Controls** tab, scroll down to **Control
   sets** and then choose a control.
4. On the **Evidence folders** tab, choose **Add manual
   evidence**, and then choose **Import file from S3**.
5. On the next page, enter the S3 URI of the evidence. You can find the S3 URI by
   navigating to the object in the [Amazon S3 console](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/") and
   choosing **Copy S3 URI**.
6. Choose **Upload**.

AWS CLI

###### Important

We strongly recommend that you never import any sensitive or personally identifiable
information (PII) as manual evidence. This includes, but is not limited to, Social Security
numbers, addresses, phone numbers, or any other information that could be used to identify
an individual.

In the following procedure, replace the `placeholder text`
with your own information.

###### To import a file from S3 in the AWS CLI

1. Run the `list-assessments` command to see a list of your assessments.

```
aws auditmanager list-assessments
```

In the response, find the assessment that you want to upload evidence to and take
note of the assessment ID. 2. Run the `get-assessment` command and specify the assessment ID from step
one.

```
aws auditmanager get-assessment --assessment-id `1a2b3c4d-5e6f-7g8h-9i0j-0k1l2m3n4o5p`
```

In the response, find the control set and the control that you want to upload
evidence to, and take note of their IDs. 3. Run the `batch-import-evidence-to-assessment-control` command with the following
parameters:

    * `--assessment-id` – Use the assessment ID from step one.
    * `--control-set-id` – Use the control set ID from step two.
    * `--control-id` – Use the control ID from step two.
    * `--manual-evidence` – Use `s3ResourcePath` as the
     manual evidence type and specify the S3 URI of the evidence. You can find the S3 URI by
     navigating to the object in the [Amazon S3 console](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/") and
     choosing **Copy S3 URI**.

```
aws auditmanager batch-import-evidence-to-assessment-control --assessment-id `1a2b3c4d-5e6f-7g8h-9i0j-0k1l2m3n4o5p` --control-set-id `ControlSet` --control-id `a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6` --manual-evidence s3ResourcePath=`s3://amzn-s3-demo-bucket/EXAMPLE-FILE.extension`
```

Audit Manager API

###### Important

We strongly recommend that you never import any sensitive or personally identifiable
information (PII) as manual evidence. This includes, but is not limited to, Social Security
numbers, addresses, phone numbers, or any other information that could be used to identify
an individual.

###### To import a file from S3 using the API

1. Call the `ListAssessments` operation to see a list of your assessments. In the
   response, find the assessment that you want to upload evidence to and take note of the
   assessment ID.
2. Call the `GetAssessment` operation and specify the assessment ID from step one. In
   the response, find the control set and the control that you want to upload evidence to,
   and take note of their IDs.
3. Call the `BatchImportEvidenceToAssessmentControl` operation with the following
   parameters:
   - `assessmentId` – Use the assessment ID from step one.
   - `controlSetId` – Use the control set ID from step two.
   - `controlId` – Use the control ID from step two.
   - `manualEvidence` – Use `s3ResourcePath` as the manual
     evidence type and specify the S3 URI of the evidence. You can find the S3 URI by
     navigating to the object in the [Amazon S3 console](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/") and
     choosing **Copy S3 URI**.

For more information, choose any of the links in the previous procedure to read more in
the _AWS Audit Manager API Reference_. This includes information
about how to use these operations and parameters in one of the language-specific AWS
SDKs.

## Next steps

After you've added and reviewed the evidence for your assessment, you can generate an
assessment report. For more information, see [Preparing an assessment report in AWS Audit Manager](generate-assessment-report.md "generate-assessment-report.md").

## Additional resources

To learn which file formats you can use, see [Supported file formats for manual evidence](supported-manual-evidence-files.md "supported-manual-evidence-files.md").
