# Entering free-form text responses as manual

evidence

You can provide additional context and supporting information for an assessment control by
entering free-form text and saving that text as evidence. This allows you to manually document
details that aren’t captured through automatic evidence collection.

For example, you can use Audit Manager to create custom controls that represent questions in a
vendor risk assessment questionnaire. In this case, the name of each control is a specific
question that asks for information about your organization’s security and compliance posture. To
record your response to a given vendor risk assessment question, you can enter a text response
and save it as manual evidence for the control.

## Prerequisites

- When a control is _inactive_, you can't add manual
  evidence to that control. To add manual evidence, you must first [change the
  control status](change-assessment-control-status.md "change-assessment-control-status.md") to either _under review_ or
  _reviewed_.
- Make sure your IAM identity has appropriate permissions to manage an assessment in
  AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
  AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

You can enter text responses using the Audit Manager console, the Audit Manager API, or the AWS Command Line Interface
(AWS CLI).

AWS console

###### Important

We strongly recommend that you never enter any sensitive or personally identifiable
information (PII) as manual evidence. This includes, but is not limited to, Social Security
numbers, addresses, phone numbers, or any other information that could be used to identify
an individual.

###### To enter a text response on the Audit Manager console

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the left navigation pane, choose **Assessments** and then choose
   an assessment.
3. Choose the **Controls** tab, scroll down to **Control
   sets** and then choose a control.
4. From the **Evidence folders** tab, choose **Add manual
   evidence**.
5. Choose **Enter text response**.
6. In the pop-up window that appears, enter your response in plain text format.
7. Choose **Confirm**.

AWS CLI

###### Important

We strongly recommend that you never enter any sensitive or personally identifiable
information (PII) as manual evidence. This includes, but is not limited to, Social Security
numbers, addresses, phone numbers, or any other information that could be used to identify
an individual.

In the following procedure, replace the `placeholder text`
with your own information.

###### To enter a text response in the AWS CLI

1. Run the `list-assessments` command.

```
aws auditmanager list-assessments
```

In the response, find the assessment that you want to upload evidence to and take
note of the assessment ID. 2. Run the `get-assessment` command and specify the assessment ID from step one.

```
aws auditmanager get-assessment --assessment-id `1a2b3c4d-5e6f-7g8h-9i0j-0k1l2m3n4o5p`
```

In the response, find the control set and control that you want to upload evidence
to, and take note of their IDs. 3. Run the `batch-import-evidence-to-assessment-control` command with the following
parameters:

    * `--assessment-id` – Use the assessment ID from step one.
    * `--control-set-id` – Use the control set ID from step two.
    * `--control-id` – Use the control ID from step two.
    * `--manual-evidence` – Use `textResponse` as the manual
     evidence type and enter the text that you want to save as manual evidence.

```
aws auditmanager batch-import-evidence-to-assessment-control --assessment-id `1a2b3c4d-5e6f-7g8h-9i0j-0k1l2m3n4o5p` --control-set-id `ControlSet` --control-id `a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6` --manual-evidence textResponse=`"enter text here"`
```

Audit Manager API

###### Important

We strongly recommend that you never enter any sensitive or personally identifiable
information (PII) as manual evidence. This includes, but is not limited to, Social Security
numbers, addresses, phone numbers, or any other information that could be used to identify
an individual.

###### To enter a text response using the API

1. Call the `ListAssessments` operation. In the response, find the assessment that you
   want to upload evidence to and take note of the assessment ID.
2. Call the `GetAssessment` operation and specify the `assessmentId` from
   step one. In the response, find the control set and control that you want to upload
   evidence to, and take note of their IDs.
3. Call the `BatchImportEvidenceToAssessmentControl` operation with the following
   parameters:
   - `assessmentId` – Use the assessment ID from step one.
   - `controlSetId` – Use the control set ID from step two.
   - `controlId` – Use the control ID from step two.
   - `manualEvidence` – Use `textResponse` as the manual
     evidence type and enter the text that you want to save as manual evidence.

For more information, choose any of the links in the previous procedure to read more in
the _AWS Audit Manager API Reference_. This includes information
about how to use these operations and parameters in one of the language-specific AWS
SDKs.

## Next steps

After you've collected and reviewed the evidence for your assessment, you can generate an
assessment report. For more information, see [Preparing an assessment report in AWS Audit Manager](generate-assessment-report.md "generate-assessment-report.md").
