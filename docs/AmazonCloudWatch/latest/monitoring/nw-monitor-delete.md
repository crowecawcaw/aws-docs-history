# Delete a monitor

Before you can delete a monitor in Network Synthetic Monitor, you must deactivate or delete all probes associated with
 the monitor, regardless of the monitor **State**. After a monitor is
 deleted, you are no longer be charged for probes in the monitor. Be aware that you can't restore
 a deleted monitor.

You can work with monitors and probes by using either the Amazon CloudWatch
 console or the AWS Command Line Interface. To work with Network Synthetic Monitor programmatically, see the 
 [Network Synthetic Monitor API Reference](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html") and
 [networkmonitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/ "https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/") in the AWS Command Line Interface Command Reference.

###### To delete a monitor using the console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"), and then, under **Network
 Monitoring**, choose **Synthetic monitors**.
2. In the **Monitors** section, choose the monitor that you want to
 delete.
3. Choose **Actions**, and then choose **Delete**.
4. If you have any active probes for the monitor, you're prompted to deactivate them. Choose
 **Deactivate probes**. 


###### Note

You can't cancel or undo this action after you choose **Deactivate
 probes**. Deactivated probes, however, aren't removed from the monitor. If you like, you can
 reactivate them later. For more information, see [Activate or deactivate a probe](nw-monitor-probe-status.md "nw-monitor-probe-status.md").
5. Enter `confirm` in the confirmation field, and then choose
 **Delete**.
Alternatively, you can delete a monitor programmatically, for example, by using the AWS Command Line Interface. 

###### To delete a monitor by using the CLI

1. To delete a monitor, you need the monitor name. If you don't know the name, get a list of your monitors 
 by running the 
 [list-monitors](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/list-monitors.html "https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/list-monitors.html") command. Note the name of the monitor that you want to delete.
2. Verify whether the monitor contains any active probes. Use [get-monitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/get-monitor.html "https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/get-monitor.html") with the
 monitor name from the previous step. This returns a list of any probes associated with that
 monitor.
3. If the monitor contains active probes, you must first either set the probes to inactive
 or delete them. 




	* To set a probe to inactive, use [update-probe](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/update-probe.html "https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/update-probe.html"), and set the state to `INACTIVE`.
	* To delete a probe, use [delete-probe](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/delete-probe.html "https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/delete-probe.html").
4. After the probes are set to `INACTIVE` or deleted, you can delete the monitor 
 by running the [delete-monitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/create-probe.html "https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/create-probe.html") command. Inactive probes are not deleted when you delete the monitor.
