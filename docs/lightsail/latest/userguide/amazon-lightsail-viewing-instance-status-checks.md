

# View status checks for your Lightsail instance
<a name="amazon-lightsail-viewing-instance-status-checks"></a>

Amazon Lightsail runs status checks on your instance to detect problems that can prevent it from running your applications. You can see the current result of these checks on the instance management page, with **Instance state**. When a check fails, the check that failed tells you where the problem is. The problem can be with the AWS infrastructure that your instance runs on, or with the software and configuration inside your instance.

**Note**  
Status checks are different from the instance state. The instance state shows where the instance is in its lifecycle, such as running, stopped, or pending. Status checks show whether a running instance is reachable. An instance can be in the running state even if one of its status checks has failed.

**Contents**
+ [Types of status checks](#status-check-types)
+ [Status check results](#status-check-results)
+ [View status checks using the Lightsail console](#viewing-status-checks)
+ [View status check history and get notified](#status-check-history)
+ [Next steps](#next-steps-status-checks)

## Types of status checks
<a name="status-check-types"></a>

Each status check is a reachability check that runs automatically every minute as long as your instance is running. You don't need to turn the checks on, and you can't turn them off.

Lightsail reports the following two status checks for each instance:
+ **System status check** – Monitors the AWS infrastructure that your instance runs on. A failure means there is a problem with the underlying host that needs AWS involvement to repair. Examples include a loss of network connectivity, a loss of system power, or a hardware or software issue on the physical host.
+ **Instance status check** – Monitors the software and network configuration inside your instance. A failure means there is a problem that you need to fix from within the instance. Examples include incorrect networking or startup configuration, exhausted memory, a corrupted file system, or an incompatible kernel. A failed system status check can also cause the instance status check to fail.

## Status check results
<a name="status-check-results"></a>

Each status check shows one of the following results:
+ **Passed** – The check is passing. The instance is reachable and operating normally. The console shows this result with a green success icon.
+ **Failed** – The check has failed. The instance has a problem that needs attention. The console shows this result with a red error icon. For the steps to take, see [Troubleshoot failed status checks on your Lightsail instance](amazon-lightsail-instance-status-checks.md).
+ **Initializing** – The instance was recently started or restarted, and the check is still in progress. This typically resolves within a few minutes. The console shows this result with a yellow warning icon.
+ **Insufficient data** – There is not yet enough data to determine the result. This can occur briefly after the instance starts. The console shows this result with a yellow warning icon.
+ **Not applicable** – The check does not apply to the instance at this time. The console shows this result with a gray stopped icon.

## View status checks using the Lightsail console
<a name="viewing-status-checks"></a>

View the status checks when your instance or its applications are unreachable, to find out whether the problem is with the AWS infrastructure or with your instance. Before you begin, you need a running instance.

To view the status checks for an instance using the Lightsail console, complete the following steps:

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Instances**.

1. Choose the name of the instance for which you want to view status checks.

1. On the instance management page, find **System status check** and **Instance status check**, which appear with **Instance state**.

1. (Optional) To see what a check monitors, choose the Tips icon next to it. To open the steps for fixing a failed check, choose **How to fix status check failures** in the popover.

The following image shows an instance whose system status check and instance status check have both passed.

![Instance management page showing Instance state Running, System status check Passed, and Instance status check Passed.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-status-checks-passed.png)


On the **Instances** page, the card for each instance shows **Status check failed** with the instance state when either status check has failed. The card does not show anything extra when both checks are passing.

## View status check history and get notified
<a name="status-check-history"></a>

The status checks on the instance management page show only the current result. To see how the results changed over time, use the **Status check failures**, **Instance status check failures**, and **System status check failures** metrics on the **Metrics** tab of the instance management page. For more information about these metrics, see [Monitor Lightsail instance performance with metrics](amazon-lightsail-viewing-instance-health-metrics.md).

To be notified when a status check fails, create an alarm on one of these metrics. For more information, see [Configure status check alarms for your Lightsail instance](amazon-lightsail-configure-status-check-alarms.md).

## Next steps
<a name="next-steps-status-checks"></a>
+ If a status check has failed, see [Troubleshoot failed status checks on your Lightsail instance](amazon-lightsail-instance-status-checks.md).
+ To learn how status checks work on the underlying Amazon EC2 instance, see [Status checks for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html) in the Amazon EC2 documentation.
+ To get status checks programmatically, set `includeHealthStatus` to `true` when you call [GetInstance](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstance.html) or [GetInstances](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetInstances.html). For the response fields, see the *Lightsail API Reference*.

**Topics**
+ [Types of status checks](#status-check-types)
+ [Status check results](#status-check-results)
+ [View status checks using the Lightsail console](#viewing-status-checks)
+ [View status check history and get notified](#status-check-history)
+ [Next steps](#next-steps-status-checks)
+ [Configure status check alarms](amazon-lightsail-configure-status-check-alarms.md)
+ [Troubleshoot status checks](amazon-lightsail-instance-status-checks.md)