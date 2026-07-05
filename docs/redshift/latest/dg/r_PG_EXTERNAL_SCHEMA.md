Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# PG\_EXTERNAL\_SCHEMA

Stores information about external schemas.

PG\_EXTERNAL\_SCHEMA is visible to all users. Superusers can see all rows; regular users
can see only metadata to which they have access. For more information, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md").

## Table columns

| Column name | Data type | Description              |
| ----------- | --------- | ------------------------ |
| esoid       | oid       | External schema ID.      |
| eskind      | integer   | Kind of external schema. |
| esdbname    | text      | External database name.  |
| esoptions   | text      | External schema options. |

## Example

The following example shows details for external schemas.

```
select esoid, nspname as schemaname, nspowner, esdbname as external_db, esoptions
from pg_namespace a,pg_external_schema b where a.oid=b.esoid;

esoid  | schemaname      | nspowner | external_db | esoptions
-------+-----------------+----------+-------------+-------------------------------------------------------------
100134 | spectrum_schema |      100 | spectrum_db | {"IAM_ROLE":"arn:aws:iam::123456789012:role/mySpectrumRole"}
100135 | spectrum        |      100 | spectrumdb  | {"IAM_ROLE":"arn:aws:iam::123456789012:role/mySpectrumRole"}
100149 | external        |      100 | external_db | {"IAM_ROLE":"arn:aws:iam::123456789012:role/mySpectrumRole"}
```
