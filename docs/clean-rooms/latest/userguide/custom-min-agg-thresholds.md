# Minimum aggregation thresholds

Data aggregation is a privacy-enhancing technique that helps enforce anonymization by
preventing queries from returning results about individuals or small groups. When minimum
aggregation thresholds are configured on your tables, AWS Clean Rooms suppresses results that do not
meet the data provider's specified minimum threshold.

###### Topics

- [Aggregation thresholds](#custom-min-agg-aggregation-thresholds "#custom-min-agg-aggregation-thresholds")
- [Overriding the minimum aggregation threshold for specific output columns](#custom-min-agg-output-override "#custom-min-agg-output-override")
- [Allowing nested expressions in aggregate functions](#custom-min-agg-nested-expressions "#custom-min-agg-nested-expressions")
- [Configuring minimum aggregation thresholds in the console](#custom-min-agg-console "#custom-min-agg-console")
- [Considerations and limitations](#custom-min-agg-considerations "#custom-min-agg-considerations")

## Aggregation thresholds

You can configure minimum aggregation thresholds in a Custom analysis rule for your
configured table. Data providers specify the `identityColumns` and the
`minimumIdentityCount`, N. Supported values for
`minimumIdentityCount` are between 2 and 100,000. The
`identityColumns` value must be a `string`, `varchar`, or
`char` type. Minimum aggregation thresholds
ensure that each row in a SQL query result has at least N distinct data subjects contributing
to it. For information about how `identityColumns` interacts with query filters,
see [Comparison controls](custom-comparison-controls.md "custom-comparison-controls.md").

The following example sets the minimum aggregation threshold to 100 with
`user_id` as the `identityColumns` value:

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

## Overriding the minimum aggregation threshold for specific output columns

Output columns have different sensitivity levels, and data providers can enforce
different `minimumIdentityCount` values depending on the output column. For
example, `campaign_id` might be a low-sensitivity column with a minimum
threshold of 5 distinct data subjects, while `postal_code` and
`income_bracket` get a minimum threshold of 100 because they are
high-sensitivity columns.

A per-column override accepts `0`, which exempts that output column from
minimum aggregation, or a value between 2 and 100,000.

The following example sets a minimum aggregation threshold override for the
`campaign_id` column:

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

Allowing expressions inside aggregation functions increases the risk that data
subjects can be re-identified in clean room queries. The default setting for
`allowedAggregateExpressionType` is `COLUMNS_ONLY`, which is
recommended as the privacy-enhanced configuration. With this setting, only columns are
accepted inside an aggregation function, such as:

- SUM(cost)
- COUNT(DISTINCT campaign\_id)

Alternatively, for collaborations where the query runner is a trusted partner, you
can allow `ANY_EXPRESSION` inside an aggregation function. This setting
increases the flexibility of SQL queries that can run on your data, but introduces
privacy risk because query runners can isolate small groups within an aggregation
function.

###### Privacy and compliance review required

Before allowing `ANY_EXPRESSION` inside aggregate functions, consult your
privacy, security, legal, and compliance teams to make sure that this adheres to your
organization's requirements.

The following is an example of an expression in an aggregation function that is
generally considered safe:

- SUM(cost \* quantity)

The following is an example of an expression in an aggregation function that is
considered a privacy risk:

- SUM(CASE WHEN zip\_code = '10001'
  THEN salary ELSE 0 END)

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

## Configuring minimum aggregation thresholds in the console

You configure minimum aggregation thresholds as part of adding a custom analysis rule
to a configured table, after the configured table exists. For the complete custom analysis
rule guided flow, see [Adding a custom analysis rule to a table (guided flow)](add-analysis-rule.md#add-custom-analysis-rule-wizard "add-analysis-rule.md#add-custom-analysis-rule-wizard").

###### To configure minimum aggregation thresholds

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Tables**, and then choose
   your configured table.
3. On the configured table detail page, choose **Configure analysis
   rule**.
4. For **Analysis rule type**, choose
   **Custom**.
5. Choose either **Review each new analysis** or **Allow any
   analysis by specific collaborators**. The remaining steps follow the
   **Allow any analysis by specific collaborators** path.
6. Choose **Add AWS account** to configure which partners can submit
   analyses on this configured table, then choose the AWS account to allow.
7. On **Specify analysis results controls - optional**, for
   **Enforce aggregation thresholds?**, choose
   **Yes**.
8. Configure the minimum aggregation threshold.

   1. Choose your identity column. The identity column must be a
      `string`, `varchar`, or `char` type.
   2. Specify your minimum identity count. Supported values are between 2 and
      100,000.
   3. **Aggregate type** is preconfigured to **Count
      distinct**.

9. For **Allow nested expressions in aggregate functions?**, the
   default is **No**. Leaving this option turned off is the
   privacy-enhanced configuration. For more information, see [Allowing nested expressions in aggregate functions](#custom-min-agg-nested-expressions "#custom-min-agg-nested-expressions").
10. (Optional) Configure output column overrides.

    1. Choose **Add column override**.
    2. Choose your output column from the dropdown list.
    3. Specify your minimum identity count. Supported values are `0` to
       exempt the column from minimum aggregation, or between 2 and 100,000.For more information, see [Overriding the minimum aggregation threshold for specific output columns](#custom-min-agg-output-override "#custom-min-agg-output-override").

11. (Recommended) Configure columns allowed for comparison.

    1. By default, all columns are eligible for comparison. Explicitly configuring
       which columns are allowed for literal and column-to-column comparison is the
       privacy-enhanced configuration.
    2. Choose **Custom list**.
    3. Choose which columns are allowed for literal comparison. For example, allowing
       the `state` column lets the query runner run a query with a literal
       filter, such as `WHERE state = 'New York'`.
    4. Choose which columns can be used for column-to-column comparison. For example,
       allowing the `state` column lets the query runner run a cross-table join
       with a column comparison, such as `JOIN my_table t
 ON t.state = partner_table.state`.For more information, see [Comparison controls](custom-comparison-controls.md "custom-comparison-controls.md").

12. Choose **Next**.
13. Choose **Next**. Differential privacy is turned off and is not
    supported with minimum aggregation thresholds or comparison controls. For more
    information, see [Limitations](custom-considerations.md#custom-limitations "custom-considerations.md#custom-limitations").
14. Review your custom analysis rule configuration.
15. Choose **Configure analysis rule**.
16. Associate the configured table to a collaboration. For more information, see [Step 2: Associate a configured table](associate-configured-table.md#associate-config-table "associate-configured-table.md#associate-config-table").

## Considerations and limitations

Considerations and limitations apply when you use minimum aggregation thresholds. For
the full list, see [Considerations and limitations](custom-considerations.md "custom-considerations.md").
