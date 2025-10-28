# Managing data filters

To implement column-level, row-level, and cell-level security, you can create and maintain
data filters. Each data filter belongs to a Data Catalog table. You can create multiple data filters
for a table, and then use one or more of them when granting permissions on the table. You can
also define and apply data filters on nested columns that have `struct` datatypes allowing users to access only
sub-structures of nested columns.

You require `SELECT` permission with the grant option to create or view a
data filter. To allow principals in your
account to view and use a data filter, you can grant the
`DESCRIBE` permission on it.

###### Note

Lake Formation doesn't support granting `Describe` permission on a data filter, which is shared from another account.

You can manage data filters by using the AWS Lake Formation console, the API, or the AWS Command Line Interface
(AWS CLI).

For information about data filters, see [Data filters in Lake Formation](data-filtering.md#data-filters-about "data-filtering.md#data-filters-about")
