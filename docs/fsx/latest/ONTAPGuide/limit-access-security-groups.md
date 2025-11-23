# File System Access Control with Amazon VPC

You access your Amazon FSx for NetApp ONTAP file systems and SVMs using the DNS name or the IP address
of one of their endpoints, depending on what type of access it is. The DNS name maps to the private
IP address of the file system's or SVM's elastic network interface in your VPC. Only resources within
the associated VPC, or resources connected with the associated VPC by Direct Connect or VPN, can access
the data in your file system over the NFS, SMB, or iSCSI protocols. For more information,
see [What is
Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the _Amazon VPC User Guide._

###### Warning

You must not modify or delete the elastic network interface(s) associated with your file system.
Modifying or deleting the network interface can cause a permanent loss of connection between your VPC and your file system.

## Amazon VPC security groups

A security group acts as a virtual firewall for your FSx for ONTAP file systems to
control incoming and outgoing traffic. Inbound rules control the incoming traffic to
your file system, and outbound rules control the outgoing traffic from your file system.
When you create a file system, you specify the VPC that it gets created in, and the default
security group for that VPC is applied. You can add rules to each security group that
allow traffic to or from its associated file systems and SVMs. You can modify the rules
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
Group Rules](../../../AWSEC2/latest/UserGuide/using-network-security.md#security-group-rules "../../../AWSEC2/latest/UserGuide/using-network-security.md#security-group-rules") in the _Amazon EC2 User Guide._

### Creating a VPC security group

###### To create a security group for Amazon FSx

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. In the navigation pane, choose **Security
   Groups**.
3. Choose **Create Security Group**.
4. Specify a name and description for the security group.
5. For **VPC**, choose the Amazon VPC associated with your file
   system to create the security group within that VPC.
6. For outbound rules, allow all traffic on all ports.
7. Add the following rules to the inbound ports of your security group.
   For the **source** field, you should choose **Custom**
   and enter the security groups or IP address ranges associated with the instances
   that need to access your FSx for ONTAP file system, including:
   - Linux, Windows, and/or macOS clients that access data in your
     file system over NFS, SMB, or iSCSI.
   - Any ONTAP file systems/clusters that you will peer to your
     file system (for example, to use SnapMirror, SnapVault, or FlexCache).
   - Any clients that you will use to access the ONTAP REST API, CLI,
     or ZAPIs (for example, a Harvest/Grafana instance, NetApp Connector, or
     NetApp Console).

| Protocol | Ports   | Role                                                                                           |
| -------- | ------- | ---------------------------------------------------------------------------------------------- |
| All ICMP | All     | Pinging the instance                                                                           |
| SSH      | 22      | SSH access to the IP address of the cluster management LIF or a node management LIF            |
| TCP      | 111     | Remote procedure call for NFS                                                                  |
| TCP      | 135     | Remote procedure call for CIFS                                                                 |
| TCP      | 139     | NetBIOS service session for CIFS                                                               |
| TCP      | 161-162 | Simple network management protocol (SNMP)                                                      |
| TCP      | 443     | ONTAP REST API access to the IP address of the cluster management LIF or an SVM management LIF |
| TCP      | 445     | Microsoft SMB/CIFS over TCP with NetBIOS framing                                               |
| TCP      | 635     | NFS mount                                                                                      |
| TCP      | 749     | Kerberos                                                                                       |
| TCP      | 2049    | NFS server daemon                                                                              |
| TCP      | 3260    | iSCSI access through the iSCSI data LIF                                                        |
| TCP      | 4045    | NFS lock daemon                                                                                |
| TCP      | 4046    | Network status monitor for NFS                                                                 |
| TCP      | 10000   | Network data management protocol (NDMP) and NetApp SnapMirror intercluster<br>communication    |
| TCP      | 11104   | Management of NetApp SnapMirror intercluster communication                                     |
| TCP      | 11105   | SnapMirror data transfer using intercluster LIFs                                               |
| UDP      | 111     | Remote procedure call for NFS                                                                  |
| UDP      | 135     | Remote procedure call for CIFS                                                                 |
| UDP      | 137     | NetBIOS name resolution for CIFS                                                               |
| UDP      | 139     | NetBIOS service session for CIFS                                                               |
| UDP      | 161-162 | Simple network management protocol (SNMP)                                                      |
| UDP      | 635     | NFS mount                                                                                      |
| UDP      | 2049    | NFS server daemon                                                                              |
| UDP      | 4045    | NFS lock daemon                                                                                |
| UDP      | 4046    | Network status monitor for NFS                                                                 |
| UDP      | 4049    | NFS quota protocol                                                                             |

8. Add the security group to the file system's elastic network interface.

#### Disallow access to a file system

To temporarily disallow network access to your file system from all clients, you can remove all the security groups associated with your
file system's elastic network interface(s) and replace them with a group that has no inbound/outbound rules.
