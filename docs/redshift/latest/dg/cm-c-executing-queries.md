Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Assigning queries to queues

With Amazon Redshift, you can manage workload concurrency and prioritize queries by assigning them to queues.
Queues allow you to allocate resources like memory and CPU for different types of queries or users,
ensuring critical queries get prioritized over less important ones. The following sections describe
how to create queues, configure their properties, and assign incoming queries based on criteria you define.

The following examples assign queries to queues according to user roles, user groups, and query groups.

##

Assigning queries to queues based on user roles

If a user is assigned to a role and that role is attached to a queue, then queries run by that user are assigned to that queue.
The following example creates a user role named `sales_rw` and assigns the user `test_user` to that role.

```
create role sales_rw;
grant role sales_rw to test_user;

```

You can also combine permissions of two roles by explicitly granting one role to another role. Assigning a nested role
to a user grants permissions of both roles to the user.

```
create role sales_rw;
create role sales_ro;
grant role sales_ro to role sales_rw;
grant role sales_rw to test_user;

```

To see the list of users that have been granted roles in the cluster, query the SVV_USER_GRANTS table. To see the list
of roles that have been granted roles in the cluster, query the SVV_ROLE_GRANTS table.

```
select * from svv_user_grants;
select * from svv_role_grants;
```

## Assigning queries to queues based on user groups

If a user group name is listed in a queue definition, queries run by members of that
user group are assigned to the corresponding queue. The following example creates user
groups and adds users to groups by using the SQL commands [CREATE USER](r_CREATE_USER.md "r_CREATE_USER.md"), [CREATE GROUP](r_CREATE_GROUP.md "r_CREATE_GROUP.md"), and [ALTER GROUP](r_ALTER_GROUP.md "r_ALTER_GROUP.md").

```
create group admin_group with user admin246, admin135, sec555;
create user vp1234 in group ad_hoc_group password 'vpPass1234';
alter group admin_group add user analyst44, analyst45, analyst46;
```

## Assigning a

query to a query group

You can assign a query to a queue at runtime by assigning your query to the
appropriate query group. Use the SET command to begin a query group.

```
SET query_group TO *`group_label`*
```

Here, `group_label`
is a query group label that is listed in the WLM configuration.

All queries that you run after the `SET query_group` command run as
members of the specified query group until you either reset the query group or end your
current login session. For information about setting and resetting Amazon Redshift objects, see
[SET](r_SET.md "r_SET.md") and [RESET](r_RESET.md "r_RESET.md") in the SQL Command Reference.

The query group labels that you specify must be included in the current WLM
configuration; otherwise, the _SET query_group_ command has no effect
on query queues.

The label defined in the TO clause is captured in the query logs so that you can use
the label for troubleshooting. For information about the query_group configuration
parameter, see [query_group](r_query_group.md "r_query_group.md") in the
Configuration Reference.

The following example runs two queries as part of the query group 'priority' and then
resets the query group.

```
set query_group to 'priority';
select count(*)from stv_blocklist;
select query, elapsed, substring from svl_qlog order by query desc limit 5;
reset query_group;
```

## Assigning queries to

the superuser queue

To assign a query to the superuser queue, log on to Amazon Redshift as a superuser and then
run the query in the superuser group. When you are done, reset the query group so that
subsequent queries do not run in the superuser queue.

The following example assigns two commands to run in the superuser queue.

```
set query_group to 'superuser';

analyze;
vacuum;
reset query_group;
```

To view a list of superusers, query the PG_USER system catalog table.

```
select * from pg_user where usesuper = 'true';
```
