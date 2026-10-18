

# Row-level security policy limitations
<a name="rls-policies-limitations"></a>

The following limitations apply to row-level security (RLS) policies in AWS Lake Formation. For more information about RLS policies, see [Row-level security policies in AWS Lake Formation](rls-policies.md).

**Filter expression limitations**  
The following limitations apply to RLS policy filter expressions.
+ Subqueries, joins, and references to external tables are not supported. All filtering logic must use columns within the target table.
+ User-defined functions (UDFs) are not supported.
+ Only static filter expressions are supported. Dynamic filters that reference user attributes (for example, `table.region = user.region`) are not supported. Create a separate policy for each distinct filter value.
+ Column-to-column comparisons are not supported (for example, `column_a = column_b`). Compare columns to constant values instead.
+ Aggregate functions (such as `SUM`, `COUNT`, `AVG`) and window functions are not supported.
+ Every column referenced in the filter expression must be declared in `AttachmentColumns`.
+ The total length of a filter expression must be less than 2048 characters.
+ `IS [NOT] NULL` on partition columns is not supported.

For the full filter expression syntax and supported operators, see [Filter expression syntax for RLS policies](rls-policies-sql-support.md).

**Attachment validation**  
When you attach RLS policies through Lake Formation tags, validation occurs at query time rather than at attachment time. For a matched table that does not contain a referenced column, the query returns an empty result for that table rather than failing, and no error is raised when the policy is attached.

Column names in RLS filter expressions are late binding: they are resolved against the table's columns at query time, not when you create or attach the policy. If you rename a column that a filter expression references, the policy no longer matches that column, which can cause queries to return an empty result. Review and update affected RLS policies before renaming columns.

**Identity limitations**  
Only IAM principal attributes are supported for attribute-based access control (ABAC). IAM Identity Center attributes are not currently supported.

**Operation limitations**  
RLS policies apply to `SELECT` operations only. They filter the rows a principal can read and do not filter or authorize write operations. Write operations such as `INSERT`, `UPDATE`, and `DELETE` are governed by the principal's separate Lake Formation table permissions and are not restricted by an RLS policy.

**Interaction with data cell filters**  
RLS policies and data cell filters (DCF) can apply to the same table at the same time. When a principal is subject to both a DCF row filter and an RLS policy, Lake Formation combines the two row filters using union (OR) semantics: the principal sees every row that matches either filter. Because the filters are additive, using both together can only expand the rows a principal sees.

To consolidate DCF row filters into RLS policies, create the corresponding RLS policies first, then revoke the existing data cell filter row-level permissions. For a step-by-step migration workflow, see [Best practices for RLS policies](rls-policies-best-practices.md).