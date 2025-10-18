# Create a monitor

The following sections describe how to create a monitor in Network Synthetic Monitor, including the required probes. 
 When you create a monitor, you specify probes by choosing source subnets, and then adding up to 
 four destinations for each one. Each source-destination pair is a probe.

You can make changes to a monitor after you create it, for example, to add, remove, or deactivate
 probes. For more information, see [Working with monitors and probes in Network Synthetic Monitor](nw-monitor-working-with.md "nw-monitor-working-with.md").

You can work with monitors and probes by using either the Amazon CloudWatch
 console or the AWS Command Line Interface. To work with Network Synthetic Monitor programmatically, see the 
 [Network Synthetic Monitor API Reference](https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html "https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html") and
 [networkmonitor](https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/ "https://docs.aws.amazon.com/cli/latest/reference/networkmonitor/") in the AWS Command Line Interface Command Reference.

The following procedures provide step-by-step instructions for how to create a monitor by using the Amazon CloudWatch
 console. 


* [Define monitor details](#NWDefineDetails "#NWDefineDetails")
* [Choose sources and destinations](#NWSourceDestination "#NWSourceDestination")
* [Confirm probes](#NWConfirmProbes "#NWConfirmProbes")
* [Review and create monitor](#NWReviewCreate "#NWReviewCreate")
###### Important

These steps are designed to be completed all at once. You can't save in-process work to continue later.

## Define monitor details


The first step to create a monitor is to define the basic details, by giving
 the monitor a name and defining the aggregation period. Optionally, you can also add tags.


###### To define monitor details

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"), and then, under **Network
 Monitoring**, choose **Synthetic monitors**.
2. Choose **Create monitor**.
3. For **Monitor name**, enter a name for the monitor.
4. For **Aggregation period**, choose how often you want to send
 metrics to CloudWatch: **30 seconds** or **60 seconds**.


###### Note

A shorter aggregation period provides faster detection of network issues. However, the 
aggregation period that you choose can affect your billing costs. For more information about pricing, see the [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") page.
5. (Optional) For **Tags**, add **Key** and
 **Value** pairs to help identify this resource, so that you can
 search or filter on specific information.




	1. Choose **Add new tag**.
	2. Enter a **Key** name and associated **Value**.
	3. Choose **Add new tag** to add the new tag.
	
	
	You can add multiple tags by choosing **Add new tag**, or you can
	 remove a tag by choosing **Remove**.
	4. If you want to associate your tags with the probes for the monitor, keep **Add tags to probes
	 created by monitor** selected. This adds the tags to the monitor probes, which can
	 be helpful for tag-based authentication or metering.
6. Choose **Next**. On the next page, you'll specify sources and destinations,
 to create probes for the monitor.

## Choose sources and destinations


For each monitor in Network Synthetic Monitor, you specify one or more probes, which are a combination
 of an AWS source and a destination.



* A source for a probe is a VPC and associated subnets (or
 just a VPC subnet) in the Regions where your network operates.
* A destination is the combination of on-premises IP addresses, network protocols, 
 ports, and network packet size.

###### Important

These steps are designed to be completed all at once. You can't save in-process work to continue later.


###### To choose sources and destinations

1. Prerequisite: [Define monitor details](#define-details-nw "#define-details-nw").
2. Under **AWS**
**network source**, choose one or more subnets to include in the monitor. To
 choose all subnets within a VPC, choose the VPC. Or, choose specific subnets within a VPC.
 The subnets that you choose are the monitor sources.
3. For **Destination 1**, enter a destination IP address of the
 on-premises network. IPv4 and IPv6 addresses are both supported.
4. Choose **Advanced settings**.
5. For **Protocol**, choose the network protocol for the on-premises destination.
 The protocol can be either **ICMP** or **TCP**.
6. If you choose **TCP**, enter the following information:




	1. Enter the **Port** that your network uses to connect. The port must be
	 a number from **1** to **65535**.
	2. Enter the **Packet size**. This is the size, in bytes, of each packet
	 that's sent on the probe, between the source and destination. Packet size must be a number
	 from **56** to **8500**.
7. Choose **Add destination** to add another on-premises
 destination to the monitor. Repeat these steps for each destination that you want to
 add.
8. When you're finished adding sources and destinations, choose **Next** to confirm 
 the probes for the monitor.

## Confirm probes


On the **Confirm probes** page, review all the probes that will be created
 for the monitor, to make sure that they're the correct set of sources and destinations.


The **Confirm probes** page shows all the possible combinations of the 
 sources and destinations for the probe specifications that you provided in the previous step.
 For example, if you have six source subnets and four destination IP addresses, there are 24 
 possible probe combinations, so 24 probes will be created. 


###### Important


* These steps are intended to be completed in one session. You can't save
 in-process work to continue later.
* The **Confirm probes** page does not indicate whether a probe is
 valid. We recommend that you review this page carefully, and then delete any probes that
 aren't valid. You might be charged for probes that aren't valid if you don't remove them.

###### To confirm monitor probes

1. Prerequisite: [Choose sources and destinations](#source-destination-nw "#source-destination-nw").
2. On the **Confirm probes** page, review the list of source and destination
 probe combinations.
3. Choose any probes that you want to remove from the monitor, and then choose
 **Remove**.


###### Note

You are not prompted to confirm deleting a probe. If you delete a probe and want to
 restore it, you must set it up again. You can add a probe to an existing monitor by
 following the steps in [Add a probe to a monitor](nw-monitor-add-probe.md "nw-monitor-add-probe.md").
4. Choose **Next**, and then review the monitor details.

## Review and create monitor


The final step is to review the details of the monitor and the probes for the monitor,
 and then create the monitor. You can change any information about the monitor at this point. 


When you have finished reviewing and updating any information that isn't correct, create the monitor.


As soon as you create the monitor, Network Synthetic Monitor begins tracking metrics and you'll start being charged
 for probes in the monitor.


###### Important


* This step is intended to be completed in one session. You can't save in-process work to continue later.
* If you choose to edit a section, you must step through the process to create a monitor from
 the point that you make the edits. Earlier monitor creation pages maintain the information that 
 you already entered.

###### To review and create a monitor

1. On the **Review and create probes** page, choose
 **Edit** for any section where you want to make changes.
2. Make changes in that section, and then choose **Next**.
3. When you're finished making edits, choose **Create monitor**.


The Network Synthetic Monitor page displays the current state of monitor creation in the
 **Monitors** section. When Network Synthetic Monitor is still creating the monitor, the
 **State** is **Pending**. When the
 **State** changes to **Active**, you can view CloudWatch metrics
 in the monitor dashboard.


For information on working with the monitor dashboard, see [Network Synthetic Monitor dashboards](nw-monitor-dashboards.md "nw-monitor-dashboards.md").

###### Note

It can take several minutes for a newly-added monitor to begin collecting network metrics.
