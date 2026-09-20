

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).

# Deploy a default Amazon EC2 host for FSx File Gateway
<a name="ec2-quicklaunch-settings"></a>

This topic lists the steps to deploy an Amazon EC2 host using the default specifications.

You can deploy and activate an Amazon FSx File Gateway on an Amazon Elastic Compute Cloud (Amazon EC2) instance. The AWS Storage Gateway Amazon Machine Image (AMI) is available as a community AMI.

**Note**  
Storage Gateway community AMIs are published and fully supported by AWS. You can see that the publisher is AWS, a verified provider.

1. To set up the Amazon EC2 instance, choose **Amazon EC2** as the **Host platform** in the **Platform options** section of the workflow. For instructions on configuring the Amazon EC2 instance, see [Deploying an Amazon EC2 instance to host your Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/ec2-gateway-file.html).

1. Select **Launch instance** to open the AWS Storage Gateway AMI template in the Amazon EC2 console and customize additional settings such as **Instance types**, **Network settings** and **Configure storage**.

1. Optionally, you can select **Use default settings** in the Storage Gateway console to deploy an Amazon EC2 instance with the default configuration.

   The Amazon EC2 instance that **Use default settings** creates has the following default specifications:
   + **Instance type** — *m5.xlarge*
   + **Network Settings**
     + For **VPC**, select the VPC that you want your EC2 instance to run in.
     + For **Subnet**, specify the subnet that your EC2 instance should be launched in.
**Note**  
VPC subnets will appear in the drop down only if they have the auto-assign public IP address setting activated from the VPC management console.
     + **Auto-assign Public IP** — *Activated*
     + An EC2 security group is created and associated with the EC2 Instance. The security group has the following inbound port rules:
**Note**  
You will need Port 80 open during gateway activation. The port is closed immediately following activation. Thereafter, your EC2 instance can only be accessed over the other ports from the selected VPC.   
 The file shares on your gateway are only accessible from the hosts in the same VPC as the gateway. If the file shares need to be accessed from hosts outside of the VPC, you should update the appropriate security group rules.   
 You can edit security groups at any time by navigating to the Amazon EC2 instance details page, selecting **Security**, navigating to **Security group details**, and choosing the security group ID. 


<table>
<thead>
  <tr><th><b>Port</b></th><th><b>Protocol</b></th><th><b>File System Protocol</b></th><th></th><th></th><th></th><th></th></tr>
</thead>
<tbody>
  <tr><td>80</td><td>TCP</td><td>HTTP access for activation</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>137</td><td>UDP</td><td>NetBIOS</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>138</td><td>UDP</td><td>NetBIOS</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>139</td><td>TCP, UDP</td><td>SMB</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>389</td><td>TCP</td><td>LDAP</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>445</td><td>TCP</td><td>SMB</td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>

   + **Configure storage**


<table>
<thead>
  <tr><th><b>Default Settings</b></th><th><b>AMI Root Volume</b></th><th><b>Volume 2 Cache</b></th><th></th><th></th><th></th><th></th></tr>
</thead>
<tbody>
  <tr><td>Device Name</td><td></td><td>'/dev/sdb'</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Size</td><td>80 Gib</td><td>165 GiB</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Volume Type</td><td>gp3</td><td>gp3</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>IOPS</td><td>3000</td><td>3000</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Delete on termination</td><td>Yes</td><td>Yes</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Encrypted</td><td>No</td><td>No</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Throughput</td><td>125</td><td>125</td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>
