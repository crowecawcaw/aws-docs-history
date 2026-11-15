

# Reading from Checkout.com entities
<a name="checkout-reading-from-entities"></a>

**Prerequisites**

A Checkout.com object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| disputes | Yes | Yes | Yes | No | No | 

**Example – Reading from a Checkout.com entity**  
The following example reads from the `disputes` entity. Replace {{connectionName}} with the name of your Checkout.com connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="checkout",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "disputes"
    }
)
```