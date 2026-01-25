# Configuring Amazon EC2 instances with namespace options

You can use the [configuration options](command-options.md "command-options.md") in the `aws:autoscaling:launchconfiguration` namespace to configure the
instances for your environment, including additional options that aren't available in the console.

###### Important

The `DisableIMDSv1`, `RootVolumeType`, or `BlockDeviceMappings`
option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch
templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom
policies instead of our managed policies, environment creation or updates might fail when you update your environment
configuration. For more information
and other considerations, see [Migrating your Elastic Beanstalk
environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md") .

The following [configuration file](ebextensions.md "ebextensions.md") example uses the
basic configuration options that are explained in this topic. To see examples of additional
configuration options when you need to specify security groups for load balancers, see [Configuring with the
AWS CLI](using-features.managing.ec2.md "using-features.managing.ec2.md").

```
option_settings:
  aws:autoscaling:launchconfiguration:
    SecurityGroups: my-securitygroup
    MonitoringInterval: "1 minute"
    DisableIMDSv1: false
    DisableDefaultEC2SecurityGroup: true
    SecurityGroups: "sg-abcdef01, sg-abcdef02"
    EC2KeyName: my-keypair
    IamInstanceProfile: "aws-elasticbeanstalk-ec2-role"
    BlockDeviceMappings: "/dev/sdj=:100,/dev/sdh=snap-51eef269,/dev/sdb=ephemeral0"
  aws:elasticbeanstalk:environment:
    EnvironmentType: SingleInstance
```

The `DisableDefaultEC2SecurityGroup` and `BlockDeviceMappings` are not
available in the console.

You can use `BlockDeviceMappings` to configure additional block devices for
your instances. For more information, see [Block Device Mapping](../../../AWSEC2/latest/UserGuide/block-device-mapping-concepts.md "../../../AWSEC2/latest/UserGuide/block-device-mapping-concepts.md") in the
_Amazon EC2 User Guide_.

The EB CLI and Elastic Beanstalk console apply recommended values for the preceding options.
You must remove these settings if you want to use configuration files to configure the same. See
[Recommended values](command-options.md#configuration-options-recommendedvalues "command-options.md#configuration-options-recommendedvalues") for details.
