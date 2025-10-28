# Set up Microsoft SQL Server on Amazon EC2

Describes the prerequisites, permissions, and configurations that you should consider when
preparing to use Microsoft SQL Server on Amazon EC2 instances for your SQL Server workloads.

###### Topics for setting up SQL Server on Amazon EC2

- [Prerequisites](#sql-server-on-ec2-prereqs "#sql-server-on-ec2-prereqs")
- [Permissions](#sql-server-on-ec2-permissions "#sql-server-on-ec2-permissions")

## Prerequisites for using SQL Server on Amazon EC2

Complete the tasks in this section to start using SQL Server on Amazon EC2 instances for the first time:

1. [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
2. [Create a user with administrative access](#create-an-admin "#create-an-admin")
3. [Create a key pair](#create-a-key-pair "#create-a-key-pair")
4. [Create a security group](#create-a-base-security-group "#create-a-base-security-group")

### Sign up for an AWS account

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

### Create a user with administrative access

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

### Create a key pair

AWS uses public-key cryptography to secure the login information for your instance. You
specify the name of the key pair when you launch your instance, then provide the private key to
obtain the administrator password for your Windows instance so you can log in using RDP.

If you haven't created a key pair already, you can create one by using the Amazon EC2 console.
Note that if you plan to launch instances in multiple Regions, you'll need to create a key pair
in each Region. For more information about Regions, see [Regions and
Zones](../../../AWSEC2/latest/WindowsGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/WindowsGuide/using-regions-availability-zones.md") in the _User Guide for Windows Instances_.

###### To create your key pair

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Key Pairs**.
3. Choose **Create key pair**.
4. For **Name**, enter a descriptive name for the key pair. Amazon EC2
   associates the public key with the name that you specify as the key name. A key name can
   include up to 255 ASCII characters. It can’t include leading or trailing spaces.
5. For **Key pair type**, choose either **RSA** or
   **ED25519**. Note that **ED25519** keys are not supported
   for Windows instances.
6. For **Private key file format**, choose the format in which to save the
   private key. To save the private key in a format that can be used with OpenSSH, choose
   **pem**. To save the private key in a format that can be used with PuTTY,
   choose **ppk**.

If you chose **ED25519** in the previous step, the **Private key
file format** options do not appear, and the private key format defaults to
**pem**. 7. Choose **Create key pair**. 8. The private key file is automatically downloaded by your browser. The base file name is
the name you specified as the name of your key pair, and the file name extension is determined
by the file format you chose. Save the private key file in a safe place.

###### Important

This is the only chance for you to save the private key file.

For more information, see [Amazon EC2 key pairs and Windows
instances](../../../AWSEC2/latest/WindowsGuide/ec2-key-pairs.md "../../../AWSEC2/latest/WindowsGuide/ec2-key-pairs.md") in the _User Guide for Windows Instances_.

### Create a security group

Security groups act as a firewall for associated instances, controlling both inbound and
outbound traffic at the instance level. You must add rules to a security group that enable you
to connect to your instance from your IP address using RDP. You can also add rules that allow
inbound and outbound HTTP and HTTPS access from anywhere.

Note that if you plan to launch instances in multiple Regions, you'll need to create a
security group in each Region. For more information about Regions, see [Regions and Zones](../../../AWSEC2/latest/WindowsGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/WindowsGuide/using-regions-availability-zones.md") in the _User Guide for Windows Instances_.

###### Prerequisites

You'll need the public IPv4 address of your local computer. The security group editor in
the Amazon EC2 console can automatically detect the public IPv4 address for you. Alternatively, you
can use the search phrase "what is my IP address" in an Internet browser, or use the following
service: [Check IP](http://checkip.amazonaws.com/ "http://checkip.amazonaws.com/"). If you are connecting
through an Internet service provider (ISP) or from behind a firewall without a static IP
address, you need to find out the range of IP addresses used by client computers.

You can create a custom security group using one of the following methods.

New Amazon EC2 console

###### To create a security group with least privilege

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the top navigation bar, select a Region for the security group. Security groups
   are specific to a Region, so you should select the same Region in which you created your
   key pair.
3. In the left navigation pane, choose **Security Groups**.
4. Choose **Create security group**.
5. For **Basic details**, do the following:
   1. Enter a name for the new security group and a description. Use a name that is easy
      for you to remember, such as your user name, followed by \_SG\_, plus the Region name. For
      example, _me_\_SG\__uswest2_.
   2. In the **VPC** list, select your default VPC for the Region.

6. For **Inbound rules**, create rules that allow specific traffic to
   reach your instance. For example, use the following rules for a web server that accepts
   HTTP and HTTPS traffic. For more examples, see [Security group rules
   for different use cases](../../../AWSEC2/latest/WindowsGuide/security-group-rules-reference.md "../../../AWSEC2/latest/WindowsGuide/security-group-rules-reference.md") in the _User Guide for Windows
   Instances_.
   1. Choose **Add rule**. For **Type**, choose
      **HTTP**. For **Source**, choose
      **Anywhere**.
   2. Choose **Add rule**. For **Type**, choose
      **HTTPS**. For **Source**, choose
      **Anywhere**.
   3. Choose **Add rule**. For **Type**, choose
      **RDP**. For **Source**, do one of the
      following:
      - Choose **My IP** to automatically add the public IPv4 address of
        your local computer.
      - Choose **Custom** and specify the public IPv4 address of your
        computer or network in CIDR notation. To specify an individual IP address in CIDR
        notation, add the routing suffix `/32`, for example,
        `203.0.113.25/32`. If your company or your router allocates addresses from
        a range, specify the entire range, such as `203.0.113.0/24`.

   ###### Warning

   For security reasons, do not choose **Anywhere** for
   **Source** with a rule for RDP. This would allow access to your
   instance from all IP addresses on the internet. This is acceptable for a short time in a
   test environment, but it is unsafe for production environments.

7. For **Outbound rules**, keep the default rule, which allows all
   outbound traffic.
8. Choose **Create security group**.

Old Amazon EC2 console

###### To create a security group with least privilege

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **Security Groups**.
3. Choose **Create Security Group**.
4. Enter a name for the new security group and a description. Use a name that is easy for
   you to remember, such as your user name, followed by \_SG\_, plus the Region name. For
   example, _me_\_SG\__uswest2_.
5. In the **VPC** list, select your default VPC for the Region.
6. On the **Inbound rules** tab, create the following rules (choose
   **Add rule** for each new rule):
   - Choose **HTTP** from the **Type** list, and make
     sure that **Source** is set to **Anywhere**
     (`0.0.0.0/0`).
   - Choose **HTTPS** from the **Type** list, and make
     sure that **Source** is set to **Anywhere**
     (`0.0.0.0/0`).
   - Choose **RDP** from the **Type** list. In the
     **Source** box, choose **My IP** to automatically
     populate the field with the public IPv4 address of your local computer. Alternatively,
     choose **Custom** and specify the public IPv4 address of your computer
     or network in CIDR notation. To specify an individual IP address in CIDR notation, add
     the routing suffix `/32`, for example, `203.0.113.25/32`. If your
     company allocates addresses from a range, specify the entire range, such as
     `203.0.113.0/24`.

   ###### Warning

   For security reasons, do not allow RDP access from all IP addresses to your
   instance. This is acceptable for a short time in a test environment, but it is unsafe
   for production environments.

7. On the **Outbound rules** tab, keep the default rule, which allows
   all outbound traffic.
8. Choose **Create security group**.

Command line

###### To create a security group with least privilege

Use one of the following commands:

- [create-security-group](../../../cli/latest/reference/ec2/create-security-group.md "../../../cli/latest/reference/ec2/create-security-group.md")
  (AWS CLI)
- [New-EC2SecurityGroup](../../../powershell/latest/reference/items/New-EC2SecurityGroup.md "../../../powershell/latest/reference/items/New-EC2SecurityGroup.md")
  (AWS Tools for Windows PowerShell)

For more information, see [Amazon EC2 security groups for
Windows instances](../../../AWSEC2/latest/WindowsGuide/ec2-security-groups.md "../../../AWSEC2/latest/WindowsGuide/ec2-security-groups.md") in the _Amazon EC2 User Guide_.

## Permissions required to use SQL Server on Amazon EC2

For information about the permissions required to create or modify Amazon EC2 resources, or to
perform tasks using the Amazon EC2 API, see [IAM policies for Amazon
EC2](../../../AWSEC2/latest/WindowsGuide/iam-policies-for-amazon-ec2.md "../../../AWSEC2/latest/WindowsGuide/iam-policies-for-amazon-ec2.md") in the _User Guide for Windows Instances_.
