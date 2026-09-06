

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Monitoring zero-ETL integrations
<a name="zero-etl-monitoring"></a>

You can monitor your zero-ETL integrations by querying the system views or with Amazon EventBridge.

## Monitoring zero-ETL integrations with Amazon Redshift system views
<a name="zero-etl-monitoring-sysviews"></a>

You can monitor your zero-ETL integrations by querying the following system views in Amazon Redshift.
+ [SVV\_INTEGRATION](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION.html) provides information about configuration details of zero-ETL integrations.
+ [ SYS\_INTEGRATION\_ACTIVITY](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_INTEGRATION_ACTIVITY.html) provides information about completed zero-ETL integrations.
+ [SVV\_INTEGRATION\_TABLE\_MAPPING](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION_TABLE_MAPPING.html) provides information about mapping metadata values from source to target.
+ [SVV\_INTEGRATION\_TABLE\_STATE](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_INTEGRATION_TABLE_STATE.html) provides information about integration state.
+ [ SYS\_INTEGRATION\_TABLE\_ACTIVITY](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_INTEGRATION_TABLE_ACTIVITY.html) provides information about insert, delete, and update activity of integrations.
+ [ SYS\_INTEGRATION\_TABLE\_STATE\_CHANGE](https://docs.aws.amazon.com/redshift/latest/dg/r_SYS_INTEGRATION_TABLE_STATE_CHANGE.html) provides information about table state change log for integrations.

## Monitoring zero-ETL integrations with Amazon EventBridge
<a name="zero-etl-monitoring-events"></a>

Amazon Redshift sends integration-related events to Amazon EventBridge. For a list of events and their corresponding event IDs, see [Zero-ETL integration event notifications with Amazon EventBridge](integration-event-notifications.md).