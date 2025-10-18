# Add a probe to a monitor

You can add a probe to an existing monitor in Network Synthetic Monitor. Note that when you add probes to a monitor,
 your billing structure is updated to include the new probe. 

You can work with monitors and probes by using either the Amazon CloudWatch
 console or the AWS Command Line Interface. To work with Network Synthetic Monitor programmatically, see the 
 [Network Synthetic Monitor API Reference](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html") and
 [networkmonitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/ "https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/") in the AWS Command Line Interface Command Reference.

###### To add a probe to a monitor using the console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"), and then, under **Network
 Monitoring**, choose **Synthetic monitors**.
2. In the **Monitors** section, do one of the following:




	* Choose the **Name** link of the monitor that you want to add a probe
	 to. Choose the **Monitor details** tab, and then in the
	 **Probes** section, choose **Add probe**.
	* Choose the monitor check box, choose **Actions**, and then choose
	 **Add probe**.
3. On the **Add probe** page, do the following:




	1. Under **AWS**
	**network source**, choose a subnet to add to the monitor. 
	
	
	###### Note
	
	You can only add one probe at a time and up to four probes per monitor.
	2. Enter the destination **IP address** of the on-premises network.
	 Both IPv4 and IPv6 addresses are supported.
	3. Choose **Advanced settings**.
	4. Choose the network **Protocol** for the destination. It can be either
	 **ICMP** or **TCP**.
	5. If the **Protocol** is **TCP**, enter the following
	 information. Otherwise, skip to the next step: 
	
	
	
	
		* Enter the **Port** that your network uses to connect. The port must
		 be a number from **1** to **65535**.
		* Enter the **Packet size**. This is the size, in bytes, of each
		 packet sent along the probe between the source and destination. Packet size must be a
		 number from **56** to **8500**.
4. (Optional) In the **Tags** section, add **Key** and
 **Value** pairs to further help identify this resource, allowing you to
 search or filter on specific information.




	1. Choose **Add new tag**.
	2. Enter a **Key** name and associated **Value**.
	3. Choose **Add new tag** to add the new tag.
	
	
	You can add multiple tags by choosing **Add new tag**, or you can
	 remove any tag by choosing **Remove**.
5. Choose **Add probe**.


While the probe is being activated, the **State** shows
 **Pending**. It might take several minutes for the probe to become
 **Active**.
