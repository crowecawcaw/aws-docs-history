

# Reading from GoCardless entities

**Prerequisites**

A GoCardless object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| block | Yes | Yes | Yes | No | No | 
| creditor | No | Yes | Yes | No | No | 
| creditor-bank-account | Yes | Yes | Yes | No | No | 
| customer | Yes | Yes | Yes | No | No | 
| customer-bank-account | Yes | Yes | Yes | No | No | 
| event | Yes | Yes | Yes | No | No | 
| instalment-schedule | Yes | Yes | Yes | No | No | 
| institution | Yes | Yes | Yes | No | No | 
| mandate | Yes | Yes | Yes | No | No | 
| payment | Yes | Yes | Yes | No | No | 
| payout | Yes | Yes | Yes | No | No | 
| refund | Yes | Yes | Yes | No | No | 
| scheme-identifier | Yes | Yes | Yes | No | No | 
| subscription | Yes | Yes | Yes | No | No | 
| tax-rate | Yes | Yes | Yes | No | No | 

**Example – Reading from a GoCardless entity**  
The following example reads from the `block` entity. Replace {{connectionName}} with the name of your GoCardless connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="gocardless",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "block"
    }
)
```