

# Remediating exposures for Azure SQL databases
<a name="exposure-azure-sql-database"></a>

AWS Security Hub can generate exposure findings for Azure SQL databases.

On the Security Hub console, the Azure SQL database involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the [GetFindingsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Microsoft Azure resources. 

**Contents**
+ [Misconfiguration traits for Azure SQL databases](#azure-sql-misconfiguration)
  + [The Azure SQL database has public network access enabled](#sql-server-public-network-access)
  + [The Azure SQL database does not enforce Azure AD-only authentication](#sql-server-azure-ad-only-auth)
  + [The Azure SQL database uses a default or common admin username](#sql-server-default-admin-name-used)
  + [The Azure SQL database has geo-redundant backup disabled](#sql-server-backups-disabled)

## Misconfiguration traits for Azure SQL databases
<a name="azure-sql-misconfiguration"></a>

Here are misconfiguration traits for Azure SQL databases and suggested remediation steps.

### The Azure SQL database has public network access enabled
<a name="sql-server-public-network-access"></a>

 When public network access is enabled on the logical server, the database is reachable through a public endpoint and can accept connections from the public internet (subject to firewall rules). A public endpoint increases the attack surface of your database and exposes it to unauthorized connection attempts. Following standard security principles, disable public network access and connect to the database privately, or tightly restrict the server firewall rules. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Disable public network access and use Private Link**  
 Set the logical server's public network access to `Disabled` and connect to the database through a private endpoint (Azure Private Link) within your virtual network. This keeps database traffic on the Azure backbone and off the public internet. For more information, see [Network access controls for Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/network-access-controls-overview) in the Microsoft Azure documentation. 

**Restrict firewall rules if public access is required**  
 If you must keep public access enabled, remove any rule that allows the full internet range, and disable **Allow Azure services and resources to access this server** when it is not needed. Limit server-level firewall rules to the specific trusted IP addresses your workload requires. For more information, see [Network access controls for Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/network-access-controls-overview) in the Microsoft Azure documentation. 

**Enforce a minimum TLS version**  
 Set the logical server's minimum TLS version to 1.2 so that connections that use older, less secure protocol versions are rejected. Confirm that your clients support TLS 1.2 before you enforce this setting. For more information, see [Connectivity settings for Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings) in the Microsoft Azure documentation. 

### The Azure SQL database does not enforce Azure AD-only authentication
<a name="sql-server-azure-ad-only-auth"></a>

 When Microsoft Entra-only authentication (formerly Azure AD-only authentication) is not enforced, the logical server also accepts SQL authentication, which relies on passwords stored and managed within the database. SQL authentication is more susceptible to credential theft and brute-force attacks and does not benefit from centralized Microsoft Entra controls such as Conditional Access and multifactor authentication. Following standard security principles, enforce Microsoft Entra-only authentication so that only Microsoft Entra identities can connect. 

**Remediation: Enforce Microsoft Entra-only authentication**  
 Set a Microsoft Entra admin for the logical server, then enable Microsoft Entra-only authentication. This disables SQL authentication so that only Microsoft Entra identities can connect to the server and its databases. Confirm that your applications support Microsoft Entra authentication before enforcing this setting. For more information, see [Microsoft Entra-only authentication](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-azure-ad-only-authentication) in the Microsoft Azure documentation. 

### The Azure SQL database uses a default or common admin username
<a name="sql-server-default-admin-name-used"></a>

 The logical server's administrator login uses a well-known or common username, such as `sqladmin`, `admin`, or `sa`. Common administrator usernames are predictable, which makes the server an easier target for brute-force and credential-stuffing attacks because an attacker needs to guess only the password. Following standard security principles, avoid default or common administrator usernames and centralize administrative access through Microsoft Entra ID. 

**Remediation: Use a non-default administrator and Microsoft Entra authentication**  
 Avoid predictable administrator login names. Where possible, enforce Microsoft Entra-only authentication and manage administrative access through Microsoft Entra identities and groups rather than a SQL administrator login. Follow the Azure SQL security best practices for managing logins and least-privilege access. For more information, see [Azure SQL Database security best practices](https://learn.microsoft.com/en-us/azure/azure-sql/database/security-best-practice) in the Microsoft Azure documentation. 

### The Azure SQL database has geo-redundant backup disabled
<a name="sql-server-backups-disabled"></a>

 Azure SQL Database stores automated backups in geo-redundant storage by default, which replicates backups to a paired region and enables geo-restore during a regional outage. When backup storage redundancy is set to locally redundant or zone-redundant storage instead, geo-restore is unavailable. You cannot recover the database in another region if the primary region becomes unavailable. Following data protection best practices, use geo-redundant backup storage for databases that require resilience to regional outages. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Configure geo-redundant backup storage**  
 Set the database's backup storage redundancy to geo-redundant storage (GRS) or geo-zone-redundant storage (GZRS) so that geo-restore is available. Changes apply to future backups and can take up to 48 hours to take effect. For more information, see [Automated backups in Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview) in the Microsoft Azure documentation. 

**Configure long-term retention**  
 For databases with compliance or long-term recovery requirements, configure a long-term retention (LTR) policy. LTR retains full backups for up to 10 years, in addition to the default short-term retention. For more information, see [Long-term retention in Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview) in the Microsoft Azure documentation. 