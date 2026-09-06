

# Location
<a name="location-rule-action"></a>

The Location (`location`) action sends your geographical location data to [Amazon Location Service](https://docs.aws.amazon.com/location/latest/developerguide/welcome.html).

## Requirements
<a name="location-rule-action-requirements"></a>

This rule action has the following requirements:
+ An IAM role that AWS IoT can assume to perform the `geo:BatchUpdateDevicePosition` operation. For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md).

  In the AWS IoT console, you can choose or create a role to allow AWS IoT to perform this rule action.

## Parameters
<a name="location-rule-action-parameters"></a>

When you create an AWS IoT rule with this action, you must specify the following information:

`deviceId`  
The unique ID of the device providing the location data. For more information, see [`DeviceId`](https://docs.aws.amazon.com/location/latest/APIReference/API_DevicePositionUpdate.html) from the *Amazon Location Service API Reference*.  
Supports [substitution templates](iot-substitution-templates.md): Yes

`latitude`  
A string that evaluates to a double value that represents the latitude of the device's location.  
Supports [substitution templates](iot-substitution-templates.md): Yes

`longitude`  
A string that evaluates to a double value that represents the longitude of the device's location.  
Supports [substitution templates](iot-substitution-templates.md): Yes

`roleArn`  
The IAM role that allows access to the Amazon Location Service domain. For more information, see [Requirements](#location-rule-action-requirements). 

`timestamp`  
The time that the location data was sampled. The default value is the time that the MQTT message was processed.  
The `timestamp` value consists of the following two values:  
+ `value`: An expression that returns a long epoch time value. You can use the [time\_to\_epoch(String, String)](iot-sql-functions.md#iot-sql-function-time-to-epoch) function to create a valid timestamp from a date or time value passed in the message payload. Supports [substitution templates](iot-substitution-templates.md): Yes.
+ `unit`: (Optional) The precision of the timestamp value that results from the expression described in `value`. Valid values: `SECONDS` \| `MILLISECONDS` \| `MICROSECONDS` \| `NANOSECONDS`. The default is `MILLISECONDS`. Supports [substitution templates](iot-substitution-templates.md): API and AWS CLI only.

`trackerName`  
The name of the tracker resource in Amazon Location in which the location is updated. For more information, see [Tracker](https://docs.aws.amazon.com/location/latest/developerguide/geofence-tracker-concepts.html#tracking-overview) from the *Amazon Location Service Developer Guide*.  
Supports [substitution templates](iot-substitution-templates.md): API and AWS CLI only

## Examples
<a name="location-rule-action-examples"></a>

The following JSON example defines a Location action in an AWS IoT rule.

```
{
	"topicRulePayload": {
		"sql": "SELECT * FROM 'some/topic'",
		"ruleDisabled": false,
		"awsIotSqlVersion": "2016-03-23",
		"actions": [
			{
				"location": {
					"roleArn": "arn:aws:iam::123454962127:role/service-role/ExampleRole",
					"trackerName": "MyTracker",
					"deviceId": "001",
					"sampleTime": {
						"value": "${timestamp()}",
						"unit": "MILLISECONDS"
					},
					"latitude": "-12.3456",
					"longitude": "65.4321"
				}
			}
		]
	}
}
```

The following JSON example defines a Location action with substitution templates in an AWS IoT rule.

```
{
	"topicRulePayload": {
		"sql": "SELECT * FROM 'some/topic'",
		"ruleDisabled": false,
		"awsIotSqlVersion": "2016-03-23",
		"actions": [
			{
				"location": {
					"roleArn": "arn:aws:iam::123456789012:role/service-role/ExampleRole",
					"trackerName": "${TrackerName}",
					"deviceId": "${DeviceID}",
					"timestamp": {
						"value": "${timestamp()}",
						"unit": "MILLISECONDS"
					},
					"latitude": "${get(position, 0)}",
					"longitude": "${get(position, 1)}"
				}
			}
		]
	}
}
```

The following MQTT payload example shows how substitution templates in the preceding example accesses data. You can use the [**get-device-position-history**](https://docs.aws.amazon.com/cli/latest/reference/location/get-device-position-history.html) CLI command to verify that the MQTT payload data is delivered in your location tracker.

```
{
	"TrackerName": "mytracker",
	"DeviceID": "001",
	"position": [
		"-12.3456",
		"65.4321"
	]
}
```

```
aws location get-device-position-history --device-id {{001}} --tracker-name {{mytracker}}
```

```
{
	"DevicePositions": [
		{
			"DeviceId": "001",
			"Position": [
				-12.3456,
				65.4321
			],
			"ReceivedTime": "2022-11-11T01:31:54.464000+00:00",
			"SampleTime": "2022-11-11T01:31:54.308000+00:00"
		}
	]
}
```

## See also
<a name="location-rule-action-see-also"></a>
+ [What is Amazon Location Service?](https://docs.aws.amazon.com/location/latest/developerguide/welcome.html) in the *Amazon Location Service Developer Guide*.