# Managing file system access with with Amazon VPC

You access your Amazon FSx for OpenZFS file systems and volumes using the file system's DNS name. The DNS name maps to the private
IP address of the file system's elastic network interface in your VPC. Only resources within
the associated VPC, or resources connected with the associated VPC by AWS Direct Connect or VPN, can access
the data in your file system over the NFS protocol. For more information,
see [What is
Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the _Amazon VPC User Guide._

###### Warning

You must not modify or delete the elastic network interface(s) associated with your file system.
Modifying or deleting the network interface can cause a permanent loss of connection between your VPC and your file system.

## Amazon VPC security groups

A security group acts as a virtual firewall for your FSx for OpenZFS file systems to
control incoming and outgoing traffic. Inbound rules control the incoming traffic to
your file system, and outbound rules control the outgoing traffic from your file system.
When you create a file system, you specify the VPC that it gets created in, and the default
security group for that VPC is applied. You can add rules to each security group that
allow traffic to or from its associated file systems and volumes. You can modify the rules
for a security group at any time. New and modified rules are automatically applied to all
resources that are associated with the security group. When Amazon FSx decides whether to allow
traffic to reach a resource, it evaluates all of the rules from all of the security groups
that are associated with the resource.

To use a security group to control access to your Amazon FSx file system, add inbound
and outbound rules. Inbound rules control incoming traffic, and outbound rules
control outgoing traffic from your file system. Make sure that you have the right
network traffic rules in your security group to map your Amazon FSx file system's file
share to a folder on your supported compute instance.

For more information on security group rules, see [Security
Group Rules](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#security-group-rules.html "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md#security-group-rules.html") in the _Amazon EC2 User Guide._

### Creating a VPC security group

###### To create a security group for Amazon FSx

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. In the navigation pane, choose **Security
   Groups**.
3. Choose **Create Security Group**.
4. Specify a name and description for the security group.
5. For **VPC**, choose the Amazon VPC associated with your file
   system to create the security group within that VPC.
6. Remove any outbound rules on the security group. FSx for OpenZFS file systems
   do not initiate outbound connections in your VPC.
7. Add the following rules to the inbound ports of your security group.

| Protocol | Ports            | Role                                       |
| -------- | ---------------- | ------------------------------------------ |
| TCP      | 111              | Remote procedure call for NFS              |
| UDP      | 111              | Remote procedure call for NFS              |
| TCP      | 2049             | NFS server daemon                          |
| UDP      | 2049             | NFS server daemon                          |
| TCP      | 20001<br>• 20003 | NFS mount, status monitor, and lock daemon |
| UDP      | 20001<br>• 20003 | NFS mount, status monitor, and lock daemon |

#### Disallow access to a file system

To temporarily disallow network access to your file system from all clients, you can remove all the security groups associated with your
file system's elastic network interface(s) and replace them with a group that has no inbound/outbound rules.
