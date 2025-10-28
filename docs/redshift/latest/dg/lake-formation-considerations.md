Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations for data sharing with AWS Lake Formation in

Amazon Redshift

The following are considerations and limitations for sharing Amazon Redshift data with Lake Formation.
For information on data sharing considerations and limitations, see [Considerations when using data sharing in Amazon Redshift](datashare-considerations.md "datashare-considerations.md"). For information about
Lake Formation limitations, see [Notes on working with Amazon Redshift
datashares in Lake Formation](../../../lake-formation/latest/dg/notes-rs-datashare.md "../../../lake-formation/latest/dg/notes-rs-datashare.md").

- Sharing a datashare to Lake Formation across Regions is currently unsupported.
- If column-level filters are defined for a user on a shared relation, performing
  a `SELECT *` operation returns only the columns the user has access
  to.
- Cell-level filters from Lake Formation are unsupported.
- If you created and shared a view and its tables to Lake Formation, you can configure
  filters to manage access of the tables, Amazon Redshift enforces Lake Formation defined policies
  when consumer cluster users access shared objects. When a user accesses a view
  shared with Lake Formation, Redshift enforces only the Lake Formation policies defined on the view
  and not the tables contained within the view. However, when users directly access
  the table, Redshift enforces the defined Lake Formation policies on the table.
- You can't create materialized views on the consumer based on a shared
  table if the table has Lake Formation filters configured.
- The Lake Formation administrator must have [data lake administrator](../../../lake-formation/latest/dg/getting-started-setup.md#create-data-lake-admin "../../../lake-formation/latest/dg/getting-started-setup.md#create-data-lake-admin") permissions and the [required permissions to accept a datashare](../../../lake-formation/latest/dg/redshift-ds-prereqs.md "../../../lake-formation/latest/dg/redshift-ds-prereqs.md").
- The producer consumer cluster must be an RA3 cluster with the latest Amazon Redshift
  cluster version or a serverless workgroup to share datashares via Lake Formation.
- Both the producer and consumer clusters must be encrypted.
- Redshift row-level and column-level access control policies implemented in the
  producer cluster or workgroup are ignored when the datashare is shared to Lake Formation.
  The Lake Formation administrator must configure these policies in Lake Formation. The producer cluster
  or workgroup administrator can turn off RLS for a table by using the [ALTER
  TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md") command.
- Sharing datashares via Lake Formation is only available to users who have access to both
  Redshift and Lake Formation.
