Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Deleting a datashare created in your account in

Amazon Redshift

You can delete a datashare created in your account using the console or with
SQL.

Console
To delete a datashare created in your account using the console, first
connect to a database to see the list of datashares created in your
account.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   then choose your cluster. The cluster details page appears.
3. Choose **Datashares**. The datashare list
   appears.
4. In the **Datashares created in my account**
   section, choose **Connect to database**.
5. Choose one or more datashares you want to delete, then choose
   **Delete**. The Delete datashares page
   appears.

Deleting a datashare shared with Lake Formation doesn't automatically
remove the associated permissions in Lake Formation. To remove them, go to
the Lake Formation console. 6. Type **Delete** to confirm deleting the
specified datashares. 7. Choose **Delete**.

After datashares are deleted, datashare consumers lose access to the
datashares.

SQL
You can use SQL to delete the datashare objects at any point using
[DROP DATASHARE](r_DROP_DATASHARE.md "r_DROP_DATASHARE.md").
Cluster superusers and owners of datashare can drop datashares.

The following example drops a datashare named
`salesshare`.

```
DROP DATASHARE salesshare;
```
