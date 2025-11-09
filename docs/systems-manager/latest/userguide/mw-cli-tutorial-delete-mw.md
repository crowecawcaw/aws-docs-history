AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

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
