# Accessing your data from on-premises

FSx for OpenZFS supports the use of AWS Direct Connect or AWS VPN to access your file
systems from your on-premises compute instances. Using AWS Direct Connect, you access your file system over a
dedicated network connection from your on-premises environment. Using AWS VPN, you access your file system
from your on-premises devices over a secure and private tunnel.

After you connect your on-premises environment to the VPC associated with your Amazon FSx file system,
you can access your file system using its DNS name or a DNS alias. You do so just as you do from
compute instances within the VPC. For more information about AWS Direct Connect, see
[What is AWS Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")
in the _AWS Direct Connect User Guide_. For more information on setting up AWS VPN connections,
see [VPN connections](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md") in the _Amazon VPC User Guide_.

###### Topics

- [Accessing Multi-AZ file systems](#access-multi-az-fs "#access-multi-az-fs")

## Accessing Multi-AZ file systems

Amazon FSx requires that you use AWS Transit Gateway to access Multi-AZ file systems from an
on-premises network. In order to support failover across AZs for Multi-AZ file
systems, Amazon FSx uses floating IP addresses for the interfaces used for NFS endpoints. Because the NFS endpoints use floating IPs, you must use [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/transit-gateway/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc") in conjunction with AWS Direct Connect or AWS VPN to access
these interfaces from an on-premises network. The floating IP addresses used for
these interfaces are within the endpoint IP address range you specify
when creating your Multi-AZ file system. By default, the Amazon FSx API selects a CIDR block of 16 available addresses from within the VPC's CIDR ranges.
The floating IP addresses are used to enable a seamless transition of your clients to the
standby file system in the event a failover is required. For more information,
see [Failover process for FSx for OpenZFS](availability-durability.md#multi-az-failover "availability-durability.md#multi-az-failover").

If you have a Multi-AZ file system with an endpoint IP address range
that's outside your VPC's CIDR range, you need to set up additional routing
in your AWS Transit Gateway to access your file system from peered or on-premises networks.
For information, see [Configuring routing using
AWS Transit Gateway](access-within-aws.md#configuring-routing-using-AWSTG "access-within-aws.md#configuring-routing-using-AWSTG").
