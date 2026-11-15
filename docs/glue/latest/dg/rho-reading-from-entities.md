

# Reading from Rho entities
<a name="rho-reading-from-entities"></a>

**Prerequisites**

A Rho object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| accounts | No | Yes | Yes | No | No | 
| business | No | No | Yes | No | No | 
| cards | Yes | Yes | Yes | No | No | 
| credit-balance | No | No | Yes | No | No | 
| credit-programs | No | Yes | Yes | No | No | 
| fields | No | Yes | Yes | No | No | 
| invoicing-customers | No | Yes | Yes | No | No | 
| invoicing-invoices | Yes | Yes | Yes | No | No | 
| reimbursements | Yes | Yes | Yes | No | No | 
| statements | Yes | Yes | Yes | No | No | 
| transactions | Yes | Yes | Yes | No | No | 
| users | Yes | Yes | Yes | No | No | 

**Example – Reading from a Rho entity**  
The following example reads from the `accounts` entity. Replace {{connectionName}} with the name of your Rho connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="rho",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "accounts"
    }
)
```