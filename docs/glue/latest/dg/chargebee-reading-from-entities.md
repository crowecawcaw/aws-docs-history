

# Reading from Chargebee entities

**Prerequisites**

A Chargebee object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| coupons | Yes | Yes | Yes | No | No | 
| credit\_notes | Yes | Yes | Yes | No | No | 
| customers | Yes | Yes | Yes | No | No | 
| events | Yes | Yes | Yes | No | No | 
| invoices | Yes | Yes | Yes | No | No | 
| item\_families | Yes | Yes | Yes | No | No | 
| item\_prices | Yes | Yes | Yes | No | No | 
| items | Yes | Yes | Yes | No | No | 
| payment\_sources | Yes | Yes | Yes | No | No | 
| subscriptions | Yes | Yes | Yes | No | No | 
| transactions | Yes | Yes | Yes | No | No | 

**Example – Reading from a Chargebee entity**  
The following example reads from the `coupons` entity. Replace {{connectionName}} with the name of your Chargebee connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="chargebee",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "coupons"
    }
)
```