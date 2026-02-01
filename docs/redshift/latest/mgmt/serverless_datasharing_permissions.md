Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Granting access to view

datashares

A superuser can provide access to users who aren't superusers so that they
can view the datashares created by all users.

To grant access to a datashare for a user, use the following command to provide
datashare access for a user, where datashare_name is the name of the datashare and
user-name is the name of the user for whom you want to provide access.

```
grant share on datashare datashare_name to "IAM:test_user";
```

To grant access to a datashare for a user group, first create a user group with
users. For information on how to create user groups, see [CREATE GROUP](../dg/r_CREATE_GROUP.md "../dg/r_CREATE_GROUP.md"). Then, grant
datashare access to a user using the following command, where datashare_name is the
name of the datashare and user-group is the name of the user-group to that you want
to grant access.

```
grant share on datashare datashare_name to group user_group;
```

For information on how to use the GRANT statement, see [GRANT](../dg/r_GRANT.md "../dg/r_GRANT.md").
