

# Row-level security policies in AWS Lake Formation
<a name="rls-policies"></a>

Row-level security (RLS) policies in AWS Lake Formation let you grant access to specific rows in a table based on filter expressions. When a principal queries a table with an attached RLS policy, Lake Formation automatically applies the filter so that only matching rows are returned.

**How RLS policies work**  


An RLS policy consists of a named filter expression and a set of columns the predicate applies to. You create a policy once, then attach it to one or more tables for specific principals. When a principal queries a table with an RLS policy attachment, Lake Formation evaluates the policy and returns only the rows the principal is allowed to see.

RLS policies are **additive**. If multiple policies are attached to a table for a principal, the principal sees the union of all matching rows. This means attaching additional policies only expands access, never restricts it.

With RLS policies in Lake Formation, you can implement fine-grained row-level data security that scales across thousands of tables.

**Key concepts**  


**Policy components**  
Each RLS policy has the following components:
+ **Name** – A unique identifier for the policy within your catalog. Names are case-insensitive.
+ **FilterExpression** – A [PartiQL-subset expression](https://docs.aws.amazon.com/lake-formation/latest/dg/partiql-support.html) that defines which rows are visible. For example: `department = 'Engineering'`. For the supported syntax, operators, and data types, see [Filter expression syntax for RLS policies](rls-policies-sql-support.md).
+ **AttachmentColumns** – The columns referenced in the filter expression, each with a name and data type.

**Attachment methods**  
You can attach RLS policies to tables in two ways:
+ **Direct attachment** – Attach the policy to a specific table for a specific principal.
+ **Tag-based attachment** – Attach the policy to an LF-Tag. Any table matching the tag expression inherits the policy.

**Prerequisite: SELECT permission**  
RLS policies filter rows, but they do not grant `SELECT` permission on the table. Principals must already have `SELECT` permission (granted through Lake Formation permissions, Lake Formation tag-based access control (LF-TBAC), attribute-based access control (ABAC), or data cell filters), which can be granted by a data lake administrator.

**Default policy**  
A default RLS policy applies to every principal with `SELECT` access on the table. If a principal also has an explicit policy attached, they see the union of the default policy's rows and their explicit policy's rows. Set a default policy by specifying `SetDefault: true` when attaching the policy. As a best practice, set a default policy before you grant any permissions.

**RLS policies compared to data cell filters**  


Data cell filters (DCF) also provide row-level filtering. The following table compares the two approaches.


| Feature | Data cell filters | RLS policies | 
| --- | --- | --- | 
| Reusability | Bound to a single table | Attach one policy to many tables | 
| Column filtering | Supported (include/exclude columns) | Not supported (use column-level permissions instead) | 
| Tag-based attachment | Not supported | Supported via LF-Tag policy resources | 
| Default policy | Not supported | Supported (applies to all principals without explicit attachment) | 
| ABAC conditions | Supported | Supported | 
| Update propagation | Must update each filter individually per table | Update once, change propagates to all attached tables | 

**Important**  
DCF provides column filtering and per-table row filtering with a simpler setup. RLS policies provide scalable, reusable row filtering across many tables with stronger enforcement against `SELECT` statements. Evaluate your requirements before choosing one or both. For a detailed comparison and migration guidance, see [Best practices for RLS policies](rls-policies-best-practices.md).

**Integration with other Lake Formation features**  


**Column-level security**  
RLS policies work alongside column-level permissions. If a principal has access to only certain columns and also has an RLS policy attached, both restrictions apply. The principal sees only the permitted columns for the rows matching the filter.

**Lake Formation tag-based access control (LF-TBAC)**  
You can use LF-Tags to attach RLS policies to multiple tables. When you attach an RLS policy using LF-Tags, the policy automatically applies to any table that matches the tag.

**Attribute-based access control (ABAC)**  
You can attach an RLS policy using attributes that are IAM tags and session tags associated with IAM roles and principals. Lake Formation evaluates IAM session attributes at query time and determines whether the attachment applies to the caller. This lets you create attribute-driven row filtering without creating separate attachments for each principal.

**Data cell filters**  
RLS policies and data cell filters (DCF) can apply to the same table at the same time. When a principal is subject to both a DCF row filter and an RLS policy on a table, Lake Formation combines the two row filters using union (OR) semantics. The principal sees every row that matches either the DCF row filter or the RLS policy filter.

Because the row filters are additive, adding an RLS policy to a table that already has a DCF row filter can only expand the rows a principal sees, never restrict them. Plan for this behavior when you use both features together.

**RLS compatibility**  


**Table types**  
RLS policies are supported on any table registered in the AWS Glue Data Catalog, including:
+ Apache Iceberg tables
+ Apache Hive tables
+ Delta Lake tables
+ Apache Hudi tables
+ Amazon S3 Tables
+ Tables registered through federated catalogs (Amazon Redshift, and third-party catalogs where supported)

**Query engines**  
RLS policies are enforced by any analytics engine integrated with Lake Formation fine-grained access control, including:
+ Amazon Athena
+ Amazon Redshift Spectrum
+ Amazon EMR (Spark in FGAC mode)
+ AWS Glue ETL (Spark in FGAC mode)
+ Third-party engines that support Lake Formation fine-grained access control via session tags

**Identity types**  
RLS policies can be attached to any principal type supported by Lake Formation.

**Unsupported features**  
You cannot attach RLS policies to multi-dialect views. For more information, see [Row-level security policy limitations](rls-policies-limitations.md).

**Getting started**  


To use RLS policies, create an RLS policy with a filter expression and attachment columns, attach the policy to the table for one or more principals (or set it as a default), and grant `SELECT` on the table to the principals who need access. Principals then query the table and automatically see only the filtered rows. For detailed steps, see [Managing RLS policies](rls-policies-managing.md).