

# Reading from Zoho Invoice entities
<a name="zohoinvoice-reading-from-entities"></a>

**Prerequisites**

A Zoho Invoice object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| contact\_addresses | No | Yes | Yes | No | No | 
| contact\_persons | No | Yes | Yes | No | No | 
| contacts | Yes | Yes | Yes | No | No | 
| creditnote\_refunds | No | Yes | Yes | No | No | 
| creditnotes | Yes | Yes | Yes | No | No | 
| currencies | No | Yes | Yes | No | No | 
| customerpayment\_refunds | No | Yes | Yes | No | No | 
| customerpayments | Yes | Yes | Yes | No | No | 
| estimates | No | Yes | Yes | No | No | 
| expense\_comments | No | Yes | Yes | No | No | 
| expensecategories | No | Yes | Yes | No | No | 
| expenses | Yes | Yes | Yes | No | No | 
| invoice\_comments | No | Yes | Yes | No | No | 
| invoice\_creditsapplied | No | Yes | Yes | No | No | 
| invoice\_payments | No | Yes | Yes | No | No | 
| invoices | Yes | Yes | Yes | No | No | 
| items | Yes | Yes | Yes | No | No | 
| organizations | No | Yes | Yes | No | No | 
| pricebooks | No | Yes | Yes | No | No | 
| projects | No | Yes | Yes | No | No | 
| recurringexpenses | No | Yes | Yes | No | No | 
| recurringinvoice\_comments | No | Yes | Yes | No | No | 
| recurringinvoices | No | Yes | Yes | No | No | 
| retainerinvoices | No | Yes | Yes | No | No | 
| taxes | No | Yes | Yes | No | No | 
| timeentries | No | Yes | Yes | No | No | 
| users | No | Yes | Yes | No | No | 

**Example – Reading from a Zoho Invoice entity**  
The following example reads from the `contact_addresses` entity. Replace {{connectionName}} with the name of your Zoho Invoice connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="zohoinvoice",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "contact_addresses"
    }
)
```