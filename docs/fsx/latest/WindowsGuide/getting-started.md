# Getting started with Amazon FSx for Windows File Server

Following, you can learn how to get started using FSx for Windows File Server.
This getting started exercise includes the following steps.

1. Sign up for an AWS account and create an administrative user in the account.
2. Create an AWS Managed Microsoft AD Active Directory using the Directory Service. You will join your file system and compute instance to the Active Directory.
3. Create an Amazon Elastic Compute Cloud compute instance running Microsoft Windows Server. You will use this instance to access your file system.
4. Create an Amazon FSx for Windows File Server file system using the Amazon FSx console.
5. Map your file system to your EC2 instance
6. Write data to your file system.
7. Back up your file system.
8. Clean up the resources you created.

###### Topics

- [Setting up your AWS account](#setting-up "#setting-up")
- [Step 1. Setting up an Active Directory](#prereq-step1 "#prereq-step1")
- [Step 2: Launch a Windows instance in the Amazon EC2 console](#prereqs-step2 "#prereqs-step2")
- [Step 3: Connect to your instance](#prereqs-step3 "#prereqs-step3")
- [Step 4: Join your instance to your Directory Service directory](#prereqs-step4 "#prereqs-step4")
- [Step 5. Create your file system](#getting-started-step1 "#getting-started-step1")
- [Step 6. Map your file share to an EC2 instance running
  Windows Server](#getting-started-step2 "#getting-started-step2")
- [Step 7. Write data to your file share](#getting-started-step3 "#getting-started-step3")
- [Step 8. Back up your file system](#getting-started-step4 "#getting-started-step4")
- [Step 9. Clean up resources](#getting-started-step5 "#getting-started-step5")

## Setting up your AWS account

Before you use Amazon FSx for the first time, complete the following tasks:

1. [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
2. [Create a user with administrative access](#create-an-admin "#create-an-admin")

###

#### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

#### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Step 1. Setting up an Active Directory

With Amazon FSx, you can operate fully managed file storage for Windows-based workloads.
Likewise, Directory Service provides fully managed directories to use in your workload deployment. If you
have an existing corporate Active Directory domain running in AWS in a virtual private cloud (VPC) using EC2
instances, you can enable user-based authentication and access control. You do this by
establishing a trust relationship between your AWS Managed Microsoft Active Directory and your corporate
domain. For Windows authentication in Amazon FSx, you only need a one-way directional forest trust,
where the AWS managed forest trusts the corporate domain forest.

Your corporate domain takes the role of the trusted domain, and the Directory Service managed domain
takes the role of the trusting domain. Validated authentication requests travel between the
domains in only one direction—allowing accounts in your corporate domain to authenticate
against resources shared in the managed domain. In this case, Amazon FSx interacts only with the
managed domain. The managed domain then passes on the authentication requests to your corporate
domain.

###### Note

You can also use an external trust type with Amazon FSx for trusted domains.

Your Active Directory security group must enable inbound access from the Amazon FSx file system’s
security group.

###### To create an AWS Directory Services for Microsoft Active Directory

- If you don't already have one, use the Directory Service to create your AWS Managed Microsoft
  Active Directory directory. For more information, see [Create Your AWS Managed
  Microsoft Active Directory](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.md") in the _AWS Directory Service Administration Guide_.

###### Important

Remember the password you assign to your Admin user; you need it later in this getting
started exercise. If you forget the password, you need to repeat steps in this exercise with
the new Directory Service directory and Admin user.

- If you have an existing Active Directory, create a trust relationship between your AWS Managed Microsoft
  Active Directory and your existing Active Directory. For more information, see [When to Create a Trust Relationship](../../../directoryservice/latest/admin-guide/ms_ad_setup_trust.md "../../../directoryservice/latest/admin-guide/ms_ad_setup_trust.md") in the
  _AWS Directory Service Administration Guide._

## Step 2: Launch a Windows instance in the Amazon EC2 console

You can launch a Windows instance using the AWS Management Console as described in the following
procedure. This is intended to help you launch your first instance quickly, so it doesn't cover
all possible options. For more information about the advanced options, see [Launching an Instance](../../../AWSEC2/latest/UserGuide/launching-instance.md "../../../AWSEC2/latest/UserGuide/launching-instance.md").

###### To launch an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the console dashboard, choose **Launch Instance**.
3. The **Choose an Amazon Machine Image (AMI)** page displays a list of
   basic configurations, called _Amazon Machine Images (AMIs)_, that serve as
   templates for your instance. Select the AMI for Windows Server 2016 Base or later. Notice
   that these AMIs are marked "Free tier eligible."
4. On the **Choose an Instance Type** page, you can select the hardware
   configuration of your instance. Select the `t2.micro` type, which is selected by
   default. Notice that this instance type is eligible for the free tier.
5. Choose **Review and Launch** to let the wizard complete the other
   configuration settings for you.
6. On the **Review Instance Launch** page, under **Security
   Groups**, a security group appears that the wizard created and selected for you. You
   can use this security group, or you can choose the security group that you created when getting
   set up using the following steps:
   1. Choose **Edit security groups**.
   2. On the **Configure Security Group** page, ensure that **Select
      an existing security group** is selected.
   3. Select your security group from the list of existing security groups, and then choose
      **Review and Launch**.

7. On the **Review Instance Launch** page, choose
   **Launch**.
8. When prompted for a key pair, select **Choose an existing key pair**,
   then select the key pair that you created when getting set up.

Alternatively, you can create a new key pair. Select **Create a new key
pair**, enter a name for the key pair, and then choose **Download Key
Pair**. This is the only chance for you to save the private key file, so be sure to
download it. Save the private key file in a safe place. You'll need to provide the name of your
key pair when you launch an instance and the corresponding private key each time you connect to
the instance.

###### Warning

Don't select the **Proceed without a key pair** option. If you launch
your instance without a key pair, then you can't connect to it.

When you are ready, select the acknowledgement check box, and then choose **Launch
Instances**. 9. A confirmation page lets you know that your instance is launching. Choose **View
Instances** to close the confirmation page and return to the console. 10. On the **Instances** screen, you can view the status of the launch. It
takes a short time for an instance to launch. When you launch an instance, its initial state is
`pending`. After the instance starts, its state changes to `running` and
it receives a public DNS name. (If the **Public DNS (IPv4)** or
**(IPv6)** column is hidden,
choose **Show/Hide Columns** (the gear-shaped icon) in the top right corner of
the page and then select **Public DNS (IPv4)** or
**(IPv6)**.) 11. It can take a few minutes for the instance to be ready so that you can connect to it.
Check that your instance has passed its status checks; you can view this information in the
**Status Checks** column.

###### Important

Make a note of the ID of the security group that was created when you launched this
instance. You'll need it when you create your Amazon FSx file system.

Now that your instance is launched, you can connect to your instance.

## Step 3: Connect to your instance

To connect to a Windows instance, you must retrieve the initial administrator password and
then specify this password when you connect to your instance using Remote Desktop.

The name of the administrator account depends on the language of the operating system. For
example, for English it's Administrator, for French it's Administrateur, and for
Portuguese it's Administrador. For more information, see [Localized Names for Administrator Account in Windows](http://social.technet.microsoft.com/wiki/contents/articles/13813.localized-names-for-administrator-account-in-windows.aspx "http://social.technet.microsoft.com/wiki/contents/articles/13813.localized-names-for-administrator-account-in-windows.aspx") in the Microsoft TechNet
Wiki.

If you joined your instance to a domain, you can connect to your instance using domain
credentials you defined in Directory Service. On the Remote Desktop login screen, don't use the local
computer name and the generated password. Instead, use the fully qualified user name for the
administrator and the password for this account. An example is
`corp.example.com\Admin`.

The license for the Windows Server operating system (OS) allows two simultaneous remote
connections for administrative purposes. The license for Windows Server is included in the price
of your Windows instance. If you need more than two simultaneous remote connections, you must
purchase a Remote Desktop Services (RDS) license. If you attempt a third connection, an error
occurs. For more information, see [Configure the Number of
Simultaneous Remote Connections Allowed for a Connection](http://technet.microsoft.com/en-us/library/cc753380.aspx "http://technet.microsoft.com/en-us/library/cc753380.aspx").

###### To connect to your Windows instance using an RDP client

1. In the Amazon EC2 console, select the instance, and then choose
   **Connect**.
2. In the **Connect to Your Instance** dialog box, choose **Get
   Password** (it takes a few minutes after the instance is launched before the password
   is available).
3. Choose **Browse** and navigate to the private key file you created when
   you launched the instance. Select the file and choose **Open** to copy the
   entire contents of the file into the **Contents** field.
4. Choose **Decrypt Password**. The console displays the default
   administrator password for the instance in the **Connect to Your Instance**
   dialog box, replacing the link to **Get Password** shown previously with the
   actual password.
5. Record the default administrator password, or copy it to the clipboard. You need this
   password to connect to the instance.
6. Choose **Download Remote Desktop File**. Your browser prompts you to
   either open or save the .rdp file. Either option is fine. When you have finished, you can
   choose **Close** to dismiss the **Connect to Your Instance**
   dialog box.
   - If you opened the .rdp file, you see the **Remote Desktop Connection**
     dialog box.
   - If you saved the .rdp file, navigate to your downloads directory, and open the .rdp file
     to display the dialog box.

7. You may get a warning that the publisher of the remote connection is unknown. You can
   continue to connect to your instance.
8. When prompted, log in to the instance, using the administrator account for the operating
   system and the password that you recorded or copied previously. If your **Remote
   Desktop Connection** already has an administrator account set up, you might have to
   choose the **Use another account** option and type the user name and password
   manually.

###### Note

Sometimes copying and pasting content can corrupt data. If you encounter a "Password
Failed" error when you log in, try typing in the password manually. 9. Due to the nature of self-signed certificates, you may get a warning that the security
certificate could not be authenticated. Use the following steps to verify the identity of the
remote computer, or simply choose **Yes** or **Continue** to
continue if you trust the certificate.

    1. If you are using **Remote Desktop Connection** from a Windows PC,
     choose **View certificate**. If you are using **Microsoft Remote
     Desktop** on a Mac, choose **Show Certificate**.
    2. Choose the **Details** tab, and scroll down to the
     **Thumbprint** entry on a Windows PC, or the **SHA1
     Fingerprints** entry on a Mac. This is the unique identifier for the remote
     computer's security certificate.
    3. In the Amazon EC2 console, select the instance, choose **Actions**, and then
     choose **Get System Log**.
    4. In the system log output, look for an entry labeled
     `RDPCERTIFICATE-THUMBPRINT`. If this value matches the thumbprint or fingerprint
     of the certificate, you have verified the identity of the remote computer.
    5. If you are using **Remote Desktop Connection** from a Windows PC,
     return to the **Certificate** dialog box and choose **OK**.
     If you are using **Microsoft Remote Desktop** on a Mac, return to the
     **Verify Certificate** and choose **Continue**.
    6. [Windows] Choose **Yes** in the **Remote Desktop
     Connection** window to connect to your instance.

Now that you're connected to your instance, you can join the instance to your Directory Service
directory.

## Step 4: Join your instance to your Directory Service directory

The following procedure shows you how to manually join an existing Amazon EC2 Windows instance to
your Directory Service directory.

###### To join a Windows instance to your Directory Service directory

1. Connect to the instance using any Remote Desktop Protocol client.
2. Open the TCP/IPv4 or IPv6 properties dialog box on the instance.
   1. Open **Network Connections**.

   ###### Tip

   You can open **Network Connections** directly by running the following
   from a command prompt on the instance.

   ```
   %SystemRoot%\system32\control.exe ncpa.cpl
   ```

   2. Open the context (right-click) menu for any enabled network connection and then choose
      **Properties**.
   3. In the connection properties dialog box, open (double-click) **Internet Protocol Version 4**
      or **Internet Protocol Version 6**.

3. (Optional) Select **Use the following DNS server addresses**, change the
   **Preferred DNS server** and **Alternate DNS server**
   addresses to the IPv4 or IPv6 addresses of the Directory Service–provided DNS servers, and choose
   **OK**.
4. Open the **System Properties** dialog box for the instance, choose the
   **Computer Name** tab, and choose **Change**.

###### Tip

You can open the **System Properties** dialog box directly by running
the following from a command prompt on the instance.

```
%SystemRoot%\system32\control.exe sysdm.cpl
```

5. In the **Member of** box, choose **Domain**, enter the
   fully qualified name of your Directory Service directory, and choose **OK**.
6. When prompted for the name and password for the domain administrator, enter the user name
   and password of the Admin account.

###### Note

You can enter either the fully qualified name of your domain or the NetBios name,
followed by a backslash (\), and then the user name, in this case, **Admin**.
For example, **corp.example.com\Admin** or
**corp\Admin**. 7. After you receive the message welcoming you to the domain, restart the instance to have
the changes take effect. 8. Reconnect to your instance over RDP, and sign into the instance using the user name and
password for your Directory Service directory's Admin user.

Now that your instance has been joined to the domain, you're ready to create your Amazon FSx file
system.

## Step 5. Create your file system

###### To create your file system (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. On the dashboard, choose **Create file system** to start the file
   system creation wizard.
3. On the **Select file system type** page, choose
   **FSx for Windows File Server**, and then choose **Next**. The
   **Create file system** page appears.
4. For **Creation method** choose **Standard create**.

###### File system details

1.  In the **File system details** section, provide a name for your file
    system. It's easier to find and manage your file systems when you name them. You can use a
    maximum of 256 Unicode letters, white space, and numbers, plus the special characters + -
    = . \_ : /
2.  For **Deployment type** choose **Multi-AZ** or
    **Single-AZ**.

        * Choose **Multi-AZ** to deploy a file system that is tolerant to
         Availability Zone unavailability. This option supports SSD and HDD storage.
        * Choose **Single-AZ** to deploy a file system that is deployed in
         a single Availability Zone. *Single-AZ 2* is the latest generation
         of single Availability Zone file systems, and it supports SSD and HDD storage.

    For more information, see [Availability and durability: Single-AZ and Multi-AZ file systems](high-availability-multiAZ.md "high-availability-multiAZ.md").

3.  For **Storage type**, you can choose either **SSD**
    or **HDD**.

FSx for Windows File Server offers solid state drive (SSD) and hard disk drive (HDD) storage types.
**SSD** storage is designed for the highest-performance and most
latency-sensitive workloads, including databases, media processing workloads, and data
analytics applications. **HDD** storage is designed for a broad spectrum
of workloads, including home directories, user and departmental file shares, and content
management systems. For more information, see [About storage types](managing-storage-configuration.md#about-storage-types "managing-storage-configuration.md#about-storage-types"). 4. For **Provisioned SSD IOPS**, you can choose either **Automatic**
or **User-provisioned** mode.

If you choose Automatic mode, FSx for Windows File Server automatically scales your SSD IOPS to maintain 3 SSD IOPS per GiB of storage capacity.
If you choose User-provisioned mode, enter any whole number in the range of 96–400,000. Scaling SSD IOPS above 80,000 is available
in US East (N. Virginia), US West (Oregon),
US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo), and Asia Pacific (Singapore). For more information, see [Managing SSD IOPS](managing-storage-configuration.md#managing-provisioned-ssd-iops "managing-storage-configuration.md#managing-provisioned-ssd-iops"). 5. For **Storage capacity**, enter the storage capacity of your file
system, in GiB. If you're using SSD storage, enter any whole number in the range of
32–65,536. If you're using HDD storage, enter any whole number in the range of
2,000–65,536. You can increase the amount of storage capacity as needed at any time
after you create the file system. For more information, see [Managing storage capacity](managing-storage-configuration.md#managing-storage-capacity "managing-storage-configuration.md#managing-storage-capacity"). 6. Keep **Throughput capacity** at its default setting.
**Throughput capacity** is the sustained speed at which the file server
that hosts your file system can serve data. The **Recommended throughput
capacity** setting is based on the amount of storage capacity you choose. If
you need more than the recommended throughput capacity, choose **Specify
throughput capacity**, and then choose a value. For more information, see [FSx for Windows File Server performance](performance.md "performance.md").

###### Note

If you are going to enable file access auditing, you must choose a throughput
capacity of 32 MBps or greater. For more information, see [Logging end user access with file access auditing](file-access-auditing.md "file-access-auditing.md").

You can modify the throughput capacity as needed at any time after you create the file
system. For more information, see [Managing throughput capacity](managing-throughput-capacity.md "managing-throughput-capacity.md").

###### Network & security

1.  In the **Network & security** section, choose the Amazon VPC that you
    want to associate with your file system. For this getting started exercise, choose the
    same Amazon VPC that you chose for your Directory Service directory and your Amazon EC2 instance.
2.  For **VPC Security Groups**, the default security group for your
    default Amazon VPC is already added to your file system in the console. If you're not
    using the default security group, make sure that the security group you choose is in
    the same AWS Region as your file system. To ensure that you can connect an EC2 instance
    with your file system, you will need to add the following rules to your
    chosen security group:
    1. Add the following inbound and outbound rules to allow the following ports.

    | Rules | Ports                                                                |
    | ----- | -------------------------------------------------------------------- |
    | UDP   | 53, 88, 123, 389, 464                                                |
    | TCP   | 53, 88, 135, 389, 445, 464, 636, 3268, 3269, 5985, 9389, 49152-65535 |

    Add from and to IP addresses or security group IDs associated with the client
    compute instances that you want to access your file system from. 2. Add outbound rules to allow all traffic to the Active Directory that you're
    joining your file system to. To do this, do one of the following:

        * Allow outbound traffic to the security group ID associated with your AWS
         Managed AD directory.
        * Allow outbound traffic to the IP addresses associated with your self-managed
         Active Directory domain controllers.###### Note

In some cases, you might have modified the rules of your AWS Managed Microsoft AD security group
from the default settings. If so, make sure that this security group has the required
inbound rules to allow traffic from your Amazon FSx file system. For more information about
the required inbound rules, see [AWS Managed Microsoft AD
Prerequisites](../../../directoryservice/latest/admin-guide/ms_ad_getting_started_prereqs.md "../../../directoryservice/latest/admin-guide/ms_ad_getting_started_prereqs.md") in the _AWS Directory Service Administration Guide_.

For more information, see [File system access control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md"). 3. Multi-AZ file systems have a primary and a standby file server, each in its own Availability
Zone and subnet. If you are creating a Multi-AZ file system (see step 5), choose a **Preferred
subnet** value for the primary file server and a **Standby
subnet** value for the standby file server.

If you are creating a Single-AZ file system, choose the **Subnet** for your file system. 4. For **Network type**, select either **IPv4**
(for only IPv4 support) or **Dual-stack** (for both IPv4
and IPv6 support). You can change the network type of an existing file system
at any time. For more information,
see [Changing network type](manage-network-type.md#change-network-type "manage-network-type.md#change-network-type").

###### Note

If you intend to create an FSx for Windows File Server file system that uses dual-stack mode, you must first assign an
Amazon-provided IPv6 CIDR block to your VPC and subnets. For more information, see [Add IPv6 support for your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md "../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md") in the
_Amazon Virtual Private Cloud User Guide_.

###### Windows authentication

- For **Windows authentication**, you have the following
  options:

Choose **AWS Managed Microsoft Active Directory** if you want
to join your file system to a Microsoft Active Directory domain that is
managed by AWS, and then choose your Directory Service directory from the list. For more information, see [Working with Microsoft Active Directory](aws-ad-integration-fsxW.md "aws-ad-integration-fsxW.md").

Choose **Self-managed Microsoft Active Directory** if you want
to join your file system to a self-managed Microsoft Active Directory
domain, and provide the following details for your Active Directory.
For more information see
[Using a self-managed Microsoft Active Directory](self-managed-AD.md "self-managed-AD.md").

    + The fully qualified domain name of your Active Directory.


    ###### Important

    For Single-AZ 2 and all Multi-AZ file systems, the Active Directory domain name
     cannot exceed 47 characters. This limitation applies to both Directory Service and
     self-managed Active Directory domain names.

    Amazon FSx requires a direct connection for internal traffic to your DNS IP address.
     Connection via an internet gateway is not supported. Instead, use AWS Virtual Private Network, VPC peering,
     Direct Connect, or AWS Transit Gateway association.
    + **DNS server IP addresses**—the IPv4 or IPv6 addresses of the DNS
     servers for your domain.


    ###### Note

    Your DNS server must have EDNS (Extension Mechanisms for DNS) enabled. If EDNS
     is disabled, your file system might fail to create.
    + Credentials for an Active Directory service account that Amazon FSx uses to join the file system to your domain. You can provide these as either:




    	- **Option 1**: AWS Secrets Manager secret ARN - The secret containing the username and password for a service account on your Active Directory domain. For more information, see [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows "self-managed-AD.md#bp-store-ad-creds-using-secret-manager-windows").
    	- **Option 2**: Plaintext credentials




    		* **Service account username** – The user name of the service account in your existing Microsoft Active Directory. Don't include a domain prefix or suffix. For example, for `EXAMPLE\ADMIN`, use only `ADMIN`.
    		* **Service account password** – The password for the service account.
    + (Optional) **Organizational Unit (OU)**—the distinguished
     path name of the organizational unit in which you want to join your file
     system.
    + (Optional) **Delegated file system administrators group**—
     the name of the group in your Active Directory that can administer your file system.
     The default group is 'Domain Admins'. For more information, see
     [Amazon FSx service account](self-managed-AD.md#self-managed-AD-service-account "self-managed-AD.md#self-managed-AD-service-account").

###### Encryption, Auditing, and Access (DNS aliases)

1. For **Encryption**, choose the AWS KMS key **Encryption
   key** used to encrypt the data on your file system at rest. You can choose the default
   **aws/fsx (default)** that is managed by AWS KMS, an existing key, or a customer managed key
   by specifying the ARN for the key. For more information, see
   [Encryption of data at rest](encryption-at-rest.md "encryption-at-rest.md").
2. For **Auditing - optional**, file access auditing is disabled by
   default. For information about enabling and configuring file access auditing, see [Logging end user access with file access auditing](file-access-auditing.md "file-access-auditing.md").
3. For **Access - optional**, enter any DNS aliases that you want to
   associate with the file system. Each alias name must be formatted as a fully qualified
   domain name (FQDN). For more information, see [Managing DNS aliases](managing-dns-aliases.md "managing-dns-aliases.md").

###### Backup and maintenance

For more information about automatic daily backups and the settings in this
section, see [Protecting your data with backups](using-backups.md "using-backups.md").

1. **Daily automatic backup** is enabled by default. You can
   disable this setting if you do not want Amazon FSx to take backups of your file system automatically
   on a daily basis.
2. If automatic backups are enabled, they occur within a time period known as the backup window. You can use the default
   window, or choose an **Automatic backup window start time** that is best for your workflow.
3. For **Automatic backup retention period**, you can use the default setting of
   **30** days, or set a value between 1 and 90 days that Amazon FSx will retain
   automatic daily backups of your file system for. This setting does not apply to user initiated backups,
   or backups taken by AWS Backup.
4. For **Tags - optional**, enter a key and value to add tags to your
   file system. A tag is a case-sensitive key-value pair that helps you manage, filter, and
   search for your file system. For more information, see
   [Tagging your Amazon FSx resources](tag-resources.md "tag-resources.md").

Choose **Next**.

###### Review your configuration and create

1. Review the file system configuration shown on the **Create file
   system** page. For your reference, you can see which file system settings you can and
   can't modify after file system is created. Choose **Create file system**.
2. After Amazon FSx creates the file system, choose the file system ID from the list
   in the **File Systems** dashboard to view the details. Choose **Attach**,
   and note the **DNS name** for your file system the **Network & security** tab.
   You will need it in the following procedure to map a share to an EC2 instance.

## Step 6. Map your file share to an EC2 instance running

Windows Server

You can now mount your Amazon FSx file system to your Microsoft Windows–based Amazon EC2
instance joined to your Directory Service directory. The name of your file share is not the same as the
name of your file system.

###### To map a file share on an Amazon EC2 Windows instance using the GUI

1. Before you can mount a file share on a Windows instance, you must launch the EC2
   instance and join it to the AWS Directory Service for Microsoft Active Directory that your file system has joined.
   To perform this action, choose one of the
   following procedures from the AWS Directory Service Administration Guide:
   - [Seamlessly join a Windows EC2
     instance](../../../directoryservice/latest/admin-guide/launching_instance.md "../../../directoryservice/latest/admin-guide/launching_instance.md")
   - [Manually join a Windows
     instance](../../../directoryservice/latest/admin-guide/join_windows_instance.md "../../../directoryservice/latest/admin-guide/join_windows_instance.md")

2. Connect to your instance. For more information, see [Connecting to Your Windows
   Instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md") in the _Amazon EC2 User Guide_.
3. When you're connected, open File Explorer.
4. From the navigation pane, open the context (right-click) menu for
   **Network** and choose **Map Network Drive**.
5. Choose a drive letter of your choice for **Drive**.
6. You can map your file system using either its default DNS name assigned by Amazon FSx, or
   using a DNS alias of your choosing. This procedure describes mapping a file share using
   the default DNS name. If you want to map a file share using a DNS alias, see
   [Accessing data using DNS aliases](dns-aliases.md "dns-aliases.md").

For **Folder**, enter the file system DNS name and the share name.
The default Amazon FSx share is called `\share`. You can find the DNS name in the
Amazon FSx console, [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/"), **Windows File Server > Network &
Security** section, or in the response of **CreateFileSystem**
or **DescribeFileSystems** API command.

    * For a Single-AZ file system joined to an AWS Managed Microsoft Active Directory, the DNS name looks like the
     following.



    ```
    fs-0123456789abcdef0.`ad-domain`.com
    ```
    * For a Single-AZ file system joined to a self-managed Active Directory, and any
     Multi-AZ file system, the DNS name looks like the following.



    ```
    amznfsxaa11bb22.`ad-domain`.com
    ```

For example, enter
`\\fs-0123456789abcdef0.`ad-domain`.com\share`. 7. Choose whether the file share should **Reconnect at sign-in**, and
then choose **Finish**.

## Step 7. Write data to your file share

Now that you've mapped your file share to your instance, you can use your file share like
any other directory in your Windows environment.

###### To write data to your file share

1. Open the Notepad text editor.
2. Write some content in the text editor. For example: `Hello,
World!`
3. Save the file to your file share's drive letter.
4. Using File Explorer, navigate to your file share and find the text file that you just
   saved.

## Step 8. Back up your file system

Now that you've had a chance to use your Amazon FSx file system and its file shares, you can
back it up. By default, daily backups are created automatically during your file system's
30-minute backup window. However you can create a user-initiated backup at any time. Backups
have additional costs associated with them. For more information on backup pricing, see [Pricing](https://aws.amazon.com/fsx/windows/pricing "https://aws.amazon.com/fsx/windows/pricing").

###### To create a backup of your file system from the console

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the console dashboard, choose the name of the file system you created for this
   exercise.
3. From the **Overview** tab for your file system, choose
   **Create backup**.
4. In the **Create backup** dialog box that opens, provide a name for
   your backup. This name can contain a maximum of 256 Unicode letters and include white
   space, numbers, and the following special characters: + - = . \_ : /
5. Choose **Create backup**.
6. To view all your backups in a list, so you can restore your file system or delete the
   backup, choose **Backups**.

When you create a new backup, its status is set to **CREATING** while it
is being created. This can take a few minutes. When the backup is available for use, its
status changes to **AVAILABLE**.

## Step 9. Clean up resources

After you have finished this exercise, you should follow these steps to clean up your
resources and protect your AWS account.

###### To clean up resources

1. On the Amazon EC2 console, terminate your instance. For more information, see [Terminate Your Instance](../../../AWSEC2/latest/WindowsGuide/terminating-instances.md "../../../AWSEC2/latest/WindowsGuide/terminating-instances.md") in the
   _Amazon EC2 User Guide._
2. On the Amazon FSx console, delete your file system. All automatic backups are deleted
   automatically. However, you still need to delete the manually created backups. The
   following steps outline this process:
   1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
   2. From the console dashboard, choose the name of the file system you created for
      this exercise.
   3. For **Actions**, choose **Delete file
      system**.
   4. In the **Delete file system** dialog box that opens, decide
      whether you want to create a final backup. If you do, provide a name for the final
      backup. Any automatically created backups are also deleted.

   ###### Important

   New file systems can be created from backups. We recommend that you create a
   final backup as a best practice. If you find you don't need it after a certain
   period of time, you can delete this and other manually created backups. 5. Enter the ID of the file system that you want to delete in the **File
   system ID** box. 6. Choose **Delete file system**. 7. The file system is now being deleted, and its status in the dashboard changes to
   **DELETING**. When the file system has been deleted, it no longer
   appears in the dashboard. 8. Now you can delete any manually created backups for your file system. From the
   left-side navigation, choose **Backups**. 9. From the dashboard, choose any backups that have the same **File system
   ID** as the file system that you deleted, and choose **Delete
   backup**. 10. The **Delete backups** dialog box opens. Leave the check box
   checked for the ID of the backup you selected, and choose **Delete
   backups**.Your Amazon FSx file system and related automatic backups are now deleted.

3. To delete the Directory Service directory you created for this exercise, see
   [Delete your directory](../../../directoryservice/latest/admin-guide/simple_ad_delete.md "../../../directoryservice/latest/admin-guide/simple_ad_delete.md") in the AWS Directory Service Administration Guide.
