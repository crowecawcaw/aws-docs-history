# Amazon EC2 Auto Scaling your Elastic Beanstalk environment instances

This topic describes how you can customize the Amazon EC2 Auto Scaling features to manage your Elastic Beanstalk
environment’s workload. You can configure Amazon EC2 Auto Scaling for your environment using the [Elastic Beanstalk console](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console"), [namespace configuration options](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace"), the
[AWS CLI](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli"), or the [EB CLI](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-ebcli "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-ebcli").

###### Load-balanced or single instance environments

Your AWS Elastic Beanstalk environment includes an _Amazon EC2 Auto Scaling group_ that manages the
[Amazon EC2 instances](using-features.managing.md "using-features.managing.md") in your environment. In a
single-instance environment, the Amazon EC2 Auto Scaling group ensures that there is always one instance running.
In a load-balanced environment, you configure the group with a range of instances to run, and
Amazon EC2 Auto Scaling adds or removes instances as needed, based on load.

###### EC2 Instance configuration

The Amazon EC2 Auto Scaling group also applies your configuration choices to provision and manage the EC2
instances in your environment. You can [modify the
EC2 configuration](using-features.managing.md "using-features.managing.md") to change the instance type, key pair, Amazon Elastic Block Store (Amazon EBS) storage,
and other settings that can only be configured when you launch an instance.

###### On-Demand and Spot Instances

As an option, Elastic Beanstalk can include [Spot
Instances](environments-cfg-autoscaling-spot.md "environments-cfg-autoscaling-spot.md") in your environment and manage them in combination with On-Demand
instances. You can configure Amazon EC2 Amazon EC2 Auto Scaling to monitor and automatically respond to changes that
affect the availability of your Spot Instances by enabling [Capacity Rebalancing](../../../autoscaling/ec2/userguide/capacity-rebalance.md "../../../autoscaling/ec2/userguide/capacity-rebalance.md"). You
can also configure the
[Spot
allocation strategy](environments-cfg-autoscaling-spot-allocation-strategy.md "environments-cfg-autoscaling-spot-allocation-strategy.md") that the Amazon EC2 Auto Scaling
service uses to provision Spot Instances to your environment.

###### Required permissions when enabling Spot Instances

Enabling Spot Instance requests requires using Amazon EC2 launch templates.
When you configure this feature during environment creation or updates, Elastic Beanstalk attempts to configure your
environment to use Amazon EC2 launch templates (if the environment isn't using them already). In this case, if your user policy lacks the necessary
permissions, environment creation or updates might fail. Therefore, we recommend that you use our managed user policy or add the required permissions
to your custom policies. For details about the required permissions, see
[Required
permissions for launch templates](environments-cfg-autoscaling-launch-templates.md#environments-cfg-autoscaling-launch-templates-permissions "environments-cfg-autoscaling-launch-templates.md#environments-cfg-autoscaling-launch-templates-permissions").

###### Amazon EC2 Auto Scaling triggers

The Amazon EC2 Auto Scaling group uses two Amazon CloudWatch alarms to trigger scaling operations. The default
triggers scale when the average outbound network traffic from each instance is higher than 6
MiB or lower than 2 MiB over a period of five minutes. To use Amazon EC2 Auto Scaling effectively, [configure triggers](environments-cfg-autoscaling-triggers.md "environments-cfg-autoscaling-triggers.md") that are
appropriate for your application, instance type, and service requirements. You can scale based
on several statistics including latency, disk I/O, CPU utilization, and request count.

###### Schedule Amazon EC2 Auto Scaling actions

To optimize your environment's use of Amazon EC2 instances through predictable periods of peak
traffic, [configure your Amazon EC2 Auto Scaling
group to change its instance count on a schedule](environments-cfg-autoscaling-scheduledactions.md "environments-cfg-autoscaling-scheduledactions.md"). You can schedule changes to your
group's configuration that recur daily or weekly, or schedule one-time changes to prepare for
marketing events that will drive a lot of traffic to your site.

###### Amazon EC2 Auto Scaling health check

Amazon EC2 Auto Scaling monitors the health of each Amazon EC2 instance that it launches. If any instance
terminates unexpectedly, Amazon EC2 Auto Scaling detects the termination and launches a replacement instance. To
configure the group to use the load balancer's health check mechanism, see [Amazon EC2 Auto Scaling health check setting for your Elastic Beanstalk environment](environmentconfig-autoscaling-healthchecktype.md "environmentconfig-autoscaling-healthchecktype.md").

###### Topics

- [Migrating your Elastic Beanstalk
  environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md")
- [Spot Instance support for your Elastic Beanstalk
  environment](environments-cfg-autoscaling-spot.md "environments-cfg-autoscaling-spot.md")
- [Amazon EC2 Auto Scaling triggers for your Elastic Beanstalk environment](environments-cfg-autoscaling-triggers.md "environments-cfg-autoscaling-triggers.md")
- [Scheduled Amazon EC2 Auto Scaling actions for your Elastic Beanstalk environments](environments-cfg-autoscaling-scheduledactions.md "environments-cfg-autoscaling-scheduledactions.md")
- [Amazon EC2 Auto Scaling health check setting for your Elastic Beanstalk environment](environmentconfig-autoscaling-healthchecktype.md "environmentconfig-autoscaling-healthchecktype.md")
