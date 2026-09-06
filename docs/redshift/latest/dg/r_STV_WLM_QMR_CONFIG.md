

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STV\_WLM\_QMR\_CONFIG
<a name="r_STV_WLM_QMR_CONFIG"></a>

Records the configuration for WLM query monitoring rules (QMR). For more information, see [WLM query monitoring rules](cm-c-wlm-query-monitoring-rules.md).

STV\_WLM\_QMR\_CONFIG is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_STV_WLM_QMR_CONFIG-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| service\_class | integer  | ID for the WLM query queue (service class). Query queues are defined in the WLM configuration. Rules can be defined only for user-defined queues. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids). | 
| rule\_name  | character(256)  | Name of the query monitoring rule. | 
| action | character(256)  | Rule action. Possible values are log, hop, abort, and change\_query\_priority.  | 
| metric\_name  | character(256)  | Name of the metric. | 
| metric\_operator | character(256)  | The metric operator. Possible values are >, =, <.  | 
| metric\_value | double  | The threshold value for the specified metric that triggers an action.  | 
| action\_value | character(256) | If action is change\_query\_priority, then possible values are highest, high, normal, low, and lowest. If `action` is `log`, `hop`, or `abort` then the value is empty.  | 

## Sample query
<a name="r_STV_WLM_QMR_CONFIG-sample-query2"></a>

To view the QMR rule definitions for all service classes greater than 5 (which includes user-defined queues), run the following query. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids).

```
Select *
from stv_wlm_qmr_config
where service_class > 5
order by service_class;
```