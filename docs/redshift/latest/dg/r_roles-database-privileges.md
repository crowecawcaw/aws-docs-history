Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Database object permissions

Apart from system permissions, Amazon Redshift includes database object permissions that
define access options. These include such options as the ability to read data in tables
and views, write data, create tables, and drop tables. For more information, see [GRANT](r_GRANT.md "r_GRANT.md").

By using RBAC, you can assign database object permissions to roles, similarly to
how you can with system permissions. Then you can assign roles to users, authorize users
with system permissions, and authorize users with database permissions.
