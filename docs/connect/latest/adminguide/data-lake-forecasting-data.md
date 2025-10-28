# Forecasting data in the Amazon Connect analytics

data lake

This topic details the content in the Amazon Connect analytics data lake forecasting
tables. Each table lists the column, type, and description of the content in the
table.

There are two ways to access the analytics data lake and configure data to be
shared:

- [Option 1: Use the Amazon Connect
  console](access-datalake.md#option1-configure-data-to-be-shared "access-datalake.md#option1-configure-data-to-be-shared")
- [Option 2: Use CLI or
  CloudShell](access-datalake.md#option2-configure-data-to-be-shared "access-datalake.md#option2-configure-data-to-be-shared")
  If you are unable to access the scheduling tables by using Option 1, try using
  Option 2.

###### Contents

- [Important things to
  know](#data-lake-forecasting-data-important "#data-lake-forecasting-data-important")
- [Forecast groups table](#data-lake-forecast-groups "#data-lake-forecast-groups")
- [Long-term forecasts table](#data-lake-longterm-forecasts "#data-lake-longterm-forecasts")
- [Short-term forecasts
  table](#data-lake-shortterm-forecasts "#data-lake-shortterm-forecasts")
- [Intraday forecasts table](#data-lake-intraday-forecasts "#data-lake-intraday-forecasts")

## Important things to

know

- You can use the tables described in this topic to access published
  forecasts data in the data lake.
- The Forecast groups table stores versioned records. A new version is
  created when forecast group details are changed, for example, adding or
  removing queues from the forecast group. You can get the latest record
  using the highest value of forecast_group_version.
- You can join the Forecast groups table to the Long-term and Short-term
  forecasts tables by using the following columns: forecast_group_arn and
  forecast_group_version.

## Forecast groups table

Table name: forecast_groups

Composite primary key: {instance_id, forecast_group_arn,
forecast_group_version}

| Column                             | Type      | Description                                                                                                                                                                                     |
| ---------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| instance_id                        | String    | The identifier of the Amazon Connect instance.                                                                                                                                                  |
| forecast_group_arn                 | String    | The ARN of the forecast group.                                                                                                                                                                  |
| forecast_group_version             | Number    | The version of the forecast group. A new version is created every time a change is made to a forecast group, for example, addition of new queues.                                               |
| forecast_group_name                | String    | The name of the forecast group.                                                                                                                                                                 |
| instance_arn                       | String    | The ARN of the Amazon Connect instance.                                                                                                                                                         |
| is_deleted                         | Boolean   | Whether the forecast group is deleted.                                                                                                                                                          |
| last_updated_timestamp             | String    | The epoch Timestamp in milliseconds when the last time the forecast group was created/updated/deleted.                                                                                          |
| data_lake_last_processed_timestamp | Timestamp | The Timestamp for the last time the data lake processed the record. This can include transformation and backfill processes. This field cannot be used to determine reliably data freshness.     | ## Long-term forecasts table Table name: long_term_forecasts Composite primary key: {instance_id, long_term_forcast_id}     |
| Column                             | Type      | Description                                                                                                                                                                                     |
| ---                                | ---       | ---                                                                                                                                                                                             |
| instance_id                        | String    | The ID of the Amazon Connect instance                                                                                                                                                           |
| long_term_forcast_id               | String    | Unique Identifier of the forecast data row. Key is hash of multiple values: instanceId, forecastGroupId, forecastGroupVersion, forecastType, queueId, channel, forecastStarttime, creationTime. |
| forecast_group_arn                 | String    | The ARN of the forecast group.                                                                                                                                                                  |
| forecast_group_version             | Number    | The version of the forecast group.                                                                                                                                                              |
| interval                           | String    | Time interval of the forecast data. For example, Daily for long term forecast data.                                                                                                             |
| queue_id                           | String    | The ID of the queue for the forecast.                                                                                                                                                           |
| channel                            | String    | The channel of the forecast. For example, VOICE.                                                                                                                                                |
| forecast_interval_start_time_ms    | Timestamp | Epoch in milliseconds of the start time of the time interval for this data row.                                                                                                                 |
| creation_timestamp_ms              | Timestamp | Epoch in milliseconds of when this forecast is first computed or published.                                                                                                                     |
| computed_timestamp_ms              | Timestamp | Epoch in milliseconds of when this forecast is first computed.                                                                                                                                  |
| published_timestamp_ms             | Timestamp | Epoch in milliseconds of when this forecast is first published.                                                                                                                                 |
| timezone                           | String    | The timezone of the forecast, for example, UTC.                                                                                                                                                 |
| is_published                       | Boolean   | Whether this forecast is published or not.                                                                                                                                                      |
| average_handle_time                | Number    | The average handle time metric value of the forecast data row.                                                                                                                                  |
| contact_volume                     | Number    | The contact volume metric value of the forecast data row.                                                                                                                                       |
| average_handle_time_override       | Number    | The customer applied override value of the average handle time metric.                                                                                                                          |
| contact_volume_override            | Number    | The customer applied override value of the contact volume metric value.                                                                                                                         |
| instance_arn                       | String    | The ARN of the Amazon Connect instance of the forecast.                                                                                                                                         |
| data_lake_last_processed_timestamp | Timestamp | The Timestamp for the last time the data lake processed the record. This can include transformation and backfill processes. This field cannot be used to determine reliably data freshness.     | ## Short-term forecasts table Table name: short_term_forecasts Composite primary key: {instance_id, short_term_forecast_id} |
| Column                             | Type      | Description                                                                                                                                                                                     |
| ---                                | ---       | ---                                                                                                                                                                                             |
| instance_id                        | String    | The ID of the Amazon Connect instance.                                                                                                                                                          |
| short_term_forecast_id             | String    | Unique Identifier of the forecast data row. Key is hash of multiple values: instanceId, forecastGroupId, forecastGroupVersion, forecastType, queueId, channel, forecastStarttime, creationTime. |
| forecast_group_arn                 | String    | The ARN of the forecast group for the forecast data row.                                                                                                                                        |
| forecast_group_version             | Number    | The version of the forecast group.                                                                                                                                                              |
| interval                           | String    | Time interval of the forecast data row. For example, FIFTEEN_MINUTES for short term 15 minutes forecast data row.                                                                               |
| queue_id                           | String    | The ID of the queue for the forecast.                                                                                                                                                           |
| channel                            | String    | The channel of this forecast, for example, VOICE.                                                                                                                                               |
| forecast_interval_start_time_ms    | Timestamp | Epoch in milliseconds of the start time of the time interval for this data row.                                                                                                                 |
| creation_timestamp_ms              | Timestamp | Epoch in milliseconds of when this forecast is first computed or published.                                                                                                                     |
| computed_timestamp_ms              | Timestamp | Epoch in milliseconds of when this forecast is first computed.                                                                                                                                  |
| published_timestamp_ms             | Timestamp | Epoch in milliseconds of when this forecast is first published.                                                                                                                                 |
| is_published                       | Boolean   | Whether this forecast is published or not.                                                                                                                                                      |
| average_handle_time                | Number    | The average handle time metric value of the forecast data row.                                                                                                                                  |
| contact_volume                     | Number    | The contact volume metric value of the forecast data row.                                                                                                                                       |
| average_handle_time_override       | Number    | The customer applied override value of the average handle time metric.                                                                                                                          |
| contact_volume_override            | Number    | The customer applied override value of the contact volume metric value.                                                                                                                         |
| instance_arn                       | String    | The ARN of the Amazon Connect instance of the forecast.                                                                                                                                         |
| data_lake_last_processed_timestamp | Timestamp | The Timestamp for the last time the data lake processed the record. This can include transformation and backfill processes. This field cannot be used to determine reliably data freshness.     | ## Intraday forecasts table Table name: intraday_forecasts Composite primary key: {instance_id, intraday_forecast_id}       |
| **Column**                         | **Type**  | **Description**                                                                                                                                                                                 |
| ---                                | ---       | ---                                                                                                                                                                                             |
| intraday_forecast_id               | string    | Unique identifier of this intraday forecast data.                                                                                                                                               |
| aws_account_id                     | string    | The identifier of the AWS account that owns the Intraday Forecast.                                                                                                                              |
| instance_id                        | string    | The identifier of the Amazon Connect instance. You can [find the instance ID](find-instance-arn.md "find-instance-arn.md") in the Amazon Resource Name (ARN) of the instance.                   |
| instance_arn                       | string    | Instance ARN of the Amazon Connect instance.                                                                                                                                                    |
| channel                            | string    | The method used to contact your contact center.                                                                                                                                                 |
| queue_arn                          | string    | The Amazon Resource Name of the queue.                                                                                                                                                          |
| forecast_interval_start_time       | Timestamp | Start Timestamp of the forecast interval.                                                                                                                                                       |
| creation_timestamp                 | Timestamp | When the forecast was computed in forecasting system.                                                                                                                                           |
| average_handle_time                | Double    | Forecasted metric data: average handle time.                                                                                                                                                    |
| average_queue_answer_time          | Double    | Forecasted metric data: average queue answer time.                                                                                                                                              |
| contact_volume                     | Double    | Forecasted metric data: contact volume.                                                                                                                                                         |
| effective_agent_staffing           | Double    | Forecasted metric data: effective agent staffing.                                                                                                                                               |
| data_lake_last_processed_timestamp | Timestamp | Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot be used to determine reliably data freshness.          |
