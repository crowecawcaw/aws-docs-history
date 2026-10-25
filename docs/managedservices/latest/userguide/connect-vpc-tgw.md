

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Connecting a new VPC to the shared Transit Gateway
<a name="connect-vpc-tgw"></a>

When you create an account and VPC yourself, you configure Transit Gateway connectivity directly instead of through a managed request. The following AWS Command Line Interface (AWS CLI) procedure reproduces the connectivity that the Create application account (with VPC) change type previously configured. The procedure attaches the VPC, associates it with a route domain, applies your `routable` or `isolated` choice, and adds the routes that preserve shared-services, egress, and on-premises connectivity in both directions. It then points the VPC's subnet route tables at the Transit Gateway and verifies the result.

## Which account to use for each step
<a name="connect-vpc-tgw-accounts"></a>

The AWS Transit Gateway is created in the networking account and shared with your application account through AWS Resource Access Manager (AWS RAM). The work therefore spans two accounts:


| Task | Account | Why | 
| --- | --- | --- | 
| Create the VPC attachment (Step 1) | Application account (owns the VPC and subnets) | The attachment references your VPC and subnets. | 
| Associate the attachment to a route domain, create the Transit Gateway routes in both directions, and check the AWS Direct Connect advertisement (Steps 2–7) | Networking account (owns the Transit Gateway and its route tables) | Only the Transit Gateway owner can associate route tables and create routes. | 
| Point the VPC subnet route tables at the Transit Gateway, then verify and test (Steps 8–9) | Application account (owns the VPC route tables and instances) | Subnet route tables and the test instances are in your VPC. | 

Run each command with credentials for the account named in each step.

**Note**  
Your application account doesn't have its own Transit Gateway, and it doesn't need one. Your multi-account landing zone has a single Transit Gateway in the networking account, shared with your entire organization by default through AWS Resource Access Manager (AWS RAM). Confirm that you can see it by running `aws ec2 describe-transit-gateways` in your application account.

**Important**  
The Transit Gateway is shared with the organization, not with individual accounts. Your new application account must be created inside the same AWS Organizations as the networking account. Otherwise, Step 1 fails because the shared Transit Gateway is not visible to the account.

## Prerequisites
<a name="connect-vpc-tgw-prerequisites"></a>

Before you begin, make sure that you have the following:
+ A nonoverlapping Classless Inter-Domain Routing (CIDR) block for the VPC in your application account, from your existing landing-zone address plan or Amazon VPC IP Address Manager (IPAM).
+ The shared Transit Gateway ID (`tgw-...`). Confirm it's visible by running `aws ec2 describe-transit-gateways` in your application account.
+ Credentials for both the application account and the networking account.
+ The name of the route domain (route table) to join, which is the value you would have provided for `TransitGatewayApplicationRouteTableName`.
+ Your choice of `RouteType`: `routable` or `isolated`.
+ The on-premises CIDR ranges, from your network team, if your landing zone has an on-premises connection. Needed for Steps 6 and 7.
+ To run the connectivity test in Step 9: an Amazon EC2 instance in your new VPC and an instance in a VPC already attached to the same route domain, with security groups that allow Internet Control Message Protocol (ICMP) between them.

The procedure uses the following placeholders.


| Placeholder | Meaning | How to obtain | 
| --- | --- | --- | 
| `tgw-id` | Shared Transit Gateway ID | `aws ec2 describe-transit-gateways --query 'TransitGateways[].TransitGatewayId'` (application account) | 
| `vpc-id` | Your application VPC ID | `aws ec2 describe-vpcs` (application account) | 
| `subnet-id-az-a subnet-id-az-b` | One subnet per Availability Zone (AZ) for the attachment elastic network interfaces (ENIs) | `aws ec2 describe-subnets --filters Name=vpc-id,Values=vpc-id` | 
| `app-cidr` | The VPC CIDR to advertise, for example `10.20.0.0/16` | `aws ec2 describe-vpcs --vpc-ids vpc-id --query 'Vpcs[0].CidrBlock'` | 
| `attachment-id` | The Transit Gateway VPC attachment ID | Output of Step 1 | 
| `app-route-domain-name` | The application route domain name (same as `TransitGatewayApplicationRouteTableName`) | The route table's `Name` tag; default `defaultAppRouteDomain` | 
| `app-route-table-id` | The route table ID for the application route domain | Output of Step 2 | 
| `onprem-cidr` | An on-premises CIDR range reachable through the Transit Gateway, for example `192.168.0.0/16` (repeat Step 6 for each range) | Your network team | 
| `onprem-test-ip` | Any single IP address inside `onprem-cidr`, used to test route resolution | Your network team | 
| `onprem-attachment-id` | The Direct Connect or VPN attachment that carries on-premises traffic | Output of the first command in Step 6 | 
| `dxgw-id` | Direct Connect gateway ID, if connectivity is through Direct Connect | `aws directconnect describe-direct-connect-gateways` (networking account) | 
| `lz-cidr` | The destination range to reach through the Transit Gateway (for example, your landing-zone supernet such as `10.0.0.0/8`, or `0.0.0.0/0`) | Your network design | 
| `vpc-route-table-id` | A subnet route table ID in your VPC | `aws ec2 describe-route-tables --filters Name=vpc-id,Values=vpc-id` (application account) | 
| `peer-private-ip` | Private IP of an instance in a peer VPC, for the Step 9 test | From the peer instance | 

## Connect the VPC to the Transit Gateway
<a name="connect-vpc-tgw-procedure"></a>

Run each command with credentials for the account named in each step.

1. Create the VPC attachment (application account). The shared Transit Gateway accepts attachments automatically, so you don't need a separate acceptance step.

   ```
   aws ec2 create-transit-gateway-vpc-attachment \
     --transit-gateway-id {{tgw-id}} \
     --vpc-id {{vpc-id}} \
     --subnet-ids {{subnet-id-az-a}} {{subnet-id-az-b}} \
     --query 'TransitGatewayVpcAttachment.TransitGatewayAttachmentId' --output text
   ```

   Wait until the attachment state is `available` before continuing:

   ```
   aws ec2 describe-transit-gateway-attachments \
     --transit-gateway-attachment-ids {{attachment-id}} \
     --query 'TransitGatewayAttachments[0].State' --output text
   ```

1. Get the application route table ID (networking account).

   ```
   aws ec2 describe-transit-gateway-route-tables \
     --filters Name=transit-gateway-id,Values={{tgw-id}} \
               Name=tag:Name,Values={{app-route-domain-name}} \
     --query 'TransitGatewayRouteTables[?State==`available`].TransitGatewayRouteTableId | [0]' --output text
   ```
**Note**  
The Core, DMZ, Egress, and on-premises route domains have the fixed names `CoreRouteDomain`, `DMZBastionsRouteDomain`, `EgressRouteDomain`, and `OnPremiseRouteDomain`. Application route domains do not: the default is `defaultAppRouteDomain`, but your landing zone might have several. List all route domains and their names by running `aws ec2 describe-transit-gateway-route-tables` in the networking account.
**Important**  
If your landing zone segments application traffic across multiple application route domains (for example, separate route domains for production and non-production), identify the route domain matching the segment this VPC belongs to, and use its ID for every following step. Placing a VPC in the wrong application route domain grants it the wrong peer connectivity.

1. Associate the attachment with the route domain (networking account). An attachment can be associated with only one route table.

   ```
   aws ec2 associate-transit-gateway-route-table \
     --transit-gateway-route-table-id {{app-route-table-id}} \
     --transit-gateway-attachment-id {{attachment-id}}
   ```

1. Add the VPC route in the route domain (networking account). This is the only step affected by your `RouteType` choice.

   For `routable`, create a route to the attachment so that other VPCs in the domain can reach the VPC:

   ```
   aws ec2 create-transit-gateway-route \
     --transit-gateway-route-table-id {{app-route-table-id}} \
     --destination-cidr-block {{app-cidr}} \
     --transit-gateway-attachment-id {{attachment-id}}
   ```

   For `isolated`, create a blackhole route so that other VPCs in the domain can't reach the VPC:

   ```
   aws ec2 create-transit-gateway-route \
     --transit-gateway-route-table-id {{app-route-table-id}} \
     --destination-cidr-block {{app-cidr}} \
     --blackhole
   ```

1. Add the VPC route to the Core, DMZ, Egress, and on-premises domains (networking account). These routes allow shared services, the DMZ, the egress VPC, and on-premises networks to send traffic to your VPC. They are the same regardless of `RouteType`. Run the following command once per domain, using the route table ID for each (get each ID with the route table command in the preceding step and the domain's name).

   ```
   aws ec2 create-transit-gateway-route \
     --transit-gateway-route-table-id {{route-table-id}} \
     --destination-cidr-block {{app-cidr}} \
     --transit-gateway-attachment-id {{attachment-id}}
   ```

1. Add the on-premises routes to the application route domain (networking account). Complete this step only if your landing zone has a Direct Connect or VPN connection to an on-premises environment.

   The preceding step allows on-premises networks to reach your VPC. This step allows your VPC to reach your on-premises network. Transit Gateway routing is directional: traffic leaving your VPC is routed by the application route domain, so that route domain needs a route for each on-premises CIDR range.
**Note**  
These routes are shared by every VPC in the application route domain, so they might already exist. Verify before you create them.

   First, get the ID of the Direct Connect or VPN attachment.

   ```
   aws ec2 describe-transit-gateway-attachments \
     --filters Name=transit-gateway-id,Values={{tgw-id}} \
               Name=resource-type,Values=vpn,direct-connect-gateway \
     --query 'TransitGatewayAttachments[].{Id:TransitGatewayAttachmentId,Type:ResourceType}'
   ```

   Next, check which route the application route domain currently uses for an on-premises address.

   ```
   aws ec2 search-transit-gateway-routes \
     --transit-gateway-route-table-id {{app-route-table-id}} \
     --filters Name=route-search.longest-prefix-match,Values={{onprem-test-ip}} \
     --query 'Routes[].{Cidr:DestinationCidrBlock,State:State,Attachment:TransitGatewayAttachments[0].TransitGatewayAttachmentId}'
   ```

   If the result is a route for your on-premises CIDR range that targets the attachment you found earlier, the routes already exist and you can skip the rest of this step. If the only result is `0.0.0.0/0`, continue.

   Create a route for each on-premises CIDR range.
**Note**  
For customers using a standalone customer Active Directory account architecture, replace `onprem-cidr` with the standalone customer Active Directory account VPC CIDR, and replace `onprem-attachment-id` with the standalone customer Active Directory account transit gateway attachment ID.

   ```
   aws ec2 create-transit-gateway-route \
     --transit-gateway-route-table-id {{app-route-table-id}} \
     --destination-cidr-block {{onprem-cidr}} \
     --transit-gateway-attachment-id {{onprem-attachment-id}}
   ```
**Important**  
If you skip this step, traffic from your VPC to the on-premises environment matches the `0.0.0.0/0` route to the egress VPC and is discarded. Connections time out without a routing error.

1. Confirm your VPC CIDR is advertised to the on-premises environment (networking account). Skip this step if your landing zone connects to an on-premises environment over VPN rather than Direct Connect.

   The Transit Gateway's association with a Direct Connect gateway carries an allowed-prefixes list, and on-premises routers learn only the prefixes on that list over Border Gateway Protocol (BGP). If `app-cidr` is not covered by an allowed prefix, the on-premises environment cannot reach your VPC even though the preceding step succeeded.

   ```
   aws directconnect describe-direct-connect-gateway-associations \
     --direct-connect-gateway-id {{dxgw-id}} \
     --query 'directConnectGatewayAssociations[].{State:associationState,Allowed:allowedPrefixesToDirectConnectGateway}'
   ```

   If `app-cidr` is not inside one of the listed prefixes, extend the list with `update-direct-connect-gateway-association`. Prefer widening to your landing-zone supernet over adding one prefix per VPC, because the list is limited to 20 prefixes.

1. Point the VPC subnet route tables at the Transit Gateway (application account). Traffic leaves your VPC through the Transit Gateway only if the VPC's subnet route tables have a route to it. For each subnet route table that needs landing-zone connectivity, add a route whose destination is the range you want to reach through the Transit Gateway and whose target is the Transit Gateway. Repeat for each subnet route table.

   ```
   aws ec2 create-route \
     --route-table-id {{vpc-route-table-id}} \
     --destination-cidr-block {{lz-cidr}} \
     --transit-gateway-id {{tgw-id}}
   ```

   `lz-cidr` must also cover your on-premises ranges. If any on-premises prefix falls outside your landing-zone supernet, add a separate `create-route` for it with the same Transit Gateway target.

1. Verify and test. Confirm the attachment is associated with the expected route domain (networking account):

   ```
   aws ec2 describe-transit-gateway-attachments \
     --transit-gateway-attachment-ids {{attachment-id}} \
     --query 'TransitGatewayAttachments[0].Association'
   ```

   Confirm the route for your VPC CIDR in the route domain. The state is `active` for `routable`, or `blackhole` for `isolated` (networking account):

   ```
   aws ec2 search-transit-gateway-routes \
     --transit-gateway-route-table-id {{app-route-table-id}} \
     --filters Name=route-search.exact-match,Values={{app-cidr}} \
     --query 'Routes[].{Cidr:DestinationCidrBlock,State:State,Type:Type}'
   ```

   If your landing zone connects to an on-premises environment, confirm both directions of on-premises routing. First confirm the inbound half. Confirm that `app-cidr` is `active` in `OnPremiseRouteDomain` (networking account). Repeat for `CoreRouteDomain`, `DMZBastionsRouteDomain`, and `EgressRouteDomain`:

   ```
   aws ec2 search-transit-gateway-routes \
     --transit-gateway-route-table-id {{onprem-route-table-id}} \
     --filters Name=route-search.exact-match,Values={{app-cidr}} \
     --query 'Routes[].{Cidr:DestinationCidrBlock,State:State,Type:Type}'
   ```

   Then confirm the outbound half. The application route domain's longest-prefix match for an on-premises address must point to the Direct Connect or VPN attachment, not to `0.0.0.0/0` (networking account):

   ```
   aws ec2 search-transit-gateway-routes \
     --transit-gateway-route-table-id {{app-route-table-id}} \
     --filters Name=route-search.longest-prefix-match,Values={{onprem-test-ip}} \
     --query 'Routes[].{Cidr:DestinationCidrBlock,State:State,Attachment:TransitGatewayAttachments[0].TransitGatewayAttachmentId}'
   ```

   Test end-to-end connectivity (application account). Connect to an Amazon EC2 instance in your new VPC and ping the private IP address of an instance in a VPC attached to the same route domain:

   ```
   ping {{peer-private-ip}}
   ```

   If your VPC is `routable` and the peer is in the same route domain, the ping succeeds. If your VPC is `isolated`, the ping fails by design, because its CIDR is a blackhole in the route domain. Connectivity to shared services, egress, and the on-premises environment continues to work.

   Test on-premises connectivity in both directions: from an instance in your VPC to an on-premises host, and from an on-premises host to an instance in your VPC. A route that is missing in only one direction appears only when you test both directions.

1. (Optional) Point the VPC to Active Directory DNS (application account). Complete this step only if your landing zone uses the Active Directory from your AMS landing zone for Amazon EC2 access.

   Create a DHCP option set with the Active Directory domain name and the domain controller addresses, then associate it with your VPC. Get both values by running `aws ds describe-directories` in the account that hosts the directory.

   ```
   aws ec2 create-dhcp-options \
     --dhcp-configurations "Key=domain-name,Values=[{{ad-domain}}]" \
                           "Key=domain-name-servers,Values=[{{dc-ip-1}},{{dc-ip-2}}]" \
     --query 'DhcpOptions.DhcpOptionsId' --output text
   ```

   ```
   aws ec2 associate-dhcp-options \
     --dhcp-options-id {{dhcp-options-id}} \
     --vpc-id {{vpc-id}}
   ```

   Match the option set your existing application accounts use, so the new account resolves names the same way they do.
**Note**  
Instances that are already running keep their current DNS settings until they renew their DHCP lease or reboot.

   If your landing zone shares Amazon Route 53 Resolver rules from the account that hosts the directory, associate each shared rule with your VPC. Because the rules are shared with the organization, run these commands in the application account to create the association.

   ```
   aws route53resolver list-resolver-rules \
     --query 'ResolverRules[?ShareStatus==`SHARED_WITH_ME`].{Id:Id,Name:Name,Domain:DomainName}'
   ```

   ```
   aws route53resolver associate-resolver-rule \
     --resolver-rule-id {{resolver-rule-id}} \
     --vpc-id {{vpc-id}} \
     --name {{association-name}}
   ```

   Confirm resolution from an instance in your VPC:

   ```
   nslookup {{ad-domain}}
   nslookup {{onprem-ad-domain}}
   ```