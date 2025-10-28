Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Dynamic data masking system views

Superusers, users with the `sys:operator` role,
and users with the ACCESS SYSTEM TABLE permission can
access the following DDM-related system views.

- [SVV_MASKING_POLICY](r_SVV_MASKING_POLICY.md "r_SVV_MASKING_POLICY.md")

Use SVV_MASKING_POLICY to view all masking policies created on the cluster or workgroup.

- [SVV_ATTACHED_MASKING_POLICY](r_SVV_ATTACHED_MASKING_POLICY.md "r_SVV_ATTACHED_MASKING_POLICY.md")

Use SVV_ATTACHED_MASKING_POLICY to view all the relations and users or roles with policies attached on the currently connected database.

- [SYS_APPLIED_MASKING_POLICY_LOG](SYS_APPLIED_MASKING_POLICY_LOG.md "SYS_APPLIED_MASKING_POLICY_LOG.md")

Use SYS_APPLIED_MASKING_POLICY_LOG to trace the
application of masking policies on queries
that reference DDM-protected relations.
Following are some examples of the information that
you can find using system views.

```
--Select all policies associated with specific users, as opposed to roles
SELECT policy_name,
       schema_name,
       table_name,
       grantee
FROM svv_attached_masking_policy
WHERE grantee_type = 'user';

--Select all policies attached to a specific user
SELECT policy_name,
       schema_name,
       table_name,
       grantee
FROM svv_attached_masking_policy
WHERE grantee = '`target_grantee_name`'

--Select all policies attached to a given table
SELECT policy_name,
       schema_name,
       table_name,
       grantee
FROM svv_attached_masking_policy
WHERE table_name = '`target_table_name`'
      AND schema_name = '`target_schema_name`';

--Select the highest priority policy attachment for a given role
SELECT samp.policy_name,
       samp.priority,
       samp.grantee,
       smp.policy_expression
FROM svv_masking_policy AS smp
JOIN svv_attached_masking_policy AS samp
    ON samp.policy_name = smp.policy_name
WHERE
    samp.grantee_type = 'role' AND
    samp.policy_name = mask_get_policy_for_role_on_column(
        '`target_schema_name`',
        '`target_table_name`',
        '`target_column_name`',
        '`target_role_name`')
ORDER BY samp.priority desc
LIMIT 1;

--See which policy a specific user will see on a specific column in a given relation
SELECT samp.policy_name,
       samp.priority,
       samp.grantee,
       smp.policy_expression
FROM svv_masking_policy AS smp
JOIN svv_attached_masking_policy AS samp
    ON samp.policy_name = smp.policy_name
WHERE
    samp.grantee_type = 'role' AND
    samp.policy_name = mask_get_policy_for_user_on_column(
        '`target_schema_name`',
        '`target_table_name`',
        '`target_column_name`',
        '`target_user_name`')
ORDER BY samp.priority desc;

 --Select all policies attached to a given relation.
SELECT policy_name,
schema_name,
relation_name,
database_name
FROM sys_applied_masking_policy_log
WHERE relation_name = 'relation_name'
AND schema_name = 'schema_name';
```
