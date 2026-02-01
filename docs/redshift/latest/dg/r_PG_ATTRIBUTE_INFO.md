Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_ATTRIBUTE_INFO

PG_ATTRIBUTE_INFO is an Amazon Redshift system view built on the PostgreSQL catalog table
PG_ATTRIBUTE and the internal catalog table PG_ATTRIBUTE_ACL. PG_ATTRIBUTE_INFO includes
details about columns of a table or view, including column access control lists, if
any.

## Table columns

PG_ATTRIBUTE_INFO shows the following column in addition to the columns in
PG_ATTRIBUTE.

| Column name | Data type | Description                                                                                     |
| ----------- | --------- | ----------------------------------------------------------------------------------------------- |
| attacl      | aclitem[] | The column-level access privileges, if any, that have been granted specifically on this column. |
