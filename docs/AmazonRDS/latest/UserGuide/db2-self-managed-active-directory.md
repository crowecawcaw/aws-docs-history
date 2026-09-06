

# Working with self-managed Active Directory with an RDS for Db2 DB instance
<a name="db2-self-managed-active-directory"></a>

RDS for Db2 integrates with your self-managed Active Directory (AD) domain. Your AD can be hosted in your data center, on Amazon EC2, or with other cloud providers. This integration enables direct user authentication through the Kerberos protocol, eliminating the need for complex intermediary domains or forest trusts. When you connect to your RDS for Db2 DB instance, RDS for Db2 securely forwards authentication requests to your designated AD domain. This maintains your existing identity management structure while using Amazon RDS managed database capabilities.

## Region and version availability
<a name="db2-self-managed-active-directory.RegionVersionAvailability"></a>

Amazon RDS supports self-managed AD for Db2 using Kerberos in all commercial AWS Regions and AWS GovCloud (US) Regions.

For information about setting up and managing self-managed Active Directory with RDS for Db2, see the following topics:

**Topics**
+ [Requirements](db2-self-managed-active-directory.Requirements.md)
+ [Setting up self-managed Active Directory](db2-self-managed-active-directory.SettingUp.md)
+ [Managing a DB instance in a self-managed Active Directory domain](db2-self-managed-active-directory.Managing.md)