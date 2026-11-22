

# Pausing and resuming Elastic Beanstalk environments

When you **pause** an AWS Elastic Beanstalk environment, Elastic Beanstalk scales its Auto Scaling group to zero instances. The environment keeps its name, ID, URL, configuration, application version history, and any attached resources. As a result, you stop paying for the environment's Amazon EC2 instances without terminating the environment or rebuilding it later.

Pausing is useful for development and test environments that sit idle outside working hours.

A paused environment reports a health status of **Paused** in the Elastic Beanstalk console. Because the environment has no instances, it doesn't serve requests while it's paused.

The Elastic Beanstalk console displays this status. However, Elastic Beanstalk has no corresponding environment state. The health that the [DescribeEnvironments](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html) operation returns for a paused environment depends on which health reporting system the environment uses. Because a paused environment has no instances to report health, an environment that uses enhanced health reporting returns a `Health` of `Grey` and a `HealthStatus` of `No Data`. An environment that uses basic health reporting returns a `Health` of `Red`.

**Note**  
Pausing doesn't stop charges for resources that exist independently of the environment's instances, such as a load balancer, an Elastic IP address that a single-instance environment keeps allocated, a coupled Amazon RDS database instance, or stored application versions and CloudWatch data. To stop the charges that pausing leaves in place, terminate the environment, which also deletes the AWS resources that Elastic Beanstalk created for it. Terminating doesn't delete your application versions or a retained database. It also keeps your CloudWatch Logs logs, unless log streaming is configured to delete them when the environment terminates. For more information, see [Terminate an Elastic Beanstalk environment](using-features.terminating.md).

You can pause both load-balanced and single-instance environments. In either case, Elastic Beanstalk scales the environment to zero instances while it's paused. The two types differ only when you resume: a load-balanced environment resumes with the capacity you choose, while a single-instance environment always resumes with exactly one instance.

## Pausing an environment
<a name="environment-management-pause-pausing"></a>

**To pause an environment (console)**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. Choose **Actions**, and then choose **Pause environment**.

1. Review the options in the dialog box. Depending on how the environment is configured, the dialog box shows both of the following options, one of them, or neither.
   + **Turn off managed platform updates** – A paused environment has no instances to update, so each maintenance window records a failed managed update. The console offers to turn managed updates back on when you resume the environment. This option appears only for an environment that uses enhanced health reporting, which managed platform updates require.
   + **Suspend scheduled scaling actions** – A scheduled action that sets a nonzero capacity would launch instances again while the environment is paused. This option appears only if the environment has scheduled scaling actions that aren't already suspended.

1. Choose **Pause**.

To pause an environment with the Elastic Beanstalk API, use the [UpdateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html) operation with the AWS CLI or the AWS SDK to set the minimum and maximum instance counts to zero.

```
$ aws elasticbeanstalk update-environment --environment-id e-{{vdnftxubwq}} \
  --option-settings Namespace=aws:autoscaling:asg,OptionName=MinSize,Value=0 \
                    Namespace=aws:autoscaling:asg,OptionName=MaxSize,Value=0
```

Pausing with the API changes only the instance counts. If the environment has scheduled scaling actions, set `Suspend` to `true` for each one in the `aws:autoscaling:scheduledaction` namespace, or they can launch instances again while the environment is paused. For more information, see [aws:autoscaling:scheduledaction](command-options-general.md#command-options-general-autoscalingscheduledaction).

## Resuming an environment
<a name="environment-management-pause-resuming"></a>

To resume an environment, set its minimum and maximum instance counts back to nonzero values. For a load-balanced environment that you paused in the Elastic Beanstalk console, the console saves your instance counts and suggests them when you resume. If you resume in a different browser, or the console didn't save the counts, enter them yourself. If the environment's minimum was 0, the console saves a minimum of 1.

A single-instance environment always resumes with exactly one instance. The console doesn't offer a capacity choice for it.

**To resume an environment (console)**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. Choose **Actions**, and then choose **Resume environment**.

1. For a load-balanced environment, review the capacity that the environment resumes with. To change it, expand **Change capacity** and enter the minimum and maximum instance counts. If the console has no saved capacity, enter both values.

1. (Optional) Choose **Turn managed platform updates back on** or **Turn suspended scheduled scaling actions back on**. These options are selected by default only if you paused the environment from this browser.

1. Choose **Resume**.

To resume an environment with the Elastic Beanstalk API, use the [UpdateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html) operation to set the minimum and maximum instance counts back to the values you want.

```
$ aws elasticbeanstalk update-environment --environment-id e-{{vdnftxubwq}} \
  --option-settings Namespace=aws:autoscaling:asg,OptionName=MinSize,Value={{1}} \
                    Namespace=aws:autoscaling:asg,OptionName=MaxSize,Value={{4}}
```

This example applies to a load-balanced environment. A single-instance environment always resumes with one instance, so set both `MinSize` and `MaxSize` to `1`. Elastic Beanstalk overrides other values for a single-instance environment.