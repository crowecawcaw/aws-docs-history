

# Filter expression syntax for RLS policies
<a name="rls-policies-sql-support"></a>

This section describes the syntax, operators, data types, and rules for filter expressions used in row-level security (RLS) policies. Filter expressions use a subset of PartiQL.

## Overview
<a name="w2aac15c15c73b5"></a>

A filter expression defines the condition that rows must satisfy for a principal to see them. The expression is specified in the `FilterExpression` field when creating or updating an RLS policy.

## Simple expressions
<a name="w2aac15c15c73b7"></a>

A simple expression compares an attachment column to a literal value or to another attachment column, or uses a boolean column or literal as the condition.

```
column_name operator value
column_name operator column_name
boolean_column
```

**Example Simple expressions**  

```
department = 'Engineering'
age >= 21
home_region = region
is_active
NOT is_deleted
```

## Composite expressions
<a name="w2aac15c15c73b9"></a>

Combine multiple conditions using `AND`, `OR`, and `NOT`.

```
condition AND condition
condition OR condition
NOT condition
(condition) AND (condition)
```

**Example Composite expressions**  

```
department = 'Engineering' AND country = 'US'
region = 'us-east-1' OR region = 'eu-west-1'
NOT (status = 'inactive')
is_active AND (region = 'us-east-1' OR region = 'eu-west-1')
```

Use parentheses to control evaluation order. Without parentheses, `AND` has higher precedence than `OR`.

Each operand of `AND`, `OR`, and `NOT` must be a condition or a boolean value, such as a boolean column, `TRUE`, `FALSE`, or a function that returns a boolean. A subquery can't be an operand directly. For more information, see Reference table subqueries in this section.

## Reference table subqueries
<a name="w2aac15c15c73c11"></a>

Filter expressions support `EXISTS`, `NOT EXISTS`, `IN`, and `NOT IN` subqueries over reference tables. To compare an attachment column to a reference table column, use a subquery.

```
[NOT] EXISTS (
  SELECT select_item [, select_item ...]
  FROM database_name.table_name [[AS] alias]
  [supported join clauses]
  [WHERE condition]
)

attachment_column [NOT] IN (
  SELECT select_item
  FROM database_name.table_name [[AS] alias]
  [supported join clauses]
  [WHERE condition]
)
```

A reference table name must be qualified as `databaseName.tableName` or `catalogId.databaseName.tableName`. The catalog ID must be the policy creator's account ID. Enclose a numeric catalog ID in double quotes, such as `"123456789012".security.entitlements`.

A reference table column can be qualified by a table alias (`e.region`), `databaseName.tableName` (`security.entitlements.region`), or `catalogId.databaseName.tableName`. Scalar struct fields of a reference table can also be referenced, such as `e.profile.customer_id`. An unqualified column name always refers to an attachment column.

Each reference table must meet the following requirements:
+ The table is a base table registered with Lake Formation. Views and resource links aren't supported.
+ The policy creator's IAM permissions allow `glue:GetTable` on the table.
+ The policy creator has Lake Formation `SELECT` with grant option on the table.

```
EXISTS (
  SELECT 1
  FROM security.entitlements e
  WHERE e.region = region
    AND e.access_level = 'full'
)
```

A regular subquery select list can contain a column, `*`, a literal, a `CAST`, `TRIM`, `SUBSTRING`, or a supported function call. A star can be unqualified or qualified by a namespace, such as `security.entitlements.*`.

A subquery's `WHERE` clause can contain another `EXISTS` or `IN` subquery, up to the limit of four subqueries in total.

**Note**  
Tables included in RLS policy filter expressions are referenced by ID. If a table is deleted, the policy is considered INVALID. INVALID policies are treated as FALSE. For more information, see [Row-level security policy limitations](rls-policies-limitations.md).

**Join clauses**  
Use `JOIN` to reference multiple tables in a policy expression.

The `ON` condition follows the same rules as a `WHERE` condition, and can be a boolean column such as `ON r.enabled`.

```
EXISTS (
  SELECT 1
  FROM security.customer_regions c
  JOIN security.region_status r ON r.region = c.region
  WHERE c.customer_id = customer_id
    AND r.enabled = true
)
```

## Supported operators
<a name="w2aac15c15c73c13"></a>


| Operator | Description | Example | 
| --- | --- | --- | 
| = | Equal to | status = 'active' | 
| > | Greater than | amount > 1000 | 
| < | Less than | age < 65 | 
| >= | Greater than or equal to | score >= 80 | 
| <= | Less than or equal to | priority <= 3 | 
| <> | Not equal to | region <> 'internal' | 
| \!= | Not equal to (alternative) | type \!= 'draft' | 
| BETWEEN, NOT BETWEEN | Tests an inclusive range | age BETWEEN 18 AND 65 | 
| IN, NOT IN | Tests a literal list or a subquery result | region IN ('us-east-1', 'us-west-2') | 
| LIKE, NOT LIKE | Pattern matching with wildcards | email LIKE '%@example.com' | 
| AND, OR, NOT | Combines or negates conditions | active = true AND deleted = false | 
| IS NULL, IS NOT NULL | Tests for a null or non-null value | manager\_id IS NULL | 
| \+, -, \* | Numeric arithmetic | (amount \* quantity) > 1000 | 
| unary - | Negates a numeric value | balance >= -100 | 
| EXISTS, NOT EXISTS | Tests whether a subquery returns rows | EXISTS (SELECT 1 FROM security.entitlements e WHERE e.region = region) | 
| literal IN array | Tests whether an array contains a literal | 'admin' IN roles | 

The operands of a comparison must have compatible types. For example, you can't compare a string column with a numeric literal. For more information, see Type compatibility in this section.

**BETWEEN operator**  
The `BETWEEN` operator tests whether a value falls within an inclusive range.

```
salary BETWEEN 50000 AND 100000
start_date BETWEEN '2026-01-01' AND CURRENT_DATE
```

`salary BETWEEN 50000 AND 100000` is equivalent to `salary >= 50000 AND salary <= 100000`.

Each bound must be type-compatible with the tested value. A bound can be a column, a literal, or an expression, but not a subquery.

**IN operator**  
The `IN` operator supports a literal list, a subquery, or array containment.

```
department IN ('Engineering')
region IN ('us-east-1', 'us-west-2', 'eu-west-1')
region IN (SELECT r.region FROM security.region_status r WHERE r.enabled = true)
'admin' IN roles
```

The left operand of an `IN` literal list or an `IN` subquery must be a column. An `IN` literal list must contain one or more literals, and each literal must be type-compatible with the column. For array containment, the left operand must be a literal and the right operand must be an array column.

When an `IN` subquery selects exactly one item, that item must be type-compatible with the compared column. An `IN` subquery compared with a `string` or `varchar` column has the following additional rules:
+ The subquery must select exactly one column.
+ The subquery can't select an aggregate function (`MIN` or `MAX`).
+ The subquery's `FROM` clause must use table names and aliases that differ from every qualifier of the compared column.

**LIKE operator**  
The `LIKE` operator performs pattern matching on strings. Use `%` as a wildcard for any sequence of characters and `_` for a single character.

```
email LIKE '%@example.com'
name LIKE 'J%'
code LIKE 'A_B'
```

The value and the pattern must both be strings. The `ESCAPE` clause isn't supported.

**IS NULL and IS NOT NULL**  
Test whether a value is null or not null. The operand can be a column or an expression of any type.

```
manager_id IS NULL
email IS NOT NULL
```

To test for null, use `IS NULL`. A comparison such as `manager_id = NULL` isn't supported.

## Supported functions
<a name="w2aac15c15c73c15"></a>

The following builtin functions are supported:
+ `EXISTS`
+ `LENGTH`
+ `LOWER`
+ `MAX`
+ `MIN`
+ `SUBSTRING`
+ `TRIM`
+ `UPPER`

Function names are case-insensitive. Other builtin functions, such as `CONCAT`, `SUM`, `AVG`, `CEIL`, or `DATEADD`, aren't supported.

Builtin functions have the following argument and result rules:
+ `LENGTH` takes one string argument and returns an integer.
+ `LOWER` and `UPPER` take one string argument and return a string.
+ `TRIM` takes string arguments and returns a string. Both `TRIM(value)` and `TRIM([LEADING | TRAILING | BOTH] [characters] FROM value)` are supported.
+ `SUBSTRING` takes a string value, a start, and an optional length, and returns a string. Both `SUBSTRING(value, start [, length])` and `SUBSTRING(value FROM start [FOR length])` are supported. The start must be an integer literal of at least 1. The length must be a non-negative integer literal.
+ `MIN` and `MAX` take one argument and return the argument's type. The query engine, rather than the policy validation, checks where an aggregate function is placed.
+ `EXISTS` takes exactly one subquery and returns a boolean.

```
LENGTH(account_id) > 0
UPPER(country) = 'US'
LOWER(TRIM(email)) LIKE '%@example.com'
SUBSTRING(account_id FROM 1 FOR 3) = 'acc'
TRIM(LEADING '0' FROM employee_code) = '42'
```

**CAST**  
`CAST` supports the following conversions:


| Source | Target | 
| --- | --- | 
| Integer | VARCHAR or STRING, without a length | 
| string or varchar, or integer | TINYINT, SMALLINT, INT, INTEGER, or BIGINT | 
| Integer or decimal | DECIMAL(p,s) or NUMERIC(p,s) | 
| Integer | FLOAT, REAL, or DOUBLE PRECISION | 
| String literal in YYYY-MM-DD format | DATE | 
| String literal in YYYY-MM-DD HH:MM:SS[.ffffff] format | TIMESTAMP | 
| Timestamp | DATE | 

`DECIMAL` without a precision and scale is `DECIMAL(10,0)`. Other conversions, including casts to `CHAR(n)`, to `VARCHAR(n)` with a length, from `char(n)` values, and from boolean, date, or decimal values to strings, aren't supported.

**EXTRACT and CURRENT\_DATE**  
`EXTRACT` supports the `YEAR`, `MONTH`, and `DAY` fields of a `DATE` value and returns an integer. To extract a field from a timestamp, cast the timestamp to `DATE` first.

```
EXTRACT(YEAR FROM created_date) >= 2024
EXTRACT(MONTH FROM CURRENT_DATE) = 12
EXTRACT(DAY FROM CAST(updated_at AS DATE)) = 1
```

`CURRENT_DATE` returns the current UTC date as a `DATE`. Write it without parentheses. `CURRENT_TIMESTAMP`, `CURRENT_USER`, and other session attributes aren't supported. To use the querying identity, see Dynamic user attributes in this section.

**Derived tables and window functions**  
The supported window functions are `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, and `LEAD`. A window function is supported only in a derived table's select list. It can't appear in a `WHERE` or `ON` condition.

A derived table must:
+ Have an alias
+ Project qualified columns, such as `e.account_id`, or supported window functions. `*` isn't supported.
+ Give every projected item an explicit `AS` alias

Outside the derived table, refer to a projected item as `alias.item`, such as `d.rn`.

```
EXISTS (
  SELECT 1
  FROM (
    SELECT e.account_id AS account_id,
           ROW_NUMBER() OVER (
             PARTITION BY e.account_id
             ORDER BY e.updated_at DESC
           ) AS rn
    FROM security.entitlements e
  ) d
  WHERE d.account_id = account_id
    AND d.rn = 1
)
```

`ROW_NUMBER`, `RANK`, and `DENSE_RANK` take no arguments and return an integer. `LAG` and `LEAD` take one operand. An offset, a default value, and `IGNORE NULLS` or `RESPECT NULLS` aren't supported. An `OVER` clause can contain `PARTITION BY`, `ORDER BY` with `ASC` or `DESC`, or both. Named windows (`OVER w`) and the `WINDOW` clause aren't supported.

## Dynamic user attributes
<a name="w2aac15c15c73c17"></a>

Dynamic user attributes insert a value from the querying identity at query time, so one policy can return different rows for each caller.

```
${context.namespace.attribute_name}
```

The following table lists the supported dynamic user attributes.


| Dynamic attribute | Description | Example | 
| --- | --- | --- | 
| ${context.aws.PrincipalAccount} | The AWS account ID of the querying principal, such as 111122223333. | owner\_account\_id = ${context.aws.PrincipalAccount} | 
| ${context.aws.PrincipalArn} | The ARN of the querying IAM principal, such as arn:aws:iam::111122223333:role/Analyst. | ${context.aws.PrincipalArn} LIKE '%:role/Analyst%' | 
| ${context.iam.{{tag-key}}} | The value of the IAM session tag {{tag-key}} on the querying principal. | ${context.iam.team} = 'analytics' | 
| ${context.datazone.projectId} | The Amazon DataZone project ID of the querying principal. | project\_id = ${context.datazone.projectId} | 

The `aws.` namespace supports only `PrincipalAccount` and `PrincipalArn`. The `datazone.` namespace supports only `projectId`.

**Example Dynamic user attributes**  

```
owner_account_id = ${context.aws.PrincipalAccount}
${context.aws.PrincipalArn} LIKE '%:role/Analyst%'
department = ${context.iam.department}
${context.iam.team} = 'analytics'
project_id = ${context.datazone.projectId}
${context.iam.team} IN allowed_teams
region IN (${context.iam.home_region}, 'global')
```

The following rules apply to all dynamic user attributes:
+ The `context.` prefix and the namespace are case-sensitive and must be lowercase. Attribute names are case-sensitive.
+ The attribute name after the namespace can contain up to 128 characters from `A-Z`, `a-z`, `0-9`, `_`, `+`, `=`, `.`, `:`, `/`, `@`, and `-`.
+ Write the attribute outside quotes. Inside a string literal or a double-quoted identifier, `${...}` is literal text. Outside quotes, a `$` must start a dynamic attribute.
+ The resolved value is inserted as a string literal, so compare it with a string value. You can't compare it directly with a numeric, date, or timestamp value.
+ A missing attribute resolves to `NULL`, so a comparison against it is never true.
+ To match a dynamic attribute against several values, combine equality expressions with `OR`, or test whether an array column contains it, as in `${context.iam.team} IN allowed_teams`. A dynamic attribute can be a value in an `IN` list, but it can't be the left operand of an `IN` list.
+ To match part of a principal ARN, such as the role name, use `LIKE`. Filter expressions don't support string split functions.

## Supported data types
<a name="w2aac15c15c73c19"></a>

The following data types are supported in `AttachmentColumns` and for resolved reference table columns.


| Data type | Description | Example literal | 
| --- | --- | --- | 
| string, varchar, varchar(n), nvarchar, nvarchar(n) | Character strings | 'hello' | 
| char, char(n), nchar, nchar(n) | Fixed-length, blank-padded character strings | 'abc' | 
| int, tinyint, smallint, integer, int2, int4 | Integer values | 42 | 
| bigint, int8, long | 64-bit integer values | 1000000000000 | 
| float, float4, float8, double | Floating-point values | 3.14 | 
| decimal(p,s), numeric | Exact numeric values | 99.99 | 
| boolean, bool | True or false values | true | 
| date | Date value compared to another date, CURRENT\_DATE, or a date literal | '2026-10-19', DATE '2026-10-19' | 
| timestamp | Timestamp value compared to another timestamp or a timestamp literal | '2026-10-19 12:00:00', TIMESTAMP '2026-10-19 12:00:00' | 
| timestamptz | Timestamp with time zone, compared to another timestamptz value | created\_at < updated\_at | 
| array<...> | Array used for literal containment tests | 'admin' IN roles | 
| binary, varbinary | Opaque binary value compared to another binary column | checksum = expected\_checksum | 
| void | Value used with null predicates | value IS NULL | 

**Note**  
In the `AttachmentColumns` `Type` field, type strings are case-sensitive and must be lowercase (for example, `string`, `int`, `bigint`, `double`, `decimal`, `boolean`).

Other column types, such as `map<...>` or a whole `struct<...>`, can't be used in an expression. To use a struct, reference one of its scalar fields. For more information, see Nested column references in this section.

Exact numeric literals, coercions, and arithmetic results can contain at most 38 digits. A `decimal(p,s)` type requires a precision from 1 through 38 and a scale from 0 through the precision.

A date string literal must use the `YYYY-MM-DD` format. A timestamp string literal must use the `YYYY-MM-DD HH:MM:SS[.ffffff]` format. To compare a timestamp with a date, cast the timestamp to `DATE`. `DATE '...'` and `TIMESTAMP '...'` are the only supported typed literals.

**Type compatibility**  
The operands of a comparison, `BETWEEN`, `IN`, or `LIKE` must have compatible types:
+ Integer, decimal, and floating-point values are compatible with each other. Two exact numeric values are compatible only if both fit in 38 digits at their larger scale. For example, a `decimal(38,38)` column can't be compared with `1`.
+ Character string values, including `char(n)`, are compatible with each other and with string literals.
+ Boolean values are compatible with boolean values.
+ A `date` value is compatible with another `date`, `CURRENT_DATE`, and a string literal in `YYYY-MM-DD` format.
+ A `timestamp` value is compatible with another `timestamp` and a string literal in `YYYY-MM-DD HH:MM:SS[.ffffff]` format.
+ A `timestamptz` value is compatible only with another `timestamptz` value.
+ A `binary` or `varbinary` value is compatible only with another binary value.
+ An array can only be tested for containment. A `void` value can only be tested with `IS NULL`.

Arithmetic operands must be numeric. String concatenation (`||`), division (`/`), and modulo (`%`) aren't supported.

**String literals**  
String literals must be enclosed in single quotes:

```
department = 'Engineering'
name = 'O''Brien'
```

To include a single quote within a string literal, use two consecutive single quotes (`''`).

String equality is exact. For `string` and `varchar` values, `=`, `<>`, `!=`, and `IN` treat trailing spaces as significant on every query engine, so `'abc '` doesn't equal `'abc'`. `char(n)` values are blank-padded and compare without regard to trailing spaces.

**Numeric literals**  
Numeric literals are specified without quotes:

```
amount > 1000
ratio >= 0.75
balance >= -100
```

## Case sensitivity rules
<a name="w2aac15c15c73c21"></a>
+ **Attachment and reference column names** in filter expressions are case-insensitive. `Department`, `department`, and `DEPARTMENT` refer to the same column.
+ **Database and table names** are case-insensitive.
+ **Table aliases, function names, and keywords** are case-insensitive.
+ **Dynamic attribute prefixes, namespaces, and attribute names** are case-sensitive. For more information, see Dynamic user attributes in this section.
+ **String literal values** in comparisons are case-sensitive. `'Engineering'` does not match `'engineering'`.
+ **Policy names** are case-insensitive.

## Reserved keyword escaping
<a name="w2aac15c15c73c23"></a>

If an identifier matches a reserved [PartiQL keyword](https://partiql.org/syntax/antlr.html) or contains characters other than letters, digits, and underscores, enclose it in double quotes within the filter expression. Quoted identifiers are still case-insensitive.

```
"year" > 2020
e."type" = 'internal'
"a""b" = 'value'
EXISTS (SELECT 1 FROM "my db"."acl-table" a WHERE a.id = id)
```

To include a literal double quote in an identifier, use two consecutive double quotes (`""`).

## Comments
<a name="w2aac15c15c73c25"></a>

A filter expression can contain `--` line comments and `/* ... */` block comments. Comments count toward the 2048-character limit.

```
region = 'us-east-1' -- primary region only
/* entitlement check */ EXISTS (SELECT 1 FROM security.entitlements e WHERE e.region = region)
```

## Unsupported syntax
<a name="w2aac15c15c73c27"></a>

The following SQL constructs aren't supported in a filter expression:
+ `GROUP BY`, `HAVING`, `ORDER BY` (except inside `OVER`), `LIMIT`, `OFFSET`, and `WITH`
+ `SELECT DISTINCT` and `SELECT ALL`
+ `FULL [OUTER] JOIN`, `CROSS JOIN`, and comma-separated `FROM` lists
+ A subquery used as a value, such as `amount < (SELECT ...)` or `(SELECT ...) IS NOT NULL`
+ Array subscripts, such as `regions[0]`
+ `LIKE ... ESCAPE`
+ `IS [NOT] TYPE` predicates, such as `col IS BOOLEAN`
+ `||`, `/`, and `%` operators
+ Functions other than the supported functions
+ `UNPIVOT` and `AT` in a `FROM` clause

## Complete examples
<a name="w2aac15c15c73c29"></a>

The following examples create RLS policies with the AWS CLI. If a filter expression contains a dynamic attribute, enclose the expression in single quotes, or escape each `$` as `\$`, so that the shell doesn't expand it.

**Example Simple department filter**  

```
aws lakeformation create-rls-policy \
  --name "engineering-only" \
  --filter-expression "department = 'Engineering'" \
  --attachment-columns '[{"Name": "department", "Type": "string"}]'
```

**Example Multi-condition filter with numeric comparison**  

```
aws lakeformation create-rls-policy \
  --name "high-value-us-orders" \
  --filter-expression "country = 'US'
    AND amount >= 10000" \
  --attachment-columns '[
    {"Name": "country", "Type": "string"},
    {"Name": "amount", "Type": "decimal"}
  ]'
```

**Example IN clause with multiple values**  

```
aws lakeformation create-rls-policy \
  --name "multi-region-access" \
  --filter-expression "region IN ('us-east-1', 'us-west-2', 'eu-west-1')" \
  --attachment-columns '[{"Name": "region", "Type": "string"}]'
```

**Example BETWEEN with numeric range**  

```
aws lakeformation create-rls-policy \
  --name "recent-records" \
  --filter-expression "year BETWEEN 2023 AND 2026" \
  --attachment-columns '[{"Name": "year", "Type": "int"}]'
```

**Example Pattern matching with LIKE**  

```
aws lakeformation create-rls-policy \
  --name "internal-emails-only" \
  --filter-expression "email LIKE '%@example.com'" \
  --attachment-columns '[{"Name": "email", "Type": "string"}]'
```

**Example Composite filter with parentheses**  

```
aws lakeformation create-rls-policy \
  --name "sales-marketing-us" \
  --filter-expression "(department = 'Sales' OR department = 'Marketing')
    AND country = 'US'" \
  --attachment-columns '[
    {"Name": "department", "Type": "string"},
    {"Name": "country", "Type": "string"}
  ]'
```

**Example Reference table entitlement**  

```
aws lakeformation create-rls-policy \
  --name "region-entitlement" \
  --filter-expression 'EXISTS (
      SELECT 1
      FROM security.entitlements e
      WHERE e.principal = ${context.iam.employee_id}
        AND e.region = region
    )' \
  --attachment-columns '[{"Name": "region", "Type": "string"}]'
```

**Example IN subquery**  

```
aws lakeformation create-rls-policy \
  --name "allowed-cost-centers" \
  --filter-expression 'cost_center IN (
      SELECT e.cost_center
      FROM security.cost_center_entitlements e
      WHERE e.principal = ${context.iam.employee_id}
    )' \
  --attachment-columns '[{"Name": "cost_center", "Type": "string"}]'
```

**Example Entitlement table keyed on the querying principal**  
The caller sees only the regions mapped to their principal ARN in an entitlement table.  

```
aws lakeformation create-rls-policy \
  --name "principal-region-entitlement" \
  --filter-expression 'EXISTS (
      SELECT 1
      FROM auth_db.principal_access a
      WHERE a.principal_arn = ${context.aws.PrincipalArn}
        AND a.region = region
    )' \
  --attachment-columns '[{"Name": "region", "Type": "string"}]'
```

**Example Querying principal's account and role**  
A caller using the `Analyst` role sees only the rows for their own account.  

```
aws lakeformation create-rls-policy \
  --name "analyst-own-account" \
  --filter-expression "owner_account_id = \${context.aws.PrincipalAccount}
    AND \${context.aws.PrincipalArn} LIKE '%:role/Analyst%'" \
  --attachment-columns '[{"Name": "owner_account_id", "Type": "string"}]'
```

## Nested column references
<a name="w2aac15c15c73c31"></a>

If your table contains struct columns, you can reference scalar nested fields in RLS policy filter expressions. Specify the nested path using dot notation in both `AttachmentColumns` and the `FilterExpression`.

**Valid nested column formats in AttachmentColumns**  
The following formats are supported when specifying a nested column in `AttachmentColumns`:

**Dot notation (recommended)**  


```
{
  "Name": "address.city",
  "Type": "string"
}
```

**Quoted dot notation**  


```
{
  "Name": "\"address\".\"city\"",
  "Type": "string"
}
```

Quoted notation is equivalent to dot notation.

Reference the leaf-level nested field directly instead of declaring the parent struct as the attachment column.

**Important rules for column names with dots**  

+ Dot notation walks a struct field path.
+ Avoid a top-level column whose name contains a dot when the table also contains the equivalent struct path, because the references are ambiguous.

**Filter expression with nested columns**  
When filtering on a nested column, use dot notation in the filter expression:

```
address.city = 'Seattle'
EXISTS (SELECT 1 FROM security.entitlements e WHERE e.profile.city = address.city)
```

Scalar struct fields of a reference table can be referenced the same way, after the table alias or qualified table name. Array subscripts, such as `orders[0].amount`, aren't supported. To test an array, use containment, such as `'admin' IN roles`.

## Limitations
<a name="w2aac15c15c73c33"></a>

Filter expressions have the following constraints:
+ Maximum length: 2048 characters before dynamic attribute substitution, including comments
+ Maximum of four subqueries
+ Maximum of 10 distinct references
+ A derived table can't contain another derived table
+ Reference tables must be in the policy creator's catalog

When you update a policy, the new filter expression is validated against the attachment columns declared when the policy was created. `UpdateRLSPolicy` doesn't change `AttachmentColumns`.

For the complete list of RLS policy limitations, see [Row-level security policy limitations](rls-policies-limitations.md).