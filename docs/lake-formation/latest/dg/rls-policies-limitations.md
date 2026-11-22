

# Row-level security policy limitations

The following limitations apply to row-level security (RLS) policies in AWS Lake Formation. For more information about RLS policies, see [Row-level security policies in AWS Lake Formation](rls-policies.md).

**Filter expression limitations**  
The following limitations apply to RLS policy filter expressions.
+ A filter expression can contain at most four subqueries, including derived tables, and at most 10 distinct reference tables.
+ Reference tables must be in the policy creator's catalog. Each reference table must be a base table registered with Lake Formation. Views and resource links are not supported as reference tables.
+ Aggregate functions other than `MAX` and `MIN` are not supported. Window functions are supported only in a derived table's select list.
+ Every attachment table column referenced in the filter expression must be declared in `AttachmentColumns`.
+ The total length of a filter expression, including comments, can be at most 2048 characters before dynamic attribute substitution.

For the full filter expression syntax and supported operators, see [Filter expression syntax for RLS policies](rls-policies-sql-support.md).

**Attachment validation**  
When you attach RLS policies through Lake Formation tags, validation occurs at query time rather than at attachment time. For a matched table that does not contain a referenced column, the query returns an empty result for that table rather than failing, and no error is raised when the policy is attached.

Column names in RLS filter expressions are late binding: they are resolved against the table's columns at query time, not when you create or attach the policy. If you rename a column that a filter expression references, the policy no longer matches that column, which can cause queries to return an empty result. Review and update affected RLS policies before renaming columns.

**Invalid RLS policies**  

+ Tables included in RLS policy filter expressions are referenced by ID.
+ If a table is deleted, the policy is considered INVALID.
+ INVALID policies are treated as FALSE.

**Re-activating an INVALID RLS policy**  
`UpdateRLSPolicy` fails while a table that the filter expression references doesn't exist. To re-activate the policy, do one of the following:
+ **Restore the referenced table.**

  1. Re-create the deleted table with the same database and table name.

  1. Make sure the re-created table meets the reference table requirements: it's registered with Lake Formation, your IAM permissions allow `glue:GetTable` on it, and you have Lake Formation `SELECT` with grant option on it.

  1. Call `UpdateRLSPolicy` and pass in the same filter expression that you used when you created the policy.
+ **Remove the reference.** Call `UpdateRLSPolicy` with a filter expression that doesn't reference the deleted table.

After `UpdateRLSPolicy` succeeds, the policy's `Status` returns to `VALID` and it filters rows again.

For more information, see [Filter expression syntax for RLS policies](rls-policies-sql-support.md).

**Identity limitations**  
Only IAM principal attributes are supported for attribute-based access control (ABAC). IAM Identity Center attributes are not currently supported.

**Operation limitations**  
RLS policies apply to `SELECT` operations only. They filter the rows a principal can read and do not filter or authorize write operations. Write operations such as `INSERT`, `UPDATE`, and `DELETE` are governed by the principal's separate Lake Formation table permissions and are not restricted by an RLS policy.

**Interaction with data cell filters**  
RLS policies and data cell filters (DCF) can apply to the same table at the same time. When a principal is subject to both a DCF row filter and an RLS policy, Lake Formation combines the two row filters using union (OR) semantics: the principal sees every row that matches either filter. Because the filters are additive, using both together can only expand the rows a principal sees.

To consolidate DCF row filters into RLS policies, create the corresponding RLS policies first, then revoke the existing data cell filter row-level permissions. For a step-by-step migration workflow, see [Best practices for RLS policies](rls-policies-best-practices.md).