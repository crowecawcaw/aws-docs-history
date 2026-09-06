

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Troubleshooting communication errors
<a name="Troubleshooting-Communication-Errors"></a>

Use the information in this section to troubleshoot communication errors.

**Topics**
+ [Solving communication problems over TCP Port 443 between the staging area and the AWS Transform MGN](#Solving-Communication-Problems)
+ [Authenticate with service errors](#Authenticate-With-Service-Errors)
+ [Calculating the required bandwidth for TCP Port 1500](#Calculating-Bandwidth)
+ [Verifying communication over Port 1500](#Verifying-Communication-1500)
+ [Solving communication problems over Port 1500](#Solving-Problems-1500)
+ [Missing Amazon Linux 2023 repository access](#missing-al2023-repo-access)

## Solving communication problems over TCP Port 443 between the staging area and the AWS Transform MGN
<a name="Solving-Communication-Problems"></a>
+ **DHCP** – [Check the DHCP options set of the VPC of the staging area.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/dhcp_options_set.html)

  Ensure that the IPv4 CIDR, the DHCP options set, the route table, and the network ACL are correct.
+ **DNS** – Ensure that your security groups allow outbound DNS resolution over TCP Port 53, and outbound HTTPS connectivity over TCP Port 443.
+ **Route Rules** – the route rules on the staging area subnet may be inaccurately set. The route rules should allow outbound traffic to the Internet.

   To check and set the route rules on the staging area subnet:

  1. Sign in to [AWS console](https://console.aws.amazon.com/), choose **Services** and select **VPC** under **Networking & Content Delivery**.

  1. On the **VPC Dashboard** toolbar, select the **Route Tables** option.

  1. On **Route Tables** page, check the box of the route table of your staging area. 

  1. This will open the details for your Route Table. Navigate to the **Routes** tab.

  1. Within the **Target** column of the **Routes** tab, find the route you are using for the outbound communication to the Internet (either **igw**- Internet Gateway, vgw - **VPN** or **i** - EC2 instance). Verify that the address space in the Destination column is allowing access to Amazon S3, Amazon EC2, and MGN in the AWS Region.

  1. If the address is not **0.0.0.0/0**, change it to **0.0.0.0/0.**

     Choose the **Edit** button.

  1. Input **0.0.0.0/0** into the Destination field for the correct **Target**. Choose **Save**.

     **Note**: If you are using VPN, enter a specific IP address range in the **Destination** column. 
+ **Network ACL** – The network ACL on the staging area subnet may block the traffic. Verify that the ephemeral ports are open. 

## Authenticate with service errors
<a name="Authenticate-With-Service-Errors"></a>

The replication server needs to be able to reach the MGN endpoint and have the proper IAM permissions. This can fail for a number of reasons, including:
+ The replication server is in a subnet without access to VPC endpoints for MGN or the [public endpoints](https://docs.aws.amazon.com/general/latest/gr/mgn.html).
+ In some use cases, when using a custom DNS server, DNS traffic shifts to TCP instead of UDP. The solution for this is to [update](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#updating-security-group-rules) the [Migration Service Security Group](replication-server-settings.md#cirrus-security-group) to allow outbound TCP traffic on port 53.
+ The Replication Server does not have the proper [IAM policy](security-iam-awsmanpol-AWSApplicationMigrationReplicationServerPolicy.md).

## Calculating the required bandwidth for TCP Port 1500
<a name="Calculating-Bandwidth"></a>

The required bandwidth for transferring the replicated data over TCP Port 1500 should be based on the write speed of the participating source servers. The recommended bandwidth should be at least the sum of the average write speed of all replicated source servers. 

*Minimal bandwidth = the sum of the average write speeds of all Source servers*

For example, suppose you are replicating two source servers. One has a write speed of 5 MBps (meaning 5 megabytes of data every second), while the other has 7 MBps. In this case, the recommended bandwidth should be at least 12 MBps. 

### Finding the write speed of your source servers
<a name="Write-speed"></a>

To calculate the required bandwidth for transferring replicated data over TCP Port 1500, you need to know the write speed of your source servers. Use the following tools to find the write speed of your source servers: 

#### Linux
<a name="Linux-speed"></a>

Use the iostat command-line utility, located in the systat package. The iostat utility monitors system input/output device loading and generates statistical reports.

The links below lead to third-party websites not affiliated with or endorsed by AWS. The content on these external sites has not been reviewed or verified by AWS.

The iostat utility is installed [with yum](https://www.redhat.com/sysadmin/io-reporting-linux) (RHEL/CentOS), via [apt-get](https://www.howtoforge.com/tutorial/how-to-install-and-use-iostat-on-ubuntu-1604/) (Ubuntu) and via [zypper](https://documentation.suse.com/sles/15-SP2/html/SLES-all/cha-util.html#sec-util-system-iostat) (SUSE.)

To use iostat for checking the write speed of a Source Server, enter the following:iostat -x <interval>
+ -x - displays extended statistics.
+ <interval> - the number of seconds iostat waits between each report. Each subsequent report covers the time since the previous report.

For example, to check the write speed of a machine every 3 seconds, enter the following command:

iostat -x 3

We recommend that you run the iostat utility for at least 24 hours, since the write speed to the disk changes during the day, and it will take 24 hours of runtime to identify the average running speed. 

#### Windows
<a name="Windows-speed"></a>

Choose one of these options to determine the read/write speed:
+ Open Resource Monitor `perfmon.exe /res` and view the disk activity on the **Disk** tab.
+ Open Performance Monitor `perfmon.exe` and add the **Avg. Disk Bytes/Write** or **Avg. Disk Bytes/Read** counter for Logical Disk or Physical Disk.

## Verifying communication over Port 1500
<a name="Verifying-Communication-1500"></a>

If there is a connection problem from the Source server to the Replication Servers or the Staging Area, use the following methods to check the connection.

To verify the integrity of the connection from a Source server to the Staging Area over TCP Port 1500:

1. Launch a new Linux machine in the Staging Area subnet.

1.  On the new Linux machine, run the following command to open a listener in the Staging Area subnet:

   nc -l 1500

1. On the Source Server, run the following command to check connectivity:

   telnet <new machine ip> 1500

## Solving communication problems over Port 1500
<a name="Solving-Problems-1500"></a>

To solve connectivity problems between Source server and the staging area, check the following:
+ The Network ACL on the staging area subnet may deny the traffic.
+ Route Rules on the staging area subnet may be inaccurately set.
+ The firewall, both internal and external, in the Source Server/infrastructure may block communication.
+ The **Use VPN...** checkbox in AWS Transform MGN console may not be set correctly.

### Enabling the network ACL
<a name="Enabling-Network-ACL"></a>

The Network ACL on the staging area subnet may block connectivity. By default, the network ACL allows connectivity. However, if the ACL setting was changed to deny traffic, you need to change it back. 

To check and activate the network ACL on the staging area subnet:

1. Sign in to the AWS console, choose **Services** and select **VPC** under **Networking & Content Delivery.**

1. On the **Resources** list, select the **Network ACL** option:

1. On **Network ACL** page, select the check box next to the Network ACL of your staging area.

1. On the details table of the selected **Network ACL**, select the **Inbound Rules** tab.

1. On the **Inbound Rules t**ab, verify that the rule that determines the traffic to replication server subnet set to **Allow**. 

   **Note**: The target should allow traffic on TCP Port 1500 from the address space of the source environment. The Network ACL does not necessarily need to be open to all port ranges, as in the screenshot below.

1. If the rule is set to **Deny**, choose **Edit**. 

1. Choose the dropdown under **Allow/Deny** and select **Allow**. Choose **Save**. 

1. You will also need to check the **Ephemeral Ports** on the **Outbound Rules** tab. Within the same **Network ACL**, navigate to the **Outbound Rules** tab.

1. You will need to ensure that you are allowing the correct **Ephemeral Port range** for your particular client. [Ephemeral Port range varies based on each client's operating system.](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-ephemeral-ports) Choose the Edit button to edit your **Ephemeral Port's Port Range** category.

1.  Edit the **Port Range** and choose **Save**. You may have to create a new Rule by choosing the **Add another rule** button.

### Setting route rules on the staging area subnet
<a name="Setting-Route-Rules"></a>

To check and set the route rules on the staging area subnet in AWS:

1. Sign in to AWS console, choose **Services** and select **VPC** under **Networking & Content Delivery**. 

1. On the **VPC Dashboard** toolbar, select the **Route Tables** option.

1. On the **Route Tables** page, check the box of the Route Table of your staging network. 

1. This will open the details for your Route Table. Navigate to the **Routes** tab.

1. Within the **Target** column of the **Routes** tab, find the route you are using for the inbound traffic from the **Source** on TCP Port 1500 (either **igw** - Internet Gateway, **vgw** - VPN or **i** – EC2 instance). Verify that the **Destination address** is **0.0.0.0/0.**

   **Note**: The Rule may be specific to the address space of the source servers.

1. If the address is not 0.0.0.0/0, you will need change it to 0.0.0.0/0.

   **Note**: The Rule may be specific to the address space of the Source Servers.

   1. Choose the Edit button.

   1. Input **0.0.0.0/0** into the **Destination** field for the correct target. Choose **Save**.

      **Note**: If you are using VPN, enter a specific IP address range in the **Destination** column. 

### Firewall (both internal and external) in the source server/infrastructure.
<a name="Firewall-Source"></a>

Firewall issues may have several causes. Check the following if you experience any firewall issues, such as Windows Firewall connection issues:

![Windows Defender Firewall overview showing Domain, Private, and Public profiles are on.](http://docs.aws.amazon.com/mgn/latest/ug/images/troubleshooting-24-re.png)

+ Ensure that the subnet you assigned for the replication servers still exists. 

## Missing Amazon Linux 2023 repository access
<a name="missing-al2023-repo-access"></a>

Replication servers and conversion servers are based on Amazon Linux 2023 (AL2023) and require access to the AL2023 package repository hosted in Amazon S3. If the staging area subnet cannot reach this repository, replication or conversion may fail.

Symptoms of this issue include:
+ Replication stalling or failing after the replication server is launched.
+ Replication server unable to install or update required packages.
+ Conversion server failing during the boot conversion process.

**Cause: Amazon S3 VPC gateway endpoint policy missing AL2023 bucket (isolated subnets)**

If the staging area subnet does not have outbound internet access and uses an Amazon S3 VPC gateway endpoint, the endpoint policy must allow access to the AL2023 repository bucket. Add the following resource ARN to the endpoint policy:

```
"arn:aws:s3:::al2023-repos-<REGION>-de612dc2/*"
```

**Cause: Firewall or proxy blocking the AL2023 repository URL (firewall-restricted environments)**

If the staging area subnet has outbound internet access through a firewall or proxy, ensure that the AL2023 repository URL is allowlisted. The AL2023 repository is accessed through the Amazon S3 dual-stack endpoint:

```
https://al2023-repos-<region>-de612dc2.s3.dualstack.<region>.amazonaws.com/
```

For the complete list of Amazon S3 buckets required by AWS Transform MGN and the example Amazon S3 VPC endpoint policy, see [Communication between the staging area subnet and S3](preparing-environments.md#Communication-Staging-S3).