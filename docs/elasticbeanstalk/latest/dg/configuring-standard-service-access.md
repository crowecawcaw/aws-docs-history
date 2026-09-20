

# Configuring service access for a Beanstalk Standard environment
<a name="configuring-standard-service-access"></a>

A Beanstalk Standard environment uses a service role that Elastic Beanstalk assumes on your behalf and an Amazon EC2 instance profile that its instances assume. For details about these roles and how to create them, see [Elastic Beanstalk Service roles, instance profiles, and user policies](concepts-roles.md).

## Environment security configuration namespaces
<a name="using-features.managing.security.namespaces"></a>

Elastic Beanstalk provides [configuration options](command-options.md) in the following namespaces to enable you to customize the security of your environment:
+ [`aws:elasticbeanstalk:environment`](command-options-general.md#command-options-general-elasticbeanstalkenvironment) – Configure the environment's service role using the `ServiceRole` option.
+ [`aws:autoscaling:launchconfiguration`](command-options-general.md#command-options-general-autoscalinglaunchconfiguration) – Configure permissions for the environment's Amazon EC2 instances using the `EC2KeyName`, `IamInstanceProfile`, `DisableDefaultEC2SecurityGroup`, and `SecurityGroups` options.

The EB CLI and Elastic Beanstalk console apply recommended values for the preceding options. You must remove these settings if you want to use configuration files to configure the same. See [Recommended values](command-options.md#configuration-options-recommendedvalues) for details.