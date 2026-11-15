

# Reading from Brevo entities
<a name="brevo-reading-from-entities"></a>

**Prerequisites**

A Brevo object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| contacts | Yes | Yes | Yes | No | No | 
| emailCampaigns | No | Yes | Yes | No | No | 
| lists | No | Yes | Yes | No | No | 
| senders | No | Yes | Yes | No | No | 

**Example – Reading from a Brevo entity**  
The following example reads from the `contacts` entity. Replace {{connectionName}} with the name of your Brevo connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="brevo",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "contacts"
    }
)
```