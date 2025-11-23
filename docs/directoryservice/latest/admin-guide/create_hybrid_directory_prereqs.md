# Hybrid directory prerequisites

Hybrid directory extends your self-managed Active Directory to the AWS Cloud. Before creating a
hybrid directory, ensure your environment meets these requirements:

## Microsoft Active Directory domain

requirements

Before creating a hybrid directory, ensure your self-managed AD environment and
infrastructure meet the following requirements, and gather the necessary
information.

### Domain requirements

Your self-managed AD environment must meet the following requirements:

- Uses a Windows Server 2012 R2 or 2016
  functional level.
- Uses standard domain controllers to be assessed for hybrid directory creation.
  Read-only domain controllers (RODC) can not be used for hybrid directory
  creation.
- Has two domain controllers with all Active Directory services running.
- The Primary Domain Controller (PDC) must be routable at all times.

Specifically, the PDC Emulator and RID Master IPs of your
self-managed AD must be in one of these categories:

    + Part of RFC1918 private IP address ranges (10.0.0.0/8,
     172.16.0.0/12, or 192.168.0.0/16)
    + Within your VPC CIDR range
    + Match the DNS IPs of your self-managed instances for the
     directory

You can add additional IP routes for the directory after the hybrid directory
is created.

### Required information

Gather the following information about your self-managed AD:

- Directory DNS name
- Directory DNS IPs
- Service account credentials with Administrator permissions to your
  self-managed AD
- AWS Secret ARN for storing your service account credentials (see [AWS Secret ARN for
  hybrid directory](#aws_secret_arn_for_hybrid "#aws_secret_arn_for_hybrid"))

### AWS Secret ARN for

hybrid directory

To configure a hybrid directory with your self-managed AD, you need to create a
KMS key to encrypt your AWS secret and then create the secret itself. Both
resources must be created in the same AWS account that contains the
hybrid directory.

#### Create a KMS key

The KMS key is used to encrypt your AWS secret.

###### Important

For **Encryption Key**, don't use the AWS
default KMS key. Be sure to create the AWS KMS key in the same
AWS account that contains the hybrid directory you want to create to join with
your self-managed AD.

###### To create an AWS KMS key

1. In the AWS KMS console, choose **Create key**.
2. For **Key Type**, choose
   **Symmetric**.
3. For **Key Usage**, choose **Encrypt and
   decrypt**.
4. For **Advanced options**:
   1. For **Key material origin**, choose
      **KMS**.
   2. For **Regionality**, choose
      **Single-Region key** and choose
      **Next**.

5. For **Alias**, provide a name for the
   KMS key.
6. (Optional) For **Description**, provide a description
   of the KMS key.
7. (Optional) For **Tags**, add tags for the KMS key
   and choose **Next**.
8. For **Key administrators**, select an IAM
   user.
9. For **Key deletion**, keep the default selection for
   **Allow key administrators to delete this key** and
   choose **Next**.
10. For **Key users**, select the same IAM user from
    the previous step and choose **Next**.
11. Review the configuration.
12. For **Key policy**, add the following statement to
    the policy:
13. Choose **Finish**.

#### Create an AWS secret

Create a secret in Secrets Manager to store the credentials for your self-managed AD
user account.

###### Important

Create the secret in the same AWS account that contains the hybrid directory
you want to join with your self-managed AD.

To create a secret

- In Secrets Manager, choose **Store a new secret**
- For **Secret type**, choose **Other type of
  secret**
- For **Key/value pairs**, add your two keys:

1. Add the username key
   1. For the first key, enter
      `customerAdAdminDomainUsername`.
   2. For the value of the first key, enter only the username
      (without the domain prefix) of the AD user. Do not include the
      domain name as this causes instance creation to fail.

2. Add the password key
   1. For the second key, enter
      `customerAdAdminDomainPassword`.
   2. For the value of the second key, enter the password that you
      created for the AD user on your domain.

##### Complete the secret

configuration

1. For **Encryption key**, select the KMS key that
   you created in [Create a KMS key](#create_kms_key_for_hybrid "#create_kms_key_for_hybrid") and choose
   **Next**.
2. For **Secret name**, enter a description for the
   secret.
3. (Optional) For **Description**, enter a
   description for the secret.
4. Choose **Next**.
5. For **Configure rotation settings**, keep the
   default values and choose **Next**.
6. Review the settings for the secret and choose
   **Store**.
7. Choose the secret you created and copy the value for the
   **Secret ARN**. You will use this ARN in the
   next step to set up your self-managed Active Directory.

### Infrastructure requirements

Prepare the following infrastructure components:

- Two AWS Systems Manager nodes with administrator privileges for SSM agents
  - If your Active Directory is **self-managed outside of the
    AWS Cloud**, you will need two Systems Manager node
    for a hybrid and multicloud environment. For more
    information on how to provision these nodes, see [Setting up Systems Manager for hybrid and multicloud
    environments](../../../systems-manager/latest/userguide/systems-manager-hybrid-multicloud.md "../../../systems-manager/latest/userguide/systems-manager-hybrid-multicloud.md").
  - If your Active Directory is **self-managed within the AWS Cloud**,
    you will need two Systems Manager managed EC2 instances. For more
    information on how to provision these instances, see [Managing EC2 instances with Systems Manager](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md").

## Required Active Directory

services

Ensure the following services are running on your self-managed AD:

- Active Directory Domain Services
- Active Directory Web Service (ADWS)
- COM+ Event System
- Distributed File System Replication (DFSR)
- Domain Name System (DNS)
- DNS Server
- Group Policy Client
- Intersite Messaging
- Remote Procedure Call (RPC)
- Security Accounts Manager
- Windows Time Server

###### Note

Hybrid directory requires both the UDP port 123 to be open and the Windows
Time Server to be enabled and functional. We synchronize time with your
domain controller to ensure hybrid directory replication works properly.

## Kerberos authentication

requirements

Your user accounts must have Kerberos preauthentication enabled. For detailed
instructions on how to enable this setting, see [Ensure that Kerberos pre-authentication is enabled](ms-ad-tutorial-setup-trust-prepare-onprem.md#tutorial-setup-trust-enable-kerberos "ms-ad-tutorial-setup-trust-prepare-onprem.md#tutorial-setup-trust-enable-kerberos"). For general information
about this setting, go to [Preauthentication](http://technet.microsoft.com/en-us/library/cc961961.aspx "http://technet.microsoft.com/en-us/library/cc961961.aspx") on Microsoft TechNet.

## Supported encryption

types

hybrid directory supports the following encryption types when authenticating via Kerberos
to your Active Directory domain controllers:

- AES-256-HMAC

## Network port

requirements

For AWS to extend your self-managed Active Directory domain controllers, the firewall for your
existing network must have the following ports open to the CIDRs for both
subnets in your Amazon VPC:

- TCP/UDP 53 - DNS
- TCP/UDP 88 - Kerberos authentication
- UDP 123 - Time server
- TCP 135 - Remote Procedure Call
- TCP/UDP 389 - LDAP
- TCP 445 - SMB
- TCP 636 - Only needed for environments with Lightweight Directory Access
  Protocol Secure (LDAPS)
- TCP 49152-65535 - RPC randomly allocated high TCP ports
- TCP 3268 and 3269 - Global Catalog
- TCP 9389 Active Directory Web Services (ADWS)

These are the minimum ports needed to create a hybrid directory. Your specific
configuration may require additional ports be open.

###### Note

The DNS IPs provided for your Domain Controllers and FSMO Role holders must have
the above ports open to the CIDRs for both subnets in the Amazon VPC.

###### Note

Hybrid directory requires both the UDP port 123 to be open and the Windows Time Server
to be enabled and functional. We synchronize time with your domain controller to
ensure hybrid directory replication works properly.

## AWS account permissions

You will need permissions to the following actions in your AWS account:

- ec2:AuthorizeSecurityGroupEgress
- ec2:AuthorizeSecurityGroupIngress
- ec2:CreateNetworkInterface
- ec2:CreateSecurityGroup
- ec2:DescribeNetworkInterfaces
- ec2:DescribeSubnets
- ec2:DescribeVpcs
- ec2:CreateTags
- ec2:CreateNetworkInterfacePermission
- ssm:ListCommands
- ssm:GetCommandInvocation
- ssm:GetConnectionStatus
- ssm:SendCommand
- secretsmanager:DescribeSecret
- secretsmanager:GetSecretValue
- iam:GetRole
- iam:CreateServiceLinkedRole

## Amazon VPC network requirements

A VPC with the following:

- At least two subnets. Each of the subnets must be in a different Availability
  Zone
- The VPC must have default tenancy

You cannot create a hybrid directory in a VPC using addresses in the 198.18.0.0/15 address
space.

Directory Service uses a two VPC structure. The EC2 instances which make up your directory run
outside of your AWS account, and are managed by AWS. They have two network adapters,
`ETH0` and `ETH1`. `ETH0` is the management
adapter, and exists outside of your account. `ETH1` is created within your
account.

The management IP range of the ETH0 network for your directory is
`198.18.0.0/15`.

For more information, see the following topics in the
_Amazon VPC User Guide_:

- [What is
  Amazon VPC?](ms_ad_getting_started.md "ms_ad_getting_started.md")
- [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")
- [VPCs and
  subnets](../../../vpc/latest/userguide/how-it-works.md#how-it-works-subnet "../../../vpc/latest/userguide/how-it-works.md#how-it-works-subnet")
- [What is
  AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC-VPN.md "../../../vpn/latest/s2svpn/VPC-VPN.md")

For more information about AWS Direct Connect, see the [What
is AWS Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")

## AWS security group

configuration

By default, AWS attaches a security group to allow network access to the AWS Systems Manager
managed nodes in your VPC. You can optionally supply your own security group that allows
network traffic to and from your self-managed domain controllers outside of your
VPC.

You can optionally supply your own security group that allows network traffic to and
from your self-managed domain controllers outside of your VPC. If you are supply your
own security group, then you need to:

- Allowlist your VPC CIDR ranges and self-managed ranges.
- Ensure these ranges don't overlap with [AWS reserved IP
  ranges](../../../vpc/latest/userguide/aws-ip-ranges.md "../../../vpc/latest/userguide/aws-ip-ranges.md")

## Directory assessments considerations

The following are considerations when creating directory assessments and the number of assessments you
can have in your AWS account:

- A directory assessment is automatically created when you create a hybrid directory. There are two
  types of assessments: `CUSTOMER` and `SYSTEM`. Your
  AWS account has a limit of 100 `CUSTOMER` directory assessments.
- If you attempt to create a hybrid directory and you already have 100
  `CUSTOMER` directory assessments, you will encounter an error. Delete assessments
  to free up capacity before trying again.
- You can request an increase to your `CUSTOMER` directory assessment quota by
  contacting Support or delete existing CUSTOMER directory assessments to free up capacity.
