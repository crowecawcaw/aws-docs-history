Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER DEFAULT PRIVILEGES for RBAC

Use the ALTER DEFAULT PRIVILEGES statement to define the default set of access
permissions to be applied to objects that are created in the future by the specified
user. By default, users can change only their own default access permissions. With RBAC,
you can set the default access permissions for roles. For more information, see the
[ALTER DEFAULT PRIVILEGES](r_ALTER_DEFAULT_PRIVILEGES.md "r_ALTER_DEFAULT_PRIVILEGES.md") command.

RBAC enables you to assign database object permissions to roles, similarly to system
permissions. Then you can assign roles to users, authorize users with system and/or
database permissions.
