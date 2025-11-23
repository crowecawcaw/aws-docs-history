# Transit gateway connection in

Local Zones

A transit gateway connects your Amazon Virtual Private Cloud and on-premises networks through a central hub. Transit
gateways live in AWS Regions. While you can use a transit gateway to connect data centers to a
Local Zone, this is not a direct connection.

For more information about transit gateways, see [Connect your VPC to other VPCs and networks using a
transit gateway](../../../vpc/latest/userguide/extend-tgw.md "../../../vpc/latest/userguide/extend-tgw.md") in the _Amazon VPC User Guide_.

The following diagram shows the connection from the customer gateway over the Direct Connect
into the transit gateway in the AWS Region using a Transit VIF. From there, it connects to the
VPC to enable traffic to the Local Zone.

![An AWS Region with a VPC. The VPC contains an Availability Zone and a Local Zone. Each zone has a private subnet. The diagram also shows an on-premise data center with a customer gateway outside the AWS Region. Traffic between the private subnet in the Local Zone and the customer gateway traverses through a transit gateway in the AWS Region, a Transit VIF, the Direct Connect connection.](images/local-zones-internet-gateway2.png)
When you use this connectivity option for Local Zones, all traffic from the data center to the
Local Zone will first go to the parent Region (also known as “hairpinning”) of the destination Local Zone and
then to the Local Zone. Using a transit gateway to connect to a Local Zone from your premises is not an ideal
path since your data must travel to the Region first, increasing latency.
