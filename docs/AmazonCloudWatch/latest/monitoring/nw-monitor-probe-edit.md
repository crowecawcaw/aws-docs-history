# Edit a probe

You can change any information for an existing probe, regardless of whether that probe is
active or inactive.

You can work with monitors and probes by using either the Amazon CloudWatch
console or the AWS Command Line Interface. To work with Network Synthetic Monitor programmatically, see the
[Network Synthetic Monitor API Reference](../../../networkmonitor/latest/APIReference/Welcome.md "../../../networkmonitor/latest/APIReference/Welcome.md") and
[networkmonitor](../../../cli/latest/reference/networkmonitor.md "../../../cli/latest/reference/networkmonitor.md") in the AWS Command Line Interface Command Reference.

###### To edit a probe by using the console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"), and then, under **Network
   Monitoring**, choose **Synthetic monitors**.

Under **Name**, choose a monitor link to open the monitor dashboard. 2. Choose the **Monitor details** tab. 3. In the **Probes** section, choose the link for the probe that you want to
edit. 4. On the probe details page, choose **Edit**. 5. On the **Edit _probe_** page, enter the
new destination **IP address** for the probe. IPv4 and IPv6 addresses are both
supported. 6. Choose **Advanced settings**. 7. Choose a network **Protocol**, **ICMP** or **TCP**. 8. If the **Protocol** is **TCP**, enter the following
information:

    * Enter the **Port** that your network uses to connect. The port must be
     a number from **1** to **65535**.
    * Enter the **Packet size**. This is the size, in bytes, of each packet
     sent along the probe between the source and destination. Packet size must be a number from
     **56** to **8500**.

9. (Optional) Add, change, or remove Tags for the probe.
10. Choose **Save changes**.
