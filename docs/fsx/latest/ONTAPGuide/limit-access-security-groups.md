

# File System Access Control with Amazon VPC
<a name="limit-access-security-groups"></a>

You access your Amazon FSx for NetApp ONTAP file systems and SVMs using the DNS name or the IP address of one of their endpoints, depending on what type of access it is. The DNS name maps to the private IP address of the file system's or SVM's elastic network interface in your VPC. Only resources within the associated VPC, or resources connected with the associated VPC by Direct Connect or VPN, can access the data in your file system over the NFS, SMB, or iSCSI protocols. For more information, see [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in the * Amazon VPC User Guide.* 

**Warning**  
You must not modify or delete the elastic network interface(s) associated with your file system. Modifying or deleting the network interface can cause a permanent loss of connection between your VPC and your file system.

## Amazon VPC security groups
<a name="fsx-vpc-security-groups"></a>

A security group acts as a virtual firewall for your FSx for ONTAP file systems to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your file system, and outbound rules control the outgoing traffic from your file system. When you create a file system, you specify the VPC that it gets created in, and the default security group for that VPC is applied. You can add rules to each security group that allow traffic to or from its associated file systems and SVMs. You can modify the rules for a security group at any time. New and modified rules are automatically applied to all resources that are associated with the security group. When Amazon FSx decides whether to allow traffic to reach a resource, it evaluates all of the rules from all of the security groups that are associated with the resource.

 To use a security group to control access to your Amazon FSx file system, add inbound and outbound rules. Inbound rules control incoming traffic, and outbound rules control outgoing traffic from your file system. Make sure that you have the right network traffic rules in your security group to map your Amazon FSx file system's file share to a folder on your supported compute instance. 

For more information on security group rules, see [Security Group Rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#security-group-rules) in the *Amazon EC2 User Guide.*

### Creating a VPC security group
<a name="create-security-group"></a>

**To create a security group for Amazon FSx**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2).

1. In the navigation pane, choose **Security Groups**.

1. Choose **Create Security Group**.

1. Specify a name and description for the security group.

1. For **VPC**, choose the Amazon VPC associated with your file system to create the security group within that VPC.

1. For outbound rules, allow all traffic on all ports.

1. Add the following rules to the inbound ports of your security group. For the **source** field, you should choose **Custom** and enter the security groups or IP address ranges associated with the instances that need to access your FSx for ONTAP file system, including:
   + Linux, Windows, and/or macOS clients that access data in your file system over NFS, SMB, or iSCSI.
   + Any ONTAP file systems/clusters that you will peer to your file system (for example, to use SnapMirror, SnapVault, or FlexCache).
   + Any clients that you will use to access the ONTAP REST API, CLI, or ZAPIs (for example, a Harvest/Grafana instance, NetApp Connector, or NetApp Console).


<table>
<thead>
  <tr><th>Protocol</th><th>Ports</th><th>Role</th></tr>
</thead>
<tbody>
  <tr><td>All ICMP</td><td>All</td><td>Pinging the instance</td></tr>
  <tr><td>SSH</td><td>22</td><td>SSH access to the IP address of the cluster management LIF or a node management LIF</td></tr>
  <tr><td>TCP</td><td>111</td><td>Remote procedure call for NFS</td></tr>
  <tr><td>TCP</td><td>135</td><td>Remote procedure call for CIFS</td></tr>
  <tr><td>TCP</td><td>139</td><td>NetBIOS service session for CIFS</td></tr>
  <tr><td>TCP</td><td>161-162</td><td>Simple network management protocol (SNMP)</td></tr>
  <tr><td>TCP</td><td>443</td><td>ONTAP REST API access to the IP address of the cluster management LIF or an SVM management LIF</td></tr>
  <tr><td>TCP</td><td>445</td><td>Microsoft SMB/CIFS over TCP with NetBIOS framing</td></tr>
  <tr><td>TCP</td><td>635</td><td>NFS mount</td></tr>
  <tr><td>TCP</td><td>749</td><td>Kerberos</td></tr>
  <tr><td>TCP</td><td>2049</td><td>NFS server daemon</td></tr>
  <tr><td>TCP</td><td>3260</td><td>iSCSI access through the iSCSI data LIF</td></tr>
  <tr><td>TCP</td><td>4045</td><td>NFS lock daemon</td></tr>
  <tr><td>TCP</td><td>4046</td><td>Network status monitor for NFS</td></tr>
  <tr><td>TCP</td><td>10000</td><td>Network data management protocol (NDMP) and NetApp SnapMirror intercluster communication</td></tr>
  <tr><td>TCP</td><td>11104</td><td>Management of NetApp SnapMirror intercluster communication</td></tr>
  <tr><td>TCP</td><td>11105</td><td>SnapMirror data transfer using intercluster LIFs</td></tr>
  <tr><td>UDP</td><td>111</td><td>Remote procedure call for NFS</td></tr>
  <tr><td>UDP</td><td>135</td><td>Remote procedure call for CIFS</td></tr>
  <tr><td>UDP</td><td>137</td><td>NetBIOS name resolution for CIFS</td></tr>
  <tr><td>UDP</td><td>139</td><td>NetBIOS service session for CIFS</td></tr>
  <tr><td>UDP</td><td>161-162</td><td>Simple network management protocol (SNMP)</td></tr>
  <tr><td>UDP</td><td>635</td><td>NFS mount</td></tr>
  <tr><td>UDP</td><td>2049</td><td>NFS server daemon</td></tr>
  <tr><td>UDP</td><td>4045</td><td>NFS lock daemon</td></tr>
  <tr><td>UDP</td><td>4046</td><td>Network status monitor for NFS</td></tr>
  <tr><td>UDP</td><td>4049</td><td>NFS quota protocol</td></tr>
</tbody>
</table>


1. Add the security group to the file system's elastic network interface.

#### Disallow access to a file system
<a name="disallow-access"></a>

 To temporarily disallow network access to your file system from all clients, you can remove all the security groups associated with your file system's elastic network interface(s) and replace them with a group that has no inbound/outbound rules. 