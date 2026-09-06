

# Edit a probe
<a name="nw-monitor-probe-edit"></a>

You can change any information for an existing probe, regardless of whether that probe is active or inactive.

You can work with monitors and probes by using either the Amazon CloudWatch console or the AWS Command Line Interface. To work with Network Synthetic Monitor programmatically, see the [Network Synthetic Monitor API Reference](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html) and [networkmonitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/) in the AWS Command Line Interface Command Reference.

**To edit a probe by using the console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/), and then, under **Network Monitoring**, choose **Synthetic monitors**.

   Under **Name**, choose a monitor link to open the monitor dashboard. 

1. Choose the **Monitor details** tab. 

1. In the **Probes** section, choose the link for the probe that you want to edit.

1. On the probe details page, choose **Edit**.

1. On the **Edit *probe*** page, enter the new destination **IP address** for the probe. IPv4 and IPv6 addresses are both supported. 

1. Choose **Advanced settings**.

1. Choose a network **Protocol**, **ICMP** or **TCP**.

1.  If the **Protocol** is **TCP**, enter the following information: 
   + Enter the **Port** that your network uses to connect. The port must be a number from **1** to **65535**.
   + Enter the **Packet size**. This is the size, in bytes, of each packet sent along the probe between the source and destination. Packet size must be a number from **56** to **8500**.

1. (Optional) Add, change, or remove Tags for the probe. 

1. Choose **Save changes**.