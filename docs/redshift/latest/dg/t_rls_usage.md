Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations and limitations using RLS policies

## Considerations

Following are considerations for working with RLS policies:

- Amazon Redshift applies RLS policies to SELECT, UPDATE, or DELETE statements.
- Amazon Redshift doesn't apply RLS policies to INSERT, COPY, ALTER TABLE APPEND statements.
- RLS policies can be attached to tables, views, late binding views (LBVs),
  and materialized views (MVs).
- Row-level security works with column-level security to protect your data.
- When RLS is turned on for the source relation, Amazon Redshift supports the ALTER TABLE APPEND
  statement for superusers, users that have been explicitly granted the system
  permission IGNORE RLS, or the sys:secadmin role. In this case, you can run the ALTER TABLE
  APPEND statement to append rows to a target table by moving data from an existing
  source table. Amazon Redshift moves all tuples from the source relation into the target
  relation. The RLS status of the target relation doesn't affect the ALTER TABLE
  APPEND statement.
- To facilitate migration from other data warehouse systems,
  you can set and retrieve customized session context variables
  for a connection by specifying the variable name and value.

The following example sets session context variables for a
row-level security (RLS) policy.

```
-- Set a customized context variable.
SELECT set_config(‘app.category’, ‘Concerts’, FALSE);

-- Create a RLS policy using current_setting() to get the value of a customized context variable.
CREATE RLS POLICY policy_categories
WITH (catgroup VARCHAR(10))
USING (catgroup = current_setting('app.category', FALSE));

-- Set correct roles and attach the policy on the target table to one or more roles.
ATTACH RLS POLICY policy_categories ON tickit_category_redshift TO ROLE analyst, ROLE dbadmin;
```

For details on how to set and retrieve customized session context variables, go to
[SET](r_SET.md "r_SET.md"),
[SET_CONFIG](r_SET_CONFIG.md "r_SET_CONFIG.md"),
[SHOW](r_SHOW.md "r_SHOW.md"),
[CURRENT_SETTING](r_CURRENT_SETTING.md "r_CURRENT_SETTING.md"), and
[RESET](r_RESET.md "r_RESET.md").
For more information on modifying the server configuration in general, go to
[Modifying the server
configuration](cm_chap_ConfigurationRef.md#t_Modifying_the_default_settings "cm_chap_ConfigurationRef.md#t_Modifying_the_default_settings").

###### Important

When using session context variables within RLS policies,
the security policy is reliant on the user or role that
invokes the policy. Be careful to avoid security vulnerabilities
when using session context variables in RLS policies.

- Changing session user using SET SESSION AUTHORIZATION between DECLARE and FETCH or between subsequent FETCH statements won't refresh the already prepared plan based on the user policies at DECLARE time. Avoid changing session user when cursors are used with RLS-protected tables.
- When the base objects inside a view object are RLS-protected, policies attached to the user
  running the query are applied on the respective base objects. This is different
  from object-level permission checks,
  where the view owner's permissions are checked against the view base objects.
  You can view the RLS-protected relations of a
  query in its EXPLAIN plan output.
- When a user-defined function (UDF) is referenced in a RLS policy of a relation attached to a user, the user must have the EXECUTE permission over the UDF to query the relation.
- Row-level security might limit query optimization. We recommend carefully evaluating query performance before
  deploying RLS-protected views on large datasets.
- Row-level security policies applied to late-binding views might be pushed into federated tables. These RLS policies might be visible in external processing engine logs.

## Limitations

Following are the limitations when working with RLS policies:

- RLS policies can't be attached to external tables and several other relation types. For more
  information, see [ATTACH RLS POLICY](r_ATTACH_RLS_POLICY.md "r_ATTACH_RLS_POLICY.md").
- Amazon Redshift supports SELECT statements for certain RLS policies with lookups
  that have complex joins, but doesn't support UPDATE or DELETE statements.
  In cases with UPDATE or DELETE statements, Amazon Redshift returns the following
  error:

```
ERROR: One of the RLS policies on target relation is not supported in UPDATE/DELETE.
```

- Whenever a user-defined function (UDF) is referenced in a RLS policy of a
  relation attached to a user, the user must have the EXECUTE permission over the
  UDF to query the relation.
- Correlated subqueries aren't supported. Amazon Redshift returns the following error:

```
ERROR: RLS policy could not be rewritten.
```

- Amazon Redshift doesn't support datasharing with RLS. If a relation doesn't have RLS turned off for
  datashares, the query fails on the consumer cluster with the following
  error:

```
RLS-protected relation "rls_protected_table" cannot be accessed via datasharing query.
```

You can turn off RLS for datashares using the ALTER TABLE command with the parameter ROW LEVEL SECURITY OFF FOR DATASHARES. For more information
about using ALTER TABLE to enable or disable RLS, go to [ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md").

- In cross-database queries, Amazon Redshift blocks reads to RLS-protected relations. Users with the IGNORE RLS permission can access the protected relation using cross-database queries. When a user without the IGNORE RLS permission accesses RLS-protected relation through a cross-database query, the following error appears:

```
RLS-protected relation "rls_protected_table" cannot be accessed via cross-database query.
```

- ALTER RLS POLICY only supports modifying a RLS policy using the USING ( using_predicate_exp )
  clause. You can't modify a RLS policy with a WITH clause when running
  ALTER RLS POLICY.
- You can't query relations that have row-level security turned on
  if the values for any of the following configuration options don't
  match the default value of the session:

      + `enable_case_sensitive_super_attribute`
      + `enable_case_sensitive_identifier`
      + `downcase_delimited_identifier`

  Consider resetting your session’s configuration options if you attempt to query a relation with row-level security on
  and see the message "RLS protected relation does not support session level config on case sensitivity being different from its default value."

- When your provisioned cluster or serverless namespace has any row-level security policies,
  the following commands are blocked for regular users:

```
ALTER <current_user> SET enable_case_sensitive_super_attribute/enable_case_sensitive_identifier/downcase_delimited_identifier
```

When you create RLS policies, we recommend that you change the default
configuration option settings for regular users to match the session’s
configuration option settings at the time the policy was created. Superusers
and users with the ALTER USER privilege can do this by using parameter group
settings or the ALTER USER command. For information about parameter groups, see
[Amazon Redshift
parameter groups](../mgmt/working-with-parameter-groups.md "../mgmt/working-with-parameter-groups.md") in the _Amazon Redshift Management Guide_. For
information about the ALTER USER command, see [ALTER USER](r_ALTER_USER.md "r_ALTER_USER.md").

- Views and late-binding views with row-level security policies can't be replaced by regular
  users using the [CREATE VIEW](r_CREATE_VIEW.md "r_CREATE_VIEW.md") command.
  To replace views or LBVs with RLS policies, first detach any RLS policies attached to them,
  replace the views or LBVs, and reattach the policies. Superusers and users with the
  `sys:secadmin permission` can use CREATE VIEW on views or LBVs with
  RLS policies without detaching the policies.
- Views with row-level security policies can't reference system tables and system views.
- A late-binding view that's referenced by a regular view can't be RLS protected.
- RLS-protected relations and nested data from data lakes can't be accessed in the same query.
