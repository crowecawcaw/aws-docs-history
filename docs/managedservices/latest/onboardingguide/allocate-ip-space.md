# Allocate IP Space for your AMS Environment

AMS was designed and tested using a /16 CIDR block as the recommended network allocation. It is important that the
trusted network connected to AMS use a CIDR block that does not overlap with the CIDR block assigned to AMS.
These addresses are required to set up your virtual private cloud (VPC) and subnets. For more information about AWS VPCs,
see [Amazon VPC Limits](../../../AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.md "../../../AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.md") and
[Amazon VPC FAQs](https://aws.amazon.com/vpc/faqs/ "https://aws.amazon.com/vpc/faqs/").

While a /16 CIDR block may seem like a lot of IP addresses, a VPC, once created, cannot be expanded. So this allocation
ensures that your AMS-managed VPC can function for a considerable period. Within the CIDR block, you must allocate
IP address ranges for, at least, two private subnets and two public subnets.

AWS accepts connectivity to the AMS environment via native AWS virtual private network (VPN)
functionality. On your side, this can be achieved via AWS Direct Connect (DX), hardware
VPN, or software VPN. On the AMS side, we use the Virtual Gateway functionality of VPCs.

| Basic Environment Components | User Network-to-Amazon VPC Connectivity Options                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hardware VPN**             | Establishes a hardware VPN connection from your network equipment on a remote network to AMS-managed network equipment attached to your VPC.           |
| **AWS Direct Connect (DX)**  | Establishes a private, logical (or encrypted if used with a VPN) connection from your remote network to the Amazon VPC, leveraging AWS Direct Connect. |
| **Software VPN**             | Establishes a VPN connection from your equipment on a remote network to a user-managed software VPN appliance running inside an Amazon VPC.            | ###### Note AMS recommends redundant private VPN to DX connections. Your customer service delivery manager (CSDM) will assist in setting this up at the time of onboarding your account. |
