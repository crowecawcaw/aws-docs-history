# View deployment configuration

details with CodeDeploy

You can use the CodeDeploy console, the AWS CLI, or the CodeDeploy APIs to view details about
deployment configurations associated with your AWS account. For descriptions of the
predefined CodeDeploy deployment configurations, see [Predefined deployment configurations
for an EC2/on-premises compute platform](deployment-configurations.md#deployment-configurations-predefined "deployment-configurations.md#deployment-configurations-predefined").

###### Topics

- [View deployment
  configuration details (console)](#deployment-configurations-view-details-console "#deployment-configurations-view-details-console")
- [View deployment
  configuration (CLI)](#deployment-configurations-view-details-cli "#deployment-configurations-view-details-cli")

## View deployment

configuration details (console)

To use the CodeDeploy console to view a list of deployment configuration names:

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, and choose **Deployment configurations**.

Here you can see the
deployment configuration names and criteria for each deployment configuration.

###### Note

If no entries are displayed, make sure the correct region is selected. On the
navigation bar, in the region selector, choose one of the regions listed in [Region and Endpoints](../../../general/latest/gr/rande.md#codedeploy_region "../../../general/latest/gr/rande.md#codedeploy_region") in the
_AWS General Reference_. CodeDeploy is supported in these regions only.

## View deployment

configuration (CLI)

To use the AWS CLI to view deployment configuration details, call either the
`get-deployment-config` command or the
`list-deployment-configs` command.

To view details about a single deployment configuration, call the
[get-deployment-config](../../../cli/latest/reference/deploy/get-deployment-config.md "../../../cli/latest/reference/deploy/get-deployment-config.md") command, specifying the unique deployment
configuration name.

To view details about multiple deployment configurations, call the
[list-deployments](../../../cli/latest/reference/deploy/list-deployments.md "../../../cli/latest/reference/deploy/list-deployments.md") command.
