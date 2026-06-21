# Semantic search for AWS Glue Data Catalog

###### Note

Business context and semantic search is in preview for AWS Glue and is subject
to change.

Semantic search enables you to discover data assets by meaning in addition
to exact keyword matching. Results are ranked by semantic similarity to your query. You
can narrow results using filters on asset type, metadata fields, and glossary terms.

## Using the Search API

The `Search` API requires at least one of `SearchText` or
`FilterClause`. Optional parameters: `Sort`,
`Aggregations`, `MaxResults`, `NextToken`.

### Text search

```
aws glue search \
    --search-text "customer purchases"
```

Example output:

```
{
    "Items": [
        {"Id": "c9vq7sh2fk4t2h", "AssetName": "Customer Sales Transactions", "AssetTypeId": "glue-table"}
    ],
    "TotalCount": 2
}
```

Limit results with `--max-results`:

```
aws glue search \
    --search-text "quarterly revenue" \
    --max-results 5
```

### Filtering search results

Use `FilterClause` to narrow results. Supported filter types:

- **AttributeFilter** – Operators:
  `equals`, `greaterThan`, `greaterThanOrEquals`,
  `lessThan`, `lessThanOrEquals`, `notExists`.
- **MapFilter** – Filters on a map
  attribute's key-value pair.
- **AndAllFilters** – All filters must
  match (logical AND).
- **OrAnyFilters** – At least one must
  match (logical OR).

###### To filter by a single attribute

Filter to table assets only:

```
aws glue search \
    --search-text "revenue" \
    --filter-clause '{
        "AttributeFilter": {
            "Attribute": "assetTypeId",
            "Operator": "equals",
            "Value": {"StringValue": "glue-table"}
        }
    }'
```

###### To combine filters with AND logic

Find table assets updated after a timestamp:

```
aws glue search \
    --search-text "customer data" \
    --filter-clause '{
        "AndAllFilters": [
            {"AttributeFilter": {"Attribute": "assetTypeId", "Operator": "equals", "Value": {"StringValue": "glue-table"}}},
            {"AttributeFilter": {"Attribute": "updatedAt", "Operator": "greaterThan", "Value": {"LongValue": 1718400000}}}
        ]
    }'
```

###### To combine filters with OR logic

Search for tables or views:

```
aws glue search \
    --search-text "customer data" \
    --filter-clause '{
        "OrAnyFilters": [
            {"AttributeFilter": {"Attribute": "assetTypeId", "Operator": "equals", "Value": {"StringValue": "glue-table"}}},
            {"AttributeFilter": {"Attribute": "assetTypeId", "Operator": "equals", "Value": {"StringValue": "glue-view"}}}
        ]
    }'
```

###### To filter by a map attribute

Filter by glossary term key-value pair:

```
aws glue search \
    --search-text "financial data" \
    --filter-clause '{
        "MapFilter": {
            "Attribute": "glossaryTerms",
            "Key": "classification",
            "Value": {"StringValue": "PII"}
        }
    }'
```

###### To use nested AND and OR filters

Find table or view assets with a specific glossary term:

```
aws glue search \
    --search-text "customer" \
    --filter-clause '{
        "AndAllFilters": [
            {"OrAnyFilters": [
                {"AttributeFilter": {"Attribute": "assetTypeId", "Operator": "equals", "Value": {"StringValue": "glue-table"}}},
                {"AttributeFilter": {"Attribute": "assetTypeId", "Operator": "equals", "Value": {"StringValue": "glue-view"}}}
            ]},
            {"MapFilter": {"Attribute": "glossaryTerms", "Key": "term", "Value": {"StringValue": "Revenue"}}}
        ]
    }'
```

### Sorting search results

By default, results are sorted by semantic relevance. To sort by attribute:

```
aws glue search \
    --search-text "customer purchases" \
    --sort '{"Attribute": "assetName", "Order": "ASCENDING"}'
```

```
aws glue search \
    --search-text "customer purchases" \
    --sort '{"Attribute": "updatedAt", "Order": "DESCENDING"}'
```

###### Note

When you specify a sort attribute, results are ordered by that attribute
rather than by semantic relevance.

### Computing aggregations

Use `Aggregations` to compute counts grouped by attribute values.

```
aws glue search \
    --search-text "customer data" \
    --aggregations '[{"Attribute": "assetTypeId"}]'
```

Example output:

```
{
    "TotalCount": 15,
    "Aggregations": [
        {"Attribute": "assetTypeId", "Items": [
            {"Value": "glue-table", "Count": 10},
            {"Value": "glue-view", "Count": 3}
        ]}
    ]
}
```

Request multiple aggregations in a single call:

```
aws glue search \
    --search-text "financial data" \
    --aggregations '[{"Attribute": "assetTypeId"}, {"Attribute": "glossaryTerms"}]'
```

### Paginating search results

When results exceed `MaxResults`, the response includes a
`NextToken`. Use it to retrieve additional pages.

```
aws glue search \
    --search-text "customer data" \
    --max-results 10 \
    --next-token "eyJsYXN0RXZhbHVhdGVkS2V5Ijp7ImlkIjp7InMiOiJhMWIyYzNkNCJ9fX0="
```

Continue until the response no longer includes a `NextToken`.

## Running filter-only queries

Use only `FilterClause` without `SearchText` to list assets
without semantic ranking.

```
aws glue search \
    --filter-clause '{"AttributeFilter": {"Attribute": "assetTypeId", "Operator": "equals", "Value": {"StringValue": "glue-table"}}}' \
    --max-results 20
```

###### Note

You must provide at least one of `SearchText` or
`FilterClause`.

## Examples

###### To discover skill assets for a domain

Find skill assets related to sales data:

```
aws glue search \
    --search-text "sales domain usage rules" \
    --filter-clause '{"AttributeFilter": {"Attribute": "assetTypeId", "Operator": "equals", "Value": {"StringValue": "skill-asset"}}}'
```

###### Note

This query returns only custom skill assets. Managed skills are not
returned by the Search API.

###### To combine text search, aggregations, and sorting

Get a comprehensive view of matching assets:

```
aws glue search \
    --search-text "customer" \
    --aggregations '[{"Attribute": "assetTypeId"}]' \
    --sort '{"Attribute": "updatedAt", "Order": "DESCENDING"}' \
    --max-results 10
```
