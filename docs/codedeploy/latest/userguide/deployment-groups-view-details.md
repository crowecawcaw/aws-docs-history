# View deployment group details with

CodeDeploy

You can use the CodeDeploy console, the AWS CLI, or the CodeDeploy APIs to view details about all
deployment groups associated with an application.

###### Topics

- [View deployment group details
  (console)](#deployment-groups-view-details-console "#deployment-groups-view-details-console")
- [View deployment group details
  (CLI)](#deployment-groups-view-details-cli "#deployment-groups-view-details-cli")

## View deployment group details

(console)

To use the CodeDeploy console to view deployment group details:

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, then choose **Applications**. 3. On the **Applications** page, choose the application name
associated with the deployment group.

###### Note

If no entries are displayed, make sure the correct region is selected. On the
navigation bar, in the region selector, choose one of the regions listed in [Region and Endpoints](../../../general/latest/gr/rande.md#codedeploy_region "../../../general/latest/gr/rande.md#codedeploy_region") in the
_AWS General Reference_. CodeDeploy is supported in these regions only. 4. To view details about an individual deployment group, on the
**Deployment groups** tab, choose the name of the
deployment group.

## View deployment group details

(CLI)

To use the AWS CLI to view deployment group details, call either the
`get-deployment-group` command or the `list-deployment-groups`
command.

To view details about a single deployment group, call the
[get-deployment-group](../../../cli/latest/reference/deploy/get-deployment-group.md "../../../cli/latest/reference/deploy/get-deployment-group.md") command, specifying:

- The application name associated with the deployment group. To obtain the
  application name, call the [list-applications](../../../cli/latest/reference/deploy/list-applications.md "../../../cli/latest/reference/deploy/list-applications.md") command.
- The deployment group name. To get the deployment group name, call the
  [list-deployment-groups](../../../cli/latest/reference/deploy/list-deployment-groups.md "../../../cli/latest/reference/deploy/list-deployment-groups.md") command.

To view a list of deployment group names, call the
[list-deployment-groups](../../../cli/latest/reference/deploy/list-deployment-groups.md "../../../cli/latest/reference/deploy/list-deployment-groups.md") command, specifying the application name
associated with the deployment groups. To get the application name, call the
[list-applications](../../../cli/latest/reference/deploy/list-applications.md "../../../cli/latest/reference/deploy/list-applications.md") command.
