

# Reading from SonarCloud entities

**Prerequisites**

A SonarCloud object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| analyses | No | Yes | Yes | No | No | 
| hotspots | No | Yes | Yes | No | No | 
| issues | No | Yes | Yes | No | No | 
| metrics | No | Yes | Yes | No | No | 
| projects | No | Yes | Yes | No | No | 
| quality\_gates | No | Yes | Yes | No | No | 
| rules | No | Yes | Yes | No | No | 

**Example – Reading from a SonarCloud entity**  
The following example reads from the `analyses` entity. Replace {{connectionName}} with the name of your SonarCloud connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="sonarcloud",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "analyses"
    }
)
```