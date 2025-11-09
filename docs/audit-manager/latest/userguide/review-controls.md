# Reviewing an assessment control in AWS Audit Manager

When you need to review the controls in an assessment, you'll find the information
organized into several sections on the assessment control details page. These sections help you
easily access and understand the relevant information for your task.

###### Contents

- [Prerequisites](review-controls.md#review-controls-prerequisites "review-controls.md#review-controls-prerequisites")
- [Procedure](review-controls.md#review-controls-procedure "review-controls.md#review-controls-procedure")
  - [Control details section](review-controls.md#review-control-detail "review-controls.md#review-control-detail")
  - [Evidence folders tab](review-controls.md#review-evidence-folders "review-controls.md#review-evidence-folders")
  - [Details tab](review-controls.md#review-details "review-controls.md#review-details")
  - [Evidence sources tab](review-controls.md#review-data-sources "review-controls.md#review-data-sources")
  - [Comments tab](review-controls.md#review-comments "review-controls.md#review-comments")
  - [Changelog tab](review-controls.md#review-changelog "review-controls.md#review-changelog")

- [Next steps](review-controls.md#review-controls-next-steps "review-controls.md#review-controls-next-steps")
- [Additional resources](review-controls.md#review-controls-additional-resources "review-controls.md#review-controls-additional-resources")

## Prerequisites

The following procedure assumes that you have previously created at least one assessment.
If you haven’t created an assessment yet, you won’t see any results when you follow these
steps.

Make sure your IAM identity has appropriate permissions to view an assessment in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### To open and review an assessment control details page

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Assessments** and choose the name of
   an assessment to open it.
3. From the assessment page, choose the **Controls** tab, scroll down to
   the **Control sets** table, and then choose the name of a control to open
   it.
4. Review the assessment control details using the following information as
   reference.

###### Sections of the assessment control details page

- [Control details section](#review-control-detail "#review-control-detail")
- [Evidence folders tab](#review-evidence-folders "#review-evidence-folders")
- [Details tab](#review-details "#review-details")
- [Evidence sources tab](#review-data-sources "#review-data-sources")
- [Comments tab](#review-comments "#review-comments")
- [Changelog tab](#review-changelog "#review-changelog")

### Control details section

You can use the **Control details** section to see a summary of the
assessment control.

In this section, you can review the following information:

| Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description**    | The description that's provided for this control.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Control status** | The status of the control.<br>• **Under review** – The control hasn't been reviewed yet.<br>Evidence is still being collected for this control, and you can add manual evidence.<br>This is the default status.<br>• **Reviewed** – The evidence for this control is reviewed.<br>Evidence is still being collected, and you can add manual evidence.<br>• **Inactive** – Automated evidence collection is stopped<br>for this control. You can no longer add manual evidence. |

### Evidence folders tab

You can use this tab to see the evidence that's collected for this control. It's
organized into folders on a daily basis. From here, you can also take the following
actions:

- **Review an evidence folder** – To see details for
  any evidence folder, choose the hyperlinked folder name.
- **Add an evidence folder to an assessment report**
  – To include an evidence folder, select it and choose **Add to assessment
  report**.
- **Remove an evidence folder from an assessment report**
  – To exclude a folder, select it and choose **Remove from assessment
  report**.
- **Add manual evidence** – For instructions, see
  [Adding manual evidence in AWS Audit Manager](upload-evidence.md "upload-evidence.md").

In this section, you can review the following information:

| Name                            | Description                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Evidence folder**             | The name of the evidence folder. The name is based on the date when the evidence was<br>collected or manually added.                                                                                                                                                                                                                                              |
| **Compliance check**            | The number of issues in the evidence folder. This number represents the total number<br>of security issues that were reported directly from AWS Security Hub, AWS Config, or both.<br>If you see **Not applicable**, this indicates that you either don't<br>have Security Hub or AWS Config enabled, or the evidence comes from a different data source<br>type. |
| **Total evidence**              | The total number of evidence items inside the folder.                                                                                                                                                                                                                                                                                                             |
| **Assessment report selection** | The number of evidence items within the folder that are included in the assessment<br>report.                                                                                                                                                                                                                                                                     |

###### Tip

If you can't see the evidence folder that you're looking for, change the dropdown filter
to **All time**. Otherwise, you'll see the last seven days of
folders by default.

### Details tab

In this section, you can review the following information:

| Name                    | Description                                                                |
| ----------------------- | -------------------------------------------------------------------------- |
| **Testing information** | The recommended procedure to test that the control is working as intended. |
| **Action plan**         | The recommended actions to take if the control needs to be remediated.     |

### Evidence sources tab

You can use this tab to see where the assessment control collects evidence from. The
evidence sources can include any of the following:

| Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Common controls** | These are the common controls that collect evidence to support the assessment<br>control.<br>Common controls collect evidence using underlying data sources that AWS manages<br>for you. For every common control that’s listed, Audit Manager collects the relevant evidence for<br>all of the supporting core controls. Choose a common control to see the related core<br>controls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Core controls**   | These are the core controls that collect evidence to support the assessment<br>control.<br>Core controls collect evidence by using a predefined group of data sources that<br>AWS manages for you. Choose a core control to see the underlying data<br>sources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Data sources**    | These are the individual data sources that collect evidence to support the<br>assessment control.<br>• **Name** – The name of the data source.<br>• **Type** – The type of data source that the evidence comes<br>from.<br>+ If Audit Manager collects the evidence, the type can be _AWS Security Hub_, _AWS Config_, _AWS CloudTrail_, or _AWS API<br>calls_.<br>+ If you upload your own evidence, the type is _Manual_. A description indicates if the required manual evidence is a<br>*File upload<br>• or a *Text<br>response*.<br>• **Mapping** – The specific keyword that's used to collect<br>evidence.<br>+ If the type is *AWS Config*, the mapping is an<br>AWS Config rule (such as `SNS_ENCRYPTED_KMS`)<br>+ If the type is *AWS Security Hub*, the mapping is a<br>Security Hub control (such as `EC2.1`).<br>+ If the type is *AWS API calls*, the mapping<br>is an API call (such as `kms_ListKeys`).<br>+ If the type is *AWS CloudTrail\*, the mapping is a<br>CloudTrail event (such as `CreateAccessKey`).<br>• **Frequency** – How often Audit Manager collects evidence for an<br>AWS API call data source. |

### Comments tab

In this tab, you can add a comment about the control and its evidence. You can also see a
list of previous comments.

- Under **Send comments**, you can add comments for a control by
  entering text and then choosing **Submit comments**.
- Under **Previous comments**, you can view a list of previous comments
  along with the date the comment was made and the associated user ID.

### Changelog tab

You can use this tab to see the user activity for the assessment control. The same
information is available as audit trail logs in AWS CloudTrail. With the user activity that's
captured directly in Audit Manager, you can easily review an audit trail of activity for a given
control.

In this section, you can review the following information:

| Name         | Description                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------------ |
| **Date**     | The date and time of the activity, represented in Coordinated Universal Time<br>(UTC).                       |
| **User**     | The user or role that performed the activity.                                                                |
| **Action**   | The action that occurred, such as an assessment being created.                                               |
| **Type**     | The object type that changed, such as an assessment.                                                         |
| **Resource** | The resource that was affected by the change, such as the framework that the<br>assessment was created from. |

Audit Manager tracks the following user activity in changelogs:

- Creating an assessment
- Editing an assessment
- Completing an assessment
- Deleting an assessment
- Delegating a control set for review
- Submitting a reviewed control set back to the audit owner
- Uploading manual evidence
- Updating a control status
- Generating assessment reports

## Next steps

To continue reviewing your assessment, follow the steps in [Reviewing an evidence folder in
AWS Audit Manager](review-evidence-folders-detail.md "review-evidence-folders-detail.md").
This page will guide you through the evidence folders and show you how to understand the
information that you see.

## Additional resources

- [I can’t see any
  controls or control sets in my assessment](control-issues.md#cannot-view-controls "control-issues.md#cannot-view-controls")
