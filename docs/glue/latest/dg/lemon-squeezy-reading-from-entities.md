

# Reading from Lemon Squeezy entities

**Prerequisites**

A Lemon Squeezy object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| checkouts | Yes | Yes | Yes | No | No | 
| customers | Yes | Yes | Yes | No | No | 
| discounts | Yes | Yes | Yes | No | No | 
| files | Yes | Yes | Yes | No | No | 
| license-keys | Yes | Yes | Yes | No | No | 
| order-items | Yes | Yes | Yes | No | No | 
| orders | Yes | Yes | Yes | No | No | 
| prices | Yes | Yes | Yes | No | No | 
| products | Yes | Yes | Yes | No | No | 
| stores | No | Yes | Yes | No | No | 
| subscription-invoices | Yes | Yes | Yes | No | No | 
| subscription-items | Yes | Yes | Yes | No | No | 
| subscriptions | Yes | Yes | Yes | No | No | 
| variants | Yes | Yes | Yes | No | No | 

**Example – Reading from a Lemon Squeezy entity**  
The following example reads from the `checkouts` entity. Replace {{connectionName}} with the name of your Lemon Squeezy connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="lemon-squeezy",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "checkouts"
    }
)
```