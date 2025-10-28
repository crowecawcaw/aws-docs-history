# Overlay IP Routing with Network Load Balancer

If you do not use Amazon Route 53 or AWS Transit Gateway, you can use [Network Load Balancer](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md") for accessing the overlay IP address externally. The Network Load Balancer functions at the fourth layer of the Open Systems Interconnection (OSI) model. It can handle millions of requests per second. After the load balancer receives a connection request, it selects a target from the Network Load Balancer target group to route network connection request to a destination address which can be an overlay IP address.

## Architecture

The following figure shows the network access flow of ASCS or SAP HANA overlay IP from outside the VPC.

**Figure 6: SAP High Availability with Overlay IP and Elastic Load Balancer**

![SAP High Availability with Overlay IP and Elastic Load Balancer](images/ha-overlay-ip-image6.png)

_Pricing for Network Load Balancers_:

With Network Load Balancers, you only pay for what you use. See [Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/"), for more information.
