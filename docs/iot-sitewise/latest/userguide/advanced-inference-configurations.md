# Advanced inference configurations

AWS IoT SiteWise allows customers to configure model inference schedules tailored to their
operational needs.

Inference scheduling is broadly categorized into three modes:

- [High frequency inferencing (5 minutes – 1
  hour)](#high-frequency-inferencing "#high-frequency-inferencing")
- [Low frequency inferencing (2 hours – 1
  day)](#low-frequency-inferencing "#low-frequency-inferencing")
- [Flexible scheduling](#flexible-scheduling "#flexible-scheduling")

## High frequency inferencing (5 minutes – 1

hour)

This mode is ideal for processes that operate continuously, or have a high rate of
change in sensor values. In this configuration, inference runs frequently as often as every
5 minutes.

**Use cases:**

- It is used in monitoring fast-changing equipment like compressors or
  conveyors.
- It is helpful in catching short-lived anomalies that require immediate
  response.
- It's an always-on operation where data is consistently flowing.

**Conditional offset support:**

You can define a **conditional offset** (0 - 60 minutes) to
delay inference after data ingestion. This ensures late-arriving data is still included in
the analysis window.

To configure high frequency inferencing:

- Configure `AWS/ANOMALY_DETECTION_INFERENCE` action payload value with
  `DataUploadFrequency` with values: `PT5M, PT10M, PT15M, PT30M,
PT1H` while starting inference.
- (Optional) Configure `DataDelayOffsetInMinutes` with the delay offset in
  minutes. Set this value between 0 and 60 minutes.

```
{
    "inferenceMode": "START",
    "dataDelayOffsetInMinutes": "DataDelayOffsetInMinutes",
    "dataUploadFrequency": "DataUploadFrequency"
}
```

###### Example of high frequency inference configuration:

```
{
    "inferenceMode": "START",
    "dataDelayOffsetInMinutes": "2",
    "dataUploadFrequency": "PT5M"
}
```

## Low frequency inferencing (2 hours – 1

day)

This mode is suited for slower-moving processes or use cases where daily evaluations are
sufficient. Customers configure inference to run hourly or once per day.

**Start time support for 1-day interval:**

For daily inference, optionally specify a **`startTime`** (8 AM every day), along with timezone awareness.

**Timezone support:**

When a `startTime` is provided, AWS IoT SiteWise uses [Time Zone Database](https://www.iana.org/time-zones "https://www.iana.org/time-zones"), maintained by the
Internet Assigned Numbers Authority (IANA). This ensures your inference aligns with local
working hours even across regions.

**Conditional offset support:**

As with other modes, a conditional offset of 0 – 60 minutes is configured.

**Use cases:**

- Daily health checks for batch processes or shift-based operations.
- Avoids inference during maintenance or downtime.
- It's helpful in resource-constrained environments, where compute usage must be
  minimized.

To configure low frequency inferencing:

- Configure `AWS/ANOMALY_DETECTION_INFERENCE` action payload value with
  `DataUploadFrequency` with values: `PT2H..PT12H`.
  - In the case of 1 day, `DataUploadFrequency` is
    `P1D`.

- (Optional) Configure `DataDelayOffsetInMinutes` with the delay offset in
  minutes. Set this value between 0 and 60 minutes.

###### Example of low frequency inference configuration:

```
{
    "inferenceMode": "START",
    "dataUploadFrequency": "P1D",
    "inferenceStartTime": "13:00",
    "inferenceTimeZone": "America/Chicago"
}
```

## Flexible scheduling

Flexible scheduling allows customers to define **specific days and
time ranges**, during which inference is run. This gives customers complete
control over scheduling based on production hours, shift timings, and planned
downtimes.

The `weeklyOperatingWindow` helps when:

- The equipment runs only during specific hours (8 AM – 4 PM).
- There is no production on weekends.
- Daily maintenance is scheduled during known time blocks.

**Timezone support:**

When a `startTime` is provided, AWS IoT SiteWise uses [Time Zone Database](https://www.iana.org/time-zones "https://www.iana.org/time-zones"), maintained by the
Internet Assigned Numbers Authority (IANA). This ensures the inference aligns with local
working hours even across regions.

**Conditional offset support:**

As with other modes, a conditional offset of 0 – 60 minutes can be configured.

Benefits of `weeklyOperatingWindow`:

- It avoids inference during idle or maintenance periods, reducing false
  positives.
- It aligns anomaly detection with operational priorities and shift-based
  workflows.

To configure flexible scheduling:

- Configure `AWS/ANOMALY_DETECTION_INFERENCE` action payload value with
  `DataUploadFrequency`.
- (Optional) `DataDelayOffsetInMinutes` with the delay offset in minutes.
  Set this value between 0 and 60 minutes.
- Configure `weeklyOperatingWindow` with a shift configuration:
  - Keys for the `weeklyOperatingWindow` are days of the week:
    `monday|tuesday|wednesday|thursday|friday|saturday|sunday`.
  - Each time range must be in **24-hour format** as
    `"HH:MM-HH:MM"` (`"08:00-16:00"`).
  - Multiple ranges can be specified per day.

###### Example of flexible scheduling configuration:

```
{
    "inferenceMode": "START",
    "dataUploadFrequency": "PT5M",
    "weeklyOperatingWindow": {
      "tuesday": ["11:00-13:00"],
      "monday": ["10:00-11:00", "13:00-15:00"]
    }
}
```

## Model version activation

When starting inference, you can optionally activate a specific model version to use for
anomaly detection. This feature allows you to select a particular trained model version, roll back to
previous versions, or override automatic model promotion decisions.

### Use cases:

- **Production rollback**: Quickly revert to a stable
  model version when the current version shows degraded performance or unexpected
  behavior.
- **A/B testing**: Compare performance between
  different model versions by switching between them during controlled time
  periods.
- **Manual model selection**: Override automatic
  promotion decisions, and manually select your preferred model version based on
  business requirements.
- **Staged deployment**: Test newer model versions in
  non-critical time windows before promoting them to full production use.
- **Performance optimization**: Select model versions
  that perform better for specific operational conditions, or seasonal patterns.
- **Rollback during maintenance**: Use older,
  well-tested model versions during system maintenance, or upgrades to ensure
  stability.

### Model version selection

behavior

When `targetModelVersion` is specified:

- The system activates the requested model version for inference.
- Validates that the specified model version exists.
- Overrides any automatic promotion settings.

When `targetModelVersion` is not specified:

- Activates the last active model version if inference was previously
  started.
- If inference was never activated, uses the latest trained model version.

To activate a specific model version:

- Configure the inference action payload, with targetModelVersion set to your
  desired model version number.
- The specified model version is validated and activated if it exists.

###### Example of model version activation:

```
{
    "inferenceMode": "START",
    "dataUploadFrequency": "PT15M",
    "targetModelVersion": 2
}
```

## Checking model versions

To verify the currently active model version:

- Use the [DescribeComputationModelExecutionSummary](../APIReference/API_DescribeComputationModelExecutionSummary.md "../APIReference/API_DescribeComputationModelExecutionSummary.md") API, which includes the active
  model version in the response.

To view all available model versions:

- Use the [ListExecutions](../APIReference/API_ListExecutions.md "../APIReference/API_ListExecutions.md")
  API to retrieve a complete list of historical model versions.
- Use the Use the [DescribeExecution](../APIReference/API_DescribeExecution.md "../APIReference/API_DescribeExecution.md") API to retrieve trained model information including export
  data time range, computation model version, and billable duration in minutes.

### Model version characteristics

- Model version numbers are assigned sequentially starting from 1.
- You can activate any previously trained model versions.
- The activated model version persists until explicitly changed.
- Model version activation works with all inference scheduling modes
  (high-frequency, low-frequency, and flexible).
- If the specified model version doesn't exist, the inference action fails with an
  error.
