

# Requirements
<a name="db2-self-managed-active-directory.Requirements"></a>

Make sure that you meet the following requirements before joining an RDS for Db2 DB instance to your self-managed AD domain.

**Topics**
+ [Configure your on-premises AD](#db2-self-managed-active-directory.Requirements.OnPremConfig)
+ [Configure your network connectivity](#db2-self-managed-active-directory.Requirements.NetworkConfig)
+ [Configure your AD domain service account](#db2-self-managed-active-directory.Requirements.DomainAccountConfig)

## Configure your on-premises AD
<a name="db2-self-managed-active-directory.Requirements.OnPremConfig"></a>

Make sure that you have an on-premises or other self-managed Microsoft AD that you can join the RDS for Db2 instance to. Your on-premises AD should have the following configuration:
+ If you have AD sites defined, make sure the subnets in the VPC associated with your RDS for Db2 DB instance are defined in your AD site. Confirm there aren't any conflicts between the subnets in your VPC and the subnets in your other AD sites.
+ Your AD domain controller has a domain functional level of Windows Server 2008 R2 or higher.
+ The fully qualified domain name (FQDN) for your AD can't exceed 47 characters.

## Configure your network connectivity
<a name="db2-self-managed-active-directory.Requirements.NetworkConfig"></a>

Make sure that you meet the following network requirements:
+ Configure connectivity between the Amazon VPC where you want to create the RDS for Db2 DB instance and your self-managed AD. You can set up connectivity using AWS Direct Connect, AWS VPN, VPC peering, or AWS Transit Gateway.
+ For VPC security groups, the default security group for your default VPC is already added to your RDS for Db2 DB instance in the console. Make sure that the security group and the VPC network ACLs for the subnets where you're creating your RDS for Db2 DB instance allow traffic on the ports identified in the following table.  
**Required ports for self-managed AD**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-self-managed-active-directory.Requirements.html)
+ Generally, the domain DNS servers are located in the AD domain controllers. You do not need to configure the VPC DHCP option set to use this feature. For more information, see [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.

**Important**  
If you're using VPC network ACLs, you must also allow outbound traffic on dynamic ports (49152-65535) from your RDS for Db2 DB instance. Make sure that these traffic rules are also mirrored on the firewalls that apply to each of the AD domain controllers, DNS servers, and RDS for Db2 DB instances.  
VPC security groups require ports to be opened only in the direction from which network traffic originates. However, most Windows firewalls and VPC network ACLs require ports to be open in both directions.

## Configure your AD domain service account
<a name="db2-self-managed-active-directory.Requirements.DomainAccountConfig"></a>

Make sure that you meet the following requirements for an AD domain service account:
+ Make sure that you have a domain service account in your self-managed AD domain with delegated permissions to create and manage user objects in a dedicated Organizational Unit (OU). A domain service account is a user account in your self-managed AD to which you have delegated permission to perform certain tasks.
+ The domain service account needs to be delegated the following permissions in the OU that you're joining your RDS for Db2 DB instance to:
  + Create and delete user objects
  + Reset Password
  + Read and write `msDS-SupportedEncryptionTypes`
  + Read and write `servicePrincipalName`

  For step-by-step instructions for setting these permissions, see [Step 3: Delegate control to the AD domain service account](db2-self-managed-active-directory.SettingUp.md#db2-self-managed-active-directory.SettingUp.DelegateControl).

**Important**  
Do not move the user objects that RDS for Db2 creates in the Organizational Unit after your DB instance is created. If you move the associated objects, your RDS for Db2 DB instance becomes misconfigured. If you need to move the user objects created by Amazon RDS, use the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) API operation to modify the domain parameters with the desired location of the user objects.