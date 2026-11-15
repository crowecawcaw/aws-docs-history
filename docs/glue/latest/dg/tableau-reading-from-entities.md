

# Reading from Tableau entities
<a name="tableau-reading-from-entities"></a>

**Prerequisites**

A Tableau object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| datasource-connections | No | No | Yes | No | No | 
| datasources | No | No | Yes | No | No | 
| flows | No | No | Yes | No | No | 
| groups | No | No | Yes | No | No | 
| jobs | Yes | No | Yes | No | No | 
| projects | No | No | Yes | No | No | 
| subscriptions | No | No | Yes | No | No | 
| users | Yes | No | Yes | No | No | 
| views | No | No | Yes | No | No | 
| workbook-connections | No | No | Yes | No | No | 
| workbooks | No | No | Yes | No | No | 

**Example – Reading from a Tableau entity**  
The following example reads from the `datasource-connections` entity. Replace {{connectionName}} with the name of your Tableau connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="tableau",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "datasource-connections"
    }
)
```