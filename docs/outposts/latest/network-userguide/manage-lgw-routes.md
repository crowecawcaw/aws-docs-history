# Local gateway route table routes

You can create local gateway route tables and inbound routes to network interfaces on your
Outpost. You can also modify an existing local gateway inbound route to change the target
network interface.

A route is in **active** status only when its target network interface is
attached to a running instance. If the instance is stopped or the interface is detached, the
route status changes from **active** to
**blackhole**.

###### Contents

- [Requirements and limitations](#lgw-requirements-limitations "#lgw-requirements-limitations")
- [Create custom local gateway route tables](#create-lgw-route-table "#create-lgw-route-table")
- [Switch local gateway route table modes or delete a local
  gateway route table](#switch-modes "#switch-modes")

## Requirements and limitations

The following requirements and limitations apply:

- The target network interface must belong to a subnet on your Outpost and must be
  attached to an instance in that Outpost. A local gateway route can't target an Amazon EC2
  instance on a different Outpost or in the parent AWS Region.
- The subnet must belong to a VPC that is associated to the local gateway route table.
- You must not exceed more than 100 network interface routes in the same route
  table.
- AWS prioritizes the most specific route, and if the routes match, we prioritize
  static routes over propagated routes.
- Interface VPC endpoints are not supported.
- BGP advertisement is only for subnets on an Outpost that have a route in the route
  table that targets the local gateway. If subnets do not have a route in the route table
  that targets the local gateway, then those subnets are not advertised with BGP.
- Only network interfaces that are attached to Outpost instances can communicate
  through the local gateway for that Outpost. Network interfaces that belong to the
  Outpost subnet but attached to an instance in the Region can't communicate through the
  local gateway for that Outpost.
- Requester-managed interfaces, such as those created for VPC endpoints, can't be
  reached from the on-premises network through the local gateway. They can be reached only
  from instances that are in the Outpost subnet.

The following NAT considerations apply:

- The local gateway does not perform NAT on traffic that matches an network interface
  route. Instead, the destination IP address is preserved.
- Turn off source/destination checking for the target network interface. For more
  information, see [Network interface
  concepts](../../../AWSEC2/latest/UserGuide/using-eni.md#eni-basics "../../../AWSEC2/latest/UserGuide/using-eni.md#eni-basics") in the _Amazon EC2 User Guide_.
- Configure the operating system to allow traffic from the destination CIDR to be
  accepted on the network interface.

## Create custom local gateway route tables

You can create a custom route table for your local gateway using the AWS Outposts
console.

###### To create a custom local gateway route table using the console

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of the
   page.
3. On the navigation pane, choose **Local gateway route
   table**.
4. Choose **Create local gateway route table**.
5. (Optional) For **Name**, enter a name for your local gateway route
   table.
6. For **Local gateway**, choose your local gateway.
7. (Optional) Choose **Associate VIF group** and choose your
   **VIF group**.

Edit the local gateway route table to add a static route that has the VIF Group as
the target. 8. For **Mode**, choose a mode for communication with your on-premises
network.

    * Choose **Direct VPC routing** to use the private IP address of
     an instance.
    * Choose **CoIP** to use the customer-owned IP address.




    	+ (Optional) Add or remove CoIP pools and additional CIDR blocks


    	[Add a CoIP pool] Choose **Add new pool** and do the
    	 following:




    		- For **Name**, enter a name for your CoIP pool.
    		- For **CIDR**, enter a CIDR block of customer-owned IP
    		 addresses.
    	+ [Add CIDR blocks] Choose **Add new CIDR** and enter a range
    	 of customer-owned IP addresses.
    	+ [Remove a CoIP pool or an additional CIDR block] Choose
    	 **Remove** to the right of a CIDR block or below the CoIP
    	 pool.


    	You can specify up to 10 CoIP pools and 100 CIDR blocks.

9. (Optional) Add or remove a tag.

[Add a tag] Choose **Add new tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.

[Remove a tag] Choose **Remove** to the right of the tag’s key and
value. 10. Choose **Create local gateway route table**.

## Switch local gateway route table modes or delete a local

gateway route table

You must delete and recreate the local gateway route table to switch modes. Deleting the
local gateway route table causes network traffic interruption.

###### To switch modes or delete a local gateway route table

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. Verify that you are in the correct AWS Region.

To change the Region, use the Region selector in the top-right corner of the
page. 3. On the navigation pane, choose **Local gateway route
tables**. 4. Verify if the local gateway route table is associated with a VIF group. If it is
associated, you must remove the association between the local gateway route table and
the VIF group.

    1. Choose the ID of the local gateway route table.
    2. Choose the **VIF group association** tab.
    3. If one or more VIF groups are associated with the local gateway route table,
     choose **Edit VIF group association**.
    4. Clear the **Associate VIF group** checkbox.
    5. Choose **Save changes**.

5. Choose **Delete local gateway route table**.
6. In the confirmation dialog box, type `delete` and then choose
   **Delete**.
7. (Optional) Create a local gateway route table with a new mode.
   1. On the navigation pane, choose **Local gateway route
      tables**.
   2. Choose **Create local gateway route table**.
   3. Configure the local gateway route table using the new mode. For more
      information, see [Create custom local gateway
      route tables](#create-lgw-route-table "#create-lgw-route-table").
