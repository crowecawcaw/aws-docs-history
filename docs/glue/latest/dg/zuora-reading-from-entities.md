

# Reading from Zuora entities
<a name="zuora-reading-from-entities"></a>

**Prerequisites**

A Zuora object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| account-contacts | No | Yes | Yes | No | No | 
| accounting-codes | No | Yes | Yes | No | No | 
| accounting-periods | No | Yes | Yes | No | No | 
| catalog-products | No | Yes | Yes | No | No | 
| customer-accounts | No | Yes | Yes | No | No | 
| gl-segments | No | Yes | Yes | No | No | 
| payment-methods | No | Yes | Yes | No | No | 
| product-rate-plans | No | Yes | Yes | No | No | 
| revenue-books | No | Yes | Yes | No | No | 
| revenue-calendars | No | Yes | Yes | No | No | 
| revenue-contract-bills | No | Yes | Yes | No | No | 
| revenue-contract-lines | No | Yes | Yes | No | No | 
| revenue-contract-pobs | No | Yes | Yes | No | No | 
| revenue-contracts | No | Yes | Yes | No | No | 
| revenue-costs | No | Yes | Yes | No | No | 
| revenue-exchange-rates | No | Yes | Yes | No | No | 
| revenue-holds | No | Yes | Yes | No | No | 
| revenue-organizations | No | Yes | Yes | No | No | 
| revenue-release-events | No | Yes | Yes | No | No | 
| sequence-sets | No | Yes | Yes | No | No | 

**Example – Reading from a Zuora entity**  
The following example reads from the `account-contacts` entity. Replace {{connectionName}} with the name of your Zuora connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="zuora",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "account-contacts"
    }
)
```