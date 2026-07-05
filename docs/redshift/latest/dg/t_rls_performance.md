Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Best practices for RLS performance

Following are best practices to ensure better performance from Amazon Redshift on tables
protected by RLS.

## Safety of operators and functions

When querying RLS-protected tables, the usage of certain operators or functions
may lead to performance degradation. Amazon Redshift classifies operators and functions
either as safe or unsafe for querying RLS-protected tables. A function or operator is
classified as RLS-safe when it doesn't have any observable side-effects
depending on the inputs. In particular, a RLS-safe function or operator can't be
one of the following:

- Outputs an input value, or any value that is dependent on the input value,
  with or without an error message.
- Fails or returns errors that are dependent on the input value.

RLS-unsafe operators include:

- Arithmetic operators — +, -, /, \*, %.
- Text operators — LIKE and SIMILAR TO.
- Some cast operators. Note that certain casts are classified as safe,
  including date-to-timestamp and timestamp-to-date conversions, integer
  widening casts (such as INT2 to INT8 or INT4 to INT8), and integer-to-text
  casts.
- UDFs.

Use the following SELECT statement to check the safety of operators and
functions.

```
SELECT proname, proc_is_rls_safe(oid) FROM pg_proc;
```

Amazon Redshift imposes restrictions on the order of evaluation of user predicates
containing RLS-unsafe operators and functions when planning queries on RLS-protected
tables. Queries referencing RLS-unsafe operators or functions might cause performance
degradation when querying RLS-protected tables. Performance can degrade significantly
when Amazon Redshift can't push RLS-unsafe predicates down to base table scans to take
advantage of sort keys. For better performance, avoid queries using RLS-unsafe
predicates that take advantage of a sort key. To verify that Amazon Redshift is able to push
down operators and functions, you can use EXPLAIN statements in combination with the
system permission EXPLAIN RLS.

### Conditionally safe functions

Some functions are classified as unsafe in general but become safe when
specific arguments are constant values (literal values, not column references).
When the relevant arguments are constants, Amazon Redshift can push these predicates
down to base table scans, improving query performance.

For example, `DATE_TRUNC('day', timestamp_col)` is
conditionally safe because `'day'` is a constant literal.
However, `DATE_TRUNC(datepart_col, timestamp_col)` is not
conditionally safe because `datepart_col` is a column
reference.

The following table lists the categories of conditionally safe functions and
which arguments must be constant for the function to be considered safe.

| Function category    | Functions                                                                                                                                | Argument that must be constant |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| DATE\_TRUNC          | DATE\_TRUNC(datepart, timestamp),<br>DATE\_TRUNC(datepart, timestamptz)                                                                  | datepart (first argument)      |
| EXTRACT / DATE\_PART | EXTRACT(field FROM source),<br>DATE\_PART(field, source) for timestamp, timestamptz, date,<br>time, timetz, interval, and datetime types | field (first argument)         |
| DATEDIFF             | DATEDIFF(datepart, start, end) for timestamp and time<br>types                                                                           | datepart (first argument)      |
| TO\_CHAR             | TO\_CHAR(timestamp, format),<br>TO\_CHAR(timestamptz, format)                                                                            | format (second argument)       |
| CONVERT\_TIMEZONE    | CONVERT\_TIMEZONE(source\_tz, target\_tz, timestamp),<br>CONVERT\_TIMEZONE(target\_tz, timestamp)                                        | timezone arguments             |
| LEFT / RIGHT         | LEFT(string, length), RIGHT(string, length)                                                                                              | length (second argument)       |
| SUBSTRING            | SUBSTRING(string, start, length) for text, bytea, and<br>varbyte types                                                                   | length (third argument)        |
| SPLIT\_PART          | SPLIT\_PART(string, delimiter, part)                                                                                                     | part (third argument)          |

Use the following SELECT statement to check which functions are conditionally
safe and which argument positions must be constant.

```
SELECT proname, proc_is_rls_conditionally_safe(oid) FROM pg_proc
WHERE proc_is_rls_conditionally_safe(oid) IS NOT NULL;
```

The function returns an array of 0-indexed argument positions that must be
constant, or NULL if the function is not conditionally safe.

## Result caching

To reduce query runtime and improve system performance, Amazon Redshift caches the
results of certain types of queries in the memory on the leader node.

Amazon Redshift uses cached results for a new query scanning RLS-protected tables when
all the conditions for unprotected tables are true and when all of the following are
true:

- The tables or views in the policy haven't been modified.
- The policy doesn't use a function that must be evaluated each time
  it's run, such as GETDATE or CURRENT\_USER.

For better performance, avoid using policy predicates that don't satisfy the
preceding conditions.

For more information about result caching in Amazon Redshift, see [Result caching](c_challenges_achieving_high_performance_queries.md#result-caching "c_challenges_achieving_high_performance_queries.md#result-caching").

## Complex policies

For better performance, avoid using complex policies with subqueries that join
multiple tables.

## Using constant arguments for better pushdown

When using functions such as DATE\_TRUNC, EXTRACT, DATEDIFF, TO\_CHAR,
CONVERT\_TIMEZONE, LEFT, RIGHT, SUBSTRING, or SPLIT\_PART in queries on
RLS-protected tables, use constant literal arguments instead of column references
for the arguments that control error behavior. This allows Amazon Redshift to classify
these functions as safe and push predicates down to base table scans, which can
significantly improve performance.

For example, the following query allows predicate pushdown because the datepart
argument is a constant:

```
SELECT * FROM rls_protected_table
WHERE DATE_TRUNC('month', event_date) = '2024-01-01';
```

The following query prevents predicate pushdown because the datepart argument
is a column reference:

```
SELECT * FROM rls_protected_table
WHERE DATE_TRUNC(datepart_col, event_date) = '2024-01-01';
```

For the full list of conditionally safe functions and which arguments must be
constant, see [Conditionally safe functions](#t_rls_conditional_safety "#t_rls_conditional_safety").
