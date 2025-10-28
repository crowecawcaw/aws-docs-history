Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Granting query monitoring

permissions for a role

Users with a role that has `sys:monitor` permission can view all
queries. In addition, users with a role that has `sys:operator`
permission can cancel queries, analyze query history, and perform vacuum
operations.

###### To grant query monitoring permission for a role

1. Enter the following command to provide system monitor access, where
   _role-name_ is the name of the role for which you
   want to provide access.

```
grant role sys:monitor to "IAMR:*role-name*";
```

2. (Optional) Enter the following command to provide system operator access,
   where _role-name_ is the name of the role for which you
   want to provide access.

```
grant role sys:operator to "IAMR:*role-name*";
```
