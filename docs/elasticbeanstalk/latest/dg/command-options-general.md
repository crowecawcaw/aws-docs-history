

# General options for all environments
<a name="command-options-general"></a>

**Topics**
+ [aws:autoscaling:asg](#command-options-general-autoscalingasg)
+ [aws:autoscaling:launchconfiguration](#command-options-general-autoscalinglaunchconfiguration)
+ [aws:autoscaling:scheduledaction](#command-options-general-autoscalingscheduledaction)
+ [aws:autoscaling:trigger](#command-options-general-autoscalingtrigger)
+ [aws:autoscaling:updatepolicy:rollingupdate](#command-options-general-autoscalingupdatepolicyrollingupdate)
+ [aws:ec2:instances](#command-options-general-ec2instances)
+ [aws:ec2:vpc](#command-options-general-ec2vpc)
+ [aws:elasticbeanstalk:application](#command-options-general-elasticbeanstalkapplication)
+ [aws:elasticbeanstalk:application:environment](#command-options-general-elasticbeanstalkapplicationenvironment)
+ [aws:elasticbeanstalk:application:environmentsecrets](#command-options-general-elasticbeanstalk-application-environmentsecrets)
+ [aws:elasticbeanstalk:cloudwatch:logs](#command-options-general-cloudwatchlogs)
+ [aws:elasticbeanstalk:cloudwatch:logs:health](#command-options-general-cloudwatchlogs-health)
+ [aws:elasticbeanstalk:command](#command-options-general-elasticbeanstalkcommand)
+ [aws:elasticbeanstalk:environment](#command-options-general-elasticbeanstalkenvironment)
+ [aws:elasticbeanstalk:environment:process:default](#command-options-general-environmentprocess)
+ [aws:elasticbeanstalk:environment:process:process\_name](#command-options-general-environmentprocess-process)
+ [aws:elasticbeanstalk:environment:proxy:staticfiles](#command-options-general-environmentproxystaticfiles)
+ [aws:elasticbeanstalk:healthreporting:system](#command-options-general-elasticbeanstalkhealthreporting)
+ [aws:elasticbeanstalk:hostmanager](#command-options-general-elasticbeanstalkhostmanager)
+ [aws:elasticbeanstalk:managedactions](#command-options-general-elasticbeanstalkmanagedactions)
+ [aws:elasticbeanstalk:managedactions:platformupdate](#command-options-general-elasticbeanstalkmanagedactionsplatformupdate)
+ [aws:elasticbeanstalk:monitoring](#command-options-general-elasticbeanstalkmonitoring)
+ [aws:elasticbeanstalk:sns:topics](#command-options-general-elasticbeanstalksnstopics)
+ [aws:elasticbeanstalk:sqsd](#command-options-general-elasticbeanstalksqsd)
+ [aws:elasticbeanstalk:trafficsplitting](#command-options-general-elasticbeanstalktrafficsplitting)
+ [aws:elasticbeanstalk:windows:activedirectory](#command-options-general-elasticbeanstalkwindowsactivedirectory)
+ [aws:elasticbeanstalk:xray](#command-options-general-elasticbeanstalkxray)
+ [aws:elb:healthcheck](#command-options-general-elbhealthcheck)
+ [aws:elb:loadbalancer](#command-options-general-elbloadbalancer)
+ [aws:elb:listener](#command-options-general-elblistener)
+ [aws:elb:listener:listener\_port](#command-options-general-elblistener-listener)
+ [aws:elb:policies](#command-options-general-elbpolicies)
+ [aws:elb:policies:policy\_name](#command-options-general-elbpolicies-custom)
+ [aws:elbv2:listener:default](#command-options-general-elbv2-listener-default)
+ [aws:elbv2:listener:listener\_port](#command-options-general-elbv2-listener)
+ [aws:elbv2:listenerrule:rule\_name](#command-options-general-elbv2-listenerrule)
+ [aws:elbv2:loadbalancer](#command-options-general-elbv2)
+ [aws:rds:dbinstance](#command-options-general-rdsdbinstance)

## aws:autoscaling:asg
<a name="command-options-general-autoscalingasg"></a>

Configure your environment's Auto Scaling group. For more information, see [Auto Scaling your Elastic Beanstalk environment instances](using-features.managing.as.md).


**Namespace: `aws:autoscaling:asg`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| Availability Zones | Availability Zones (AZs) are distinct locations within an AWS Region that are engineered to be isolated from failures in other AZs. They provide inexpensive, low-latency network connectivity to other AZs in the same Region. Choose the number of AZs for your instances. | `Any` | `Any`<br />`Any 1`<br />`Any 2`<br />`Any 3` | 
| Cooldown | Cooldown periods help prevent Amazon EC2 Auto Scaling from initiating additional scaling activities before the effects of previous activities are visible. A cooldown period is the amount of time, in seconds, after a scaling activity completes before another scaling activity can start. | `360`  | `0` to `10000` | 
| Custom Availability Zones | Define the AZs for your instances. | None | `us-east-1a` <br />`us-east-1b` <br />`us-east-1c` <br />`us-east-1d` <br />`us-east-1e` <br />`eu-central-1`  | 
| EnableCapacityRebalancing | Specifies whether to enable the Capacity Rebalancing feature for Spot Instances in your Auto Scaling Group. For more information, see [Capacity Rebalancing](https://docs.aws.amazon.com/autoscaling/ec2/userguide/capacity-rebalance.html) in the *Amazon EC2 Auto Scaling User Guide*.<br />This option is only relevant when `EnableSpot` is set to `true` in the [`aws:ec2:instances`](#command-options-general-ec2instances) namespace, and there is at least one Spot Instance in your Auto Scaling group. | `false` | `true`<br />`false` | 
| MinSize | The minimum number of instances that you want in your Auto Scaling group. | `1`  | `1` to `10000` | 
| MaxSize | The maximum number of instances that you want in your Auto Scaling group. | `4`  | `1` to `10000` | 

## aws:autoscaling:launchconfiguration
<a name="command-options-general-autoscalinglaunchconfiguration"></a>

Configure the Amazon Elastic Compute Cloud (Amazon EC2) instances for your environment.

The instances that are used for your environment are created using either an Amazon EC2 launch template or an Auto Scaling group launch configuration resource. The following options work with both of these resource types.

For more information, see [The Amazon EC2 instances for your Elastic Beanstalk environment](using-features.managing.ec2.md). You can also reference more information about Amazon Elastic Block Store (EBS) in [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) chapter in the *Amazon EC2 User Guide*.


**Namespace: `aws:autoscaling:launchconfiguration`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| DisableDefaultEC2SecurityGroup | When set to the default value of `false`, Elastic Beanstalk creates a default security group that allows traffic from the internet or load balancer on the standard ports for HTTP (80). It attaches this security group to the EC2 instances of the environment when it creates the environment.<br />When set to `true` Elastic Beanstalk will not assign the default security group to the EC2 instances for a new environment. For an existing environment, Elastic Beanstalk will unassign the default EC2 security group from your environment's EC2 instances. As a result, you must also set the following configurations:+  The `SecurityGroups` option of this namespace will require at least one value to define your custom security group(s). <br />+  For environments with a load balancer, you will also need to set the `SecurityGroups` options in another namespace to configure custom security groups for the load balancer. For application load balancers, set the option in the [aws:elbv2:loadbalancer](#command-options-general-elbv2) namespace. For classic load balancers, set the option in the [aws:elb:loadbalancer](#command-options-general-elbloadbalancer) namespace. <br />+  For more information, see [Managing EC2 security groups](using-features.managing.ec2.instances.sg.md).  <br />If a value is specified for EC2KeyName in an environment that has `DisableDefaultEC2SecurityGroup` set to `true` a default security group will not be associated with the EC2 instances. | `false` | `true`<br />`false` | 
| DisableIMDSv1 | Set to `true` to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2.<br />Set to `false` to enable both IMDSv1 and IMDSv2.<br />The instances for your environment default as follows, based on the platform operating system: +   *Windows Server 2019, AL2, and earlier* – enable both IMDSv1 and IMDSv2 (DisableIMDSv1 defaults to `false`) <br />+  *AL2023, and Windows Server 2022 and later* – enable only IMDSv2 (DisableIMDSv1 defaults to `true`) <br />For more information, see [Configuring the instance metadata service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html).  This option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom policies instead of our managed policies, environment creation or updates might fail when you update your environment configuration. For more information and other considerations, see [Migrating your Elastic Beanstalk environment to launch templates](environments-cfg-autoscaling-launch-templates.md).  | `false` – platforms based on Windows server, Amazon Linux 2 and earlier<br />`true` – platforms based on Amazon Linux 2023 | `true`<br />`false` | 
| EC2KeyName | You can use a key pair to securely log into your EC2 instance.<br />If a value is specified for `EC2KeyName` in an environment that has `DisableDefaultEC2SecurityGroup` set to `true` a default security group will not be associated with the EC2 instances. If you use the Elastic Beanstalk console to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console overrides this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | None |  | 
| IamInstanceProfile | An instance profile enables AWS Identity and Access Management (IAM) users and AWS services to access temporary security credentials to make AWS API calls. Specify the instance profile's name or its ARN.<br />Examples:+  `aws-elasticbeanstalk-ec2-role` <br />+  `arn:aws:iam::123456789012:instance-profile/aws-elasticbeanstalk-ec2-role`  If you use the Elastic Beanstalk console or EB CLI to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console and EB CLI override this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | None | Instance profile name or ARN. | 
| ImageId | You can override the default Amazon Machine Image (AMI) by specifying your own custom AMI ID.<br />Example: `ami-1f316660` | None |  | 
| InstanceType | The instance type that's used to run your application in an Elastic Beanstalk environment. The `InstanceType` option is obsolete. It's replaced by the newer and more powerful `InstanceTypes` option in the [`aws:ec2:instances`](#command-options-general-ec2instances) namespace. You can use this new option to specify a list of one or more instance types for your environment. The first value on that list is equivalent to the value of the `InstanceType` option that's included in the `aws:autoscaling:launchconfiguration` namespace that's described here. We recommend that you specify instance types by using the new option. If specified, the new option takes precedence over the previous one. For more information, see [The aws:ec2:instances namespace](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace.instances). <br />The instance types that are available depend on the Availability Zones and Region used. If you choose a subnet, the Availability Zone that contains that subnet determines the available instance types. +  Elastic Beanstalk doesn't support Amazon EC2 Mac instance types. <br />+  For more information about Amazon EC2 instance families and types, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*. <br />+  For more information on the available instance types across Regions, see [Available instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes) in the *Amazon EC2 User Guide*.  If you use the Elastic Beanstalk console or EB CLI to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console and EB CLI override this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | Varies by account and Region. | One EC2 instance type.<br />Varies by account, Region, and Availability Zone. You can obtain a list of Amazon EC2 instance types filtered by these values. For more information, see [Available instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes) in the *Amazon EC2 User Guide*. | 
| LaunchTemplateTagPropagationEnabled | Set to `true` to enable the propagation of environment tags to the launch templates for specific resources provisioned to the environment. <br />Elastic Beanstalk can only propagate tags to launch templates for the following resources:+  EBS volumes <br />+  EC2 instances  <br />+  EC2 network interfaces <br />+  CloudFormation launch templates that define a resource <br />This constraint exists because CloudFormation only allows tags on template creation for specific resources. For more information see [TagSpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecification.html) in the *AWS CloudFormation User Guide*.   Changing this option value from `false` to `true` for an existing environment may be a breaking change for previously existing tags.   When this feature is enabled, the propagation of tags will require EC2 replacement, which can result in downtime. You can enable *rolling updates* to apply configuration changes in batches and prevent downtime during the update process. For more information, see [Configuration changes](environments-updating.md).   <br />For more information about launch templates, see the following:+  [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html) in the *Amazon EC2 Auto Scaling User Guide* <br />+  [Working with templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the *AWS CloudFormation User Guide* <br />+  [Elastic Beanstalk template snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-elasticbeanstalk.html) in the *AWS CloudFormation User Guide* <br />For more information about this option, see [Tag propagation to launch templates](applications-tagging-resources.launch-templates.md). | `false` | `true`<br />`false` | 
| MonitoringInterval | The interval (in minutes) that you want Amazon CloudWatch metrics to be returned at. | `5 minute` | `1 minute`<br />`5 minute` | 
| SecurityGroups | Lists the Amazon EC2 security group IDs to assign to the EC2 instances in the Auto Scaling group to define firewall rules for the instances.<br />Use this option along with `DisableDefaultEC2SecurityGroup` to attach your own custom security groups that define firewall rules for the EC2 instances. For more information, see [Load balanced (multi-instance) environments](using-features.managing.ec2.instances.sg.md#using-features.managing.ec2.instances.sg.load-balancer-security). You may need to complete some additional configuration to prevent incoming traffic to your EC2 instances from being blocked. This only applies to multi-instance environments with custom EC2 security groups. The EC2 security groups must include an inbound rule that grants access to traffic routed from the load balancer. For more information, see [Managing EC2 security groups in multi-instance environments](using-features.managing.ec2.instances.sg.md#using-features.managing.ec2.instances.sg.load-balancer-security). <br />You can provide a single string of comma-separated values that contain existing Amazon EC2 security groups IDs or references to AWS::EC2::SecurityGroup resources created in the template. <br />You must provide at least one value for this option if `DisableDefaultEC2SecurityGroup` for this namespace is set to `true`. | `elasticbeanstalk-default`  |  | 
|  SSHSourceRestriction | Used to lock down SSH access to an environment. For example, you can lock down SSH access to the EC2 instances so that only a bastion host can access the instances in the private subnet.<br />This string takes the following form:<br />`{{protocol}}, {{fromPort}}, {{toPort}}, {{source_restriction}}`**{{protocol}}**<br /> The protocol for the ingress rule. <br />**{{fromPort}}**<br /> The starting port number. <br />**{{toPort}}**<br /> The ending port number. <br />**{{source\_restriction}}**<br /> The Classless Inter-Domain Routing (CIDR) range or the security group that traffic must route through. Specify the security group with the security group ID. <br />To specify a security group from another account, include the AWS account ID before the security group ID, separated by a forward slash. The other account must be in the same AWS Region. Note the syntax: `{{aws-account-id}}/{{security-group-id}}`. For example: `123456789012/sg-99999999` +  `tcp, 22, 22, 54.240.196.185/32` <br />+  `tcp, 22, 22, my-security-group-id` <br />+  `tcp, 22, 22, 123456789012/their-security-group-id`  | None |  | 
| BlockDeviceMappings | Attach additional Amazon EBS volumes or instance store volumes on all of the instances in the Auto Scaling group. This option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom policies instead of our managed policies, environment creation or updates might fail when you update your environment configuration. For more information and other considerations, see [Migrating your Elastic Beanstalk environment to launch templates](environments-cfg-autoscaling-launch-templates.md). <br />When mapping instance store volumes, you only need to map the device name to a volume name. However, we recommend, when mapping Amazon EBS volumes, you additionally specify some or all of the following fields (each field must be separated by a colon):+  snapshot ID <br />+  size, in GB <br />+  delete on terminate (`true` or `false`) <br />+  storage type (only for `gp3`, `gp2`, `standard`, `st1`, `sc1`, or `io1`) <br />+  IOPS (only for `gp3` or `io1`) <br />+  throughput (only for `gp3`) <br />The following example attaches three Amazon EBS volumes, one blank 100GB gp2 volume and one snapshot, one blank 20GB io1 volume with 2000 provisioned IOPS, and an instance store volume `ephemeral0`. Multiple instance store volumes can be attached if the instance type supports it.<br /> `/dev/sdj=:100:true:gp2,/dev/sdh=snap-51eef269,/dev/sdi=:20:true:io1:2000,/dev/sdb=ephemeral0`  | None |  +  size — must be between 500 and 16384 GiB <br />+  throughput — must be between 125 and 1000 mebibytes per second (MiB/s)   | 
| RootVolumeType | Volume type (magnetic, general purpose SSD or provisioned IOPS SSD) to use for the root Amazon EBS volume attached to the EC2 instances for your environment. This option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom policies instead of our managed policies, environment creation or updates might fail when you update your environment configuration. For more information and other considerations, see [Migrating your Elastic Beanstalk environment to launch templates](environments-cfg-autoscaling-launch-templates.md).  | Varies by platform. | `standard` for magnetic storage.<br />`gp2` or `gp3` for general purpose SSD.<br />`io1` for provisioned IOPS SSD. | 
| RootVolumeSize | The storage capacity of the root Amazon EBS volume in whole GB.<br />Required if you set `RootVolumeType` to provisioned IOPS SSD.<br />For example, `"64"`. | Varies per platform for magnetic storage and general purpose SSD.<br />None for provisioned IOPS SSD. | `10` to `16384` GB for general purpose and provisioned IOPS SSD.<br />`8` to `1024` GB for magnetic. | 
| RootVolumeIOPS | The desired input/output operations per second (IOPS) for a provisioned IOPS SSD root volume or for a general purpose `gp3` SSD root volume.<br />The maximum ratio of IOPS to volume size is 500 to 1. For example, a volume with 3000 IOPS must be at least 6 GiB. | None | `100` to `20000` for io1 provisioned IOPS SSD root volumes.<br />`3000` to `16000` for general purpose `gp3` SSD root volumes. | 
| RootVolumeThroughput | The desired throughput of mebibytes per second (MiB/s) to provision for the Amazon EBS root volume attached to your environment's EC2 instance. This option is only applicable to `gp3` storage types.  | None | `125` to `1000` | 

## aws:autoscaling:scheduledaction
<a name="command-options-general-autoscalingscheduledaction"></a>

Configure [scheduled actions](environments-cfg-autoscaling-scheduledactions.md) for your environment's Auto Scaling group. For each action, specify a `resource_name` in addition to the option name, namespace, and value for each setting. See [The aws:autoscaling:scheduledaction namespace](environments-cfg-autoscaling-scheduledactions.md#environments-cfg-autoscaling-scheduledactions-namespace) for examples.


**Namespace: `aws:autoscaling:scheduledaction`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| StartTime | For one-time actions, choose the date and time to run the action. For recurrent actions, choose when to activate the action. | None | A [ISO-8601 timestamp](http://www.w3.org/TR/NOTE-datetime) unique across all scheduled scaling actions. | 
| EndTime | A date and time in the future (in the UTC/GMT time zone) when you want the scheduled scaling action to stop repeating. If you don't specify an **EndTime**, the action recurs according to the `Recurrence` expression.<br />Example: `2015-04-28T04:07:2Z`<br />When a scheduled action ends, Amazon EC2 Auto Scaling doesn't automatically revert to its previous settings. Configure a second scheduled action to return to the original settings as needed. | None | A [ISO-8601 timestamp](http://www.w3.org/TR/NOTE-datetime) unique across all scheduled scaling actions. | 
| MaxSize | The maximum instance count to apply when the action runs. | None | `0` to `10000` | 
| MinSize | The minimum instance count to apply when the action runs. | None | `0` to `10000` | 
| DesiredCapacity | Set the initial desired capacity for the Auto Scaling group. After the scheduled action is applied, triggers adjust the desired capacity based on their settings. | None | `0` to `10000` | 
| Recurrence | The frequency that you want the scheduled action to occur at. If you don't specify a recurrence, then the scaling action occurs only once, as specified by the `StartTime`. | None | A [Cron](http://en.wikipedia.org/wiki/Cron) expression. | 
| Suspend | Set to `true` to deactivate a recurrent scheduled action temporarily. |  `false`  |  `true` <br /> `false`  | 

## aws:autoscaling:trigger
<a name="command-options-general-autoscalingtrigger"></a>

Configure scaling triggers for your environment's Auto Scaling group.

**Note**  
Three options in this namespace determine how long the metric for a trigger can remain beyond its defined limits before the trigger initates. These options are related as follows:  
`BreachDuration = Period * EvaluationPeriods`  
The default values for these options (5, 5, and 1, respectively) satisfy this equation. If you specify inconsistent values, Elastic Beanstalk might modify one of the values so that the equation is still satisfied.


**Namespace: `aws:autoscaling:trigger`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| BreachDuration | The amount of time, in minutes, a metric can be beyond its defined limit (as specified in the `UpperThreshold` and `LowerThreshold`) before the trigger is invoked. | `5` | `1` to `600` | 
| LowerBreachScaleIncrement | How many Amazon EC2 instances to remove when performing a scaling activity. | `-1` |  | 
| LowerThreshold | If the measurement falls below this number for the breach duration, a trigger is invoked. | `2000000` | `0` to `20000000` | 
| MeasureName | The metric that's used for your Auto Scaling trigger. `HealthyHostCount`, `UnhealthyHostCount` and `TargetResponseTime` are only applicable for environments with a dedicated load balancer. These aren't valid metric values for environments configured with a shared load balancer. For more information about load balancer types, see [Load balancer for your Elastic Beanstalk environment](using-features.managing.elb.md).  | `NetworkOut` | `CPUUtilization`<br />`NetworkIn`<br />`NetworkOut`<br />`DiskWriteOps`<br />`DiskReadBytes`<br />`DiskReadOps`<br />`DiskWriteBytes`<br />`Latency`<br />`RequestCount`<br />`HealthyHostCount`<br />`UnhealthyHostCount`<br />`TargetResponseTime` | 
| Period | Specifies how frequently Amazon CloudWatch measures the metrics for your trigger. The value is the number of minutes between two consecutive periods. | `5` | `1` to `600` | 
| EvaluationPeriods | The number of consecutive evaluation periods that's used to determine if a breach is occurring. | `1` | `1` to `600` | 
| Statistic | The Statistic the trigger uses, such as `Average`. | `Average` | `Minimum`<br />`Maximum`<br />`Sum`<br />`Average` | 
| Unit | The unit for the trigger measurement, such as `Bytes`. | `Bytes` | `Seconds`<br />`Percent`<br />`Bytes` <br />`Bits` <br />`Count` <br />`Bytes/Second` <br />`Bits/Second` <br />`Count/Second` <br />`None`  | 
| UpperBreachScaleIncrement | Specifies how many Amazon EC2 instances to add when performing a scaling activity. | `1` |  | 
| UpperThreshold | If the measurement is higher than this number for the breach duration, a trigger is invoked. | `6000000` | `0` to `20000000` | 

## aws:autoscaling:updatepolicy:rollingupdate
<a name="command-options-general-autoscalingupdatepolicyrollingupdate"></a>

Configure rolling updates your environment's Auto Scaling group.


**Namespace: `aws:autoscaling:updatepolicy:rollingupdate`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| MaxBatchSize | The number of instances included in each batch of the rolling update. | One-third of the minimum size of the Auto Scaling group, rounded to the next highest integer. | `1` to `10000` | 
| MinInstancesInService | The minimum number of instances that must be in service within the Auto Scaling group while other instances are terminated. | The minimum size of the Auto Scaling group or one fewer than the maximum size of the Auto Scaling group, whichever is lower. | `0` to `9999` | 
| RollingUpdateEnabled | If `true`, it enables rolling updates for an environment. Rolling updates are useful when you need to make small, frequent updates to your Elastic Beanstalk software application and you want to avoid application downtime.<br />Setting this value to true automatically enables the `MaxBatchSize`, `MinInstancesInService`, and `PauseTime` options. Setting any of those options also automatically sets the `RollingUpdateEnabled` option value to `true`. Setting this option to `false` disables rolling updates. If you use the Elastic Beanstalk console or EB CLI to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console and EB CLI override this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `false` | `true`<br />`false` | 
| RollingUpdateType | This includes three types: time-based rolling updates, health-based rolling updates, and immutable updates. <br />Time-based rolling updates apply a PauseTime between batches. Health-based rolling updates wait for new instances to pass health checks before moving on to the next batch. [Immutable updates](environmentmgmt-updates-immutable.md) launch a full set of instances in a new Auto Scaling group. If you use the Elastic Beanstalk console or EB CLI to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console and EB CLI override this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `Time` | `Time`<br />`Health`<br />`Immutable` | 
| PauseTime | The amount of time (in seconds, minutes, or hours) the Elastic Beanstalk service waits after it completed updates to one batch of instances and before it continues on to the next batch. | Automatically computed based on instance type and container. | `PT0S`\* (0 seconds) to `PT1H` (1 hour) | 
| Timeout | The maximum amount of time (in minutes or hours) to wait for all instances in a batch of instances to pass health checks before canceling the update. | `PT30M` (30 minutes) | `PT5M`\* (5 minutes) to `PT1H` (1 hour)<br />\*[ISO8601 duration](http://en.wikipedia.org/wiki/ISO_8601#Durations) format: `PT{{#}}H{{#}}M{{#}}S` where each \# is the number of hours, minutes, and/or seconds, respectively. | 

## aws:ec2:instances
<a name="command-options-general-ec2instances"></a>

Configure your environment's instances, including Spot options. This namespace complements [`aws:autoscaling:launchconfiguration`](#command-options-general-autoscalinglaunchconfiguration) and [`aws:autoscaling:asg`](#command-options-general-autoscalingasg).

For more information, see [Auto Scaling your Elastic Beanstalk environment instances](using-features.managing.as.md).


**Namespace: `aws:ec2:instances`**  

| **Name** | **Description** | **Default** | **Valid values** | 
| --- | --- | --- | --- | 
| EnableSpot | Enable Spot Instance requests for your environment. When `false`, some options in this namespace don't take effect. This option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom policies instead of our managed policies, environment creation or updates might fail when you update your environment configuration. For more information and other considerations, see [Migrating your Elastic Beanstalk environment to launch templates](environments-cfg-autoscaling-launch-templates.md).  | `false` | `true`<br />`false` | 
| InstanceTypes | A comma-separated list of instance types that you want your environment to use (for example, `t2.micro,t3.micro`).<br />When `EnableSpot` is `true` and `SpotAllocationStrategy` is set to `capacity-optimized-prioritized`, the list of values specified in this option determines the instance type priority for the Spot Instance allocation strategy.<br />When Spot Instances are not activated (`EnableSpot` is `false`), only the first instance type on the list is used.<br />The first instance type on the list in this option is equivalent to the value of the `InstanceType` option in the [`aws:autoscaling:launchconfiguration`](#command-options-general-autoscalinglaunchconfiguration) namespace. We don't recommend using the latter option because it's obsolete. If you specify both, the first instance type on the list in the `InstanceTypes` option is used, and `InstanceType` is ignored.<br />The instance types that are available depend on the Availability Zones and Region used. If you choose a subnet, the Availability Zone that contains that subnet determines the available instance types. +  Elastic Beanstalk doesn't support Amazon EC2 Mac instance types. <br />+  For more information about Amazon EC2 instance families and types, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*. <br />+  For more information on the available instance types across Regions, see [Available instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes) in the *Amazon EC2 User Guide*.  Some older AWS accounts might provide Elastic Beanstalk with default instance types that don't support Spot Instances (for example, t1.micro). If you activate Spot Instance requests and you get an error about an instance type that doesn’t support Spot, be sure to configure instance types that support Spot. To choose Spot Instance types, use the [Spot Instance Advisor](https://aws.amazon.com/ec2/spot/instance-advisor/). <br />When you update your environment configuration and remove one or more instance types from the `InstanceTypes` option, Elastic Beanstalk terminates any Amazon EC2 instances running on any of the removed instance types. Your environment's Auto Scaling group then launches new instances, as necessary to complete the desired capacity, using your current specified instance types. | A list of two instance types.<br />Varies by account and Region. | One to forty EC2 instance types. We recommend at least two.<br />Varies by account, Region, and Availability Zone. You can obtain a list of Amazon EC2 instance types filtered by these values. For more information, see [Available instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes) in the *Amazon EC2 User Guide*.<br />The instance types must all be part of the same architecture (`arm64`, `x86_64`, `i386`).<br />`SupportedArchitectures` is also part of this namespace. If you provide any values for `SupportedArchitectures`, the value(s) you enter for `InstanceTypes` must belong to one, and only one, of the architectures you provide for `SupportedArchitectures`. | 
| SpotAllocationStrategy | Specifies the [spot instance allocation strategy](environments-cfg-autoscaling-spot-allocation-strategy.md) that determines how Spot Instances are allocated from the available spot capacity pools.<br />If set to `capacity-optimized-prioritized`, the order of the values in `InstanceTypes` sets the instance type priority for allocation.<br />This option is relevant only when `EnableSpot` is `true`. | `capacity-optimized` | `capacity-optimized`<br />`price-capacity-optimized`<br />`capacity-optimized-prioritized`<br />`lowest-price ` | 
| SpotFleetOnDemandBase | The minimum number of On-Demand Instances that your Auto Scaling group provisions before considering Spot Instances as your environment scales up.<br />This option is relevant only when `EnableSpot` is `true`. | `0` | `0` to `MaxSize` option in [`aws:autoscaling:asg`](#command-options-general-autoscalingasg) namespace | 
| SpotFleetOnDemandAboveBasePercentage | The percentage of On-Demand Instances as part of additional capacity that your Auto Scaling group provisions beyond the `SpotOnDemandBase` instances.<br />This option is relevant only when `EnableSpot` is `true`. | `0` for a single-instance environment<br />`70` for a load-balanced environment | `0` to `100` | 
| SpotMaxPrice | The maximum price per unit hour, in USD, that you're willing to pay for a Spot Instance. For recommendations about maximum price options for Spot Instances, see [Spot Instance pricing history](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html) in the *Amazon EC2 User Guide*.<br />This option is relevant only when `EnableSpot` is `true`. | On-Demand price, for each instance type. The option's value in this case is `null`. | `0.001` to `20.0`<br />`null` | 
| SupportedArchitectures | A comma-separated list of EC2 instance architecture types that you'll use for your environment.<br />Elastic Beanstalk supports instance types based on the following processor architectures:+  AWS Graviton 64-bit Arm architecture (arm64) <br />+  64-bit architecture (x86\_64) <br />+  32-bit architecture (i386) <br />For more information about processor architecture and Amazon EC2 instance types see [Amazon EC2 instance types](using-features.managing.ec2.instance-types.md). | None | `arm64`<br />`x86_64`<br />`i386` The 32-bit architecture `i386` is not supported by the majority of Elastic Beanstalk platforms. We recommended that you choose the `x86_64` or `arm64` architecture types instead.  | 

## aws:ec2:vpc
<a name="command-options-general-ec2vpc"></a>

Configure your environment to launch resources in a custom [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/) (Amazon VPC). If you don't configure settings in this namespace, Elastic Beanstalk launches resources in the default VPC.


**Namespace: `aws:ec2:vpc`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| VPCId | The ID for your Amazon VPC. | None |  | 
| Subnets | The IDs of the Auto Scaling group subnet or subnets. If you have multiple subnets, specify the value as a single comma-separated string of subnet IDs (for example, `"subnet-11111111,subnet-22222222"`). | None |  | 
| ELBSubnets | The IDs of the subnet or subnets for the elastic load balancer. If you have multiple subnets, specify the value as a single comma-separated string of subnet IDs (for example, `"subnet-11111111,subnet-22222222"`). | None |  | 
| ELBScheme | Specify `internal` if you want to create an internal load balancer in your Amazon VPC so that your Elastic Beanstalk application can't be accessed from outside your Amazon VPC. If you specify a value other than `public` or `internal`, Elastic Beanstalk ignores the value. | `public`  | `public` <br />`internal`  | 
| DBSubnets | Contains the IDs of the database subnets. This is only used if you want to add an Amazon RDS DB Instance as part of your application. If you have multiple subnets, specify the value as a single comma-separated string of subnet IDs (for example, `"subnet-11111111,subnet-22222222"`). | None |  | 
| AssociatePublicIpAddress | Specifies whether to launch instances with public IP addresses in your Amazon VPC. Instances with public IP addresses don't require a NAT device to communicate with the Internet. You must set the value to `true` if you want to include your load balancer and instances in a single public subnet.<br />This option has no effect on a single-instance environment, which always has a single Amazon EC2 instance with an Elastic IP address. The option is relevant to load-balanced, scalable environments. | None | `true` <br />`false`  | 

## aws:elasticbeanstalk:application
<a name="command-options-general-elasticbeanstalkapplication"></a>

Configure a health check path for your application. For more information, see [Basic health reporting](using-features.healthstatus.md).


**Namespace: `aws:elasticbeanstalk:application`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| Application Healthcheck URL | The path where health check requests are sent to. If this path isn't set, the load balancer attempts to make a TCP connection on port 80 to verify the health status of your application. Set to a path starting with `/` to send an HTTP GET request to that path. You can also include a protocol (HTTP, HTTPS, TCP, or SSL) and port before the path to check HTTPS connectivity or use a non-default port. If you use the Elastic Beanstalk console to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console overrides this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | None | Valid values include:<br />`/` (HTTP GET to root path)<br />`/{{health}}`<br />`HTTPS:443/`<br />`HTTPS:443/{{health}}` | 

The EB CLI and Elastic Beanstalk console apply recommended values for the preceding options. You must remove these settings if you want to use configuration files to configure the same. See [Recommended values](command-options.md#configuration-options-recommendedvalues) for details.

## aws:elasticbeanstalk:application:environment
<a name="command-options-general-elasticbeanstalkapplicationenvironment"></a>

Configure environment properties for your application.


**Namespace: `aws:elasticbeanstalk:application:environment`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| Any environment variable name. | Pass in key-value pairs. | None | Any environment variable value. | 

See [Environment variables and other software settings](environments-cfg-softwaresettings.md) for more information.

## aws:elasticbeanstalk:application:environmentsecrets
<a name="command-options-general-elasticbeanstalk-application-environmentsecrets"></a>

Configure environment variables to serve as *environment secrets* for your application. Environment secrets store AWS Secrets Manager secrets or AWS Systems Manager Parameter Store parameters.


**Namespace: `aws:elasticbeanstalk:application:environmentsecrets`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| OptionName | Specifies the name of the environment variable to hold the secret store or parameter store value. | None | Any environment variable name. | 
| Value | Specifies the ARN for the value stored in AWS Secrets Manager or AWS Systems Manager Parameter Store. During instance bootstrapping Elastic Beanstalk initiates the environment variable to the value stored in this ARN resource. Ensure that the necessary permissions are in place for your environment's EC2 instance profile role to access the secret and parameter ARNs. For more information, see [Required IAM permissions](AWSHowTo.secrets.IAM-permissions.md).  | None | Valid ARN value for an AWS Secrets Manager secret or AWS Systems Manager Parameter Store parameter value. | 

For more information, see [Configuring secrets as environment variables](AWSHowTo.secrets.env-vars.md).

## aws:elasticbeanstalk:cloudwatch:logs
<a name="command-options-general-cloudwatchlogs"></a>

Configure instance log streaming for your application.


**Namespace: `aws:elasticbeanstalk:cloudwatch:logs`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| StreamLogs | Specifies whether to create groups in CloudWatch Logs for proxy and deployment logs, and stream logs from each instance in your environment. | `false` | `true`<br />`false` | 
| DeleteOnTerminate | Specifies whether to delete the log groups when the environment is terminated. If `false`, the logs are kept `RetentionInDays` days. | `false` | `true`<br />`false` | 
| RetentionInDays | The number of days to keep log events before they expire. | 7 | 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653 | 

## aws:elasticbeanstalk:cloudwatch:logs:health
<a name="command-options-general-cloudwatchlogs-health"></a>

Configure environment health log streaming for your application.


**Namespace: `aws:elasticbeanstalk:cloudwatch:logs:health`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| HealthStreamingEnabled | For environments with enhanced health reporting enabled, specifies whether to create a group in CloudWatch Logs for environment health and archive Elastic Beanstalk environment health data. For information about enabling enhanced health, see [`aws:elasticbeanstalk:healthreporting:system`](#command-options-general-elasticbeanstalkhealthreporting). | `false` | `true`<br />`false` | 
| DeleteOnTerminate | Specifies whether to delete the log group when the environment is terminated. If `false`, the health data is kept `RetentionInDays` days. | `false` | `true`<br />`false` | 
| RetentionInDays | The number of days to keep the archived health data before it expires. | 7 | 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653 | 

## aws:elasticbeanstalk:command
<a name="command-options-general-elasticbeanstalkcommand"></a>

Configure the deployment policy for your application code. For more information, see [Deployment policies and settings](using-features.rolling-version-deploy.md).


**Namespace: `aws:elasticbeanstalk:command`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| DeploymentPolicy | Choose a [deployment policy](using-features.rolling-version-deploy.md) for application version deployments. If you use the Elastic Beanstalk console to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console overrides this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `AllAtOnce` | `AllAtOnce`<br />`Rolling`<br />`RollingWithAdditionalBatch`<br />`Immutable`<br />`TrafficSplitting` | 
| Timeout | The amount of time, in seconds, to wait for an instance to complete executing commands.<br />Elastic Beanstalk internally adds 240 seconds (four minutes) to the `Timeout` value. For example, the effective timeout by default is 840 seconds (600 \+ 240), or 14 minutes. | `600`  | `1` to `3600` | 
| BatchSizeType | The type of number that's specified in **BatchSize**. If you use the Elastic Beanstalk console or EB CLI to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console and EB CLI override this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `Percentage`  | `Percentage` <br />`Fixed`  | 
| BatchSize | The percentage or the fixed number of Amazon EC2 instances in the Auto Scaling group to simultaneously perform deployments on. Valid values vary depending on the **BatchSizeType** setting used. If you use the Elastic Beanstalk console or EB CLI to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console and EB CLI override this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `100`  | `1` to `100` (`Percentage`).<br />`1` to [aws:autoscaling:asg::MaxSize](#command-options-general-autoscalingasg) (`Fixed`) | 
| IgnoreHealthCheck | Don't cancel a deployment due to failed health checks. | false  | `true` <br />`false`  | 

## aws:elasticbeanstalk:environment
<a name="command-options-general-elasticbeanstalkenvironment"></a>

Configure your environment's architecture and service role.


**Namespace: `aws:elasticbeanstalk:environment`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| EnvironmentType | Set to `SingleInstance` to launch one EC2 instance with no load balancer. | `LoadBalanced`  | `SingleInstance` <br />`LoadBalanced`  | 
| ServiceRole | The name of an IAM role that Elastic Beanstalk uses to manage resources for the environment. Specify a role name (optionally prefixed with a custom path) or its ARN.<br />Examples:+  `aws-elasticbeanstalk-service-role` <br />+  `{{custom-path}}/{{custom-role}}` <br />+  `arn:aws:iam::123456789012:role/aws-elasticbeanstalk-service-role`  If you use the Elastic Beanstalk console or EB CLI to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console and EB CLI override this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | None | IAM role name, path/name, or ARN | 
| LoadBalancerType | The type of load balancer for your environment. For more information, see [Load balancer for your Elastic Beanstalk environment](using-features.managing.elb.md). | `classic` | `classic`<br />`application`<br />`network` | 
| LoadBalancerIsShared | Specifies whether the environment's load balancer is dedicated or shared. This option can only be set for an Application Load Balancer. It can't be changed after the environment is created.<br />When `false`, the environment has its own dedicated load balancer, created, and managed by Elastic Beanstalk. When `true`, the environment uses a shared load balancer, created by you and specified in the `SharedLoadBalancer` option of the [aws:elbv2:loadbalancer](#command-options-general-elbv2) namespace. |  `false`  |  `true` <br /> `false`  | 

## aws:elasticbeanstalk:environment:process:default
<a name="command-options-general-environmentprocess"></a>

Configure your environment's default process.


**Namespace: `aws:elasticbeanstalk:environment:process:default`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| DeregistrationDelay | The amount of time, in seconds, to wait for active requests to complete before deregistering. | `20` | `0` to `3600` | 
| HealthCheckInterval | The interval of time, in seconds, that Elastic Load Balancing checks the health of the Amazon EC2 instances of your application. | With classic or application load balancer: `15`<br />With network load balancer: `30` | With classic or application load balancer: `5` to `300`<br />With network load balancer: `10`, `30` | 
| HealthCheckPath | The path that HTTP requests for health checks are sent to. | `/`  | A routable path. | 
| HealthCheckTimeout | The amount of time, in seconds, to wait for a response during a health check.<br />This option is only applicable to environments with an application load balancer. | `5` | `1` to `60` | 
| HealthyThresholdCount | The number of consecutive successful requests before Elastic Load Balancing changes the instance health status. | With classic or application load balancer: `3`<br />With network load balancer: `5` | `2` to `10` | 
| MatcherHTTPCode | A comma-separated list of HTTP code(s) that indicate that an instance is healthy.<br />This option is only applicable to environments with a network or application load balancer. | `200` | With application load balancer: `200` to `499`<br />With network load balancer: `200` to `399` | 
| Port | Port that the process listens on. | `80` | `1` to `65535` | 
| Protocol | The protocol that the process uses.<br />With an application load balancer, you can only set this option to `HTTP` or `HTTPS`.<br />With a network load balancer, you can only set this option to `TCP`. | With classic or application load balancer: `HTTP`<br />With network load balancer: `TCP` | `TCP`<br />`HTTP`<br />`HTTPS` | 
| StickinessEnabled | Set to true to enable sticky sessions.<br />This option is only applicable to environments with an application load balancer. | `'false'` | `'false'`<br />`'true'` | 
| StickinessLBCookieDuration | The lifetime, in seconds, of the sticky session cookie.<br />This option is only applicable to environments with an application load balancer. | `86400` (one day) | `1` to `604800` | 
| StickinessType | Set to `lb_cookie` to use cookies for sticky sessions.<br />This option is only applicable to environments with an application load balancer. | `lb_cookie` | `lb_cookie` | 
| UnhealthyThresholdCount | The number of consecutive unsuccessful requests before Elastic Load Balancing changes the instance health status. | `5` | `2` to `10` | 

## aws:elasticbeanstalk:environment:process:process\_name
<a name="command-options-general-environmentprocess-process"></a>

Configure additional processes for your environment.


**Namespace: `aws:elasticbeanstalk:environment:process:{{process_name}}`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| DeregistrationDelay | The amount of time, in seconds, to wait for active requests to complete before deregistering. | `20` | `0` to `3600` | 
| HealthCheckInterval | The interval, in seconds, that Elastic Load Balancing checks the health of Amazon EC2 instances for your application. | With classic or application load balancer: `15`<br />With network load balancer: `30` | With classic or application load balancer: `5` to `300`<br />With network load balancer: `10`, `30` | 
| HealthCheckPath | The path that HTTP requests for health checks are sent to. | `/`  | A routable path. | 
| HealthCheckTimeout | The amount of time, in seconds, to wait for a response during a health check.<br />This option is only applicable to environments with an application load balancer. | `5` | `1` to `60` | 
| HealthyThresholdCount | The number of consecutive successful requests before Elastic Load Balancing changes the instance health status. | With classic or application load balancer: `3`<br />With network load balancer: `5` | `2` to `10` | 
| MatcherHTTPCode | A comma-separated list of HTTP code(s) that indicates that an instance is healthy.<br />This option is only applicable to environments with a network or application load balancer. | `200` | With application load balancer: `200` to `499`<br />With network load balancer: `200` to `399` | 
| Port | The port that the process listens on. | `80` | `1` to `65535` | 
| Protocol | The protocol that the process uses.<br />With an application load balancer, you can only set this option to `HTTP` or `HTTPS`.<br />With a network load balancer, you can only set this option to `TCP`. | With classic or application load balancer: `HTTP`<br />With network load balancer: `TCP` | `TCP`<br />`HTTP`<br />`HTTPS` | 
| StickinessEnabled | Set to true to enable sticky sessions.<br />This option is only applicable to environments with an application load balancer. | `'false'` | `'false'`<br />`'true'` | 
| StickinessLBCookieDuration | The lifetime, in seconds, of the sticky session cookie.<br />This option is only applicable to environments with an application load balancer. | `86400` (one day) | `1` to `604800` | 
| StickinessType | Set to `lb_cookie` to use cookies for sticky sessions.<br />This option is only applicable to environments with an application load balancer. | `lb_cookie` | `lb_cookie` | 
| UnhealthyThresholdCount | The number of consecutive unsuccessful requests before Elastic Load Balancing changes the instance health status. | `5` | `2` to `10` | 

## aws:elasticbeanstalk:environment:proxy:staticfiles
<a name="command-options-general-environmentproxystaticfiles"></a>

You can use the following namespace to configure the proxy server to serve static files. When the proxy server receives a request for a file under the specified path, it serves the file directly instead of routing the request to your application. This reduces the number of requests that your application has to process.

Map a path served by the proxy server to a folder in your source code that contains static assets. Each option that you define in this namespace maps a different path.

**Note**  
This namespace applies to platform branches based on Amazon Linux 2 and later. If your environment uses a platform version based on Amazon Linux AMI (preceding Amazon Linux 2), refer to [Platform specific options](command-options-specific.md) for platform-specific static file namespaces.


**Namespace: `aws:elasticbeanstalk:environment:proxy:staticfiles`**  

| **Name**  | **Value**  | 
| --- | --- | 
| The path where the proxy server serves the files. Start the value with `/`.<br />For example, specify `/images` to serve files at `{{subdomain}}.eleasticbeanstalk.com/images`. | The name of the folder containing the files.<br />For example, specify `staticimages` to serve files from a folder named `staticimages` at the top level of your source bundle. | 

## aws:elasticbeanstalk:healthreporting:system
<a name="command-options-general-elasticbeanstalkhealthreporting"></a>

Configure enhanced health reporting for your environment.


**Namespace: `aws:elasticbeanstalk:healthreporting:system`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| SystemType | The health reporting system ([basic](using-features.healthstatus.md) or [enhanced](health-enhanced.md)). Enhanced health reporting requires a [service role](concepts-roles-service.md) and a version 2 or newer [platform version](concepts.platforms.md). If you use the Elastic Beanstalk console or EB CLI to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console and EB CLI override this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `basic`  | `basic` <br />`enhanced`  | 
| ConfigDocument | A JSON document that describes the environment and instance metrics to publish to CloudWatch. | None |  | 
| EnhancedHealthAuthEnabled | Enables authorization for the internal API that Elastic Beanstalk uses to communicate enhanced health information from your environment instances to the Elastic Beanstalk service.<br />For more information, see [Enhanced health roles](health-enhanced.md#health-enhanced-roles). This option is only applicable to enhanced health reporting (such as when `SystemType` is set to `enhanced`).  | `true`  | `true` <br />`false`  | 
| HealthCheckSuccessThreshold | Lowers the threshold for instances to pass health checks. If you use the Elastic Beanstalk console to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console overrides this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `Ok` | `Ok`<br />`Warning`<br />`Degraded`<br />`Severe` | 

## aws:elasticbeanstalk:hostmanager
<a name="command-options-general-elasticbeanstalkhostmanager"></a>

Configure the EC2 instances in your environment to upload rotated logs to Amazon S3.


**Namespace: `aws:elasticbeanstalk:hostmanager`**  

| **Name**  | **Description**  | **Default**  | Valid values | 
| --- | --- | --- | --- | 
| LogPublicationControl | Copy the log files of the Amazon EC2 instances for your application to the Amazon S3 bucket that's associated with your application. | `false`  | `true` <br />`false`  | 

## aws:elasticbeanstalk:managedactions
<a name="command-options-general-elasticbeanstalkmanagedactions"></a>

Configure managed platform updates for your environment.


**Namespace: `aws:elasticbeanstalk:managedactions`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| ManagedActionsEnabled | Enable [managed platform updates](environment-platform-update-managed.md#environment-platform-update-managed-namespace).<br />When you set this to `true`, you must also specify a `PreferredStartTime` and `UpdateLevel`. | `false`  | `true` <br />`false`  | 
| PreferredStartTime | Configure a maintenance window for managed actions in UTC.<br />For example, `"Tue:09:00"`. | None | Day and time in the<br /> {{day}}:{{hour}}:{{minute}}<br /> format. | 
| ServiceRoleForManagedUpdates | The name of an IAM role that Elastic Beanstalk uses to perform managed platform updates for your environment.<br />You can use either the same role that you specified for the `ServiceRole` option of the `aws:elasticbeanstalk:environment` namespace, or your account's [managed updates service-linked role](using-service-linked-roles-managedupdates.md). In the latter case, if the account doesn't have a managed-updates service-linked role yet, Elastic Beanstalk creates it. | None | Same as `ServiceRole`<br />or<br />`AWSServiceRoleForElasticBeanstalkManagedUpdates` | 

## aws:elasticbeanstalk:managedactions:platformupdate
<a name="command-options-general-elasticbeanstalkmanagedactionsplatformupdate"></a>

Configure managed platform updates for your environment.


**Namespace: `aws:elasticbeanstalk:managedactions:platformupdate`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| UpdateLevel | The highest level of update to apply with managed platform updates. Platforms are versioned {{major}}.{{minor}}.{{patch}}. For example, 2.0.8 has a major version of 2, a minor version of 0, and a patch version of 8. | None | `patch` for patch version updates only.<br />`minor` for both minor and patch version updates. | 
| InstanceRefreshEnabled | Enable weekly instance replacement.<br />This requires `ManagedActionsEnabled` to be set to `true`. | false | `true` <br />`false`  | 

## aws:elasticbeanstalk:monitoring
<a name="command-options-general-elasticbeanstalkmonitoring"></a>

Configure your environment to terminate EC2 instances that fail health checks.


**Namespace: `aws:elasticbeanstalk:monitoring`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| Automatically Terminate Unhealthy Instances | Terminate an instance if it fails health checks. This option was only supported on [legacy environments](using-features.migration.md). It determined the health of an instance based on being able to reach it and on other instance-based metrics. <br />Elastic Beanstalk doesn't provide a way to automatically terminate instances based on application health.  | `true`  | `true` <br />`false`  | 

## aws:elasticbeanstalk:sns:topics
<a name="command-options-general-elasticbeanstalksnstopics"></a>

Configure notifications for your environment.


**Namespace: `aws:elasticbeanstalk:sns:topics`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| Notification Endpoint | The endpoint where you want to be notified of important events affecting your application. If you use the Elastic Beanstalk console to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console overrides this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | None |  | 
| Notification Protocol | The protocol that's used to send notifications to your endpoint. | `email`  | `http` <br />`https` <br />`email` <br />`email-json` <br />`sqs`  | 
| Notification Topic ARN | The Amazon Resource Name (ARN) for the topic you subscribed to. | None |  | 
| Notification Topic Name | The name of the topic you subscribed to. | None |  | 

## aws:elasticbeanstalk:sqsd
<a name="command-options-general-elasticbeanstalksqsd"></a>

Configure the Amazon SQS queue for a worker environment.


**Namespace: `aws:elasticbeanstalk:sqsd`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| WorkerQueueURL | The URL of the queue that the daemon in the worker environment tier reads messages from. When you don't specify a value, the queue that Elastic Beanstalk automatically creates is a [standard](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html) Amazon SQS queue. When you provide a value, you can provide the URL of either a standard or a [FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html) Amazon SQS queue. Be aware that if you provide a FIFO queue, [periodic tasks](using-features-managing-env-tiers.md#worker-periodictasks) aren't supported.  | automatically generated | If you don't specify a value, then Elastic Beanstalk automatically creates a queue. | 
| HttpPath | The relative path to the application that HTTP POST messages are sent to. | / |   | 
| MimeType | The MIME type of the message that's sent in the HTTP POST request. | `application/json`  | `application/json` <br />`application/x-www-form-urlencoded` <br />`application/xml` <br />`text/plain` <br />Custom MIME type. | 
| HttpConnections | The maximum number of concurrent connections to any applications that are within an Amazon EC2 instance. If you use the Elastic Beanstalk console to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console overrides this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `50`  | `1` to `100` | 
| ConnectTimeout | The amount of time, in seconds, to wait for successful connections to an application. | `5`  | `1` to `60` | 
| InactivityTimeout | The amount of time, in seconds, to wait for a response on an existing connection to an application.The message is reprocessed until the daemon receives a 200 (OK) response from the application in the worker environment tier or the RetentionPeriod expires. | `299`  | `1` to `36000` | 
| VisibilityTimeout | The amount of time, in seconds, an incoming message from the Amazon SQS queue is locked for processing. After the configured amount of time has passed, then the message is again made visible in the queue for any other daemon to read. | 300 | `0` to `43200` | 
| ErrorVisibilityTimeout | The amount of time, in seconds, that elapses before Elastic Beanstalk returns a message to the Amazon SQS queue after a processing attempt fails with an explicit error. | `2` seconds | `0` to `43200` seconds | 
| RetentionPeriod | The amount of time, in seconds, a message is valid and is actively processed for. | `345600`  | `60` to `1209600` | 
| MaxRetries | The maximum number of attempts that Elastic Beanstalk attempts to send the message to the web application that will process it before moving the message to the dead-letter queue. |  `10`  | `1` to `100` | 

## aws:elasticbeanstalk:trafficsplitting
<a name="command-options-general-elasticbeanstalktrafficsplitting"></a>

Configure traffic-splitting deployments for your environment.

This namespace applies when you set the `DeploymentPolicy` option of the [aws:elasticbeanstalk:command](#command-options-general-elasticbeanstalkcommand) namespace to `TrafficSplitting`. For more information about deployment policies, see [Deployment policies and settings](using-features.rolling-version-deploy.md).


**Namespace: `aws:elasticbeanstalk:trafficsplitting`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| NewVersionPercent | The initial percentage of incoming client traffic that Elastic Beanstalk shifts to environment instances running the new application version you're deploying. |  `10`  | `1` to `100` | 
| EvaluationTime | The time period, in minutes, that Elastic Beanstalk waits after an initial healthy deployment before proceeding to shift all incoming client traffic to the new application version that you're deploying. |  `5`  | `3` to `600` | 

## aws:elasticbeanstalk:windows:activedirectory
<a name="command-options-general-elasticbeanstalkwindowsactivedirectory"></a>

Configure the Windows Server instances in your environment to join an AWS Directory Service directory at launch. For more information, see [Joining instances to an Active Directory domain](dotnet-activedirectory.md).

This namespace applies only to Windows Server platform versions released on or after [August 18, 2026](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-08-18-windows.html). Earlier platform versions reject these options during validation.


**Namespace: `aws:elasticbeanstalk:windows:activedirectory`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| DirectoryId | The ID of the AWS Directory Service directory that the environment's instances join at launch. Setting this option turns on Active Directory domain join. `DirectoryName` is required when this option is set. | None | `d-` followed by 10 hexadecimal characters (for example, `d-1234567890`) | 
| DirectoryName | The fully qualified DNS name of the directory. Required when `DirectoryId` is set. | None | A fully qualified domain name (for example, `corp.example.com`) | 
| DirectoryOU | The distinguished name of the organizational unit (OU) that instances create their computer objects in. The OU must already exist in the directory. If you don't set this option, computer objects are created in the directory's default container. `DirectoryId` is required when this option is set. | None | An LDAP distinguished name (for example, `OU=WebServers,DC=corp,DC=example,DC=com`) | 

## aws:elasticbeanstalk:xray
<a name="command-options-general-elasticbeanstalkxray"></a>

Run the AWS X-Ray daemon to relay trace information from your [X-Ray integrated](environment-configuration-debugging.md) application.


**Namespace: `aws:elasticbeanstalk:xray`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| `XRayEnabled` | Set to `true` to run the X-Ray daemon on the instances in your environment. | `false` | `true`<br />`false` | 

## aws:elb:healthcheck
<a name="command-options-general-elbhealthcheck"></a>

Configure healthchecks for a Classic Load Balancer.


**Namespace: `aws:elb:healthcheck`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| HealthyThreshold | The number of consecutive successful requests before Elastic Load Balancing changes the instance health status. | `3`  | `2` to `10` | 
| Interval | The interval that Elastic Load Balancing checks the health of your application's Amazon EC2 instances at. | `10`  | `5` to `300` | 
| Timeout | The amount of time, in seconds, that Elastic Load Balancing waits for a response before it considers the instance nonresponsive. | `5`  | `2` to `60` | 
| UnhealthyThreshold | The number of consecutive unsuccessful requests before Elastic Load Balancing changes the instance health status. | `5`  | `2` to `10` | 
| (deprecated) Target | The destination on a backend instance that health checks are sent to. Use `Application Healthcheck URL` in the [`aws:elasticbeanstalk:application`](#command-options-general-elasticbeanstalkapplication) namespace instead. | `TCP:80`  | Target in the format {{PROTOCOL}}:{{PORT}}{{/PATH}} | 

## aws:elb:loadbalancer
<a name="command-options-general-elbloadbalancer"></a>

Configure your environment's Classic Load Balancer.

Several of the options in this namespace are no longer supported in favor of listener-specific options in the [aws:elb:listener](#command-options-general-elblistener) namespace. With these options that aren't supported anymore, you can only configure two listeners (one secure and one unsecure) on standard ports.


**Namespace: `aws:elb:loadbalancer`**  

| Name | Description | Default | Valid values | 
| --- | --- | --- | --- | 
| CrossZone | Configure the load balancer to route traffic evenly across all instances in all Availability Zones rather than only within each zone. If you use the Elastic Beanstalk console or EB CLI to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console and EB CLI override this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `false`  | `true` <br />`false`  | 
| SecurityGroups | Assign one or more security groups that you created to the load balancer.<br />Required if `DisableDefaultEC2SecurityGroup` ([aws:autoscaling:launchconfiguration](#command-options-general-autoscalinglaunchconfiguration)) is set to `true`. Load balanced environments that have opted out of the default Elastic Beanstalk EC2 security group must provide one or more security groups with this option. For more information, see [Managing EC2 security groups](using-features.managing.ec2.instances.sg.md). | None | One or more security group IDs. | 
| ManagedSecurityGroup | Assign an existing security group to the load balancer for your environment, instead of creating a new one. To use this setting, update the `SecurityGroups` setting in this namespace to include your security group’s ID, and remove the ID of the security group that was created automatically, if one was created.<br />To allow traffic from the load balancer to your environment’s EC2 instances, Elastic Beanstalk adds a rule to the security group of the instances that allows inbound traffic from the managed security group. | None | A security group ID. | 
| (deprecated) LoadBalancerHTTPPort | The port to listen on for the unsecure listener.  | `80`  | `OFF` <br />`80`  | 
| (deprecated) LoadBalancerPortProtocol | The protocol to use on the unsecure listener. | `HTTP`  | `HTTP` <br />`TCP`  | 
| (deprecated) LoadBalancerHTTPSPort | The port to listen on for the secure listener. | `OFF`  | `OFF` <br />`443` <br />`8443`  | 
| (deprecated) LoadBalancerSSLPortProtocol | The protocol to use on the secure listener. | `HTTPS`  | `HTTPS` <br />`SSL`  | 
| (deprecated) SSLCertificateId | The Amazon Resource Name (ARN) of an SSL certificate to bind to the secure listener. | None |  | 

## aws:elb:listener
<a name="command-options-general-elblistener"></a>

Configure the default listener (port 80) on a Classic Load Balancer.


**Namespace: `aws:elb:listener`**  

| Name | Description | Default | Valid values | 
| --- | --- | --- | --- | 
| ListenerProtocol | The protocol used by the listener. | HTTP  | HTTP TCP  | 
| InstancePort | The port that this listener uses to communicate with the EC2 instances. | 80 | 1 to 65535 | 
| InstanceProtocol | The protocol that this listener uses to communicate with the EC2 instances.<br />It must be at the same internet protocol layer as the `ListenerProtocol`. It also must have the same security level as any other listener using the same `InstancePort` as this listener.<br />For example, if `ListenerProtocol` is `HTTPS` (application layer, using a secure connection), you can set `InstanceProtocol` to `HTTP` (also at the application layer, using an insecure connection). If, in addition, you set `InstancePort` to `80`, you must set `InstanceProtocol` to `HTTP` in all other listeners with `InstancePort` set to `80`. | `HTTP` when `ListenerProtocol` is `HTTP`<br />`TCP` when `ListenerProtocol` is `TCP` | HTTP or HTTPS when ListenerProtocol is HTTP or HTTPS`TCP` or `SSL` when `ListenerProtocol` is `TCP` or `SSL` | 
| PolicyNames | A comma-separated list of policy names to apply to the port for this listener. We recommend that you use the LoadBalancerPorts option of the [aws:elb:policies](#command-options-general-elbpolicies) namespace instead. | None |  | 
| ListenerEnabled | Specifies whether this listener is enabled. If you specify false, the listener isn't included in the load balancer.  | true | `true`<br />`false` | 

## aws:elb:listener:listener\_port
<a name="command-options-general-elblistener-listener"></a>

Configure additional listeners on a Classic Load Balancer.


**Namespace: `aws:elb:listener:{{listener_port}}`**  

| Name | Description | Default | Valid values | 
| --- | --- | --- | --- | 
| ListenerProtocol | The protocol used by the listener. |  HTTP  |  HTTP HTTPS TCP SSL  | 
| InstancePort | The port that this listener uses to communicate with the EC2 instances. | The same as {{listener\_port}}. | 1 to 65535 | 
| InstanceProtocol | The protocol that this listener uses to communicate with the EC2 instances.<br />It must be at the same internet protocol layer as the `ListenerProtocol`. It also must have the same security level as any other listener using the same `InstancePort` as this listener.<br />For example, if `ListenerProtocol` is `HTTPS` (application layer, using a secure connection), you can set `InstanceProtocol` to `HTTP` (also at the application layer, using an insecure connection). If, in addition, you set `InstancePort` to `80`, you must set `InstanceProtocol` to `HTTP` in all other listeners with `InstancePort` set to `80`. | `HTTP` when `ListenerProtocol` is `HTTP` or `HTTPS`<br />`TCP` when `ListenerProtocol` is `TCP` or `SSL` | HTTP or HTTPS when ListenerProtocol is HTTP or HTTPS`TCP` or `SSL` when `ListenerProtocol` is `TCP` or `SSL` | 
| PolicyNames | A comma-separated list of policy names to apply to the port for this listener. We suggest that you use the LoadBalancerPorts option of the [aws:elb:policies](#command-options-general-elbpolicies) namespace instead. | None |  | 
| SSLCertificateId | The Amazon Resource Name (ARN) of an SSL certificate to bind to the listener. | None |  | 
| ListenerEnabled | Specifies whether this listener is enabled. If you specify false, the listener isn't included in the load balancer.  | true if any other option is set. false otherwise. |  true false  | 

## aws:elb:policies
<a name="command-options-general-elbpolicies"></a>

Modify the default stickiness and global load balancer policies for a Classic Load Balancer.


**Namespace: `aws:elb:policies`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| ConnectionDrainingEnabled | Specifies whether the load balancer maintains existing connections to instances that have become unhealthy or deregistered to complete in-progress requests. If you use the Elastic Beanstalk console or EB CLI to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console and EB CLI override this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `false`  | `true` <br />`false`  | 
| ConnectionDrainingTimeout | The maximum number of seconds that the load balancer maintains existing connections to an instance during connection draining before forcibly closing the connections. If you use the Elastic Beanstalk console to create an environment, you can't set this option in a [configuration file](ebextensions.md). The console overrides this option with a [recommended value](command-options.md#configuration-options-recommendedvalues).  | `20`  | `1` to `3600` | 
| ConnectionSettingIdleTimeout | The amount of time, in seconds, that the load balancer waits for any data to be sent or received over the connection. If no data has been sent or received after this time period elapses, the load balancer closes the connection. | `60`  | `1` to `3600` | 
| LoadBalancerPorts | A comma-separated list of the listener ports that the default policy (`AWSEB-ELB-StickinessPolicy`) applies to. | None | You can use :all to indicate all listener ports | 
| Stickiness Cookie Expiration | The amount of time, in seconds, that each cookie is valid. Uses the default policy (`AWSEB-ELB-StickinessPolicy`) . |  `0`  | `0` to `1000000` | 
| Stickiness Policy | Binds a user's session to a specific server instance so that all requests coming from the user during the session are sent to the same server instance. Uses the default policy (`AWSEB-ELB-StickinessPolicy`) . |  `false`  |  true false  | 

## aws:elb:policies:policy\_name
<a name="command-options-general-elbpolicies-custom"></a>

Create additional load balancer policies for a Classic Load Balancer.


**Namespace: `aws:elb:policies:{{policy_name}}`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| CookieName | The name of the application-generated cookie that controls the session lifetimes of a AppCookieStickinessPolicyType policy. This policy can be associated only with HTTP/HTTPS listeners.  | None |  | 
| InstancePorts | A comma-separated list of the instance ports that this policy applies to. | None | A list of ports, or :all | 
| LoadBalancerPorts | A comma-separated list of the listener ports that this policy applies to. | None | A list of ports, or :all | 
| ProxyProtocol | For a `ProxyProtocolPolicyType` policy, specifies whether to include the IP address and port of the originating request for TCP messages. This policy can be associated only with TCP/SSL listeners. | None | true false  | 
| PublicKey | The contents of a public key for a `PublicKeyPolicyType` policy to use when authenticating the backend server or servers. This policy can't be applied directly to backend servers or listeners. It must be part of a `BackendServerAuthenticationPolicyType` policy. | None |  | 
| PublicKeyPolicyNames | A comma-separated list of policy names (from the `PublicKeyPolicyType` policies) for a `BackendServerAuthenticationPolicyType` policy that controls authentication to a backend server or servers. This policy can be associated only with backend servers that are using HTTPS/SSL. | None |  | 
| SSLProtocols | A comma-separated list of SSL protocols to be enabled for a `SSLNegotiationPolicyType` policy that defines the ciphers and protocols that are accepted by the load balancer. This policy can be associated only with HTTPS/SSL listeners. | None |  | 
| SSLReferencePolicy | The name of a predefined security policy that adheres to AWS security best practices and that you want to activate for a `SSLNegotiationPolicyType` policy that defines the ciphers and protocols that are accepted by the load balancer. This policy can be associated only with HTTPS/SSL listeners. | None |  | 
| Stickiness Cookie Expiration | The amount of time, in seconds, that each cookie is valid. | `0`  | `0` to `1000000` | 
| Stickiness Policy | Binds a user's session to a specific server instance so that all requests coming from the user during the session are sent to the same server instance. | `false`  | true false  | 

## aws:elbv2:listener:default
<a name="command-options-general-elbv2-listener-default"></a>

Configure the default listener (port 80) on an Application Load Balancer or a Network Load Balancer.

This namespace doesn't apply to an environment that uses a shared load balancer. Shared load balancers don't have a default listener.


**Namespace: `aws:elbv2:listener:default`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| DefaultProcess | The name of the [process](#command-options-general-environmentprocess) to forward traffic to when no rules match. | `default` | A process name. | 
| ListenerEnabled | Set to `false` to disable the listener. You can use this option to disable the default listener on port 80. | `true` | `true`<br />`false` | 
| Protocol | The protocol of traffic to process. | With application load balancer: `HTTP`<br />With network load balancer: `TCP` | With application load balancer: `HTTP`, `HTTPS`<br />With network load balancer: `TCP`, `TLS` | 
| Rules | A list of [rules](#command-options-general-elbv2-listenerrule) to apply to the listener<br />This option is only applicable to environments with an Application Load Balancer. | None | A comma-separated list of rule names. | 
| SSLCertificateArns | The Amazon Resource Name (ARN) of the SSL certificate to bind to the listener.<br />This option is only applicable to environments with an Application Load Balancer or Network Load Balancer. | None | The ARN of a certificate stored in IAM or ACM. | 
| SSLPolicy | Specify a security policy to apply to the listener.<br />This option is only applicable to environments with an Application Load Balancer or Network Load Balancer. | None (ELB default) | The name of a load balancer security policy. | 

## aws:elbv2:listener:listener\_port
<a name="command-options-general-elbv2-listener"></a>

Configure additional listeners on an Application Load Balancer or a Network Load Balancer.

**Note**  
For a shared Application Load Balancer, you can specify only the `Rule` option. The other options aren't applicable to shared load balancers.


**Namespace: `aws:elbv2:listener:{{listener_port}}`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| DefaultProcess | The name of the [process](#command-options-general-environmentprocess) where traffic is forwarded when no rules match. | `default` | A process name. | 
| ListenerEnabled | Set to `false` to disable the listener. You can use this option to disable the default listener on port 80. | `true` | `true`<br />`false` | 
| Protocol | The protocol of traffic to process. | With application load balancer: `HTTP`<br />With network load balancer: `TCP` | With application load balancer: `HTTP`, `HTTPS`<br />With network load balancer: `TCP`, `TLS` | 
| Rules | List of [rules](#command-options-general-elbv2-listenerrule) to apply to the listener<br />This option is applicable only to environments with an Application Load Balancer.<br />If your environment uses a shared Application Load Balancer, and you don't specify this option for any listener, Elastic Beanstalk automatically associates the `default` rule with a port 80 listener. | None | A comma-separated list of rule names. | 
| SSLCertificateArns | The Amazon Resource Name (ARN) of the SSL certificate to bind to the listener.<br />This option is only applicable to environments with an Application Load Balancer or Network Load Balancer. | None | The ARN of a certificate stored in IAM or ACM. | 
| SSLPolicy | Specify a security policy to apply to the listener.<br />This option is only applicable to environments with an Application Load Balancer or Network Load Balancer. | None (ELB default) | The name of a load balancer security policy. | 

## aws:elbv2:listenerrule:rule\_name
<a name="command-options-general-elbv2-listenerrule"></a>

Define listener rules for an Application Load Balancer. If a request matches the host names or paths in a rule, the load balancer forwards it to the specified process. To use a rule, add it to a listener with the `Rules` option in the [`aws:elbv2:listener:{{listener_port}}`](#command-options-general-elbv2-listener) namespace.

**Note**  
This namespace isn't applicable to environments with a network load balancer.


**Namespace: `aws:elbv2:listenerrule:{{rule_name}}`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| HostHeaders | A list of host names to match. For example, `my.example.com`. | Dedicated load balancer: None<br />Shared load balancer: The environment's CNAME | Each name can contain up to 128 characters. A pattern can include both uppercase and lowercase letters, numbers, hyphens (–), and up to three wildcard characters (`*` matches zero or more characters; `?` matches exactly one character). You can list more than one name, each separated by a comma. Application Load Balancer supports up to five combined `HostHeader` and `PathPattern` rules.<br />For more information, see [Host conditions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#host-conditions) in the *User Guide for Application Load Balancers*. | 
| PathPatterns | The path patterns to match (for example, `/img/*`).<br />This option is only applicable to environments with an application load balancer. | None | Each pattern can contain up to 128 characters. A pattern can include uppercase and lowercase letters, numbers, hyphens (–), and up to three wildcard characters (`*` matches zero or more characters; `?` matches exactly one character). You can add multiple comma-separated path patterns. Application Load Balancer supports up to five combined `HostHeader` and `PathPattern` rules.<br />For more information, see [Path conditions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#path-conditions) in the *User Guide for Application Load Balancers*. | 
| Priority | The precedence of this rule when multiple rules match. The lower number takes precedence. No two rules can have the same priority.<br />With a shared load balancer, Elastic Beanstalk treats rule priorities as relative across sharing environments, and maps them to absolute priorities during creation. | `1` | `1` to `1000` | 
| Process | The name of the [process](#command-options-general-environmentprocess) to forward traffic when this rule matches the request. | `default` | A process name. | 

## aws:elbv2:loadbalancer
<a name="command-options-general-elbv2"></a>

Configure an Application Load Balancer.

For a shared load balancer, only the `SharedLoadBalancer` and `SecurityGroups` options are valid.

**Note**  
This namespace isn't applicable to environments with a Network Load Balancer.


**Namespace: `aws:elbv2:loadbalancer`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| AccessLogsS3Bucket | The Amazon S3 bucket where access logs are stored. The bucket must be in the same Region as the environment and allow the load balancer write access. | None | A bucket name. | 
| AccessLogsS3Enabled | Enable access log storage. | `false` | `true`<br />`false` | 
| AccessLogsS3Prefix | A prefix to prepend to access log names. By default, the load balancer uploads logs to a directory named AWSLogs in the bucket you specify. Specify a prefix to place the AWSLogs directory inside another directory. | None |  | 
| IdleTimeout | The amount of time, in seconds, to wait for a request to complete before closing connections to client and instance. | None | `1` to `3600` | 
| IpAddressType | Specifies the IP address format configuration for the environment's load balancer. Use the *dualstack* option to enable IPv6 protocol, along with IPv4 protocol.<br />Only Application Load Balancers and Network Load Balancers support the *dualstack* option. Single instance environments and environments that use Classic Load Balancers do not support it.<br />You must associate the environment's VPC and all of the VPC subnets with IPv6 CIDR blocks to support the *dualstack* option.<br />For more information, see [Configuring dual-stack Elastic Beanstalk load balancers](environments-cfg-elbv2-ipv6-dualstack.md). | ipv4 | ipv4, dualstack | 
| ManagedSecurityGroup | Assign an existing security group to your environment’s load balancer, instead of creating a new one. To use this setting, update the `SecurityGroups` setting in this namespace to include your security group’s ID, and remove the automatically created security group’s ID, if one exists.<br />To allow traffic from the load balancer to the EC2 instances for your environment, Elastic Beanstalk adds a rule to the security group of your instances that allows inbound traffic from the managed security group. | The security group that Elastic Beanstalks creates for your load balancer. | A security group ID. | 
| SecurityGroups | A list of security groups to attach to the load balancer.<br />Required if `DisableDefaultEC2SecurityGroup` ([aws:autoscaling:launchconfiguration](#command-options-general-autoscalinglaunchconfiguration)) is set to `true`. Load balanced environments that have opted out of the default Elastic Beanstalk EC2 security group must provide one or more security groups with this option. For more information, see [Managing EC2 security groups](using-features.managing.ec2.instances.sg.md).<br />For a shared load balancer, if you don't specify this value, Elastic Beanstalk checks if an existing security group that it manages is already attached to the load balancer. If one isn't attached to the load balancer, Elastic Beanstalk creates a security group and attaches it to the load balancer. Elastic Beanstalk deletes this security group when the last environment sharing the load balancer terminates.<br />The load balancer security groups are used to set up the Amazon EC2 instance security group ingress rule. | The security group that Elastic Beanstalk creates for your load balancer. | Comma-separated list of security group IDs. | 
| SharedLoadBalancer | The Amazon Resource Name (ARN) of a shared load balancer. This option is relevant only to an Application Load Balancer. It's required when the `LoadBalancerIsShared` option of the [aws:elasticbeanstalk:environment](#command-options-general-elasticbeanstalkenvironment) namespace is set to `true`. You can't change the shared load balancer ARN after the environment is created.<br />Criteria for a valid value:+  It must be a valid, active load balancer in the AWS Region where the environment is located. <br />+  It must be in the same Amazon Virtual Private Cloud (Amazon VPC) as the environment. <br />+  It can't be a load balancer that was created by Elastic Beanstalk as the dedicated load balancer for another environment. You can identify these dedicated load balancers by using the prefix `awseb-`. <br />Example:<br />`arn:aws:elasticloadbalancing:us-east-2:123456789012:loadbalancer/app/FrontEndLB/0dbf78d8ad96abbc` | None | ARN of a valid load balancer that meets all of the criteria described here. | 

## aws:rds:dbinstance
<a name="command-options-general-rdsdbinstance"></a>

Configure an attached Amazon RDS DB instance.


**Namespace: `aws:rds:dbinstance`**  

| **Name**  | **Description**  | **Default**  | **Valid values**  | 
| --- | --- | --- | --- | 
| DBAllocatedStorage | The allocated database storage size, specified in gigabytes. | MySQL: `5`<br />Oracle: `10`<br />sqlserver-se: `200`<br />sqlserver-ex: `30`<br />sqlserver-web: `30` | MySQL: `5`-`1024`<br />Oracle: `10`-`1024`<br />sqlserver: cannot be modified | 
| DBDeletionPolicy | Specifies whether to retain, delete, or create snapshot of the DB instance when an environment is terminated.<br />This option works in conjunction with `HasCoupledDatabase`, also an option of this namespace. Deleting a DB instance results in permanent data loss.  | `Delete`  | `Delete` <br />`Retain` <br />`Snapshot`  | 
| DBEngine | The name of the database engine to use for this instance. | `mysql`  | `mysql` <br />`oracle-se1` <br />`sqlserver-ex` <br />`sqlserver-web` <br />`sqlserver-se` <br />`postgres`  | 
| DBEngineVersion | The version number of the database engine. | `5.5`  |  | 
| DBInstanceClass | The database instance type. | `db.t2.micro` <br />(`db.m1.large` for an environment not running in an Amazon VPC)  | For more information, see [DB Instance Class](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the * Amazon Relational Database Service User Guide*. | 
| DBPassword | The name of master user password for the database instance. | None |  | 
| DBSnapshotIdentifier | The identifier for the DB snapshot to restore from. | None |  | 
| DBUser | The name of master user for the DB Instance. | **ebroot**  |  | 
| HasCoupledDatabase | Specifies whether a DB instance is coupled to your environment. If toggled to `true`, Elastic Beanstalk creates a new DB instance coupled to your environment. If toggled to `false`, Elastic Beanstalk initiates decoupling of the DB instance from your environment.<br />This option works in conjunction with `DBDeletionPolicy`, also an option of this namespace. Note: If you toggle this value back to `true` after decoupling the previous database, Elastic Beanstalk creates a new database with the previous database option settings. However, to maintain the security of your environment, it doesn't retain the existing `DBUser` and `DBPassword` settings. You need to specify `DBUser` and `DBPassword` again.  | `false`  | `true` <br />`false`  | 
| MultiAZDatabase | Specifies whether a database instance Multi-AZ deployment needs to be created. For more information about Multi-AZ deployments with Amazon Relational Database Service (RDS), see [Regions and Availability Zones](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html) in the * Amazon Relational Database Service User Guide*. | `false`  | `true` <br />`false`  | 