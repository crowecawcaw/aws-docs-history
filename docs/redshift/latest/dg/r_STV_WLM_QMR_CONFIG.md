Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_WLM_QMR_CONFIG

Records the configuration for WLM query monitoring rules (QMR). For more information,
see [WLM query monitoring rules](cm-c-wlm-query-monitoring-rules.md "cm-c-wlm-query-monitoring-rules.md").

STV_WLM_QMR_CONFIG is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type      | Description                                                                                                                                                                                                                                                                                                                                  |
| --------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| service_class   | integer        | ID for the WLM query queue (service class). Query<br>queues are defined in the WLM configuration. Rules can be defined<br>only for user-defined queues. For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids "cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids"). |
| rule_name       | character(256) | Name of the query monitoring rule.                                                                                                                                                                                                                                                                                                           |
| action          | character(256) | Rule action. Possible values<br>are `log`, `hop`, `abort`, and `change_query_priority`.                                                                                                                                                                                                                                                      |
| metric_name     | character(256) | Name of the metric.                                                                                                                                                                                                                                                                                                                          |
| metric_operator | character(256) | The metric operator. Possible values are >, =,<br><.                                                                                                                                                                                                                                                                                         |
| metric_value    | double         | The threshold value for the specified metric that triggers an<br>action.                                                                                                                                                                                                                                                                     |
| action_value    | character(256) | If `action` is `change_query_priority`, then possible values are `highest`, `high`, `normal`, `low`, and `lowest`.<br>If `action` is `log`, `hop`, or `abort` then the value is empty.                                                                                                                                                       |

## Sample query

To view the QMR rule definitions for all service classes greater than 5 (which includes user-defined queues), run the following query.
For a list of service class IDs, see [WLM service class IDs](cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids "cm-c-wlm-system-tables-and-views.md#wlm-service-class-ids").

```
Select *
from stv_wlm_qmr_config
where service_class > 5
order by service_class;

```
