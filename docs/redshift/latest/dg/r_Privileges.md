Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Default database user permissions

When you create a database object, you are its owner. By default, only a superuser or
the owner of an object can query, modify, or grant permissions on the object. For users to
use an object, you must grant the necessary permissions to the user or the group that
contains the user. Database superusers have the same permissions as database owners.

Amazon Redshift supports the following permissions: SELECT, INSERT, UPDATE, DELETE, REFERENCES,
CREATE, TEMPORARY, and USAGE. Different permissions are associated with different object
types. For information about database object permissions supported by Amazon Redshift, see the
[GRANT](r_GRANT.md "r_GRANT.md") command.

Only the owner has the permission to modify or destroy an object.

By default, all users have CREATE and USAGE permissions on the PUBLIC schema of a database.
To disallow users from creating objects in the PUBLIC schema of a database, use the REVOKE command to remove that permission.

To revoke a permission that was previously granted, use the [REVOKE](r_REVOKE.md "r_REVOKE.md") command. The permissions of the object owner, such as DROP,
GRANT, and REVOKE permissions, are implicit and cannot be granted or revoked. Object owners
can revoke their own ordinary permissions, for example, to make a table read-only for
themselves and others. Superusers retain all permissions regardless of GRANT and REVOKE
commands.
