

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Finding and reviewing the delegations that you've sent in AWS Audit Manager
<a name="delegation-for-audit-owners-reviewing-delegations"></a>



You can access a list of your delegations at any time by choosing **Delegations** in the left navigation pane of Audit Manager. The delegations page contains a list of your active and completed delegations.

When a delegation is completed, you receive a notification in Audit Manager. You might also receive comments with remarks from the delegate. The following procedure explains how to check your delegations in Audit Manager after they are completed, and how to view any comments that the delegate might have left for you.

## Prerequisites
<a name="delegation-for-audit-owners-reviewing-delegations-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to view a delegation in AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="delegation-for-audit-owners-reviewing-delegations-procedure"></a>

Follow these steps to find and review the delegations that you previously created.

**To view a completed delegation and check for comments**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Delegations**. 

1. Review the **Delegations** page, which includes a table with the following information:     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-audit-owners-reviewing-delegations.html)

1. Find the assessment and control set that the delegate reviewed and submitted to you, and choose the name of the assessment to open it.

1. Under the **Controls** tab of the assessment detail page, scroll down to the **Control sets** table. 

1. Under **Controls grouped by control set**, find the name of the control set that you delegated.

1. Expand the name of the control set to show its controls, and choose the name of a control to open the control detail page. 

1. Choose the **Comments** tab to view any remarks added by the delegate for that particular control. 

1. When you're satisfied that the review is complete for a control set, select the control set and choose **Complete control set review**. 

**Important**  
Audit Manager collects evidence continuously. As a result, additional new evidence might be collected *after* the delegate completes their review of a control.  
If you only want to use reviewed evidence in your assessment reports, you can refer to the *control reviewed* timestamp to determine when evidence was reviewed. This timestamp can be found on the [Changelog tab](review-controls.md#review-changelog) of the control detail page. You can then use this timestamp to identify which evidence you add to your assessment reports.

## Next steps
<a name="delegation-for-audit-owners-reviewing-delegations-next-steps"></a>

To delete a delegation after it's complete and you no longer need it, see [Deleting your completed delegations in AWS Audit Manager](delegation-for-audit-owners-cancel-delegations.md).