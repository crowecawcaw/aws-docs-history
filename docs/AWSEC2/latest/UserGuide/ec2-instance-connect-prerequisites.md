# Prerequisites for

EC2 Instance Connect

###### The following are the prerequisites for installing and using

EC2 Instance Connect:

- [Install EC2 Instance Connect](#eic-prereqs-install-eic-on-instance "#eic-prereqs-install-eic-on-instance")
- [Ensure network connectivity](#eic-prereqs-network-access "#eic-prereqs-network-access")
- [Allow inbound SSH
  traffic](#ec2-instance-connect-setup-security-group "#ec2-instance-connect-setup-security-group")
- [Grant permissions](#eic-prereqs-grant-permissions "#eic-prereqs-grant-permissions")
- [Install an SSH client on your local
  computer](#eic-prereqs-install-ssh-client "#eic-prereqs-install-ssh-client")
- [Meet username requirements](#eic-prereqs-username "#eic-prereqs-username")

## Install EC2 Instance Connect

To use EC2 Instance Connect to connect to an instance, the instance must have
EC2 Instance Connect installed. You can either launch the instance using an AMI that comes
pre-installed with EC2 Instance Connect, or you can install EC2 Instance Connect on instances that
are launched with supported AMIs. For more information, see [Install EC2 Instance Connect on your EC2
instances](ec2-instance-connect-set-up.md "ec2-instance-connect-set-up.md").

## Ensure network connectivity

Instances can be configured to allow users to connect to your instance over the
internet or through the instance's private IP address. Depending on how your users
will connect to your instance using EC2 Instance Connect, you must configure the following
network access:

- If your users will connect to your instance over the internet, then your instance must
  have a public IPv4 or IPv6 address and be in a public subnet with a route to
  the internet. If you haven't modified your default public subnet, then it
  contains a route to the internet for IPv4 only, and not for IPv6. For more
  information, see [Enable VPC internet access using internet gateways](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#vpc-igw-internet-access "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#vpc-igw-internet-access") in the
  _Amazon VPC User Guide_.
- If your users will connect to your instance through the instance's private
  IPv4 address, then you must establish private network connectivity to your
  VPC, such as by using AWS Direct Connect, AWS Site-to-Site VPN, or VPC peering, so that your
  users can reach the instance's private IP address.

If your instance does not have a public IPv4 or IPv6 address and you prefer not to
configure the network access as described above, you can consider EC2 Instance Connect Endpoint as
an alternative to EC2 Instance Connect. With EC2 Instance Connect Endpoint, you can connect to an instance
using SSH or RDP even if the instance does not have a public IPv4 or IPv6 address.
For more information, see [Connect to your Linux instance using
the Amazon EC2 console](connect-using-eice.md#connect-using-the-ec2-console "connect-using-eice.md#connect-using-the-ec2-console").

## Allow inbound SSH

traffic

###### When using the Amazon EC2 console to connect to an instance

When users connect to an instance using the Amazon EC2 console, the traffic that must be
allowed to reach the instance is traffic from the EC2 Instance Connect service. The
service is identified by specific IP address ranges, which AWS manages through
prefix lists. You must create a security group that allows inbound SSH traffic
from the EC2 Instance Connect service. To configure this, for the inbound rule, in the
field next to **Source**, select the EC2 Instance Connect prefix
list.

AWS provides different managed prefix lists for IPv4 and IPv6 addresses for each Region.
The names of the EC2 Instance Connect prefix lists are as follows, with
`region` replaced by the Region code:

- IPv4 prefix list name:
  `com.amazonaws.`region`.ec2-instance-connect`
- IPv6 prefix list name:
  `com.amazonaws.`region`.ipv6.ec2-instance-connect`

For the instructions for creating the security group, see [Task 2: Allow inbound traffic from the
EC2 Instance Connect service to your instance](ec2-instance-connect-tutorial.md#eic-tut1-task2 "ec2-instance-connect-tutorial.md#eic-tut1-task2"). For more information, see [Available AWS-managed prefix lists](../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md#available-aws-managed-prefix-lists "../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md#available-aws-managed-prefix-lists") in the _Amazon VPC User Guide_.

###### When using the CLI or SSH to connect to an instance

Ensure that the security group associated with your instance [allows inbound SSH traffic](security-group-rules-reference.md#sg-rules-local-access "security-group-rules-reference.md#sg-rules-local-access") on port 22
from your IP address or from your network. The default security group for the
VPC does not allow incoming SSH traffic by default. The security group created
by the launch instance wizard allows incoming SSH traffic by default. For more
information, see [Rules to connect to instances from your computer](security-group-rules-reference.md#sg-rules-local-access "security-group-rules-reference.md#sg-rules-local-access").

## Grant permissions

You must grant the required permissions to every IAM user who will use
EC2 Instance Connect to connect to an instance. For more information, see [Grant IAM permissions for
EC2 Instance Connect](ec2-instance-connect-configure-IAM-role.md "ec2-instance-connect-configure-IAM-role.md").

## Install an SSH client on your local

computer

If your users will connect using SSH, they must ensure that their local computer
has an SSH client.

A user's local computer most likely has an SSH client installed by default. They
can check for an SSH client by typing **ssh** at the command line. If
their local computer doesn't recognize the command, they can install an SSH client.
For information about installing an SSH client on Linux or macOS X, see [http://www.openssh.com](http://www.openssh.com/ "http://www.openssh.com/"). For information
about installing an SSH client on Windows 10, see [OpenSSH in Windows](https://learn.microsoft.com/en-us/windows-server/administration/OpenSSH/openssh-overview "https://learn.microsoft.com/en-us/windows-server/administration/OpenSSH/openssh-overview").

There is no need to install an SSH client on a local computer if your users use
only the Amazon EC2 console to connect to an instance.

## Meet username requirements

When using EC2 Instance Connect to connect to an instance, the username must meet the
following requirements:

- First character: Must be a letter (`A-Z`, `a-z`), a
  digit (`0-9`), or an underscore (`_`)
- Subsequent characters: Can be letters (`A-Z`,
  `a-z`), digits (`0-9`), or the following characters:
  `@ . _ -`
- Minimum length: 1 character
- Maximum length: 31 characters
