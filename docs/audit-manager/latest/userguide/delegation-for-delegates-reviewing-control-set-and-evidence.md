# Reviewing the

delegated control set and its related evidence

You can assist audit owners by reviewing the control sets that they have delegated to
you.

You can examine these controls and their related evidence to determine if any additional
action is needed. Such additional action could include [manually uploading additional
evidence](upload-evidence.md "upload-evidence.md") to demonstrate compliance, or [leaving a
comment](delegation-for-delegates-add-comment.md "delegation-for-delegates-add-comment.md") that details the remediation steps that you followed.

## Prerequisites

Make sure your IAM identity has appropriate permissions to view a control set in
AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2 "security_iam_id-based-policy-examples.md#example-2") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### To review a control set

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Notifications**.
3. On the **Notifications** page, you can see a list of control sets
   that were delegated to you. Identify which control set you want to review, and choose
   the name of the related assessment to open the assessment detail page.
4. Under the **Controls** tab of the assessment detail page, scroll
   down to the **Control sets** table.
5. Under the **Controls grouped by control set** column, expand the
   name of a control set to show its controls.
6. Choose the name of a control to open the control detail page.
7. (Optional) Choose **Update control status** to change the status of
   the control. While your review is in progress, you can mark the status as
   **Under Review**.
8. Review information about the control in the **Evidence folders**,
   **Details**, **Data sources**,
   **Comments**, and **Changelog** tabs.
   - To learn about each of these tabs and how to understand the data that they
     contain, see [Reviewing an assessment control in AWS Audit Manager](review-controls.md "review-controls.md").

###### To review the evidence for a control

1. From the control detail page, choose the **Evidence folders** tab.
2. Navigate to the **Evidence folders** table to see a list of folders
   that contain evidence for that control. These folders are organized and named based on
   the date when the evidence was collected.
3. Choose the name of an evidence folder to open it. Then, review a summary of all
   evidence gathered on that date.
   - This summary includes the total number of compliance check issues that were
     reported directly from AWS Security Hub, AWS Config, or both.
   - To learn more about this information, see [Reviewing an evidence folder in
     AWS Audit Manager](review-evidence-folders-detail.md "review-evidence-folders-detail.md").

4. From the evidence folder summary page, navigate to the
   **Evidence** table. Under the **Time** column,
   choose a piece of evidence to open.
5. Review the details of the evidence.
   - To learn more about this information, see [Reviewing evidence in AWS Audit Manager](review-evidence.md "review-evidence.md").

## Next steps

In some cases you might need to provide additional evidence to demonstrate compliance.
In these cases, you can manually upload evidence. For instructions, see [Adding manual evidence in AWS Audit Manager](upload-evidence.md "upload-evidence.md").

If you want to leave comments about one or more of the controls that were delegated to
you, see [Adding comments about a control during a control set review](delegation-for-delegates-add-comment.md "delegation-for-delegates-add-comment.md").
