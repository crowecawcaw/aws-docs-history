

# Reading from Recurly entities

**Prerequisites**

A Recurly object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| accounts | Yes | Yes | Yes | No | No | 
| coupons | No | Yes | Yes | No | No | 
| invoices | Yes | Yes | Yes | No | No | 
| items | Yes | Yes | Yes | No | No | 
| line\_items | Yes | Yes | Yes | No | No | 
| plans | Yes | Yes | Yes | No | No | 
| subscriptions | Yes | Yes | Yes | No | No | 
| transactions | Yes | Yes | Yes | No | No | 

**Example – Reading from a Recurly entity**  
The following example reads from the `accounts` entity. Replace {{connectionName}} with the name of your Recurly connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="recurly",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "accounts"
    }
)
```