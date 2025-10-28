# Internet gateway connection in Local Zones

Internet gateways provide two-way public connectivity to applications running in
AWS Regions and/or in Local Zones. For more information, see [Internet gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the
_Amazon VPC User Guide_.

In the following diagram, end users access a public-facing application in Local Zone 1. Traffic
goes directly to the internet gateway in Local Zone 1 without going through the parent AWS Region.
Use this type of connectivity for low-latency use-cases where you want your public-facing
applications to be closer to end users than an AWS Region can provide.

![An AWS Region with a VPC. The VPC contains two Availability Zones and a Local Zone. Each zone has a public subnet and a private subnet. The VPC also has an internet gateway through which traffic passes between an application in the public subnet of the Local Zone and the end user.](images/local-zones-internet-gateway.png)
For your private applications that require outbound-only connectivity to the internet, use a
NAT gateway.
