

# Reading from Pipeliner entities
<a name="pipeliner-reading-from-entities"></a>

**Prerequisites**

A Pipeliner object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Accounts | No | Yes | Yes | No | No | 
| Activities | No | No | Yes | No | No | 
| Appointments | No | Yes | Yes | No | No | 
| Calls | No | No | Yes | No | No | 
| Clients | No | Yes | Yes | No | No | 
| CloudObjects | No | No | Yes | No | No | 
| Contacts | No | Yes | Yes | No | No | 
| EmailSequences | No | Yes | Yes | No | No | 
| EmailTemplates | No | Yes | Yes | No | No | 
| Emails | No | Yes | Yes | No | No | 
| Forecasts | No | Yes | Yes | No | No | 
| Leads | No | Yes | Yes | No | No | 
| Memos | No | Yes | Yes | No | No | 
| Notes | No | Yes | Yes | No | No | 
| Opportunities | No | Yes | Yes | No | No | 
| OpptyProductRelations | No | Yes | Yes | No | No | 
| Pipelines | No | Yes | Yes | No | No | 
| ProcessTemplates | No | Yes | Yes | No | No | 
| Processes | No | Yes | Yes | No | No | 
| ProductCategories | No | Yes | Yes | No | No | 
| ProductPriceListPrices | No | No | Yes | No | No | 
| ProductPriceLists | No | Yes | Yes | No | No | 
| Products | No | Yes | Yes | No | No | 
| Projects | No | Yes | Yes | No | No | 
| Quotes | No | Yes | Yes | No | No | 
| Reports | No | Yes | Yes | No | No | 
| SalesUnits | No | Yes | Yes | No | No | 
| Steps | No | Yes | Yes | No | No | 
| Tasks | No | Yes | Yes | No | No | 

**Example – Reading from a Pipeliner entity**  
The following example reads from the `Accounts` entity. Replace {{connectionName}} with the name of your Pipeliner connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="pipeliner",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "Accounts"
    }
)
```