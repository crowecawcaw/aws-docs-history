# Cross-account data sharing in Lake Formation

Lake Formation cross-account capabilities allow users to securely share distributed data lakes across
multiple AWS accounts, AWS organizations or directly with IAM principals in another
account providing fine-grained access to the Data Catalog metadata and underlying data. Large
enterprises typically use multiple AWS accounts, and many of those accounts might need
access to a data lake managed by a single AWS account. Users and AWS Glue extract, transform,
and load (ETL) jobs can query and join tables across multiple accounts and still take
advantage of Lake Formation table-level and column-level data protections.

When you grant Lake Formation permissions on a Data Catalog resource to an external account or directly
to an IAM principal in another account, Lake Formation uses the AWS Resource Access Manager (AWS RAM) service to share the
resource. If the grantee account is in the same organization as the grantor account, the
shared resource is available immediately to the grantee. If the grantee account is not in the
same organization, AWS RAM sends an invitation to the grantee account to accept or reject the
resource grant. Then, to make the shared resource available, the data lake administrator in
the grantee account must use the AWS RAM console or AWS CLI to accept the invitation.

Lake Formation supports sharing Data Catalog resources with external accounts in hybrid access mode.
Hybrid access mode provides the flexibility to selectively enable Lake Formation permissions for
databases and tables in your AWS Glue Data Catalog.
With the Hybrid access mode, you now have an
incremental path that allows you to set Lake Formation permissions for a specific set of users without
interrupting the permission policies of other existing users or workloads.

For more information, see [Hybrid access mode](hybrid-access-mode.md "hybrid-access-mode.md").

###### Direct cross-account share

Authorized principals can share resources explicitly with an IAM principal in an
external account. This feature is useful when an account owner wants to have control over who
in the external account can access the resources. The permissions the IAM principal receives
will be a union of direct grants and the account level grants that is cascaded down to the
principals. Only the recipient of the permission grant can view the direct cross-account
grants. The principal who receives the resource share cannot share the resource with other
principals.

###### Methods for sharing Data Catalog resources

With a single Lake Formation grant operation, you can grant cross-account permissions on the following Data Catalog resources.

- A database
- An individual table (with optional column filtering)
- A few selected tables
- All tables in a database (by using the All Tables wildcard)
  There are two options for sharing your databases and tables with another AWS account or
  IAM principals in another account.

- Lake Formation tag-based access control (LF-TBAC) (recommended)

Lake Formation tag-based access control is an authorization strategy that defines permissions based
on attributes. You can use tag-based access control to share Data Catalog resources (databases,
tables, and columns) with external IAM principals, AWS accounts, Organizations and organizational units (OUs). In Lake Formation, these
attributes are called LF-tags. For more information, see [Managing a data
lake using Lake Formation tag-based access control](managing-dl-tutorial.md "managing-dl-tutorial.md").

###### Note

The LF-TBAC method of granting Data Catalog permissions use AWS Resource Access Manager for cross-account grants.

Lake Formation now supports granting cross-account permissions to Organizations and organizational units using LF-TBAC method.

To enable this capability, you need to update the **Cross account version settings** to **Version 3** or above.

For more information, see [Updating cross-account data sharing version settings](optimize-ram.md "optimize-ram.md").

- Lake Formation named resources

The Lake Formation cross-account data sharing using named resource method allows you to grant Lake Formation permissions with a grant option on Data Catalog tables and databases to external AWS accounts, IAM principals, organizations, or organizational units.
The grant operation automatically shares those resources.

###### Note

You can also allow the AWS Glue crawler to access a data store in a different account using Lake Formation credentials. For more information, see [Cross-account crawling](../../../glue/latest/dg/crawler-configuration.md#cross-account-crawling "../../../glue/latest/dg/crawler-configuration.md#cross-account-crawling") in AWS Glue Developer Guide.

Integrated services such as Athena and Amazon Redshift Spectrum require resource links to be able to include
shared resources in queries. For more information about resource links, see [How resource links work in Lake Formation](resource-links-about.md "resource-links-about.md").

For considerations and limitation, see [Cross-account data sharing best practices and considerations](cross-account-notes.md "cross-account-notes.md").

###### Topics

- [Prerequisites](cross-account-prereqs.md "cross-account-prereqs.md")
- [Updating cross-account data sharing version settings](optimize-ram.md "optimize-ram.md")
- [Sharing Data Catalog tables and databases across
  AWS accounts or IAM principals from external accounts](cross-account-data-share-steps.md "cross-account-data-share-steps.md")
- [Granting permissions on a database or table shared
  with your account](regranting-shared-resources.md "regranting-shared-resources.md")
- [Granting resource link permissions](granting-link-permissions.md "granting-link-permissions.md")
- [Accessing the underlying data of a shared
  table](cross-account-read-data.md "cross-account-read-data.md")
- [Cross-account CloudTrail logging](cross-account-logging.md "cross-account-logging.md")
- [Managing cross-account permissions using both
  AWS Glue and Lake Formation](hybrid-cross-account.md "hybrid-cross-account.md")
- [Viewing all cross-account grants using
  the GetResourceShares API operation](cross-account-getresourcepolicies.md "cross-account-getresourcepolicies.md")

###### Related topics

- [Overview of Lake Formation permissions](lf-permissions-overview.md "lf-permissions-overview.md")
- [Accessing and viewing shared Data Catalog tables and
  databases](viewing-shared-resources.md "viewing-shared-resources.md")
- [Creating resource links](creating-resource-links.md "creating-resource-links.md")
- [Troubleshooting cross-account access](troubleshooting.md#trouble-cross-account "troubleshooting.md#trouble-cross-account")
