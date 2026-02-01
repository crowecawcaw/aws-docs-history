Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Granting object level permissions to consumer

users and roles in Amazon Redshift

As a consumer administrator, you can grant permissions to consumer users and
roles at the object level by completing the following steps.

SQL
If you created your database without WITH PERMISSIONS, you can only
assign permissions on the entire database created from the datashare to
your users and roles.

```
GRANT USAGE ON DATABASE sales_db TO Bob;
```

```
GRANT USAGE ON SCHEMA sales_schema TO ROLE Analyst_role;
```

You can also create late-binding views on top of shared objects and
use these to assign granular permissions. You can also consider having
producer clusters create additional datashares for you with the
granularity required.

If you created your database with WITH PERMISSIONS, you must assign
object-level permissions for objects in the shared database. A user with
only the USAGE permission can’t access any objects in a database created
with WITH PERMISSIONS until they’re granted additional object-level
permissions..

```
GRANT SELECT ON sales_db.public.tickit_sales_redshift to Bob;
```

For more information about granting permissions with multi-warehouse writes,
see [Managing permissions for a
datashares in Amazon Redshift](writes-managing-permissions.md "writes-managing-permissions.md").
