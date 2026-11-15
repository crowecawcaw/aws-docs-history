

# Minimum aggregation thresholds
<a name="custom-min-agg-thresholds"></a>

Data aggregation is a privacy-enhancing technique that helps enforce anonymization by preventing queries from returning results about individuals or small groups. When minimum aggregation thresholds are configured on your tables, AWS Clean Rooms suppresses results that do not meet the data provider's specified minimum threshold.

**Topics**
+ [Aggregation thresholds](#custom-min-agg-aggregation-thresholds)
+ [Qualifying aggregate functions](#custom-min-agg-qualifying-functions)
+ [Overriding the minimum aggregation threshold for specific output columns](#custom-min-agg-output-override)
+ [Allowing nested expressions in aggregate functions](#custom-min-agg-nested-expressions)
+ [Using MIN, MAX, and percentile functions](#custom-min-agg-value-selecting)
+ [Configuring minimum aggregation thresholds in the console](#custom-min-agg-console)
+ [LEFT SEMI JOIN and LEFT ANTI JOIN](#custom-min-agg-semi-anti-joins)
+ [Considerations and limitations](#custom-min-agg-considerations)

## Aggregation thresholds
<a name="custom-min-agg-aggregation-thresholds"></a>

You can configure minimum aggregation thresholds in a Custom analysis rule for your configured table. Data providers specify the `identityColumns` and the `minimumIdentityCount`, N. Supported values for `minimumIdentityCount` are between 2 and 100,000. The `identityColumns` value must be a `string`, `varchar`, or `char` type. Minimum aggregation thresholds ensure that each row in a SQL query result has at least N distinct data subjects contributing to it. For information about how `identityColumns` interacts with query filters, see [Comparison controls](custom-comparison-controls.md).

The following example sets the minimum aggregation threshold to 100 with `user_id` as the `identityColumns` value:

```
{
  "aggregationThresholds": [
    {
      "identityColumns": [
        "user_id"
      ],
      "minimumIdentityCount": 100,
      "type": "COUNT_DISTINCT"
    }
  ]
}
```

## Qualifying aggregate functions
<a name="custom-min-agg-qualifying-functions"></a>

When minimum aggregation thresholds apply, your query must include at least one qualifying aggregation. A SELECT that aggregates data is a qualifying aggregation only if every aggregate function in that SELECT is a qualifying aggregate function. If your query has no qualifying aggregation, it fails with the error `Data must be aggregated before being included in the query output`.

The following table lists which aggregate functions are qualifying aggregate functions.


| Aggregate functions | Qualifying aggregate function | 
| --- |--- |
| AVG, COUNT, COUNT DISTINCT, APPROX\_COUNT\_DISTINCT, SUM, STDDEV / STDDEV\_SAMP, STDDEV\_POP, VAR\_SAMP / VARIANCE, VAR\_POP, SKEWNESS | Yes | 
| MIN, MAX, PERCENTILE, APPROX\_PERCENTILE, MEDIAN | Only if the function's value doesn't reach an output column. For more information, see [Using MIN, MAX, and percentile functions](#custom-min-agg-value-selecting). | 
| COLLECT\_LIST, COLLECT\_SET | No | 

For the aggregate functions and other SQL constructs that you can use when minimum aggregation thresholds apply, see [SQL capabilities for minimum aggregation and comparison controls](custom-sql-capabilities.md).

## Overriding the minimum aggregation threshold for specific output columns
<a name="custom-min-agg-output-override"></a>

Output columns have different sensitivity levels, and data providers can enforce different `minimumIdentityCount` values depending on the output column. For example, `campaign_id` might be a low-sensitivity column with a minimum threshold of 5 distinct data subjects, while `postal_code` and `income_bracket` get a minimum threshold of 100 because they are high-sensitivity columns.

A per-column override accepts `0`, which exempts that output column from minimum aggregation, or a value between 2 and 100,000.

The following example sets a minimum aggregation threshold override for the `campaign_id` column:

```
{
  "outputColumnThresholds": [
    {
      "outputColumnName": "campaign_id",
      "minimumIdentityCount": 5
    }
  ]
}
```

## Allowing nested expressions in aggregate functions
<a name="custom-min-agg-nested-expressions"></a>

Allowing expressions inside aggregation functions increases the risk that data subjects can be re-identified in clean room queries. The default setting for `allowedAggregateExpressionType` is `COLUMNS_ONLY`, which is recommended as the privacy-enhanced configuration. With this setting, only columns are accepted inside an aggregation function, such as:
+ SUM(cost)
+ COUNT(DISTINCT campaign\_id)

Alternatively, for collaborations where the query runner is a trusted partner, you can allow `ANY_EXPRESSION` inside an aggregation function. This setting increases the flexibility of SQL queries that can run on your data, but introduces privacy risk because query runners can isolate small groups within an aggregation function.

**Privacy and compliance review required**  
Before allowing `ANY_EXPRESSION` inside aggregate functions, consult your privacy, security, legal, and compliance teams to make sure that this adheres to your organization's requirements.

The following is an example of an expression in an aggregation function that is generally considered safe:
+ SUM(cost \* quantity)

The following is an example of an expression in an aggregation function that is considered a privacy risk:
+ SUM(CASE WHEN zip\_code = '10001' THEN salary ELSE 0 END)

The following is a complete `aggregationThresholds` example:

```
{
  "aggregationThresholds": [
    {
      "identityColumns": [
        "user_id"
      ],
      "minimumIdentityCount": 100,
      "type": "COUNT_DISTINCT",
      "allowedAggregateExpressionType": "COLUMNS_ONLY",
      "outputColumnThresholds": [
        {
          "outputColumnName": "campaign_id",
          "minimumIdentityCount": 5
        }
      ]
    }
  ]
}
```

## Using MIN, MAX, and percentile functions
<a name="custom-min-agg-value-selecting"></a>

MIN, MAX, PERCENTILE, APPROX\_PERCENTILE, and MEDIAN return a single value taken from one input row. When minimum aggregation thresholds apply, they're qualifying aggregate functions only if that value can't reach an output column. For the full list of qualifying aggregate functions, see [Qualifying aggregate functions](#custom-min-agg-qualifying-functions).

The value reaches an output column if you return it directly, transform it (for example, with CAST, COALESCE, CONCAT, or arithmetic), or return it as a result branch of an IF or CASE expression. In that case, the SELECT isn't a qualifying aggregation, even if it also uses qualifying aggregate functions.

You can't run the following SQL queries:

```
-- Blocked: each SELECT returns a MIN or MAX value. Other aggregate functions,
-- such as SUM or COUNT, in the same SELECT don't make it qualify.
SELECT campaign_id, MIN(price) AS cheapest, SUM(spend) AS total_spend
FROM sales
GROUP BY campaign_id

SELECT campaign_id, CAST(MAX(event_time) AS STRING) AS latest_event, COUNT(*) AS events
FROM events
GROUP BY campaign_id

SELECT campaign_id, IF(SUM(spend) > 0, MAX(amount), 0) AS top_amount
FROM sales
GROUP BY campaign_id
```

If you use the value only in a comparison, in the condition of an IF or CASE expression, in a HAVING clause, or in a join condition, it doesn't reach the output and these functions qualify. You can run the following SQL queries:

```
-- Allowed: you use the MAX value only in a comparison or a HAVING clause,
-- so it never reaches the output.
SELECT campaign_id, MAX(age) > 21 AS has_adult
FROM users
GROUP BY campaign_id

SELECT campaign_id, SUM(spend) AS total_spend
FROM sales
GROUP BY campaign_id
HAVING MAX(spend) > 1000
```

You can also compute MIN or MAX in a subquery or common table expression (CTE), and then aggregate the result in an outer SELECT that uses only qualifying aggregate functions. The inner SELECT isn't a qualifying aggregation, but the outer SELECT is, so you can run the query:

```
-- Allowed: the outer SELECT uses only SUM, so it's a qualifying aggregation.
WITH per_household AS (
  SELECT campaign_id, household_id, MAX(spend) AS max_spend
  FROM sales
  GROUP BY campaign_id, household_id
)
SELECT campaign_id, SUM(max_spend) AS total_max_spend
FROM per_household
GROUP BY campaign_id
```

## Configuring minimum aggregation thresholds in the console
<a name="custom-min-agg-console"></a>

You configure minimum aggregation thresholds as part of adding a custom analysis rule to a configured table, after the configured table exists. For the complete custom analysis rule guided flow, see [Adding a custom analysis rule to a table (guided flow)](add-analysis-rule.md#add-custom-analysis-rule-wizard).

**To configure minimum aggregation thresholds**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Tables**, and then choose your configured table.

1. On the configured table detail page, choose **Configure analysis rule**.

1. For **Analysis rule type**, choose **Custom**.

1. Choose either **Review each new analysis** or **Allow any analysis by specific collaborators**. The remaining steps follow the **Allow any analysis by specific collaborators** path.

1. Choose **Add AWS account** to configure which partners can submit analyses on this configured table, then choose the AWS account to allow.

1. On **Specify analysis results controls - optional**, for **Enforce aggregation thresholds?**, choose **Yes**.

1. Configure the minimum aggregation threshold.

   1. Choose your identity column. The identity column must be a `string`, `varchar`, or `char` type.

   1. Specify your minimum identity count. Supported values are between 2 and 100,000.

   1. **Aggregate type** is preconfigured to **Count distinct**.

1. For **Allow nested expressions in aggregate functions?**, the default is **No**. Leaving this option turned off is the privacy-enhanced configuration. For more information, see [Allowing nested expressions in aggregate functions](#custom-min-agg-nested-expressions).

1. (Optional) Configure output column overrides.

   1. Choose **Add column override**.

   1. Choose your output column from the dropdown list.

   1. Specify your minimum identity count. Supported values are `0` to exempt the column from minimum aggregation, or between 2 and 100,000.

   For more information, see [Overriding the minimum aggregation threshold for specific output columns](#custom-min-agg-output-override).

1. (Recommended) Configure columns allowed for comparison.

   1. By default, all columns are eligible for comparison. Explicitly configuring which columns are allowed for literal and column-to-column comparison is the privacy-enhanced configuration.

   1. Choose **Custom list**.

   1. Choose which columns are allowed for literal comparison. For example, allowing the `state` column lets the query runner run a query with a literal filter, such as `WHERE state = 'New York'`.

   1. Choose which columns can be used for column-to-column comparison. For example, allowing the `state` column lets the query runner run a cross-table join with a column comparison, such as `JOIN my_table t ON t.state = partner_table.state`.

   For more information, see [Comparison controls](custom-comparison-controls.md).

1. Choose **Next**.

1. Choose **Next**. Differential privacy is turned off and is not supported with minimum aggregation thresholds or comparison controls. For more information, see [Limitations](custom-considerations.md#custom-limitations).

1. Review your custom analysis rule configuration.

1. Choose **Configure analysis rule**.

1. Associate the configured table to a collaboration. For more information, see [Step 2: Associate a configured table](associate-configured-table.md#associate-config-table).

## LEFT SEMI JOIN and LEFT ANTI JOIN
<a name="custom-min-agg-semi-anti-joins"></a>

A LEFT SEMI JOIN returns the rows of the left table that have a match in the right table. AWS Clean Rooms applies minimum aggregation thresholds to the right table of a LEFT SEMI JOIN, as it does for an INNER JOIN.

To get the results you expect, use only equality conditions between columns in the ON condition, and filter the right table in a subquery. If the ON condition contains other comparisons, such as a range comparison, OR, or a condition on the right table, the threshold can remove more rows than expected. A query that doesn't aggregate its results can also be rejected.

```
-- Can return fewer rows than expected
SELECT s.region, COUNT(*) AS stores
FROM stores s
LEFT SEMI JOIN partner_purchases p
  ON s.region = p.region AND p.amount > 5
GROUP BY s.region;

-- Recommended: filter the right table first
SELECT s.region, COUNT(*) AS stores
FROM stores s
LEFT SEMI JOIN (SELECT region FROM partner_purchases WHERE amount > 5) p
  ON s.region = p.region
GROUP BY s.region;
```

AWS Clean Rooms rejects a LEFT ANTI JOIN when its right side uses a column that is protected by a minimum aggregation threshold. This includes a column that the right side uses in the ON condition, in a filter, join, expression, grouping, or ordering, and a table that only filters the right side, for example through a LEFT SEMI JOIN or an IN subquery. A LEFT ANTI JOIN returns the rows of the left table that have no match in the right table, so no data subject from the right table contributes to the result. A minimum aggregation threshold can't protect the right table in this case, because the result reveals which values are absent from it.

The following query is rejected because the right side of the LEFT ANTI JOIN uses `user_id` from `partner_purchases`, which is protected by a minimum aggregation threshold:

```
-- Rejected: partner_purchases.user_id is protected by a minimum aggregation threshold
SELECT a.campaign, COUNT(*) AS non_converters
FROM ad_exposures a
LEFT ANTI JOIN partner_purchases p
  ON a.user_id = p.user_id
GROUP BY a.campaign;
```

The query fails with the following error:

```
LEFT ANTI JOIN isn't supported when the right side of the join uses columns protected by an aggregation threshold: 'user_id'. Remove the LEFT ANTI JOIN, or remove these columns, or the tables they come from, from its right side.
```

A LEFT ANTI JOIN is allowed in the following cases:
+ The right side uses only columns whose minimum aggregation threshold is overridden to `0`. For more information, see [Overriding the minimum aggregation threshold for specific output columns](#custom-min-agg-output-override).
+ The right side doesn't use any protected column.
+ Only the left table is protected by a minimum aggregation threshold. The threshold of the left table applies to the result.

## Considerations and limitations
<a name="custom-min-agg-considerations"></a>

Considerations and limitations apply when you use minimum aggregation thresholds. For the full list, see [Considerations and limitations](custom-considerations.md).