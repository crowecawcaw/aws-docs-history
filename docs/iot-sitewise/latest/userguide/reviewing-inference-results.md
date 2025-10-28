# Review inference results

## Retrieve inference results

### Latest inference results

Run the following command to fetch the most recent inference result for an asset
property. For more information, see [get-asset-property-value](../../../cli/latest/reference/iotsitewise/get-asset-property-value.md "../../../cli/latest/reference/iotsitewise/get-asset-property-value.md") in the _AWS CLI Command Reference
Guide_.

```
aws iotsitewise get-asset-property-value \
    —asset-id `asset-id` \
    —property-id `result-property-id`
```

### Inference results history

Run the following command to fetch the history of inference results for a specified
time window. For more information, see [get-asset-property-value-history](../../../cli/latest/reference/iotsitewise/get-asset-property-value-history.md "../../../cli/latest/reference/iotsitewise/get-asset-property-value-history.md") in the _AWS CLI Command Reference
Guide_.

```
aws iotsitewise get-asset-property-value-history \
    —asset-id `asset-id` \
    —property-id `result-property-id` \
    —start-date `start-time` \
    —end-date `end-time`
```

### Example response

###### Example of an inference result response:

```
{
  "value": {
    "stringValue": "{\"timestamp\": \"2025-02-10T22:42:00.000000\", \"prediction\": 0, \"prediction_reason\": \"NO_ANOMALY_DETECTED\", \"diagnostics\": [{\"name\": \"asset-id\\\\property-id\", \"value\": 0.53528}]}"
  },
  "timestamp": {
    "timeInSeconds": 1739227320,
    "offsetInNanos": 0
  },
  "quality": "GOOD"
}
```

### Response fields

- **value.stringValue** – A JSON string containing the
  inference result with the following fields:
  - **timestamp** – The timestamp of the TQV against
    which inference is performed.
  - **prediction** – The prediction result (0 for no
    anomaly, 1 for anomaly detected).
  - **prediction_reason** – The reason for the
    prediction (`NO_ANOMALY_DETECTED` or
    `ANOMALY_DETECTED`).
  - **diagnostics** – An array of diagnostic
    information showing contributing factors.

- **timestamp** – The timestamp when the result is
  recorded in AWS IoT SiteWise.
- **quality** – The quality of the data point
  (typically `GOOD`).

## Understand inference results

An inference result returned by AWS IoT SiteWise anomaly detection includes key information about
the model's prediction at a specific timestamp, including whether an anomaly was detected
and which sensors contributed to the anomaly.

###### Example of a detailed inference result:

```
{
    "timestamp": "2021-03-11T22:25:00.000000",
    "prediction": 1,
    "prediction_reason": "ANOMALY_DETECTED",
    "anomaly_score": 0.72385,
    "diagnostics": [
      { "name": "asset_id_1\\\\property_id_1", "value": 0.02346 },
      { "name": "asset_id_2\\\\property_id_2", "value": 0.10011 },
      { "name": "asset_id_3\\\\property_id_3", "value": 0.11162 }
    ]
}
```

The `diagnostics` field is useful for interpreting _why_
the model makes a certain prediction. Each entry in the list includes:

- `name`: The sensor that contributed to the prediction (format:
  `asset_id\\\\property_id`).
- `value`: A floating-point number between 0 and 1, representing the
  **relative weight or importance**, of that sensor at that
  point in time.

User benefits:

- Understand which sensors had the strongest impact on an anomaly.
- Correlate high-weight sensors with physical equipment behavior.
- Inform root cause analysis.

###### Note

Even when `prediction = 0` (normal behavior), the diagnostics list is
returned. This helps assess which sensors are currently influencing the model's decisions,
even in healthy states.
