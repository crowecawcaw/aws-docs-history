Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Monitoring zero-ETL integrations

You can monitor your zero-ETL integrations by querying the system views or with Amazon EventBridge.

## Monitoring zero-ETL integrations with Amazon Redshift system

views

You can monitor your zero-ETL integrations by querying the following system views in
Amazon Redshift.

- [SVV_INTEGRATION](../dg/r_SVV_INTEGRATION.md "../dg/r_SVV_INTEGRATION.md") provides information about configuration details of
  zero-ETL integrations.
- [SYS_INTEGRATION_ACTIVITY](../dg/r_SYS_INTEGRATION_ACTIVITY.md "../dg/r_SYS_INTEGRATION_ACTIVITY.md") provides information about completed
  zero-ETL integrations.
- [SVV_INTEGRATION_TABLE_MAPPING](../dg/r_SVV_INTEGRATION_TABLE_MAPPING.md "../dg/r_SVV_INTEGRATION_TABLE_MAPPING.md") provides information about mapping metadata
  values from source to target.
- [SVV_INTEGRATION_TABLE_STATE](../dg/r_SVV_INTEGRATION_TABLE_STATE.md "../dg/r_SVV_INTEGRATION_TABLE_STATE.md") provides information about integration
  state.
- [SYS_INTEGRATION_TABLE_ACTIVITY](../dg/r_SYS_INTEGRATION_TABLE_ACTIVITY.md "../dg/r_SYS_INTEGRATION_TABLE_ACTIVITY.md") provides information about insert, delete, and
  update activity of integrations.
- [SYS_INTEGRATION_TABLE_STATE_CHANGE](../dg/r_SYS_INTEGRATION_TABLE_STATE_CHANGE.md "../dg/r_SYS_INTEGRATION_TABLE_STATE_CHANGE.md") provides information about table state
  change log for integrations.

## Monitoring zero-ETL integrations with Amazon EventBridge

Amazon Redshift sends integration-related events to Amazon EventBridge. For a list of events and their
corresponding event IDs, see [Zero-ETL integration event notifications with
Amazon EventBridge](integration-event-notifications.md "integration-event-notifications.md").
