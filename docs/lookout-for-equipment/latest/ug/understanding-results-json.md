On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Reviewing inference results in a JSON file

The JSON file containing the inference results is stored in the Amazon Simple Storage Service (Amazon S3) bucket that
you've specified.

For the sensor data that your asset sends to Amazon S3, Amazon Lookout for Equipment marks the group of
readings as either normal or abnormal. For each group of abnormal readings, you can see
the sensors that Lookout for Equipment used to indicate that the equipment is behaving
abnormally.

The following shows example JSON output.

```
{"timestamp": "2021-03-11T22:24:00.000000", "prediction": 0, "prediction_reason": "MACHINE_OFF"}
{"timestamp": "2021-03-11T22:25:00.000000", "prediction": 1, "prediction_reason": "ANOMALY_DETECTED", "anomaly_score": 0.72385, "diagnostics": [{"name": "component_5feceb66\\sensor0", "value": 0.02346}, {"name": "component_5feceb66\\sensor1", "value": 0.10011}, {"name": "component_5feceb66\\sensor2", "value": 0.11162}, {"name": "component_5feceb66\\sensor3", "value": 0.14419}, {"name": "component_5feceb66\\sensor4", "value": 0.12219}, {"name": "component_5feceb66\\sensor5", "value": 0.14936}, {"name": "component_5feceb66\\sensor6", "value": 0.17829}, {"name": "component_5feceb66\\sensor7", "value": 0.00194}, {"name": "component_5feceb66\\sensor8", "value": 0.05446}, {"name": "component_5feceb66\\sensor9", "value": 0.11437}]}
{"timestamp": "2021-03-11T22:26:00.000000", "prediction": 0, "prediction_reason": "NO_ANOMALY_DETECTED", "anomaly_score": 0.41227, "diagnostics": [{"name": "component_5feceb66\\sensor0", "value": 0.03533}, {"name": "component_5feceb66\\sensor1", "value": 0.24063}, {"name": "component_5feceb66\\sensor2", "value": 0.06327}, {"name": "component_5feceb66\\sensor3", "value": 0.08303}, {"name": "component_5feceb66\\sensor4", "value": 0.18598}, {"name": "component_5feceb66\\sensor5", "value": 0.10839}, {"name": "component_5feceb66\\sensor6", "value": 0.08721}, {"name": "component_5feceb66\\sensor7", "value": 0.06792}, {"name": "component_5feceb66\\sensor8", "value": 0.1309}, {"name": "component_5feceb66\\sensor9", "value": 0.07735}]}
{"timestamp": "2021-03-11T22:27:00.000000", "prediction": 0, "prediction_reason": "NO_ANOMALY_DETECTED", "anomaly_score": 0.10541, "diagnostics": [{"name": "component_5feceb66\\sensor0", "value": 0.02533}, {"name": "component_5feceb66\\sensor1", "value": 0.34063}, {"name": "component_5feceb66\\sensor2", "value": 0.07327}, {"name": "component_5feceb66\\sensor3", "value": 0.03303}, {"name": "component_5feceb66\\sensor4", "value": 0.18598}, {"name": "component_5feceb66\\sensor5", "value": 0.10839}, {"name": "component_5feceb66\\sensor6", "value": 0.08721}, {"name": "component_5feceb66\\sensor7", "value": 0.06792}, {"name": "component_5feceb66\\sensor8", "value": 0.1309}, {"name": "component_5feceb66\\sensor9", "value": 0.07735}]}
{"timestamp": "2021-03-11T22:28:00.000000", "prediction": 0, "prediction_reason": "NO_ANOMALY_DETECTED", "anomaly_score": 0.24867, "diagnostics": [{"name": "component_5feceb66\\sensor0", "value": 0.04533}, {"name": "component_5feceb66\\sensor1", "value": 0.14063}, {"name": "component_5feceb66\\sensor2", "value": 0.08327}, {"name": "component_5feceb66\\sensor3", "value": 0.07303}, {"name": "component_5feceb66\\sensor4", "value": 0.18598}, {"name": "component_5feceb66\\sensor5", "value": 0.10839}, {"name": "component_5feceb66\\sensor6", "value": 0.08721}, {"name": "component_5feceb66\\sensor7", "value": 0.06792}, {"name": "component_5feceb66\\sensor8", "value": 0.1309}, {"name": "component_5feceb66\\sensor9", "value": 0.07735}]}
{"timestamp": "2021-03-11T22:29:00.000000", "prediction": 1, "prediction_reason": "ANOMALY_DETECTED", "anomaly_score": 0.79376, "diagnostics": [{"name": "component_5feceb66\\sensor0", "value": 0.04533}, {"name": "component_5feceb66\\sensor1", "value": 0.14063}, {"name": "component_5feceb66\\sensor2", "value": 0.08327}, {"name": "component_5feceb66\\sensor3", "value": 0.07303}, {"name": "component_5feceb66\\sensor4", "value": 0.18598}, {"name": "component_5feceb66\\sensor5", "value": 0.10839}, {"name": "component_5feceb66\\sensor6", "value": 0.08721}, {"name": "component_5feceb66\\sensor7", "value": 0.06792}, {"name": "component_5feceb66\\sensor8", "value": 0.1309}, {"name": "component_5feceb66\\sensor9", "value": 0.07735}]}
```

For the `prediction` field, a `value` of `1` indicates abnormal
equipment behavior. A `value` of `0` indicates normal equipment behavior.

If the value of `prediction_reason` isn't `MACHINE_OFF`,
Amazon Lookout for Equipment returns an object that contains a diagnostics list, regardless of the value of
`prediction`. The
`diagnostics` list has the name of the sensors and the weights of the
sensors' contributions in indicating abnormal equipment behavior. For each sensor, the
`name` field indicates the name of the sensor. The `value`
field indicates the percentage of the sensor's contribution to the prediction value. By
seeing the percentage of each sensor's contribution to the prediction value, you can see
how the data from each sensor was weighted.

The anomaly score is a value between 0 and 1 that indicates the intensity of the anomaly.

The prediction reason can be ANOMALY_DETECTED, NO_ANOMALY_DETECTED or MACHINE_OFF.
