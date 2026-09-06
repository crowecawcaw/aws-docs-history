

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STV\_WLM\_SERVICE\_CLASS\_CONFIG
<a name="r_STV_WLM_SERVICE_CLASS_CONFIG"></a>

Records the service class configurations for WLM. 

STV\_WLM\_SERVICE\_CLASS\_CONFIG is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_STV_WLM_SERVICE_CLASS_CONFIG-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| service\_class  | integer  | ID for the service class. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids).  | 
| queueing\_strategy  | character(32)  | Reserved for system use.  | 
| num\_query\_tasks  | integer  | Current actual concurrency level of the service class. If num\_query\_tasks and target\_num\_query\_tasks are different, a dynamic WLM transition is in process. A value of -1 indicates that Auto WLM is configured.  | 
| target\_num\_query\_tasks  | integer  | Concurrency level set by the most recent WLM configuration change.  | 
| evictable  | character(8)  | Reserved for system use. | 
| eviction\_threshold  | bigint  | Reserved for system use. | 
| query\_working\_mem  | integer  | Current actual amount of working memory, in MB per slot, per node, assigned to the service class. If query\_working\_mem and target\_query\_working\_mem are different, a dynamic WLM transition is in process. A value of -1 indicates than Auto WLM is configured. | 
| target\_query\_working\_mem  | integer  | The amount of working memory, in MB per slot, per node, set by the most recent WLM configuration change.  | 
| min\_step\_mem  | integer  | Reserved for system use. | 
| name  | character(64)  | The name of the service class. | 
| max\_execution\_time | bigint | Number of milliseconds that the query can run before being terminated. | 
| user\_group\_wild\_card  | Boolean | If TRUE, the WLM queue treats an asterisk (\*) as a wildcard character in user group strings in the WLM configuration. | 
| query\_group\_wild\_card  | Boolean | If TRUE, the WLM queue treats an asterisk (\*) as a wildcard character in query group strings in the WLM configuration. | 
| concurrency\_scaling  | character(20) | Describes if the concurrency scaling is on or off. | 
| query\_priority  | character(20) | The value of the query priority.  | 
| user\_role\_wild\_card | Boolean | If TRUE, the WLM queue treats an asterisk (\*) as a wildcard character in user user strings in the WLM configuration. | 

## Sample query
<a name="r_STV_WLM_SERVICE_CLASS_CONFIG-sample-query2"></a>

The first user-defined service class is service class 6, which is named Service class \#1. The following query displays the current configuration for service classes greater than 4. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids). 

```
select rtrim(name) as name, 
num_query_tasks as slots, 
query_working_mem as mem, 
max_execution_time as max_time, 
user_group_wild_card as user_wildcard, 
query_group_wild_card as query_wildcard
from stv_wlm_service_class_config
where service_class > 4;

name                         | slots | mem | max_time | user_wildcard | query_wildcard
-----------------------------+-------+-----+----------+---------------+---------------
Service class for super user |     1 | 535 |        0 | false         | false   
Queue 1                      |     5 | 125 |        0 | false         | false         
Queue 2                      |     5 | 125 |        0 | false         | false         
Queue 3                      |     5 | 125 |        0 | false         | false         
Queue 4                      |     5 | 627 |        0 | false         | false         
Queue 5                      |     5 | 125 |        0 | true          | true          
Default queue                |     5 | 125 |        0 | false         | false
```

The following query shows the status of a dynamic WLM transition. While the transition is in process, `num_query_tasks` and `target_query_working_mem` are updated until they equal the target values. For more information, see [WLM dynamic and static configuration properties](cm-c-wlm-dynamic-properties.md).

```
select rtrim(name) as name, 
num_query_tasks as slots, 
target_num_query_tasks as target_slots, 
query_working_mem as memory, 
target_query_working_mem as target_memory
from stv_wlm_service_class_config
where num_query_tasks > target_num_query_tasks
or query_working_mem > target_query_working_mem
and service_class > 5;

 name             | slots | target_slots | memory | target_mem 
------------------+-------+--------------+--------+------------
 Queue 3          |     5 |           15 |    125 |       375 
 Queue 5          |    10 |            5 |    250 |       125 
 (2 rows)
```