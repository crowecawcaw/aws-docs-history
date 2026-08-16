# Allowed analyses

The `allowedAnalyses` control in the custom analysis rule lets you allow
specific custom queries, stored in analysis templates, to run on your configured table. You
review analysis templates before adding them to this control. For more information about
analysis templates, see [Analysis templates in AWS Clean Rooms](create-analysis-template.md "create-analysis-template.md").

Analysis templates are collaboration-specific and visible only in the collaboration where
they are created. Only the member who can query in that collaboration can run analysis
templates.

You can allow analysis templates or accounts to create queries, not both. If you leave the
`allowedAnalyses` control empty, the member who can query cannot run queries on the
configured table.

To allow any query without reviewing individual templates, set `allowedAnalyses`
to `["ANY_QUERY"]` and use the `allowedAnalysisProviders` control
together. For more information, see [Allowed
analysis providers](#custom-allowed-analysis-providers "#custom-allowed-analysis-providers").

The following example adds an analysis template ARN to the `allowedAnalyses`
control:

```
{
  "allowedAnalyses": [
    "arn:aws:cleanrooms:us-east-1:111122223333:membership/41327cc4-bbf0-43f1-b70c-a160dddceb08/analysistemplate/1ff1bf9d-781c-418d-a6ac-2b80c09d6292"
  ]
}
```

## Allowed analysis providers

Instead of reviewing individual analysis templates, you can allow other members (query
providers) to create queries without review. You add the query providers' AWS account IDs to
the `allowedAnalysisProviders` control. When you use this control, set
`allowedAnalyses` to `["ANY_QUERY"]`.

If the query provider is the member who can query, they can run any query directly on the
configured table. Query providers can also create analysis templates.

AWS Clean Rooms automatically allows any query that an allowed query provider creates to run on the
table in all collaborations where that AWS account is present and the table is
associated.

###### Scope of allowed analysis providers

Allowing analysis providers is more permissive than reviewing templates individually.
When you add a query provider, all current and future queries from that AWS account are
allowed to run on your configured table. For finer control, use
`allowedAnalyses` with specific analysis template ARNs instead.

The following example adds a query provider AWS account ID to the
`allowedAnalysisProviders` control:

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

## Minimum aggregation thresholds with analysis templates

AWS Clean Rooms enforces minimum aggregation thresholds on queries that run from analysis
templates, not only on queries submitted directly by allowed analysis providers. If you
configure a minimum aggregation threshold on your configured table and also allow specific
analysis templates, AWS Clean Rooms still suppresses any result row that does not meet the
threshold.

This provides an additional guardrail. Reviewing an analysis template tells you what a
query is allowed to do. The minimum aggregation threshold independently constrains what any
allowed query can return. The two controls work together, so you do not have to rely on
template review alone to prevent results about individuals or small groups.

For more information, see [Minimum aggregation thresholds](custom-min-agg-thresholds.md "custom-min-agg-thresholds.md").
