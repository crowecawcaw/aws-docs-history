

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Adding comments about a control during a control set review
<a name="delegation-for-delegates-add-comment"></a>



You can add comments for any controls that you review. These comments are visible to the audit owner.

## Prerequisites
<a name="delegation-for-delegates-add-comment-prerequisite"></a>

Make sure your IAM identity has appropriate permissions to add comments to an assessment control in AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="delegation-for-delegates-add-comment-procedure"></a>

**To add a comment to a control**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. Choose **Notifications** in the left navigation pane.

1. On the **Notifications** page, review the list of control sets that were delegated to you.

1. Find the control set that contains the control that you want to leave a comment for, then choose the name of the related assessment to open the assessment.

1. Choose the **Controls** tab, scroll down to the **Control sets** table, and then select the name of a control to open it. 

1. Choose the **Comments** tab.

1. Under **Send comments**, enter your comment in the text box.

1. Choose **Submit comment** to add your comment. Your comment then appears under the **Previous comments** section of the page, along with any other comments regarding this control.

## Next steps
<a name="delegation-for-delegates-add-comment-next-steps"></a>

When you've finished reviewing the control, follow the steps in [Marking a control as reviewed in AWS Audit Manager](delegation-for-delegates-changing-control-status.md).