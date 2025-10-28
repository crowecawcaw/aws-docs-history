# **eb terminate**

## Description

Terminates the running environment so that you don't incur charges for unused AWS resources.

Using the `--all` option, deletes the application that the current directory was initialized to using [eb init](eb3-init.md "eb3-init.md"). The command terminates all environments in the application. It also terminates the [application versions](applications-versions.md "applications-versions.md") and [saved configurations](environment-configuration-savedconfig.md "environment-configuration-savedconfig.md") for the application, and then deletes
the application.

If the root directory contains a `platform.yaml` file specifying a custom platform, this command terminates the running custom
environment.

###### Note

You can always launch a new environment using the same version later.

If you have data from an environment that you want to preserve, set the database deletion policy to `Retain` before terminating the
environment. This keeps the database operational outside of Elastic Beanstalk. After this, any Elastic Beanstalk environments must connect to it as an external database. If you
want to back up the data without keeping the database operational, set the deletion policy to take a snapshot of the database before terminating the
environment. For more information, see [Database lifecycle](using-features.managing.md#environments-cfg-rds-lifecycle "using-features.managing.md#environments-cfg-rds-lifecycle") in the
_Configuring environments_ chapter of this guide.

###### Important

If you terminate an environment, you must also delete any CNAME mappings that you created, as other customers can reuse an available hostname. Be sure to
delete DNS records that point to your terminated environment to prevent a _dangling DNS entry_. A dangling DNS entry can expose internet
traffic destined for your domain to security vulnerabilities. It can also present other risks.

For more information, see [Protection from dangling
delegation records in Route 53](../../../Route53/latest/DeveloperGuide/protection-from-dangling-dns.md "../../../Route53/latest/DeveloperGuide/protection-from-dangling-dns.md") in the _Amazon Route 53 Developer Guide_. You can also learn more about dangling DNS entries in [Enhanced Domain Protections for Amazon CloudFront Requests](https://aws.amazon.com/blogs/security/enhanced-domain-protections-for-amazon-cloudfront-requests/ "https://aws.amazon.com/blogs/security/enhanced-domain-protections-for-amazon-cloudfront-requests/") in the _AWS Security Blog_.

## Syntax

**eb terminate**

**eb terminate `environment-name`**

## Options

| Name             | Description                                                                                                                                                                                                                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--all`          | Terminates all environments in the application, the application's [application versions](applications-versions.md "applications-versions.md"), and its [saved configurations](environment-configuration-savedconfig.md "environment-configuration-savedconfig.md"), and then deletes the application. |
| `--force`        | Terminates the environment without prompting for confirmation.                                                                                                                                                                                                                                        |
| `--ignore-links` | Terminates the environment even if there are dependent environments with links to it. See [Compose Environments](ebcli-compose.md "ebcli-compose.md").                                                                                                                                                |
| `--timeout`      | The number of minutes before the command times out.                                                                                                                                                                                                                                                   | ## Output If successful, the command returns the status of the `terminate` operation. ## Example The following example request terminates the environment tmp-dev. ``$ `eb terminate` The environment "tmp-dev" and all associated instances will be terminated. To confirm, type the environment name: tmp-dev 2018-07-11 21:05:25    INFO: terminateEnvironment is starting. 2018-07-11 21:05:40    INFO: Deleted CloudWatch alarm named: awseb-e-2cpfjbra9a-stack-AWSEBCloudwatchAlarmHigh-16V08YOF2KQ7U 2018-07-11 21:05:41    INFO: Deleted CloudWatch alarm named: awseb-e-2cpfjbra9a-stack-AWSEBCloudwatchAlarmLow-6ZAWH9F20P7C 2018-07-11 21:06:42    INFO: Deleted Auto Scaling group policy named: arn:aws:autoscaling:us-east-2:11122223333:scalingPolicy:5d7d3e6b-d59b-47c5-b102-3e11fe3047be:autoScalingGroupName/awseb-e-2cpfjbra9a-stack-AWSEBAutoScalingGroup-7AXY7U13ZQ6E:policyName/awseb-e-2cpfjbra9a-stack-AWSEBAutoSca lingScaleUpPolicy-1876U27JEC34J 2018-07-11 21:06:43    INFO: Deleted Auto Scaling group policy named: arn:aws:autoscaling:us-east-2:11122223333:scalingPolicy:29c6e7c7-7ac8-46fc-91f5-cfabb65b985b:autoScalingGroupName/awseb-e-2cpfjbra9a-stack-AWSEBAutoScalingGroup-7AXY7U13ZQ6E:policyName/awseb-e-2cpfjbra9a-stack-AWSEBAutoSca lingScaleDownPolicy-SL4LHODMOMU 2018-07-11 21:06:48    INFO: Waiting for EC2 instances to terminate. This may take a few minutes. 2018-07-11 21:08:55    INFO: Deleted Auto Scaling group named: awseb-e-2cpfjbra9a-stack-AWSEBAutoScalingGroup-7AXY7U13ZQ6E 2018-07-11 21:09:10    INFO: Deleted security group named: awseb-e-2cpfjbra9a-stack-AWSEBSecurityGroup-XT4YYGFL7I99 2018-07-11 21:09:40    INFO: Deleted load balancer named: awseb-e-2-AWSEBLoa-AK6RRYFQVV3S 2018-07-11 21:09:42    INFO: Deleting SNS topic for environment tmp-dev. 2018-07-11 21:09:52    INFO: terminateEnvironment completed successfully.`` |
