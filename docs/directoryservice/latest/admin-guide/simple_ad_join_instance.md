# Ways to join an Amazon EC2 instance to your

Simple AD

You can seamlessly join an Amazon EC2 instance to your Active Directory domain when the instance is
launched. For more information, see [Joining an Amazon EC2 Windows instance to your AWS Managed Microsoft AD
Active Directory](launching_instance.md "launching_instance.md"). You can also
launch an EC2 instance and join it to an Active Directory domain directly from the Directory Service console with
[AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md").

If you need to manually join an EC2 instance to your Active Directory domain, you must launch the instance
in the proper Region and security group or subnet, then join the instance to the
domain.

To be able to connect remotely to these instances, you must have IP connectivity to the
instances from the network you are connecting from. In most cases, this requires that an
internet gateway be attached to your VPC and that the instance has a public IP
address.

###### Topics

- [Joining an Amazon EC2 Windows instance to your
  Simple AD Active Directory](simple_ad_launching_instance.md "simple_ad_launching_instance.md")
- [Join an Amazon EC2 Linux instance to
  your Simple AD Active Directory](simple_ad_linux_domain_join.md "simple_ad_linux_domain_join.md")
- [Delegating directory join privileges for
  Simple AD](simple_ad_directory_join_privileges.md "simple_ad_directory_join_privileges.md")
- [Creating a DHCP options set for
  Simple AD](simple_ad_dhcp_options_set.md "simple_ad_dhcp_options_set.md")
