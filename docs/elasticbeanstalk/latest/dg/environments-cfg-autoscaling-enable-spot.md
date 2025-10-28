# Enabling Spot Instances for your

environment

To take advantage of Amazon EC2 Spot Instances, set the `EnableSpot`
option for your environment. Your environment's Auto Scaling group then combines Amazon EC2 purchase
options and maintains a mix of On-Demand and Spot Instances.

You can use the [Elastic Beanstalk
console](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console"), [namespace
configuration options](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace"), the [AWS CLI](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli"), or the [EB CLI](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-ebcli "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-ebcli") to
enable Spot Instance requests for your environment.

Before you enable Spot Instances for your environment, become familiar with the Auto Scaling,
capacity, and load balancing configuration options that are available. Your application's
requirements that are related to workload, impact of instance interruptions, and pricing,
are all important considerations in your planning to enable Spot Instances.

The topics that follow provide details about the Auto Scaling and capacity management options
and how their combined use affects your environment. There are procedures and example
configurations to inform and guide you about the various options and how to configure them.
We also offer tools and features to help you manage your configuration and respond to
events. You can schedule automated changes to your configuration based on predictable
periods of traffic, configure triggers to respond to factors such as traffic volume, and
configure Auto Scaling monitoring and health checks.

For more detailed information about Spot Instances, including explanation of key
concepts and best practices, see [Spot
Instances](../../../AWSEC2/latest/UserGuide/using-spot-instances.md "../../../AWSEC2/latest/UserGuide/using-spot-instances.md") in the _Amazon EC2 User Guide_.

###### Important

The `EnableSpot`
option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch
templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom
policies instead of our managed policies, environment creation or updates might fail when you update your environment
configuration. For more information
and other considerations, see [Migrating your Elastic Beanstalk
environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md") .
