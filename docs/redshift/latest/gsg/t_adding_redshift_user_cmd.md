Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Create a user

By default, only the admin user that you created when you launched the data warehouse has
access to the default database in the data warehouse. To grant other users access, create one
or more accounts. Database user accounts are global across all the databases in a
data warehouse, and not per individual database.

Use the CREATE USER command to create a new user. When you create a new user, you
specify the name of the new user and a password. We recommend that you specify a
password for the user. It must have 8–64 characters, and it must include at least
one uppercase letter, one lowercase letter, and one numeral.

For example, to create a user named `GUEST` with password
`ABCd4321`, run the following command.

```
CREATE USER GUEST PASSWORD 'ABCd4321';
```

To connect to the `SALESDB` database as the `GUEST` user, use the same password when you created the user, such as `ABCd4321`.

For information about other command options, see [CREATE USER](../dg/r_CREATE_USER.md "../dg/r_CREATE_USER.md") in the _Amazon Redshift Database Developer Guide_.
