Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SQL commands for managing dynamic

data masking policies

You can perform the following actions to create, attach, detach, and delete dynamic data masking policies:

- To create a DDM policy, use the [CREATE MASKING POLICY](r_CREATE_MASKING_POLICY.md "r_CREATE_MASKING_POLICY.md") command.

The following is an example of creating a masking policy using a SHA-2 hash function.

```
CREATE MASKING POLICY hash_credit
WITH (credit_card varchar(256))
USING (sha2(credit_card + 'testSalt', 256));
```

- To alter an existing DDM policy, use the [ALTER MASKING POLICY](r_ALTER_MASKING_POLICY.md "r_ALTER_MASKING_POLICY.md") command.

The following is an example of altering an existing masking policy.

```
ALTER MASKING POLICY hash_credit
USING (sha2(credit_card + 'otherTestSalt', 256));
```

- To attach a DDM policy on a table to one or more users or roles, use the [ATTACH MASKING POLICY](r_ATTACH_MASKING_POLICY.md "r_ATTACH_MASKING_POLICY.md") command.

The following is an example of attaching a masking policy to a column/role pair.

```
 ATTACH MASKING POLICY hash_credit
ON credit_cards (credit_card)
TO ROLE science_role
PRIORITY 30;
```

The PRIORITY clause determines which masking policy applies to a user
session when multiple policies are attached to the same column. For example, if
the user in the preceding example has another masking policy attached to the same credit card column with a
priority of 20, science_role's policy is the one that applies, as it
has the higher priority of 30.

- To detach a DDM policy on a table from one or more users or roles, use the [DETACH MASKING POLICY](r_DETACH_MASKING_POLICY.md "r_DETACH_MASKING_POLICY.md") command.

The following is an example of detaching a masking policy from a column/role pair.

```
DETACH MASKING POLICY hash_credit
ON credit_cards(credit_card)
FROM ROLE science_role;
```

- To drop a DDM policy from all databases, use the [DROP MASKING POLICY](r_DROP_MASKING_POLICY.md "r_DROP_MASKING_POLICY.md") command.

The following is an example of dropping a masking policy from all databases.

```
DROP MASKING POLICY hash_credit;
```
