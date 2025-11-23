# Change deployment group settings with CodeDeploy

You can use the CodeDeploy console, the AWS CLI, or the CodeDeploy APIs to change the settings of a
deployment group.

###### Warning

Do not use these steps if you want the deployment group to use a not-yet-created
custom deployment group. Instead, follow the instructions in [Create a Deployment Configuration](deployment-configurations-create.md "deployment-configurations-create.md"), and then return to this topic.
Do not use these steps if you want the deployment group to use a different,
not-yet-created service role. The service role must trust CodeDeploy with, at minimum, the
permissions described in [Step 2: Create a service role for
CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md"). To create and configure a
service role with the correct permissions, follow the instructions in [Step 2: Create a service role for
CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md"), and then return to this
topic.

###### Topics

- [Change deployment group settings
  (console)](#deployment-groups-edit-console "#deployment-groups-edit-console")
- [Change deployment group settings
  (CLI)](#deployment-groups-edit-cli "#deployment-groups-edit-cli")

## Change deployment group settings

(console)

To use the CodeDeploy console to change deployment group settings:

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, then choose **Applications**. 3. In the list of applications, choose the name of the application that is
associated with the deployment group you want to change.

###### Note

If no entries are displayed, make sure the correct region is selected. On the
navigation bar, in the region selector, choose one of the regions listed in [Region and Endpoints](../../../general/latest/gr/rande.md#codedeploy_region "../../../general/latest/gr/rande.md#codedeploy_region") in the
_AWS General Reference_. CodeDeploy is supported in these regions only. 4. Choose the **Deployment groups** tab, and then choose the
name of the deployment group you want to change. 5. On the **Depoyment group** page, choose
**Edit**. 6. Edit the deployment group options as needed.

For information about deployment group components, see [Create a deployment group with CodeDeploy](deployment-groups-create.md "deployment-groups-create.md"). 7. Choose **Save changes**.

## Change deployment group settings

(CLI)

To use the AWS CLI to change deployment group settings, call the
[update-deployment-group](../../../cli/latest/reference/deploy/update-deployment-group.md "../../../cli/latest/reference/deploy/update-deployment-group.md") command, specifying:

- For EC2/On-Premises and AWS Lambda
  deployments:
  - The application name. To view a list of application names, call the
    [list-applications](../../../cli/latest/reference/deploy/list-applications.md "../../../cli/latest/reference/deploy/list-applications.md") command.
  - The current deployment group name. To view a list of deployment group
    names, call the [list-deployment-groups](../../../cli/latest/reference/deploy/list-deployment-groups.md "../../../cli/latest/reference/deploy/list-deployment-groups.md") command.
  - (Optional) A different deployment group name.
  - (Optional) A different Amazon Resource Name (ARN) that corresponds to
    a service role that allows CodeDeploy to act on your AWS account's behalf
    when interacting with other AWS services. To get the service role ARN,
    see [Get the service role ARN (CLI)](getting-started-create-service-role.md#getting-started-get-service-role-cli "getting-started-create-service-role.md#getting-started-get-service-role-cli") . For more
    information about service roles, see [Roles terms and
    concepts](../../../IAM/latest/UserGuide/cross-acct-access.md "../../../IAM/latest/UserGuide/cross-acct-access.md") in _IAM User Guide_.
  - (Optional) The name of the deployment configuration. To view a list of
    deployment configurations, see [View Deployment Configuration Details](deployment-configurations-view-details.md "deployment-configurations-view-details.md"). (If not
    specified, CodeDeploy uses a default deployment configuration.)
  - (Optional) Commands to add one or more existing CloudWatch alarms to the
    deployment group that are activated if a metric specified in an alarm
    falls below or exceeds a defined threshold.
  - (Optional) Commands for a deployment to roll back to the last known
    good revision when a deployment fails or a CloudWatch alarm is
    activated.
  - (Optional) Commands for a deployment to generate lifecycle event hooks during
    an Amazon EC2 Auto Scaling scale-in event. For more information, see [How Amazon EC2 Auto Scaling works with
    CodeDeploy](integrations-aws-auto-scaling.md#integrations-aws-auto-scaling-behaviors "integrations-aws-auto-scaling.md#integrations-aws-auto-scaling-behaviors").
  - (Optional) Commands to create or update a trigger that publishes to a
    topic in Amazon Simple Notification Service, so that subscribers to that topic receive
    notifications about deployment and instance events in this deployment
    group. For information, see [Monitoring Deployments with Amazon SNS Event Notifications](monitoring-sns-event-notifications.md "monitoring-sns-event-notifications.md").

- For EC2/On-Premises deployments only:
  - (Optional) Replacement tags or tag groups that uniquely identify the
    instances to be included in the deployment group.
  - (Optional) The names of replacement Amazon EC2 Auto Scaling groups to be added to the
    deployment group.

- For Amazon ECS deployments only:
  - The Amazon ECS service to deploy.
  - Load balancer information, including the Application Load Balancer or Network Load Balancer, the target
    groups required for an Amazon ECS deployment, and production and optional
    test listener information.
