# Deploy an application with AWS Launch Wizard for SQL Server

on Windows (Console)

## Access AWS Launch Wizard

You can launch AWS Launch Wizard from the [AWS Launch Wizard console](https://console.aws.amazon.com/launchwizard "https://console.aws.amazon.com/launchwizard").

## Deploy AWS Launch Wizard on Windows

The following steps guide you through a SQL Server Always On application
deployment with AWS Launch Wizard after you have launched it from the console.

1. When you select **Workload library** from the
   AWS Launch Wizard landing page, you are directed to the **Workload
   library** wizard, where you are prompted to select the type
   of application that you want to deploy. Select **Microsoft SQL
   Server**, then **Launch new
   deployment**.
2. From the **Choose deployment pattern** list of
   available deployment patterns, choose **SQL Server Always On -
   Windows** and then **Configure
   deployment**.
3. Under **Review Permissions**, Launch Wizard displays the
   AWS Identity and Access Management (IAM) role required for Launch Wizard to access other AWS services
   on your behalf. For more information about setting up IAM for Launch Wizard,
   see [AWS Identity and Access Management (IAM)](launch-wizard-getting-started.md#launch-wizard-iam "launch-wizard-getting-started.md#launch-wizard-iam"). Choose **Next** .
4. On the **Configure application settings** page,
   select the **Operating System** on which you want to
   install SQL Server — in this case,
   **Windows**.
5. **Deployment model**. Choose **High availability deployment** to deploy your
   SQL Server Always On application across multiple Availability Zones or
   **Single instance deployment** to
   deploy your SQL Server application on a single node.
6. You are prompted to enter the specifications for the new deployment.
   The following tabs provide information about the specification
   fields.

General

    * **Deployment name**.
     Enter a unique application name for your
     deployment.
    * (Optional) **Simple
     Notification Service (SNS) topic ARN**.
     Specify an SNS topic where AWS Launch Wizard can send
     notifications and alerts. For more information, see
     the [*Amazon Simple Notification Service Developer Guide*](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").
    * (Optional for HA deployments) **CloudWatch application
     monitoring**. Select the check box to set
     up monitors and automated insights for your
     deployment using CloudWatch Application Insights.
     For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md").
    * **Enable rollback on failed
     deployment**. By default, if a deployment
     fails, your provisioned resources will not be rolled
     back/deleted. This default configuration helps you
     to troubleshoot errors at the resource level as you
     debug deployment issues. If you want your
     provisioned resources to be immediately deleted if a
     deployment fails, select the check box.

Connectivity
Enter specifications for how you want to connect to your
instance and configure your Virtual Private Cloud (VPC).

**Key pair name**

    * Select an existing key pair from the dropdown list
     or create a new one. If you select **Create
     new key pair name**, you are directed to
     the Amazon EC2 console. From there, under
     **Network and Security**, choose
     **Key Pairs**. Choose
     **Create a new key pair**, enter
     a name for the key pair, and then choose
     **Download Key Pair**.


    ###### Important

    This is the only opportunity for you to save
     the private key file. Download it and save it in a
     safe place. You must provide the name of your key
     pair when you launch an instance and provide the
     corresponding private key each time that you
     connect to the instance.


    Return to the Launch Wizard console and choose the refresh
     button next to the **Key Pairs**
     dropdown list. The newly created key pair appears in
     the dropdown list. For more information about key
     pairs, see [Amazon EC2 Key Pairs and Windows
     Instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").

**Tenancy model (HA deployments
only)**

Select your preferred tenancy. Each instance that you
launch into a VPC has a tenancy attribute. The
**Shared** tenancy option means that
the instance runs on shared hardware. The
**Dedicated Host (HA deployments)**
tenancy option means that the instance runs on a Dedicated
Host, which is an isolated server with configurations that
you can control. For more information, see [Dedicated Hosts](../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md "../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md").

**Virtual Private Cloud
(VPC)**. Choose whether you want to use an
existing VPC or create a new VPC.

    * **Select Virtual Private Cloud
     (VPC)** option. Choose the VPC that you
     want to use from the dropdown list. If you choose to
     enable Remote Desktop Gateway access on single-node
     deployments, then your VPC must include one public
     subnet and one private subnet. It must include at
     least two private subnets for HA deployments . Your
     VPC must be associated with a [DHCP Options Set](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") to enable DNS
     translations to work. The private subnets must have
     outbound connectivity to the internet and other
     AWS services (S3, CFN, SSM, Logs). We recommend
     that you enable this connectivity with a NAT
     Gateway. For more information about NAT Gateways,
     see [NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
     Amazon VPC User Guide.




    	+ **Public
    	 Subnet**. If you choose to enable Remote
    	 Desktop Gateway access on single-node deployments,
    	 then your VPC must include one public subnet and
    	 one private subnet. It must include at least two
    	 private subnets for HA deployments. Choose a
    	 public subnet for your VPC from the dropdown list.
    	 To continue, you must select the check box that
    	 indicates that the public subnet has been set up
    	 and the private subnets have outbound connectivity
    	 enabled.



    	###### To add a new public subnet


    	If a subnet's traffic is routed to an
    	 internet gateway, the subnet is known as a public
    	 subnet. If, however, a subnet doesn't have a route
    	 to the internet gateway, the subnet is known as a
    	 private subnet. To use an existing VPC that does
    	 not have a public subnet, you can add a new public
    	 subnet using the following steps.



    		- Follow the steps in [Creating a Subnet in the Amazon VPC User
    		 Guide](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Create_Subnet "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Create_Subnet") using the existing VPC you intend to
    		 use AWS Launch Wizard.
    		- To add an internet gateway to your VPC,
    		 follow the steps in [Attaching an Internet Gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway") in the
    		 Amazon VPC User Guide.
    		- To configure your subnets to route internet
    		 traffic through the internet gateway, follow the
    		 steps in [Creating a Custom Route Table](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing") in the
    		 Amazon VPC User Guide. Use IPv4 format (0.0.0.0/0) for
    		 Destination.
    		- The public subnet should have the
    		 “auto-assign public IPv4 address” setting enabled.
    		 To enable this setting, follow the steps in [Modifying the Public IPv4 Addressing Attribute
    		 for Your Subnet](../../../vpc/latest/userguide/vpc-ip-addressing.md#subnet-public-ip "../../../vpc/latest/userguide/vpc-ip-addressing.md#subnet-public-ip") in the
    		 Amazon VPC User Guide.
    	+ **Availability Zone (AZ)
    	 configuration**. You must choose at least
    	 two Availability Zones for High Availability (HA)
    	 deployments and one Availability Zone for
    	 single-node deployments, with one private subnet
    	 for each zone that you select. For HA deployments,
    	 select the **Availability Zones**
    	 within which you want to deploy your **primary** and **secondary** SQL nodes.
    	 Depending on the number of secondary nodes that
    	 you plan to use to set up a SQL Server Always On
    	 deployment, you may have to specify a **private subnet** for each of them.
    	 Cross-Region replication is not supported.



    	###### To create a private subnet


    	If a subnet doesn't have a route to an
    	 internet gateway, the subnet is known as a private
    	 subnet. To create a private subnet, you can use
    	 the following steps. We recommend that you enable
    	 the outbound connectivity for each of your
    	 selected private subnets using a NAT Gateway. To
    	 enable outbound connectivity from private subnets
    	 with public subnet, see the steps in [Creating a NAT Gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating") to create a NAT
    	 Gateway in your chosen public subnet. Then, follow
    	 the steps in [Updating Your Route Table](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-create-route "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-create-route") for each of
    	 your chosen private subnets.



    		- Follow the steps in [Creating a Subnet](../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet "../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet") in the Amazon VPC User Guide
    		 using the existing VPC you will use in AWS
    		 Launch Wizard.
    		- When you create a VPC, it includes a main
    		 route table by default. On the **Route
    		 Tables** page in the Amazon VPC console,
    		 you can view the main route table for a VPC by
    		 looking for Yes in the Main column. The main route
    		 table controls the routing for all subnets that
    		 are not explicitly associated with any other route
    		 table. If the main route table for your VPC has an
    		 outbound route to an internet gateway, then any
    		 subnet created using the previous step, by
    		 default, becomes a public subnet. To ensure the
    		 subnets are private, you may need to create
    		 separate route table(s) for your private subnets.
    		 These route tables must not contain any routes to
    		 an internet gateway. Alternatively, you can create
    		 a custom route table for your public subnet and
    		 remove the internet gateway entry from the main
    		 route table.
    	If you selected **Dedicated
    	 host** tenancy, you must select a
    	 Dedicated Host for each Availability Zone. If you
    	 have not allocated any dedicated hosts to your
    	 account, you can choose **Create new
    	 dedicated host** to do so from the EC2
    	 console.
    	+ **Remote Desktop Gateway
    	 preferences (single-node deployments
    	 only)**. When you select **Set up
    	 Remote Desktop Gateway**, enter the
    	 public subnet into which to deploy the RDGW
    	 instance.
    	+ (Optional) **Remote
    	 Desktop Gateway access**. Select
    	 **Custom IP** from the dropdown
    	 list. Enter the CIDR block. If you do not specify
    	 any value for the Custom IP parameter, Launch Wizard does
    	 not set the inbound RDP access (Port 3389) from
    	 any IP. You can choose to do this later by
    	 modifying the security group settings via the
    	 Amazon EC2 console. See [Adding a Rule for Inbound RDP Traffic to a
    	 Windows Instance](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access") for instructions on
    	 adding a rule that allows inbound RDP traffic to
    	 your RDGW instance.


    * **Create new Virtual Private
     Cloud (VPC)** option. Launch Wizard creates your
     VPC. You can optionally enter a **VPC name tag**. If you
     selected **Dedicated Host** tenancy
     for high availability deployments, select a primary
     and secondary Dedicated Host. If you haven't
     allocated any Dedicated Hosts to your account,
     select **Create a new dedicated
     host**. You will be directed to the EC2
     console to create the new host.




    	+ **Remote Desktop Gateway
    	 preferences (single-node deployments
    	 only)**. When you select **Set up
    	 Remote Desktop Gateway**, only the Remote
    	 Desktop Gateway access information will be taken
    	 from the VPC.
    	+ (Optional) **Remote
    	 Desktop Gateway access**. Select
    	 **Custom IP** from
    	 the dropdown list. Enter the CIDR block. If you do
    	 not specify any value for the Custom IP parameter,
    	 Launch Wizard does not set the inbound RDP access (Port
    	 3389) from any IP. You can choose to do this later
    	 by modifying the security group settings via the
    	 Amazon EC2 Console. See [Adding a Rule for Inbound RDP Traffic to a
    	 Windows Instance](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access") for instructions on
    	 adding a rule that allows inbound RDP traffic to
    	 your RDGW instance.

Active Directory
You can connect to an existing Active Directory or, for
high availability deployments, you can create a new one. If
you selected the **Create new Virtual Private Cloud
(VPC)** option for high availability
deployments, you must select **Create a new Active
Directory**.

###### Connecting to existing AWS Managed Active Directory

or Self Managed Active Directory

From the dropdown list, select whether you want to use
**AWS Managed Active Directory**,
or **Self Managed Active Directory**.
If you select **Self Managed Active
Directory**, select the check box to verify
that you have ensured a connection between the Active
Directory and the VPC.

Follow the steps for granting permissions in the
Active Directory Default Organizational Unit (OU).

    * **Domain user name and
     password**. Enter the user name and
     password for your directory. For required
     permissions for the domain user, see [Active Directory (Windows deployment)](launch-wizard-getting-started.md#launch-wizard-ad "launch-wizard-getting-started.md#launch-wizard-ad"). Launch Wizard stores
     the password in AWS Secrets Manager as a
     secure string parameter. It does not store the
     password on the service side. To create a functional
     SQL Server Always On deployment, it reads from
     AWS Secrets Manager.
    * **DNS address**.
     Enter the IP address of the DNS servers to which you
     are connecting. These servers must be reachable from
     within the VPC that you selected.
    * **Optional DNS
     address**. If you would like to use a
     backup DNS server, enter the IP address of the DNS
     server that you want to use as backup. These servers
     must be reachable from within the VPC that you
     selected.
    * **Domain DNS name**.
     Enter the Fully Qualified Domain Name (FQDN) of the
      [forest root domain](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/selecting-the-forest-root-domain "https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/selecting-the-forest-root-domain")  used for the Active
     Directory. When you choose to create a new Active
     Directory, Launch Wizard creates a domain admin user on your
     Active Directory.

###### Creating a new AWS Managed Active Directory through

Launch Wizard

    * **Domain user name and
     password**. The domain user name is
     preset to “admin.” Enter a password for your
     directory. Launch Wizard stores the password in
     AWS Secrets Manager as a secure string
     parameter. It does not store the password on the
     server side. To create a functional SQL Server
     Always On deployment, it reads from
     AWS Secrets Manager.
    * **Domain DNS name**.
     Enter a Fully Qualified Domain Name (FQDN) of the
     forest root domain used for the Active Directory.
     When you choose to create a new Active Directory,
     Launch Wizard creates a domain admin user on your Active
     Directory.

###### Connecting to a Self Managed Active Directory through

Launch Wizard

Launch Wizard allows you to connect to a Self Managed Active
Directory environment during deployment. For more
information, see [Self Managed Active Directory](launch-wizard-getting-started.md#launch-wizard-ad-onprem "launch-wizard-getting-started.md#launch-wizard-ad-onprem").

SQL Server

When you use an existing Active Directory, you have
the option of using an existing SQL Server service
account or creating a new account. If you create a new
Active Directory account, you must create a new SQL
Server account.

    * **User name and
     password**. If you are using an existing
     SQL Server service account, provide your user name
     and password. This SQL Server service account should
     be part of the Managed Active Directory in which you
     are deploying. If you are creating a new SQL Server
     service account through Launch Wizard, enter a user name for
     the SQL Server service account. Create a complex
     Password that is at least 8 characters long, and
     then reenter the password to verify it. See [Password Policy](https://docs.microsoft.com/en-us/sql/relational-databases/security/password-policy?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/security/password-policy?view=sql-server-2017") for more
     information.
    * **SQL Server install
     type**. Select the version of SQL Server
     Enterprise that you want to deploy. You can select
     an AMI from either the License-included AMI or
     Custom AMI dropdown lists.
    * **License-included
     AMI**. Choose an AMI for your SQL Server
     deployment which determines the version and edition
     of Windows Server and SQL Server that will be
     deployed.
    * (Optional) **tempdb
     configuration**. To improve performance,
     you can opt for the SQL Server tempdb system
     database to reside on a local NVMe SSD ephemeral
     storage device, also called the (instance store
     volume). NVMe SSD instance store volumes are
     available only on instance types that provide these
     local storage devices. Additionally, only data that
     changes frequently should ever reside on these
     volumes. They are not intended to store data
     long-term. For more information, see [Amazon EC2 instance store](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md").
    * (Optional) **Additional SQL
     Server settings**. You can specify the
     following:




    	+ **Nodes**.
    	 Enter a **Primary SQL node
    	 name** and a **Secondary SQL node name (HA deployments
    	 only)**.
    	+ **Additional secondary
    	 SQL node (HA deployments only, maximum of
    	 5)**. Enter a secondary **Node name**, and select the
    	 **Access type**, the
    	 **Private subnet**,
    	 and the **Dedicated host**, if
    	 applicable, for the additional secondary SQL node
    	 from the dropdown lists. You can add more
    	 secondary nodes by selecting **Add additional secondary node**.
    	+ (Optional, HA deployments only) **Witness node**. For improved
    	 fault tolerance, select the check box to add a
    	 file share quorum witness node.
    	+ **Additional naming**.
    	 Enter a **Database
    	 name**. For HA deployments, enter an
    	 **Availability group
    	 name**, a **Listener
    	 name**, and a **Windows cluster virtual network name**.

7. When you are satisfied with your configuration selections, select
   **Next**. If you don't want to complete the
   configuration, select **Cancel**. When you select
   **Cancel**, all of the selections on the
   specification page are lost and you are returned to the landing page. To
   go to the previous screen, select **Previous**.
8. After configuring your application, you are prompted to define the
   infrastructure requirements for the new deployment on the
   **Define infrastructure requirements** page. The
   following tabs provide information about the input fields.

Define infrastructure requirements

You can choose to select your instances and volume
types, or to use AWS recommended resources. If you
choose to use AWS recommended resources, you have the
option of defining your high availability cluster needs.
If no selections are made, default values are
assigned.

    * **Number of instance
     cores**. Choose the number of CPU cores
     for your infrastructure. The default value assigned
     is 4.
    * **Network
     performance**. Choose your preferred
     network performance in Gbps.
    * **Memory (GB)**.
     Choose the amount of RAM that you want to attach to
     your EC2 instances. The default value assigned is 4
     GB.
    * **Type of storage
     drive**. Select the storage drive type
     for the SQL data and tempdb volumes. If you chose to
     place your tempdb on local storage, only the SQL
     data will be on the storage drive you select. The
     default value assigned is SSD.
    * **SQL Server
     throughput**. Select the sustained SQL
     Server throughput that you need.
    * **Recommended
     resources**. Launch Wizard displays the
     system-recommended resources based on your
     infrastructure selections. If you want to change the
     recommended resources, select different
     infrastructure requirements.

###### Infrastructure requirements based on instance

type

You can choose to select your instance and volume
type, or to use AWS recommended resources. If no
selections are made, default values are assigned.

    * **Instance type**.
     Select your preferred instance type from the
     dropdown list.
    * **Volume type**.
     Choose your preferred EBS volume type. For more
     information about volume types, see [Amazon EBS volume types](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md").

###### Drive letters and volume size

    * **Drive letter**.
     Select the storage drive letter for **Root
     drive**, **Logs**,
     **Data**, and
     **Backup** volumes.


    ###### Important

    For custom AMIs, Launch Wizard assumes the root volume
     drive is `C:`.
    * **Volume size**.
     Select the size of the SQL Server data volume in Gb
     for **Root drive**,
     **Logs**,
     **Data**, and
     **Backup** volumes. SQL Server
     logs and data will be staged on the same data volume
     for this deployment. Make sure that you select an
     adequate size for the data volume.

###### Note

For Launch Wizard deployments created after January 2023,
IMDSv1 is disabled on all instances. If your
software or scripts use IMDSv1, you will have to
meet the requirements to use IMDSv2. For more
information, see [Use IMDSv2](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md").

(Optional) Tags
You can provide optional custom tags for the resources
Launch Wizard creates on your behalf. For example, you can
set different tags for EC2 instances, EBS volumes, VPC, and
subnets. If you select **All**, you can
assign a common set of tags to your resources. Launch Wizard assigns
tags with a fixed key
`LaunchWizardResourceGroupID` and value that
corresponds to the ID of the AWS resource group created
for a deployment. Launch Wizard does not support custom tagging for
root volumes.

Estimated on-demand cost to deploy additional
resources
AWS Launch Wizard provides an estimate for application charges
incurred to deploy the selected resources. The estimate
updates each time you change a resource type in the Wizard.
The provided estimates are only for general comparisons.
They are based upon On-Demand costs and your actual costs
may be lower. 9. When you are satisfied with your infrastructure selections, select
**Next**. If you don't want to complete the
configuration, select **Cancel**. When you select
**Cancel**, all of the selections on the
specification page are lost and you are returned to the landing page. To
go to the previous screen, select **Previous**. 10. On the **Review and deploy** page, review your
configuration details. If you want to make changes, select
**Previous**. To stop, select
**Cancel**. When you select
**Cancel**, all of the selections on the
specification page are lost and you are returned to the landing page.
When you choose **Deploy**, you agree to the terms of
the **Acknowledgment**. 11. Launch Wizard validates the inputs and notifies you of any issues you must
address. 12. When validation is complete, Launch Wizard deploys your AWS resources and
configures your SQL Server Always On application. Launch Wizard provides you with
status updates about the progress of the deployment on the **Deployments** page. From the **Deployments** page, you can view the list of
current and previous deployments. 13. When your deployment is ready, a notification informs you that your
SQL Server application is successfully deployed. If you have set up an
SNS notification, you are also alerted through SNS. You can manage and
access all of the resources related to your SQL Server Always On
application by selecting the deployment, and then selecting
**Manage** from the **Actions** dropdown list. 14. When the SQL Server Always On application is deployed, you can access
your Amazon EC2 instances through the EC2 console. You can also use [AWS SSM](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") to manage your SQL Server Always On application
for future updates and patches through built-in integration via resource
groups.
The following steps guide you through a SQL Failover Clustering application
deployment with AWS Launch Wizard after you have launched it from the console.

1. When you select **Workload library** from the
   AWS Launch Wizard landing page, you are directed to the **Workload
   library** wizard, where you are prompted to select the type
   of application that you want to deploy. Select **Microsoft SQL
   Server**, then **Launch new
   deployment**.
2. From the **Choose deployment pattern** list of
   available deployment patterns, choose **SQL Server Failover
   Clustering - Windows** and then **Configure
   deployment**.
3. Under **Review Permissions**, Launch Wizard displays the
   AWS Identity and Access Management (IAM) role required for Launch Wizard to access other AWS services
   on your behalf. For more information about setting up IAM for Launch Wizard,
   see [AWS Identity and Access Management (IAM)](launch-wizard-getting-started.md#launch-wizard-iam "launch-wizard-getting-started.md#launch-wizard-iam"). Choose **Next** .
4. On the **Configure application settings** page,
   select the **Operating System** on which you want to
   install SQL Server — in this case,
   **Windows**.
5. **Deployment model**. Choose **High availability deployment**, and then choose
   **Always On Failover Cluster Instances** to deploy
   a SQL Server Failover Clustering (FCI) application across multiple
   Availability Zones.
6. You are prompted to enter the specifications for the new deployment
   The following tabs provide information about the specification
   fields.

General

    * **Deployment name**.
     Enter a unique application name for your
     deployment.
    * (Optional) **Simple
     Notification Service (SNS) topic ARN**.
     Specify an SNS topic where AWS Launch Wizard can send
     notifications and alerts. For more information, see
     the [*Amazon Simple Notification Service Developer Guide*](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").
    * (Optional for HA deployments) **CloudWatch application
     monitoring**. Select the check box to set
     up monitors and automated insights for your
     deployment using CloudWatch Application Insights.
     For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md").
    * **Enable rollback on failed
     deployment**. By default, if a deployment
     fails, your provisioned resources will not be rolled
     back/deleted. This default configuration helps you
     to troubleshoot errors at the resource level as you
     debug deployment issues. If you want your
     provisioned resources to be immediately deleted if a
     deployment fails, select the check box.

Connectivity
Enter the specifications for how you want to connect to
your instance and configure your Virtual Private Cloud
(VPC).

**Key pair name**

    * Select an existing key pair from the dropdown list
     or create a new one. If you select **Create
     new key pair name**, you are directed to
     the Amazon EC2 console. From there, under
     **Network and Security**, choose
     **Key Pairs**. Choose
     **Create a new key pair**, enter
     a name for the key pair, and then choose
     **Download Key Pair**.


    ###### Important

    This is the only opportunity for you to save
     the private key file. Download it and save it in a
     safe place. You must provide the name of your key
     pair when you launch an instance and provide the
     corresponding private key each time that you
     connect to the instance.


    Return to the Launch Wizard console and choose the refresh
     button next to the **Key Pairs**
     dropdown list. The newly created key pair appears in
     the dropdown list. For more information about key
     pairs, see [Amazon EC2 Key Pairs and Windows
     Instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").

**Tenancy model (HA deployments
only)**

Select your preferred tenancy. Each instance that you
launch into a VPC has a tenancy attribute. The
**Shared** tenancy option means that
the instance runs on shared hardware. The
**Dedicated Host (HA deployments)**
tenancy option means that the instance runs on a Dedicated
Host, which is an isolated server with configurations that
you can control. For FCI deployments, select
**Shared** tenancy.

**Virtual Private Cloud
(VPC)**. Choose whether you want to use an
existing VPC or create a new VPC.

    * **Select Virtual Private Cloud
     (VPC)** option. Choose the VPC that you
     want to use from the dropdown list. If you choose to
     enable Remote Desktop Gateway access, then your VPC
     must include at least one public subnet and two
     private subnets for HA deployments . Your VPC must
     be associated with a [DHCP Options Set](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") to enable DNS
     translations to work. The private subnets must have
     outbound connectivity to the internet and other
     AWS services (S3, CFN, SSM, Logs). We recommend
     that you enable this connectivity with a NAT
     Gateway. For more information about NAT Gateways,
     see [NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
     Amazon VPC User Guide.




    	+ **Public
    	 Subnet**. If you choose to enable Remote
    	 Desktop Gateway access, then your VPC must include
    	 at least one public subnet and two private subnets
    	 for HA deployments. Choose a public subnet for
    	 your VPC from the dropdown list. To continue, you
    	 must select the check box that indicates that the
    	 public subnet has been set up and the private
    	 subnets have outbound connectivity enabled.



    	If a subnet's traffic is routed to an
    	 internet gateway, the subnet is known as a public
    	 subnet. If, however, a subnet doesn't have a route
    	 to the internet gateway, the subnet is known as a
    	 private subnet.


    	To use an existing VPC that does
    	 not have a public subnet, you can add a new public
    	 subnet using the following steps:



    		- Follow the steps in [Creating a Subnet in the Amazon VPC User
    		 Guide](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Create_Subnet "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Create_Subnet") using the existing VPC you intend to
    		 use AWS Launch Wizard.
    		- To add an internet gateway to your VPC,
    		 follow the steps in [Attaching an Internet Gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway") in the
    		 Amazon VPC User Guide.
    		- To configure your subnets to route internet
    		 traffic through the internet gateway, follow the
    		 steps in [Creating a Custom Route Table](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing") in the
    		 Amazon VPC User Guide. Use IPv4 format (0.0.0.0/0) for
    		 Destination.
    		- The public subnet should have the
    		 “auto-assign public IPv4 address” setting enabled.
    		 To enable this setting, follow the steps in [Modifying the Public IPv4 Addressing Attribute
    		 for Your Subnet](../../../vpc/latest/userguide/vpc-ip-addressing.md#subnet-public-ip "../../../vpc/latest/userguide/vpc-ip-addressing.md#subnet-public-ip") in the
    		 Amazon VPC User Guide.
    	+ **Availability Zone (AZ)
    	 configuration**. You must choose at least
    	 two Availability Zones for High Availability (HA)
    	 deployments, with one private subnet for each zone
    	 that you select. For HA deployments, select the
    	 **Availability Zones** within
    	 which you want to deploy your **primary** and **secondary** SQL nodes.
    	 Depending on the number of secondary nodes that
    	 you plan to use to set up a SQL Server Always On
    	 deployment, you may have to specify a **private subnet** for each of them.
    	 Cross-Region replication is not supported.



    	###### To create a private subnet


    	If a subnet doesn't have a route to an
    	 internet gateway, the subnet is known as a private
    	 subnet. To create a private subnet, you can use
    	 the following steps. We recommend that you enable
    	 the outbound connectivity for each of your
    	 selected private subnets using a NAT Gateway. To
    	 enable outbound connectivity from private subnets
    	 with public subnet, see the steps in [Creating a NAT Gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating") to create a NAT
    	 Gateway in your chosen public subnet. Then, follow
    	 the steps in [Updating Your Route Table](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-create-route "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-create-route") for each of
    	 your chosen private subnets.



    		- Follow the steps in [Creating a Subnet](../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet "../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet") in the Amazon VPC User Guide
    		 using the existing VPC you will use in AWS
    		 Launch Wizard.
    		- When you create a VPC, it includes a main
    		 route table by default. On the **Route
    		 Tables** page in the Amazon VPC console,
    		 you can view the main route table for a VPC by
    		 looking for Yes in the Main column. The main route
    		 table controls the routing for all subnets that
    		 are not explicitly associated with any other route
    		 table. If the main route table for your VPC has an
    		 outbound route to an internet gateway, then any
    		 subnet created using the previous step, by
    		 default, becomes a public subnet. To ensure the
    		 subnets are private, you may need to create
    		 separate route table(s) for your private subnets.
    		 These route tables must not contain any routes to
    		 an internet gateway. Alternatively, you can create
    		 a custom route table for your public subnet and
    		 remove the internet gateway entry from the main
    		 route table.
    	+ **Remote Desktop Gateway
    	 preferences**. When you select
    	 **Set up Remote Desktop
    	 Gateway**, enter the public subnet into
    	 which to deploy the RDGW instance.
    	+ (Optional) **Remote
    	 Desktop Gateway access**. Select
    	 **Custom IP** from the dropdown
    	 list. Enter the CIDR block. If you do not specify
    	 any value for the Custom IP parameter, Launch Wizard does
    	 not set the inbound RDP access (Port 3389) from
    	 any IP. You can choose to do this later by
    	 modifying the security group settings via the
    	 Amazon EC2 console. See [Adding a Rule for Inbound RDP Traffic to a
    	 Windows Instance](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access") for instructions on
    	 adding a rule that allows inbound RDP traffic to
    	 your RDGW instance.


    * **Create new Virtual Private
     Cloud (VPC)** option. Launch Wizard creates your
     VPC. You can optionally enter a **VPC name tag**.




    	+ **Remote Desktop Gateway
    	 preferences**. When you select
    	 **Set up Remote Desktop
    	 Gateway**, only the Remote Desktop
    	 Gateway access information will be taken from the
    	 VPC.
    	+ (Optional) **Remote
    	 Desktop Gateway access**. Select
    	 **Custom IP** from
    	 the dropdown list. Enter the CIDR block. If you do
    	 not specify any value for the Custom IP parameter,
    	 Launch Wizard does not set the inbound RDP access (Port
    	 3389) from any IP. You can choose to do this later
    	 by modifying the security group settings via the
    	 Amazon EC2 Console. See [Adding a Rule for Inbound RDP Traffic to a
    	 Windows Instance](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access") for instructions on
    	 adding a rule that allows inbound RDP traffic to
    	 your RDGW instance.

Active Directory
You can connect to an existing Active Directory or create
a new one. If you selected the **Create new Virtual
Private Cloud (VPC)** option for high
availability deployments, you must select **Create a
new Active Directory**.

###### Connecting to existing AWS Managed Active Directory

or Self Managed Active Directory

From the dropdown list, select whether you want to use
**AWS Managed Active Directory**,
or **Self Managed Active Directory**.
If you select **Self Managed Active
Directory**, select the check box to verify
that you have ensured a connection between the Active
Directory and the VPC.

Follow the steps for granting permissions in the
Active Directory Default Organizational Unit (OU).

    * **Domain user name and
     password**. Enter the user name and
     password for your directory. For required
     permissions for the domain user, see [Active Directory (Windows deployment)](launch-wizard-getting-started.md#launch-wizard-ad "launch-wizard-getting-started.md#launch-wizard-ad"). Launch Wizard stores
     the password in AWS Secrets Manager as a
     secure string parameter. It does not store the
     password on the service side. To create a functional
     SQL Server FCI deployment, Launch Wizard reads from
     AWS Secrets Manager.
    * **DNS address**.
     Enter the IP address of the DNS servers to which you
     are connecting. These servers must be reachable from
     within the VPC that you selected.
    * **Optional DNS
     address**. If you would like to use a
     backup DNS server, enter the IP address of the DNS
     server that you want to use as backup. These servers
     must be reachable from within the VPC that you
     selected.
    * **Domain DNS name**.
     Enter the Fully Qualified Domain Name (FQDN) of the
      [forest root domain](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/selecting-the-forest-root-domain "https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/selecting-the-forest-root-domain")  used for the Active
     Directory. When you choose to create a new Active
     Directory, Launch Wizard creates a domain admin user on your
     Active Directory.
    * (Optional) **Domain User
     security group**. To specify an existing
     security group, select one from the dropdown list.
     The prerequisites for adding security groups can be
     viewed by selecting **Info**.

###### Creating a new AWS Managed Active Directory through

Launch Wizard

    * **Domain user name and
     password**. The domain user name is
     preset to “admin.” Enter a password for your
     directory. Launch Wizard stores the password in
     AWS Secrets Manager as a secure string
     parameter. It does not store the password on the
     server side. To create a functional SQL Server FCI
     deployment, Launch Wizard reads from
     AWS Secrets Manager.
    * **Domain DNS name**.
     Enter a Fully Qualified Domain Name (FQDN) of the
     forest root domain used for the Active Directory.
     When you choose to create a new Active Directory,
     Launch Wizard creates a domain admin user on your Active
     Directory.

###### Connecting to a Self Managed Active Directory through

Launch Wizard

Launch Wizard allows you to connect to a Self Managed Active
Directory environment during deployment. For more
information, see [Self Managed Active Directory](launch-wizard-getting-started.md#launch-wizard-ad-onprem "launch-wizard-getting-started.md#launch-wizard-ad-onprem").

SQL Server

When you use an existing Active Directory, you have
the option of using an existing SQL Server service
account or creating a new account. If you create a new
Active Directory account, you must create a new SQL
Server account.

    * **User name and
     password**. If you are using an existing
     SQL Server service account, provide your user name
     and password. This SQL Server service account should
     be part of the Managed Active Directory in which you
     are deploying. If you are creating a new SQL Server
     service account through Launch Wizard, enter a user name for
     the SQL Server service account. Create a complex
     Password that is at least 8 characters long, and
     then reenter the password to verify it. See [Password Policy](https://docs.microsoft.com/en-us/sql/relational-databases/security/password-policy?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/security/password-policy?view=sql-server-2017") for more
     information.
    * **SQL Server install
     type**. Select the version of SQL Server
     Enterprise that you want to deploy. You can select
     an AMI from either the License-included AMI or
     Custom AMI dropdown lists.
    * **License-included
     AMI**. Choose an AMI for your SQL Server
     deployment which determines the version and edition
     of Windows Server and SQL Server that will be
     deployed.
    * (Optional) **Additional SQL
     Server settings**. You can optionally
     specify the following:




    	+ **Nodes**.
    	 Enter a **Primary SQL node
    	 name** and a **Secondary SQL node name**.
    	+ **Additional naming**.
    	 Enter a **SQL Server virtual
    	 network name** and a **Windows
    	 cluster virtual network name**.

7. When you are satisfied with your configuration selections, select
   **Next**. If you don't want to complete the
   configuration, select **Cancel**. When you select
   **Cancel**, all of the selections on the
   specification page are lost and you are returned to the landing page. To
   go to the previous screen, select **Previous**.
8. After configuring your application, you are prompted to define the
   infrastructure requirements for the new deployment on the
   **Define infrastructure requirements** page. The
   following tabs provide information about the input fields.

Define infrastructure requirements

You can choose to select your instances and volume
types, or to use AWS recommended resources. If you
choose to use AWS recommended resources, you have the
option of defining your high availability cluster needs.
If no selections are made, default values are
assigned.

**Instances**

    * **Cores**. Choose the
     number of CPU cores for your infrastructure. The
     default value assigned is 4.
    * **Network
     performance**. Choose your preferred
     network performance in Gbps.
    * **Memory (GB)**.
     Choose the amount of RAM that you want to attach to
     your EC2 instances. The default value assigned is 4
     GB.

**Storage and
performance**

    * **Type of storage
     drive**. The default value assigned is
     SSD for FCI application deployments.
    * **Average and peak
     IOPS**. Select the average and peak IOPS
     required for your FSx share.
    * **Allocated storage
     space**. Select the amount of storage
     required for your FSx drive.
    * **Recommended
     resources**. Launch Wizard displays the
     system-recommended resources based on your
     infrastructure selections. If you want to change the
     recommended resources, select different
     infrastructure requirements.

###### Infrastructure requirements based on instance

type

You can choose to select your instance and storage
capacity, or to use AWS recommended resources. If no
selections are made, default values are assigned.

    * **Instance type**.
     Select your preferred instance type from the
     dropdown list.
    * **Storage capacity**.
     Choose your preferred EBS volume type. For more
     information about volume types, see [Amazon EBS volume types](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md").
    * **Throughput
     capacity**. Select the required sustained
     SQL Server throughput.

###### Note

For Launch Wizard deployments created after January 2023,
IMDSv1 is disabled on all instances. If your
software or scripts use IMDSv1, you will have to
meet the requirements to use IMDSv2. For more
information, see [Use IMDSv2](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md").

Tags-Optional
You can provide optional custom tags for the resources
Launch Wizard creates on your behalf. For example, you can
set different tags for EC2 instances, EBS volumes, VPC, and
subnets. If you select **All**, you can
assign a common set of tags to your resources. Launch Wizard assigns
tags with a fixed key
`LaunchWizardResourceGroupID` and value that
corresponds to the ID of the AWS resource group created
for a deployment. Launch Wizard does not support custom tagging for
root volumes.

Estimated on-demand cost to deploy additional
resources
AWS Launch Wizard provides an estimate for application charges
incurred to deploy the selected resources. The estimate
updates each time you change a resource type in the Wizard.
The provided estimates are only for general comparisons.
They are based upon On-Demand costs and your actual costs
may be lower. 9. When you are satisfied with your infrastructure selections, select
**Next**. If you don't want to complete the
configuration, select **Cancel**. When you select
**Cancel**, all of the selections on the
specification page are lost and you are returned to the landing page. To
go to the previous screen, select **Previous**. 10. On the **Review and deploy** page, review your
configuration details. If you want to make changes, select
**Previous**. To stop, select
**Cancel**. When you select
**Cancel**, all of the selections on the
specification page are lost and you are returned to the landing page.
When you choose **Deploy**, you agree to the terms of
the **Acknowledgment**. 11. Launch Wizard validates the inputs and notifies you of any issues you must
address. 12. When validation is complete, Launch Wizard deploys your AWS resources and
configures your SQL Server FCI application. Launch Wizard provides you with
status updates about the progress of the deployment on the **Deployments** page. From the **Deployments** page, you can view the list of
current and previous deployments. 13. When your deployment is ready, a notification informs you that your
SQL Server application is successfully deployed. If you have set up an
SNS notification, you are also alerted through SNS. You can manage and
access all of the resources related to your SQL Server FCI application
by selecting the deployment, and then selecting
**Manage** from the **Actions** dropdown list. 14. When the SQL Server FCI application is deployed, you can access your
Amazon EC2 instances through the EC2 console. You can also use [AWS SSM](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") to manage your SQL Server FCI application for
future updates and patches through built-in integration via resource
groups.
The following steps guide you through a SQL Server Developer Edition
application deployment with AWS Launch Wizard after you have launched it from the
console.

1. When you select **Workload library** from the
   AWS Launch Wizard landing page, you are directed to the **Workload
   library** wizard, where you are prompted to select the type
   of application that you want to deploy. Select **Microsoft SQL
   Server**, then **Launch new
   deployment**.
2. From the **Choose deployment pattern** list of
   available deployment patterns, choose **SQL Server Developer
   Edition - Single Node - Windows** and then
   **Configure deployment**.
3. Under **Review Permissions**, Launch Wizard displays the
   AWS Identity and Access Management (IAM) role required for Launch Wizard to access other AWS services
   on your behalf. For more information about setting up IAM for Launch Wizard,
   see [AWS Identity and Access Management (IAM)](launch-wizard-getting-started.md#launch-wizard-iam "launch-wizard-getting-started.md#launch-wizard-iam"). Choose **Next** .
4. On the **Configure application settings** page, you
   are prompted to enter the specifications for the new deployment. The
   following tabs provide information about the specification
   fields.

General

    * **Deployment name**.
     Enter a unique application name for your
     deployment.
    * **CloudWatch application
     monitoring**. Select the check box to set
     up monitors and automated insights for your
     deployment using CloudWatch Application Insights.
     For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md").
    * **Enable rollback on failed
     deployment**. By default, if a deployment
     fails, your provisioned resources will not be rolled
     back/deleted. This default configuration helps you
     to troubleshoot errors at the resource level as you
     debug deployment issues. If you want your
     provisioned resources to be immediately deleted if a
     deployment fails, select the check box.
    * **AWS Service Catalog product
     creation**. Select the check box to
     export the CloudFormation template to create AWS Service Catalog for
     this deployment. When enabled, you must specify an
     S3 bucket location to store the CloudFormation
     templates and application configuration scripts for
     Service Catalog. You can select an existing bucket
     or create a new one using the provided link.
    * (Optional) **Amazon Simple Notification Service (SNS)
     topic ARN**. Specify an SNS topic where
     AWS Launch Wizard can send notifications and alerts. For more
     information, see the [Amazon Simple
     Notification Service Developer
     Guide](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").

Connectivity
Enter specifications for how you want to connect to your
instance and configure your Virtual Private Cloud
(VPC).

**Key pair name**

    * Select an existing key pair from the dropdown list
     or create a new one. If you select **Create
     new key pair name**, you are directed to
     the Amazon EC2 console. From there, under
     **Network and Security**, choose
     **Key Pairs**. Choose
     **Create a new key pair**, enter
     a name for the key pair, and then choose
     **Download Key Pair**.


    ###### Important

    This is the only opportunity for you to save
     the private key file. Download it and save it in a
     safe place. You must provide the name of your key
     pair when you launch an instance and provide the
     corresponding private key each time that you
     connect to the instance.


    Return to the Launch Wizard console and choose the refresh
     button next to the **Key Pairs**
     dropdown list. The newly created key pair appears in
     the dropdown list. For more information about key
     pairs, see [Amazon EC2 Key Pairs and Windows
     Instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").

**Virtual Private Cloud
(VPC)**. Choose whether you want to use an
existing VPC or create a new VPC.

    * **Select Virtual Private Cloud
     (VPC)** option. Choose the VPC that you
     want to use from the dropdown list. If you choose to
     enable Remote Desktop Gateway access, then your VPC
     must include one public subnet and one private
     subnet. Your VPC must be associated with a [DHCP Options Set](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") to enable DNS
     translations to work. The private subnets must have
     outbound connectivity to the internet and other
     AWS services (S3, CFN, SSM, Logs). We recommend
     that you enable this connectivity with a NAT
     Gateway. For more information about NAT Gateways,
     see [NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
     Amazon VPC User Guide.




    	+ **Public
    	 Subnet**. If you choose to enable Remote
    	 Desktop Gateway access, then your VPC must include
    	 one public subnet and one private subnet. Choose a
    	 public subnet for your VPC from the dropdown list.
    	 To continue, you must select the check box that
    	 indicates that the public subnet has been set up
    	 and the private subnet has outbound connectivity
    	 enabled.



    	If a subnet's traffic is routed to an
    	 internet gateway, the subnet is known as a public
    	 subnet. If, however, a subnet doesn't have a route
    	 to the internet gateway, the subnet is known as a
    	 private subnet.


    	To use an existing VPC that does
    	 not have a public subnet, you can add a new public
    	 subnet using the following steps:



    		- Follow the steps in [Creating a Subnet in the Amazon VPC User
    		 Guide](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Create_Subnet "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Create_Subnet") using the existing VPC you intend to
    		 use for AWS Launch Wizard.
    		- To add an internet gateway to your VPC,
    		 follow the steps in [Attaching an Internet Gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway") in the
    		 Amazon VPC User Guide.
    		- To configure your subnets to route internet
    		 traffic through the internet gateway, follow the
    		 steps in [Creating a Custom Route Table](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing") in the
    		 Amazon VPC User Guide. Use IPv4 format (0.0.0.0/0) for
    		 Destination.
    		- The public subnet should have the
    		 “auto-assign public IPv4 address” setting enabled.
    		 To enable this setting, follow the steps in [Modifying the Public IPv4 Addressing Attribute
    		 for Your Subnet](../../../vpc/latest/userguide/vpc-ip-addressing.md#subnet-public-ip "../../../vpc/latest/userguide/vpc-ip-addressing.md#subnet-public-ip") in the
    		 Amazon VPC User Guide.
    	+ **Availability Zone (AZ)
    	 configuration**. You must choose an
    	 Availability Zone and a private subnet for that zone. Cross-Region replication is not supported.



    	If a subnet doesn't have a route to an
    	 internet gateway, the subnet is known as a private
    	 subnet. To create a private subnet, you can use
    	 the following steps. We recommend that you enable
    	 the outbound connectivity for your selected private subnet using a NAT Gateway.


    	To enable outbound connectivity from the selected private subnet with public subnet, see the steps in [Creating a NAT Gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating") to create a NAT
    	 Gateway in your chosen public subnet.


    	Then, follow
    	 the steps in [Updating Your Route Table](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-create-route "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-create-route") for your chosen private subnet.



    		- Follow the steps in [Creating a Subnet](../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet "../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet") in the Amazon VPC User Guide
    		 using the existing VPC you will use in AWS
    		 Launch Wizard.
    		- When you create a VPC, it includes a main
    		 route table by default. On the **Route
    		 Tables** page in the Amazon VPC console,
    		 you can view the main route table for a VPC by
    		 looking for Yes in the Main column. The main route
    		 table controls the routing for all subnets that
    		 are not explicitly associated with any other route
    		 table. If the main route table for your VPC has an
    		 outbound route to an internet gateway, then any
    		 subnet created using the previous step, by
    		 default, becomes a public subnet. To ensure the
    		 subnets are private, you may need to create
    		 separate route table(s) for your private subnets.
    		 These route tables must not contain any routes to
    		 an internet gateway. Alternatively, you can create
    		 a custom route table for your public subnet and
    		 remove the internet gateway entry from the main
    		 route table.
    	+ **Remote Desktop Gateway
    	 preferences (single-node deployments
    	 only)**. When you select **Set up
    	 Remote Desktop Gateway**, enter the
    	 public subnet into which to deploy the RDGW
    	 instance.
    	+ (Optional) **Remote
    	 Desktop Gateway access**. Select
    	 **Custom IP** from the dropdown
    	 list. Enter the CIDR block. If you do not specify
    	 any value for the Custom IP parameter, Launch Wizard does
    	 not set the inbound RDP access (Port 3389) from
    	 any IP. You can choose to do this later by
    	 modifying the security group settings via the
    	 Amazon EC2 console. See [Adding a Rule for Inbound RDP Traffic to a
    	 Windows Instance](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access") for instructions on
    	 adding a rule that allows inbound RDP traffic to
    	 your RDGW instance.


    * **Create new Virtual Private
     Cloud (VPC)** option. Launch Wizard creates your
     VPC. You can optionally enter a **VPC name tag**.




    	+ **Remote Desktop Gateway
    	 preferences**. When you select
    	 **Set up Remote Desktop
    	 Gateway**, only the Remote Desktop
    	 Gateway access information will be taken from the
    	 VPC.
    	+ (Optional) **Remote
    	 Desktop Gateway access**. Select
    	 **Custom IP** from
    	 the dropdown list. Enter the CIDR block. If you do
    	 not specify any value for the Custom IP parameter,
    	 Launch Wizard does not set the inbound RDP access (Port
    	 3389) from any IP. You can choose to do this later
    	 by modifying the security group settings via the
    	 Amazon EC2 Console. See [Adding a Rule for Inbound RDP Traffic to a
    	 Windows Instance](../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access "../../../AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.md#add-rule-authorize-access") for instructions on
    	 adding a rule that allows inbound RDP traffic to
    	 your RDGW instance.

(Optional) Active Directory
SQL Server Developer Edition can be deployed with or
without Active Directory integration. To enable Active
Directory with the SQL Server Developer Edition Single Node
deployment, set the **Enable Active
Directory** toggle to on.

You can connect to an existing Active Directory or, when
creating a new VPC, you can create a new one. If you
selected the **Create new Virtual Private Cloud
(VPC)** option and want to enable Active
Directory, you must select **Create a new Active
Directory**.

###### Connecting to existing AWS Managed Active Directory

or Self Managed Active Directory

From the dropdown list, select whether you want to use
**AWS Managed Active Directory**,
or **Self Managed Active Directory**.
If you select **Self Managed Active
Directory**, select the check box to verify
that you have ensured a connection between the Active
Directory and the VPC.

Follow the steps for granting permissions in the
Active Directory.

    * **Domain user name and
     password**. Enter the user name and
     password for your directory. For required
     permissions for the domain user, see [Active Directory (Windows deployment)](launch-wizard-getting-started.md#launch-wizard-ad "launch-wizard-getting-started.md#launch-wizard-ad"). Launch Wizard stores
     the password in AWS Secrets Manager as a
     secure string parameter. It does not store the
     password on the service side. To create a functional
     SQL Server Developer Edition deployment, it reads
     from AWS Secrets Manager.
    * **DNS address**.
     Enter the IP address of the DNS servers to which you
     are connecting. These servers must be reachable from
     within the VPC that you selected.
    * **Optional DNS
     address**. If you would like to use a
     backup DNS server, enter the IP address of the DNS
     server that you want to use as backup. These servers
     must be reachable from within the VPC that you
     selected.
    * **Domain DNS name**.
     Enter the Fully Qualified Domain Name (FQDN) of the
      [forest root domain](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/selecting-the-forest-root-domain "https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/selecting-the-forest-root-domain")  used for the Active
     Directory. When you choose to create a new Active
     Directory, Launch Wizard creates a domain admin user on your
     Active Directory.
    * (Optional) **Organization Unit
     (OU) Path**. Specify the distinguished
     path name of the Organizational Unit (OU) within
     which you want to join for the Active Directory. For
     example: OU=org,DC=example,DC=com

###### Creating a new AWS Managed Active Directory through

Launch Wizard

    * **Domain user name and
     password**. The domain user name is
     preset to “admin.” Enter a password for your
     directory. Launch Wizard stores the password in
     AWS Secrets Manager as a secure string
     parameter. It does not store the password on the
     server side. To create a functional SQL Server
     Developer Edition deployment, it reads from
     AWS Secrets Manager.
    * **Domain DNS name**.
     Enter a Fully Qualified Domain Name (FQDN) of the
     forest root domain used for the Active Directory.
     When you choose to create a new Active Directory,
     Launch Wizard creates a domain admin user on your Active
     Directory.
    * (Optional) **Organization Unit
     (OU) Path**. Specify the distinguished
     path name of the Organizational Unit (OU) within
     which you want to join for the Active Directory. For
     example: OU=org,DC=example,DC=com

###### Connecting to a Self Managed Active Directory through

Launch Wizard

Launch Wizard allows you to connect to a Self Managed Active
Directory environment during deployment. For more
information, see [Self Managed Active Directory](launch-wizard-getting-started.md#launch-wizard-ad-onprem "launch-wizard-getting-started.md#launch-wizard-ad-onprem").

SQL Server configuration

When you use an existing Active Directory (if Active
Directory is enabled), you have the option of using an
existing SQL Server service account or creating a new
account. If you create a new Active Directory account,
you must create a new SQL Server account. If Active
Directory is disabled, skip this section and SQL Server
authentication will be configured.

    * **User name and
     password**. If you are using an existing
     SQL Server service account, provide your user name
     and password. This SQL Server service account should
     be part of the Managed Active Directory in which you
     are deploying. If you are creating a new SQL Server
     service account through Launch Wizard, enter a user name for
     the SQL Server service account. Create a complex
     password that is at least 8 characters long, and
     then reenter the password to verify it. See [Password Policy](https://docs.microsoft.com/en-us/sql/relational-databases/security/password-policy?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/security/password-policy?view=sql-server-2017") for more
     information.
    * **SQL Server install
     type**. Select the version of SQL Server that you want to deploy. You can select
     an AMI from either the License-included AMI or
     Custom AMI dropdown lists.
    * **License-included
     AMI**. Choose an AMI for your SQL Server
     deployment which determines the version and edition
     of Windows Server that will be deployed. Available
     options include:




    	+ Windows Server 2022: Full-base AMI with
    	 Windows Server 2022
    	+ Windows Server 2025: Full-base AMI with
    	 Windows Server 2025
    * (Optional) **tempdb
     configuration**. To improve performance,
     you can opt for the SQL Server tempdb system
     database to reside on a local NVMe SSD ephemeral
     storage device, also called the (instance store
     volume). NVMe SSD instance store volumes are
     available only on instance types that provide these
     local storage devices. Additionally, only data that
     changes frequently should ever reside on these
     volumes. They are not intended to store data
     long-term. For more information, see [Amazon EC2 instance store](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md").
    * (Optional) **Additional SQL
     Server settings**. You can specify the
     following:




    	+ **Node name**.
    	 Enter a **SQL node
    	 name** for the single instance
    	 deployment.

5. When you are satisfied with your configuration selections, select
   **Next**. If you don't want to complete the
   configuration, select **Cancel**. When you select
   **Cancel**, all of the selections on the
   specification page are lost and you are returned to the landing page. To
   go to the previous screen, select **Previous**.
6. After configuring your application, you are prompted to define the
   infrastructure requirements for the new deployment on the
   **Configure infrastructure settings** page. The
   following tabs provide information about the input fields.

Define SQL Server Developer Edition settings

Configure the SQL Server Developer Edition software
settings including version selection, license agreement,
and installation media source. You must accept the
Microsoft EULA and provide installation media either
through S3 or a direct download URL.

    * **SQL Server Developer Edition
     Version —** Select the version of
     SQL Server Developer Edition you want to
     install:




    	+ SQL Server 2022 Developer Edition
    * **Microsoft EULA Agreement
     —** You must review and agree to
     the license terms for the Microsoft software you are
     providing to AWS Launch Wizard. This is a mandatory
     requirement and the deployment cannot proceed
     without acceptance.
    * **Installation method
     —** Choose how you want to provide
     the SQL Server Developer Edition installation
     media.




    	+ *Bring Your Own
    	 Media*




    		- Provide a SQL Developer Edition installation
    		 media to be used for installing SQL Server
    		 Developer Edition.
    		- Select the S3 bucket that starts with
    		 "launchwizard" (e.g.,
    		 launchwizard-sql-media-bucket) containing your SQL
    		 Server installation files.
    	+ *Bring Your Own
    	 URL*


    	Launch Wizard will download the SQL Server Developer
    	 Edition installation media from a customer
    	 provided public URL.

Define compute and storage requirements

You can choose to select your instances and volume
types, or to use AWS recommended resources. If you
choose to use AWS recommended resources, you have the
option of defining your infrastructure needs.
If no selections are made, default values are
assigned.

    * **Number of instance
     cores**. Choose the number of CPU cores
     for your infrastructure. The default value assigned
     is 4.
    * **Network
     performance**. Choose your preferred
     network performance in Gbps.
    * **Memory (GB)**.
     Choose the amount of RAM that you want to attach to
     your EC2 instance. The default value assigned is 4
     GB.
    * **Type of storage
     drive**. Select the storage drive type
     for the SQL data and tempdb volumes. If you chose to
     place your tempdb on local storage, only the SQL
     data will be on the storage drive you select. The
     default value assigned is SSD.
    * **SQL Server
     throughput**. Select the sustained SQL
     Server throughput that you need.
    * **Recommended
     resources**. Launch Wizard displays the
     system-recommended resources based on your
     infrastructure selections. If you want to change the
     recommended resources, select different
     infrastructure requirements.

###### Infrastructure requirements based on instance

type

You can choose to select your instance and volume
type, or to use AWS recommended resources. If no
selections are made, default values are assigned.

    * **Instance type**.
     Select your preferred instance type from the
     dropdown list.
    * **Volume type**.
     Choose your preferred EBS volume type. For more
     information about volume types, see [Amazon EBS volume types](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md").

###### Drive letters and volume size

    * **Drive letter**.
     Select the storage drive letter for **Root
     drive**, **Logs**,
     **Data**, and
     **Backup** volumes.


    ###### Important

    For custom AMIs, Launch Wizard assumes the root volume
     drive is `C:`.
    * **Volume size**.
     Select the size of the SQL Server data volume in Gb
     for **Root drive**,
     **Logs**,
     **Data**, and
     **Backup** volumes. SQL Server
     logs and data will be staged on the same data volume
     for this deployment. Make sure that you select an
     adequate size for the data volume.

###### Note

For Launch Wizard deployments created after January 2023,
IMDSv1 is disabled on all instances. If your
software or scripts use IMDSv1, you will have to
meet the requirements to use IMDSv2. For more
information, see [Use IMDSv2](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md").

(Optional) Tags
You can provide optional custom tags for the resources
Launch Wizard creates on your behalf. For example, you can
set different tags for EC2 instances, EBS volumes, VPC, and
subnets. If you select **All**, you can
assign a common set of tags to your resources. Launch Wizard assigns
tags with a fixed key
`LaunchWizardResourceGroupID` and value that
corresponds to the ID of the AWS resource group created
for a deployment. Launch Wizard does not support custom tagging for
root volumes.

Estimated on-demand cost to deploy additional
resources
AWS Launch Wizard provides an estimate for application charges
incurred to deploy the selected resources. The estimate
updates each time you change a resource type in the Wizard.
The provided estimates are only for general comparisons.
They are based upon On-Demand costs and your actual costs
may be lower. 7. When you are satisfied with your infrastructure selections, select
**Next**. If you don't want to complete the
configuration, select **Cancel**. When you select
**Cancel**, all of the selections on the
specification page are lost and you are returned to the landing page. To
go to the previous screen, select **Previous**. 8. On the **Review and deploy** page, review your
configuration details. If you want to make changes, select
**Previous**. To stop, select
**Cancel**. When you select
**Cancel**, all of the selections on the
specification page are lost and you are returned to the landing page.
When you choose **Deploy**, you agree to the terms of
the **Acknowledgment**. 9. Launch Wizard validates the inputs and notifies you of any issues you must
address. 10. When validation is complete, Launch Wizard deploys your AWS resources and
configures your SQL Server Developer Edition application. Launch Wizard provides
you with status updates about the progress of the deployment on the
**Deployments** page. From the
**Deployments** page, you can view the
list of current and previous deployments. 11. When your deployment is ready, a notification informs you that your
SQL Server application is successfully deployed. If you have set up an
SNS notification, you are also alerted through SNS. You can manage and
access all of the resources related to your SQL Server Developer Edition
application by selecting the deployment, and then selecting
**Manage** from the **Actions** dropdown list. 12. When the SQL Server Developer Edition application is deployed, you can
access your Amazon EC2 instance through the EC2 console. You can also use
[AWS SSM](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") to manage your SQL Server Developer Edition
application for future updates and patches with built-in integration
through resource groups.
