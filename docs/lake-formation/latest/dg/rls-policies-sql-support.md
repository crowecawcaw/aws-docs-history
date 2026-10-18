

# Filter expression syntax for RLS policies
<a name="rls-policies-sql-support"></a>

This section describes the syntax, operators, data types, and rules for filter expressions used in row-level security (RLS) policies. Filter expressions use the PartiQL subset supported by Lake Formation data cell filters.

**Overview**  


A filter expression defines the condition that rows must satisfy for a principal to see them. The expression is specified in the `FilterExpression` field when creating or updating an RLS policy.

Filter expressions have the following constraints:
+ Maximum length: 2048 characters
+ Must reference only columns declared in `AttachmentColumns`
+ Must use supported operators and data types
+ Cannot contain subqueries, joins, user-defined functions, or column-to-column comparisons

**Simple expressions**  


A simple expression compares a column to a literal value.

```
column_name operator value
```

**Example Simple expressions**  

```
department = 'Engineering'
age >= 21
salary < 100000
country <> 'US'
```

**Composite expressions**  


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
(department = 'Sales' OR department = 'Marketing') AND country = 'US'
```

Use parentheses to control evaluation order. Without parentheses, `AND` has higher precedence than `OR`.

**Supported operators**  



| Operator | Description | Example | 
| --- | --- | --- | 
| = | Equal to | status = 'active' | 
| > | Greater than | amount > 1000 | 
| < | Less than | age < 65 | 
| >= | Greater than or equal to | score >= 80 | 
| <= | Less than or equal to | priority <= 3 | 
| <> | Not equal to | region <> 'internal' | 
| \!= | Not equal to (alternative) | type \!= 'draft' | 
| BETWEEN | Within a range (inclusive) | age BETWEEN 18 AND 65 | 
| IN | Matches any value in a list | region IN ('us-east-1', 'us-west-2') | 
| LIKE | Pattern matching with wildcards | email LIKE '%@example.com' | 
| NOT | Negates a condition | NOT (status = 'deleted') | 
| IS NULL | Checks for null value | manager\_id IS NULL | 
| IS NOT NULL | Checks for non-null value | email IS NOT NULL | 

**BETWEEN operator**  
The `BETWEEN` operator tests whether a value falls within an inclusive range. `salary BETWEEN 50000 AND 100000` is equivalent to `salary >= 50000 AND salary <= 100000`.

**IN operator**  
The `IN` operator tests whether a value matches any value in a list, for example `department IN ('Engineering', 'Sales', 'Marketing')`.

**LIKE operator**  
The `LIKE` operator performs pattern matching. Use `%` as a wildcard for any sequence of characters and `_` for a single character, for example `email LIKE '%@example.com'`.

**IS NULL and IS NOT NULL**  
Test whether a column value is null or not null, for example `manager_id IS NULL` or `email IS NOT NULL`.

**Note**  
`IS NULL` and `IS NOT NULL` cannot be used on partition columns. See [Row-level security policy limitations](rls-policies-limitations.md) for details.

**Supported data types**  


The following data types are supported in the `Type` field of AttachmentColumns and determine what literal values are valid in the filter expression.


| Data type | Description | Example literal | 
| --- | --- | --- | 
| STRING | Variable-length character string | 'hello' | 
| CHAR | Fixed-length character string | 'A' | 
| VARCHAR | Variable-length character string | 'hello world' | 
| INT | 32-bit signed integer | 42 | 
| LONG | 64-bit signed integer | 9223372036854775807 | 
| BIGINT | 64-bit signed integer (alias for LONG) | 1000000000000 | 
| FLOAT | 32-bit floating point | 3.14 | 
| DECIMAL | Arbitrary precision decimal | 99.99 | 
| DOUBLE | 64-bit floating point | 2.718281828 | 
| BOOLEAN | True or false value | true | 

**Note**  
In the `AttachmentColumns` `Type` field, type strings are case-sensitive and must be lowercase (for example, `string`, `int`, `bigint`, `double`, `decimal`, `boolean`).

**String literals**  
String literals must be enclosed in single quotes, for example `department = 'Engineering'`. To include a single quote within a string literal, use two consecutive single quotes (`''`), for example `name = 'O''Brien'`.

**Numeric literals**  
Numeric literals are specified without quotes, for example `amount > 1000`, `ratio >= 0.75`, `is_active = true`.

**Case sensitivity rules**  

+ **Column names** in filter expressions are case-insensitive. `Department`, `department`, and `DEPARTMENT` all refer to the same column.
+ **String literal values** in comparisons are case-sensitive. `'Engineering'` does not match `'engineering'`.
+ **Keywords** (AND, OR, NOT, BETWEEN, IN, LIKE, IS, NULL) are case-insensitive.
+ **Policy names** are case-insensitive.

**Reserved keyword escaping**  


If a column name matches a reserved keyword (for example, `status`, `name`, `type`), enclose it in double quotes within the filter expression.

```
"status" = 'active'
"name" LIKE 'J%'
"type" IN ('order', 'return')
```

Using double quotes ensures the identifier is treated as a column name rather than a keyword.

**Complete examples**  


**Example Simple department filter**  

```
{
  "Name": "engineering-only",
  "FilterExpression": "department = 'Engineering'",
  "AttachmentColumns": [
    {
      "Name": "department",
      "Type": "string"
    }
  ]
}
```

**Example Multi-condition filter with numeric comparison**  

```
{
  "Name": "high-value-us-orders",
  "FilterExpression": "country = 'US' AND amount >= 10000",
  "AttachmentColumns": [
    {
      "Name": "country",
      "Type": "string"
    },
    {
      "Name": "amount",
      "Type": "decimal"
    }
  ]
}
```

**Example IN clause with multiple values**  

```
{
  "Name": "multi-region-access",
  "FilterExpression": "region IN ('us-east-1', 'us-west-2', 'eu-west-1')",
  "AttachmentColumns": [
    {
      "Name": "region",
      "Type": "string"
    }
  ]
}
```

**Example BETWEEN with numeric range**  

```
{
  "Name": "recent-records",
  "FilterExpression": "year BETWEEN 2023 AND 2026",
  "AttachmentColumns": [
    {
      "Name": "year",
      "Type": "int"
    }
  ]
}
```

**Example Pattern matching with LIKE**  

```
{
  "Name": "internal-emails-only",
  "FilterExpression": "email LIKE '%@example.com'",
  "AttachmentColumns": [
    {
      "Name": "email",
      "Type": "string"
    }
  ]
}
```

**Example Composite filter with parentheses**  

```
{
  "Name": "sales-marketing-us",
  "FilterExpression": "(department = 'Sales' OR department = 'Marketing') AND country = 'US'",
  "AttachmentColumns": [
    {
      "Name": "department",
      "Type": "string"
    },
    {
      "Name": "country",
      "Type": "string"
    }
  ]
}
```

**Nested column references**  


If your table contains struct (nested) columns, you can reference nested fields in RLS policy filter expressions. The nested path must be specified using dot notation or double-quoted path notation in both the `AttachmentColumns` and the `FilterExpression`.

**Dot notation (recommended)**  


```
{
  "Name": "a.city",
  "Type": "string"
}
```

**Quoted path notation**  


```
{
  "Name": "\"a\".\"city\"",
  "Type": "string"
}
```

The following format is **not** supported:

```
{
  "Name": "a",
  "Type": "struct<city: string>"
}
```

You must reference the leaf-level nested field directly (for example, `a.city`), not the parent struct column with its full type definition.

**Important rules for column names with dots**  

+ A column name containing a dot (for example, `addr.zip`) is always interpreted as a nested column path (parent `addr`, child `zip`). If you have a top-level column literally named `addr.zip`, it cannot be used in an RLS policy because the dot is treated as a path separator.
+ Column names containing literal double-quote characters (`"`) are not supported in RLS policies.

When filtering on a nested column, use dot notation in the filter expression, for example `a.city = 'Seattle'`.

**Limitations**  


Any expression or feature not described in this section is not supported. For the complete list of RLS policy limitations, see [Row-level security policy limitations](rls-policies-limitations.md).