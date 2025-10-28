# VPN connection in Local Zones

A VPN connection can provide secure, two-way communication between workloads running in an
on-premises data center and a Local Zone. For Local Zones, you must deploy a software-based VPN solution on
an Amazon EC2 instance. Visit the [AWS Marketplace](https://aws.amazon.com/marketplace/search/results/ref=brs_navgno_search_box?searchTerms=vpn "https://aws.amazon.com/marketplace/search/results/ref=brs_navgno_search_box?searchTerms=vpn") and find VPN solutions that are ready to run on an Amazon EC2 instance.
You’ll also need to deploy an internet gateway so that you can establish your VPN
connection.

The following diagram shows a data center connected to Local Zone 1 by a software-based VPN
solution running on an Amazon EC2 instance in Local Zone 1. This allows for encrypted connectivity from the
data center directly into the Local Zone without traffic going through the parent Region.

![An AWS Region with a VPC. The VPC contains two Availability Zones and a Local Zone. Each zone has a public subnet and a private subnet. The diagram also shows an on-premise data center with a customer gateway outside the AWS Region. The public subnet in the Local Zone includes a software-based VPN solution. The VPC has an internet gateway through which traffic flows between the public subnet in the Local Zone to a customer data center.](images/local-zone-on-premise-vpn.png)
