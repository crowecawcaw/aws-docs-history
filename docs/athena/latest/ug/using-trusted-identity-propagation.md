

# Use Trusted identity propagation with Amazon Athena drivers
<a name="using-trusted-identity-propagation"></a>

Trusted identity propagation provides a new authentication option for organizations that want to centralize data permissions management and authorize requests based on their IdP identity across service boundaries. With IAM Identity Center, you can configure an existing IdP to manage users and groups and use AWS Lake Formation to define fine-grained access control permissions on catalog resources for these IdP identities. Athena supports identity propagation when querying data to audit data access by IdP identities to help your organization meet their regulatory and compliance requirements.

You can now connect to Athena using Java Database Connectivity (JDBC) or Open Database Connectivity (ODBC) drivers with single sign-on capabilities through IAM Identity Center. When you access Athena from tools like PowerBI, Tableau, or DBeaver, your identity and permissions automatically propagate to Athena through IAM Identity Center. This means your individual data access permissions are enforced directly when querying data, without requiring separate authentication steps or credential management.

For administrators, this feature centralizes access control through IAM Identity Center and Lake Formation, ensuring consistent permission enforcement across all supported analysis tools connecting to Athena. To get started, ensure your organization has configured IAM Identity Center as your identity source and set up the appropriate data access permissions for your users.

**Topics**
+ [Key definitions](#using-trusted-identity-propagation-key-definitions)
+ [Considerations](#using-trusted-identity-propagation-considerations)
+ [Prerequisites](#using-trusted-identity-propagation-prerequisites)
+ [Connect Athena to IAM Identity Center](using-trusted-identity-propagation-setup.md)
+ [Configure and deploy resources using AWS CloudFormation](using-trusted-identity-propagation-cloudformation.md)

## Key definitions
<a name="using-trusted-identity-propagation-key-definitions"></a>

1. **Application Role** – Role to exchange tokens, retrieve workgroup and customer managed AWS IAM Identity Center application ARN.

1. **Access Role** – Role to use with Athena drivers for running customer workflows with Identity enhanced credentials. This means this role is needed to access downstream services.

1. **Customer Managed Application** – The AWS IAM Identity Center Application. For more information, see [Customer Managed Application](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps.html).

## Considerations
<a name="using-trusted-identity-propagation-considerations"></a>

1. This feature only works for regions where Athena is generally available with trusted identity propagation. For more information on availability, see [Considerations and Limitations](https://docs.aws.amazon.com/athena/latest/ug/workgroups-identity-center.html).

1. The JDBC and ODBC drivers support trusted identity propagation with IAM-enabled workgroups.

1. You can use both JDBC and ODBC either as standalone drivers or with any BI or SQL tool with trusted identity propagation using this authentication plugin.

## Prerequisites
<a name="using-trusted-identity-propagation-prerequisites"></a>

1. You must have an AWS IAM Identity Center instance enabled. For more information, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html) for more information.

1. You must have a working external identity provider and the users or groups must be present in AWS IAM Identity Center. You can provision your users or groups automatically either manually or with SCIM. For more information, see [Provisioning an external identity provider into IAM Identity Center using SCIM](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html).

1. You must grant Lake Formation Permissions to users or groups for catalogs, databases, and tables. For more information, see [Use Athena to query data with Lake Formation](https://docs.aws.amazon.com/athena/latest/ug/security-athena-lake-formation.html).

1. You must have a working BI tool or SQL client to run Athena queries using the JDBC or ODBC driver.