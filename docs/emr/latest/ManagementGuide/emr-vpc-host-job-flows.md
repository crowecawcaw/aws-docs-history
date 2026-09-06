

# Set up a VPC to host Amazon EMR clusters
<a name="emr-vpc-host-job-flows"></a>

Before you can launch clusters in a VPC, you must create a VPC and a subnet. For public subnets, you must create an internet gateway and attach it to the subnet. The following instructions describe how to create a VPC capable of hosting Amazon EMR clusters. 

**To create a VPC with subnets for an Amazon EMR cluster**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the top-right of the page, choose the [AWS Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) for your VPC.

1. Choose **Create VPC**.

1. On the **VPC settings** page, choose **VPC and more**.

1. Under **Name tag auto-generation**, enable **Auto-generate** and enter a name for your VPC. This helps you to identify the VPC and subnet in the Amazon VPC console after you've created them.

1. In the **IPv4 CIDR block** field, enter a private IP address space for your VPC to ensure proper DNS hostname resolution; otherwise, you may experience Amazon EMR cluster failures. This includes the following IP address ranges: 
   + 10.0.0.0 - 10.255.255.255
   + 172.16.0.0 - 172.31.255.255
   + 192.168.0.0 - 192.168.255.255

1. Under **Number of Availability Zones (AZs)**, choose the number of Availability Zones you want to launch your subnets in.

1. Under **Number of public subnets**, choose a single public subnet to add to your VPC. If the data used by the cluster is available on the internet (for example, in Amazon S3 or Amazon RDS), you only need to use a public subnet and don't need to add a private subnet.

1. Under **Number of private subnets**, choose the number of private subnets you want to add to your VPC. Select one or more if the the data for your application is stored in your own network (for example, in an Oracle database). For a VPC in a private subnet, all Amazon EC2 instances must at minimum have a route to Amazon EMR through the elastic network interface. In the console, this is automatically configured for you.

1. Under **NAT gateways**, optionally choose to add NAT gateways. They are only necessary if you have private subnets that need to communicate with the internet.

1. Under **VPC endpoints**, optionally choose to add endpoints for Amazon S3 to your subnets.

1. Verify that **Enable DNS hostnames** and**Enable DNS resolution** are checked. For more information, see [Using DNS with your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html).

1. Choose **Create VPC**.

1. A status window shows the work in progress. When the work completes, choose **View VPC** to navigate to the **Your VPCs** page, which displays your default VPC and the VPC that you just created. The VPC that you created is a nondefault VPC, therefore the **Default VPC** column displays **No**. 

1. If you want to associate your VPC with a DNS entry that does not include a domain name, navigate to **DHCP option sets**, choose **Create DHCP options set**, and omit a domain name. After you create your option set, navigate to your new VPC, choose **Edit DHCP options set** under the **Actions** menu, and select the new option set. You cannot edit the domain name using the console after the DNS option set has been created. 

   It is a best practice with Hadoop and related applications to ensure resolution of the fully qualified domain name (FQDN) for nodes. To ensure proper DNS resolution, configure a VPC that includes a DHCP options set whose parameters are set to the following values:
   + **domain-name** = **ec2.internal**

     Use **ec2.internal** if your Region is US East (N. Virginia). For other Regions, use {{region-name}}**.compute.internal**. For examples in `us-west-2`, use **us-west-2.compute.internal**. For the AWS GovCloud (US-West) Region, use **us-gov-west-1.compute.internal**.
   + **domain-name-servers** = **AmazonProvidedDNS**

   For more information, see [DHCP options sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.

1. After the VPC is created, go to the **Subnets** page and note the **Subnet ID** of one of the subnets of your new VPC. You use this information when you launch the Amazon EMR cluster into the VPC.