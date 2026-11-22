

# Reading from Constant Contact entities

**Prerequisites**

A Constant Contact object you want to read from. For the available entities, see the following supported entities table.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| account-emails | Yes | No | Yes | No | No | 
| account-summary | No | No | Yes | No | No | 
| activities | Yes | Yes | Yes | No | No | 
| contact-custom-fields | No | Yes | Yes | No | No | 
| contact-lists | No | Yes | Yes | No | No | 
| contact-tags | No | Yes | Yes | No | No | 
| contacts | Yes | Yes | Yes | No | No | 
| email-campaigns | No | Yes | Yes | No | No | 
| segments | No | No | Yes | No | No | 

**Example – Reading from a Constant Contact entity**  
The following example reads from the `account-emails` entity. Replace {{connectionName}} with the name of your Constant Contact connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="constantcontact",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "account-emails"
    }
)
```