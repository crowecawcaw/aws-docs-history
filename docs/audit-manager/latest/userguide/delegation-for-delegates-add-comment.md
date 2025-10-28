# Adding comments about a control during a control set review

You can add comments for any controls that you review. These comments are visible to the
audit owner.

## Prerequisites

Make sure your IAM identity has appropriate permissions to add comments to an
assessment control in AWS Audit Manager. Two suggested policies that grant these permissions are
[Allow users full administrator access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2 "security_iam_id-based-policy-examples.md#example-2") and [Allow users management access to
AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### To add a comment to a control

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. Choose **Notifications** in the left navigation pane.
3. On the **Notifications** page, review the list of control sets
   that were delegated to you.
4. Find the control set that contains the control that you want to leave a comment
   for, then choose the name of the related assessment to open the assessment.
5. Choose the **Controls** tab, scroll down to the **Control
   sets** table, and then select the name of a control to open it.
6. Choose the **Comments** tab.
7. Under **Send comments**, enter your comment in the text box.
8. Choose **Submit comment** to add your comment. Your comment then
   appears under the **Previous comments** section of the page, along with
   any other comments regarding this control.

## Next steps

When you've finished reviewing the control, follow the steps in [Marking a control as
reviewed in AWS Audit Manager](delegation-for-delegates-changing-control-status.md "delegation-for-delegates-changing-control-status.md").
