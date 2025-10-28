# Delete a deployment group with CodeDeploy

You can use the CodeDeploy console, the AWS CLI, or the CodeDeploy APIs to delete deployment groups
associated with your AWS account.

###### Warning

If you delete a deployment group, all details associated with that deployment group
will also be deleted from CodeDeploy. The instances used in the deployment group will remain
unchanged. This action cannot be undone.

###### Topics

- [Delete a deployment group
  (console)](#deployment-groups-delete-console "#deployment-groups-delete-console")
- [Delete a deployment group (CLI)](#deployment-groups-delete-cli "#deployment-groups-delete-cli")

## Delete a deployment group

(console)

To use the CodeDeploy console to delete a deployment group:

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, then choose **Applications**. 3. In the list of applications, choose the name of the application associated
with the deployment group. 4. On the **Application details** page, on the
**Deployment groups** tab, choose the name of the
deployment group you want to delete. 5. On the **Deployment details** page, choose
**Delete**. 6. When prompted, type the name of the deployment group to confirm you want to
delete it, and then choose **Delete**.

## Delete a deployment group (CLI)

To use the AWS CLI to delete a deployment group, call the
[delete-deployment-group](../../../cli/latest/reference/deploy/delete-deployment-group.md "../../../cli/latest/reference/deploy/delete-deployment-group.md") command, specifying:

- The name of the application associated with the deployment group. To view a
  list of application names, call the [list-applications](../../../cli/latest/reference/deploy/list-applications.md "../../../cli/latest/reference/deploy/list-applications.md")
  command.
- The name of the deployment group associated with the application. To view a
  list of deployment group names, call the [list-deployment-groups](../../../cli/latest/reference/deploy/list-deployment-groups.md "../../../cli/latest/reference/deploy/list-deployment-groups.md")
  command.
