

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Creating the consumer database
<a name="query-editor-v2-datashare-consumer"></a>

On the consumer cluster, you create a database from the datashare. These steps describe how to share data between two clusters in the same account. For information on sharing data across AWS accounts, see [Sharing data across AWS accounts](https://docs.aws.amazon.com/redshift/latest/dg/across-account.html) in the *Amazon Redshift Database Developer Guide*.

You can use SQL commands or the query editor v2 tree-view panel to create the database.

**To use SQL**

1. Create a database from the datashare for your account and the namespace of the producer cluster. For example:

   ```
   create database share_db from datashare mysource of account '123456789012' namespace 'p1234567-8765-4321-p10987654321'; 
   ```

1. Set permissions so that users can access the database and the schema. For example:

   ```
   grant usage on database share_db to usernames;
   ```

   ```
   grant usage on schema public to usernames;
   ```

**To use the query editor v2 tree-view panel**

1. Choose ![Plus sign icon inside a circle, indicating an add or create action.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/qev2-add.png)**Create**, and then choose **Database**.

1. Enter a **Database name**.

1. (Optional) Select **Users and groups**, and choose a **Database user**.

1. Choose **Create using a datashare**.

1. Choose the datashare.

1. Choose **Create database**.

   The new ![datashare](http://docs.aws.amazon.com/redshift/latest/mgmt/images/qev2-datashare.png)**datashare** database displays in the query editor v2 tree-view panel.

1. Set permissions so that users can access the database and the schema. For example:

   ```
   grant usage on database share_db to usernames;
   ```

   ```
   grant usage on schema public to usernames;
   ```