# Adding an Amazon S3 location to your data lake

To add a data location as storage in your data lake, you _register_ the
location (**Data lake location**) with AWS Lake Formation. You can then use Lake Formation
permissions for fine-grained access control to AWS Glue Data Catalog objects that point to this location
and to the underlying data in the location.

Lake Formation also allows to register a data location in hybrid access mode and provide you the
flexibility to selectively enable Lake Formation permissions for databases and tables in your Data Catalog.
With the Hybrid access mode, you have an incremental path that allows you to set Lake Formation
permissions for a specific set of users without interrupting the permission policies of other
existing users or workloads.

For more information on setting up hybrid access mode, see [Hybrid access mode](hybrid-access-mode.md "hybrid-access-mode.md")

When you register a location, that Amazon S3 path and all folders under that path are
registered.

For example, suppose that you have an Amazon S3 path organization like the following:

`/mybucket/accounting/sales/`

If you register `S3://mybucket/accounting`, the `sales`
folder is also registered and under Lake Formation management.

For more information about registering locations, see [Underlying data access control](access-control-underlying-data.md#underlying-data-access-control "access-control-underlying-data.md#underlying-data-access-control").

###### Note

Lake Formation permissions are recommended for structured data
(arranged in tables with rows and columns). If your data contains object-based
unstructured data, consider using Amazon S3 access grants to manage data access.

###### Topics

- [Requirements for roles used to register
  locations](registration-role.md "registration-role.md")
- [Registering an Amazon S3 location](register-location.md "register-location.md")
- [Registering an encrypted Amazon S3 location](register-encrypted.md "register-encrypted.md")
- [Registering an Amazon S3 location in another AWS
  account](register-cross-account.md "register-cross-account.md")
- [Registering an encrypted Amazon S3 location across AWS
  accounts](register-cross-encrypted.md "register-cross-encrypted.md")
- [Deregistering an Amazon S3 location](unregister-location.md "unregister-location.md")
