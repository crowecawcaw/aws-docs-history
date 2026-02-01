Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations when using Amazon Redshift federated permissions

The following are considerations and limitations for sharing Amazon Redshift data with AWS Glue Data Catalog using federated permissions. For general
information on data sharing considerations and limitations, see [Considerations when using data sharing in Amazon Redshift](datashare-considerations.md "datashare-considerations.md").

This feature is supported only with [cluster versions 197 and onwards](../mgmt/cluster-versions.md#cluster-version-197 "../mgmt/cluster-versions.md#cluster-version-197").

**Supported Regions**

- Asia Pacific (Mumbai)
- US West (N. California)
- Europe (Frankfurt)
- US East (Ohio)
- US East (N. Virginia)
- US West (Oregon)
- Asia Pacific (Hong Kong)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Europe (Ireland)
- Europe (Stockholm)
  **Environment Requirements**

Both registered and consumer Redshift instances must meet these requirements:

- **Instance type**: RA3 provisioned clusters or Serverless workgroups
- **Region**: Same AWS Region
- **Account**: Same AWS account
- **Encryption**: Enabled
- **Isolation level**: Snapshot isolation
  **Unsupported Objects**

Consumer instances cannot access the following objects from the federated permissions catalog:

- SQL UDFs, Python UDFs, and Lambda UDFs
- ML Models
- External schema created on the registered instance
  **Coarse-grained Access Control Restrictions**

Grant is supported only on table, database, schema, functions used with 3dot notation

**Fine-grained access control restrictions**

In addition to standard Row-level Security (RLS) and Dynamic Data Masking (DDM) policy restrictions in Amazon Redshift, consumer instances cannot access RLS or
DDM protected objects from the federated permissions catalog if the policies contain these system functions:

- `user_is_member_of`
- `role_is_member_of`
- `user_is_member_of_role`
  Note: In current release of Redshift, metadata of FGAC related tables accessed on consuming Redshift Warehouses are temporarily visible in catalog.

**Metadata Discovery**

- SHOW commands are supported for Columns, Tables, Stored Procedures, Functions, and Parameters.
  **Lake Formation**

- Lake Formation permissions are not supported on objects in Amazon Redshift federated permissions catalog.
  **Identity**

- Only users registered with IAM or AWS IAM Identity Center can query objects in Amazon Redshift federated permissions catalog.
- When your Amazon Redshift Cluster or Amazon Redshift Serverless Namespace is registered with Amazon Redshift federated permissions, you cannot manage the data governance for IAM federated user(s) using the IAM federated group(s). This includes any previously configured granular access controls on objects through IAM federated groups.
- When registering an existing Amazon Redshift Cluster or Amazon Redshift Serverless Namespace with an Amazon Redshift federated permissions catalog, all AWS IAM Identity Center federated users, including those who previously had access,
  must be explicitly granted CONNECT privileges to access the cluster or workgroup.
  For more information about granting CONNECT privileges, see [Connect privileges](federated-permissions-prereqs.md#federated-permissions-prereqs-connect "federated-permissions-prereqs.md#federated-permissions-prereqs-connect").
- AWS IAM Federated users who connect to Amazon Redshift clusters or workgroups using principal tags and temporary IAM credentials are not recognized as global identities and cannot access Amazon Redshift federated permissions catalogs. Only AWS IAM Identity Center
  federated users and AWS IAM federated users or roles are authorized to query Amazon Redshift federated permissions catalogs.
- When your Amazon Redshift Cluster or Amazon Redshift Serverless namespace is registered with Amazon Redshift federated permissions, the following GRANT command limitations apply to AWS IAM Identity Center federated users or roles and AWS IAM federated users or roles:

      + You cannot grant a federated role to any user or role. One exception to this rule is you can grant a Redshift database role to a IAM federated user.
      + You cannot grant any role to a federated role or user. One exception to this rule is you can grant a system-defined role to federated user or role.

  **Engine Access**

- Access from engines other than Redshift is not supported
  **Alter User Set Global identity**

- Supported only on "Select", "Delete", "Update", "Show", "Insert"
- IAM role associated with a user via ALTER USER SET GLOBAL IDENTITY is only used when the query is against Redshift Warehouse with Federated Permissions and only when the query targets a relation, such as SELECT, UDPATE and DELETE queries.
- Such IAM role is also used SHOW DATABASES, SHOW SCHEMAS and SHOW TABLES queries against resources in Redshift Warehouse with Federated Permissions.
- Such IAM role is not used on data definition queries such as CREATE, ALTER and DROP.
  **Error Message**

- Any unsupported operations against database in Amazon Redshift Federated Permissions catalog will show following error:

```
Operation is not supported through datashares
```
