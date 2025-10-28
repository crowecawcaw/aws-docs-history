# Editing an assessment in AWS Audit Manager

You might encounter situations where you need to edit your existing assessments in AWS Audit Manager.
Perhaps the scope of your audit has changed, requiring updates to the AWS accounts included in
the assessment. Or, you might need to revise the list of audit owners assigned to the assessment
due to personnel changes. In such cases, you can edit your active assessments and make necessary
adjustments without disrupting your evidence collection.

The following page outlines the steps to edit your assessment details, change the
AWS accounts in scope, update the audit owners, and review and save your changes.

## Prerequisites

The following procedure assumes that you have previously created at least one assessment,
and it is in an active state.

Make sure your IAM identity has appropriate permissions to edit an assessment in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### Tasks

- [Step 1: Edit assessment details](edit-assessment.md#edit-specify-details "edit-assessment.md#edit-specify-details")
- [Step 2: Edit AWS accounts in scope](edit-assessment.md#edit-accounts "edit-assessment.md#edit-accounts")
- [Step 3: Edit audit owners](edit-assessment.md#edit-choose-audit-owners "edit-assessment.md#edit-choose-audit-owners")
  - [Audit owner permissions](edit-assessment.md#edit-choose-audit-owners-permissions "edit-assessment.md#edit-choose-audit-owners-permissions")

- [Step 4: Review and save](edit-assessment.md#edit-review-and-create "edit-assessment.md#edit-review-and-create")

### Step 1: Edit assessment details

Follow these steps to edit the details of your assessment.

###### To edit an assessment

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Assessments**.
3. Select an assessment, and choose **Edit**.
4. Under **Edit assessment details**, edit your assessment details as
   needed.
5. Choose **Next**.

### Step 2: Edit AWS accounts in scope

In this step, you can change which accounts are included in your assessment. Audit Manager can
support up to 200 accounts in the scope of an assessment, and 250 unique member accounts across
all assessments.

###### To edit AWS accounts in scope

1. To add an AWS account, select the check box next to the account name.
2. To remove an AWS account, clear the check box next to the account name.
3. Choose **Next**.

###### Note

To edit the delegated administrator for Audit Manager, see [Changing a delegated administrator](change-delegated-admin.md "change-delegated-admin.md").

### Step 3: Edit audit owners

In this step, you can change which audit owners are included in your assessment.

###### To edit audit owners

1. To add an audit owner, select the check box next to the account name.
2. To remove an audit owner, clear the check box next to the account name.
3. Choose **Next**.

#### Audit owner permissions

The below policy is attached for all the audit owners of an assessment.

Audit Manager replaces the `placeholder text` with your account and
resource identifiers before attaching the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AuditOwner",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`Principal for user/role who are the audit owners of the Assessment`"
 },
 "Action": [
 "auditmanager:GetAssessment",
 "auditmanager:UpdateAssessment",
 "auditmanager:UpdateAssessmentControlSetStatus",
 "auditmanager:UpdateAssessmentStatus",
 "auditmanager:UpdateAssessmentControl",
 "auditmanager:DeleteAssessment",
 "auditmanager:GetChangeLogs",
 "auditmanager:GetEvidenceFoldersByAssessment",
 "auditmanager:GetEvidenceFoldersByAssessmentControl",
 "auditmanager:BatchImportEvidenceToAssessmentControl",
 "auditmanager:GetEvidenceFolder",
 "auditmanager:GetEvidence",
 "auditmanager:GetEvidenceByEvidenceFolder",
 "auditmanager:BatchCreateDelegationByAssessment",
 "auditmanager:BatchDeleteDelegationByAssessment",
 "auditmanager:AssociateAssessmentReportEvidenceFolder",
 "auditmanager:BatchAssociateAssessmentReportEvidence",
 "auditmanager:BatchDisassociateAssessmentReportEvidence",
 "auditmanager:CreateAssessmentReport",
 "auditmanager:DeleteAssessmentReport",
 "auditmanager:DisassociateAssessmentReportEvidenceFolder",
 "auditmanager:GetAssessmentReportUrl"
 ],
 "Resource": [
 "arn:aws:auditmanager:`us-east-1`:`123456789012`:assessment/`assessment_ID`",
 "arn:aws:auditmanager:`us-east-1`:`123456789012`:assessment/`assessment_ID`/*"
 ]
 }
 ]
}`

```

### Step 4: Review and save

Review the information for your assessment. To change the information for a step, choose
**Edit**. When you're finished, choose **Save changes** to
confirm your edits.

After you complete your edits, the changes to the assessment take effect at 00:00 UTC the
following day.

## Next steps

When you no longer need to collect evidence for a specific assessment control, you can
change the status of that control. For instructions, see [Changing the status of an assessment control
in AWS Audit Manager](change-assessment-control-status.md "change-assessment-control-status.md").

When you no longer need to collect evidence for the entire assessment, you can change the
assessment status to inactive. For instructions, see [Changing the status of an assessment to
inactive in AWS Audit Manager](change-assessment-status-to-inactive.md "change-assessment-status-to-inactive.md").

## Additional resources

- For solutions to assessment issues in Audit Manager, see [Troubleshooting assessment and evidence
  collection issues](evidence-collection-issues.md "evidence-collection-issues.md").
- For information about why it's no longer possible to edit services in scope, see [I can't edit the
  services in scope for my assessment](evidence-collection-issues.md#unable-to-edit-services "evidence-collection-issues.md#unable-to-edit-services") in the _Troubleshooting_ section of this guide.
