Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with read-only

data sharing in the console

With Amazon Redshift, you can manage data sharing with writes using the console to control
access and govern data across Amazon Redshift clusters and AWS accounts. The following sections
provide step-by-step instructions on configuring and managing data sharing with writes
using the Amazon Redshift console.

Use the Amazon Redshift console to manage datashares created in your account or shared from
other accounts.

You need permissions to create, edit, or delete datashares. For information, see
[Managing permissions for a
datashares in Amazon Redshift](writes-managing-permissions.md "writes-managing-permissions.md").

- If you are a producer administrator, you can create datashares, add data
  consumers, add datashare objects, create databases from datashares, edit
  datashares, or delete datashares from the **CLUSTERS** tab.

From the navigation menu, navigate the **Clusters** tab,
choose a cluster from the cluster list. Then do one of the following:

    + Choose the **Datashares** tab, choose a datashare from
     the **Datashares created in my namespace** section. Then do
     one of the following:




    	- [Create a datashare](datashare-creation.md#create-datashare-console "datashare-creation.md#create-datashare-console")


    	When a datashare is created, you can add datashare objects or data
    	 consumers. For more information, see [Add datashare objects to
    	 datashares](datashare-creation.md#add-datashare-object-console "datashare-creation.md#add-datashare-object-console") and [Add data consumers to
    	 datashares](datashare-creation.md#add-data-consumer-console "datashare-creation.md#add-data-consumer-console").
    	- [Editing datashares created in your
    	 account](manage-datashare-existing-console.md#edit-datashare-console "manage-datashare-existing-console.md#edit-datashare-console")
    	- [Deleting a datashare created in your
    	 account](manage-datashare-existing-console.md#delete-datashare-console "manage-datashare-existing-console.md#delete-datashare-console")
    + Choose **Datashares** and choose a datashare from the
     **Datashares from other clusters** section. Then do one
     of the following:




    	- [Create a datashare](datashare-creation.md#create-datashare-console "datashare-creation.md#create-datashare-console")
    	- [Creating databases from
    	 datashares](query-datashare-console.md#create-database-from-datashare-console "query-datashare-console.md#create-database-from-datashare-console")
    + Choose **Databases** and choose a database from the
     **Databases** section. Then choose **Create
     datashare**. For more information, see [Creating databases from
     datashares](query-datashare-console.md#create-database-from-datashare-console "query-datashare-console.md#create-database-from-datashare-console").

###### Note

To view databases and objects within databases or to view datashares in the
cluster, connect to a database. For more information, see [Connecting to a database](connect-database-console.md "connect-database-console.md").
