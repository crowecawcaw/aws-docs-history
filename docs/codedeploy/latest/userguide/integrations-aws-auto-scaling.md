# Integrating CodeDeploy with Amazon EC2 Auto Scaling

CodeDeploy supports Amazon EC2 Auto Scaling, an AWS service that launches Amazon EC2 instances automatically
according to conditions you define. These conditions can include limits exceeded in a
specified time interval for CPU utilization, disk reads or writes, or inbound or outbound
network traffic. Amazon EC2 Auto Scaling terminates the instances when they are no longer needed. For more
information, see [What is Amazon EC2 Auto Scaling?](../../../autoscaling/latest/userguide/WhatIsAutoScaling.md "../../../autoscaling/latest/userguide/WhatIsAutoScaling.md")
in the _Amazon EC2 Auto Scaling User Guide_.

When new Amazon EC2 instances are launched as part of an Amazon EC2 Auto Scaling group, CodeDeploy can deploy your
revisions to the new instances automatically. You can also coordinate deployments in CodeDeploy
with Amazon EC2 Auto Scaling instances registered with ELB load balancers. For more information, see
[Integrating CodeDeploy with Elastic Load Balancing](integrations-aws-elastic-load-balancing.md "integrations-aws-elastic-load-balancing.md") and [Set up a load balancer in ELB
for CodeDeploy Amazon EC2 deployments](deployment-groups-create-load-balancer.md "deployment-groups-create-load-balancer.md").

###### Note

You might encounter issues if you associate multiple deployment groups with a single
Amazon EC2 Auto Scaling group. If one deployment fails, for example, the instance will begin to shut
down, but the other deployments that were running can take an hour to time out. For more
information, see [Avoid associating multiple deployment
groups with a single Amazon EC2 Auto Scaling group](troubleshooting-auto-scaling.md#troubleshooting-multiple-depgroups "troubleshooting-auto-scaling.md#troubleshooting-multiple-depgroups") and [Under the hood: CodeDeploy and Amazon EC2 Auto Scaling integration](https://aws.amazon.com/blogs/devops/under-the-hood-aws-codedeploy-and-auto-scaling-integration/ "https://aws.amazon.com/blogs/devops/under-the-hood-aws-codedeploy-and-auto-scaling-integration/").

###### Topics

- [Deploying CodeDeploy applications to
  Amazon EC2 Auto Scaling groups](#integrations-aws-auto-scaling-deploy "#integrations-aws-auto-scaling-deploy")
- [Enabling
  termination deployments during Amazon EC2 Auto Scaling scale-in events](#integrations-aws-auto-scaling-behaviors-hook-enable "#integrations-aws-auto-scaling-behaviors-hook-enable")
- [How Amazon EC2 Auto Scaling works with
  CodeDeploy](#integrations-aws-auto-scaling-behaviors "#integrations-aws-auto-scaling-behaviors")
- [Using a custom AMI with CodeDeploy
  and Amazon EC2 Auto Scaling](#integrations-aws-auto-scaling-custom-ami "#integrations-aws-auto-scaling-custom-ami")

## Deploying CodeDeploy applications to

Amazon EC2 Auto Scaling groups

To deploy a CodeDeploy application revision to an Amazon EC2 Auto Scaling group:

1. Create or locate an IAM instance profile that allows the Amazon EC2 Auto Scaling group to
   work with Amazon S3. For more information, see [Step 4: Create an IAM instance
   profile for your Amazon EC2 instances](getting-started-create-iam-instance-profile.md "getting-started-create-iam-instance-profile.md").

###### Note

You can also use CodeDeploy to deploy revisions from GitHub repositories to
Amazon EC2 Auto Scaling groups. Although Amazon EC2 instances still require an IAM instance
profile, the profile doesn't need any additional permissions to deploy from
a GitHub repository. 2. Create or use an Amazon EC2 Auto Scaling group, specifying the IAM instance profile in your
launch configuration or template. For more information, see [IAM
role for applications that run on Amazon EC2 instances](../../../autoscaling/ec2/userguide/us-iam-role.md "../../../autoscaling/ec2/userguide/us-iam-role.md"). 3. Create or locate a service role that allows CodeDeploy to create a deployment group
that contains the Amazon EC2 Auto Scaling group. 4. Create a deployment group with CodeDeploy, specifying the Amazon EC2 Auto Scaling group name, the
service role, and a few other options. For more information, see [Create a deployment group for an
in-place deployment (console)](deployment-groups-create-in-place.md "deployment-groups-create-in-place.md") or [Create a deployment group for an
in-place deployment (console)](deployment-groups-create-in-place.md "deployment-groups-create-in-place.md"). 5. Use CodeDeploy to deploy your revision to the deployment group that contains the
Amazon EC2 Auto Scaling group.

For more information, see [Tutorial: Use CodeDeploy to deploy an application
to an Amazon EC2 Auto Scaling group](tutorials-auto-scaling-group.md "tutorials-auto-scaling-group.md").

## Enabling

termination deployments during Amazon EC2 Auto Scaling scale-in events

A _termination deployment_ is a type of CodeDeploy deployment that is
activated automatically when an Amazon EC2 Auto Scaling [scale-in event](../../../autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.md#as-lifecycle-scale-in "../../../autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.md#as-lifecycle-scale-in") occurs. CodeDeploy performs the termination deployment right
before the Amazon EC2 Auto Scaling service terminates the instance. During a termination deployment, CodeDeploy
doesn't deploy anything. Instead, it generates lifecycle events, which you can hook up
to your own scripts to enable custom shutdown functionality. For example, you could hook
up the `ApplicationStop` lifecycle event to a script that shuts down your
application gracefully before the instance is terminated.

For a list of lifecycle events that CodeDeploy generates during a termination deployment,
see [Lifecycle event
hook availability](reference-appspec-file-structure-hooks.md#reference-appspec-file-structure-hooks-availability "reference-appspec-file-structure-hooks.md#reference-appspec-file-structure-hooks-availability").

If the termination deployment fails for any reason, CodeDeploy will allow the instance
termination to proceed. This means that the instance will be shut down even though CodeDeploy
did not run the full set (or any) of the lifecycle events to completion.

If you don't enable termination deployments, the Amazon EC2 Auto Scaling service will still terminate
Amazon EC2 instances when a scale-in event occurs, but CodeDeploy will not generate lifecycle
events.

###### Note

Regardless of whether you enable termination deployments or not, if the Amazon EC2 Auto Scaling
service terminates an Amazon EC2 instance while a CodeDeploy deployment is underway, then a
race condition may occur between the lifecycle events generated by the Amazon EC2 Auto Scaling and
CodeDeploy services. For example, the `Terminating` lifecycle event (generated
by the Amazon EC2 Auto Scaling service) might override the `ApplicationStart` event
(generated by the CodeDeploy deployment). In this scenario, you may experience a failure
with either the Amazon EC2 instance termination or the CodeDeploy deployment.

###### To enable CodeDeploy to perform termination deployments

- Select the **Add a termination hook to Amazon EC2 Auto Scaling groups** check
  box when creating or updating your deployment group. For instructions, see [Create a deployment group for an
  in-place deployment (console)](deployment-groups-create-in-place.md "deployment-groups-create-in-place.md"), or [Create a deployment group for an
  EC2/On-Premises blue/green deployment (console)](deployment-groups-create-blue-green.md "deployment-groups-create-blue-green.md").

Enabling this check box causes CodeDeploy to install an [Amazon EC2 Auto Scaling lifecycle
hook](../../../autoscaling/ec2/userguide/lifecycle-hooks.md "../../../autoscaling/ec2/userguide/lifecycle-hooks.md") into the Amazon EC2 Auto Scaling groups that you specify when you create or update
your CodeDeploy deployment group. This hook is called the _termination
hook_ and enables termination deployments.

**After the termination hook is installed, a scale-in
(termination) event unfolds as follows:**

1. The Amazon EC2 Auto Scaling service (or simply, Amazon EC2 Auto Scaling) determines that a scale-in event needs to
   occur, and contacts the EC2 service to terminate an EC2
   instance.
2. The EC2 service starts terminating the EC2 instance. The
   instance moves into the `Terminating` state, and then into the
   `Terminating:Wait` state.
3. During `Terminating:Wait`, Amazon EC2 Auto Scaling runs all the lifecycle hooks
   attached to the Amazon EC2 Auto Scaling group, including the termination hook installed by
   CodeDeploy.
4. The termination hook sends a notification to the [Amazon SQS
   queue](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md") that is polled by CodeDeploy.
5. Upon receiving the notification, CodeDeploy parses the message, performs some
   validation, and performs a termination
   deployment.
6. While the termination deployment is running, CodeDeploy sends heartbeats every five
   minutes to Amazon EC2 Auto Scaling to let it know that the instance is still being worked
   on.
7. So far, the EC2 instance is still in the `Terminating:Wait`
   state (or possibly the `Warmed:Pending:Wait` state, if you've enabled
   [Amazon EC2 Auto Scaling group
   warm pools](../../../autoscaling/ec2/userguide/warm-pool-instance-lifecycle.md "../../../autoscaling/ec2/userguide/warm-pool-instance-lifecycle.md")).
8. When the deployment completes, CodeDeploy indicates to Amazon EC2 Auto Scaling to
   `CONTINUE` the EC2 termination process, regardless of
   whether the termination deployment succeeded or failed.

## How Amazon EC2 Auto Scaling works with

CodeDeploy

When you create or update a CodeDeploy deployment group to include an Amazon EC2 Auto Scaling group, CodeDeploy
accesses the Amazon EC2 Auto Scaling group using the CodeDeploy service role, and then installs [Amazon EC2 Auto Scaling
lifecycle hooks](../../../autoscaling/ec2/userguide/lifecycle-hooks.md "../../../autoscaling/ec2/userguide/lifecycle-hooks.md") into your Amazon EC2 Auto Scaling groups.

###### Note

_Amazon EC2 Auto Scaling lifecycle hooks_ are different from the
_lifecycle events_ (also called _lifecycle event
hooks_) generated by CodeDeploy and described in the [AppSpec 'hooks' section](reference-appspec-file-structure-hooks.md "reference-appspec-file-structure-hooks.md") of this guide.

The Amazon EC2 Auto Scaling lifecycle hooks that CodeDeploy installs are:

- **A launch hook** — This hook notifies
  CodeDeploy that an Amazon EC2 Auto Scaling [scale-out event](../../../autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.md#as-lifecycle-scale-out "../../../autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.md#as-lifecycle-scale-out") is in progress, and that CodeDeploy needs to start a
  launch deployment.

During a _launch
deployment_, CodeDeploy:

    + Deploys a revision of your application to the scaled-out
     instance.
    + Generates lifecycle events to indicate the progress of the deployment.
     You can hook up these lifecycle events to your own scripts to enable
     custom startup functionality. For more information, see the table in
     [Lifecycle event
     hook availability](reference-appspec-file-structure-hooks.md#reference-appspec-file-structure-hooks-availability "reference-appspec-file-structure-hooks.md#reference-appspec-file-structure-hooks-availability").

The launch hook and associated launch deployment are always enabled and cannot
be turned off.

- **A termination hook** — This optional
  hook notifies CodeDeploy that an Amazon EC2 Auto Scaling [scale-in event](../../../autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.md#as-lifecycle-scale-in "../../../autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.md#as-lifecycle-scale-in") is in progress, and that CodeDeploy needs to start a
  termination deployment.

During a _termination deployment_, CodeDeploy generates
lifecycle events to indicate the progress of the instance shutdown. For more
information, see [Enabling
termination deployments during Amazon EC2 Auto Scaling scale-in events](#integrations-aws-auto-scaling-behaviors-hook-enable "#integrations-aws-auto-scaling-behaviors-hook-enable").

###### Topics

- [After CodeDeploy
  installs the lifecycle hooks, how are they used?](#integrations-aws-auto-scaling-behaviors-hook-usage "#integrations-aws-auto-scaling-behaviors-hook-usage")
- [How CodeDeploy names
  Amazon EC2 Auto Scaling groups](#integrations-aws-auto-scaling-behaviors-naming "#integrations-aws-auto-scaling-behaviors-naming")
- [Execution order
  of custom lifecycle hook events](#integrations-aws-auto-scaling-behaviors-hook-order "#integrations-aws-auto-scaling-behaviors-hook-order")
- [Scale-out events during a deployment](#integrations-aws-auto-scaling-behaviors-mixed-environment "#integrations-aws-auto-scaling-behaviors-mixed-environment")
- [Scale-in events
  during a deployment](#integrations-aws-auto-scaling-behaviors-scale-in "#integrations-aws-auto-scaling-behaviors-scale-in")
- [Order of
  events in AWS CloudFormation cfn-init scripts](#integrations-aws-auto-scaling-behaviors-event-order "#integrations-aws-auto-scaling-behaviors-event-order")

### After CodeDeploy

installs the lifecycle hooks, how are they used?

After the launch and termination lifecycle hooks are installed, they are used by
CodeDeploy during Amazon EC2 Auto Scaling group scale-out and scale-in events, respectively.

**A scale-out (launch) event unfolds as
follows:**

1. The Amazon EC2 Auto Scaling service (or simply, Amazon EC2 Auto Scaling) determines that a scale-out event needs
   to occur, and contacts the EC2 service to launch a new EC2
   instance.
2. The EC2 service launches a new EC2 instance. The instance
   moves into the `Pending` state, and then into the
   `Pending:Wait` state.
3. During `Pending:Wait`, Amazon EC2 Auto Scaling runs all the lifecycle hooks
   attached to the Amazon EC2 Auto Scaling group, including the launch hook installed by
   CodeDeploy.
4. The launch hook sends a notification to the [Amazon SQS
   queue](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md") that is polled by CodeDeploy.
5. Upon receiving the notification, CodeDeploy parses the message, performs some
   validation, and starts a [launch
   deployment](#launch-deployment "#launch-deployment").
6. While the launch deployment is running, CodeDeploy sends heartbeats every five
   minutes to Amazon EC2 Auto Scaling to let it know that the instance is still being worked
   on.
7. So far, the EC2 instance is still in the `Pending:Wait`
   state.
8. When the deployment completes, CodeDeploy indicates to Amazon EC2 Auto Scaling to either
   `CONTINUE` or `ABANDON` the EC2 launch
   process, depending on whether the deployment succeeded or failed.
   - If CodeDeploy indicates `CONTINUE`, Amazon EC2 Auto Scaling continues the
     launch process, either waiting for other hooks to complete, or
     putting the instance into the `Pending:Proceed` and then
     the `InService` state.
   - If CodeDeploy indicates `ABANDON`, Amazon EC2 Auto Scaling terminates the
     EC2 instance, and restarts the launch procedure if needed to
     meet the desired number of instances, as defined in the Amazon EC2 Auto Scaling
     **Desired Capacity** setting.

**A scale-in (termination) event unfolds as
follows:**

See [Enabling
termination deployments during Amazon EC2 Auto Scaling scale-in events](#integrations-aws-auto-scaling-behaviors-hook-enable "#integrations-aws-auto-scaling-behaviors-hook-enable").

### How CodeDeploy names

Amazon EC2 Auto Scaling groups

During blue/green deployments on an EC2/On-Premises compute platform, you have two
options for adding instances to your replacement (green) environment:

- Use instances that already exist or that you create manually.
- Use settings from an Amazon EC2 Auto Scaling group that you specify to define and create
  instances in a new Amazon EC2 Auto Scaling group.

If you choose the second option, CodeDeploy provisions a new Amazon EC2 Auto Scaling group for you.
It uses the following convention to name the group:

```
CodeDeploy_`deployment_group_name`_`deployment_id`
```

For example, if a deployment with ID `10` deploys a deployment group
named `alpha-deployments`, the provisioned Amazon EC2 Auto Scaling group is named
`CodeDeploy_alpha-deployments_10`. For more information, see [Create a deployment group for an
EC2/On-Premises blue/green deployment (console)](deployment-groups-create-blue-green.md "deployment-groups-create-blue-green.md") and [GreenFleetProvisioningOption](../APIReference/API_GreenFleetProvisioningOption.md "../APIReference/API_GreenFleetProvisioningOption.md").

### Execution order

of custom lifecycle hook events

You can add your own lifecycle hooks to Amazon EC2 Auto Scaling groups to which CodeDeploy deploys.
However, the order in which those custom lifecycle hook events are executed cannot
be predetermined in relation to CodeDeploy default deployment lifecycle events. For
example, if you add a custom lifecycle hook named
`ReadyForSoftwareInstall` to an Amazon EC2 Auto Scaling group, you cannot know
beforehand whether it will be executed before the first, or after the last, CodeDeploy
default deployment lifecycle event.

To learn how to add custom lifecycle hooks to an Amazon EC2 Auto Scaling group, see [Adding lifecycle
hooks](../../../autoscaling/latest/userguide/lifecycle-hooks.md#adding-lifecycle-hooks "../../../autoscaling/latest/userguide/lifecycle-hooks.md#adding-lifecycle-hooks") in the _Amazon EC2 Auto Scaling User Guide_.

### Scale-out events during a deployment

If an Amazon EC2 Auto Scaling scale-out event occurs while a deployment is underway, the new
instances will be updated with the application revision that was previously
deployed, not the newest application revision. If the deployment succeeds, the old
instances and the newly scaled-out instances will be hosting different application
revisions. To bring the instances with the older revision up to date, CodeDeploy
automatically starts a follow-on deployment (immediately after the first) to update
any outdated instances. If you'd like to change this default behavior so that
outdated EC2 instances are left at the older revision, see [Automatic updates to outdated instances](deployment-groups-configure-advanced-options.md#auto-updates-outdated-instances "deployment-groups-configure-advanced-options.md#auto-updates-outdated-instances").

If you want to suspend Amazon EC2 Auto Scaling scale-out processes while deployments are taking
place, you can do this through a setting in the
`common_functions.sh` script that is used for load balancing
with CodeDeploy. If `HANDLE_PROCS=true`, the following Amazon EC2 Auto Scaling events are
suspended automatically during the deployment process:

- AZRebalance
- AlarmNotification
- ScheduledActions
- ReplaceUnhealthy

###### Important

Only the CodeDeployDefault.OneAtATime deployment configuration supports this
functionality.

For more information about using `HANDLE_PROCS=true` to avoid
deployment problems when using Amazon EC2 Auto Scaling, see [Important notice about handling AutoScaling processes](https://github.com/awslabs/aws-codedeploy-samples/tree/master/load-balancing/elb#important-notice-about-handling-autoscaling-processes "https://github.com/awslabs/aws-codedeploy-samples/tree/master/load-balancing/elb#important-notice-about-handling-autoscaling-processes") in [aws-codedeploy-samples](https://github.com/awslabs/aws-codedeploy-samples "https://github.com/awslabs/aws-codedeploy-samples") on GitHub.

### Scale-in events

during a deployment

If an Amazon EC2 Auto Scaling group starts scaling in while a CodeDeploy deployment is underway on that
Amazon EC2 Auto Scaling group, a race condition could occur between the termination process (including
the CodeDeploy termination deployment lifecycle events) and other CodeDeploy lifecycle events
on the terminating instance. The deployment on that specific instance may fail if
the instance is terminated before all CodeDeploy lifecycle events complete. Also, the
overall CodeDeploy deployment may or may not fail, depending on how you've set your
**Minimum healthy hosts** setting in your deployment
configuration.

### Order of

events in AWS CloudFormation cfn-init scripts

If you use `cfn-init` (or `cloud-init`) to run scripts on
newly provisioned Linux-based instances, your deployments might fail unless you
strictly control the order of events that occur after the instance starts.

That order must be:

1. The newly provisioned instance starts.
2. All `cfn-init` bootstrapping scripts run to completion.
3. The CodeDeploy agent starts.
4. The latest application revision is deployed to the instance.

If the order of events is not carefully controlled, the CodeDeploy agent might start a
deployment before all the scripts have finished running.

To control the order of events, use one of these best practices:

- Install the CodeDeploy agent through a `cfn-init` script, placing it
  after all other scripts.
- Include the CodeDeploy agent in a custom AMI and use a `cfn-init`
  script to start it, placing it after all other scripts.

For information about using `cfn-init`, see [cfn-init](../../../AWSCloudFormation/latest/UserGuide/cfn-init.md "../../../AWSCloudFormation/latest/UserGuide/cfn-init.md") in the
_AWS CloudFormation User Guide_.

## Using a custom AMI with CodeDeploy

and Amazon EC2 Auto Scaling

You have two options for specifying the base AMI to use when new Amazon EC2 instances are
launched in an Amazon EC2 Auto Scaling group:

- You can specify a base custom AMI that already has the CodeDeploy agent installed.
  Because the agent is already installed, this option launches new Amazon EC2 instances
  more quickly than the other option. However, this option provides a greater
  likelihood that initial deployments of Amazon EC2 instances will fail, especially if
  the CodeDeploy agent is out of date. If you choose this option, we recommend you
  regularly update the CodeDeploy agent in your base custom AMI.
- You can specify a base AMI that doesn't have the CodeDeploy agent installed and
  have the agent installed as each new instance is launched in an Amazon EC2 Auto Scaling group.
  Although this option launches new Amazon EC2 instances more slowly than the other
  option, it provides a greater likelihood that initial deployments of instances
  will succeed. This option uses the most recent version of the CodeDeploy
  agent.
