# View instance details with CodeDeploy

You can use the CodeDeploy console, the AWS CLI, or the CodeDeploy APIs to view details about
instances used in a deployment.

For information about using CodeDeploy API actions to view instances, see [GetDeploymentInstance](../APIReference/API_GetDeploymentInstance.md "../APIReference/API_GetDeploymentInstance.md"), [ListDeploymentInstances](../APIReference/API_ListDeploymentInstances.md "../APIReference/API_ListDeploymentInstances.md"), and
[ListOnPremisesInstances](../APIReference/API_ListOnPremisesInstances.md "../APIReference/API_ListOnPremisesInstances.md").

###### Topics

- [View instance details (console)](#instances-view-details-console "#instances-view-details-console")
- [View instance details (CLI)](#instances-view-details-cli "#instances-view-details-cli")

## View instance details (console)

To view instance details:

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, and then choose **Deployments**.

###### Note

If no entries are displayed, make sure the correct region is selected. On the
navigation bar, in the region selector, choose one of the regions listed in [Region and Endpoints](../../../general/latest/gr/rande.md#codedeploy_region "../../../general/latest/gr/rande.md#codedeploy_region") in the
_AWS General Reference_. CodeDeploy is supported in these regions only. 3. To display deployment details, choose the deployment ID for the instance. 4. You can view all instances in the **Instance activity**
section of the deployment's page. 5. To see information about individual deployment lifecycle events for an
instance, on the deployment details page, in the **Events**
column, choose **View events**.

###### Note

If **Failed** is displayed for any of the lifecycle
events, on the instance details page, choose **View logs**,
**View in EC2**, or both. You can find troubleshooting
tips in [Troubleshoot instance issues](troubleshooting-ec2-instances.md "troubleshooting-ec2-instances.md"). 6. If you want to see more information about an Amazon EC2 instance, choose the ID of
the instance in the **Instance ID** column.

## View instance details (CLI)

To use the AWS CLI to view instance details, call either the
`get-deployment-instance` command or the
`list-deployment-instances` command.

To view details about a single instance, call the
[get-deployment-instance](../../../cli/latest/reference/deploy/get-deployment-instance.md "../../../cli/latest/reference/deploy/get-deployment-instance.md") command, specifying:

- The unique deployment ID. To get the deployment ID, call the
  [list-deployments](../../../cli/latest/reference/deploy/list-deployments.md "../../../cli/latest/reference/deploy/list-deployments.md") command.
- The unique instance ID. To get the instance ID, call the
  [list-deployment-instances](../../../cli/latest/reference/deploy/list-deployment-instances.md "../../../cli/latest/reference/deploy/list-deployment-instances.md") command.

To view a list of IDs for instances used in a deployment, call the
[list-deployment-instances](../../../cli/latest/reference/deploy/list-deployment-instances.md "../../../cli/latest/reference/deploy/list-deployment-instances.md") command, specifying:

- The unique deployment ID. To get the deployment ID, call the
  [list-deployments](../../../cli/latest/reference/deploy/list-deployments.md "../../../cli/latest/reference/deploy/list-deployments.md") command.
- Optionally, whether to include only specific instance IDs by their deployment
  status. (If not specified, all matching instance IDs will be listed, regardless
  of their deployment status.)
