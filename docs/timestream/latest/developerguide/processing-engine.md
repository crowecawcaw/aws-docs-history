For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Extend Timestream for InfluxDB with processing engine

plugins

The Processing engine is an embedded Python virtual machine that runs inside your InfluxDB
3 database in Amazon Timestream. It's available in both Core and Enterprise editions. It enables you to
extend your database with custom Python code that can automate workflows, transform data, and
create custom API endpoints.

The Processing engine executes Python plugins in response to specific database events:

- **Data writes**: Process and transform data as it enters the
  database
- **Scheduled events**: Run code at defined intervals or specific
  times
- **HTTP requests**: Expose custom API endpoints that execute
  your code
  The engine includes an in-memory cache for managing state between executions, enabling you
  to build stateful applications directly within your database.

## InfluxData certified plugins

At launch, InfluxDB 3 includes a set of pre-built, fully configurable plugins certified
by InfluxData:

- **Data transformation**: Process and enrich incoming data
- **Alerting**: Send notifications based on data thresholds
- **Aggregation**: Calculate statistics on time-series data
- **System monitoring**: Track resource usage and health
  metrics
- **Integration**: Connect to external services and APIs

These certified plugins are ready to use and can be configured through trigger arguments
to meet your specific requirements.

## Plugin types and trigger

specifications

| **Plugin Type**  | **Trigger Specification**                 | **When Plugin Runs**            | **Use Cases**                                  |
| ---------------- | ----------------------------------------- | ------------------------------- | ---------------------------------------------- |
| **Data write**   | `table:<TABLE_NAME>` or `all_tables`      | When data is written to tables  | Data transformation, alerting, derived metrics |
| **Scheduled**    | `every:<DURATION>` or `cron:<EXPRESSION>` | At specified intervals          | Periodic aggregation, reports, health checks   |
| **HTTP request** | `request:<REQUEST_PATH>`                  | When HTTP requests are received | Custom APIs, webhooks, user interfaces         |

## Create triggers

Triggers connect plugins to database events and define when they execute. Use
the `influxdb3 create trigger` command.

To create a data write trigger:

```
# Trigger on writes to a specific table
influxdb3 create trigger \
  --trigger-spec "table:sensor_data" \
  --plugin-filename "process_sensors.py" \
  --database DATABASE_NAME \
  sensor_processor

# Trigger on all table writes
influxdb3 create trigger \
  --trigger-spec "all_tables" \
  --plugin-filename "process_all_data.py" \
  --database DATABASE_NAME \
  all_data_processor

```

To create a scheduled trigger:

```
# Run every 5 minutes
influxdb3 create trigger \
  --trigger-spec "every:5m" \
  --plugin-filename "periodic_check.py" \
  --database DATABASE_NAME \
  regular_check

# Run daily at 8am (cron format with seconds)
influxdb3 create trigger \
  --trigger-spec "cron:0 0 8 * * *" \
  --plugin-filename "daily_report.py" \
  --database DATABASE_NAME \
  daily_report

```

To create an HTTP request trigger:

```
# Create endpoint at /api/v3/engine/webhook
influxdb3 create trigger \
  --trigger-spec "request:webhook" \
  --plugin-filename "webhook_handler.py" \
  --database DATABASE_NAME \
  webhook_processor

```

Access the endpoint
at: `https://your-cluster-endpoint:8086/api/v3/engine/webhook`

## Configure triggers

### Passing arguments to plugins

Configure plugin behavior using trigger arguments:

```
influxdb3 create trigger \
  --trigger-spec "every:1h" \
  --plugin-filename "threshold_check.py" \
  --trigger-arguments "threshold=90,notify_email=admin@example.com" \
  --database DATABASE_NAME \
  threshold_monitor

```

Arguments are passed to the plugin as a dictionary:

```
def process_scheduled_call(influxdb3_local, call_time, args=None):
    if args and "threshold" in args:
        threshold = float(args["threshold"])
        email = args.get("notify_email", "default@example.com")
        # Use arguments in your logic

```

### Error handling behavior

Configure how triggers handle errors:

```
# Log errors (default)
influxdb3 create trigger \
  --trigger-spec "table:metrics" \
  --plugin-filename "process.py" \
  --error-behavior log \
  --database DATABASE_NAME \
  log_processor

# Retry on error
influxdb3 create trigger \
  --trigger-spec "table:critical_data" \
  --plugin-filename "critical.py" \
  --error-behavior retry \
  --database DATABASE_NAME \
  retry_processor

# Disable trigger on error
influxdb3 create trigger \
  --trigger-spec "request:webhook" \
  --plugin-filename "webhook.py" \
  --error-behavior disable \
  --database DATABASE_NAME \
  auto_disable_processor

```

### Asynchronous execution

Allow multiple trigger instances to run simultaneously:

```
influxdb3 create trigger \
  --trigger-spec "table:metrics" \
  --plugin-filename "heavy_process.py" \
  --run-asynchronous \
  --database DATABASE_NAME \
  async_processor

```

## Manage triggers

To view triggers for a database:

```
# Show all triggers for a database
influxdb3 show summary \
  --database DATABASE_NAME \
  --token YOUR_TOKEN

```

### Table exclusion for write

triggers

To filter tables within your plugin code when using `all_tables`:

```
influxdb3 create trigger \
  --trigger-spec "all_tables" \
  --plugin-filename "processor.py" \
  --trigger-arguments "exclude_tables=temp_data,debug_info" \
  --database DATABASE_NAME \
  data_processor

```

The plugin implementation is as follows:

```
def process_writes(influxdb3_local, table_batches, args=None):
    excluded_tables = set(args.get('exclude_tables', '').split(','))

    for table_batch in table_batches:
        if table_batch["table_name"] in excluded_tables:
            continue
        # Process allowed tables

```

## Distributed deployment

considerations

In multi-node deployments, configure plugins based on node roles:

| **Plugin Type**      | **Node Type**       | **Reason**                         |
| -------------------- | ------------------- | ---------------------------------- |
| Data write plugins   | Ingester nodes      | Process data at ingestion point    |
| HTTP request plugins | Querier nodes       | Handle API traffic                 |
| Scheduled plugins    | Any configured node | Can run on any node with scheduler |

The following considerations are important for enterprise deployments:

- Maintain identical plugin configurations across all relevant nodes.
- Route external clients (Grafana, dashboards) to querier nodes.
- Ensure plugins are available on nodes where their triggers execute.

## Best practices

- **Plugin configuration**
  - Use trigger arguments for configurable values instead of hardcoding.
  - Implement proper error handling within plugins.
  - Use the `influxdb3_local` API for database operations.

- **Performance optimization**
  - Use asynchronous execution for heavy processing tasks.
  - Implement early returns for filtered data.
  - Minimize database queries within plugins.

- **Error management**
  - Choose appropriate error behavior (log, retry, or disable).
  - Monitor plugin execution through system tables.
  - Test plugins thoroughly before production deployment.

- **Security considerations**
  - Validate all input data in HTTP request plugins.
  - Use secure methods for storing sensitive configuration.
  - Limit plugin permissions to required operations only.

## Monitor plugin execution

Query system tables to monitor plugin performance:

```
-- View processing engine logs
SELECT * FROM system.processing_engine_logs
WHERE time > now() - INTERVAL '1 hour'
ORDER BY time DESC

-- Check trigger status
SELECT * FROM system.processing_engine_triggers
WHERE database = 'DATABASE_NAME'

```

The Processing engine provides a powerful way to extend InfluxDB 3 functionality while
keeping your data processing logic close to your data, reducing latency and simplifying your
architecture.

### InfluxData certified plugins

Amazon Timestream for InfluxDB 3 includes a comprehensive set of pre-built, certified plugins
that extend database functionality without requiring custom development. These plugins are
fully configurable and ready to use at launch, providing advanced capabilities for data
processing, monitoring, and alerting.

For complete documentation and source code, visit the [InfluxData
Plugins Repository](https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata "https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata").

## Available plugins

### Anomaly detection plugins

#### MAD-based anomaly detection

- **Trigger types**: Data write (real-time)
- **Use cases**: Real-time outlier detection for streaming
  data, sensor monitoring, quality control.
- **GitHub**: [MAD Anomaly Detection Documentation](https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/mad_check "https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/mad_check")

**How it works:** Uses Median Absolute Deviation (MAD) to
establish a robust baseline for normal behavior. As new data arrives, it calculates how
many MADs away from the median each point is. Points exceeding the threshold (k \* MAD) are
flagged as anomalies.

**Key features:**

- Real-time processing as data is written.
- Maintains in-memory sliding windows for efficiency.
- Count-based alerts (e.g., 5 consecutive anomalies).
- Duration-based alerts (e.g., anomaly for 2 minutes).
- Flip suppression to prevent alert fatigue from rapidly changing values.

**Example usage:**

```
# Detect temperature anomalies in real-time
influxdb3 create trigger \
  --database sensors \
  --plugin-filename "gh:influxdata/mad_check/mad_check_plugin.py" \
  --trigger-spec "all_tables" \
  --trigger-arguments 'measurement=temperature_sensors,mad_thresholds="temp:2.5:20:5@humidity:3:30:2m",senders=slack,slack_webhook_url="YOUR_WEBHOOK"' \
  temp_anomaly_detector

# Threshold format: field:k_multiplier:window_size:trigger_condition
# temp:2.5:20:5 = temperature field, 2.5 MADs, 20-point window, alert after 5 consecutive anomalies
# humidity:3:30:2m = humidity field, 3 MADs, 30-point window, alert after 2 minutes of anomaly

```

**Output:** Sends real-time notifications when anomalies are
detected, including the field name, value, and duration.

### Data transformation plugins

#### Basic transformation

- **Trigger types**: Scheduled, Data write
- **Use cases**: Data standardization, unit conversions,
  field name normalization, data cleaning.
- **GitHub**: [Basic Transformation Documentation](https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/basic_transformation "https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/basic_transformation")

**How it works:** Applies a chain of transformations to field
names and values. Can process historical data in batches (scheduled) or transform data as
it arrives (data write). Transformations are applied in the order specified, allowing
complex data pipelines.

**Key features:**

- Field name transformations: snake_case, remove spaces, alphanumeric only.
- Unit conversions: Temperature, pressure, length, time units.
- Custom string replacements with regex support.
- Dry-run mode for testing without writing data.
- Batch processing for historical data.

**Example usage:**

```
# Transform temperature data from Celsius to Fahrenheit with field name standardization
influxdb3 create trigger \
  --database weather \
  --plugin-filename "gh:influxdata/basic_transformation/basic_transformation.py" \
  --trigger-spec "every:30m" \
  --trigger-arguments 'measurement=raw_weather,window=1h,target_measurement=weather_fahrenheit,names_transformations="Temperature Reading":"snake",values_transformations=temperature_reading:"convert_degC_to_degF"' \
  temp_converter

# Real-time field name cleaning for incoming sensor data
influxdb3 create trigger \
  --database iot \
  --plugin-filename "gh:influxdata/basic_transformation/basic_transformation.py" \
  --trigger-spec "all_tables" \
  --trigger-arguments 'measurement=raw_sensors,target_measurement=clean_sensors,names_transformations=.*:"snake alnum_underscore_only collapse_underscore"' \
  sensor_cleaner

```

**Output:** Creates a new table with transformed data,
preserving original timestamps and tags.

#### Downsampler

- **Trigger types**: Scheduled, HTTP
- **Use cases**: Data reduction, long-term storage
  optimization, creating summary statistics, performance improvement.
- **GitHub**: [Downsampler Documentation](https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/downsampler "https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/downsampler")

**How it works:** Aggregates high-resolution time-series data
into lower-resolution summaries. For example, converts 1-second data into 1-hour averages.
Each downsampled point includes metadata about the number of original points compressed
and the time range covered.

**Key features:**

- Multiple aggregation functions: avg, sum, min, max, median, derivative.
- Field-specific aggregations (different functions for different fields).
- Metadata tracking (record_count, time_from, time_to).
- HTTP API for on-demand downsampling with backfill.
- Configurable batch sizes for large datasets.

**Example usage:**

```
# Downsample CPU metrics from 10-second to hourly resolution
influxdb3 create trigger \
  --database metrics \
  --plugin-filename "gh:influxdata/downsampler/downsampler.py" \
  --trigger-spec "every:1h" \
  --trigger-arguments 'source_measurement=cpu_detailed,target_measurement=cpu_hourly,interval=1h,window=6h,calculations="usage:avg.max_usage:max.total_processes:sum",specific_fields=usage.max_usage.total_processes' \
  cpu_downsampler

# HTTP endpoint for on-demand downsampling
curl -X POST http://localhost:8086/api/v3/engine/downsample \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "source_measurement": "sensor_data",
    "target_measurement": "sensor_daily",
    "interval": "1d",
    "calculations": [["temperature", "avg"], ["humidity", "avg"], ["pressure", "max"]],
    "backfill_start": "2024-01-01T00:00:00Z",
    "backfill_end": "2024-12-31T23:59:59Z"
  }'

```

**Output:** Creates downsampled data with aggregated values
plus metadata columns showing the number of points compressed and time range.

### Monitoring and alerting plugins

#### State change monitor

- **Trigger types**: Scheduled, Data write
- **Use cases**: Status monitoring, equipment state
  tracking, process monitoring, change detection.
- **GitHub**: [State Change Documentation](https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/state_change "https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/state_change")

**How it works:** Tracks field value changes over time and
alerts when the number of changes exceeds configured thresholds. Can detect both value
changes (different values) and specific value conditions (equals a target value). Includes
stability checks to prevent alerts from noisy signals.

**Key features:**

- Count-based change detection (e.g., five changes in ten minutes).
- Duration-based monitoring (e.g., status = "error" for five minutes).
- State change window for noise reduction.
- Multi-field monitoring with independent thresholds.
- Configurable stability requirements.

**Example usage:**

```
# Monitor equipment status changes
influxdb3 create trigger \
  --database factory \
  --plugin-filename "gh:influxdata/state_change/state_change_check_plugin.py" \
  --trigger-spec "every:5m" \
  --trigger-arguments 'measurement=equipment,field_change_count="status:3.temperature:10",window=15m,state_change_window=5,senders=slack,notification_text="Equipment $field changed $changes times in $window"' \
  equipment_monitor

# Real-time monitoring for specific state conditions
influxdb3 create trigger \
  --database systems \
  --plugin-filename "gh:influxdata/state_change/state_change_check_plugin.py" \
  --trigger-spec "all_tables" \
  --trigger-arguments 'measurement=service_health,field_thresholds="status:down:5@health_score:0:10",senders=pagerduty' \
  service_monitor

```

**Output:** Alerts include the field name, number of changes
detected, time window, and relevant tag values.

#### System metrics collector

- **Trigger types**: Scheduled
- **Use cases**: Infrastructure monitoring, performance
  baselines, capacity planning, resource tracking.
- **GitHub**: [System Metrics Documentation](https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/system_metrics "https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/system_metrics")

**How it works:** Uses the psutil library to collect
comprehensive system metrics from the host running InfluxDB. Collects CPU, memory, disk,
and network statistics at configurable intervals. Each metric type can be enabled/disabled
independently.

**Key features:**

- Per-core CPU statistics with load averages.
- Memory usage including swap and page faults.
- Disk I/O metrics with calculated IOPS and latency.
- Network interface statistics with error tracking.
- Configurable metric collection (enable/disable specific types).
- Automatic retry on collection failures.

**Example usage:**

```
# Collect all system metrics every 30 seconds
influxdb3 create trigger \
  --database monitoring \
  --plugin-filename "gh:influxdata/system_metrics/system_metrics.py" \
  --trigger-spec "every:30s" \
  --trigger-arguments 'hostname=db-server-01,include_cpu=true,include_memory=true,include_disk=true,include_network=true' \
  system_monitor

# Focus on CPU and memory for application servers
influxdb3 create trigger \
  --database app_monitoring \
  --plugin-filename "gh:influxdata/system_metrics/system_metrics.py" \
  --trigger-spec "every:1m" \
  --trigger-arguments 'hostname=app-server-01,include_cpu=true,include_memory=true,include_disk=false,include_network=false' \
  app_metrics

```

**Output:** Creates multiple tables (system_cpu,
system_memory, system_disk_io, etc.) with detailed metrics for each subsystem.

### Predictive analytics plugins

#### Prophet forecasting

- **Trigger types**: Scheduled, HTTP
- **Use cases**: Demand forecasting, capacity planning,
  trend analysis, seasonal pattern detection.
- **GitHub**: [Prophet Forecasting Documentation](https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/prophet_forecasting "https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata/prophet_forecasting")

**How it works:** Uses Facebook's Prophet library to build
time-series forecasting models. Can train models on historical data and generate
predictions for future time periods. Models account for trends, seasonality, holidays, and
changepoints. Supports model persistence for consistent predictions.

**Key features:**

- Automatic seasonality detection (daily, weekly, yearly).
- Holiday calendar support (built-in and custom).
- Changepoint detection for trend shifts.
- Model persistence and versioning.
- Confidence intervals for predictions.
- Validation with MSRE thresholds.

**Example usage:**

```
# Train and forecast temperature data
influxdb3 create trigger \
  --database weather \
  --plugin-filename "gh:influxdata/prophet_forecasting/prophet_forecasting.py" \
  --trigger-spec "every:1d" \
  --trigger-arguments 'measurement=temperature,field=value,window=90d,forecast_horizont=7d,tag_values="location:seattle",target_measurement=temperature_forecast,model_mode=train,unique_suffix=seattle_v1,seasonality_mode=additive' \
  temp_forecast
# Validate temperature predictions with MAE
influxdb3 create trigger \
  --database weather \
  --plugin-filename "gh:influxdata/forecast_error_evaluator/forecast_error_evaluator.py" \
  --trigger-spec "every:1h" \
  --trigger-arguments 'forecast_measurement=temp_forecast,actual_measurement=temp_actual,forecast_field=predicted,actual_field=temperature,error_metric=mae,error_thresholds=WARN-"2.0":ERROR-"5.0",window=6h,rounding_freq=5min,senders=discord' \
  temp_forecast_check

```

**Output:** Sends notifications when forecast error exceeds
thresholds, including the error metric value and affected time range.

## Common configuration patterns

### Using TOML configuration files

For complex configurations, use TOML files instead of inline arguments:

```
# anomaly_config.toml
measurement = "server_metrics"
field = "cpu_usage"
window = "1h"
detector_type = "IsolationForestAD"
contamination = 0.1
window_size = 20
output_table = "cpu_anomalies"
senders = "slack"
slack_webhook_url = "https://hooks.slack.com/services/YOUR/WEBHOOK"
notification_text = "Anomaly detected in $field: value=$value at $timestamp"

```

```
# Use TOML configuration
PLUGIN_DIR=~/.plugins influxdb3 create trigger \
  --database monitoring \
  --plugin-filename "gh:influxdata/adtk_anomaly/adtk_anomaly_detection_plugin.py" \
  --trigger-spec "every:10m" \
  --trigger-arguments "config_file_path=anomaly_config.toml" \
  cpu_anomaly_detector

```

### Chaining plugins

Create data processing pipelines by chaining multiple plugins:

```
# Step 1: Transform raw data
influxdb3 create trigger \
  --database pipeline \
  --plugin-filename "gh:influxdata/basic_transformation/basic_transformation.py" \
  --trigger-spec "all_tables" \
  --trigger-arguments 'measurement=raw_sensors,target_measurement=clean_sensors,names_transformations=.*:"snake"' \
  step1_transform

# Step 2: Downsample transformed data
influxdb3 create trigger \
  --database pipeline \
  --plugin-filename "gh:influxdata/downsampler/downsampler.py" \
  --trigger-spec "every:1h" \
  --trigger-arguments 'source_measurement=clean_sensors,target_measurement=sensors_hourly,interval=1h,window=6h,calculations=avg' \
  step2_downsample

# Step 3: Detect anomalies in downsampled data
influxdb3 create trigger \
  --database pipeline \
  --plugin-filename "gh:influxdata/mad_check/mad_check_plugin.py" \
  --trigger-spec "all_tables" \
  --trigger-arguments 'measurement=sensors_hourly,mad_thresholds="value:3:20:5",senders=slack' \
  step3_anomaly

```

## Best practices for plugins

- **Start conservative** – Begin with higher thresholds
  and longer windows, then adjust based on observed patterns.
- **Test in development** – Use dry-run modes and test
  databases before production deployment.
- **Monitor plugin performance** – Check execution times
  and resource usage in system tables.
- **Use appropriate trigger types** – Choose scheduled
  for batch processing, data write for real-time.
- **Configure notifications wisely** – Use severity
  levels and debounce logic to prevent alert fatigue.
- **Leverage model persistence** – For ML-based plugins,
  save trained models for consistency.
- **Document configurations** – Use descriptive trigger
  names and maintain configuration documentation.

## Monitor plugin execution

To monitor plugin performance:

```
-- View plugin execution logs
SELECT
  event_time,
  trigger_name,
  log_level,
  log_text
FROM system.processing_engine_logs
WHERE trigger_name = 'your_trigger_name'
  AND time > now() - INTERVAL '1 hour'
ORDER BY event_time DESC;

-- Monitor plugin performance
SELECT
  trigger_name,
  COUNT(*) as executions,
  AVG(execution_time_ms) as avg_time_ms,
  MAX(execution_time_ms) as max_time_ms,
  SUM(CASE WHEN log_level = 'ERROR' THEN 1 ELSE 0 END) as error_count
FROM system.processing_engine_logs
WHERE time > now() - INTERVAL '24 hours'
GROUP BY trigger_name;

-- Check trigger status
SELECT * FROM system.processing_engine_triggers
WHERE database = 'your_database';

```

## Troubleshoot common issues

The following table shows common issues and possible solutions.

| **Issue**                 | **Solution**                                                      |
| ------------------------- | ----------------------------------------------------------------- |
| Plugin not triggering     | Verify trigger is enabled, check schedule/spec syntax             |
| Missing notifications     | Confirm Notifier plugin installed, check webhook URLs             |
| High memory usage         | Reduce window sizes, adjust batch processing intervals            |
| Incorrect transformations | Use dry-run mode, verify field names and data types               |
| Forecast inaccuracy       | Increase training data window, adjust seasonality settings        |
| Too many alerts           | Increase trigger counts, add debounce duration, adjust thresholds |

These certified plugins provide enterprise-ready functionality for common time-series
data processing needs, eliminating the need for custom development while maintaining
flexibility through comprehensive configuration options. Visit the [GitHub
repository](https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata "https://github.com/influxdata/influxdb3_plugins/tree/main/influxdata") for detailed documentation, examples, and updates.
