

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Approving and denying just-in-time node access requests
<a name="systems-manager-just-in-time-node-access-approve-deny-requests"></a>

Access request approvers can approve or deny just-in-time node access requests from the unified Systems Manager console or using your preferred command line tool. This information is intended for access request approvers. If you don't have the permissions required to approve or reject access requests, contact your administrator. The following procedures describe how to approve or deny just-in-time node access requests.

**To approve or deny just-in-time node access requests using the console**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. Select **Manage node access** in the navigation pane.

1. Select the **Access requests** tab.

1. Select the **Requests for me** toggle.

1. Select the checkbox next to the access request you want to approve or deny.

1. Select **Approve** or **Reject**.

After approving an access request you can revoke your approval at any time by selecting **Revoke**.

**To approve or deny just-in-time node access requests using the command line**

1. Note the access request ID from the notification. For example, {{oi-12345abcdef}}.

1. Run the following command to return details about the access request approval workflow, making sure to replace the {{placeholder values}} with your own information.

   ```
   aws ssm get-ops-item \
       --ops-item-id {{oi-12345abcdef}}
   ```

   Note the `automationExecutionId` value in the `/aws/accessrequest` field for the `OperationalData`. For example, {{9231944f-61c6-40be-8bce-8ee2bEXAMPLE}}.

1. Run the following command to approve or deny the access request. Use the `Approve` signal type to approve the request, and `Deny` to deny the request. Make sure to replace the {{placeholder values}} with your own information.

   ```
   aws ssm send-automation-signal \
       --automation-execution-id {{9231944f-61c6-40be-8bce-8ee2bEXAMPLE}} \
       --signal-type "Approve"
   ```