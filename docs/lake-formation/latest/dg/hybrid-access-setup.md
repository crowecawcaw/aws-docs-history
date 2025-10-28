# Setting up hybrid access mode - common scenarios

As with Lake Formation permissions, you generally have two types of scenarios in which you can use
hybrid access mode to manage data access: Provide access to principals within one
AWS account and provide access to an external AWS account or principal.

This section provides instructions for setting up hybrid access mode in the following scenarios:

###### Manage permissions in hybrid access mode within one AWS account

- [Converting an AWS Glue resource to a hybrid resource](hybrid-access-mode-new.md "hybrid-access-mode-new.md") – You
  are currently providing access to tables in a database for all principals in your account
  using IAM permissions for Amazon S3 and AWS Glue but want to adopt Lake Formation to manage permissions
  incrementally.

- [Converting a Lake Formation resource to a hybrid resource](hybrid-access-mode-update.md "hybrid-access-mode-update.md") –
  You are currently using Lake Formation to manage access for tables in a database for all principals
  in your account but want to use Lake Formation only for specific principals. You want to provide
  access to new principals by using IAM permissions for AWS Glue and Amazon S3 on the same
  database and tables.

###### Manage permissions in hybrid access mode across AWS accounts

- [Sharing an AWS Glue resource using hybrid
  access mode](hybrid-access-mode-cross-account.md "hybrid-access-mode-cross-account.md") – You're currently not using
  Lake Formation to manage permissions for a table but want to apply Lake Formation permissions to provide
  access for principals in another account.
- [Sharing a Lake Formation resource using hybrid access mode](hybrid-access-mode-cross-account-IAM.md "hybrid-access-mode-cross-account-IAM.md") – You're using Lake Formation to
  manage access for a table but want to provide access for principals in another account by
  using IAM permissions for AWS Glue and Amazon S3 on the same database and tables.

###### Setting up hybrid access mode – High-level steps

1. Register the Amazon S3 data location with Lake Formation by selecting **Hybrid access
   mode**.
2. Principals must have `DATA_LOCATION` permission on a
   data lake location to create Data Catalog tables or databases that point to that location.
3. Set the **Cross-account version setting** to Version 4.
4. Grant fine-grained permissions to specific IAM users or roles on databases and tables.
   At the same time, make sure to set `Super` or `All` permissions to the
   `IAMAllowedPrincipals` group on the database and all or selected tables in the
   database.
5. Opt in the principals and resources. Other principals in the account can continue accessing the databases and tables
   using IAM permission policies for AWS Glue and Amazon S3 actions.
6. Optionally clean up IAM permission policies for Amazon S3 for the principals that are opted in to use
   Lake Formation permissions.
