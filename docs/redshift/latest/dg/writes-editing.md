Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Editing datashares created in your account in

Amazon Redshift

You can edit a datashare created in your account using the console and with
SQL.

Console
On the console, take the following steps to connect to a database
first to see the list of datashares created in your account.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   then choose your cluster. The cluster details page appears.
3. Choose **Datashares**.
4. In the **Datashares created in my account**
   section, choose **Connect to database**.
5. Choose the datashare you want to edit, then choose
   **Edit**. The datashare details page
   appears.
6. Make any changes in the **Datashare objects**
   or **Data consumers** section.
7. Choose **Save changes**. Amazon Redshift updates your
   datashare with the changes.

###### Note

If you chose to publish your datashare to the AWS Glue Data Catalog,
you can't edit the configuration to publish the datashare
to other Amazon Redshift accounts.

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

Use REVOKE USAGE ON to revoke permissions on the datashare to certain
consumers. It revokes USAGE permissions on objects within a datashare and
instantly stops access to all consumer clusters. Listing datashares and
the metadata queries, such as listing databases and tables, doesn't
return the shared objects after access is revoked. Revoke access to the
datashare from namespaces if you don't want to share the data with
the consumers anymore.

```
REVOKE USAGE ON DATASHARE salesshare FROM NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```

If you don't want to share the data with the consumers anymore, revoke
access to the datashare from AWS accounts:

```
REVOKE USAGE ON DATASHARE salesshare FROM ACCOUNT '123456789012';
```
