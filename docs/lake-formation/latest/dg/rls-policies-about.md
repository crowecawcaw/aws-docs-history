

# How RLS policies work in detail
<a name="rls-policies-about"></a>

This section covers how row-level security (RLS) policies are structured, enforced, and used in practice, including a worked end-to-end example.

**Policy components**  


An RLS policy consists of the following fields.


| Field | Type | Description | 
| --- | --- | --- | 
| Name | String | A unique, case-insensitive identifier for the policy within a catalog. Maximum 255 characters. | 
| FilterExpression | String | A PartiQL-subset expression that defines the row filter condition. Maximum 2048 characters. | 
| AttachmentColumns | List | The columns referenced in the filter expression. Each entry contains a Name (string) and a Type (string). | 

**AttachmentColumns structure**  
Each entry in the AttachmentColumns list identifies a column by name and data type.

```
{
  "AttachmentColumns": [
    {
      "Name": "department",
      "Type": "string"
    },
    {
      "Name": "region_code",
      "Type": "int"
    }
  ]
}
```

Column names are case-insensitive, but type strings are case-sensitive and must be lowercase (`string`, `int`, `bigint`, `double`, `decimal`, `boolean`). Uppercase values such as `STRING` are rejected.

Lake Formation does not validate the type against the target table when you create or update a policy, because no table is involved at that point. For name-based table attachments, it is validated when you attach the policy. The attachment columns **must** match the table's columns by name (case-insensitive) and by equivalent type. If they do not match, the attach fails. For all-tables and tag-based attachments, the validation happens at query time.

Every column referenced in the filter expression must also appear in AttachmentColumns. Referencing a column that is not declared causes the create to fail.

**Enforcement**  


**Additive (union) semantics**  
When multiple RLS policies are attached to the same table for the same principal, Lake Formation combines them using union logic. The principal sees all rows that satisfy any of the attached policies.

**Example Additive policies**  
A principal has two policies attached:  
+ Policy A: `department = 'Engineering'`
+ Policy B: `department = 'Sales'`
The principal sees all rows where department is either Engineering or Sales.

**SELECT-based enforcement**  
An RLS policy scopes down a principal's `SELECT` permission only. It scopes down the rows a principal can read. It does not add or remove any other permission, and it does not affect principals whose access comes from a broader grant.

How RLS interacts with a principal's existing permissions on the table:
+ **SELECT permission, no RLS policy attached** – The principal sees all rows, limited to the columns their Lake Formation `SELECT` permission grants.
+ **SELECT permission, RLS policy attached** – The principal sees all columns they are granted, with rows restricted to those matching the filter.
+ **ALL or SUPER\_USER permission** – The principal sees the full table. RLS scopes down `SELECT`, so a broader `ALL` or `SUPER_USER` grant is not affected by an RLS attachment.
+ **No permission on the table** – The principal has no access. An RLS attachment alone does not grant `SELECT`.

To let a principal see all rows on a table that has RLS in effect, either grant `ALL` on the table or attach an RLS policy whose filter matches every row.

**Default policy (Highly recommended)**  
A default RLS policy applies to every principal accessing the table. It serves as a baseline filter. If a principal also has an explicit policy attachment, the default policy is combined with the explicit policy using additive (union) semantics.

**Example Default policy combined with an explicit policy**  
A table has:  
+ Default policy: `status = 'active'`
+ Explicit policy for user A: `department = 'Engineering'`
User A sees rows where `status = 'active'` OR `department = 'Engineering'`. A user with no explicit attachment sees only rows where `status = 'active'`.

**Policy lifecycle**  


The typical lifecycle of an RLS policy follows these stages.

**1. Create**  
Define the policy with a name, filter expression, and attachment columns using the `CreateRLSPolicy` API or the Lake Formation console.

**2. Attach**  
Attach the policy to one or more tables for specific principals using `AttachRLSPolicy`. You can attach using name-based attachment or tag-based attachment.

**3. Enforce**  
Once attached, the policy is immediately enforced. Any query from the specified principal against the table has the filter applied transparently.

**4. Update**  
Modify the filter expression using `UpdateRLSPolicy`. Changes take effect immediately on all existing attachments. Note that attachment columns cannot be changed after creation. To change columns, delete and recreate the policy and perform the attachment again.

**5. Delete**  
Remove the policy using `DeleteRLSPolicy`. Deletion immediately removes the policy and all its attachments. If a principal has other policies (or a default policy) still attached to the table, they see the union of the remaining policies' rows. If no policies and no default remain, RLS stops filtering and the principal sees all rows their `SELECT` permission allows.

**Worked example**  


The following example demonstrates the complete lifecycle of an RLS policy that restricts access to rows in a `transactions` table based on region.

**Step 1: Create the policy**  


```
{
  "Name": "us-east-transactions-only",
  "FilterExpression": "region = 'us-east-1'",
  "AttachmentColumns": [
    {
      "Name": "region",
      "Type": "string"
    }
  ]
}
```

**Step 2: Attach to a table for a principal**  


```
{
  "Name": "us-east-transactions-only",
  "Resource": {
    "Table": {
      "DatabaseName": "finance_db",
      "Name": "transactions"
    }
  },
  "Principal": {
    "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/AnalystRole"
  }
}
```

**Step 3: Grant SELECT for the principal**  


```
{
  "Principal": {
    "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/AnalystRole"
  },
  "Resource": {
    "Table": {
      "DatabaseName": "finance_db",
      "Name": "transactions"
    }
  },
  "Permissions": [
    "SELECT"
  ]
}
```

**Step 4: Query results**  
When the `AnalystRole` queries the `transactions` table:

```
SELECT * FROM finance_db.transactions;
```

Lake Formation appends the filter condition automatically. The role only sees rows where `region = 'us-east-1'`.

**Step 5: Update the filter**  
To expand access to include a second region:

```
{
  "Name": "us-east-transactions-only",
  "FilterExpression": "region IN ('us-east-1', 'us-west-2')"
}
```

The change takes effect immediately on all existing attachments.

**Step 6: Delete the policy**  


```
{
  "Name": "us-east-transactions-only"
}
```

After deletion, no RLS policy filters the `AnalystRole` on this table, so it sees all rows its `SELECT` permission allows (not only `us-east-1`).