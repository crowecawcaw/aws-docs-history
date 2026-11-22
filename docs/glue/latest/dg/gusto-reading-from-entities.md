

# Reading from Gusto entities

**Prerequisites**

A Gusto object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| admins | No | No | Yes | No | No | 
| benefits | No | No | Yes | No | No | 
| company | No | No | Yes | No | No | 
| company\_benefits | Yes | No | Yes | No | No | 
| contractor\_payments | No | No | Yes | No | No | 
| contractors | Yes | No | Yes | No | No | 
| departments | No | No | Yes | No | No | 
| employees | Yes | No | Yes | No | No | 
| locations | No | No | Yes | No | No | 
| pay\_periods | Yes | No | Yes | No | No | 
| pay\_schedules | No | No | Yes | No | No | 
| payrolls | Yes | No | Yes | No | No | 
| time\_off\_policies | No | No | Yes | No | No | 
| time\_off\_requests | Yes | No | Yes | No | No | 

**Example – Reading from a Gusto entity**  
The following example reads from the `admins` entity. Replace {{connectionName}} with the name of your Gusto connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="gusto",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "admins"
    }
)
```