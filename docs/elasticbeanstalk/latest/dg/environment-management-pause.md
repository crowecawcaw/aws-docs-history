

# Pausing and resuming Elastic Beanstalk environments
<a name="environment-management-pause"></a>

When you **pause** an AWS Elastic Beanstalk environment, Elastic Beanstalk scales its Auto Scaling group to zero instances. The environment keeps its name, ID, URL, configuration, application version history, and any attached resources. As a result, you stop paying for the environment's Amazon EC2 instances without terminating the environment or rebuilding it later.

Pausing is useful for development and test environments that sit idle outside working hours.

A paused environment reports a health status of **Paused** in the Elastic Beanstalk console. Because the environment has no instances, it doesn't serve requests while it's paused.

The Elastic Beanstalk console displays this status. However, Elastic Beanstalk has no corresponding environment state. The health that the [DescribeEnvironments](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html) action returns for a paused environment depends on which health reporting system the environment uses. Because a paused environment has no instances to report health, an environment that uses enhanced health reporting returns a `Health` of `Grey` and a `HealthStatus` of `No Data`. An environment that uses basic health reporting returns a `Health` of `Red`.

**Note**  
Pausing doesn't stop charges for resources that exist independently of the environment's instances, such as a load balancer, a coupled Amazon RDS database instance, or stored application versions and CloudWatch data. To stop the charges that pausing leaves in place, terminate the environment, which also deletes the AWS resources that Elastic Beanstalk created for it. Terminating doesn't delete your application versions or a retained database. It also keeps your CloudWatch Logs logs, unless log streaming is configured to delete them when the environment terminates. For more information, see [Terminate an Elastic Beanstalk environment](using-features.terminating.md).

You can pause load-balanced environments only. Single-instance environments always run exactly one instance, so their capacity can't be set to zero.

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

To pause an environment with the Elastic Beanstalk API, use the [UpdateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html) action with the AWS CLI or the AWS SDK to set the minimum and maximum instance counts to zero.

```
$ aws elasticbeanstalk update-environment --environment-id e-{{vdnftxubwq}} \
  --option-settings Namespace=aws:autoscaling:asg,OptionName=MinSize,Value=0 \
                    Namespace=aws:autoscaling:asg,OptionName=MaxSize,Value=0
```

Pausing with the API changes only the instance counts. If the environment has scheduled scaling actions, set `Suspend` to `true` for each one in the `aws:autoscaling:scheduledaction` namespace, or they can launch instances again while the environment is paused. For more information, see [aws:autoscaling:scheduledaction](command-options-general.md#command-options-general-autoscalingscheduledaction).

## Resuming an environment
<a name="environment-management-pause-resuming"></a>

To resume an environment, set its minimum and maximum instance counts back to nonzero values. When you pause an environment in the Elastic Beanstalk console, the console saves its instance counts in your browser and suggests them when you resume. If you resume in a different browser, or the counts weren't saved, the console asks you to enter them. If the environment's minimum was 0, the console saves a minimum of 1.

**To resume an environment (console)**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk), and in the **Regions** list, select your AWS Region.

1. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.

1. Choose **Actions**, and then choose **Resume environment**.

1. Review the capacity that the environment resumes with. To change it, expand **Change capacity** and enter the **Minimum instances** and **Maximum instances**. If the console has no saved capacity, enter both values.

1. (Optional) Choose **Turn managed platform updates back on** or **Turn suspended scheduled scaling actions back on**. These options are selected by default only if you paused the environment from this browser.

1. Choose **Resume**.

To resume an environment with the Elastic Beanstalk API, use the [UpdateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html) action to set the minimum and maximum instance counts back to the values you want.

```
$ aws elasticbeanstalk update-environment --environment-id e-{{vdnftxubwq}} \
  --option-settings Namespace=aws:autoscaling:asg,OptionName=MinSize,Value={{1}} \
                    Namespace=aws:autoscaling:asg,OptionName=MaxSize,Value={{4}}
```