

# Schema unnesting
<a name="zero-etl-ddb-schema-unnesting"></a>

 When integrating with analytics services through Zero-ETL, you can choose how nested structures are represented in the target tables. AWS Glue Zero-ETL provides schema unnesting options to flatten complex data structures into more analytics-friendly formats. 

## Unnesting options
<a name="unnesting-options"></a>

 When creating a Zero-ETL integration with a source, you can choose from the following unnesting options. These options correspond to specific enumeration values that you'll use when calling the CreateIntegrationTableProperty API. For all unnest options, we would traverse to most inner layer and map DDB type to target spark/iceberg primitive type with best efforts. The type mapping between source DDB and target table is as below: 


| DDB source data type | Target table data type | 
| --- | --- | 
| "S" | StringType | 
| "B" | BinaryType | 
| "N" | DoubleType | 
| "BOOL" | BooleanType | 
| "SS" | ArrayType(StringType) | 
| "NS" | ArrayType(DoubleType) | 
| "BS" | ArrayType(BinaryType) | 
| "L" | ArrayType(StringType) | 
| "NULL" | Ignore | 
| "M" | StructType (TOP/NOUNNEST) | 

No unnesting - NO\_UNNEST  
 **API value: `NO_UNNEST`**   
 Preserves the original nested structure of Amazon DynamoDB items. Maps and lists are stored as structured columns in the target.   
 Best for: Preserving the exact structure of your Amazon DynamoDB data when your analytics tools can work with nested data. 

Top level - TOP\_LEVEL  
 **API value: `TOP_LEVEL`**   
 Flattens the top level of nested maps into individual columns. List structures remain nested.   
 Preserves the exact structure of your Amazon DynamoDB data when your analytics tools can work with nested data with all DDB type information removed.   
 Best for: Balancing between data structure preservation and query simplicity when your Amazon DynamoDB table items have a consistent schema. 

Unnest all levels - FULL (default)  
 **API value: `FULL`**   
 Recursively flattens all nested structures (maps and lists) into individual columns with dot notation for naming.   
 Best for: Maximizing query simplicity when working with deeply nested structures and analytics tools that prefer flat schemas.   
 Full unnesting can lead to very wide tables with many columns if your DynamoDB data has variable or deeply nested structures. 

**Example Using unnesting options in the API**  
 When configuring schema unnesting through the CreateIntegrationTableProperty API, specify the unnesting option in the UnnestSpec parameter:   

```
aws glue create-integration-table-property 
  --resource-arn "arn:aws:glue:us-east-1:123456789012:database/my_db" 
  --table-name "my-table" 
  --cli-input-json '{
      "TargetTableConfig": {
          "UnnestSpec": "FULL",
          "TargetTableName": "my-target-table",
      }
  }'
```

## Unnesting examples
<a name="unnesting-examples"></a>

 Consider a DynamoDB item with the following structure: 

```
// Input DynamoDB Record
{
  "Item": {
    "col_1": {
      "S": "value_1"
    },
    "col_2": {
      "M": {
        "col_3": {
          "M": {
            "id": {
              "S": "value_3"
            }
          }
        },
        "col_4": {
          "BOOL": true
        }
      }
    }
  }
}
```

### NO\_UNNEST example
<a name="no-unnesting-example"></a>

 With NO\_UNNEST, the entire row is stored within one column plus the primary key. DynamoDB type information is preserved. This maintains compatibility with Redshift querying patterns. 

Resulting Iceberg table (assuming col\_1 is primary key):


| col\_1 (string) | value (struct) | 
| --- | --- | 
| value\_1 | <pre>{<br />  "col_2": {<br />    "M": {<br />      "col_3": {<br />        "M": {<br />          "id": {<br />            "S": "value_3"<br />          }<br />        }<br />      },<br />      "col_4": {<br />        "BOOL": true<br />      }<br />    }<br />  }<br />}</pre> | 

Queries would need to use struct and array access patterns:

```
SELECT 
  value.col_1,
  value.col_2.M.col_3.M.id.S,
  value.col_2.M.col_4.BOOL
FROM product_table;
```

### TOP\_LEVEL example
<a name="unnest-one-level-example"></a>

 With TOP\_LEVEL, only the top-level fields are unnested while keeping nested fields intact as structs. DynamoDB type information is removed and typing is maintained. Converts to string type when schema conflicts occur. 

Resulting Glue table after replication:


| col\_1 (string) | col\_2 (struct) | 
| --- | --- | 
| value\_1 | <pre>{<br />  "col_3": {<br />    "id": "value_3"<br />  },<br />  "col_4": true<br />}</pre> | 

Queries would be simplified for the first level:

```
SELECT 
  col_1, 
  col_2.col_3.id,
  col_2.col_4
FROM product_table;
```

### FULL example
<a name="unnest-all-levels-example"></a>

 With FULL unnesting, both top-level fields and nested struct/map fields are flattened. Dot notation is used for nested fields (e.g., "col\_2.col\_3.id"). Array elements remain unnested. Each leaf node becomes a top-level column. 

Resulting Glue table after replication:


| col\_1 (string) | col\_2.col\_3.id (string) | col\_2.col\_4 (boolean) | 
| --- | --- | --- | 
| value\_1 | value\_3 | TRUE | 

Queries would be fully flattened:

```
SELECT 
  col_1, 
  "col_2.col_3.id",
  "col_2.col_4"
FROM product_table;
```