Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating the consumer

database

On the consumer cluster, you create a database from the datashare. These steps
describe how to share data between two clusters in the same account. For information
on sharing data across AWS accounts, see [Sharing data across AWS
accounts](../dg/across-account.md "../dg/across-account.md") in the _Amazon Redshift Database Developer Guide_.

You can use SQL commands or the query editor v2 tree-view panel to create the
database.

###### To use SQL

1. Create a database from the datashare for your account and the namespace of
   the producer cluster. For example:

```
create database *share\_db* from datashare *mysource* of account '*123456789012*' namespace '*p1234567-8765-4321-p10987654321*';
```

2. Set permissions so that users can access the database and the schema. For
   example:

```
grant usage on database *share\_db* to *usernames*;
```

```
grant usage on schema *public* to *usernames*;
```

###### To use the query editor v2 tree-view panel

1. Choose
   ![Plus sign icon inside a circle, indicating an add or create action.](images/qev2-add.png)
   **Create**, and then choose
   **Database**.
2. Enter a **Database name**.
3. (Optional) Select **Users and groups**, and choose a
   **Database user**.
4. Choose **Create using a datashare**.
5. Choose the datashare.
6. Choose **Create database**.

The new
![datashare](images/qev2-datashare.png)
**datashare** database displays in the
query editor v2 tree-view panel. 7. Set permissions so that users can access the database and the schema. For
example:

```
grant usage on database *share\_db* to *usernames*;
```

```
grant usage on schema *public* to *usernames*;
```
