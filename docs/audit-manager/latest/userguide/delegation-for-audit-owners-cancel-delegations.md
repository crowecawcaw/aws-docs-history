

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Deleting your completed delegations in AWS Audit Manager
<a name="delegation-for-audit-owners-cancel-delegations"></a>



There may be circumstances where you create a delegation but later no longer need assistance reviewing that control set. When this happens, you can delete an active delegation in Audit Manager. You can also delete completed delegations that you no longer want to see on the delegations page.

## Prerequisites
<a name="delegation-for-audit-owners-cancel-delegations-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to delete a delegation in AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="delegation-for-audit-owners-cancel-delegations-procedure"></a>

**To delete a delegation**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the navigation pane, choose **Delegations**. 

1. On the **Delegations** page, select the delegation that you want to cancel and then choose **Remove delegation**. 

1. In the pop-up window that appears, choose **Delete** to confirm your choice.