

# Reading from ShipBob entities
<a name="shipbob-reading-from-entities"></a>

**Prerequisites**

A ShipBob object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| channels | No | Yes | Yes | No | No | 
| fulfillment\_centers | No | Yes | Yes | No | No | 
| inventory | No | Yes | Yes | No | No | 
| inventory\_level | No | Yes | Yes | No | No | 
| invoices | Yes | Yes | Yes | No | No | 
| locations | No | Yes | Yes | No | No | 
| orders | Yes | Yes | Yes | No | No | 
| products | Yes | Yes | Yes | No | No | 
| receiving | Yes | Yes | Yes | No | No | 
| returns | Yes | Yes | Yes | No | No | 
| shipping\_methods | No | Yes | Yes | No | No | 
| webhooks | No | Yes | Yes | No | No | 

**Example – Reading from a ShipBob entity**  
The following example reads from the `channels` entity. Replace {{connectionName}} with the name of your ShipBob connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="shipbob",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "channels"
    }
)
```