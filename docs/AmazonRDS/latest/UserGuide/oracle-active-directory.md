

# Kerberos authentication with Active Directory with Amazon RDS for Oracle
<a name="oracle-active-directory"></a>

You can use Kerberos authentication to authenticate users when they connect to your Amazon RDS for Oracle DB instance. In this configuration, your DB instance works with Active Directory. When users authenticate with an RDS for Oracle DB instance joined to a domain, authentication requests are forwarded to the directory that the DB instance is joined to: either a directory that you create with Directory Service, or your self-managed Active Directory domain.

Keeping all of your credentials in the same directory can save you time and effort. You have a centralized place for storing and managing credentials for multiple database instances. A directory can also improve your overall security profile.

Your Active Directory domain can be hosted on Directory Service for Microsoft Active Directory, also referred to as AWS Managed Microsoft AD, within AWS, or on a self-managed Active Directory in a location of your choice, including your corporate data centers, on Amazon Elastic Compute Cloud (Amazon EC2), or with other cloud providers.

**Note**  
Microsoft Entra ID (formerly Azure Active Directory) is a cloud-based identity service, not an Active Directory Domain Services (AD DS) domain. Self-managed Active Directory requires an AD DS domain that provides Kerberos authentication, so you can't join an RDS for Oracle DB instance to Microsoft Entra ID by using self-managed Active Directory.

In the following sections, you can find information about working with AWS Managed Active Directory and self-managed Active Directory for Amazon RDS for Oracle.

**Topics**
+ [Choosing between self-managed AD and AWS Managed Microsoft AD](#oracle-active-directory.choosing)
+ [Working with AWS Managed Active Directory with an Amazon RDS for Oracle DB instance](oracle-kerberos.md)
+ [Working with self-managed Active Directory with an Amazon RDS for Oracle DB instance](oracle-smad.md)

## Choosing between self-managed AD and AWS Managed Microsoft AD
<a name="oracle-active-directory.choosing"></a>

You can join an RDS for Oracle DB instance to a self-managed Active Directory domain or to an AWS Managed Microsoft AD directory. With either option, your database users sign in with their Active Directory credentials through Kerberos single sign-on. Both options use the same Oracle user model (`CREATE USER ... IDENTIFIED EXTERNALLY`) and the same Kerberos client configuration. The difference is which directory the DB instance joins and which credentials Amazon RDS uses to join it.

Choose **self-managed AD** when your users and service accounts are already in an AD domain that you run on premises, on Amazon EC2, or with another cloud provider, and you want the DB instance to join that domain directly. Because the DB instance joins your existing domain, you don't pay for or operate an AWS Managed Microsoft AD directory, and you don't need to create a forest trust. To use this option, you set up network connectivity from your virtual private cloud (VPC) to your domain controllers. You also provide an AD domain service account that has delegated permissions on an Organizational Unit (OU). Amazon RDS uses this account to join the DB instance to your domain.

Choose **AWS Managed Microsoft AD** when you want AWS to run the domain controllers for you, or when you already use an AWS Managed Microsoft AD directory with other AWS services.

The following table summarizes the differences.


| Item | AWS Managed Microsoft AD | Self-managed AD | 
| --- | --- | --- | 
| Directory | Directory Service directory in your account | Your own AD domain (on premises, on Amazon EC2, or in another cloud) | 
| Credentials that Amazon RDS uses | IAM role with the AmazonRDSDirectoryServiceAccess managed policy | AD domain service account stored in a Secrets Manager secret encrypted with your AWS KMS key | 
| AWS CLI parameters | --domain, --domain-iam-role-name | --domain-fqdn, --domain-ou, --domain-auth-secret-arn, --domain-dns-ips | 