Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Removing datashare objects from

a datashare in Amazon Redshift

You can remove one or more objects from a datashare by using the following
procedure.

Console
To remove one or more objects from a datashare on the consoe, follow
these steps.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   then choose your cluster. The cluster details page appears.
3. Choose **Datashares**.
4. In the **Datashares created in my account**
   section, choose **Connect to database**. For more
   information, see [Connecting to a database](connect-database-console.md "connect-database-console.md").
5. Choose the datashare you want to edit, then choose
   **Edit**. The datashare details page
   appears.
6. To remove one or more datashare objects to the datashare, do one
   of the following:
   - To remove schemas from the datashare, choose one or more
     schemas. Then choose **Remove**. Amazon Redshift
     removes the specified schemas and all the objects of the
     specified schemas from the datashare.
   - To remove tables and views from the datashare, choose one
     or more tables and views. Then choose
     **Remove**. Alternatively, choose
     **Remove by schema** to remove all tables
     and views in the specified schemas.
   - To remove user-defined functions from the datashare,
     choose one or more user-defined functions. Then choose
     **Remove**. Alternatively, choose
     **Remove by schema** to remove all
     user-defined functions in the specified schemas.

SQL
Use ALTER DATASHARE to remove objects from datashares at any point
from the datashare. To remove a schema, use the following command:

```
ALTER DATASHARE salesshare REMOVE SCHEMA PUBLIC;
```

To remove a table, use the following command:

```
ALTER DATASHARE salesshare REMOVE TABLE public.tickit_sales_redshift;
```
