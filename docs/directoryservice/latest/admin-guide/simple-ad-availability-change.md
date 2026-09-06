

# Simple AD availability changes
<a name="simple-ad-availability-change"></a>

This guide provides information about the Simple AD changes and recommended alternatives for AWS Directory Service Simple AD customers.

**Note**  
Only new customer onboarding to Simple AD is not permitted. Existing Simple AD customers retain full functionality. Your directories, users, computers, and integrated workloads are not affected, and you can continue to create new Simple AD directories.

## Recommended alternatives
<a name="simple-ad-availability-change-alternatives"></a>

We recommend that customers evaluate the following alternatives based on their use case:

### AWS Managed Microsoft AD
<a name="simple-ad-availability-change-managed-ad"></a>
+ AWS Managed Microsoft AD is a fully managed, native Microsoft Active Directory (AD) service hosted on AWS. Unlike Simple AD, which is Samba-based, AWS Managed Microsoft AD runs on actual Windows Server Active Directory and provides full-fidelity directory features including Group Policy, trusts, schema extensions, Kerberos authentication, and LDAP.
+ Customers can share their AWS Managed Microsoft AD directory across multiple AWS accounts, enabling EC2 domain joins and AD authentication for resources in different accounts.
+ Security logs can be forwarded to Amazon CloudWatch Logs for security monitoring, audit, and compliance reporting.
+ AWS Managed Microsoft AD integrates with a broad set of AWS services including WorkSpaces, Amazon RDS, Amazon FSx for Windows File Server, Amazon EC2, and AWS IAM Identity Center.
+ Available in Standard Edition (up to 30,000 directory objects) and Enterprise Edition (up to 500,000 directory objects) with multi-Region support.

To get started, see [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html). For pricing, see [Directory Service pricing](https://aws.amazon.com/directoryservice/pricing/).

### AD Connector
<a name="simple-ad-availability-change-ad-connector"></a>
+ AD Connector is a proxy service that connects AWS services to a self-managed AD (on-premises or in the cloud) without replicating directory data. Best if you want to use self-managed Samba-based AD or already have an existing self-managed AD with AWS applications.
+ AD Connector enables AWS application integration with a self-managed AD. For example, customers can use AD Connector to connect WorkSpaces to their on-premises AD, enable EC2 domain join, access the AWS Management Console with AD credentials, and integrate with AWS IAM Identity Center.
+ AD Connector uses your self-managed AD security policies such as password expiration, password history, and account lockout policies, no synchronization or replication of directory data to AWS.
+ Available in Small and Large sizes.

To get started, see [AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html). For pricing, see [Directory Service other directory types pricing](https://aws.amazon.com/directoryservice/other-directories-pricing/).

## Additional resources
<a name="simple-ad-availability-change-resources"></a>
+ [AWS Directory Service documentation](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/)
+ [AWS Directory Service product page](https://aws.amazon.com/directoryservice/)
+ [AWS Directory Service other directory types](https://aws.amazon.com/directoryservice/other-directories/)
+ [AWS Managed Microsoft AD Admin Guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html)
+ [AD Connector Admin Guide](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html)
+ [AWS Support](https://aws.amazon.com/support)