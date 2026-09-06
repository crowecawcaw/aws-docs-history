

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# VPN Setup
<a name="vpn-setup"></a>

This section describes the basic steps for setting up a VPN to communicate between your AMS-managed VPC and your internal network.

**Note**  
To gain overall understanding about using a VPN with AWS services refer to [What is AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) and all about [Your Customer Gateway](https://docs.aws.amazon.com/vpc/latest/adminguide/Introduction.html) (your VPN appliance).

Follow the AWS VPN User Guide [Getting Started](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html) and [Testing the Site-to-Site VPN Connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/HowToTestEndToEnd_Linux.html) sections to complete the following steps.
+ Step 1: In your AWS VPC, Create a Customer Gateway
+ Step 2: In your AWS VPC, Create a Virtual Private Gateway
+ Step 3: In your AWS VPC, Enable Route Propagation in Your Route Table
+ Step 4: In your AWS VPC, Update Your Security Group to Enable Inbound SSH, RDP, and ICMP Access
+ Step 5: In your internal Network, Create a VPN Connection and Configure the Customer Gateway
+ Step 6: Test VPN connectivity between the VPC and your internal network