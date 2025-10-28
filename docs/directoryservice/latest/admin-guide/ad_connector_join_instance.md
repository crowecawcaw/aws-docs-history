# Ways to join an Amazon EC2 instance to your Active Directory

AD Connector is a directory gateway with which you can redirect directory requests to your
on-premises Microsoft Active Directory without caching any information in the cloud. Here's more information on
how you can join an Amazon EC2 to an Active Directory domain:

- You can seamlessly join an Amazon EC2 instance to your Active Directory domain when the instance is
  launched. For more information on joining an EC2 Windows instance to an AWS Managed Microsoft AD, see [Joining an Amazon EC2 Windows instance to your AWS Managed Microsoft AD
  Active Directory](launching_instance.md "launching_instance.md").
- If you need to manually join an EC2 instance to your Active Directory domain, you must launch the
  instance in the proper AWS Region and security group or subnet, then join the instance to
  the Active Directory domain.
- To be able to connect remotely to these instances, you must have IP connectivity to the
  instances from the network you are connecting from. In most cases, this requires that an
  internet gateway be attached to your Amazon VPC and that the instance has a public IP address.
  For more information about connecting to the internet using an internet gateway see [Connect to the
  internet using an internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the Amazon VPC User Guide.

###### Note

Once you join an instance to your self-managed Active Directory (on-premises), the instance
communicates directly with your Active Directory and bypasses AD Connector.
