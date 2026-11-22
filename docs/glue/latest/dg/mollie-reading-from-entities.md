

# Reading from Mollie entities

**Prerequisites**

A Mollie object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| chargebacks | No | Yes | Yes | No | No | 
| customers | No | Yes | Yes | No | No | 
| methods | Yes | Yes | Yes | No | No | 
| methods-all | Yes | Yes | Yes | No | No | 
| payment-links | No | Yes | Yes | No | No | 
| payments | No | Yes | Yes | No | No | 
| refunds | No | Yes | Yes | No | No | 
| subscriptions | No | Yes | Yes | No | No | 
| terminals | No | Yes | Yes | No | No | 

**Example – Reading from a Mollie entity**  
The following example reads from the `chargebacks` entity. Replace {{connectionName}} with the name of your Mollie connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="mollie",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "chargebacks"
    }
)
```