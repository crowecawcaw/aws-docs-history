Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_WLM_RULE_ACTION

Records details about actions resulting from WLM query monitoring rules associated
with user-defined queues. For more information, see [WLM query monitoring rules](cm-c-wlm-query-monitoring-rules.md "cm-c-wlm-query-monitoring-rules.md").

STL_WLM_RULE_ACTION is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name        | Data type      | Description                                                                                                                                                                                                                                                                                           |
| ------------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid             | integer        | User that ran the query.                                                                                                                                                                                                                                                                              |
| query              | integer        | Query ID.                                                                                                                                                                                                                                                                                             |
| service_class      | integer        | ID for the service class. Query<br>queues are defined in the WLM configuration. Service classes greater<br>than 5 are user-defined queues.                                                                                                                                                            |
| rule               | character(256) | Name of a query monitoring rule.                                                                                                                                                                                                                                                                      |
| action             | character(256) | Resulting action. Possible values are as follows:<br>• log<br>• hop(reassign)<br>• hop(restart)<br>• abort<br>• change_query_priority<br>• none<br>A value of `none` indicates that the rule’s<br>predicates were met but the action was superseded by another<br>rule with a higher severity action. |
| recordtime         | timestamp      | Time the action was logged in UTC.                                                                                                                                                                                                                                                                    |
| action_value       | character(256) | If `action` is `change_query_priority`, then possible values are `highest`, `high`, `normal`, `low`, and `lowest`.<br>If `action` is `log`, `hop`, or `abort` then the value is empty.                                                                                                                |
| service_class_name | character(64)  | The name of the service class.                                                                                                                                                                                                                                                                        |

## Sample queries

The following example finds queries that were stopped by a query monitoring
rule.

```
Select query, rule
from stl_wlm_rule_action
where action = 'abort'
order by query;

```
