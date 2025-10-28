# Delete a trigger

from a CodeDeploy deployment group

Because there is a limit of 10 triggers per deployment group, you might want to delete
triggers if they are no longer being used. You cannot undo the deletion of a trigger,
but you can re-create one.

## Delete a

trigger from a deployment group (console)

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, then choose **Applications**. 3. On the **Applications** page, choose the name of the
application associated with the deployment group where you want to delete a
trigger. 4. On the **Application details** page, choose the
deployment group where you want to delete a trigger. 5. Choose **Edit**. 6. Expand **Advanced - optional**. 7. In the **Triggers** area, choose the trigger you want to
delete, then choose **Delete trigger**. 8. Choose **Save changes**.

## Delete a

trigger from a deployment group (CLI)

To use the CLI to delete a trigger, call the
[update-deployment-group](../../../cli/latest/reference/deploy/update-deployment-group.md "../../../cli/latest/reference/deploy/update-deployment-group.md") command, with empty trigger configuration
parameters, specifying:

- The name of the application associated with the deployment group. To view
  a list of application names, call the [list-applications](../../../cli/latest/reference/deploy/list-applications.md "../../../cli/latest/reference/deploy/list-applications.md")
  command.
- The name of the deployment group associated with the application. To view
  a list of deployment group names, call the
  [list-deployment-groups](../../../cli/latest/reference/deploy/list-deployment-groups.md "../../../cli/latest/reference/deploy/list-deployment-groups.md") command.

For example:

```
aws deploy update-deployment-group --application-name `application-name` --current-deployment-group-name `deployment-group-name` --trigger-configurations
```
