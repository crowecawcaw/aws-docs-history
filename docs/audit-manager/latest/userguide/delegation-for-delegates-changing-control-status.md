# Marking a control as reviewed in AWS Audit Manager

You can indicate your review progress by updating the status of individual controls
within a control set.

Changing the control status is optional. However, we recommend that you change the
status of each control to **Reviewed** as you complete your review for that
control. Regardless of the status of each individual control, you can still submit the
controls back to the audit owner.

## Prerequisites

Make sure your IAM identity has appropriate permissions to update an assessment
control status in AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2 "security_iam_id-based-policy-examples.md#example-2") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### To mark a control as reviewed

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. Choose **Notifications** in the left navigation pane.
3. On the **Notifications** page, review the list of control sets
   that were delegated to you.
4. Find the control set that you want to mark as reviewed, then choose the name of
   the related assessment to open the assessment.
5. Under the **Controls** tab of the assessment detail page, scroll
   down to the **Control sets** table.
6. Under the **Controls grouped by control set** column, expand the
   name of a control set to show its controls.
7. Choose the name of a control to open the control detail page.
8. Choose **Update control status** and change the status to
   **Reviewed**.
9. In the pop-up window that appears, choose **Update control
   status** to confirm that you finished reviewing the control.

## Next steps

To complete the delegation process, see
[Submitting a reviewed control set back to the audit owner](delegation-for-delegates-submitting-back-to-audit-owner.md "delegation-for-delegates-submitting-back-to-audit-owner.md").
