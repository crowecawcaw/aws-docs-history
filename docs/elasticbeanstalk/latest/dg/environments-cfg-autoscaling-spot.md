# Spot Instance support for your Elastic Beanstalk

environment

This topic describes the configuration options that are available for you to manage the
capacity and load balancing of Spot Instances in your Elastic Beanstalk environment. It also provides
details and examples for the methods you can use to configure these options. You can use the
[Elastic Beanstalk console](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console"), [namespace configuration options](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace"), the
[AWS CLI](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli"), or the [EB CLI](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-ebcli "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-ebcli") to manage the configuration
options.

###### Minimize Spot instance interruptions with Capacity Rebalancing

To help minimize the impact of Spot Instance interruptions to your application, you can
enable the Capacity Rebalancing option included with Amazon EC2 Amazon EC2 Auto Scaling.

###### Important

Demand for Spot Instances can vary significantly from moment to moment, and the
availability of Spot Instances can also vary significantly depending on how many unused
Amazon EC2 instances are available. It's always possible that your Spot Instance might be
interrupted.

When you enable Capacity Rebalancing, EC2 automatically attempts to replace Spot Instances
in an Amazon EC2 Auto Scaling group before they are interrupted. To enable this feature use the Elastic Beanstalk console to
[configure the Auto Scaling
group](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console"). Alternatively, you can set the Elastic Beanstalk `EnableCapacityRebalancing`
[configuration option](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace") to
`true` in the [aws:autoscaling:asg](command-options-general.md#command-options-general-autoscalingasg "command-options-general.md#command-options-general-autoscalingasg") namespace.

For more information, see [Capacity Rebalancing](../../../autoscaling/ec2/userguide/capacity-rebalance.md "../../../autoscaling/ec2/userguide/capacity-rebalance.md") in the
_Amazon EC2 Amazon EC2 Auto Scaling User Guide_ and [Spot Instance Interruptions](../../../AWSEC2/latest/UserGuide/spot-interruptions.md "../../../AWSEC2/latest/UserGuide/spot-interruptions.md") in the
_Amazon EC2 User Guide_.

###### Older Instance Types and Spot Instance Support

Some older AWS accounts might provide Elastic Beanstalk with default instance types that don't
support Spot Instances. If you enable Spot Instance requests and you see the error
**`None of the instance types you specified supports Spot`**, update your
configuration with instance types that support Spot Instances. To choose Spot Instance
types, use the [Spot Instance
Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/ "https://aws.amazon.com/ec2/spot/instance-advisor/").

###### Topics

- [Enabling Spot Instances for your
  environment](environments-cfg-autoscaling-enable-spot.md "environments-cfg-autoscaling-enable-spot.md")
- [Spot Instance
  allocation strategy](environments-cfg-autoscaling-spot-allocation-strategy.md "environments-cfg-autoscaling-spot-allocation-strategy.md")
- [Managing On-Demand instances
  and Spot instances](environments-cfg-autoscaling-spot-and-demand.md "environments-cfg-autoscaling-spot-and-demand.md")
- [Capacity
  configuration for your Elastic Beanstalk environment](environments-cfg-autoscaling-configuration-approaches.md "environments-cfg-autoscaling-configuration-approaches.md")
