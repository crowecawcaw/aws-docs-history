Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# RLS policy ownership and management

As a superuser, security administrator, or user that has the sys:secadmin role, you
can create, modify, attach, and detach RLS policies. RLS policies can be attached to
tables, views, late binding views (LBVs), and materialized views (MVs). At the object
level, you can turn row-level security on or off without modifying the schema definition
for tables.

To get started with row-level security, following are SQL statements that you can use:

- Use the ALTER TABLE statement to turn on or off RLS on a table, view, or late binding view.
  For more information, see [ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md").
- Use the ALTER MATERIALIZED VIEW statement to statement to turn on or off RLS on
  a materialized view (MV). For more information, see [ALTER MATERIALIZED VIEW](r_ALTER_MATERIALIZED_VIEW.md "r_ALTER_MATERIALIZED_VIEW.md").
- Use the CREATE RLS POLICY statement to create a security policy for one or more tables, and
  specify one or more users or roles in the policy.

For more information, see [CREATE RLS POLICY](r_CREATE_RLS_POLICY.md "r_CREATE_RLS_POLICY.md").

- Use the ALTER RLS POLICY statement to alter the policy, such as changing the policy
  definition. You can use the same policy for multiple tables or views.

For more information, see [ALTER RLS POLICY](r_ALTER_RLS_POLICY.md "r_ALTER_RLS_POLICY.md").

- Use the ATTACH RLS POLICY statement to attach a policy to one or more relations, to one or
  more users, or to roles.

For more information, see [ATTACH RLS POLICY](r_ATTACH_RLS_POLICY.md "r_ATTACH_RLS_POLICY.md").

- Use the DETACH RLS POLICY statement to detach a policy from one or more relations, from one
  or more users, or from roles.

For more information, see [DETACH RLS POLICY](r_DETACH_RLS_POLICY.md "r_DETACH_RLS_POLICY.md").

- Use the DROP RLS POLICY statement to drop a policy.

For more information, see [DROP RLS POLICY](r_DROP_RLS_POLICY.md "r_DROP_RLS_POLICY.md").

- Use the GRANT and REVOKE statements to explicitly grant and revoke SELECT permissions to RLS
  policies that reference lookup tables. For more information, see [GRANT](r_GRANT.md "r_GRANT.md") and [REVOKE](r_REVOKE.md "r_REVOKE.md").
  To monitor the policies created, sys:secadmin can view the [SVV_RLS_POLICY](r_SVV_RLS_POLICY.md "r_SVV_RLS_POLICY.md") and [SVV_RLS_ATTACHED_POLICY](r_SVV_RLS_ATTACHED_POLICY.md "r_SVV_RLS_ATTACHED_POLICY.md").

To list RLS-protected relations, sys:secadmin can view [SVV_RLS_RELATION](r_SVV_RLS_RELATION.md "r_SVV_RLS_RELATION.md").

To trace the application of RLS policies on queries that reference RLS-protected
relations, a superuser, sys:operator, or any user with the system permission ACCESS
SYSTEM TABLE can view [SVV_RLS_APPLIED_POLICY](r_SVV_RLS_APPLIED_POLICY.md "r_SVV_RLS_APPLIED_POLICY.md"). Note that sys:secadmin is not granted
these permissions by default.

To allow users full access to an RLS-protected relation, you can grant the IGNORE RLS
permission. Superusers or sys:secadmin are automatically granted IGNORE RLS. For more
information, see [GRANT](r_GRANT.md "r_GRANT.md").

To explain the RLS policy filters of a query in the EXPLAIN plan to troubleshoot
RLS-related queries, you can grant the permission EXPLAIN RLS to any user. For more
information, see [GRANT](r_GRANT.md "r_GRANT.md") and [EXPLAIN](r_EXPLAIN.md "r_EXPLAIN.md").
