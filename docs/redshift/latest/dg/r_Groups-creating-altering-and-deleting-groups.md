Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Creating, altering, and deleting groups

Only a superuser can create, alter, or drop groups.

You can perform the following actions:

- To create a group, use the [CREATE GROUP](r_CREATE_GROUP.md "r_CREATE_GROUP.md") command.
- To add users to or remove users from an existing group, use the [ALTER GROUP](r_ALTER_GROUP.md "r_ALTER_GROUP.md") command.
- To delete a group, use the [DROP GROUP](r_DROP_GROUP.md "r_DROP_GROUP.md") command. This command only drops the group, not
  its member users.
