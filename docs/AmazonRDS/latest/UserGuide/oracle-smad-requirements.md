

# Requirements for self-managed Active Directory
<a name="oracle-smad-requirements"></a>

Make sure that you meet the following requirements before you join an Amazon RDS for Oracle DB instance to your self-managed Active Directory (AD) domain.

**Topics**
+ [Configure your self-managed AD](#oracle-smad-requirements.configure-ad)
+ [Configure your network connectivity](#oracle-smad-requirements.configure-network)
+ [Configure your AD domain service account](#oracle-smad-requirements.configure-svc-account)

## Configure your self-managed AD
<a name="oracle-smad-requirements.configure-ad"></a>

Make sure that you have an on-premises or other self-managed Microsoft AD that you can join the RDS for Oracle instance to. Your on-premises AD should have the following configuration:
+ If you have AD sites defined, make sure the subnets in the virtual private cloud (VPC) associated with your RDS for Oracle DB instance are defined in your AD site. Confirm there aren't any conflicts between the subnets in your VPC and the subnets in your other AD sites.
+ Your AD domain controller has a domain functional level of Windows Server 2008 R2 or higher.
+ The fully qualified domain name (FQDN) for your AD can't exceed 64 characters.
+ Your domain controllers allow the AES128-CTS-HMAC-SHA1-96 or AES256-CTS-HMAC-SHA1-96 Kerberos encryption type.

## Configure your network connectivity
<a name="oracle-smad-requirements.configure-network"></a>

Make sure that you meet the following network requirements:
+ Configure connectivity between the Amazon VPC where you create the RDS for Oracle DB instance and your self-managed AD. You can set up connectivity using , Site-to-Site VPN, VPC peering, or .
+ For VPC security groups, the default security group for your default VPC is already added to your RDS for Oracle DB instance in the console. Make sure that the security group and the VPC network ACLs for the subnets where you're creating your RDS for Oracle DB instance allow traffic on the following ports.


<table>
<thead>
  <tr><th>Protocol</th><th>Ports</th><th>Role</th></tr>
</thead>
<tbody>
  <tr><td>TCP/UDP</td><td>53</td><td>DNS</td></tr>
  <tr><td>TCP/UDP</td><td>88</td><td>Kerberos authentication</td></tr>
  <tr><td>TCP/UDP</td><td>464</td><td>Change/set password</td></tr>
  <tr><td>TCP/UDP</td><td>389</td><td>LDAP</td></tr>
</tbody>
</table>

+ Generally, the domain DNS servers are located in the AD domain controllers. You do not need to configure the VPC DHCP option set to use this feature. For more information, see [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.

**Important**  
If you're using VPC network ACLs, you must also allow inbound return traffic on ports 9000–65500 to your RDS for Oracle DB instance. If your domain controllers are in a subnet with a network ACL, allow outbound traffic on ports 9000–65500 from the domain controllers to your DB instance.

## Configure your AD domain service account
<a name="oracle-smad-requirements.configure-svc-account"></a>

Make sure that you meet the following requirements for an AD domain service account:
+ Make sure that you have a domain service account in your self-managed AD domain with delegated permissions to create and manage user objects in a dedicated Organizational Unit (OU). A domain service account is a user account in your self-managed AD to which you have delegated permission to perform certain tasks.
+ The domain service account needs to be delegated the following permissions in the OU that you're joining your RDS for Oracle DB instance to:
  + Create and delete user objects
  + Read all properties of user objects
  + Reset password on user objects
  + Read and write `servicePrincipalName` on user objects
  + Read and write `msDS-SupportedEncryptionTypes` on user objects

For step-by-step instructions, see [Step 3: Delegate control to the AD domain service account](oracle-smad-setting-up.md#oracle-smad-setting-up.step3).

**Important**  
Do not move the user objects that RDS for Oracle creates in the Organizational Unit after your DB instance is created. If you move the associated objects, your RDS for Oracle DB instance becomes misconfigured. If you need to move the user objects created by Amazon RDS, use the `ModifyDBInstance` API operation to modify the domain parameters with the desired location of the user objects.