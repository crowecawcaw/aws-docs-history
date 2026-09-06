

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STV\_WLM\_CLASSIFICATION\_CONFIG
<a name="r_STV_WLM_CLASSIFICATION_CONFIG"></a>

Contains the current classification rules for WLM. 

STV\_WLM\_CLASSIFICATION\_CONFIG is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_STV_WLM_CLASSIFICATION_CONFIG-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| id  | integer  | Service class ID. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids). | 
| condition  | character(128)  | Query conditions. | 
| action\_seq  | integer  | Reserved for system use. | 
| action  | character(64)  | Reserved for system use. | 
| action\_service\_class  | integer  | The service class where the action takes place. | 

## Sample query
<a name="r_STV_WLM_CLASSIFICATION_CONFIG-sample-query2"></a>

```
select * from STV_WLM_CLASSIFICATION_CONFIG;

id | condition                                   | action_seq | action | action_service_class
---+---------------------------------------------+------------+--------+---------------------
 1 | (system user) and (query group: health)     |          0 | assign |                    1
 2 | (system user) and (query group: metrics)    |          0 | assign |                    2
 3 | (system user) and (query group: cmstats)    |          0 | assign |                    3
 4 | (system user)                               |          0 | assign |                    4
 5 | (super user) and (query group: superuser)   |          0 | assign |                    5
 6 | (query group: querygroup1)                  |          0 | assign |                    6
 7 | (user group: usergroup1)                    |          0 | assign |                    6
 8 | (user group: usergroup2)                    |          0 | assign |                    7
 9 | (query group: querygroup3)                  |          0 | assign |                    8
10 | (query group: querygroup4)                  |          0 | assign |                    9
11 | (user group: usergroup4)                    |          0 | assign |                    9
12 | (query group: querygroup*)                  |          0 | assign |                   10
13 | (user group: usergroup*)                    |          0 | assign |                   10
14 | (querytype: any)                            |          0 | assign |                   11
(4 rows)
```