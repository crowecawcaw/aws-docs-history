# Custom analysis rule in AWS Clean Rooms

In AWS Clean Rooms, a _custom analysis rule_ is a new type of
analysis rule that allows custom queries to be run on the configured table. Custom SQL queries
are still restricted to having only the SELECT command but can use more SQL
constructs than [aggregation](analysis-rules-aggregation.md#agg-query-controls "analysis-rules-aggregation.md#agg-query-controls") and [list](analysis-rules-list.md#list-query-controls "analysis-rules-list.md#list-query-controls") queries (for example, window functions, OUTER JOIN,
CTEs, or subqueries; see the [AWS Clean Rooms
SQL Reference](../sql-reference/sql-reference.md "../sql-reference/sql-reference.md") for a complete list). Custom SQL queries don’t have to follow a query
structure like [aggregation](analysis-rules-aggregation.md#agg-query-structure-syntax "analysis-rules-aggregation.md#agg-query-structure-syntax") and [list](analysis-rules-list.md#list-query-controls "analysis-rules-list.md#list-query-controls") queries.

The custom analysis rule supports more advanced use cases than those that can be supported
by the aggregation and list analysis rule such as custom attribution analysis, benchmarking,
incrementality analysis, and audience discovery. This is in addition to a superset of the use
cases supported by aggregation and list analysis rule.

The custom analysis rule also supports differential privacy. Differential privacy is a
mathematically-rigorous framework for data privacy protection. For more information, see [AWS Clean Rooms Differential Privacy](differential-privacy.md "differential-privacy.md"). When you create an
analysis template, AWS Clean Rooms Differential Privacy checks the template to determine whether it is
compatible with the general-purpose query structure for AWS Clean Rooms Differential Privacy. This
validation ensures that you don't create an analysis template that isn't allowed with a
differential privacy protected table.

To configure the custom analysis rule, data owners can choose to allow specific custom
queries, stored in [analysis templates](create-analysis-template.md "create-analysis-template.md"), to run on
their configured tables. Data owners review analysis templates before adding them to the allowed
analysis control in the custom analysis rule. Analysis templates are available and visible only
in the collaboration in which they are created (even if the table is associated to other
collaborations) and can be run only by the member who can query in that collaboration.

Alternatively, members can choose to allow other members (query providers) to create queries
without review. Members add query providers’ accounts the allowed query providers control in the
custom analysis rule. If the query provider is the member who can query, they could run any
query directly on the configured table. Query providers could also create queries by [creating analysis templates](create-analysis-template.md "create-analysis-template.md"). Any queries that have
been created by the query providers are automatically allowed to run on the table in all
collaborations in which the AWS account is present and the table is associated.

This page contains the following sections:

- [Custom analysis rule structure](#custom-predefined-structure "#custom-predefined-structure")
- [Custom analysis rule example with analysis templates](#custom-example "#custom-example")
- [Custom analysis rule example with minimum aggregation thresholds](#custom-example-min-agg "#custom-example-min-agg")
- [Custom analysis rule example with minimum aggregation thresholds and comparison controls](#custom-example-min-agg-comparison "#custom-example-min-agg-comparison")
- [Putting it all together](#custom-complete-example "#custom-complete-example")
  The custom analysis rule supports the following privacy-enhancing controls:

- [Allowed analyses](custom-allowed-analyses.md "custom-allowed-analyses.md")
- [Disallowed output columns](disallowed-output-columns.md "disallowed-output-columns.md")
- [Minimum aggregation thresholds](custom-min-agg-thresholds.md "custom-min-agg-thresholds.md")
- [Comparison controls](custom-comparison-controls.md "custom-comparison-controls.md")
- [Custom analysis rule with differential privacy](custom-diff-privacy.md "custom-diff-privacy.md")
- [Considerations and limitations](custom-considerations.md "custom-considerations.md")
- [SQL capabilities for minimum aggregation and comparison controls](custom-sql-capabilities.md "custom-sql-capabilities.md")

## Custom analysis rule structure

The following predefined structure shows the available controls in a custom analysis rule.
Include only the controls you need for your use case. The `userIdentifier` value
in the `differentialPrivacy` control is the column that uniquely identifies your
users, such as _user\_id_. When you have two or more tables with
differential privacy turned on in a collaboration, AWS Clean Rooms requires you to configure the same
column as the user identifier column in both analysis rules. This maintains a consistent
definition of the users across tables.

```
{
  "allowedAnalyses": ["ANY_QUERY"] | string[],
  "allowedAnalysisProviders": [],
  "disallowedOutputColumns": [],
  "aggregationThresholds": [
    {
      "identityColumns": [],
      "minimumIdentityCount": number,
      "type": "COUNT_DISTINCT",
      "allowedAggregateExpressionType": "COLUMNS_ONLY" | "ANY_EXPRESSION",
      "outputColumnThresholds": [
        {
          "outputColumnName": string,
          "minimumIdentityCount": number
        }
      ]
    }
  ],
  "comparisonControls": {
    "allowedLiteralComparisonColumns": [],
    "allowedColumnComparisonColumns": []
  },
  "differentialPrivacy": {
    "columns": [
      {
        "name": "`userIdentifier`"
      }
    ]
  }
}
```

You can either:

- Add analysis template ARNs to allowed analyses control. In this case, the
  `allowedAnalysisProviders` control is not included.

```
{
  allowedAnalyses: string[]
}
```

- Add member AWS account IDs to the `allowedAnalysisProviders` control. In
  this case, you add `ANY_QUERY` to the `allowedAnalyses` control.

```
{
  allowedAnalyses: ["ANY_QUERY"],
  allowedAnalysisProviders: string[]
}
```

You can also configure any of the following controls:

- The columns you do not allow to be projected in the query result. For more
  information, see [Disallowed output columns](disallowed-output-columns.md "disallowed-output-columns.md").

```
{
  disallowedOutputColumns: string[]
}
```

- A minimum aggregation threshold that requires each result row to represent at least a
  minimum number of distinct data subjects. You can override the threshold for individual
  output columns through `outputColumnThresholds`, and
  `allowedAggregateExpressionType` controls whether expressions are permitted
  inside aggregate functions. For more information, see [Minimum aggregation thresholds](custom-min-agg-thresholds.md "custom-min-agg-thresholds.md"), [Overriding the minimum aggregation threshold for specific output columns](custom-min-agg-thresholds.md#custom-min-agg-output-override "custom-min-agg-thresholds.md#custom-min-agg-output-override"), and [Allowing nested expressions in aggregate functions](custom-min-agg-thresholds.md#custom-min-agg-nested-expressions "custom-min-agg-thresholds.md#custom-min-agg-nested-expressions").

```
{
  aggregationThresholds: [
    {
      identityColumns: string[],
      minimumIdentityCount: number,
      type: "COUNT_DISTINCT",
      allowedAggregateExpressionType: "COLUMNS_ONLY" | "ANY_EXPRESSION",
      outputColumnThresholds: [
        {
          outputColumnName: string,
          minimumIdentityCount: number
        }
      ]
    }
  ]
}
```

- Comparison controls that define which columns can be compared to a literal value and
  which can be compared to another column. For more information, see [Comparison controls](custom-comparison-controls.md "custom-comparison-controls.md").

```
{
  comparisonControls: {
    allowedLiteralComparisonColumns: string[],
    allowedColumnComparisonColumns: string[]
  }
}
```

- A differential privacy configuration that protects the table by identifying the
  user identifier column. For more information, see [AWS Clean Rooms Differential Privacy](differential-privacy.md#dp-overview "differential-privacy.md#dp-overview").

```
{
  differentialPrivacy: {
    columns: [
      {
        name: string
      }
    ]
  }
}
```

Configuring minimum aggregation thresholds together with comparison controls is the
recommended configuration. A threshold on its own still leaves low-cardinality or
quasi-identifying columns comparable, which can narrow results in unintended ways.

Comparison controls are worth configuring when your table contains low-cardinality or
quasi-identifying columns — such as postal code or age band — or when the query runner is
not fully trusted. For a worked example that shows both controls configured together, see
[Custom analysis rule example with minimum aggregation thresholds and comparison controls](#custom-example-min-agg-comparison "#custom-example-min-agg-comparison").

## Custom analysis rule example with analysis templates

The following example demonstrates how two companies can collaborate in AWS Clean Rooms using
the custom analysis rule.

Company A has customer and sales data. Company A is interested in understanding the sales
incrementality of an advertising campaign on Company B site. Company B has viewership data and
segment attributes that are useful to Company (for example, the device they used when viewing
the advertising).

Company A has a specific incrementality query they want to run in the collaboration.

To create a collaboration and run a custom analysis in collaboration, the companies do the
following:

1. Company A creates a collaboration and creates a membership. The collaboration has
   Company B as another member on the collaboration. Company A enables query logging in the
   collaboration, and it enables query logging in its account.
2. Company B creates a membership in the collaboration. It enables query logging in its
   account.
3. Company A creates a CRM configured table
4. Company A adds empty custom analysis rule to sales configured table.
5. Company A associates sales configured table to the collaboration.
6. Company B creates viewership configured table.
7. Company B adds an empty custom analysis rule to the viewership configured
   table.
8. Company B associates viewership configured table to the collaboration.
9. Company A views the sales table and viewership table associated to the collaboration
   and creates analysis template, adding the incrementality query and parameter for campaign
   month.

```
{
    "analysisParameters": [
    {
        "defaultValue": ""
        "type": "DATE"
        "name": "campaign_month"
    }
    ],
    "description": "Monthly incrementality query using sales and viewership data"
    "format": "SQL"
    "name": "Incrementality analysis"
    "source":
        "WITH labeleddata AS
        (
        SELECT hashedemail, deviceid, purchases, unitprice, purchasedate,
        CASE
            WHEN testvalue IN ('value1', 'value2', 'value3') THEN 0
            ELSE 1
        END AS testgroup
        FROM viewershipdata
        )
        SELECT labeleddata.purchases, provider.impressions
        FROM labeleddata
        INNER JOIN salesdata
          ON labeleddata.hashedemail = provider.hashedemail
        WHERE MONTH(labeleddata.purchasedate) > :campaignmonth
        AND testgroup = :group
       "
}
```

10. Company A adds their account (for example, 444455556666) to the allowed analysis
    provider control in the custom analysis rule. They use the allowed analysis provider
    control because they want to allow any queries they create to run on their sales
    configured table.

```
{
  "allowedAnalyses": [
    "ANY_QUERY"
  ],
  "allowedAnalysisProviders": [
    "444455556666"
  ]
}
```

11. Company B sees the created analysis template in the collaboration and reviews its
    contents including the query string and parameter.
12. Company B determines that the analysis template achieves the incrementality use case
    and meets their privacy requirements for how their viewership configured table can be
    queried.
13. Company B adds the analysis template ARN to the allowed analysis control in the custom
    analysis rule of the viewership table. They use the allowed analysis control because they
    only want to allow the incrementality query to run on their viewership configured
    table.

```
{
  "allowedAnalyses": [
    "arn:aws:cleanrooms:us-east-1:111122223333:membership/41327cc4-bbf0-43f1-b70c-a160dddceb08/analysistemplate/1ff1bf9d-781c-418d-a6ac-2b80c09d6292"
  ]
}
```

14. Company A runs the analysis template and uses the parameter value
    `05-01-2023`.

## Custom analysis rule example with minimum aggregation thresholds

The following example demonstrates how two companies can collaborate in AWS Clean Rooms using
the custom analysis rule with minimum aggregation thresholds instead of reviewing individual
analysis templates.

Company A is a publisher with an `impressions` table containing
`user_id`, `campaign_id`, and `event_date`. Company B is an
advertiser that wants to measure campaign reach — the number of distinct users who saw a given
campaign. Company A wants to make sure no query result can reveal individuals or small groups,
so it uses minimum aggregation thresholds rather than reviewing individual analysis
templates.

To create a collaboration and run a custom analysis, the companies do the
following:

1. Company A creates a collaboration with Company B as another member and as the member
   who can query. Company A enables query logging in the collaboration and in its
   account.
2. Company B creates a membership in the collaboration and enables query logging in its
   account.
3. Company A creates an `impressions` configured table.
4. Company A adds a custom analysis rule to the `impressions` configured table
   with a minimum aggregation threshold so that every returned row represents at least 100
   distinct users. Company A sets `user_id` as the identity column and overrides the
   threshold to 5 for the lower-sensitivity `campaign_id` output column. Company A
   also allows literal comparison on `campaign_id` and `event_date` so
   that Company B can scope a query to one campaign and a date range. Every column that
   appears in a literal comparison must be in the allowlist. Finally, Company A adds
   Company B's account to the allowed analysis providers control so Company B can run
   queries without per-template review.

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
  ],
  "comparisonControls": {
    "allowedLiteralComparisonColumns": [
      "campaign_id",
      "event_date"
    ]
  },
  "allowedAnalyses": [
    "ANY_QUERY"
  ],
  "allowedAnalysisProviders": [
    "444455556666"
  ]
}
```

5. Company A associates the `impressions` configured table to the
   collaboration.
6. Company B runs a reach query grouped by `event_date` and filtered to a
   campaign:

```
SELECT event_date, COUNT(DISTINCT user_id) AS reach
FROM impressions
WHERE event_date >= '2026-01-01' AND campaign_id = 'Holiday Promotion'
GROUP BY event_date;
```

7. AWS Clean Rooms returns only the rows backed by at least 100 distinct users and suppresses the
   rest, so Company B learns daily reach for the Holiday Promotion campaign without learning
   about any individual or small group.

| `event_date` | `reach` |
| ------------ | ------- |
| 2026-01-01   | 142     |
| 2026-01-02   | 118     |
| 2026-01-04   | 103     |

The date `2026-01-03` does not appear in the results because fewer than
100 distinct users saw the campaign that day, so AWS Clean Rooms suppressed that row.

The key difference from the analysis-templates approach is that Company A never reviewed a
specific query. Instead, Company A relies on the threshold to constrain what any query can
return. For more information, see [Minimum aggregation thresholds](custom-min-agg-thresholds.md "custom-min-agg-thresholds.md") and [Comparison controls](custom-comparison-controls.md "custom-comparison-controls.md").

## Custom analysis rule example with minimum aggregation thresholds and comparison controls

Configuring minimum aggregation thresholds together with comparison controls is the
recommended baseline configuration. A threshold alone ensures that every result row represents
a minimum number of distinct data subjects, but it does not prevent comparisons on
low-cardinality or quasi-identifying columns. Without comparison controls, a query runner can
still filter or join on those columns, potentially narrowing results in unintended ways.

Comparison controls are worth configuring when your table contains low-cardinality or
quasi-identifying columns — such as postal code or age band — or when the query runner is not
fully trusted. Adding comparison controls restricts which columns can appear in literal
comparisons and column-to-column comparisons, closing the gap that a threshold alone leaves
open.

The following configuration combines both controls:

```
{
  "aggregationThresholds": [
    {
      "identityColumns": [
        "user_id"
      ],
      "minimumIdentityCount": 100,
      "type": "COUNT_DISTINCT",
      "allowedAggregateExpressionType": "COLUMNS_ONLY"
    }
  ],
  "comparisonControls": {
    "allowedLiteralComparisonColumns": [
      "campaign_id"
    ],
    "allowedColumnComparisonColumns": [
      "user_id"
    ]
  },
  "allowedAnalyses": [
    "ANY_QUERY"
  ],
  "allowedAnalysisProviders": [
    "444455556666"
  ]
}
```

With this configuration, every result row represents at least 100 distinct data subjects.
The query runner can filter by `campaign_id` using literal comparisons and join on
`user_id` using column-to-column comparisons. Because the comparison allowlists are
set, any column not listed — including low-cardinality columns such as postal code or age
band — cannot be used in a comparison at all.

For more information about each control, see [Minimum aggregation thresholds](custom-min-agg-thresholds.md "custom-min-agg-thresholds.md") and [Comparison controls](custom-comparison-controls.md "custom-comparison-controls.md"). For a fuller configuration that also includes
disallowed output columns, see [Putting it all together](#custom-complete-example "#custom-complete-example").

## Putting it all together

The following example shows a complete configuration of the custom analysis rule type,
using disallowed output columns, minimum aggregation thresholds, and comparison controls.
This configuration enforces minimum aggregation of 100 distinct data subjects, prevents
`user_id` from being projected in the query result, and allows the query runner to
analyze the intersection of customers joining on the `user_id` column.

This policy also grants additional flexibility by allowing literal comparison filtering on
low-sensitivity columns `status` and `price`, and overrides the minimum
aggregation threshold to 5 for the `campaign_id` column:

```
{
  "disallowedOutputColumns": [
    "user_id"
  ],
  "comparisonControls": {
    "allowedLiteralComparisonColumns": [
      "status",
      "price"
    ],
    "allowedColumnComparisonColumns": [
      "user_id"
    ]
  },
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
  ],
  "allowedAnalyses": [
    "ANY_QUERY"
  ],
  "allowedAnalysisProviders": [
    "444455556666",
    "333366669999"
  ]
}
```
