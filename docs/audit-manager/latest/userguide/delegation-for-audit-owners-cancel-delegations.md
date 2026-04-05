AWS Audit Manager will no longer be open to new customers starting
April 30, 2026. If you would like to use Audit Manager, sign up prior to that date. Existing customers
can continue to use the service as normal. For more information, see
[AWS Audit Manager availability change](audit-manager-availability-change.md "audit-manager-availability-change.md").

# Deleting your completed delegations in AWS Audit Manager

There may be circumstances where you create a delegation but later no longer need
assistance reviewing that control set. When this happens, you can delete an active
delegation in Audit Manager. You can also delete completed delegations that you no longer want to see
on the delegations page.

## Prerequisites

Make sure your IAM identity has appropriate permissions to delete a delegation in
AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2 "security_iam_id-based-policy-examples.md#example-2") and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access "security_iam_id-based-policy-examples.md#management-access").

## Procedure

###### To delete a delegation

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Delegations**.
3. On the **Delegations** page, select the delegation that you want to
   cancel and then choose **Remove delegation**.
4. In the pop-up window that appears, choose **Delete** to confirm
   your choice.
