

# Reading from Xero entities

**Prerequisites**

A Xero object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| accounts | Yes | Yes | Yes | No | No | 
| branding-themes | No | Yes | Yes | No | No | 
| currencies | Yes | Yes | Yes | No | No | 
| items | Yes | Yes | Yes | No | No | 
| organisations | No | Yes | Yes | No | No | 
| tax-rates | Yes | Yes | Yes | No | No | 
| tracking-categories | Yes | Yes | Yes | No | No | 
| users | Yes | Yes | Yes | No | No | 

**Example – Reading from a Xero entity**  
The following example reads from the `accounts` entity. Replace {{connectionName}} with the name of your Xero connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="xero",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "accounts"
    }
)
```