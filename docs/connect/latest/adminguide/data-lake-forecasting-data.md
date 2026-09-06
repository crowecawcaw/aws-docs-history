

# Forecasting data in the Connect Customer analytics data lake
<a name="data-lake-forecasting-data"></a>

This topic details the content in the Connect Customer data lake forecasting tables. Each table lists the column, type, and description of the content in the table.

There are two ways to access the analytics data lake and configure data to be shared: 
+ [Option 1: Use the Connect Customer console](access-datalake.md#option1-configure-data-to-be-shared)
+ [Option 2: Use CLI or CloudShell](access-datalake.md#option2-configure-data-to-be-shared)

If you are unable to access the scheduling tables by using Option 1, try using Option 2.

**Topics**
+ [Important things to know](#data-lake-forecasting-data-important)
+ [Forecast groups table](#data-lake-forecast-groups)
+ [Long-term forecasts table](#data-lake-longterm-forecasts)
+ [Short-term forecasts table](#data-lake-shortterm-forecasts)
+ [Intraday forecasts table](#data-lake-intraday-forecasts)
+ [Demand group table](#data-lake-demand-groups)
+ [Demand group definitions table](#data-lake-demand-group-definition)

## Important things to know
<a name="data-lake-forecasting-data-important"></a>
+ You can use the tables described in this topic to access published forecasts data in the data lake.
+ The Forecast groups table stores versioned records. A new version is created when forecast group details are changed, for example, adding or removing queues from the forecast group. You can get the latest record using the highest value of forecast\_group\_version.
+ You can join the Forecast groups table to the Long-term and Short-term forecasts tables by using the following columns: forecast\_group\_arn and forecast\_group\_version.

## Forecast groups table
<a name="data-lake-forecast-groups"></a>

**Table name:** `forecast_groups`

**Description:** Defines forecast groups that organize queues and channels for demand forecasting, using versioning for change tracking.

**Primary key:** `instance_id, forecast_group_arn, forecast_group_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `forecast_group_arn, forecast_group_version` — Joins to long\_term\_forecasts, short\_term\_forecasts
+ `forecast_group_arn` — Joins to staffing\_group\_forecast\_groups


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
|  instance\_id  |  String  |  No  |  The identifier of the Connect Customer instance.  | 
|  forecast\_group\_arn  |  String  |  No  |  The ARN of the forecast group.  | 
|  forecast\_group\_version |  Number  |  No  | The version of the forecast group. A new version is created every time a change is made to a forecast group, for example, addition of new queues.  | 
|  forecast\_group\_name |  String  |  Yes  |  The name of the forecast group. | 
|  instance\_arn  |  String  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  is\_deleted  |  Boolean  |  Yes  |  Whether the forecast group is deleted.  | 
|  last\_updated\_timestamp |  String  |  Yes  |  The epoch Timestamp in milliseconds when the last time the forecast group was created/updated/deleted.  | 
| data\_lake\_last\_processed\_timestamp |  Timestamp  |  Yes  | The Timestamp for the last time the data lake processed the record. This can include transformation and backfill processes. This field cannot be used to determine reliably data freshness. | 

## Long-term forecasts table
<a name="data-lake-longterm-forecasts"></a>

**Table name:** `long_term_forecasts`

**Description:** Contains long-term (daily interval) forecast data including contact volume and average handle time predictions, with support for customer-applied overrides.

**Primary key:** `instance_id, long_term_forecast_id`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `forecast_group_arn, forecast_group_version` — Joins to forecast\_groups
+ `queue_id` — Joins to Agent Queue Statistic Record


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
| instance\_id | String |  No  | The ID of the Connect Customer instance | 
| long\_term\_forecast\_id | String |  Yes  | Unique Identifier of the forecast data row. Key is hash of multiple values: instanceId, forecastGroupId, forecastGroupVersion, forecastType, queueId, channel, forecastStarttime, creationTime. | 
| forecast\_group\_arn | String |  Yes  | The ARN of the forecast group. | 
| forecast\_group\_version | Number |  Yes  | The version of the forecast group. | 
| interval | String |  Yes  | Time interval of the forecast data. For example, Daily for long term forecast data. | 
| queue\_id | String |  Yes  | The ID of the queue for the forecast. | 
| channel | String |  Yes  | The channel of the forecast. For example, VOICE. | 
| forecast\_interval\_start\_time | Timestamp |  Yes  | The start time of the time interval for this forecast data row. | 
| creation\_timestamp | Timestamp |  Yes  | The date and time when this forecast is first computed or published. | 
| computed\_time | Timestamp |  Yes  | The date and time when this forecast is computed. | 
| published\_time | Timestamp |  Yes  | The date and time when this forecast is published. This value is null until the forecast has been published. | 
| timezone | String |  Yes  | The timezone of the forecast, for example, UTC. | 
| is\_published | Boolean |  Yes  | Whether this forecast is published or not. | 
| average\_handle\_time | Number |  Yes  | The average handle time metric value of the forecast data row. | 
| contact\_volume | Number |  Yes  | The contact volume metric value of the forecast data row. | 
| average\_handle\_time\_override | Number |  Yes  | The customer applied override value of the average handle time metric. | 
| contact\_volume\_override | Number |  Yes  | The customer applied override value of the contact volume metric value. | 
| instance\_arn | String |  Yes  | The ARN of the Connect Customer instance of the forecast. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | The Timestamp for the last time the data lake processed the record. This can include transformation and backfill processes. This field cannot be used to determine reliably data freshness. | 

## Short-term forecasts table
<a name="data-lake-shortterm-forecasts"></a>

**Table name:** `short_term_forecasts`

**Description:** Contains short-term (15-minute interval) forecast data including contact volume and average handle time predictions, with support for customer-applied overrides.

**Primary key:** `instance_id, short_term_forecast_id`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `forecast_group_arn, forecast_group_version` — Joins to forecast\_groups
+ `queue_id` — Joins to Agent Queue Statistic Record


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
| instance\_id | String |  No  | The ID of the Connect Customer instance. | 
| short\_term\_forecast\_id | String |  Yes  | Unique Identifier of the forecast data row. Key is hash of multiple values: instanceId, forecastGroupId, forecastGroupVersion, forecastType, queueId, channel, forecastStarttime, creationTime. | 
| forecast\_group\_arn | String |  Yes  | The ARN of the forecast group for the forecast data row. | 
| forecast\_group\_version | Number |  Yes  | The version of the forecast group. | 
| interval | String |  Yes  | Time interval of the forecast data row. For example, FIFTEEN\_MINUTES for short term 15 minutes forecast data row. | 
| queue\_id | String |  Yes  | The ID of the queue for the forecast. | 
| channel | String |  Yes  | The channel of this forecast, for example, VOICE. | 
| forecast\_interval\_start\_time | Timestamp |  Yes  | The start time of the time interval for this forecast data row. | 
| creation\_timestamp | Timestamp |  Yes  | The date and time when this forecast is first computed or published. | 
| computed\_time | Timestamp |  Yes  | The date and time when this forecast is computed. | 
| published\_time | Timestamp |  Yes  | The date and time when this forecast is published. This value is null until the forecast has been published. | 
| is\_published | Boolean |  Yes  | Whether this forecast is published or not. | 
| average\_handle\_time | Number |  Yes  | The average handle time metric value of the forecast data row. | 
| contact\_volume | Number |  Yes  | The contact volume metric value of the forecast data row. | 
| average\_handle\_time\_override | Number |  Yes  | The customer applied override value of the average handle time metric. | 
| contact\_volume\_override | Number |  Yes  | The customer applied override value of the contact volume metric value. | 
| instance\_arn | String |  Yes  | The ARN of the Connect Customer instance of the forecast. | 
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | The Timestamp for the last time the data lake processed the record. This can include transformation and backfill processes. This field cannot be used to determine reliably data freshness. | 

## Intraday forecasts table
<a name="data-lake-intraday-forecasts"></a>

**Table name:** `intraday_forecasts`

**Description:** Contains intraday forecast data including forecasted contact volume, average handle time, queue answer time, and effective agent staffing for real-time workforce adjustments.

**Primary key:** `instance_id, intraday_forecast_id`

**Partition key:** `forecast_interval_start_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `queue_arn` — Joins to Agent Queue Statistic Record (through queue ARN and ID mapping)


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
|  intraday\_forecast\_id |  string  |  No  |  Unique identifier of this intraday forecast data.  | 
|  aws\_account\_id  |  string  |  Yes  |  The identifier of the AWS account that owns the Intraday Forecast.  | 
|  instance\_id |  string  |  No  |  The identifier of the Connect Customer instance. You can [find the instance ID](find-instance-arn.md) in the Amazon Resource Name (ARN) of the instance.  | 
|  instance\_arn |  string  |  Yes  |  Instance ARN of the Connect Customer instance.  | 
| channel  |  string  |  Yes  |  The method used to contact your contact center. | 
|  queue\_arn |  string  |  Yes  |  The Amazon Resource Name of the queue.  | 
| forecast\_interval\_start\_timestamp  |  Timestamp  |  Yes  |  Start Timestamp of the forecast interval.  | 
|  creation\_timestamp |  Timestamp  |  Yes  |  When the forecast was computed in forecasting system. | 
| average\_handle\_time  |  Double  |  Yes  | Forecasted metric data: average handle time. | 
| average\_queue\_answer\_time  |  Double  |  Yes  | Forecasted metric data: average queue answer time. | 
|  contact\_volume |  Double  |  Yes  |  Forecasted metric data: contact volume.  | 
| effective\_agent\_staffing  |  Double  |  Yes  | Forecasted metric data: effective agent staffing. | 
| data\_lake\_last\_processed\_timestamp |  Timestamp  |  Yes  | Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot reliably be used to determine data freshness.  | 

## Demand group table
<a name="data-lake-demand-groups"></a>

**Table name:** `demand_group`

**Description:** Defines demand groups that represent specific queue-channel combinations for capacity planning, associating demand targets with forecast groups.

**Primary key:** `instance_id, demand_group_arn, demand_group_version`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `forecast_group_arn` — Joins to forecast\_groups (as `forecast_group_arn`)
+ `demand_group_arn, demand_group_version` — Joins to demand\_group\_definitions
+ `demand_group_arn` — Joins to staffing\_group\_demand\_group, staff\_demand\_group


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The identifier of the Connect Customer instance.  | 
|  demand\_group\_arn  |  string  |  No  |  The ARN of the demand group.  | 
|  demand\_group\_version |  Long  |  No  | The version of the demand group. A new version is created every time a change is made to a demand group, for example, addition of new queues.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  demand\_group\_name |  string  |  Yes  |  Name of the demand group. | 
|  forecast\_group\_arn  |  string  |  Yes  |  The ARN of the forecast group.  | 
|  is\_deleted  |  Boolean  |  Yes  |  Whether the demand group is deleted.  | 
|  last\_updated\_timestamp |  Timestamp  |  Yes  |  Timestamp when the demand group was last created/updated/deleted.  | 
| data\_lake\_last\_processed\_timestamp |  Timestamp  |  Yes  | Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 

## Demand group definitions table
<a name="data-lake-demand-group-definition"></a>

**Table name:** `demand_group_definitions`

**Description:** Defines the queue and channel combinations that make up each demand group, mapping specific workload types to demand allocation targets.

**Primary key:** `instance_id, demand_group_definition_id`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `demand_group_arn, demand_group_version` — Joins to demand\_group
+ `queue_id` — Joins to Agent Queue Statistic Record


| Column | Type | Nullable | Description | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The identifier of the Connect Customer instance.  | 
|  demand\_group\_definition\_id  |  string  |  No  |  Unique Identifier for the demandGroup definition row. | 
|  demand\_group\_arn  |  string  |  Yes  |  The ARN of the demand group. | 
|  demand\_group\_version |  Long  |  Yes  | The version of the demand group. A new version is created every time a change is made to a demand group, for example, addition of new queues.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
| queue\_id |  string  |  Yes  |  ID of the queue that is part of the demand group. | 
| channel |  string  |  Yes  |  The channel of the queue-and-channel combination that belongs to the demand group. | 
|  is\_deleted  |  Boolean  |  Yes  |  Whether the demand group is deleted.  | 
|  last\_updated\_timestamp |  Timestamp  |  Yes  |  Timestamp when the demand group was last created/updated/deleted.  | 
| data\_lake\_last\_processed\_timestamp |  Timestamp  |  Yes  | Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. | 