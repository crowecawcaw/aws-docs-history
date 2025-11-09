# Reviewing an evidence folder in

AWS Audit Manager

As your assessment collects evidence, Audit Manager organizes it into folders for your convenience.
When you need to review an evidence folder, you'll find the information organized into several
sections.

###### Contents

- [Prerequisites](review-evidence-folders-detail.md#review-evidence-folders-detail-prerequisites "review-evidence-folders-detail.md#review-evidence-folders-detail-prerequisites")
- [Procedure](review-evidence-folders-detail.md#review-evidence-folders-detail-procedure "review-evidence-folders-detail.md#review-evidence-folders-detail-procedure")
  - [Evidence folder summary](review-evidence-folders-detail.md#review-evidence-folders-summary-summary "review-evidence-folders-detail.md#review-evidence-folders-summary-summary")
  - [Evidence table](review-evidence-folders-detail.md#review-evidence-folders-summary-evidence "review-evidence-folders-detail.md#review-evidence-folders-summary-evidence")

- [Next steps](review-evidence-folders-detail.md#review-evidence-folders-detail-next-steps "review-evidence-folders-detail.md#review-evidence-folders-detail-next-steps")
- [Additional
  resources](review-evidence-folders-detail.md#review-evidence-folders-detail-additional-resources "review-evidence-folders-detail.md#review-evidence-folders-detail-additional-resources")

## Prerequisites

The following procedure assumes that you have previously created at least one assessment.
If you haven’t created an assessment yet, you won’t see any results when you follow these
steps.

Make sure your IAM identity has appropriate permissions to view an assessment in
AWS Audit Manager. Two suggested policies that grant these permissions are [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

Keep in mind that it takes up to 24 hours for an assessment to start collecting automated
evidence. If your assessment has no evidence yet, you won’t see any results when you follow
these steps.

## Procedure

###### To open and review an evidence folder

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Assessments**, and then choose an
   assessment.
3. From the assessment page, choose the **Controls** tab, scroll down to
   the **Controls** table, and then choose an assessment control.
4. From the assessment control page, choose the **Evidence folders**
   tab.
5. In the **Evidence folders** table, choose the name of an evidence
   folder.
6. Review the evidence folder using the following information as reference.

###### Sections of an evidence folder page

- [Evidence folder summary](#review-evidence-folders-summary-summary "#review-evidence-folders-summary-summary")
- [Evidence table](#review-evidence-folders-summary-evidence "#review-evidence-folders-summary-evidence")

### Evidence folder summary

You can use the **Summary** section of the page to see a high-level
overview of the evidence in the evidence folder. To learn more about different evidence types,
see [Evidence](concepts.md#evidence "concepts.md#evidence").

![Screenshot of the evidence folder with labels that relate to the following definitions.](images/evidence-summary-console.png)

In this section, you can review the following information:

| Name                              | Description                                                                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Date and time**              | The time and date when the evidence folder was created. This is represented in<br>Coordinated Universal Time (UTC).                                                                        |
| **2. Control**                    | The name of the control that's related the evidence folder.                                                                                                                                |
| **3. Added to assessment report** | The number of evidence items that were selected to be included in the assessment<br>report.                                                                                                |
| **4. Total evidence**             | The total number of evidence items in the evidence folder.                                                                                                                                 |
| **5. Resources**                  | The total number of AWS resources that were assessed when collecting the evidence<br>in this folder.                                                                                       |
| **6. User activity**              | The number of evidence items that fall under the \*user<br>activity<br>• category. This evidence is collected from AWS CloudTrail logs.                                                    |
| **7. Configuration data**         | The number of evidence items that fall under the \*configuration data<br>• category. This evidence is collected from API calls that<br>take configuration snapshots of other AWS services. |
| **8. Manual**                     | The number of evidence items that fall under the \*manual<br>• category. This evidence is added manually.                                                                                  |
| **9. Compliance check**           | The number of evidence items that fall under the \*compliance<br>check<br>• category. This evidence is collected from AWS Config, AWS Security Hub, or<br>both.                            |
| **10. Compliance check status**   | The total number of issues that were reported directly from AWS Security Hub, AWS Config, or<br>both.                                                                                      |

### Evidence table

You can use the **Evidence** table to see the evidence that's contained
within the evidence folder. From here table, you can also take the following actions:

- **Review individual evidence** – To see details for
  any piece of evidence, choose the hyperlinked evidence name under the
  **Time** column.
- **Add evidence to an assessment report** – To
  include evidence, select it and choose **Add to assessment report**.
- **Remove evidence from an assessment report** – To
  exclude evidence, select it and choose **Remove from assessment
  report**.
- **Add manual evidence** – For instructions, see
  [Adding manual evidence in AWS Audit Manager](upload-evidence.md "upload-evidence.md").

In this table, you can review the following information:

| Name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Time**                        | Specifies when the evidence was collected. This also serves as the name of the<br>evidence. The time is represented in Coordinated Universal Time (UTC).                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Compliance check**            | The evaluation status for evidence that falls under the _compliance check<br>• category.<br>• For evidence that's collected from Security Hub, a **Pass** or<br>\*\*Fail_<br>• result is reported directly from Security Hub.<br>• For evidence that's collected from AWS Config, a **Compliant** or<br>**Non-compliant\*<br>• result is reported directly from AWS Config.<br>• If **Not applicable\*\* is shown, this indicates that you either<br>don't have AWS Config or Security Hub enabled, or the evidence comes from a different data<br>source type. |
| **Evidence by type**            | The type of evidence.<br>• **Compliance check** evidence is collected from AWS Config<br>or AWS Security Hub.<br>• **User activity** evidence is collected from<br>AWS CloudTrail.<br>• **Configuration data** evidence is collected from API<br>calls to other AWS services.<br>• **Manual** evidence is evidence that you add<br>manually.                                                                                                                                                                                                                    |
| **Data source**                 | The data source where the evidence is collected from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Event name**                  | The name of the event that invoked the evidence collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Event source**                | The service principal that identifies the relevant AWS service for the<br>event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Resources**                   | The number of resources that were assessed when collecting the evidence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Assessment report selection** | Indicates whether the evidence is included in the assessment report.<br>• To include evidence, select the evidence and choose **Add to assessment<br>report**.<br>• To exclude evidence, select the evidence and choose **Remove from<br>assessment report**.                                                                                                                                                                                                                                                                                                   |

## Next steps

When you're ready to explore the individual pieces of evidence in a folder, follow the
steps in [Reviewing evidence in AWS Audit Manager](review-evidence.md "review-evidence.md"). This page will
guide you through the evidence details and how to interpret the information that you see
there.

## Additional

resources

- For solutions to evidence issues in Audit Manager, see [Troubleshooting assessment and evidence
  collection issues](evidence-collection-issues.md "evidence-collection-issues.md").
