• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Tutorial: Delete a maintenance

window using the AWS CLI

To delete a maintenance window you created in these tutorials, run the
following command.

```
aws ssm delete-maintenance-window --window-id "`mw-0c50858d01EXAMPLE`"
```

The system returns information similar to the following.

```
{
   "WindowId":"mw-0c50858d01EXAMPLE"
}
```
