Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Groups

Groups are collections of users who are all granted whatever permissions are associated
with the group. You can use groups to assign permissions. For example, you can
create different groups for sales, administration, and support and give the users in each
group the appropriate access to the data they need
for their work. You can grant or revoke permissions at the group level, and those changes
will apply to all members of the group, except for superusers.

To view all user groups, query the PG\_GROUP system catalog table:

```
select * from pg_group;
```

For example, to list all database users by group, run the following SQL.

```
SELECT u.usesysid
,g.groname
,u.usename
FROM pg_user u
LEFT JOIN pg_group g ON u.usesysid = ANY (g.grolist)
```
