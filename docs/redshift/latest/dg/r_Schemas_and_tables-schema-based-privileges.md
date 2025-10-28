Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Schema-based

permissions

Schema-based permissions are determined by the owner of the schema:

- By default, all users have CREATE and USAGE permissions on the PUBLIC schema of
  a database. To disallow users from creating objects in the PUBLIC schema of a
  database, use the [REVOKE](r_REVOKE.md "r_REVOKE.md") command to
  remove that permission.
- Unless they are granted the USAGE permission by the object owner, users cannot
  access any objects in schemas they do not own.
- If users have been granted the CREATE permission to a schema that was created
  by another user, those users can create objects in that schema.
