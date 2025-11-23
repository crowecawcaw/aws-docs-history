# Apache Airflow Parameter Support

Amazon MWAA Serverless leverages Apache Airflow as its workflow orchestration engine and supports YAML workflow definitions that are build using allowlisted [Supported operators](operators.md "operators.md").
To provide the serverless experience using these operators, Amazon MWAA Serverless supports a limited set of [Apache Airflow parameters](https://airflow.apache.org/docs/apache-airflow/3.0.6/core-concepts/params.html "https://airflow.apache.org/docs/apache-airflow/3.0.6/core-concepts/params.html").
While building your workflow definitions, we recommend you to refer to the follwoing paramter support:

###### Topics

- [DAG level parameters that Amazon MWAA Serverless will validate](#dag-object-attributes-validation "#dag-object-attributes-validation")
- [Task level parameters that Amazon MWAA Serverless will validate](#task-object-attributes-validation "#task-object-attributes-validation")
- [DAG level paramters that are not supported by Amazon MWAA Serverless](#dag-object-attributes-not-supported "#dag-object-attributes-not-supported")
- [Task level paratmers that are not suppored by Amazon MWAA Serverless](#base-operator-attributes-not-supported "#base-operator-attributes-not-supported")
- [AWS base operator attributes](#aws-base-operator-attributes "#aws-base-operator-attributes")

## DAG level parameters that Amazon MWAA Serverless will validate

The following table lists the supported Apache Airflow DAG level parameters that are subject to validation by Amazon MWAA Serverless during a create or update of workflow.

| Parameter         | Validation Rule                                                                                                                                | Default Value |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| dag_id            | Must be a valid, non-empty string                                                                                                              |               |
| `schedule`        | Must be a valid CRON expression format                                                                                                         |               |
| `start_date`      | Must be in the future                                                                                                                          |               |
| `end_date`        | Must be after or equal to `start_date`                                                                                                         |               |
| `max_active_runs` | Must be smaller than account limit. Please refer to [Quotas for Amazon MWAA Serverless](mwaa-serverless-quotas.md "mwaa-serverless-quotas.md") | 16            |

## Task level parameters that Amazon MWAA Serverless will validate

The following table lists the Apache Airflow Task level parameters that are are subject to validation by Amazon MWAA Serverless during a task execution.

| Parameter           | Validation Rule                  | Default Value |
| ------------------- | -------------------------------- | ------------- |
| `task_id`           | Must be a valid string           |               |
| `retries`           | Must be between 0 to 3           | 1             |
| `retry_delay`       | Must be between 0 to 300 seconds | 300 seconds   |
| `execution_timeout` | Maximum 3600 seconds             | 3600 seconds  |

## DAG level paramters that are not supported by Amazon MWAA Serverless

The following table lists the Apache Airflow DAG level parameters that are not supported by Amazon MWAA Serverless and will be ignored.

| Parameter                         |
| --------------------------------- |
| `dag_id`                          |
| `template_searchpath`             |
| `template_undefined`              |
| `user_defined_macros`             |
| `user_defined_filters`            |
| `catchup`                         |
| `access_control`                  |
| `jinja_environment_kwargs`        |
| `render_template_as_native_obj`   |
| `tags`                            |
| `owner_links`                     |
| `auto_register`                   |
| `fail_fast`                       |
| `dag_display_name`                |
| `depends_on_past`                 |
| `email_on_failure`                |
| `email_on_retry`                  |
| `description`                     |
| `max_consecutive_failed_dag_runs` |
| `dagrun_timeout`                  |
| `sla_miss_callback`               |
| `on_failure_callback`             |
| `on_success_callback`             |
| `is_paused_upon_creation`         |

## Task level paratmers that are not suppored by Amazon MWAA Serverless

The following table lists the Apache Airflow Task level parameters that are not supported by Amazon MWAA Serverless and will be ignored.

| Parameter                               |
| --------------------------------------- |
| `email_on_retry`                        |
| `email_on_failure`                      |
| `retry_exponential_backoff`             |
| `depends_on_past`                       |
| `ignore_first_depends_on_past`          |
| `wait_for_downstream`                   |
| `priority_weight`                       |
| `sla`                                   |
| `max_active_tis_per_dag`                |
| `max_active_tis_per_dagrun`             |
| `task_concurrency`                      |
| `resources`                             |
| `run_as_user`                           |
| `executor_config`                       |
| `doc`                                   |
| `doc_md`                                |
| `doc_rst`                               |
| `doc_json`                              |
| `doc_yaml`                              |
| `task_display_name`                     |
| `logger_name`                           |
| `allow_nested_operators`                |
| `inlets`                                |
| `outlets`                               |
| `map_index_template`                    |
| `email`                                 |
| `owner`                                 |
| `max_retry_delay`                       |
| `on_execute_callback`                   |
| `on_failure_callback`                   |
| `on_success_callback`                   |
| `on_retry_callback`                     |
| `on_skipped_callback`                   |
| `wait_for_past_depends_before_skipping` |
| `do_xcom_push`                          |
| `multiple_outputs`                      |
| `start_date`                            |
| `end_date`                              |
| `weight_rule`                           |
| `queue`                                 |
| `pool`                                  |
| `pool_slots`                            |
| `pre_execute`                           |
| `post_execute`                          |
| `trigger_rule`                          |
| `executor`                              |
| `task_group`                            |

## AWS base operator attributes

| Parameter         | Amazon MWAA | Amazon MWAA Serverless       |
| ----------------- | ----------- | ---------------------------- |
| `aws_conn_id`     | Supported   | Controlled by service        |
| `verify`          | Supported   | Not supported                |
| `botocore_config` | Supported   | Not supported                |
| `region_name`     | Supported   | Gets Region from environment |
