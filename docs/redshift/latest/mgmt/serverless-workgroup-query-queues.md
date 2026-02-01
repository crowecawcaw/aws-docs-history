Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting query queues

Amazon Redshift Serverless supports queue-based query resource management. You can create dedicated query queues with customized monitoring rules for different workloads.
This feature provides granular control over resource usage.

Query monitoring rules (QMR) apply only at the Redshift Serverless workgroup level, affecting all queries run in this workgroup uniformly. Queue-based approach
lets you create queues with distinct monitoring rules. You can assign these queues to specific user roles and query groups. Each queue operates independently,
with rules affecting only the queries within that queue.

Queues let you set metrics-based predicates and automated responses. For example, you can configure rules to automatically abort queries that exceed time limits or consume too many resources.

## Considerations

Consider the following when using serverless queues:

- The following Workload Management (WLM) configuration keys used in Amazon Redshift provisioned clusters are not supported in Redshift Serverless queues: `max_execution_time`,
  `short_query_queue`, `auto_wlm`, `concurrency_scaling`, `priority`,
  `queue_type`, `query_concurrency`, `memory_percent_to_use`,
  `user_group`, `user_group_wild_card`.

Additionally hop, change_query_priority actions are not supported in Serverless.

- The hop Action (moving queries between queues) is not supported in Amazon Redshift Serverless.
- Queue priorities are supported only for Amazon Redshift provisioned clusters.
- Amazon Redshift Serverless automatically manages scaling and resource allocation for optimal performance, so you don't need to manually configure queue priorities.

## Setting up query queues

You can create queues under the Limits tab for a serverless workgroup using the AWS Management Console, AWS CLI, or Redshift Serverless API.

Console
Follow these steps to create a queue for your serverless workgroup.

1. Navigate to your Redshift Serverless workgroup.
2. Select the Limits tab.
3. Under **Query Queues**, choose **Enable Queues**.

###### Important

Enabling query queues is a permanent change. You cannot revert to queue-less monitoring once enabled. 4. Configure your queues using the following parameters:

**Queue level parameters**

    * `name` - Queue identifier (required, unique, non-empty)
    * `user_role` - Array of user roles (optional)
    * `query_group` - Array of query groups (optional)
    * `query_group_wild_card` - 0 or 1 to enable wildcard matching (optional)
    * `user_group_wild_card` - 0 or 1 to enable wildcard matching (optional)
    * `rules` - Array of monitoring rules (optional)

**Rule level parameters**

    * `rule_name` - Unique identifier, max 32 chars (required)
    * `predicate` - Array of conditions, 1-3 predicates (required)
    * `action` - "abort" or "log" (required)

**Predicate level parameters**

    * `metric_name` - Metric to monitor (required)
    * `operator` - "=", "<", or ">" (required)
    * `value` - Numeric threshold (required)

**Limits**

    * Max 8 queues
    * Max 25 rules across all queues
    * Max 3 predicates per rule
    * Rule names must be unique globally

**Example Configuration**

Three queues example: one for dashboarding queries with a short timeout, one for ETL queries with a long timeout and an admin queue:

```
[
  {
    "name": "dashboard",
    "user_role": ["analyst", "viewer"],
    "query_group": ["reporting"],
    "query_group_wild_card": 1,
    "rules": [
      {
        "rule_name": "short_timeout",
        "predicate": [
          {
            "metric_name": "query_execution_time",
            "operator": ">",
            "value": 60
          }
        ],
        "action": "abort"
      }
    ]
  },
  {
    "name": "ETL",
    "user_role": ["data_scientist"],
    "query_group": ["analytics", "ml"],
    "rules": [
      {
        "rule_name": "long_timeout",
        "predicate": [
          {
            "metric_name": "query_execution_time",
            "operator": ">",
            "value": 3600
          }
        ],
        "action": "log"
      },
      {
        "rule_name": "memory_limit",
        "predicate": [
          {
            "metric_name": "query_temp_blocks_to_disk",
            "operator": ">",
            "value": 100000
          }
        ],
        "action": "abort"
      }
    ]
  },
  {
    "name": "admin_queue",
    "user_role": ["admin"],
    "query_group": ["admin"]
  }
]
```

In this example:

- Dashboard queries are aborted if they run more than 60 seconds
- ETL queries are logged if they run more than an hour
- Admin queue does not have any resource limits

CLI
You can manage queues using the CreateWorkgroup or UpdateWorkgroup APIs with the `wlm_json_configuration` config parameter to specify queues in JSON format.

```
aws redshift-serverless create-workgroup \
  --workgroup-name test-workgroup \
  --namespace-name test-namespace \
  --config-parameters '[{"parameterKey": "wlm_json_configuration", "parameterValue": "[{\"name\":\"dashboard\",\"user_role\":[\"analyst\",\"viewer\"],\"query_group\":[\"reporting\"],\"query_group_wild_card\":1,\"rules\":[{\"rule_name\":\"short_timeout\",\"predicate\":[{\"metric_name\":\"query_execution_time\",\"operator\":\">\",\"value\":60}],\"action\":\"abort\"}]},{\"name\":\"ETL\",\"user_role\":[\"data_scientist\"],\"query_group\":[\"analytics\",\"ml\"],\"rules\":[{\"rule_name\":\"long_timeout\",\"predicate\":[{\"metric_name\":\"query_execution_time\",\"operator\":\">\",\"value\":3600}],\"action\":\"log\"},{\"rule_name\":\"memory_limit\",\"predicate\":[{\"metric_name\":\"query_temp_blocks_to_disk\",\"operator\":\">\",\"value\":100000}],\"action\":\"abort\"}]},{\"name\":\"admin_queue\",\"user_role\":[\"admin\"],\"query_group\":[\"admin\"]}]"}]'
```

## Best practices

Keep the following best practices in mind when you use serverless queues.

- Use separate queues for workloads with distinct limit requirements (e.g., ETL, reporting, or ad-hoc analysis).
- Start with simple thresholds and adjust based on query behavior and usage patterns. You can monitor query usage patterns using the tables and views documented
  in [System tables and views for query monitoring rules](../dg/cm-c-wlm-query-monitoring-rules.md#cm-c-wlm-qmr-tables-and-views "../dg/cm-c-wlm-query-monitoring-rules.md#cm-c-wlm-qmr-tables-and-views").
