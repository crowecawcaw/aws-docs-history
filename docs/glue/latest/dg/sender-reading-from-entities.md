

# Reading from Sender entities

**Prerequisites**

A Sender object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| campaign-clicks | No | Yes | Yes | No | No | 
| campaign-complaints | No | Yes | Yes | No | No | 
| campaign-hard-bounces | No | Yes | Yes | No | No | 
| campaign-opens | No | Yes | Yes | No | No | 
| campaign-sents | No | Yes | Yes | No | No | 
| campaign-soft-bounces | No | Yes | Yes | No | No | 
| campaign-unsubscribes | No | Yes | Yes | No | No | 
| campaigns | Yes | Yes | Yes | No | No | 
| fields | No | Yes | Yes | No | No | 
| group-subscribers | No | Yes | Yes | No | No | 
| groups | No | Yes | Yes | No | No | 
| segment-subscribers | No | Yes | Yes | No | No | 
| segments | No | Yes | Yes | No | No | 
| subscribers | No | Yes | Yes | No | No | 
| transactional-campaigns | No | Yes | Yes | No | No | 
| workflows | Yes | Yes | Yes | No | No | 

**Example – Reading from a Sender entity**  
The following example reads from the `campaign-clicks` entity. Replace {{connectionName}} with the name of your Sender connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="sender",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "campaign-clicks"
    }
)
```