

# Troubleshoot failed status checks on your Lightsail instance
<a name="amazon-lightsail-instance-status-checks"></a>

When a status check fails, your instance might be unreachable even though its state is **Running**. The steps to fix it depend on which check failed. A failed system status check means there is a problem with the AWS infrastructure that your instance runs on. A failed instance status check means there is a problem inside your instance. For more information about what each check monitors, see [View status checks for your Lightsail instance](amazon-lightsail-viewing-instance-status-checks.md).

**Contents**
+ [Find which status check failed](#find-failed-status-check)
+ [Fix a failed system status check](#fixing-system-status-check-failures)
+ [Fix a failed instance status check](#fixing-instance-status-check-failures)
+ [Unable to connect to your instance](#status-check-cannot-connect)
+ [Next steps](#next-steps-failed-status-checks)

## Find which status check failed
<a name="find-failed-status-check"></a>

To find which status check failed, complete the following steps:

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Instances**.

1. Choose the name of the instance that shows **Status check failed**. On the **Instances** page, each instance card shows the instance state, such as **Running**. When either status check has failed, the card also shows **Status check failed** below the instance state, as in the following image.  
![Two instance cards on the Instances page. Each card shows Running and Status check failed.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instances-status-check-failed-card.png)

1. On the instance management page, check whether **System status check**, **Instance status check**, or both show **Failed**.

If the system status check failed, start with [Fix a failed system status check](#fixing-system-status-check-failures), even if the instance status check also failed. A failed system status check can cause the instance status check to fail, so fixing it can fix both. If only the instance status check failed, see [Fix a failed instance status check](#fixing-instance-status-check-failures).

**Note**  
The instance status check can report a failure during a reboot, until the instance becomes available again. If a check fails right after you reboot or start your instance, wait a few minutes and check again before you take action.

To find when a check started to fail, view the **Status check failures** metrics on the **Metrics** tab of the instance management page. A recent change to the instance around that time, such as an update or a configuration change, can point to the cause.

## Fix a failed system status check
<a name="fixing-system-status-check-failures"></a>

A failed system status check means there is a problem with the AWS infrastructure that your instance runs on. Wait for AWS to fix the issue, or fix it yourself by stopping and then starting the instance. Stopping and starting the instance moves it to a new host in most cases.

On the instance management page of an instance with a failed system status check, **Instance state** shows **Running**, **System status check** shows **Failed**, and **Instance status check** shows **Passed**. When you choose the Tips icon next to **System status check**, the **System status checks** popover explains that the check monitors the AWS infrastructure that your instance runs on, and links to this topic with **How to fix status check failures**. The following image shows this page with the popover open.

![Instance management page showing Instance state Running, System status check Failed, and Instance status check Passed, with the System status checks popover open and its How to fix status check failures link.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-system-status-check-failed.png)


**Note**  
Rebooting your instance does not move it to a new host, so a reboot does not fix a failed system status check. You must stop the instance and then start it.

**Important**  
When you stop and start an instance, its public IP address changes unless you've attached a static IP address to it. Update any DNS records or applications that use the old public IP address. For more information about static IP addresses, see [Create and attach a static IP to your Lightsail instance](lightsail-create-static-ip.md).

To stop and then start the instance so that it moves to a new host, complete the following steps:

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Instances**.

1. Choose the name of the instance that has the failed check.

1. Choose **Stop**, and wait until the instance state is **Stopped**.

1. Choose **Start**.

1. After the instance is running, wait a few minutes for the status checks to complete, and then confirm that **System status check** shows **Passed**.

If the instance status check still shows **Failed** after the system status check passes, see [Fix a failed instance status check](#fixing-instance-status-check-failures).

## Fix a failed instance status check
<a name="fixing-instance-status-check-failures"></a>

A failed instance status check means there is a problem inside your instance that you need to fix. Common causes include the following:
+ Incorrect networking or startup configuration
+ Exhausted memory
+ A corrupted file system
+ An incompatible kernel

On the instance management page of an instance with a failed instance status check, **Instance state** shows **Running**, **System status check** shows **Passed**, and **Instance status check** shows **Failed**. When you choose the Tips icon next to **Instance status check**, the **Instance status checks** popover explains that the check monitors the software and network configuration inside your instance, and links to this topic with **How to fix status check failures**. The following image shows this page with the popover open.

![Instance management page showing Instance state Running, System status check Passed, and Instance status check Failed, with the Instance status checks popover open and its How to fix status check failures link.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-status-check-failed.png)


To find and fix the cause of a failed instance status check, complete the following steps:

1. If the system status check has also failed, fix it first. For more information, see [Fix a failed system status check](#fixing-system-status-check-failures).

1. Reboot the instance. In the Lightsail console, choose the instance, and then choose **Reboot**.

1. After the instance is running, wait a few minutes for the status checks to complete.

1. If the check still fails, connect to your instance. For more information, see [Connect to Linux or Unix instances on Lightsail](lightsail-how-to-connect-to-your-instance-virtual-private-server.md) or [Connect to your Lightsail Windows instance using RDP](connect-to-your-windows-based-instance-using-amazon-lightsail.md). If you can't connect, see [Unable to connect to your instance](#status-check-cannot-connect).

1. Check whether the instance is running out of memory, and review the system logs and any recent changes to the network or startup configuration. Fix the cause that you find, and then reboot the instance.

When the problem is fixed, **Instance status check** shows **Passed**.

## Unable to connect to your instance
<a name="status-check-cannot-connect"></a>

A failed instance status check can prevent you from connecting to your instance. If you can't connect after you reboot the instance, try the following:
+ If you have a snapshot of the instance from before the check started to fail, create a new instance from that snapshot. For more information, see [Create Lightsail instances from snapshots](lightsail-how-to-create-instance-from-snapshot.md).
+ If you use the browser-based SSH or RDP client and see a connection error, see [Resolve connection errors with Lightsail browser-based SSH and RDP clients](amazon-lightsail-troubleshooting-browser-based-ssh-rdp-client-connection.md).
+ If you still can't fix the problem, contact [AWS Support](https://aws.amazon.com/premiumsupport/).

## Next steps
<a name="next-steps-failed-status-checks"></a>
+ To be notified the next time a status check fails, create an alarm on a status check metric. For more information, see [Configure status check alarms for your Lightsail instance](amazon-lightsail-configure-status-check-alarms.md).
+ To protect your data before a problem occurs, take regular snapshots of your instance, or turn on automatic snapshots. For more information, see [Back up Linux/Unix Lightsail instances with snapshots](lightsail-how-to-create-a-snapshot-of-your-instance.md).