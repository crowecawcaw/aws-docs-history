

# Reading from Zoho Desk entities

**Prerequisites**

A Zoho Desk object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| accounts | No | Yes | Yes | No | No | 
| agents | Yes | Yes | Yes | No | No | 
| calls | Yes | Yes | Yes | No | No | 
| contacts | No | Yes | Yes | No | No | 
| departments | No | Yes | Yes | No | No | 
| products | No | Yes | Yes | No | No | 
| tasks | Yes | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 
| ticket-attachments | No | Yes | Yes | No | No | 
| ticket-comments | No | Yes | Yes | No | No | 
| ticket-threads | No | Yes | Yes | No | No | 
| tickets | Yes | Yes | Yes | No | No | 

**Example – Reading from a Zoho Desk entity**  
The following example reads from the `accounts` entity. Replace {{connectionName}} with the name of your Zoho Desk connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="zohodesk",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "accounts"
    }
)
```