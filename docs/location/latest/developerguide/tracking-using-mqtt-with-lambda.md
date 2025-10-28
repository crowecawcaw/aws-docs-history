# Use AWS Lambda with MQTT

While using AWS Lambda is no longer required when sending device location data to
Amazon Location for tracking, you may still want to use Lambda in some cases. For example, if
you wish to process your device location data yourself, before sending it on to
Amazon Location. The following topics describe how to use Lambda to process messages before
sending them to your tracker. For more information about this pattern, see the [reference architecture](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/amazon-location-service-ra.pdf "https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/amazon-location-service-ra.pdf").

###### Topics

- [Prerequisite](#mqtt-prerequisite-with-lambda "#mqtt-prerequisite-with-lambda")
- [Create a Lambda function](#mqtt-with-lambda-create-lambda "#mqtt-with-lambda-create-lambda")
- [Create an AWS IoT Core rule](#mqtt-create-iot-rule-with-lambda "#mqtt-create-iot-rule-with-lambda")
- [Test your AWS IoT Core rule in the
  console](#mqtt-test-iot-rule-with-lambda "#mqtt-test-iot-rule-with-lambda")

## Prerequisite

Before you can begin tracking, you must [create a
tracker resource](start-tracking.md "start-tracking.md"). To create a tracker resource, you can use the Amazon Location
console, the AWS CLI, or the Amazon Location APIs.

The following example uses the Amazon Location Service console to create the tracker
resource:

1. Open the Amazon Location Service console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home "https://console.aws.amazon.com/location/home").
2. In the left navigation pane, choose **Trackers**.
3. Choose **Create tracker**.
4. Fill out the following boxes:
   - **Name** – Enter a unique name that has a maximum
     of 100 characters. Valid entries include alphanumeric characters,
     hyphens, and underscores. For example,
     `MyTracker`.
   - **Description** – Enter an optional description.
     For example, `Tracker for storing AWS IoT Core device
positions`.
   - **Position filtering** – Select the filtering
     that you want to use for position updates. For example,
     **Accuracy-based filtering**.

5. Choose **Create tracker**.

## Create a Lambda function

To create a connection between AWS IoT Core and Amazon Location Service, you need an AWS Lambda
function to process messages forwarded by AWS IoT Core. This function will extract any
positional data, format it for Amazon Location Service, and submit it through the Amazon Location Tracker
API. You can create this function through the AWS Lambda console, or you can use the
AWS Command Line Interface (AWS CLI) or the AWS Lambda APIs.

To create a Lambda function that publishes position updates to Amazon Location using the
console:

1. Open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/home "https://console.aws.amazon.com/lambda/home").
2. From the left navigation, choose **Functions**.
3. Choose **Create Function**, and make sure that
   **Author from scratch** is selected.
4. Fill out the following boxes:
   - **Function name** – Enter a unique name for your
     function. Valid entries include alphanumeric characters, hyphens,
     and underscores with no spaces. For example,
     `MyLambda`.
   - **Runtime** – Choose `Python
3.8`.

5. Choose **Create function**.
6. Choose the **Code** tab to open the editor.
7. Overwrite the placeholder code in `lambda_function.py` with the
   following, replacing the value assigned to `TRACKER_NAME` with
   the name of the tracker that you created as a [prerequisite](#mqtt-prerequisite-with-lambda "#mqtt-prerequisite-with-lambda").

```
from datetime import datetime
import json
import os

import boto3

# Update this to match the name of your Tracker resource
TRACKER_NAME = "MyTracker"

"""
This Lambda function receives a payload from AWS IoT Core and publishes device updates to
Amazon Location Service via the BatchUpdateDevicePosition API.

Parameter 'event' is the payload delivered from AWS IoT Core.

In this sample, we assume that the payload has a single top-level key 'payload' and a nested key
'location' with keys 'lat' and 'long'. We also assume that the name of the device is nested in
the payload as 'deviceid'. Finally, the timestamp of the payload is present as 'timestamp'. For
example:

>>> event
{ 'payload': { 'deviceid': 'thing123', 'timestamp': 1604940328,
  'location': { 'lat': 49.2819, 'long': -123.1187 },
  'accuracy': {'Horizontal': 20.5 },
  'positionProperties': {'field1':'value1','field2':'value2'} }
}

If your data doesn't match this schema, you can either use the AWS IoT Core rules engine to
format the data before delivering it to this Lambda function, or you can modify the code below to
match it.
"""
def lambda_handler(event, context):
  update = {
      "DeviceId": event["payload"]["deviceid"],
      "SampleTime": datetime.fromtimestamp(event["payload"]["timestamp"]).strftime("%Y-%m-%dT%H:%M:%SZ"),
      "Position": [
        event["payload"]["location"]["long"],
        event["payload"]["location"]["lat"]
        ]
    }
  if "accuracy" in event["payload"]:
      update["Accuracy"] = event["payload"]['accuracy']
  if "positionProperties" in event["payload"]:
      update["PositionProperties"] = event["payload"]['positionProperties']

  client = boto3.client("location")
  response = client.batch_update_device_position(TrackerName=TRACKER_NAME, Updates=[update])

  return {
    "statusCode": 200,
    "body": json.dumps(response)
  }
```

8. Choose **Deploy** to save the updated function.
9. Choose the **Configuration** tab.
10. In the **Permissions** section, choose the hyperlinked
    Role name to grant Amazon Location Service permissions to your Lambda function.
11. From your role's **Summary** page, choose **Add
    permissions**, and then from the dropdown list, select
    **Create inline policy**.
12. Choose the **JSON** tab, and overwrite the policy with
    the following document. This allows your Lambda function to update device
    positions managed by all tracker resources across all Regions.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "WriteDevicePosition",
      "Effect": "Allow",
      "Action": "geo:BatchUpdateDevicePosition",
      "Resource": "arn:aws:geo:*:*:tracker/*"
    }
  ]
}
```

13. Choose **Review policy**.
14. Enter a policy name. For example,
    `AmazonLocationTrackerWriteOnly`.
15. Choose **Create policy**.

You can modify this function code, as necessary, to adapt to your own device
message schema.

## Create an AWS IoT Core rule

Next, create an AWS IoT Core rule to forward your devices' positional telemetry to
the AWS Lambda function for transformation and publication to Amazon Location Service. The example
rule provided assumes that any necessary transformation of device payloads is
handled by your Lambda function. You can create this rule through the AWS IoT Core
console, the AWS Command Line Interface (AWS CLI), or the AWS IoT Core APIs.

###### Note

While the AWS IoT console handles the permission necessary to allow AWS IoT Core to
invoke your Lambda function, if you are creating your rule from the AWS CLI or SDK,
you must [configure a policy to grant permission to AWS IoT](../../../iot/latest/developerguide/lambda-rule-action.md#lambda-rule-action-requirements "../../../iot/latest/developerguide/lambda-rule-action.md#lambda-rule-action-requirements").

**To create an AWS IoT Core using the console**

1. Sign in to the AWS IoT Core console at [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home").
2. In the left navigation, expand **Act**, and choose
   **Rules**.
3. Choose **Create a rule** to start the new rule
   wizard.
4. Enter a name and description for your rule.
5. For the **Rule query statement**, update the
   `FROM` attribute to refer to a topic where at least one
   device is publishing telemetry that includes location. If you are testing
   the solution, no modification is needed.

```
SELECT * FROM '`iot/topic`'
```

6. Under **Set one or more actions** , choose **Add
   action**.
7. Select **Send a message to a lambda function**.
8. Choose **Configure action**.
9. Find and select your Lambda function from the list.
10. Choose **Add action**.
11. Choose **Create rule**.

## Test your AWS IoT Core rule in the

console

If no devices are currently publishing telemetry that includes location, you can
test your rule and this solution using the AWS IoT Core console. The console has a test
client where you can publish a sample message to verify the results of the
solution.

1. Sign in to the AWS IoT Core console at [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home").
2. In the left navigation, expand **Test**, and choose
   **MQTT test client**.
3. Under **Publish to a topic**, set the **Topic
   name** to `iot/topic` (or the name of
   the topic that you set up in your AWS IoT Core rule, if different), and provide
   the following for the **Message payload**. Replace the
   timestamp `1604940328` with a valid timestamp
   within the last 30 days (any timestamps older than 30 days are
   ignored).

```
{
  "payload": {
    "deviceid": "thing123",
    "timestamp": `1604940328`,
    "location": { "lat": 49.2819, "long": -123.1187 },
    "accuracy": { "Horizontal": 20.5 },
    "positionProperties": { "field1": "value1", "field2": "value2" }
  }
}
```

4. Choose **Publish** to topic to send the test
   message.
5. To validate that the message was received by Amazon Location Service, use the following
   AWS CLI command. If you modified them during setup, replace the tracker name
   and device id with the ones that you used.

```
aws location batch-get-device-position --tracker-name MyTracker --device-ids thing123
```
