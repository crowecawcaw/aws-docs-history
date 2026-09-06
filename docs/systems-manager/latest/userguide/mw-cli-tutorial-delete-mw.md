

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Tutorial: Delete a maintenance window using the AWS CLI
<a name="mw-cli-tutorial-delete-mw"></a>

To delete a maintenance window you created in these tutorials, run the following command.

```
aws ssm delete-maintenance-window --window-id "{{mw-0c50858d01EXAMPLE}}"
```

The system returns information similar to the following.

```
{
   "WindowId":"mw-0c50858d01EXAMPLE"
}
```