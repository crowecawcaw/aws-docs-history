# Schema unnesting

When integrating with analytics services through Zero-ETL,
you can choose how nested structures are represented in the target tables. AWS Glue Zero-ETL provides schema unnesting options to
flatten complex data structures into more analytics-friendly formats.

## Unnesting options

When creating a Zero-ETL integration with a source, you can choose from the following unnesting options.
These options correspond to specific enumeration values that you'll use when calling the CreateIntegrationTableProperty API.

No unnesting (default)

**API value: `NO_UNNEST`**

Preserves the original nested structure of DynamoDB items. Maps and lists are stored as structured columns in the target.

Best for: Preserving the exact structure of your DynamoDB data when your analytics tools can work with nested data.

Unnest one level

**API value: `TOP_LEVEL`**

Flattens the top level of nested maps into individual columns. List structures remain nested.

Best for: Balancing between data structure preservation and query simplicity when your DynamoDB items have a consistent schema.

Unnest all levels

**API value: `FULL`**

Recursively flattens all nested structures (maps and lists) into individual columns with dot notation for naming.

Best for: Maximizing query simplicity when working with deeply nested structures and analytics tools that prefer flat schemas.

###### Note

Full unnesting can lead to very wide tables with many columns if your DynamoDB data has variable or deeply nested structures.

###### Example Using unnesting options in the API

When configuring schema unnesting through the CreateIntegrationTableProperty API, specify the unnesting option in the UnnestSpec parameter:

```
aws glue create-integration-table-property
  --resource-arn "arn:aws:glue:us-east-1:123456789012:integration/my-integration"
  --table-name "my-table"
  --cli-input-json '{
      "TargetTableConfig": {
          "UnnestSpec": "FULL",
          "TargetTableName": "my-target-table",
      }
  }'
```

## Unnesting examples

Consider a DynamoDB item with the following structure:

```
{
  "ProductId": "P12345",
  "ProductDetails": {
    "Name": "Smartphone",
    "Brand": "TechCo",
    "Specifications": {
      "Color": "Black",
      "Storage": "128GB"
    }
  },
  "Reviews": [
    {
      "Rating": 5,
      "Comment": "Great product!"
    },
    {
      "Rating": 4,
      "Comment": "Good value."
    }
  ]
}
```

### No unnesting example

With no unnesting, the target table would have columns:

- ProductId (string)
- ProductDetails (struct)
- Reviews (array of structs)

Queries would need to use struct and array access patterns:

```
SELECT
  ProductId,
  ProductDetails.Name,
  ProductDetails.Specifications.Color
FROM product_table;
```

### Unnest one level example

With one level unnesting, the target table would have columns:

- ProductId (string)
- ProductDetails_Name (string)
- ProductDetails_Brand (string)
- ProductDetails_Specifications (struct)
- Reviews (array of structs)

Queries would be simplified for the first level:

```
SELECT
  ProductId,
  ProductDetails_Name,
  ProductDetails_Specifications.Color
FROM product_table;
```

### Unnest all levels example

With all levels unnesting, the target table would have columns and values:

| Column Name (Type)                             | Value          |
| ---------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| ProductId (string)                             | P12345         |
| ProductDetails_Name (string)                   | Smartphone     |
| ProductDetails_Brand (string)                  | TechCo         |
| ProductDetails_Specifications_Color (string)   | Black          |
| ProductDetails_Specifications_Storage (string) | 128GB          |
| Reviews_0_Rating (number)                      | 5              |
| Reviews_0_Comment (string)                     | Great product! |
| Reviews_1_Rating (number)                      | 4              |
| Reviews_1_Comment (string)                     | Good value.    | Queries would be fully flattened: `SELECT ProductId, ProductDetails_Name, ProductDetails_Specifications_Color FROM product_table;` |
