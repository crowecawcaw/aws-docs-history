

# Best practices for RLS policies
<a name="rls-policies-best-practices"></a>

This section provides best practices for implementing and managing row-level security (RLS) policies in Lake Formation, including guidance for customers migrating from data cell filters (DCF) to RLS policies.

**Design best practices**  


**Use tag-based attachment for scale**  
When attaching the same policy across many tables, attach RLS policies using Lake Formation tags rather than naming each table individually. Tag-based attachment offers the following advantages:
+ New tables that are tagged inherit the policy automatically.
+ You manage one attachment instead of hundreds of individual table attachments.
+ You can combine tag-based RLS attachment with tag-based permission grants (LF-TBAC) for a tag-driven governance model.

When using tag-based attachment, ensure that all tables with the specified tags contain the columns referenced in the filter expression. Lake Formation validates columns at query time (not at attach time) for tag-based attachments. For a matched table that is missing a referenced column, the query returns an empty result for that table rather than failing.

**Warning**  
Tag-based attachment carries the same risk as deleting a policy. If the LF-Tag that drives the attachment is removed from a table, or the table no longer matches the tag expression, the RLS policy stops applying to that table and principals with `SELECT` see all rows, with no row-level filtering. Treat changes to the tags that drive RLS attachments as access-control changes, and keep a default no-rows policy in place so that losing a tag-based attachment does not expose all rows. For how to attach by tags, see [Attaching and detaching RLS policies](rls-policies-granting.md).

**Group tables by shared columns for tagging**  
Tag-based RLS attachment works best when tables share the same columns that you want to filter on. Design your tagging strategy around column commonality:
+ Tag tables that share a `region` column with a common tag (for example, `data-scope=regional`).
+ If some tables have a `region` column and others do not, do not apply a `region`-based RLS policy to a tag shared by both groups.
+ You may need to use table-level tags rather than database-level tag inheritance to avoid applying RLS to tables that lack the filter columns.

**Use default RLS policies for baseline security (Highly recommended)**  
This is the most important best practice we recommend. For tables containing sensitive data, set a default RLS policy that restricts all principals to a subset by default:

1. Create a policy (for example, `contains_pii = false`).

1. Attach it to the table with `SetDefault: true`.

1. Grant additional policies to principals who need broader access.

This ensures that new principals, both current and future, are automatically restricted to non-sensitive data without requiring policy attachment.

**Combine RLS with column-level permissions for cell-level security**  
For additional data protection, add RLS policies along with column-level permissions:
+ Use RLS policies to filter rows (for example, `region = 'US-WEST'`).
+ Use column-level grants (via LF-TBAC or named grants) to restrict which columns a principal can see.
+ The result is security applied at both the column and the row level. The principal sees only the intersection of allowed rows and allowed columns.

**Plan for the additive (OR) permissions model**  
When a principal is attached to multiple RLS policies on the same table, they see the union of all matching rows. Plan your policies accordingly:
+ If you want a principal to see only rows matching ALL conditions, use a single policy with an `AND` filter expression (for example, `region = 'US-WEST' AND department = 'engineering'`).
+ If you want a principal to see rows matching ANY condition, attach separate policies for the union behavior.

**Use ABAC for dynamic principal management**  
Instead of attaching each IAM role individually, use IAM principal attributes (ABAC) with the `Condition` field on `AttachRLSPolicy`. This allows an RLS policy to be applied to principals based on session tags such as department, cost center, or job role without listing each principal individually.

**Note**  
Only IAM principal attributes are supported for ABAC. IAM Identity Center attributes are not currently supported.

**Migrating from data cell filters to RLS policies**  


As a best practice, we recommend using RLS policies instead of data cell filters (DCF) for row-level security.

If you currently use data cell filters (DCF) for row-level filtering, you can migrate to RLS policies for improved scalability, centralized management, and stronger enforcement. This section explains how to achieve equivalent functionality with RLS.

**Key differences between DCF and RLS**  
The following table compares data cell filters (DCF) and RLS policies across several dimensions.


| Feature | Data cell filters | RLS policies | 
| --- | --- | --- | 
| Scope | One filter per table | One policy can apply to thousands of tables | 
| Attachment method | Named table only | Named table or Lake Formation tags | 
| Row filtering behavior | TBAC grants can provide full table access, with DCF row filters restricting access because of the union of grants | TBAC grants can provide SELECT on the full table; RLS restricts access to the rows a principal is allowed to see | 
| Column filtering | Supported directly as part of DCFs | Supported through direct column-level permissions | 
| Updating filter criteria | Must update each data cell filter individually | Update the RLS policy once and it propagates to all attached tables | 
| Dynamic application | Manual per table | Automatic via tags (new tables inherit policies) | 

**Migration workflow**  
Use the following workflow to migrate from DCF row filtering to RLS policies without disrupting existing access.

1. **Identify existing DCF row filters.** List your existing data cell filters that include row filter expressions. Note the `RowFilter.FilterExpression` value for each filter.

   ```
   aws lakeformation list-data-cells-filter \
     --table '{"CatalogId":"111122223333","DatabaseName":"mydb","Name":"mytable"}'
   ```

1. **Create equivalent RLS policies.** For each distinct filter expression, create an RLS policy. If you had 50 DCFs with the same filter logic applied to 50 tables, you now need only one RLS policy.

   ```
   aws lakeformation create-rls-policy \
     --name "restrict-to-us-west" \
     --filter-expression "region = 'US-WEST'" \
     --attachment-columns '[{"Name": "region", "Type": "string"}]'
   ```

1. **Attach the RLS policy to tables.** Attach the policy to individual tables or, for scale, to Lake Formation tags.

   ```
   aws lakeformation attach-rls-policy \
     --name "restrict-to-us-west" \
     --resource '{"LFTagPolicy": {"ResourceType": "TABLE", "Expression": [{"TagKey": "department", "TagValues": ["hr"]}]}}' \
     --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/DataAnalyst"}'
   ```

1. **Grant the RLS policy to principals.** Attach the same principals that had the DCF row filter to the new RLS policy on the table.

   ```
   aws lakeformation attach-rls-policy \
     --name "restrict-to-us-west" \
     --resource '{"Table": {"DatabaseName": "mydb", "Name": "mytable"}}' \
     --principal '{"DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/DataAnalyst"}'
   ```

1. **Remove the DCF row filter.** After verifying that the RLS policy is enforced correctly, revoke the DCF grant that included the row filter. Then re-grant `SELECT` without the DCF.

   ```
   aws lakeformation revoke-permissions \
     --principal '{"DataLakePrincipalIdentifier":"arn:aws:iam::111122223333:role/DataAnalyst"}' \
     --resource '{"Table":{"CatalogId":"111122223333","DatabaseName":"mydb","Name":"mytable"}}' \
     --permissions SELECT
   ```

**Important**  
If both a DCF row filter and an RLS policy apply to the same table for a principal, Lake Formation returns the union (OR) of the rows matched by each filter. During migration this means a principal can see rows from both sources until you remove the DCF row filter. Complete the migration by removing the DCF row filter so that only the RLS policy governs row access.

**Handling column filtering during migration**  
RLS policies do not support column filtering as part of the filter criteria. If your DCF included both row filtering and column filtering:

1. Use RLS policies for the row filtering portion.

1. Use column-level permissions (via LF-TBAC or named grants) for the column filtering portion.

Combining RLS row filtering with column-level permissions provides cell-level protection equivalent to what a DCF provides, while scaling to many tables through a single reusable policy.

**DCF-to-RLS equivalence examples**  


**Example 1: Simple row filter**  
DCF:  

```
{
  "Name": "us-only",
  "DatabaseName": "sales",
  "TableName": "orders",
  "TableCatalogId": "111122223333",
  "RowFilter": {"FilterExpression": "region='US'"},
  "ColumnWildcard": {}
}
```
RLS equivalent:  

```
aws lakeformation create-rls-policy \
  --name "us-only" \
  --filter-expression "region = 'US'" \
  --attachment-columns '[{"Name": "region", "Type": "string"}]'
```

**Example 2: Cell-level filter (row \+ column)**  
DCF:  

```
{
  "Name": "us-no-pii",
  "DatabaseName": "sales",
  "TableName": "orders",
  "TableCatalogId": "111122223333",
  "RowFilter": {"FilterExpression": "region='US'"},
  "ColumnWildcard": {"ExcludedColumnNames": ["customer_ssn", "customer_email"]}
}
```
RLS with column permissions equivalent:  

1. Create an RLS policy with `FilterExpression: "region = 'US'"`.

1. Grant `SELECT` on the table excluding `customer_ssn` and `customer_email` columns (via column-level permissions).

1. Attach the RLS policy to the principal on the table.

**Example 3: Scaling from 50 DCFs to 1 RLS policy**  
Before (DCF): 50 tables, each with an identical filter `department = 'finance'`, requiring 50 separate DCF definitions.  
After (RLS):  

1. Create one policy: `FilterExpression: "department = 'finance'"`.

1. Tag all 50 tables with `access-scope=finance`.

1. Attach the policy via tags.

1. Grant the policy to the finance analyst role.
New tables tagged with `access-scope=finance` automatically inherit the policy.

**Operational best practices**  


**Monitor with CloudTrail**  
All RLS policy operations are logged in CloudTrail: policy creation, updates, and deletions; policy attachments and detachments; and policy evaluations during query execution. Use CloudTrail events to audit who changed policies and when.

**Adopt RLS incrementally**  
RLS policies are additive. Attaching a principal to a policy restricts only that principal. Other users of the table are unaffected. This lets you adopt row-level security incrementally:

1. Start with a small set of principals.

1. Verify correct enforcement via test queries.

1. Expand to additional principals.

**Validate tag-based attachments**  
When attaching policies via tags, verify that the target tables contain the expected columns:
+ There is no console view showing which tagged tables received an RLS policy.
+ Use `ListRLSPolicyAttachments` with a `Resource` filter to verify attachments.
+ Test queries as an attached principal to confirm enforcement.

**Use descriptive policy names**  
Policy names are case-insensitive and must be unique within a catalog. Use descriptive names that indicate the filtering logic, such as `restrict-to-us-west` or `finance-department-only`, rather than unclear names such as `policy-1`.