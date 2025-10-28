Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating, altering, and

deleting groups

Only a superuser can create, alter, or drop groups.

You can perform the following actions:

- To create a group, use the [CREATE GROUP](r_CREATE_GROUP.md "r_CREATE_GROUP.md") command.
- To add users to or remove users from an existing group, use the [ALTER GROUP](r_ALTER_GROUP.md "r_ALTER_GROUP.md") command.
- To delete a group, use the [DROP GROUP](r_DROP_GROUP.md "r_DROP_GROUP.md") command. This command only drops the group, not
  its member users.
