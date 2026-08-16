# Comparison controls

In SQL, literal comparison matches a column from your dataset against a literal value
typed directly into the query. Column comparison matches values from two different columns
against each other, either within the same table or across joined tables.

## Default behavior

Comparison controls are an allowlist. Once you set
`allowedLiteralComparisonColumns`, only the columns you list can be compared to
a literal value, and every column you do not list is blocked. The same applies to
`allowedColumnComparisonColumns` for column-to-column comparisons. Adding a
column to one allowlist does not add it to the other.

If you do not configure `comparisonControls`, AWS Clean Rooms applies no comparison
restrictions — a query can compare any column to a literal value or to another
column.

If you do not configure `comparisonControls` but you do set a minimum
aggregation threshold, comparisons remain otherwise unrestricted. However, AWS Clean Rooms never
allows a literal comparison on a column listed in `identityColumns`. That
restriction comes from the threshold itself, so it applies whether or not you configure
comparison controls. For more information, see [Minimum aggregation thresholds](custom-min-agg-thresholds.md "custom-min-agg-thresholds.md").

If you configure `comparisonControls` together with disallowed output
columns, the two controls are independent and both apply. Comparison controls govern which
columns a query can compare; disallowed output columns govern which columns can appear in
the query result. A column can be allowed in a comparison and still be barred from the
result. For more information, see [Disallowed output columns](disallowed-output-columns.md "disallowed-output-columns.md").

## Literal comparison

A literal comparison evaluates a column against a single hardcoded constant (a string,
number, or date). The right side of the operator never changes during the query execution.
Syntax examples include:

- WHERE status = 'Active'
- WHERE price > 49.99

When you use [Minimum aggregation thresholds](custom-min-agg-thresholds.md "custom-min-agg-thresholds.md"), AWS Clean Rooms does not allow literal comparison
on the `identityColumns` value. This prevents the query runner from submitting a query
filtered down to an individual or specific set of users. Avoid allowing literal
comparison on low cardinality columns that can single out small groups or individual data
subjects.

```
{
  "comparisonControls": {
    "allowedLiteralComparisonColumns": [
      "status",
      "price"
    ]
  }
}
```

###### Choosing columns for literal comparison

Allow literal comparison only on columns that don't identify individuals or small
groups. Avoid allowing it on low-cardinality columns (for example, age\_band, coarse
region code). Even though these columns are not the configured
`identityColumns` value, comparing them to literals can narrow results to a small,
identifiable population. High-cardinality, non-identifying dimensions such as
`campaign_id` or `product_sku` are safer choices.

### Example: Allowing literal comparison on a campaign column

A publisher configures a custom analysis rule with a minimum aggregation threshold so
that every output row represents at least 100 distinct users (`user_id`). An
advertiser runs queries against this table but needs to scope their analysis to a specific
advertising campaign — for example, to measure reach for one campaign at a time.

Because `user_id` is the identity column, it can't be compared to a
literal, preventing the advertiser from filtering results down to a single user. But
`campaign_id` and `event_date` are high-cardinality,
non-identifying dimensions, so the publisher adds them to
`allowedLiteralComparisonColumns`, which lets the advertiser filter by campaign
and scope the analysis to a date range:

```
{
  "aggregationThresholds": [
    {
      "identityColumns": ["user_id"],
      "minimumIdentityCount": 100
    }
  ],
  "comparisonControls": {
    "allowedLiteralComparisonColumns": ["campaign_id", "event_date"]
  }
}
```

Given the preceding configuration, this query is allowed:

```
-- Allowed: campaign_id and event_date are both in allowedLiteralComparisonColumns
SELECT campaign_id, COUNT(DISTINCT user_id) AS reach
FROM impressions
WHERE campaign_id = 'CMP-1024'
  AND event_date >= '2026-01-01'
GROUP BY campaign_id;
```

Given the same configuration, this query is blocked:

```
-- Blocked: user_id is the identity column and can never be compared to a literal
SELECT campaign_id, COUNT(DISTINCT user_id) AS reach
FROM impressions
WHERE user_id = 'U-88231'
GROUP BY campaign_id;
```

The first query still returns only rows backed by at least 100 distinct users, while
the literal comparisons on `campaign_id` and `event_date` filter
which rows are considered. The second query is rejected because it attempts to single out
an individual data subject.

## Column comparison

A column comparison evaluates the value of one column against the value of another
column dynamically for every single row. Syntax examples include:

- WHERE retail\_price < wholesale\_price
- WHERE users.id = orders.user\_id

When using [Minimum aggregation thresholds](custom-min-agg-thresholds.md "custom-min-agg-thresholds.md"), a data provider can allow column
comparison on the `identityColumns` value for use cases that require joining across
tables, such as an audience overlap report.

```
{
  "comparisonControls": {
    "allowedColumnComparisonColumns": [
      "user_id"
    ]
  }
}
```

### Example: Allowing column comparison on the identity column for an overlap report

A publisher and an advertiser want to measure their audience overlap — how many users
appear in both of their datasets — without either party learning who any individual user
is. This requires joining the two tables on `user_id`, which is a
column-to-column comparison. The publisher allows the advertiser to run an audience overlap
analysis scoped to specific campaign IDs.

Because `user_id` is the identity column, the publisher has already blocked
literal comparisons on it (so no one can filter to a specific person). To enable the join
across tables, the publisher adds `user_id` to
`allowedColumnComparisonColumns`. To enable campaign filtering, the publisher
adds `campaign_id` to `allowedLiteralComparisonColumns`.

```
{
  "aggregationThresholds": [
    {
      "identityColumns": ["user_id"],
      "minimumIdentityCount": 100
    }
  ],
  "comparisonControls": {
    "allowedLiteralComparisonColumns": ["campaign_id"],
    "allowedColumnComparisonColumns": ["user_id"]
  }
}
```

Given the preceding configuration, this query is allowed:

```
-- Allowed: user_id is compared against another column (column-to-column join)
SELECT COUNT(DISTINCT p.user_id) AS overlapping_users
FROM publisher_audience p
  JOIN advertiser_audience a
ON p.user_id = a.user_id;
```

Given the same configuration, this query is blocked:

```
-- Blocked: email is not in allowedColumnComparisonColumns
SELECT COUNT(DISTINCT p.user_id) AS overlapping_users
FROM publisher_audience p
  JOIN advertiser_audience a
  ON p.email = a.email;
```

The join succeeds because a column-to-column comparison evaluates dynamically per row
and doesn't let the query runner target a known value. The result enforces the minimum
aggregation threshold, ensuring the overlap count is only returned if it represents at
least 100 distinct users. The second query is blocked because `email` is not in
the `allowedColumnComparisonColumns` allowlist and cannot be used in a
comparison — only `user_id` can.

## Comparison controls and expressions

Comparison controls follow indirect literal comparisons, not only a direct
WHERE `column = 'literal'` predicate. If you allow
`ANY_EXPRESSION` inside aggregate functions through
`allowedAggregateExpressionType`, comparison controls still block a literal
comparison on a column that is not in `allowedLiteralComparisonColumns`. This
applies even when the literal is nested inside an expression.

The following example shows a query that remains blocked because
`zip_code` is not in the allowlist, even though the literal is inside a
CASE expression rather than written as a direct predicate:

```
-- Blocked: zip_code is not in allowedLiteralComparisonColumns,
-- even though the literal comparison is nested inside a CASE expression
SELECT SUM(CASE WHEN zip_code = '00001' THEN salary ELSE 0 END) AS total
FROM employees;
```

This is why the two controls are complementary: allowing expressions inside aggregates
widens what a query can compute, while comparison controls still constrain which columns a
query can single out by value. For more information, see [Allowing nested expressions in aggregate functions](custom-min-agg-thresholds.md#custom-min-agg-nested-expressions "custom-min-agg-thresholds.md#custom-min-agg-nested-expressions").
