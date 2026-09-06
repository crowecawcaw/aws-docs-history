

# Network configuration port rules
<a name="custom-sqlserver-WinAuth.NWConfigPorts"></a>

Make sure that you have met the following network configurations:
+ Connectivity configured between the Amazon VPC where you want to create the RDS Custom for SQL Server DB instance to either your self-managed Active Directory or AWS Managed Microsoft AD. For self-managed Active Directory, set up connectivity using AWS Direct Connect, AWS VPN, VPC peering, or AWS Transit Gateway. For AWS Managed Microsoft AD, set up connectivity using VPC peering.
+ Make sure that the security group and the VPC network ACLs for the subnet(s) where you're creating your RDS Custom for SQL Server DB instance allow traffic on the ports and in the directions shown in the following diagram.  
![Microsoft Active Directory network configuration port rules.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/custom_sqlserver_ActiveDirectory_Requirements_NetworkConfig.png)

  The following table identifies the role of each port.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.NWConfigPorts.html)
+ Generally, the domain DNS servers are located in the AD domain controllers. You do not need to configure the VPC DHCP option set to use this feature. For more information, see [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.

**Important**  
If you're using VPC network ACLs, you must also allow outbound traffic on dynamic ports (49152-65535) from your RDS Custom for SQL Server DB instance. Ensure that these traffic rules are also mirrored on the firewalls that apply to each of the AD domain controllers, DNS servers, and RDS Custom for SQL Server DB instances.  
While VPC security groups require ports to be opened only in the direction that network traffic is initiated, most Windows firewalls and VPC network ACLs require ports to be open in both directions.