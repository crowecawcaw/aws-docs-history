# Application security considerations

Application security includes considering what permissions the application will need
to run, what firewall rules, what IAM roles should be enabled for access to the application.

To better understand general AWS security, see
[Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/ "https://aws.amazon.com/architecture/security-identity-compliance/").

## Access for configuration management

AWS Managed Services (AMS) seeks to provide you with a headache-free infrastructure so
you don’t have to worry about security issues, patching issues, backup issues, etc. To
do that, AMS recommends minimal IAM roles allowing only a specific group or a
master server, if using an application deployment tool, access to the instances running
your application.

## Application access firewall rules

Just like the operating system (OS), all application access should be governed using
Active Directory (AD) groups. Using Amazon Relational Database Service (Amazon RDS) as an
example, you must break the mirror (replication) to add a new user. The best approach
is to create a group in AD and add it at database creation time. Having the groups in your
AMS AD means that you can create CTs for application access. For information on the
official grouping strategy for AD, see
[Using Group Nesting Strategy – AD Best Practices for Group Strategy](http://blogs.msmvps.com/acefekay/2012/01/06/using-group-nesting-strategy-ad-best-practices-for-group-strategy/ "http://blogs.msmvps.com/acefekay/2012/01/06/using-group-nesting-strategy-ad-best-practices-for-group-strategy/").

To learn more about domain trees and parent/child domains, see
[How Domains and Forests Work](https://technet.microsoft.com/en-us/library/cc783351%28v=ws.10%29.aspx "https://technet.microsoft.com/en-us/library/cc783351%28v=ws.10%29.aspx").

The following rules illustrate a solution appropriate for a multi-domain forest trust with users located in child domains.
