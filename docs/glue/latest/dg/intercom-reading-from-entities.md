

# Reading from Intercom entities
<a name="intercom-reading-from-entities"></a>

 **Prerequisites** 
+  An Intercom object you would like to read from. Refer to the supported entities table below to check the available entities. 

 **Supported entities** 


| Entity | API\_Version | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning | 
| --- | --- | --- | --- | --- | --- | --- | 
| Admins | v2.5 | No | No | No | Yes | No | 
| Companies | v2.5 | No | Yes | No | Yes | No | 
| Conversations | v2.5 | Yes | Yes | Yes | Yes | Yes | 
| Data Attributes | v2.5 | No | No | No | Yes | No | 
| Contacts | v2.5 | Yes | Yes | Yes | Yes | Yes | 
| Segments | v2.5 | No | No | No | Yes | No | 
| Tags | v2.5 | No | No | No | Yes | No | 
| Teams | v2.5 | No | No | No | Yes | No | 

 **Example** 

```
Intercom_read = glueContext.create_dynamic_frame.from_options(
    connection_type="Intercom",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "company",
        "API_VERSION": "V2.5"
    }
)
```

 **Intercom entity and field details** 


| Entity | Field | Data Type | Supported Operators | 
| --- | --- | --- | --- | 
| Admins | type | String | NA | 
| Admins | id | String | NA | 
| Admins | avatar | Struct | NA | 
| Admins | name | String | NA | 
| Admins | email | String | NA | 
| Admins | away\_mode\_enabled | Boolean | NA | 
| Admins | away\_mode\_reassign | Boolean | NA | 
| Admins | has\_inbox\_seat | Boolean | NA | 
| Admins | teams\_ids | List | NA | 
| Admins | job\_title | String | NA | 
| Companies | type | String | NA | 
| Companies | id | String | NA | 
| Companies | app\_id | String | NA | 
| Companies | created\_at | DateTime | NA | 
| Companies | remote\_created\_at | DateTime | NA | 
| Companies | updated\_at | DateTime | NA | 
| Companies | last\_request\_at | DateTime | NA | 
| Companies | plan | Struct | NA | 
| Companies | company\_id | String | NA | 
| Companies | name | String | NA | 
| Companies | custom\_attributes | Struct | NA | 
| Companies | session\_count | Integer | NA | 
| Companies | monthly\_spend | Integer | NA | 
| Companies | user\_count | Integer | NA | 
| Companies | industry | String | NA | 
| Companies | size | Integer | NA | 
| Companies | website | String | NA | 
| Companies | tags | Struct | NA | 
| Companies | segments | Struct | NA | 
| Contacts | id | String | EQUAL\_TO.NOT\_EQUAL\_TO | 
| Contacts | type | String | NA | 
| Contacts | workspace\_id | String | NA | 
| Contacts | external\_id | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | role | String | EQUAL\_TO.NOT\_EQUAL\_TO | 
| Contacts | email | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | phone | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | name | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | avatar | String | NA | 
| Contacts | owner\_id | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Contacts | social\_profiles | Struct | NA | 
| Contacts | has\_hard\_bounced | Boolean | EQUAL\_TO | 
| Contacts | marked\_email\_as\_spam | Boolean | EQUAL\_TO | 
| Contacts | unsubscribed\_from\_emails | Boolean | EQUAL\_TO | 
| Contacts | created\_at | DateTime | EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Contacts | updated\_at | DateTime | EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Contacts | signed\_up\_at | DateTime | EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Contacts | last\_seen\_at | DateTime | EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Contacts | last\_replied\_at | DateTime | EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Contacts | last\_contacted\_at | DateTime | EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Contacts | last\_email\_opened\_at | DateTime | EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Contacts | last\_email\_clicked\_at | DateTime | EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Contacts | language\_override | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | browser | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | browser\_version | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | browser\_language | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | os | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | location | Struct | NA | 
| Contacts | location\_country | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | location\_region | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | location\_city | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | android\_app\_name | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | android\_app\_version | String | NA | 
| Contacts | android\_device | String | NA | 
| Contacts | android\_os\_version | String | NA | 
| Contacts | android\_sdk\_version | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | android\_last\_seen\_at | Date | NA | 
| Contacts | ios\_app\_name | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | ios\_app\_version | String | NA | 
| Contacts | ios\_device | String | NA | 
| Contacts | ios\_os\_version | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | ios\_sdk\_version | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Contacts | ios\_last\_seen\_at | DateTime | NA | 
| Contacts | custom\_attributes | Struct | NA | 
| Contacts | tags | Struct | NA | 
| Contacts | notes | Struct | NA | 
| Contacts | companies | Struct | NA | 
| Contacts | unsubscribed\_from\_sms | Boolean | NA | 
| Contacts | sms\_consent | Boolean | NA | 
| Contacts | opted\_out\_subscription\_types | Struct | NA | 
| Contacts | referrer | String | NA | 
| Contacts | utm\_campaign | String | NA | 
| Contacts | utm\_content | String | NA | 
| Contacts | utm\_medium | String | NA | 
| Contacts | utm\_source | String | NA | 
| Contacts | utm\_term | String | NA | 
| Conversations | type | String | NA | 
| Conversations | id | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | created\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | updated\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | source | Struct | NA | 
| Conversations | source\_id | String | EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | source\_type | String | EQUAL\_TO, NOT\_EQUAL\_TO, | 
| Conversations | source\_delivered\_as | String | EQUAL\_TO, NOT\_EQUAL\_TO, | 
| Conversations | source\_subject | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | source\_body | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | source\_author\_id | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | source\_author\_type | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | source\_author\_name | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | source\_author\_email | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | source\_url | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | contacts | Struct | NA | 
| Conversations | teammates | Struct | NA | 
| Conversations | title | String | NA | 
| Conversations | admin\_assignee\_id | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | team\_assignee\_id | Integer | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | custom\_attributes | Struct | NA | 
| Conversations | open | Boolean | EQUAL\_TO | 
| Conversations | state | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | read | Boolean | EQUAL\_TO | 
| Conversations | waiting\_since | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | snoozed\_until | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | tags | Struct | NA | 
| Conversations | first\_contact\_reply | Struct | NA | 
| Conversations | priority | String | EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | topics | Struct | NA | 
| Conversations | sla\_applied | Struct | NA | 
| Conversations | conversation\_rating | Struct | NA | 
| Conversations | conversation\_rating\_requested\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | conversation\_rating\_replied\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | conversation\_rating\_score | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | conversation\_rating\_remark | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | conversation\_rating\_contact\_id | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | conversation\_rating\_admin\_id | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | statistics | Struct | NA | 
| Conversations | statistics\_time\_to\_assignment | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_time\_to\_admin\_reply | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_time\_to\_first\_close | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_time\_to\_last\_close | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_median\_time\_to\_reply | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_first\_contact\_reply\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_first\_assignment\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_first\_admin\_reply\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_first\_close\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_last\_assignment\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_last\_assignment\_admin\_reply\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_last\_contact\_reply\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_last\_admin\_reply\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_last\_close\_at | DateTime | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_last\_closed\_by\_id | String | CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO | 
| Conversations | statistics\_count\_reopens | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_count\_assignments | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | statistics\_count\_conversation\_parts | Integer | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN | 
| Conversations | conversation\_parts | List | NA | 
| Data Attributes | id | Integer | NA | 
| Data Attributes | type | String | NA | 
| Data Attributes | model | String | NA | 
| Data Attributes | name | String | NA | 
| Data Attributes | full\_name | String | NA | 
| Data Attributes | label | String | NA | 
| Data Attributes | description | String | NA | 
| Data Attributes | data\_type | String | NA | 
| Data Attributes | options | List | NA | 
| Data Attributes | api\_writable | Boolean | NA | 
| Data Attributes | ui\_writable | Boolean | NA | 
| Data Attributes | custom | Boolean | NA | 
| Data Attributes | archived | Boolean | NA | 
| Data Attributes | created\_at | Boolean | NA | 
| Data Attributes | updated\_at | DateTime | NA | 
| Data Attributes | admin\_id | String | NA | 
| Segments | type | String | NA | 
| Segments | id | String | NA | 
| Segments | name | String | NA | 
| Segments | created\_at | DateTime | NA | 
| Segments | updated\_at | DateTime | NA | 
| Segments | person\_type | String | NA | 
| Segments | count | Integer | NA | 
| Tags | type | String | NA | 
| Tags | id | String | NA | 
| Tags | name | String | NA | 
| Teams | type | String | NA | 
| Teams | id | String | NA | 
| Teams | name | String | NA | 
| Teams | admin\_ids | List | NA | 

 **Partitioning queries** 

 Additional spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, `NUM_PARTITIONS` can be provided if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by spark tasks concurrently. 
+  `PARTITION_FIELD`: the name of the field to be used to partition query. 
+  `LOWER_BOUND`: an inclusive lower bound value of the chosen partition field. 

   For date, we accept the Spark date format used in Spark SQL queries. Example of valid values: `"2024-02-06"`. 
+  `UPPER_BOUND`: an exclusive upper bound value of the chosen partition field. 
+  `NUM_PARTITIONS`: number of partitions. 

 Entity-wise partitioning field support details are captured in the following table. 


| Entity Name | Partitioning Field | Data Type | 
| --- | --- | --- | 
| Contacts | created\_at, updated\_at,last\_seen\_at | DateTime | 
| Conversations | id | Integer | 
| Conversations | created\_at, updated\_at | DateTime | 

 **Example** 

```
Intercom_read = glueContext.create_dynamic_frame.from_options(
    connection_type="Intercom",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "conversation",
        "API_VERSION": "V2.5",
        "PARTITION_FIELD": "created_at"
        "LOWER_BOUND": "2022-07-13T07:55:27.065Z"
        "UPPER_BOUND": "2022-08-12T07:55:27.065Z"
        "NUM_PARTITIONS": "2"
    }
)
```