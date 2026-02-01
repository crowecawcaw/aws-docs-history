Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Security in Amazon Redshift

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet
the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in
  the AWS Cloud. AWS also provides you with services that you can use securely. The effectiveness of our security is regularly tested and verified
  by third-party auditors as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To
  learn about the compliance programs that apply to Amazon Redshift, see [AWS services in scope by compliance program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also
  responsible for other factors including the sensitivity of your data, your organization's requirements, and applicable laws and regulations.
  Access to Amazon Redshift resources is controlled at four levels:

- Cluster management – The ability to create,
  configure, and delete clusters is controlled by the permissions given to the user or
  account associated with your AWS security credentials. Users with the proper
  permissions can use the AWS Management Console, AWS Command Line Interface (CLI), or Amazon Redshift Application Programming
  Interface (API) to manage their clusters. This access is managed by using IAM policies.

###### Important

Amazon Redshift has a collection of best practices for managing permissions, identities and secure access. We recommend that
you get familiar with these as you get started with Amazon Redshift. For more information, see [Identity and access management in
Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

- Cluster connectivity – Amazon Redshift security groups
  specify the AWS instances that are authorized to connect to an Amazon Redshift cluster in
  Classless Inter-Domain Routing (CIDR) format. For information about creating Amazon Redshift,
  Amazon EC2, and Amazon VPC security groups and associating them with clusters, see [Amazon Redshift security groups](security-network-isolation.md#working-with-security-groups "security-network-isolation.md#working-with-security-groups").
- Database access – The ability to access database
  objects, such as tables and views, is controlled by database user accounts in the Amazon Redshift database.
  Users can only access resources in the database that their user accounts have been granted
  permission to access. You create these Amazon Redshift user accounts and manage permissions by
  using the [CREATE USER](../dg/r_CREATE_USER.md "../dg/r_CREATE_USER.md"), [CREATE GROUP](../dg/r_CREATE_GROUP.md "../dg/r_CREATE_GROUP.md"), [GRANT](../dg/r_GRANT.md "../dg/r_GRANT.md"), and [REVOKE](../dg/r_REVOKE.md "../dg/r_REVOKE.md") SQL statements. For more information, see [Managing database security](../dg/r_Database_objects.md "../dg/r_Database_objects.md")
  in the Amazon Redshift Database Developer Guide.
- Temporary database credentials and single sign-on –
  In addition to creating and managing database users using SQL commands, such as CREATE USER
  and ALTER USER, you can configure your SQL client with custom Amazon Redshift JDBC or ODBC drivers.
  These drivers manage the process of creating database users and temporary passwords as part
  of the database logon process.

The drivers authenticate database users based on AWS Identity and Access Management
(IAM) authentication. If you already manage user identities outside of AWS, you can use a
SAML 2.0-compliant identity provider (IdP) to manage access to Amazon Redshift resources. You use an
IAM role to configure your IdP and AWS to permit your federated users to generate temporary
database credentials and log on to Amazon Redshift databases. For more information, see [Using IAM authentication to
generate database user credentials](generating-user-credentials.md "generating-user-credentials.md").
This documentation helps you understand how to apply the shared responsibility model when
using Amazon Redshift. The following topics show you how to configure Amazon Redshift to meet your
security and compliance objectives. You also learn how to use other AWS services that help you
to monitor and secure your Amazon Redshift resources.

###### Topics

- [Data protection in Amazon Redshift](security-data-protection.md "security-data-protection.md")
- [Identity and access management in
  Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md")
- [Managing Amazon Redshift admin passwords
  using AWS Secrets Manager](redshift-secrets-manager-integration.md "redshift-secrets-manager-integration.md")
- [Logging and monitoring in Amazon Redshift](security-incident-response.md "security-incident-response.md")
- [Compliance validation for Amazon Redshift](security-compliance.md "security-compliance.md")
- [Resilience in Amazon Redshift](security-disaster-recovery-resiliency.md "security-disaster-recovery-resiliency.md")
- [Infrastructure security in
  Amazon Redshift](security-network-isolation.md "security-network-isolation.md")
- [Configuration and vulnerability analysis in Amazon Redshift](security-vulnerability-analysis-and-management.md "security-vulnerability-analysis-and-management.md")
