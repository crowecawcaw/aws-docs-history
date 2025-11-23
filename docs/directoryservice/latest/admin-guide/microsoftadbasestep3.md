# Step 3: Deploy an Amazon EC2 instance to manage your AWS Managed Microsoft AD Active Directory

For this lab, we are using Amazon EC2 instances that have public IP addresses to make it easy to
access the management instance from anywhere. In a production setting, you can use instances
that are in a private VPC that are only accessible through a VPN or Direct Connect
link. There is no requirement the instance have a public IP address.

In this section, you walk through the various post-deployment tasks necessary for client
computers to connect to your domain using the Windows Server on your new EC2 instance. You use
the Windows Server in the next step to verify that the lab is operational.

## Optional: Create a DHCP options set in AWS-DS-VPC01

for your directory

In this optional procedure, you set up a DHCP option scope so that EC2 instances in your
VPC automatically use your AWS Managed Microsoft AD for DNS resolution. For more information, see [DHCP options
sets](../../../AmazonVPC/latest/UserGuide/VPC_DHCP_Options.md "../../../AmazonVPC/latest/UserGuide/VPC_DHCP_Options.md").

###### To create a DHCP options set for your directory

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **DHCP Options Sets**, and then
   choose **Create DHCP options set**.
3. On the **Create DHCP options set** page, provide the following
   values for your directory:
   - For **Name**, type `AWS DS DHCP`.
   - For **Domain name**, type
     `corp.example.com`.
   - For **Domain name servers**, type the IP addresses of your
     AWS provided directory's DNS servers.

   ###### Note

   To find these addresses, go to the Directory Service **Directories**
   page, and then choose the applicable directory ID. On the
   **Details** page, identify and use the IPs that are displayed
   in **DNS address**.

   Alternatively, to find these addresses, go to the Directory Service
   **Directories** page, and choose the applicable directory ID.
   Then, choose **Scale & share**. Under **Domain
   controllers**, identify and use the IPs that are displayed in
   **IP address**.
   - Leave the settings blank for **NTP servers**, **NetBIOS
     name servers**, and **NetBIOS node type**.

4. Choose **Create DHCP options set**, and then choose
   **Close**. The new set of DHCP options appear in your list of DHCP
   options.
5. Make a note of the ID of the new set of DHCP options
   (**dopt-`xxxxxxxx`**). You use it at the
   end of this procedure when you associate the new options set with your VPC.

###### Note

Seamless domain join works without having to configure a DHCP Options Set. 6. In the navigation pane, choose **Your VPCs**. 7. In the list of VPCs, select **AWS DS VPC**, choose
**Actions**, and then choose **Edit DHCP options
set**. 8. On the **Edit DHCP options set** page, select the options set that
you recorded in Step 5, and then choose **Save**.

## Create a role to join Windows instances to your AWS Managed Microsoft AD

domain

Use this procedure to configure a role that joins an Amazon EC2 Windows instance to a domain.
For more information, see [Joining an Amazon EC2 Windows instance to your AWS Managed Microsoft AD
Active Directory](launching_instance.md "launching_instance.md").

###### To configure EC2 to join Windows instances to your domain

1.  Open the IAM console at
    [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane of the IAM console, choose **Roles**, and
    then choose **Create role**.
3.  Under **Select type of trusted entity**, choose **AWS
    service**.
4.  Immediately under **Choose the service that will use this role**,
    choose **EC2**, and then choose **Next:
    Permissions**.
5.  On the **Attached permissions policy** page, do the
    following:

        * Select the box next to the **AmazonSSMManagedInstanceCore**
         managed policy. This policy provides the minimum permissions necessary to use the
         Systems Manager service.
        * Select the box next to **AmazonSSMDirectoryServiceAccess**
         managed policy. The policy provides the permissions to join instances to an Active
         Directory managed by Directory Service.

    For information about these managed policies and other policies you can attach to an
    IAM instance profile for Systems Manager, see [Create an IAM instance profile for
    Systems Manager](../../../systems-manager/latest/userguide/setup-instance-profile.md "../../../systems-manager/latest/userguide/setup-instance-profile.md") in the _AWS Systems Manager User Guide_. For information about
    managed policies, see [AWS
    Managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

6.  Choose **Next: Tags**.
7.  (Optional) Add one or more tag key-value pairs to organize, track, or control access
    for this role, and then choose **Next: Review**.
8.  For **Role name**, enter a name for the role that
    describes that it is used to join instances to a domain, such as
    **EC2DomainJoin**.
9.  (Optional) For **Role description**, enter a description.
10. Choose **Create role**. The system returns you to the
    **Roles** page.

## Create an Amazon EC2 instance and automatically join the

directory

In this procedure you set up a Windows Server system in a EC2 instance that can be used later to
administer users, groups, and policies in Active Directory.

###### To create an EC2 instance and automatically join the directory

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Launch Instance**.
3. On the **Step 1** page, next to **Microsoft Windows Server
   2019 Base - ami-`xxxxxxxxxxxxxxxxx`** choose
   **Select**.
4. On the **Step 2** page, select **t3.micro** (note,
   you can choose a larger instance type), and then choose **Next: Configure
   Instance Details**.
5. On the **Step 3** page, do the following:
   - For **Network**, choose the VPC that ends with
     **AWS-DS-VPC01** (for example,
     **vpc-`xxxxxxxxxxxxxxxxx` |
     AWS-DS-VPC01**).
   - For **Subnet** choose **Public subnet 1**,
     which should be preconfigured for your preferred Availability Zone (for example,
     **subnet-`xxxxxxxxxxxxxxxxx` |
     AWS-DS-VPC01-Subnet01 | `us-west-2a`**).
   - For **Auto-assign Public IP**, choose
     **Enable** (if the subnet setting is not set to enable by
     default).
   - For **Domain join directory**, choose
     **corp.example.com
     (d-`xxxxxxxxxx`)**.
   - For **IAM role** choose the name you gave your instance role in
     [Create a role to join Windows instances to your AWS Managed Microsoft AD
     domain](#configureec2 "#configureec2"), such as
     **EC2DomainJoin**.
   - Leave the rest of the settings at their defaults.
   - Choose **Next: Add Storage**.

6. On the **Step 4** page, leave the default settings, and then choose
   **Next: Add Tags**.
7. On the **Step 5** page, choose **Add Tag**. Under
   **Key** type `corp.example.com-mgmt` and then
   choose **Next: Configure Security Group**.
8. On the **Step 6** page, choose **Select an
   existing security group**, select **AWS DS Test Lab Security
   Group** (which you previously set up in the [Base tutorial](microsoftadbasestep1.md#createsecuritygroup "microsoftadbasestep1.md#createsecuritygroup")), and then choose
   **Review and Launch** to review your instance.
9. On the **Step 7** page, review the page, and then choose
   **Launch**.
10. On the **Select an existing key pair or create a new key pair**
    dialog box, do the following:
    - Choose **Choose an existing key pair**.

    - Under **Select a key pair**, choose
      **AWS-DS-KP**.
    - Select the **I acknowledge...** check box.
    - Choose **Launch Instances**.

11. Choose **View Instances** to return to the Amazon EC2 console and view
    the status of the deployment.

## Install the Active Directory tools on your EC2

instance

You can choose from two methods to install the Active Directory Domain Management Tools
on your EC2 instance. You can use the Server Manager UI (recommended for this tutorial) or
PowerShell.

###### To install the Active Directory tools on your EC2 instance (Server Manager)

1. In the Amazon EC2 console, choose **Instances**, select the instance you
   just created, and then choose **Connect**.
2. In the **Connect To Your Instance** dialog box, choose
   **Get Password** to retrieve your password if you haven't already,
   and then choose **Download Remote Desktop File**.
3. In the **Windows Security** dialog box, type your local
   administrator credentials for the Windows Server computer to log in (for example,
   `administrator`).
4. From the **Start** menu, choose **Server
   Manager**.
5. In the **Dashboard**, choose **Add Roles and
   Features**.
6. In the **Add Roles and Features Wizard**, choose
   **Next**.
7. On the **Select installation type** page, choose
   **Role-based or feature-based installation**, and then choose
   **Next**.
8. On the **Select destination server** page, make sure that the local
   server is selected, and then choose **Next**.
9. On the **Select server roles** page, choose
   **Next**.
10. On the **Select features** page, do the following:
    - Select the **Group Policy Management** check box.
    - Expand **Remote Server Administration Tools**, and then expand
      **Role Administration Tools**.
    - Select the **AD DS and AD LDS Tools** check box.
    - Select the **DNS Server Tools** check box.
    - Choose **Next**.

11. On the **Confirm installation selections** page, review the
    information, and then choose **Install**. When the feature installation
    is finished, the following new tools or snap-ins will be available in the Windows
    Administrative Tools folder in the Start menu.
    - Active Directory Administrative Center
    - Active Directory Domains and Trusts
    - Active Directory Module for PowerShell
    - Active Directory Sites and Services
    - Active Directory Users and Computers
    - ADSI Edit
    - DNS
    - Group Policy Management

###### To install the Active Directory tools on your EC2 instance (PowerShell)

(Optional)

1. Start PowerShell.
2. Type the following command.

```
Install-WindowsFeature -Name GPMC,RSAT-AD-PowerShell,RSAT-AD-AdminCenter,RSAT-ADDS-Tools,RSAT-DNS-Server
```
