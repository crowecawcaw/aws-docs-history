# Capacity

configuration for your Elastic Beanstalk environment

This topic describes the different approaches to configure Auto Scaling capacity for your Elastic Beanstalk
environment. You can use the Elastic Beanstalk console, the EB CLI, the AWS CLI, or namespace
options.

###### Important

The `EnableSpot`
option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch
templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom
policies instead of our managed policies, environment creation or updates might fail when you update your environment
configuration. For more information
and other considerations, see [Migrating your Elastic Beanstalk
environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md") .

## Configuration using the

console

You can configure the capacity management of an Auto Scaling group by editing
**Capacity** on the environment's **Configuration**
page in the [Elastic Beanstalk console](environments-console.md "environments-console.md").

###### To configure Auto Scaling group capacity in the Elastic Beanstalk console

1.  Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
    and in the **Regions** list, select your AWS Region.
2.  In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3.  In the navigation pane, choose **Configuration**.
4.  In the **Capacity** configuration category, choose
    **Edit**.
5.  In the **Auto Scaling group** section, configure the following
    settings.
    - **Environment type** – Select **Load
      balanced**.
    - **Min instances** – The minimum number of EC2
      instances that the group should contain at any time. The group starts with the
      minimum count and adds instances when the scale-up trigger condition is
      met.
    - **Max instances** – The maximum number of EC2
      instances that the group should contain at any time.

    ###### Note

    If you use rolling updates, be sure that the maximum instance count is
    higher than the [Minimum
    instances in service setting](using-features.md#rollingupdates-configure "using-features.md#rollingupdates-configure") for rolling updates.
    - **Fleet composition** – The default is
      **On-Demand Instances**. To enable _Spot
      Instance_ requests, select **Combined purchase options and
      instances**.

    ###### Important

    The `EnableSpot`
    option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch
    templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom
    policies instead of our managed policies, environment creation or updates might fail when you update your environment
    configuration. For more information
    and other considerations, see [Migrating your Elastic Beanstalk
    environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md") .

    The following options are enabled if you select to enable _Spot
    Instance_ requests:

        + **Spot allocation strategy** – Determines the
         method used to manage and provision the Spot Instances in your environment,
         based on available capacity, price, and selection of instance types. Select
         from *Capacity optimized* (default), *Price
         capacity optimized*, *Capacity optimized
         prioritized*, or *Lowest price*. For a
         description of each allocation strategy and more information, see [Spot Instance
         allocation strategy](environments-cfg-autoscaling-spot-allocation-strategy.md "environments-cfg-autoscaling-spot-allocation-strategy.md").
        + **Maximum spot price** –
         For recommendations about maximum price options for Spot Instances, see [Spot Instance pricing history](../../../AWSEC2/latest/UserGuide/using-spot-instances-history.md "../../../AWSEC2/latest/UserGuide/using-spot-instances-history.md") in the
         *Amazon EC2 User Guide*.
        + **On-Demand base** – The minimum number of
         On-Demand Instances that your Auto Scaling group provisions before considering Spot
         Instances as your environment scales out.
        + **On-Demand above base** – The percentage of
         On-Demand Instances as part of any additional capacity that your Auto Scaling group
         provisions beyond the On-Demand base instances.


        ###### Note

        The options **On-Demand base** and **On-Demand
         above base** correlate to the **Min** and
         **Max**
        *Instances* options listed earlier. For more information
         about these options and examples, see [Spot Instance support for your Elastic Beanstalk
         environment](environments-cfg-autoscaling-spot.md "environments-cfg-autoscaling-spot.md").
        + **Capacity Rebalancing** – This option is only
         relevant when there is at least one Spot Instance in your Auto Scaling group. When
         this feature is enabled, EC2 automatically attempts to replace Spot Instances
         in the Auto Scaling group before they're interrupted, minimizing Spot Instance
         interruptions to your applications. For more information, see [Capacity Rebalancing](../../../autoscaling/ec2/userguide/capacity-rebalance.md "../../../autoscaling/ec2/userguide/capacity-rebalance.md") in the *Amazon EC2 Auto Scaling User
         Guide*

    - **Architecture** – The processor architecture for your
      EC2 instances. The processor architecture determines the EC2 Instance types that
      become available in the next field.
    - **Instance types** – The types of Amazon EC2 instance
      launched to run your application. For details, see [Instance types](using-features.managing.ec2.md#using-features.managing.ec2.instancetypes "using-features.managing.ec2.md#using-features.managing.ec2.instancetypes").
    - **AMI ID** – The machine image that Elastic Beanstalk uses to
      launch Amazon EC2 instances in your environment. For details, see [AMI ID](using-features.managing.ec2.md#using-features.managing.ec2.customami "using-features.managing.ec2.md#using-features.managing.ec2.customami").
    - **Availability Zones** – Choose the number of
      Availability Zones to spread your environment's instances across. By default, the
      Auto Scaling group launches instances evenly across all usable zones. To concentrate your
      instances in fewer zones, choose the number of zones to use. For production
      environments, use at least two zones to ensure that your application is available
      in case one Availability Zone goes out.
    - **Placement** (optional) – Choose the Availability
      Zones to use. Use this setting if your instances need to connect to resources in
      specific zones, or if you have purchased [reserved
      instances](../../../AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.md "../../../AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.md"), which are zone-specific.

    If you launch your environment in a custom VPC, you cannot configure this option.
    In a custom VPC, you choose Availability Zones for the subnets that you assign to
    your environment.
    - **Scaling cooldown** – The amount of time, in seconds,
      to wait for instances to launch or terminate after scaling, before continuing to
      evaluate triggers. For more information, see [Scaling Cooldowns](../../../autoscaling/ec2/userguide/Cooldown.md "../../../autoscaling/ec2/userguide/Cooldown.md").

6.  To save the changes choose **Apply** at the bottom of the page.

## Configuration using namespace

options

Elastic Beanstalk provides [configuration options](command-options.md "command-options.md") for Auto Scaling
settings in two namespaces: [aws:autoscaling:asg](command-options-general.md#command-options-general-autoscalingasg "command-options-general.md#command-options-general-autoscalingasg") and [aws:ec2:instances](command-options-general.md#command-options-general-ec2instances "command-options-general.md#command-options-general-ec2instances").

### The aws:autoscaling:asg

namespace

The [aws:autoscaling:asg](command-options-general.md#command-options-general-autoscalingasg "command-options-general.md#command-options-general-autoscalingasg") namespace provides options for overall
scale and availability.

The following [configuration file](ebextensions.md "ebextensions.md") example
configures the Auto Scaling group to use two to four instances, specific availability zones, and
a cooldown period of 12 minutes (720 seconds). It enables [Capacity Rebalancing](../../../autoscaling/ec2/userguide/capacity-rebalance.md "../../../autoscaling/ec2/userguide/capacity-rebalance.md")
for Spot Instances. This `EnableCapacityRebalancing` option only takes effect
if `EnableSpot` is set to `true` in the [aws:ec2:instances](command-options-general.md#command-options-general-ec2instances "command-options-general.md#command-options-general-ec2instances")
namespace, as shown in the configuration file example following this one.

```
option_settings:
  aws:autoscaling:asg:
    Availability Zones: Any
    Cooldown: '720'
    Custom Availability Zones: 'us-west-2a,us-west-2b'
    MaxSize: '4'
    MinSize: '2'
    EnableCapacityRebalancing: true
```

### The aws:ec2:instances

namespace

###### Note

When you update your environment configuration and remove one or more instance types from the `InstanceTypes` option, Elastic Beanstalk terminates
any Amazon EC2 instances running on any of the removed instance types. Your environment's Auto Scaling group then launches new instances, as necessary to complete
the desired capacity, using your current specified instance types.

The [aws:ec2:instances](command-options-general.md#command-options-general-ec2instances "command-options-general.md#command-options-general-ec2instances") namespace provides options related to your
environment's instances, including Spot Instance management. It complements [aws:autoscaling:launchconfiguration](command-options-general.md#command-options-general-autoscalinglaunchconfiguration "command-options-general.md#command-options-general-autoscalinglaunchconfiguration") and [aws:autoscaling:asg](command-options-general.md#command-options-general-autoscalingasg "command-options-general.md#command-options-general-autoscalingasg").

The following [configuration file](ebextensions.md "ebextensions.md") example
configures the Auto Scaling group to enable Spot Instance requests for your environment. It
designates three possible instance types that can be used. At least one On-Demand
Instance is used for baseline capacity, and a sustained 33% of On-Demand Instances is
used for any additional capacity.

The configuration sets the [spot allocation
strategy](environments-cfg-autoscaling-spot-allocation-strategy.md "environments-cfg-autoscaling-spot-allocation-strategy.md") to `capacity-optimized-prioritized`. This particular
allocation strategy prioritizes the instance launches from the pool based on the order
of the instance types specified in the `InstanceTypes` option. If
`SpotAllocationStrategy` is not specified it defaults to
`capacity-optimized`.

```
option_settings:
  aws:ec2:instances:
    EnableSpot: true
    InstanceTypes: 't2.micro,t3.micro,t3.small'
    SpotAllocationStrategy: capacity-optimized-prioritized
    SpotFleetOnDemandBase: '1'
    SpotFleetOnDemandAboveBasePercentage: '33'
```

To choose Spot Instance types, use the [Spot Instance
Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/ "https://aws.amazon.com/ec2/spot/instance-advisor/").

###### Important

The `EnableSpot`
option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch
templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom
policies instead of our managed policies, environment creation or updates might fail when you update your environment
configuration. For more information
and other considerations, see [Migrating your Elastic Beanstalk
environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md") .

## Configuration using the

AWS CLI

This section provides examples of how you can use the AWS CLI [create-environment](../../../cli/latest/reference/elasticbeanstalk/create-environment.md "../../../cli/latest/reference/elasticbeanstalk/create-environment.md") command to configure your environment with the Auto Scaling and
Capacity options described in these sections. You'll notice the namespace settings for
[aws:autoscaling:asg](command-options-general.md#command-options-general-autoscalingasg "command-options-general.md#command-options-general-autoscalingasg") and [aws:ec2:instances](command-options-general.md#command-options-general-ec2instances "command-options-general.md#command-options-general-ec2instances"), as
described in the previous [namespace
configuration options](#environments-cfg-autoscaling-namespace "#environments-cfg-autoscaling-namespace") section are also configured with this example.

The AWS Command Line Interface provides commands to create and configure Elastic Beanstalk
environments. With the `--option-settings` option, you can pass in namespace
options that are supported by Elastic Beanstalk. This means that the [namespace configuration options](#environments-cfg-autoscaling-namespace "#environments-cfg-autoscaling-namespace")
described previously can be passed into applicable AWS CLI commands to configure your Elastic Beanstalk
environment.

###### Note

You can also use the [update-environment](../../../cli/latest/reference/elasticbeanstalk/update-environment.md "../../../cli/latest/reference/elasticbeanstalk/update-environment.md") command with `--option-settings` to add or
update namespace options. If you need to remove any namespace options from your
environment use the **update-environment** command with
`--options-to-remove`.

The following example creates a new environment. Refer to the previous topic [namespace configuration options](#environments-cfg-autoscaling-namespace "#environments-cfg-autoscaling-namespace")
for more context about the options that are passed in.

The fist option listed, `IamInstanceProfile` in the [aws:autoscaling:launchconfiguration](command-options-general.md#command-options-general-autoscalinglaunchconfiguration "command-options-general.md#command-options-general-autoscalinglaunchconfiguration") namespace, is the
Elastic Beanstalk [instance profile](concepts-roles-instance.md "concepts-roles-instance.md"). It's required when
you create a new environment.

###### Example — create-environment with Auto Scaling options (namespace options inline)

```
aws elasticbeanstalk create-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2023 v4.3.0 running Python 3.12"` \
--option-settings \
Namespace=aws:autoscaling:launchconfiguration,OptionName=IamInstanceProfile,Value=`aws-elasticbeanstalk-ec2-role`
Namespace=aws:autoscaling:asg,OptionName=Availability Zones,Value=`Any` \
Namespace=aws:autoscaling:asg,OptionName=Cooldown,Value=`720` \
Namespace=aws:autoscaling:asg,OptionName=Custom Availability Zones,Value=`us-west-2a,us-west-2b` \
Namespace=aws:autoscaling:asg,OptionName=MaxSize,Value=`4` \
Namespace=aws:autoscaling:asg,OptionName=MinSize,Value=`2` \
Namespace=aws:autoscaling:asg,OptionName=EnableCapacityRebalancing,Value=`true` \
Namespace=aws:ec2:instances,OptionName=EnableSpot,Value=`true` \
Namespace=aws:ec2:instances,OptionName=InstanceTypes,Value=`t2.micro,t3.micro,t3.small` \
Namespace=aws:ec2:instances,OptionName=SpotAllocationStrategy,Value=`capacity-optimized-prioritized` \
Namespace=aws:ec2:instances,OptionName=SpotFleetOnDemandBase,Value=`1` \
Namespace=aws:ec2:instances,OptionName=SpotFleetOnDemandAboveBasePercentage,Value=`33`
```

###### Important

The `EnableSpot`
option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch
templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom
policies instead of our managed policies, environment creation or updates might fail when you update your environment
configuration. For more information
and other considerations, see [Migrating your Elastic Beanstalk
environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md") .

As an alternative, use an `options.json` file to specify the
namespace options instead of including them inline.

###### Example —create-environment with Auto Scaling options (namespace options in

`options.json` file)

```
aws elasticbeanstalk create-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2023 v4.3.0 running Python 3.12"`
--option-settings `file://options.json`
```

```
### example options.json ###
[
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "IamInstanceProfile",
        "Value": "aws-elasticbeanstalk-ec2-role"
    },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "Availability Zones",
        "Value": "Any"
    },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "Cooldown",
        "Value": "720"
    },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "Custom Availability Zones",
        "Value": "us-west-2a,us-west-2b"
    },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "MaxSize",
        "Value": "4"
    },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "MinSize",
        "Value": "2"
    },
    {
        "Namespace": "aws:autoscaling:asg",
        "OptionName": "EnableCapacityRebalancing",
        "Value": "true"
    },
    {
        "Namespace": "aws:ec2:instances",
        "OptionName": "EnableSpot",
        "Value": "true"
    },
    {
        "Namespace": "aws:ec2:instances",
        "OptionName": "InstanceTypes",
        "Value": "t2.micro,t3.micro,t3.small"
    },
    {
        "Namespace": "aws:ec2:instances",
        "OptionName": "SpotAllocationStrategy",
        "Value": "capacity-optimized-prioritized"
    },
    {
        "Namespace": "aws:ec2:instances",
        "OptionName": "SpotFleetOnDemandBase",
        "Value": "1"
    },
    {
        "Namespace": "aws:ec2:instances",
        "OptionName": "SpotFleetOnDemandAboveBasePercentage",
        "Value": "33"
    }
]
```

## Configuration using the EB

CLI

When creating an environment using the [eb
create](eb3-create.md "eb3-create.md") command, you can specify a few options that are related to
your environment's Auto Scaling group. These are some of the options that help you control the
capacity of your environment.

`--single`

Creates the environment with one Amazon EC2 instance and no load balancer. If you
don't use this option, a load-balancer is added to the environment that's
created.

`--enable-spot`

Enables Spot Instance requests for your environment.

###### Important

The `enable-spot`
option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch
templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom
policies instead of our managed policies, environment creation or updates might fail when you update your environment
configuration. For more information
and other considerations, see [Migrating your Elastic Beanstalk
environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md") .

The following options for the [eb
create](eb3-create.md "eb3-create.md") command can only be used with
`--enable-spot`.

`--instance-types`

Lists the Amazon EC2 instance types that you want your environment to
use.

`--spot-max-price`

The maximum price per unit hour, in US dollars, that you're willing to pay
for a Spot Instance. For recommendations about maximum price options for Spot Instances, see [Spot Instance pricing history](../../../AWSEC2/latest/UserGuide/using-spot-instances-history.md "../../../AWSEC2/latest/UserGuide/using-spot-instances-history.md") in the
_Amazon EC2 User Guide_.

`--on-demand-base-capacity`

The minimum number of On-Demand Instances that your Auto Scaling group provisions
before considering Spot Instances as your environment scales up.

`--on-demand-above-base-capacity`

The percentage of On-Demand Instances as part of additional capacity that
your Auto Scaling group provisions that's more than the number of instances that's
specified by the `--on-demand-base-capacity` option.

The following example creates an environment and configures the Auto Scaling group to enable
Spot Instance requests for the new environment. For this example, three possible instance
types can be used.

```
$ `eb create --enable-spot --instance-types "t2.micro,t3.micro,t3.small"`
```

###### Important

There is another similarly named option that's called `--instance-type`
(no “s”) that the EB CLI only recognizes when processing On-Demand Instances. Don't use
`--instance-type` (no "s") with the `--enable-spot` option. If
you do, the EB CLI ignores it. Instead use `--instance-types` (with "s") with
the `--enable-spot` option.
