

# Semantic search for AWS Glue Data Catalog
<a name="catalog-semantic-search"></a>

**Note**  
Business context and semantic search is in preview for AWS Glue and is subject to change.

Semantic search enables you to discover data assets by meaning in addition to exact keyword matching. Results are ranked by semantic similarity to your query. You can narrow results using filters on asset type, metadata fields, and glossary terms.

## Using the SearchAssets API
<a name="catalog-semantic-search-api"></a>

The `SearchAssets` API accepts `SearchText`, `FilterClause`, or both. When neither is provided, it returns all assets. Optional parameters: `Sort`, `MaxResults`, `NextToken`.

### Text search
<a name="catalog-semantic-search-text"></a>

```
aws glue search-assets \
    --search-text "customer purchases"
```

Example output:

```
{
    "Items": [
        {"Id": "c9vq7sh2fk4t2h", "AssetName": "Customer Sales Transactions", "AssetTypeId": "Table"}
    ]
}
```

Limit results with `--max-results`:

```
aws glue search-assets \
    --search-text "quarterly revenue" \
    --max-results 5
```

### Filtering search results
<a name="catalog-semantic-search-filters"></a>

Use `FilterClause` to narrow results. Supported filter types:
+ **AttributeFilter** – Operators: `equals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `notExists`.
+ **AndAllFilters** – All filters must match (logical AND).
+ **OrAnyFilters** – At least one must match (logical OR).

**To filter by a single attribute**  
Filter to table assets only:

```
aws glue search-assets \
    --search-text "revenue" \
    --filter-clause '{
        "AttributeFilter": {
            "Attribute": "type",
            "Operator": "equals",
            "Value": {"StringValue": "Table"}
        }
    }'
```

**To combine filters with AND logic**  
Find table assets updated after a timestamp:

```
aws glue search-assets \
    --search-text "customer data" \
    --filter-clause '{
        "AndAllFilters": [
            {"AttributeFilter": {"Attribute": "type", "Operator": "equals", "Value": {"StringValue": "Table"}}},
            {"AttributeFilter": {"Attribute": "updatedAt", "Operator": "greaterThan", "Value": {"LongValue": 1718400000}}}
        ]
    }'
```

**To combine filters with OR logic**  
Search for tables or skill assets:

```
aws glue search-assets \
    --search-text "customer data" \
    --filter-clause '{
        "OrAnyFilters": [
            {"AttributeFilter": {"Attribute": "type", "Operator": "equals", "Value": {"StringValue": "Table"}}},
            {"AttributeFilter": {"Attribute": "type", "Operator": "equals", "Value": {"StringValue": "Skill"}}}
        ]
    }'
```

**To filter by glossary term**  
Filter to assets tagged with a specific glossary term (by term ID):

```
aws glue search-assets \
    --search-text "financial data" \
    --filter-clause '{
        "AttributeFilter": {
            "Attribute": "glossaryTerms",
            "Operator": "equals",
            "Value": {"StringValue": "{{glossary-term-id}}"}
        }
    }'
```

**To use nested AND and OR filters**  
Find table or skill assets with a specific glossary term:

```
aws glue search-assets \
    --search-text "customer" \
    --filter-clause '{
        "AndAllFilters": [
            {"OrAnyFilters": [
                {"AttributeFilter": {"Attribute": "type", "Operator": "equals", "Value": {"StringValue": "Table"}}},
                {"AttributeFilter": {"Attribute": "type", "Operator": "equals", "Value": {"StringValue": "Skill"}}}
            ]},
            {"AttributeFilter": {"Attribute": "glossaryTerms", "Operator": "equals", "Value": {"StringValue": "{{glossary-term-id}}"}}}
        ]
    }'
```

### Sorting search results
<a name="catalog-semantic-search-sort"></a>

By default, results are sorted by semantic relevance. To sort by attribute:

```
aws glue search-assets \
    --search-text "customer purchases" \
    --sort '{"Attribute": "assetName", "Order": "ASCENDING"}'
```

```
aws glue search-assets \
    --search-text "customer purchases" \
    --sort '{"Attribute": "updatedAt", "Order": "DESCENDING"}'
```

**Note**  
When you specify a sort attribute, results are ordered by that attribute rather than by semantic relevance.

### Paginating search results
<a name="catalog-semantic-search-pagination"></a>

When results exceed `MaxResults`, the response includes a `NextToken`. Use it to retrieve additional pages.

```
aws glue search-assets \
    --search-text "customer data" \
    --max-results 10 \
    --next-token "eyJsYXN0RXZhbHVhdGVkS2V5Ijp7ImlkIjp7InMiOiJhMWIyYzNkNCJ9fX0="
```

Continue until the response no longer includes a `NextToken`.

## Running filter-only queries
<a name="catalog-semantic-search-filter-only"></a>

Use only `FilterClause` without `SearchText` to list assets without semantic ranking.

```
aws glue search-assets \
    --filter-clause '{"AttributeFilter": {"Attribute": "type", "Operator": "equals", "Value": {"StringValue": "Table"}}}' \
    --max-results 20
```

**Note**  
When you omit both `SearchText` and `FilterClause`, the API returns all assets.

## Examples
<a name="catalog-semantic-search-examples"></a>

**To discover skill assets for a domain**  
Find skill assets related to sales data:

```
aws glue search-assets \
    --search-text "sales domain usage rules" \
    --filter-clause '{"AttributeFilter": {"Attribute": "type", "Operator": "equals", "Value": {"StringValue": "Skill"}}}'
```

**Note**  
This query returns only custom skill assets. Managed skills are not returned by the `SearchAssets` API.

**To combine text search and sorting**  
Get a comprehensive view of matching assets:

```
aws glue search-assets \
    --search-text "customer" \
    --sort '{"Attribute": "updatedAt", "Order": "DESCENDING"}' \
    --max-results 10
```