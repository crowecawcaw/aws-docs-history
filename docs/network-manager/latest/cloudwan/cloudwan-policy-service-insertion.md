# AWS Cloud WAN service insertion

Service insertion allows you to steer same-segment or cross-segment traffic using network
 functions deployed in VPCs or on-premises networks attached to Cloud WAN. Network functions
 can be third-party network or security appliances such as NGFW, IDS, IPS appliances or
 native AWS network firewall or Gateway Load Balancer services. Using either the AWS Network Manager
 console or a JSON file, you'll create a version of one of your core network policies, create
 a network function group that contains a set of core network attachments where your network
 functions reside, and specify a segment or segment pairs for which traffic needs to be
 redirected to those network functions. Once the policy version is deployed and your new core
 network LIVE, Cloud WAN will automatically redirect network traffic between the segments to
 the specified core network attachments for the respective network function group. This
 redirection works for both same Region and cross-Region traffic on the core network. Service
 insertion works on both east-west (VPC to VPC) and north-south (VPC to the Internet or
 on-premises location) traffic. 

To create a core network that includes service insertion, you'll need to do the
 following:


1. **Create a policy version of a current policy**. The initial
 policy you deploy when you create your first core network doesn't include any
 service insertion features. To do this you'll create a version of an existing policy
 and add the service insertion features. You can do this using either the AWS Network Manager
 console or through a JSON file. 


You can create a policy version containing the service insertion action using
 either the AWS Network Manager console or through creating a JSON file which you can also
 create using the console: 




	* To create a policy version using the console, see [Create an AWS Cloud WAN core network policy version
	 using the console](cloudwan-create-policy-console.md "cloudwan-create-policy-console.md").
	* To create a policy version using a JSON file, see [Create an AWS Cloud WAN core network policy version using JSON](cloudwan-create-policy-json.md "cloudwan-create-policy-json.md").
2. Using either the console or within the JSON file you'll do the following:




	1. **Configure your core network**. Set the BGP and ASN for
	 this core network policy.
	2. **Add segments**. Add segments to your core network
	 policy. Segments with cross-segment or same-segment traffic that must be
	 steered via the network functions. Based on your policy configuration, Cloud
	 WAN will automatically propagate routes from VPCs and networks associated to
	 the network function groups and redirect VPC-to-VPC or VPC-to-Internet or
	 on-premises traffic through a network functions group.
	3. **Create a network function group**. The network function
	 group is a collection of attachments specifically used for network or
	 security functions. 
	
	
	###### Note
	
	You can only have one attachment per network function group per
	 Region.
	4. **Set segment actions**. Segment actions allow you to
	 share segments, create routes, and create a service insertion action.
	
	
	For the service insertion action, you can create a send via action which
	 sends traffic east-west between all VPCs. Or you can create a send to
	 action, which first sends traffic to a security appliance and then out from
	 the appliance. For example, you might create segment action using send via.
	 With send via (east-west traffic), traffic is routed to the Inspection VPC
	 for security processing and then re-enters the Cloud WAN core network to
	 reach its final VPC destination. See [Traffic actions and
	 modes](#cloudwan-policy-service-insertion-modes "#cloudwan-policy-service-insertion-modes") below for more
	 information about traffic actions and modes.
	
	
	By default, Cloud WAN will select an attachment in one of the two Regions
	 used for the network function. For example, if the network function is
	 steering traffic to an Inspection VPC, and that Inspection VPC exists in
	 only one Region, Cloud WAN uses the Region where the Inspection VPC resides
	 to steer all cross-Region traffic. If the Inspection VPC exists in both
	 Regions, service insertion will deterministically choose which Region to use
	 based on the default Region priority list. However, when setting the segment
	 actions, you can choose the Region priority order as well as choose the
	 preferred Region to use. If the Inspection VPC doesn't exist in either
	 Region, Cloud WAN uses the fallback Region specified in the segment policy.
	 You can only specific a single fallback Region per segment policy.
	5. **Create an attachment policy for the network function
	 group**. Add the network function group to an attachment
	 policy. The attachment policy then controls the order in which the network
	 function group runs.
3. Deploy the policy version. See [Deploy an AWS Cloud WAN core network policy version](cloudwan-policy-version-deploy.md "cloudwan-policy-version-deploy.md").

## Benefits



* **Simplified routing** — Service insertion allows for more
 simplified routing. You might need inter-VPC or VPC to internet or on-premises
 traffic to be routed through network appliances, such as network firewalls or
 load balancers. With Cloud WAN service insertion you can more easily steer
 network traffic to network or security appliances deployed in VPCs or in
 on-premises. This allows you to create and manage sometimes complex routing
 configurations or third-party automation tools.
* **Ease of deploying multi-Region inspection** — You might
 deploy Cloud WAN in multi-Region networks to support Region expansion or
 disaster recovery use cases. Service insertion simplifies mutli-Region
 deployment, allowing you to steer both intra-Region and inter-Region traffic
 through your security infrastructure without having to set up complex
 multi-Region network configurations.

## Traffic actions and
 modes


Service insertion supports the following traffic actions and modes for both east-west
 and north-south traffic.



* Send via — Traffic flows east-west between VPCs. All traffic for the service
 insertion action is first sent via a specific segment to the security appliance
 and then out to other VPCs.




	+ Single hop — Traffic traverses a single intermediate attachment, using
	 the deterministically preferred source or destination Region. You can
	 set a list of Regions to use, as well as setting a preferred Region to
	 use as a priority.
	+ Dual hop — Traffic traverses inserted attachments in both the source
	 and destination core network edges. For this option, the inspection
	 attachment should be located in both Regions for each service
	 insertion-enabled segment.
* Send to — Traffic flows north-south. That is, traffic flows into the network
 appliance, such as an Inspection VPC, and out to the Internet or to an
 on-premises location. Traffic does not re-enter the AWS cloud.

## Attachments


Within a network function group you can specify a set of core network attachments
 where your network functions will reside. For example, the attachment might be a VPC
 that you use for inspection. You'll then add a segment or segment pair to this
 attachment that will be redirected to the network functions group and then to the
 security appliance. Cloud WAN automatically redirects traffic on any segment you add to
 that VPC when creating a service insertion action to that group both in the same Region
 and cross-Region within the core network.


In order to make an attachment be part of the network function group correctly,
 service insertion relies on the key-value pair tags added to an attachment. When
 creating an attachment you'll need to add the relevant tag to each attachment. For
 example, you might want to use a particular attachment as an Inspection VPC. You could
 add a tag with the key name *Inspection VPC* and then a key value of
 *InspectionVpcs*. The same tag should be applied to any
 attachment you add to that network function group. When you create a service insertion
 function, you'll add an attachment policy rule that relies on the key tags and values
 added to those attachments in order to process the tag key. In this example, you'd add a
 policy rule that identifies the tag *Inspection VPC* and the key
 value of *InspectionVpcs*. Attachment policy rules can be created
 using either the AWS Cloud WAN console or through a JSON file. For the steps for either method,
 see [Attachment policies](cloudwan-create-policy-version.md#cloudwan-policy-create-attachment "cloudwan-create-policy-version.md#cloudwan-policy-create-attachment").


###### Important

A network function group need not be associated with an attachment in order for the
 attachment policy to succeed. If you specify segment actions of
 **send-to** or **send-via** to a network
 function group with no attachments associated to it, the Cloud WAN policy
 execution will still be successful; however, all traffic destined to that network
 function group will be blackholed until you associate attachments to that group in
 appropriate Regions.


The following are the supported core network attachments:



* Connect
* Direct Connect gateway
* Transit gateway route table
* VPC
* VPN

## Considerations



* **Attachments** — You can associate an attachment either with
 a segment or with a network function group, but it can't be associated with
 both.
* **Isolated mode** — Isolated mode is required for service
 insertion to work between attachments belonging to the same segment. This
 setting ensures there is no direct connectivity between attachments associated
 with the same segment by bypassing the network functions group.
* **Appliance mode** — Appliance mode must be enabled on the
 Inspection VPC to ensure that traffic moves in both directions.
* **Route propagation** — Static routes defined in your Cloud WAN policy are not automatically propagated to Network Function Group route tables. Route propagation to NFGs requires specific configuration in your policy to define which routes should be available to the network functions.

## Pricing


There are no additional charges for using service insertion other than the standard
 AWS Cloud WAN pricing charges. Information about Cloud WAN pricing can be found here: [AWS Cloud WAN Pricing](https://aws.amazon.com/cloud-wan/pricing/ "https://aws.amazon.com/cloud-wan/pricing/").
