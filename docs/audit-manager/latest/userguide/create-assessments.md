# Creating an assessment in AWS Audit Manager

This topic builds on the [Tutorial for Audit Owners: Creating an assessment](tutorial-for-audit-owners.md "tutorial-for-audit-owners.md"). You'll find detailed instructions on this page that
show you how to create an assessment from a framework. Follow these steps to create an assessment
and start the ongoing collection of evidence.

## Prerequisites

Before you start this tutorial, make sure that you meet the following conditions:

- You completed all the prerequisites that are described in [Setting up AWS Audit Manager with the recommended settings](setting-up.md "setting-up.md"). You must use your AWS account and the Audit Manager console to
  complete this tutorial.
- Your IAM identity has appropriate permissions to create and manage an assessment in
  Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### Tasks

- [Step 1: Specify assessment details](create-assessments.md#specify-details "create-assessments.md#specify-details")
- [Step 2: Specify AWS accounts in scope](create-assessments.md#specify-accounts "create-assessments.md#specify-accounts")
- [Step 3: Specify audit owners](create-assessments.md#choose-audit-owners "create-assessments.md#choose-audit-owners")
  - [Audit owner permissions](create-assessments.md#choose-audit-owners-permissions "create-assessments.md#choose-audit-owners-permissions")

- [Step 4: Review and create](create-assessments.md#review-and-create "create-assessments.md#review-and-create")

### Step 1: Specify assessment details

Start by selecting a framework and providing basic information for your assessment.

###### To specify assessment details

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Assessments**, and then choose
   **Create assessment**.
3. Under **Name**, enter a name for your assessment.
4. (Optional) Under **Description**, enter a description for your
   assessment.
5. Under **Assessment reports destination**, select the S3 bucket where
   you want to save your assessment reports.

###### Tip

The default assessment report destination is based on your [assessment settings](settings-destination.md "settings-destination.md").
If you prefer, you can create and use multiple S3 buckets to help you organize your
assessment reports for different assessments. AWS Audit Manager supports exporting assessment reports
to Amazon S3 buckets, including cross-account destinations. For optimal security and performance,
we recommend using an S3 bucket in the same AWS account and region as your
assessment. 6. Under **Select framework**, select the framework that you want to
create your assessment from. You can also use the search bar to look up a framework by name,
or by compliance standard or regulation.

###### Tip

To learn more about a framework, choose the framework name to see the framework details
page. 7. (Optional) Under **Tags**, choose **Add new tag** to
associate a tag with your assessment. You can specify a key and a value for each tag. The tag
key is mandatory and can be used as a search criteria when you search for this assessment. 8. Choose **Next**.

###### Note

It's important to make sure that your assessment collects the correct evidence for a
given framework. Before you start evidence collection, we recommend that you review the
requirements for your chosen framework. Then, validate these requirements against your current
AWS Config rule parameters. To ensure that your rule parameters align with framework requirements,
you can [update the rule in
AWS Config](../../../config/latest/developerguide/evaluate-config_manage-rules.md "../../../config/latest/developerguide/evaluate-config_manage-rules.md").

For example, suppose that you’re creating an assessment for CIS v1.2.0. This framework
has a control named [1.9 – Ensure IAM password policy requires a minimum length of 14 or greater](../../../securityhub/latest/userguide/securityhub-cis-controls.md#securityhub-cis-controls-1.9 "../../../securityhub/latest/userguide/securityhub-cis-controls.md#securityhub-cis-controls-1.9"). In
AWS Config, the [iam-password-policy](../../../config/latest/developerguide/iam-password-policy.md "../../../config/latest/developerguide/iam-password-policy.md") rule
has a `MinimumPasswordLength` parameter that checks password length. The default
value for this parameter is 14 characters. As a result, the rule aligns with the control
requirements. If you aren’t using the default parameter value, ensure that the value you’re
using is equal to or greater than the 14 character requirement from CIS v1.2.0. You can find
the default parameter details for each managed rule in the [AWS Config
documentation](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md").

### Step 2: Specify AWS accounts in scope

You can specify multiple AWS accounts to be in the scope of an assessment. Audit Manager supports
multiple accounts through integration with AWS Organizations. This means that Audit Manager assessments can be
run over multiple accounts, and the evidence that's collected is consolidated into a delegated
administrator account. To enable Organizations in Audit Manager, see [Enable and set up AWS Organizations](setup-recommendations.md#enabling-orgs "setup-recommendations.md#enabling-orgs").

###### Note

Audit Manager can support up to 200 accounts in the scope of an assessment. If you try to include
over 200 accounts, the assessment creation will fail.

Additionally, if you try to add over 250 unique accounts across all of your assessments,
the assessment creation will fail.

###### To specify AWS accounts in scope

1. Under **AWS accounts**, select the AWS accounts that you want to
   include in the scope of your assessment.
   - If you enabled Organizations in Audit Manager, multiple accounts are displayed. You can choose one or
     more accounts from the list. Alternatively, you can also search for an account by the
     account name, ID, or email.
   - If you didn't enable Organizations in Audit Manager, only your current AWS account is listed.

2. Choose **Next**.

###### Note

When an in-scope account is removed from your organization, Audit Manager no longer collects
evidence for that account. However, the account continues to show in your assessment under the
**AWS accounts** tab. To remove the account from the list of accounts in
scope, [edit the assessment](edit-assessment.md "edit-assessment.md"). The removed account no longer shows in the list during editing,
and you can save your changes without that account in scope.

### Step 3: Specify audit owners

In this step, you specify the audit owners for your assessment. Audit owners are the
individuals in your workplace—usually from GRC, SecOps, or DevOps teams—who are
responsible for managing the Audit Manager assessment. We recommend that they use the [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") policy.

###### To specify audit owners

1. Under **Audit owners**, review the current list of audit owners. The
   **Audit owner** column displays the user IDs and roles. The
   **AWS account** column displays the AWS account of that audit owner.
2. Audit owners that have a selected check box are included in your assessment. Clear the
   check box for any audit owner to remove them from the assessment. You can find additional
   audit owners by using the search bar to search by name or AWS account.
3. When you're finished, choose **Next**.

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

### Step 4: Review and create

Review the information for your assessment. To change the information for a step, choose
**Edit**. When you're finished, choose **Create
assessment**.

This action starts the ongoing collection of evidence for your assessment. After you
create an assessment, evidence collection continues until you [change the
assessment status](change-assessment-status-to-inactive.md "change-assessment-status-to-inactive.md") to _inactive_. Alternatively, you
can stop evidence collection for a specific control by [change the control
status](change-assessment-control-status.md "change-assessment-control-status.md") to _inactive_.

###### Note

Automated evidence becomes available 24 hours after your assessment is created. Audit Manager
automatically collects evidence from multiple data sources, and the frequency of that evidence
collection is based on the evidence type. To learn more, see [Evidence collection frequency](how-evidence-is-collected.md#frequency "how-evidence-is-collected.md#frequency") in this guide.

## Next steps

To revisit your assessment at a later date, see [Finding your assessments in AWS Audit Manager](access-assessments.md "access-assessments.md"). You can follow these steps to locate your assessment so
that you can view, edit, or continue working on it.

## Additional resources

For solutions to assessment issues in Audit Manager, see [Troubleshooting assessment and evidence collection issues](evidence-collection-issues.md "evidence-collection-issues.md").
