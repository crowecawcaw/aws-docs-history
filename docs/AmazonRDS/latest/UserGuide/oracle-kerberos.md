

# Working with AWS Managed Active Directory with an Amazon RDS for Oracle DB instance
<a name="oracle-kerberos"></a>

You can use Kerberos authentication to authenticate users when they connect to your Amazon RDS for Oracle DB instance. In this configuration, your DB instance works with AWS Managed Active Directory. When users authenticate with an RDS for Oracle DB instance joined to the trusting domain, authentication requests are forwarded to the directory that you create with Directory Service.

Keeping all of your credentials in the same directory can save you time and effort. You have a centralized place for storing and managing credentials for multiple database instances. A directory can also improve your overall security profile.

**Topics**
+ [Region and version availability for AWS Managed Active Directory](oracle-kerberos-setting-up.RegionVersionAvailability.md)
+ [Setting up AWS Managed Active Directory](oracle-kerberos-setting-up.md)
+ [Managing a DB instance for AWS Managed Active Directory](oracle-kerberos-managing.md)
+ [Connecting with Kerberos authentication for AWS Managed Active Directory](oracle-kerberos-connecting.md)