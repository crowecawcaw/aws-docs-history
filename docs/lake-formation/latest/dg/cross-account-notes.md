# Cross-account data sharing best practices and considerations

Lake Formation cross-account capabilities allow users to securely share distributed data lakes across multiple AWS accounts, AWS organizations
or directly with IAM principals in another account providing fine-grained access to the Data Catalog metadata and underlying data.

Consider the following best practices when using Lake Formation cross-account data sharing:

- There is no limit to the number of Lake Formation permission grants that you can make to
  principals in your own AWS account. However, Lake Formation uses AWS Resource Access Manager (AWS RAM) capacity for cross-account
  grants that your account can make with the named resource method. To
  maximize the AWS RAM capacity, follow these best practices for the named resource
  method:
  - Use the new cross-account grant mode (**Version 3** and above under
    **Cross account version settings**) to share a resource with an
    external AWS account. For more information, see [Updating cross-account data sharing version settings](optimize-ram.md "optimize-ram.md").
  - Arrange AWS accounts into organizations, and grant permissions to
    organizations or organizational units. A grant to an organization or
    organizational unit counts as one grant.

  Granting to organizations or organizational units also eliminates the need to
  accept an AWS Resource Access Manager (AWS RAM) resource share invitation for the grant. For more
  information, see [Accessing and viewing shared Data Catalog tables and
  databases](viewing-shared-resources.md "viewing-shared-resources.md").
  - Instead of granting permissions on many individual tables in a database, use
    the special **All tables** wildcard to grant permissions on all
    tables in the database. Granting on **All tables** counts as a
    single grant. For more information, see [Granting permissions on Data Catalog resources](granting-catalog-permissions.md "granting-catalog-permissions.md").

###### Note

For more information about requesting a higher limit for the number of resource shares in AWS RAM,
see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the _AWS General Reference_.

- You must create a resource link to a shared database for that database to appear
  in the Amazon Athena and Amazon Redshift Spectrum query editors. Similarly, to be able to
  query shared tables using Athena and Redshift Spectrum, you must create resource links to the
  tables. The resource links then appear in the tables list of the query editors.

Instead of creating resource links for many individual tables for querying, you
can use the **All tables** wildcard to grant permissions on all
tables in a database. Then, when you create a resource link for that database and
select that database resource link in the query editor, you'll have access to all
tables in that database for your query. For more information, see [Creating resource links](creating-resource-links.md "creating-resource-links.md").

- When you share resources directly with principals in another account, the IAM principal
  in the recipient account may not have permission to create resource links to be able to
  query the shared tables using Athena and Amazon Redshift Spectrum. Instead of creating a
  resource link for each table that is shared, the data lake administrator can create a
  placeholder database and grant `CREATE_TABLE` permission to the `ALLIAMPrincipal` group.
  Then, all IAM principals in the recipient account can create
  resource links in the placeholder database and start querying the shared tables.

See the example CLI command for granting permissions to `ALLIAMPrincipals` in [Granting database permissions using the
named resource method](granting-database-permissions.md "granting-database-permissions.md").

- When cross-account permissions are granted directly to a principal, only the recipient
  of the grant can view these permissions. The data lake administrator in the recipient's
  AWS account cannot view these direct grants.
- Athena and Redshift Spectrum support column-level access control, but only for inclusion, not
  exclusion. Column-level access control is not supported in AWS Glue ETL jobs.
- When a resource is shared with your AWS account, you can grant permissions on
  the resource only to users in your account. You can't grant permissions on the
  resource to other AWS accounts, to organizations (not even your own organization),
  or to the `IAMAllowedPrincipals` group.
- You can't grant `DROP` or `Super` on a database to an
  external account.
- Revoke cross-account permissions before you delete a database or table. Otherwise,
  you must delete orphaned resource shares in AWS Resource Access Manager.

###### See also

- [Lake Formation tag-based access control best
  practices and considerations](lf-tag-considerations.md "lf-tag-considerations.md")
- [CREATE_TABLE](lf-permissions-reference.md#perm-create-table "lf-permissions-reference.md#perm-create-table") in the
  [Lake Formation permissions reference](lf-permissions-reference.md "lf-permissions-reference.md") for more cross-account access rules
  and limitations.
