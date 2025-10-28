# Deploy a default Amazon EC2 host for

Tape Gateway

This topic lists the steps to deploy an Amazon EC2 host using the default
specifications.

You can deploy and activate a Tape Gateway on an Amazon Elastic Compute Cloud (Amazon EC2) instance. The
AWS Storage Gateway Amazon Machine Image (AMI) is available as a community AMI.

###### Note

Storage Gateway community AMIs are published and fully supported by AWS. You can see that
the publisher is AWS, a verified provider.

1. To set up the Amazon EC2instance, choose **Amazon EC2** as the
   **Host platform** in the **Platform options**
   section of the workflow. For instructions on configuring the Amazon EC2 instance, see
   [Deploying an Amazon EC2
   instance to host your Tape Gateway](ec2-gateway-common.md "ec2-gateway-common.md").
2. Select **Launch instance** to open the AWS Storage Gateway AMI template
   in the Amazon EC2 console and customize additional settings such as **Instance
   types**, **Network settings** and **Configure
   storage**.
3. Optionally, you can select **Use default settings** in the
   Storage Gateway console to deploy an Amazon EC2 instance with the default configuration.

The Amazon EC2 instance that **Use default settings** creates has the
following default specifications:

    * **Instance type** — *m5.xlarge*
    * **Network Settings**




    	+ For **VPC**, select the VPC that you want your
    	 EC2 instance to run in.
    	+ For **Subnet**, specify the subnet that your EC2
    	 instance should be launched in.


    	###### Note

    	VPC subnets will appear in the drop down only if they have the
    	 auto-assign public IPv4 address setting activated from the VPC
    	 management console.
    	+ **Auto-assign Public IP** —
    	 *Activated*
    An
     EC2 security group is created and associated with the EC2 instance. The
     security group has the following inbound port rules:


    ###### Note

    You will need Port 80 open during gateway activation. The port is
     closed immediately following activation. Thereafter, your EC2 instance
     can only be accessed over the other ports from the selected VPC.

     The iSCSI targets on your gateway are only accessible from the hosts
     in the same VPC as the gateway. If the iSCSI targets need to be accessed
     from hosts outside of the VPC, you should update the appropriate
     security group rules.

     You can edit security groups at any time by navigating to the Amazon EC2
     instance details page, selecting **Security**,
     navigating to **Security group details**, and choosing
     the security group ID.

| **Port**              | **Protocol**        | **File System Protocol**   |
| --------------------- | ------------------- | -------------------------- | --------------------------- |
| 80                    | TCP                 | HTTP access for activation |
| 3260                  | TCP                 | iSCSI                      | <br>• **Configure storage** |
| **Default Settings**  | **AMI Root Volume** | **Volume 2 Cache**         | **Volume 3 Cache**          |
| ---                   | ---                 | ---                        | ---                         |
| Device Name           |                     | '/dev/sdb'                 | '/dev/sdc'                  |
| Size                  | 80 Gib              | 165 GiB                    | 150 GiB                     |
| Volume Type           | gp3                 | gp3                        | gp3                         |
| IOPS                  | 3000                | 3000                       | 3000                        |
| Delete on termination | Yes                 | Yes                        | Yes                         |
| Encrypted             | No                  | No                         | No                          |
| Throughput            | 125                 | 125                        | 125                         |
