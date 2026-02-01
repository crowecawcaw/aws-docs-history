Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Permissions you can grant to datashares

Different object types and various permissions you can grant to them in a data
sharing context.

Databases:

- CREATE
- USAGE
- ALTER
- DROP
  Schemas:

- CREATE
- USAGE
- ALTER
- DROP
  Tables:

- SELECT
- INSERT
- UPDATE
- DELETE
- TRUNCATE
- DROP
- ALTER
- REFERENCES
  Functions:

- EXECUTE
