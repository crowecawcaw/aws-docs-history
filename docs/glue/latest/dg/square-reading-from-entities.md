

# Reading from Square entities

**Prerequisites**

A Square object you want to read from. For the available entities, see the following supported entities table.

The `locations-transactions` entity belongs to a location. Set `ENTITY_NAME` to the full entity path that AWS Glue returns when it lists the entities for your connection, for example `locations-transactions/{{locationId}}`. All other entities are top-level entities.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| bank-accounts | Yes | Yes | Yes | No | No | 
| catalog-list | Yes | Yes | Yes | No | No | 
| customer-segments | No | Yes | Yes | No | No | 
| customers | No | Yes | Yes | No | No | 
| devices | Yes | Yes | Yes | No | No | 
| gift-cards | Yes | Yes | Yes | No | No | 
| gift-cards-activities | Yes | Yes | Yes | No | No | 
| inventory-adjustment-reasons | No | Yes | Yes | No | No | 
| labor-workweek-configs | No | Yes | Yes | No | No | 
| locations | No | Yes | Yes | No | No | 
| locations-transactions | Yes | Yes | Yes | No | No | 
| merchants | No | Yes | Yes | No | No | 
| payments | Yes | Yes | Yes | No | No | 
| refunds | Yes | Yes | Yes | No | No | 
| team-member-wages | Yes | Yes | Yes | No | No | 
| team-members-jobs | No | Yes | Yes | No | No | 

**Example – Reading from a Square entity**  
The following example reads from the `bank-accounts` entity. Replace {{connectionName}} with the name of your Square connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="square",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "bank-accounts"
    }
)
```