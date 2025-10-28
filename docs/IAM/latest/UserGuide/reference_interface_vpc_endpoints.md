# Interface VPC endpoints

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private
connection between your VPC and AWS Identity and Access Management (IAM) or AWS Security Token Service (AWS STS). You can use this
connection to enable IAM or AWS STS to communicate with your resources in your VPC without going
through the public internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network
that you define. With a VPC, you have control over your network settings, such as the IP address
range, subnets, route tables, and network gateways. To connect your VPC to IAM or AWS STS, you
define an _interface VPC endpoint_ for each service. The endpoint provides
reliable, scalable connectivity to IAM or AWS STS without requiring an internet gateway, network
address translation (NAT) instance, or VPN connection. For more information, see [What Is Amazon VPC?](../../../vpc/latest/userguide/VPC_Introduction.md "../../../vpc/latest/userguide/VPC_Introduction.md") in the _Amazon VPC User Guide_.

Interface VPC endpoints are powered by AWS PrivateLink an AWS technology that enables
private communication between AWS services using an elastic network interface with private IP
addresses. For more information, see [AWS PrivateLink for AWS Services](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md").

The following information is for users of Amazon VPC. For more information, see [Getting Started with Amazon VPC](../../../vpc/latest/userguide/GetStarted.md "../../../vpc/latest/userguide/GetStarted.md") in the _Amazon VPC User Guide_.

###### Topics

- [VPC endpoint availability](#reference_vpc_endpoint_availability "#reference_vpc_endpoint_availability")
- [Create a VPC endpoint for IAM](reference_iam_vpc_endpoint_create.md "reference_iam_vpc_endpoint_create.md")
- [Create a VPC endpoint for AWS STS](reference_sts_vpc_endpoint_create.md "reference_sts_vpc_endpoint_create.md")

## VPC endpoint availability

###### Important

Interface VPC endpoints for IAM can only be created in the Region where the [IAM control plane](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md") is located. If your VPC
is in a different Region from the IAM control plane Region, you must use AWS Transit Gateway to
allow access to the IAM interface VPC endpoint from another Region. For more information,
see [Create a VPC endpoint for IAM](reference_iam_vpc_endpoint_create.md "reference_iam_vpc_endpoint_create.md").

IAM currently supports VPC endpoints in the following Regions:

- US East (N. Virginia)
- China (Beijing)
- AWS GovCloud (US-West)

AWS STS currently supports VPC endpoints in the following Regions:

- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)
- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Hyderabad)
- Asia Pacific (Jakarta)
- Asia Pacific (Melbourne)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Canada West (Calgary)
- China (Beijing)
- China (Ningxia)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Milan)
- Europe (Paris)
- Europe (Spain)
- Europe (Stockholm)
- Europe (Zurich)
- Israel (Tel Aviv)
- Middle East (Bahrain)
- Middle East (UAE)
- South America (São Paulo)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)
