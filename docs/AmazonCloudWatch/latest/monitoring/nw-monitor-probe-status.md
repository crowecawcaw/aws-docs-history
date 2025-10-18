# Activate or deactivate a probe

You can activate or deactivate a probe in a monitor in Network Synthetic Monitor. You might want to deactivate a
 probe, for example, if you aren't currently using it but might want to use it again in the future. By
 deactivating a probe instead of deleting it, you won't need to spend time setting it up again. You are not billed for
 deactivated probes. 

You can work with monitors and probes by using either the Amazon CloudWatch
 console or the AWS Command Line Interface. To work with Network Synthetic Monitor programmatically, see the 
 [Network Synthetic Monitor API Reference](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html") and
 [networkmonitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/ "https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/") in the AWS Command Line Interface Command Reference.

###### To set a probe to active or inactive by using the console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"), and then, under **Network
 Monitoring**, choose **Synthetic monitors**.
2. Choose the **Monitor details** tab.
3. In the **Probes** section, choose the probe that you want to activate or
 deactivate.
4. Choose **Actions**, and then choose **Activate**
 or **Deactivate**.


###### Note

When you reactivate a probe, you begin incurring billing charges on the probe again.
