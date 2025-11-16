# Resolving device location using

AWS IoT Core Device Location MQTT topics

You can use reserved MQTT topics to get the latest location information for your
devices with the AWS IoT Core Device Location feature.

## Format of device location MQTT

topics

Reserved topics for AWS IoT Core Device Location use the following prefix:

`$aws/device_location/`{customer_device_id}`/`

To create a complete topic, first replace
`customer_device_id` with your unique
ID that you use for identifying your device. We recommend that you specify the
`WirelessDeviceId`, such as for LoRaWAN and Sidewalk devices, and
`thingName`, if your device is
registered as an AWS IoT thing. You then append the topic with the topic stub, such as
`get_position_estimate` or
`get_position_estimate/accepted` as shown in the following
section.

###### Note

The `{customer_device_id}` can only
contain letters, numbers, and dashes. When subscribing to device location
topics, you can only use the plus sign (+) as a wildcard character. For example,
you can use the `+` wildcard for the
`{customer_device_id}` to obtain
the location information for your devices. When you subscribe to the topic
`$aws/device_location/`+`/get_position_estimate/accepted`,
a message will be published with the location information for devices that match
any device ID if it was successfully resolved.

The following are the reserved topics used to interact with AWS IoT Core Device Location.

| Device location MQTT topics                                              | Topic     | Allowed operations                                                                                                                  | Description |
| ------------------------------------------------------------------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| $aws/device_location/`customer_device_id`/get_position_estimate          | Publish   | A device publishes to this topic to get the scanned raw<br>measurement data to be resolved by AWS IoT Core Device Location.         |
| $aws/device_location/`customer_device_id`/get_position_estimate/accepted | Subscribe | AWS IoT Core Device Location publishes the location information to this topic when<br>it successfully resolves the device location. |
| $aws/device_location/`customer_device_id`/get_position_estimate/rejected | Subscribe | AWS IoT Core Device Location publishes the error information to this topic when it<br>fails to resolve the device location.         |

## Policy for device location MQTT

topics

To receive messages from device location topics, your device must use a policy
that allows it to connect to the AWS IoT device gateway and subscribe to the MQTT
topics.

The following is an example of the policy required for receiving messages for the
various topics.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Publish"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:topic/$aws/device_location/`customer_device_id`/get_position_estimate"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Receive"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:topic/$aws/device_location/`customer_device_id`/get_position_estimate/accepted",
 "arn:aws:iot:`us-east-1`:`111122223333`:topic/$aws/device_location/`customer_device_id`/get_position_estimate/rejected"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Subscribe"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:topicfilter/$aws/device_location/`customer_device_id`/get_position_estimate/accepted",
 "arn:aws:iot:`us-east-1`:`111122223333`:topicfilter/$aws/device_location/`customer_device_id`/get_position_estimate/rejected"
 ]
 }
 ]
}`

```

## Device location topics and

payload

The following shows the AWS IoT Core Device Location topics, the format of their message payload, and
an example policy for each topic.

###### Topics

- [/get_position_estimate](#get-position-estimate "#get-position-estimate")
- [/get_position_estimate/accepted](#get-position-estimate-accepted "#get-position-estimate-accepted")
- [/get_position_estimate/rejected](#get-position-estimate-rejected "#get-position-estimate-rejected")

### /get_position_estimate

Publish a message to this topic to get the raw measurement data from the
device to be resolved by AWS IoT Core Device Location.

```
$aws/device_location/`customer_device_id`/get_position_estimate
```

AWS IoT Core Device Location responds by publishing to either [/get_position_estimate/accepted](#get-position-estimate-accepted "#get-position-estimate-accepted") or [/get_position_estimate/rejected](#get-position-estimate-rejected "#get-position-estimate-rejected").

###### Note

The message published to this topic must be a valid JSON payload. If the
input message is not in valid JSON format, you won't get any response. For
more information, see [Message
payload](#get-position-estimate-payload "#get-position-estimate-payload").

The message payload format follows a similar structure as the
AWS IoT Wireless API operation request body, [`GetPositionEstimate`](../../../iot-wireless/latest/apireference/API_GetPositionEstimate.md "../../../iot-wireless/latest/apireference/API_GetPositionEstimate.md"). It contains:

- An optional `Timestamp` string, which corresponds
  to the date and time the location was resolved. The
  `Timestamp` string can have a minimum length of 1
  and maximum length of 10.
- An optional `MessageId` string, which can be used
  to map the request to the response. If you specify this string,
  the message published to the
  `get_position_estimate/accepted` or
  `get_position_estimate/rejected` topics will
  contain this `MessageId`. The `MessageID`
  string can have a minimum length of 1 and maximum length of

256.

- The measurement data from the device that contains one or more
  of the following measurement types:

      + [`WiFiAccessPoint`](../../../iot-wireless/latest/apireference/API_WiFiAccessPoint.md "../../../iot-wireless/latest/apireference/API_WiFiAccessPoint.md")
      + [`CellTowers`](../../../iot-wireless/latest/apireference/API_CellTowers.md "../../../iot-wireless/latest/apireference/API_CellTowers.md")
      + [`IpAddress`](../../../iot-wireless/latest/apireference/API_Ip.md "../../../iot-wireless/latest/apireference/API_Ip.md")
      + [`Gnss`](../../../iot-wireless/latest/apireference/API_Gnss.md "../../../iot-wireless/latest/apireference/API_Gnss.md")

  The following shows a sample message payload.

```
{
    "Timestamp": `"1664313161"`,
    "MessageId": `"ABCD1"`,
    "WiFiAccessPoints":  [
        {
            "MacAddress": "`A0:EC:F9:1E:32:C1`",
            "Rss": `-66`
        }
    ],
    "Ip":{
        "IpAddress": `"54.192.168.0"`
    },
    "Gnss":{
      "Payload":`"8295A614A2029517F4F77C0A7823B161A6FC57E25183D96535E3689783F6CA48"`,
      "CaptureTime":`1354393948`
    }
}
```

The following is an example of the required policy:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Publish"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:topic/$aws/device_location/`customer_device_id`/get_position_estimate"
 ]
 }
 ]
}`

```

### /get_position_estimate/accepted

AWS IoT Core Device Location publishes a response to this topic when returning the resolved
location information for your device. The location information is returned in
[GeoJSON format](https://geojson.org/ "https://geojson.org/").

```
$aws/device_location/`customer_device_id`/get_position_estimate/accepted
```

The following shows the message payload and an example policy.

The following is an example of the message payload in GeoJSON format.
If you specified a `MessageId` in your raw measurement data
and AWS IoT Core Device Location resolved the location information successfully, then the
message payload returns the same `MessageId`
information.

```
{
    "coordinates": [
        13.37704086303711,
        52.51865005493164
    ],
    "type": "Point",
    "properties": {
        "verticalAccuracy": 707,
        "verticalConfidenceLevel": 0.68,
        "horizontalAccuracy": 389,
        "horizontalConfidenceLevel": 0.68,
        "country": "USA",
        "state": "CA",
        "city": "Sunnyvalue",
        "postalCode": "91234",
        "timestamp": "2022-11-18T14:03:57.391Z",
        "messageId": "ABCD1"
    }
}
```

The following is an example of the required policy:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Subscribe"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:topicfilter/$aws/device_location/`customer_device_id`/get_position_estimate/accepted"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Receive"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:topic/$aws/device_location/`customer_device_id`/get_position_estimate/accepted"
 ]
 }
 ]
}`

```

### /get_position_estimate/rejected

AWS IoT Core Device Location publishes an error response to this topic when it fails to resolve the
device location.

```
$aws/device_location/`customer_device_id`/get_position_estimate/rejected
```

The following shows the message payload and example policy. For information
about the errors, see [Troubleshooting errors when
resolving the location](device-location-resolve-solvers.md#location-resolve-troubleshoot "device-location-resolve-solvers.md#location-resolve-troubleshoot").

The following is an example of the message payload that provides the
error code and message, which indicates why AWS IoT Core Device Location failed to resolve
the location information. If you specified a `MessageId` when
providing your raw measurement data and AWS IoT Core Device Location failed to resolve the
location information, then the same `MessageId` information
will be returned in the message payload.

```
{
    "errorCode": 500,
    "errorMessage":"Internal server error",
    "messageId": "ABCD1"
}
```

The following is an example of the required policy:

```


```
