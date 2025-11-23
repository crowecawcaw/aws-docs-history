# Create a deployment group (CLI)

To use the AWS CLI to create a deployment group, call the
[create-deployment-group](../../../cli/latest/reference/deploy/create-deployment-group.md "../../../cli/latest/reference/deploy/create-deployment-group.md") command, specifying:

- The application name. To view a list of application names, call the
  [list-applications](../../../cli/latest/reference/deploy/list-applications.md "../../../cli/latest/reference/deploy/list-applications.md") command.
- A name for the deployment group. A deployment group with this name is created
  for the specified application. A deployment group can only be associated with
  one application.
- Information about the tags, tag groups, or Amazon EC2 Auto Scaling group names that identify
  the instances to be included in the deployment group.
- The Amazon Resource Name (ARN) identifier of the service role that allows
  CodeDeploy to act on behalf of your AWS account when interacting with other AWS
  services. To get the service role ARN, see [Get the service role ARN (CLI)](getting-started-create-service-role.md#getting-started-get-service-role-cli "getting-started-create-service-role.md#getting-started-get-service-role-cli") . For more information
  about service roles, see [Roles
  terms and concepts](../../../IAM/latest/UserGuide/roles-toplevel.md#roles-about-termsandconcepts "../../../IAM/latest/UserGuide/roles-toplevel.md#roles-about-termsandconcepts") in _IAM User Guide_.
- Information about the type of deployment, either in-place or blue/green, to
  associate with the deployment group.
- (Optional) The name of an existing deployment configuration. To view a list of
  deployment configurations, see [View Deployment Configuration Details](deployment-configurations-view-details.md "deployment-configurations-view-details.md"). If not specified,
  CodeDeploy uses a default deployment configuration.
- (Optional) Commands to create a trigger that pushes notifications about
  deployment and instance events to those who are subscribed to an Amazon Simple Notification Service
  topic. For more information, see [Monitoring Deployments with Amazon SNS Event Notifications](monitoring-sns-event-notifications.md "monitoring-sns-event-notifications.md").
- (Optional) Commands to add existing CloudWatch alarms to the deployment group that
  are activated if a metric specified in an alarm falls below or exceeds a defined
  threshold.
- (Optional) Commands for a deployment to roll back to the last known good
  revision when a deployment fails or a CloudWatch alarm is activated.
- (Optional) Commands for a deployment to generate lifecycle event hooks during
  an Amazon EC2 Auto Scaling scale-in event. For more information, see [How Amazon EC2 Auto Scaling works with
  CodeDeploy](integrations-aws-auto-scaling.md#integrations-aws-auto-scaling-behaviors "integrations-aws-auto-scaling.md#integrations-aws-auto-scaling-behaviors").
- For in-place deployments:
  - (Optional) The names of the Classic Load Balancers, Application Load Balancers, or Network Load Balancers in ELB that
    manage traffic to the instances during the deployment processes.

- For blue/green deployments:
  - Configuration of the blue/green deployment process:
    - How new instances in the replacement environment are
      provisioned.
    - Whether to reroute traffic to the replacement environment
      immediately or wait a specified period for traffic to be
      rerouted manually.
    - Whether instances in the original environment should be
      terminated.

  - The names of the Classic Load Balancers, Application Load Balancers, or Network Load Balancers in ELB to be used for
    instances registered in the replacement environment.

###### Warning

If you are configuring both an Amazon EC2 Auto Scaling group and an ELB load balancer in
your deployment group, and you want to [attach the
load balancer to the Amazon EC2 Auto Scaling group](../../../autoscaling/ec2/userguide/attach-load-balancer-asg.md "../../../autoscaling/ec2/userguide/attach-load-balancer-asg.md"), we recommend completing this
attachment _before_ creating the CodeDeploy deployment from
this deployment group. Attempting to complete the attachment after creating
the deployment may cause all the instances to become deregistered from the
load balancer unexpectedly.
