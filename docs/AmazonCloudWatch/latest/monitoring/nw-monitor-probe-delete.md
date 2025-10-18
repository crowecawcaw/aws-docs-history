# Delete a probe

You can delete a probe rather than deactivating it if you know that you won't need it again
 later. You can't recover a deleted probe; instead, you must recreate it. Billing charges end
 for a probe when the probe is deleted.

You can work with monitors and probes by using either the Amazon CloudWatch
 console or the AWS Command Line Interface. To work with Network Synthetic Monitor programmatically, see the 
 [Network Synthetic Monitor API Reference](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html") and
 [networkmonitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/ "https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/") in the AWS Command Line Interface Command Reference.

###### To delete a probe using the console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"), and then, under **Network
 Monitoring**, choose **Synthetic monitors**.
2. In the **Monitors** section, under **Name**, 
 choose a monitor link to open the monitor dashboard.
3. Choose the **Monitor details** tab.
4. Choose the monitor check box, choose **Actions**, and then choose
 **Delete**.
5. In the **Delete probe** dialog box, do the following:
6. Choose **Delete** to confirm that you want to delete the probe. 


The **State** of the probe in the **Probes** section
 shows **Deleting**. After it's deleted, the probe is removed from the
 **Probes** section.
