Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations when using dynamic data masking

When using dynamic data masking, consider the following:

- When querying objects created from tables, such as views, users will see
  results based on their own masking policies, not the policies of the user who
  created the objects. For example, a user with the analyst role querying a view
  created by a secadmin would see results with masking policies attached to the
  analyst role.
- To prevent the EXPLAIN command from potentially exposing sensitive masking
  policy filters, only users with the SYS_EXPLAIN_DDM permission can see masking
  policies applied in EXPLAIN outputs. Users don't have the SYS_EXPLAIN_DDM
  permission by default.

The following is the syntax for granting the permission to a role.

```
GRANT EXPLAIN MASKING TO ROLE rolename
```

For more information about the EXPLAIN command, see [EXPLAIN](r_EXPLAIN.md "r_EXPLAIN.md").

- Users with different roles can see differing results based on the filter
  conditions or join conditions used. For example, running a SELECT command on a
  table using a specific column value will fail if the user running the command has
  a masking policy applied that obfuscates that column.
- DDM policies must be applied ahead of any predicate operations, or
  projections. Masking polices can include the following:

      + Low cost constant operations such as converting a value to null
      + Moderate cost operations such as HMAC hashing
      + High cost operations such as calls to external Lambda user defined
       functions

  As such, we recommend that you use simple masking expressions when possible.

- You can use DDM policies for roles with row-level security policies, but note
  that RLS policies are applied before DDM. A dynamic data masking expression won't
  be able to read a row that was protected by RLS. For more information about RLS,
  see [Row-level security](t_rls.md "t_rls.md").
- When using the [COPY](r_COPY.md "r_COPY.md") command to copy
  from parquet to protected target tables, you should explicitly specify columns in
  the COPY statement. For more information about mapping columns with COPY, see
  [Column mapping options](copy-parameters-column-mapping.md "copy-parameters-column-mapping.md").
- DDM policies can't attach to the following relations:
  - System tables and catalogs
  - External tables
  - Datasharing tables
  - Cross-DB relations
  - Temporary tables
  - Correlated queries

- DDM policies can contain lookup tables. Lookup tables can be present in the
  USING clause. The following relation types can’t be used as lookup tables:

      + System tables and catalogs
      + External tables
      + Datasharing tables
      + Views, materialized views, and late-binding views
      + Cross-DB relations
      + Temporary tables
      + Correlated queries

  Following is an example of attaching a masking policy to a lookup table.

```
--Create a masking policy referencing a lookup table
CREATE MASKING POLICY lookup_mask_credit_card WITH (credit_card TEXT) USING (
  CASE
    WHEN
      credit_card IN (SELECT credit_card_lookup FROM credit_cards_lookup)
    THEN '000000XXXX0000'
    ELSE REDACT_CREDIT_CARD(credit_card)
    END
  );

--Provides access to the lookup table via a policy attached to a role
GRANT SELECT ON TABLE credit_cards_lookup TO MASKING POLICY lookup_mask_credit_card;
```

- You can't attach a masking policy that would produce an output incompatible
  with the target column's type and size. For example, you can’t attach a masking
  policy that outputs a 12 character long string to a VARCHAR(10) column. Amazon Redshift
  supports the following exceptions:
  - A masking policy with the input type INTN can be attached to a policy
    with size INTM as long as M < N. For example, a BIGINT (INT8) input
    policy can be attached to a smallint (INT4) column.
  - A masking policy with the input type NUMERIC or DECIMAL can always be
    attached to a FLOAT column.

- You can't use DDM policies with data sharing. If the datashare's data producer
  attaches a DDM policy to a table in the datashare, the table becomes inaccessible
  to users from the data consumer who are trying to query the table. Attempting to
  add the relation to a datashare fails on the producer-side cluster or namespace
  with the following error:

```
<`ddm_protected_relation`> or a relation dependent on it is protected by a masking policy and cannot be added to a datashare
```

If you attach a masking policy to a relation on the producer side and the relation is
already included in a datashare, attempting to query the relation on the consumer side fails with
the following error:

```
cross-cluster query of the masked relation <`ddm_protected_relation`> is not supported.
```

You can turn off DDM for datashares using the ALTER TABLE command with the MASKING OFF FOR DATASHARES parameter. For
more information, see [ALTER TABLE](r_ALTER_TABLE.md "r_ALTER_TABLE.md").

- You can't query relations that have attached DDM policies if your values for
  any of the following configuration options don't match the default value of the
  session:

      + `enable_case_sensitive_super_attribute`
      + `enable_case_sensitive_identifier`
      + `downcase_delimited_identifier`

  Consider resetting your session’s configuration options if you attempt to query
  a relation with a DDM policy attached and see the message "DDM protected relation
  does not support session level config on case sensitivity being different from its
  default value."

- When your provisioned cluster or serverless namespace has any dynamic data
  masking policies, the following commands are blocked for regular users:

```
ALTER <current_user> SET enable_case_sensitive_super_attribute/enable_case_sensitive_identifier/downcase_delimited_identifier
```

When you create DDM policies, we recommend that you change the default
configuration option settings for regular users to match the session’s
configuration option settings at the time the policy was created. Superusers and
users with the ALTER USER privilege can do this by using parameter group settings
or the ALTER USER command. For information about parameter groups, see [Amazon Redshift parameter
groups](../mgmt/working-with-parameter-groups.md "../mgmt/working-with-parameter-groups.md") in the _Amazon Redshift Management Guide_. For information
about the ALTER USER command, see [ALTER USER](r_ALTER_USER.md "r_ALTER_USER.md").

- Views and late-binding views with attached DDM policies can't be replaced by regular users
  using the [CREATE VIEW](r_CREATE_VIEW.md "r_CREATE_VIEW.md") command.
  To replace views or LBVs with DDM policies, first detach any DDM policies attached
  to them, replace the views or LBVs, and reattach the policies. Superusers and users
  with the `sys:secadmin` permission can use CREATE VIEW on views or
  LBVs with DDM policies without detaching the policies.
- Views with attached DDM policies can't reference system tables and views. Late-binding
  views can reference system tables and views.
- Late-binding views with attached DDM policies can't reference nested data in data
  lakes, such as JSON documents.
- Late-binding views can't have DDM policies attached if that late-binding view
  is referenced by any view.
- DDM policies attached to late-binding views are attached by column name. At
  query time, Amazon Redshift validates that all masking policies attached to the
  late-binding view have been applied successfully, and that the late-binding view's
  output column type matches the types in the attached masking policies. If the
  validation fails, Amazon Redshift returns an error for the query.
- You can use customized session context variables when creating DDM policies.
  The following example sets session context variables for a DDM policy.

```
-- Set a customized context variable.
SELECT set_config('app.city', 'XXXX', FALSE);

-- Create a MASKING policy using current_setting() to get the value of a customized context variable.
CREATE MASKING POLICY city_mask
WITH (city VARCHAR(30))
USING (current_setting('app.city')::VARCHAR(30));

-- Attach the policy on the target table to one or more roles.
ATTACH MASKING POLICY city_mask
ON tickit_users_redshift(city)
TO ROLE analyst, ROLE dbadmin;
```

For details on how to set and retrieve customized session
context variables, go to [SET](r_SET.md "r_SET.md"),
[SET_CONFIG](r_SET_CONFIG.md "r_SET_CONFIG.md"),
[SHOW](r_SHOW.md "r_SHOW.md"),
[CURRENT_SETTING](r_CURRENT_SETTING.md "r_CURRENT_SETTING.md"), and
[RESET](r_RESET.md "r_RESET.md").
For more information on modifying the server configuration in general, go to
[Modifying the server
configuration](cm_chap_ConfigurationRef.md#t_Modifying_the_default_settings "cm_chap_ConfigurationRef.md#t_Modifying_the_default_settings").

###### Important

When using session context variables within DDM policies,
the security policy is reliant on the user or role that
invokes the policy. Be careful to avoid security vulnerabilities
when using session context variables in DDM policies.
