# Configuring Amazon EC2 security groups and instance types using the

AWS CLI

You can use the AWS Command Line Interface (AWS CLI) to configure the Amazon EC2 instances in
your Elastic Beanstalk environments.

## Configuring EC2 security groups using the AWS CLI

This topic provides examples for different EC2 security group configurations for both
single-instance and load balanced (multi-instance) environments. For more information about the
options in these examples, see [aws:autoscaling:launchconfiguration](command-options-general.md#command-options-general-autoscalinglaunchconfiguration "command-options-general.md#command-options-general-autoscalinglaunchconfiguration").

###### Notes

The create environment operation provides an EC2 security group by default. It also creates an environment with an application load balancer by default.

The update environment operation can be used to either disable or enable the default EC2
security group for your environment with the boolean option
`DisableDefaultEC2SecurityGroup`. _Example
5_ shows how to set your environment back to the default security configuration
if you had previously modified it.

The following examples show a [create-environment](../../../cli/latest/reference/elasticbeanstalk/create-environment.md "../../../cli/latest/reference/elasticbeanstalk/create-environment.md")
command opting out of the default EC2 security group and providing custom security groups
instead. Since the `DisableDefaultEC2SecurityGroup` option is set to
`true`, the default EC2 security group that Elastic Beanstalk normally associates to the EC2
instances is not created. Therefore, you must provide other security groups with the
`SecurityGroups` option.

Note that the [aws:elasticbeanstalk:environment](command-options-general.md#command-options-general-elasticbeanstalkenvironment "command-options-general.md#command-options-general-elasticbeanstalkenvironment")
`EnvironmentType` option is set to `SingleInstance`. To create a single
instance environment, you must specify this option, because `LoadBalanced` is the
default `EnvironmentType`. Since this environment does not include a load balancer,
we don't need to specify a load balancer security group.

###### Example 1 — New single-instance environment with custom EC2 security groups (namespace

options inline)

```
aws elasticbeanstalk create-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2023 v6.5.0 applrunning Node.js 22"` \
--option-settings \
Namespace=aws:elasticbeanstalk:environment,OptionName=EnvironmentType,Value=`SingleInstance` \
Namespace=aws:autoscaling:launchconfiguration,OptionName=IamInstanceProfile,Value=`aws-elasticbeanstalk-ec2-role` \
Namespace=aws:autoscaling:launchconfiguration,OptionName=DisableDefaultEC2SecurityGroup,Value=`true` \
Namespace=aws:autoscaling:launchconfiguration,OptionName=SecurityGroups,Value=`sg-abcdef01, sg-abcdef02` \
Namespace=aws:autoscaling:launchconfiguration,OptionName=EC2KeyName,Value=`my-keypair`
```

As an alternative, use an `options.json` file to specify the namespace
options instead of including them inline.

###### Example 2 — New single-instance environment with custom EC2 security groups (namespace

options in `options.json` file)

```
aws elasticbeanstalk create-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2023 v6.5.0 running Node.js 22"` \
--option-settings `file://options.json`
```

```
### example options.json ###
[
  { "Namespace" : "aws:elasticbeanstalk:environment",
    "OptionName" : "EnvironmentType",
    "Value" : "SingleInstance"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "IamInstanceProfile",
    "Value": "aws-elasticbeanstalk-ec2-role"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "DisableDefaultEC2SecurityGroup",
    "Value": "true"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "SecurityGroups",
    "Value": "sg-abcdef01, sg-abcdef02"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "EC2KeyName",
    "Value": "my-keypair"
  }
]
```

The following example creates a load-balanced environment. It specifies the [aws:elasticbeanstalk:environment](command-options-general.md#command-options-general-elasticbeanstalkenvironment "command-options-general.md#command-options-general-elasticbeanstalkenvironment") namespace option
`LoadBalancerType` set to `application`. Since we're disabling the
default EC2 security group with the `DisableDefaultEC2SecurityGroup` option, we need
to provide our own custom security groups for the EC2 instances again, with the [aws:autoscaling:launchconfiguration](command-options-general.md#command-options-general-autoscalinglaunchconfiguration "command-options-general.md#command-options-general-autoscalinglaunchconfiguration")
`SecurityGroups` option, like the previous example. Since this environment has a load
balancer to route traffic, we must provide security groups for the load balancer as well.

To create an environment with a with a classic load balancer, but otherwise the same
configuration, update the configuration for the [aws:elasticbeanstalk:environment](command-options-general.md#command-options-general-elasticbeanstalkenvironment "command-options-general.md#command-options-general-elasticbeanstalkenvironment") namespace option
`LoadBalancerType` to `classic`.

The different load balancer types have different namespaces that hold the options to specify
the security groups:

- application load balancer – [aws:elbv2:loadbalancer](command-options-general.md#command-options-general-elbv2 "command-options-general.md#command-options-general-elbv2")
  `SecurityGroups` option
- classic load balancer – [aws:elb:loadbalancer](command-options-general.md#command-options-general-elbloadbalancer "command-options-general.md#command-options-general-elbloadbalancer")
  `SecurityGroups` option
- network load balancer – since network load balancers do not have security groups,
  configure the EC2 security groups with VPC identifiers. For more information, see [Update the
  security groups for your Network Load Balancer](../../../elasticloadbalancing/latest/network/load-balancer-security-groups.md "../../../elasticloadbalancing/latest/network/load-balancer-security-groups.md") in the
  _User Guide for Network Load Balancers_.

###### Example 3 — New multi-instance environment with custom EC2 security groups (namespace

options in `options.json` file)

```
aws elasticbeanstalk create-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2023 v6.5.0 running Node.js 22"` \
--option-settings `file://options.json`
```

```
### example options.json ###
[
  {
    "Namespace" : "aws:elasticbeanstalk:environment",
    "OptionName" : "EnvironmentType",
    "Value" : "LoadBalanced"
  },
  {
  "Namespace" : "aws:elasticbeanstalk:environment",
    "OptionName" : "LoadBalancerType",
    "Value" : "application"
  },
  {
    "Namespace" : "aws:elbv2:loadbalancer",
    "OptionName" : "SecurityGroups",
    "Value" : "sg-abcdefghikl012345"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "IamInstanceProfile",
    "Value": "aws-elasticbeanstalk-ec2-role"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "DisableDefaultEC2SecurityGroup",
    "Value": "true"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "SecurityGroups",
    "Value": "sg-abcdef01, sg-abcdef02"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "EC2KeyName",
    "Value": "my-keypair"
  }
]
```

You can disable the default EC2 security group for an existing environment with the [update-environment](../../../cli/latest/reference/elasticbeanstalk/update-environment.md "../../../cli/latest/reference/elasticbeanstalk/update-environment.md") command. The following example command disables the default EC2
security group and assigns the environment's EC2 instances custom EC2 security groups.

Use the example `options.jason` files in examples 4(a), 4(b), or 4(c),
depending on whether the environment is load balanced and the type of load balancer.
Configuration file 4(a) specifies the security groups for a single-instance environment. Since
it doesn't require a load balancer, we only provide the security group for the EC2 instances.
Configuration files 4(b) and 4(c) specify the security groups for an application load balancer
and a classic load balancer. For these cases we also need to specify security groups for the
load balancer.

###### Example 4 — Update an existing environment to disable default EC2 security group (namespace options in

`options.json` file)

```
aws elasticbeanstalk update-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2023 v6.5.0 running Node.js 22"` \
--option-settings `file://options.json`
```

###### Example 4(a) — Configuration file for single-instance environment (no load

balancer)

```
### example options.json ###
[
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "DisableDefaultEC2SecurityGroup",
    "Value": "true"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "SecurityGroups",
    "Value": "sg-abcdef01, sg-abcdef02"
  }
]
```

To update an environment that uses an application load balancer, use the
`aws:elbv2:loadbalancer` namespace to specify the security groups for the
load balancer.

###### Example 4(b) — Configuration file for environment with an application load

balancer

```
### example options.json ###
[
  {
    "Namespace" : "aws:elbv2:loadbalancer",
    "OptionName" : "SecurityGroups",
    "Value" : "sg-abcdefghikl012345"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "DisableDefaultEC2SecurityGroup",
    "Value": "true"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "SecurityGroups",
    "Value": "sg-abcdef01, sg-abcdef02"
  }
]
```

To update an environment that uses a classic load balancer use the
`aws:elb:loadbalancer` namespace to specify the security groups for the
load balancer.

###### Example 4(c) — Configuration file for environment with a classic load balancer

```
### example options.json ###
[
  {
    "Namespace" : "aws:elb:loadbalancer",
    "OptionName" : "SecurityGroups",
    "Value" : "sg-abcdefghikl012345"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "DisableDefaultEC2SecurityGroup",
    "Value": "true"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",n
    "OptionName": "SecurityGroups",
    "Value": "sg-abcdef01, sg-abcdef02"
  }
]
```

To return your environment to the default behavior and configuration with the default security
group that Elastic Beanstalk assigns, use the [update-environment](../../../cli/latest/reference/elasticbeanstalk/update-environment.md "../../../cli/latest/reference/elasticbeanstalk/update-environment.md") command to set the `DisableDefaultEC2SecurityGroup`
to `false`. For a multi-instance environment, Elastic Beanstalk also handles the
security groups and network traffic rules for your environment's load balancer.

The following example applies to both a single-instance or multi-instance (load balanced) environment:

###### Example 5 — Update an environment back to using the default security group (namespace

options in `options.json` file)

```
aws elasticbeanstalk update-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2023 v6.5.0 running Node.js 22"` \
--option-settings `file://options.json`
```

```
### example options.json ###
[
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "DisableDefaultEC2SecurityGroup",
    "Value": "false"
  }
]
```

## Configuring EC2 with instance types using the AWS CLI

This topic provides examples for configuring the instance types of the EC2 instances in
your environment.

The first two examples creates a new environment. The command specifies an Amazon EC2 instances
type, t4g.small, that's based on arm64 processor architecture. Elastic Beanstalk defaults the Image ID
(AMI) for the EC2 instances based on the Region, platform version and instance type. The
instance type corresponds to a processor architecture. The `solution-stack-name`
parameter applies to platform version.

###### Example 1 — create a new arm64 based environment (namespace options inline)

```
aws elasticbeanstalk create-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2 v3.4.7 running Docker"` \
--option-settings \
Namespace=aws:autoscaling:launchconfiguration,OptionName=IamInstanceProfile,Value=`aws-elasticbeanstalk-ec2-role` \
Namespace=aws:ec2:instances,OptionName=InstanceTypes,Value=`t4g.small`
```

As an alternative, use an `options.json` file to specify the namespace
options instead of including them inline.

###### Example 2 — create a new arm64 based environment (namespace options in

`options.json` file)

```
aws elasticbeanstalk create-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2 v3.4.7 running Docker"` \
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
    "Namespace": "aws:ec2:instances",
    "OptionName": "InstanceTypes",
    "Value": "t4g.small"
  }
]
```

The next two examples update the configuration for an existing environment with the [update-environment](../../../cli/latest/reference/elasticbeanstalk/update-environment.md "../../../cli/latest/reference/elasticbeanstalk/update-environment.md") command. In this example we're adding another instance type that's
also based on arm64 processor architecture. For existing environments, all instance types that
are added must have the same processor architecture. If you want to replace the existing
instance types with those from a different architecture, you can do so. But make sure that all
of the instance types in the command have the same type of architecture.

###### Example 3 — update an existing arm64 based environment (namespace options inline)

```
aws elasticbeanstalk update-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2 v3.4.7 running Docker"` \
--option-settings \
Namespace=aws:autoscaling:launchconfiguration,OptionName=IamInstanceProfile,Value=`aws-elasticbeanstalk-ec2-role` \
Namespace=aws:ec2:instances,OptionName=InstanceTypes,Value=`t4g.small,t4g.micro`
```

As an alternative, use an `options.json` file to specify the namespace
options instead of including them inline.

###### Example 4 — update an existing arm64 based environment (namespace options in

`options.json` file)

```
aws elasticbeanstalk update-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2 v3.4.7 running Docker"` \
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
    "Namespace": "aws:ec2:instances",
    "OptionName": "InstanceTypes",
    "Value": "t4g.small, t4g.micro"
  }
]
```

The next two examples show more [create-environment](../../../cli/latest/reference/elasticbeanstalk/create-environment.md "../../../cli/latest/reference/elasticbeanstalk/create-environment.md")
commands. These examples don't provide values for `InstanceTypes`. When
`InstanceTypes` values aren't specified, Elastic Beanstalk defaults to x86 based processor
architecture. The Image ID (AMI) for the environment's EC2 instances will default according to
the Region, platform version and defaulted instance type. The instance type corresponds to a
processor architecture.

###### Example 5 — create a new x86 based environment (namespace options inline)

```
aws elasticbeanstalk create-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2 v3.4.7 running Docker"` \
--option-settings \
Namespace=aws:autoscaling:launchconfiguration,OptionName=IamInstanceProfile,Value=`aws-elasticbeanstalk-ec2-role`
```

As an alternative, use an `options.json` file to specify the namespace
options instead of including them inline.

###### Example 6 — create a new x86 based environment (namespace options in

`options.json` file)

```
aws elasticbeanstalk create-environment \
--region `us-east-1` \
--application-name `my-app` \
--environment-name `my-env` \
--solution-stack-name `"64bit Amazon Linux 2 v3.4.7 running Docker"` \
--option-settings `file://options.json`
```

```
### example options.json ###
[
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "IamInstanceProfile",
    "Value": "aws-elasticbeanstalk-ec2-role"
  }
]
```
