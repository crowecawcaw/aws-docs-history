Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Dynamic data masking policy hierarchy

When attaching multiple masking policies, consider the following:

- You can attach multiple masking policies to a single column.
- When multiple masking policies are applicable to a query, the highest priority policy attached to each respective column applies. Consider the following example.

```
ATTACH MASKING POLICY partial_hash
ON credit_cards(address, credit_card)
TO ROLE analytics_role
PRIORITY 20;

ATTACH MASKING POLICY full_hash
ON credit_cards(credit_card, ssn)
TO ROLE auditor_role
PRIORITY 30;

SELECT address, credit_card, ssn
FROM credit_cards;
```

When running the SELECT statement, a user with both the analytics
and auditor roles sees the address column with the `partial_hash` masking policy applied.
They see the credit card and SSN columns with the `full_hash` masking policy applied
because the `full_hash` policy has the higher priority on the credit card column.

- If you don't specify a priority when attaching a masking policy, the default priority is 0.
- You can't attach two policies to the same column with equal priority.
- You can't attach two policies to the same combination of user and column or role and column.
- When multiple masking policies are applicable along the same SUPER path while attached to the same
  user or role, only the highest priority attachment takes effect. Consider the following examples.

The first example shows two masking policies attached on the same path, with the higher priority policy taking effect.

```
ATTACH MASKING POLICY hide_name
ON employees(col_person.name)
TO PUBLIC
PRIORITY 20;

ATTACH MASKING POLICY hide_last_name
ON employees(col_person.name.last)
TO PUBLIC
PRIORITY 30;

--Only the hide_last_name policy takes effect.
SELECT employees.col_person.name FROM employees;
```

The second example shows two masking policies attached to different paths in the same SUPER object,
with no conflict between the policies. Both attachments will apply at the same time.

```
ATTACH MASKING POLICY hide_first_name
ON employees(col_person.name.first)
TO PUBLIC
PRIORITY 20;

ATTACH MASKING POLICY hide_last_name
ON employees(col_person.name.last)
TO PUBLIC
PRIORITY 20;

--Both col_person.name.first and col_person.name.last are masked.
SELECT employees.col_person.name FROM employees;
```

To confirm which masking policy applies to a given user and column or role and column combination, users
with the [`sys:secadmin`](r_roles-default.md "r_roles-default.md") role can look up the column/role or column/user
pair in the [SVV_ATTACHED_MASKING_POLICY](r_SVV_ATTACHED_MASKING_POLICY.md "r_SVV_ATTACHED_MASKING_POLICY.md") system view. For more information,
see [Dynamic data masking system views](r_ddm-svv.md "r_ddm-svv.md").
