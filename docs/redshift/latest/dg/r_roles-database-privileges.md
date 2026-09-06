

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Database object permissions
<a name="r_roles-database-privileges"></a>

Apart from system permissions, Amazon Redshift includes database object permissions that define access options. These include such options as the ability to read data in tables and views, write data, create tables, and drop tables. For more information, see [GRANT](r_GRANT.md).

By using RBAC, you can assign database object permissions to roles, similarly to how you can with system permissions. Then you can assign roles to users, authorize users with system permissions, and authorize users with database permissions.