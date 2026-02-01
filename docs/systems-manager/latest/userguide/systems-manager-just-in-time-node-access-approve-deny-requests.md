• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Approving and denying just-in-time node access requests

Access request approvers can approve or deny just-in-time node access requests
from the unified Systems Manager console or using your preferred command line tool. This
information is intended for access request approvers. If you don't have the
permissions required to approve or reject access requests, contact your
administrator. The following procedures describe how to approve or deny just-in-time
node access requests.

###### To approve or deny just-in-time node access requests using the

console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Manage node access** in the navigation
   pane.
3. Select the **Access requests** tab.
4. Select the **Requests for me** toggle.
5. Select the checkbox next to the access request you want to approve or
   deny.
6. Select **Approve** or **Reject**.
   After approving an access request you can revoke your approval at any time by
   selecting **Revoke**.

###### To approve or deny just-in-time node access requests using the command

line

1. Note the access request ID from the notification. For example,
   `oi-12345abcdef`.
2. Run the following command to return details about the access request
   approval workflow, making sure to replace the `placeholder
values` with your own information.

```
aws ssm get-ops-item \
    --ops-item-id `oi-12345abcdef`
```

Note the `automationExecutionId` value in the
`/aws/accessrequest` field for the
`OperationalData`. For example,
`9231944f-61c6-40be-8bce-8ee2bEXAMPLE`. 3. Run the following command to approve or deny the access request. Use the
`Approve` signal type to approve the request, and
`Deny` to deny the request. Make sure to replace the
`placeholder values` with your own
information.

```
aws ssm send-automation-signal \
    --automation-execution-id `9231944f-61c6-40be-8bce-8ee2bEXAMPLE` \
    --signal-type "Approve"
```
