

# Reading from Zoho Books entities
<a name="zohobooks-reading-from-entities"></a>

**Prerequisites**

A Zoho Books object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| bills | Yes | Yes | Yes | No | No | 
| chart-of-accounts | Yes | Yes | Yes | No | No | 
| contacts | Yes | Yes | Yes | No | No | 
| customer-payments | Yes | Yes | Yes | No | No | 
| estimates | Yes | Yes | Yes | No | No | 
| expenses | Yes | Yes | Yes | No | No | 
| invoices | Yes | Yes | Yes | No | No | 
| items | Yes | Yes | Yes | No | No | 
| taxes | No | Yes | Yes | No | No | 

**Example – Reading from a Zoho Books entity**  
The following example reads from the `bills` entity. Replace {{connectionName}} with the name of your Zoho Books connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="zohobooks",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "bills"
    }
)
```