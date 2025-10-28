# Data layer

The data layer of your hybrid networking environment is important
because it provides a data path for network traffic between
applications hosted on AWS and an on-premises data center. As part
of your hybrid deployment, it’s important to carefully consider
the hybrid connectivity options between AWS and an on-premises
data for the forwarding of your network traffic. The Hybrid
Networking Lens recommends using AWS Virtual Private Network (AWS VPN), AWS Direct Connect, and Amazon VPC to support your
application team’s agility and speed to market by using AWS as a
data center extension. AWS VPN and Direct Connect are used as
network paths for providing connectivity for these hybrid
networking workloads.

**AWS Virtual Private Network**
(AWS VPN) establishes a secure and private tunnel from your
network or device to the AWS Cloud. AWS Site-to-Site VPN
allows you to securely connect your on-premises network or
branch office site to your Amazon VPC.

**AWS Direct Connect** (DX) makes
it easy to establish a dedicated network connection from your
on-premises environment to AWS. Using Direct Connect, you can
establish private connectivity between AWS and your data center,
office, or colocation environment. In many cases, this can reduce
your network costs, increase bandwidth throughput, and provide a
more consistent network experience than internet-based
connections.

A **virtual private gateway** (VGW)
is part of a VPC that provides edge routing for AWS managed VPN
connections and Direct Connect connections. You associate a Direct
Connect gateway with the virtual private gateway for the VPC.

**AWS Transit Gateway** (TGW)
connects VPCs and on-premises networks through a central hub. It
is a fully managed AWS gateway that acts as a cloud router and
enables rich routing scenarios. With AWS Transit Gateway, you can
quickly add Amazon VPCs, AWS accounts, VPN capacity, or AWS Direct Connect gateways to meet unexpected demand, without having to
wrestle with complex connections or massive routing tables.
