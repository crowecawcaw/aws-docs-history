

# Ways to join an Amazon EC2 instance to your Simple AD
<a name="simple_ad_join_instance"></a>

**Important Notice**  
Simple AD is no longer open to new customers. For capabilities similar to Simple AD, explore AWS Managed Microsoft AD or AD Connector. For more information, see [Simple AD availability changes](simple-ad-availability-change.md).

You can seamlessly join an Amazon EC2 instance to your Active Directory domain when the instance is launched. For more information, see [Joining an Amazon EC2 Windows instance to your AWS Managed Microsoft AD Active Directory](launching_instance.md). You can also launch an EC2 instance and join it to an Active Directory domain directly from the Directory Service console with [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html).

If you need to manually join an EC2 instance to your Active Directory domain, you must launch the instance in the proper Region and security group or subnet, then join the instance to the domain.

To be able to connect remotely to these instances, you must have IP connectivity to the instances from the network you are connecting from. In most cases, this requires that an internet gateway be attached to your VPC and that the instance has a public IP address.

**Topics**
+ [Joining an Amazon EC2 Windows instance to your Simple AD Active Directory](simple_ad_launching_instance.md)
+ [Join an Amazon EC2 Linux instance to your Simple AD Active Directory](simple_ad_linux_domain_join.md)
+ [Delegating directory join privileges for Simple AD](simple_ad_directory_join_privileges.md)
+ [Creating a DHCP options set for Simple AD](simple_ad_dhcp_options_set.md)