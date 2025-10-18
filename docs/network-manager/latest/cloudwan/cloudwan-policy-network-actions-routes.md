# Add a segment action in an AWS Cloud WAN core network policy version

The following steps guide you through optionally setting segment actions for a core network
 for a policy version using the **Policy versions** link on the AWS Network Manager
 console. Before setting segment actions you must first configure your [network settings](cloudwan-core-network-config.md "cloudwan-core-network-config.md") and [add one or more segments](cloudwan-policy-segments.md "cloudwan-policy-segments.md"). For more
 information, about segment actions, see [Segment actions](cloudwan-create-policy-version.md#cloudwan-policy-create-action "cloudwan-create-policy-version.md#cloudwan-policy-create-action"). 


## Segment sharing


Create a shared segment between two segments.


Segment sharing is bidirectional by default. When you create a segment share between
 two segments, routes from both segments are automatically advertised to each other. For
 example, you might share a segment named `test` with another segment
 named `dev`. Routes from `test` are advertised to
 `dev`, and vice versa. To make routes in shared segments
 unidirectional, create a deny list filter to share routes from one segment to the other,
 but not vice versa. Using the previous example, you could make a deny list filter that
 prevents routes from `test` being advertised to `dev`.
 For more information on creating the deny list for a segment, see [Add a segment to an AWS Cloud WAN core network policy version](cloudwan-policy-segments.md "cloudwan-policy-segments.md").


###### To create a shared segment

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Cloud WAN**.
3. On the **Global networks** page, choose the global network ID that for the core network you want to create a policy version for, and then choose **Core network**.
4. In the navigation pane, choose **Policy versions**.
5. Choose **Create policy version**.
6. Choose **Segment actions - optional**.
7. (Optional) In the **Sharing** section, choose
 **Create**, and then do the following:




	1. From the **Segment** dropdown list, choose the core
	 network segment that you want to share.
	2. For the **Segment filter**, choose if you want to
	 **Allow all** shared routes from other segments, to
	 **Allowed selected** segments, or to **Deny
	 selected** segments. The default value is to
	 **Allow all** segments.
	3. Choose **Create sharing**.

## Segment routes


Create a segment route for a policy version.


###### To create a segment route

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Cloud WAN**.
3. On the **Global networks** page, choose the global network ID that for the core network you want to create a policy version for, and then choose **Core network**.
4. In the navigation pane, choose **Policy versions**.
5. Choose **Create policy version**.
6. Choose **Segment actions - optional**.
7. (Optional) In the **Routes** section, choose
 **Create**, and then do the following:




	1. From the **Segment** dropdown list, choose the core
	 network segment that you want to share.
	2. For **Destination CIDR Block**, enter a static route.
	 You can enter multiple CIDR blocks by choosing **Add**
	 for each block that you want to add. Choose **Remove**
	 for any blocks that you don't want. 
	
	
	###### Note
	
	You can't leave any blank destination CIDR blocks. Choose
	 **Remove** to delete any empty blocks.
	3. Choose **Blackhole** if you want to "black hole" the
	 route. If you make this choice, you can't add any attachments to the
	 route.
	4. From the **Attachments** list, choose any attachments
	 that you want to include in this route.
	5. Choose **Create segment route**.
8. (Optional) Add **Attachment policies**. For more information,
 see [Create an attachment policy in an AWS Cloud WAN core
 network policy version](cloudwan-policy-attachments.md "cloudwan-policy-attachments.md").
9. Choose **Create route**.

## Service insertion


Create a segment route for a policy version. 


###### To set up service insertion for a segment

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity** choose **Cloud WAN**.
3. On the **Global networks** page, choose the global network ID that for the core network you want to create a policy version for, and then choose **Core network**.
4. In the navigation pane, choose **Policy versions**.
5. Choose **Create policy version**.
6. Choose  **Segment actions - optional**.


###### Note

You must first have created your segments and network functions
 group.
7. If you want to create a service insertion action associated with a network
 functions group in the **Service insertion** section, choose
 **Create**, and then choose an **Action**.
 If you're not creating a service insertion action, this is an optional
 section.



Send via 
This **Action** uses an east-west traffic pattern
 from attachment to attachment. For example, you might create a
 policy that directs all traffic between a segment named
 *Production* and all other segments via
 inspection VPC attachments.




	1. For the **Mode**, choose one of the
	 following:
	
	
	
	
		* **Single hop** — This option steers
		 traffic through a single intermediate attachment.
		* **Dual hop** — Traffic traverses
		 the inserted attachments in both the source and
		 destination core network edges.
	2. For **Segment from**, choose the source
	 segment.
	3. For **Segment to**, choose the
	 destination segments.
	4. For **Send traffic via**, choose the
	 network functions group that you want to use for the service
	 insertion.
	5. (Optional) In **Edge overrides**, choose
	 **Add**.
	
	
	
	
		* From the **Edge 1** and
		 **Edge 2** drop-down lists,
		 choose the edge locations for the overrides. the
		 service the priority order for the edge locations
		 to route traffic.
		* Choose the **Preferred edge**
		 drop-down list to choose which edge location you
		 prefer to use.
		* Choose **Add** to include
		 additional edge overrides.

Send to 
This **Action** uses north-south traffic, sending
 traffic to the security appliance, such as an Inspection VPC or
 firewall, and then out to the Internet or an on-premises
 location.




	1. For **Segment from**, choose the segment
	 coming into the security appliance. For example, you might
	 have a segment named *production* that
	 you want to first go to a security appliance.
	2. For **Send traffic via**, choose the
	 network functions group that you want to use for the service
	 insertion.
	3. Optional) In **Edge overrides**, choose
	 **Add**.
	
	
	
	
		* From the **Edge 1** and
		 **Edge 2** drop-down lists,
		 choose the edge locations for the overrides. the
		 service the priority order for the edge locations
		 to route traffic.
		* Choose the **Preferred edge**
		 drop-down list to choose which edge location you
		 prefer to use.
		* + Choose **Add** to include
			 additional edge overrides.
8. Choose **Create service insertion**.
9. (Optional) Add **Attachment policies**. For more information,
 see [Create an attachment policy in an AWS Cloud WAN core
 network policy version](cloudwan-policy-attachments.md "cloudwan-policy-attachments.md").
