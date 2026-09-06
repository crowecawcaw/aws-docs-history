

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Viewing your notifications for incoming delegation requests
<a name="delegation-for-delegates-viewing-notifications"></a>



When an audit owner requests your assistance with reviewing a control set, you receive a notification that informs you of the control set that they delegated to you. 

## Prerequisites
<a name="delegation-for-delegates-viewing-notifications-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to view notifications in AWS Audit Manager. Two suggested policies that grant these permissions are [Allow users full administrator access to AWS Audit Manager](security_iam_id-based-policy-examples.md#example-2) and [Allow users management access to AWS Audit Manager](security_iam_id-based-policy-examples.md#management-access).

## Procedure
<a name="delegation-for-delegates-viewing-notifications-procedure"></a>

**To view your notifications**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. Choose **Notifications** in the left navigation pane. 

1. On the **Notifications** page, review the list of control sets that have been delegated to you for review. The table includes the following information:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/delegation-for-delegates-viewing-notifications.html)

**Tip**  
You can also subscribe to an SNS topic to receive email alerts when a control set is delegated to you for review. For more information, see [Notifications in AWS Audit Manager](notifications.md).

## Next steps
<a name="delegation-for-delegates-viewing-notifications-next-steps"></a>

When you're ready to start reviewing the controls that were delegated to you, see [Reviewing the delegated control set and its related evidence](delegation-for-delegates-reviewing-control-set-and-evidence.md).