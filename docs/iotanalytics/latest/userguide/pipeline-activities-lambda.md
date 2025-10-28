End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# AWS Lambda activity

You can use a **`lambda` activity** to perform complex
processing on messages. For example, you can enrich messages with data from the output of
external API operations, or filter for messages based on logic from Amazon DynamoDB. However, you can't
use this pipeline activity to add additional messages, or remove existing messages, before
entering a data store.

The AWS Lambda function used in a **`lambda` activity** must
receive and return an array of JSON objects. For an example, see [Lambda function example 1](#pipeline-activities-lambda-ex1 "#pipeline-activities-lambda-ex1").

To grant AWS IoT Analytics permission to invoke your Lambda function, you must add a policy. For
example, run the following CLI command and replace `exampleFunctionName`
with the name of your Lambda function, replace `123456789012`
with your AWS Account ID, and use the Amazon Resource Name (ARN) of the pipeline that invokes
the given Lambda function.

```
aws lambda add-permission --function-name `exampleFunctionName` --action lambda:InvokeFunction --statement-id iotanalytics --principal iotanalytics.amazonaws.com --source-account `123456789012` --source-arn arn:aws:iotanalytics:`us-east-1`:`123456789012`:pipeline/`examplePipeline`
```

The command returns the following:

```
{
    "Statement": "{\"Sid\":\"iotanalyticsa\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"iotanalytics.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:aws-region:aws-account:function:`exampleFunctionName`\",\"Condition\":{\"StringEquals\":{\"AWS:SourceAccount\":\"`123456789012`\"},\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:iotanalytics:`us-east-1`:`123456789012`:pipeline/`examplePipeline`\"}}}"
}
```

For more information, see [Using
resource-based policies for AWS Lambda](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md") in the
_AWS Lambda Developer Guide_.

## Lambda function example 1

In this example, the Lambda function adds information based on data in the original message.
A device publishes a message with a payload similar to the following example.

```
{
  "thingid": "00001234abcd",
  "temperature": 26,
  "humidity": 29,
  "location": {
    "lat": 52.4332935,
    "lon": 13.231694
  },
  "ip": "192.168.178.54",
  "datetime": "2018-02-15T07:06:01"
}
```

And the device has the following pipeline definition.

```
{
    "pipeline": {
        "activities": [
            {
                "channel": {
                    "channelName": "foobar_channel",
                    "name": "foobar_channel_activity",
                    "next": "lambda_foobar_activity"
                }
            },
            {
                "lambda": {
                    "lambdaName": "MyAnalyticsLambdaFunction",
                    "batchSize": 5,
                    "name": "lambda_foobar_activity",
                    "next": "foobar_store_activity"
                }
            },
            {
                "datastore": {
                    "datastoreName": "foobar_datastore",
                    "name": "foobar_store_activity"
                }
            }
        ],
        "name": "foobar_pipeline",
        "arn": "arn:aws:iotanalytics:eu-west-1:123456789012:pipeline/foobar_pipeline"
    }
}
```

The following Lambda Python function
(`MyAnalyticsLambdaFunction`) adds the GMaps URL and the temperature, in Fahrenheit,
to the message.

```
import logging
import sys

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

def c_to_f(c):
    return 9.0/5.0 * c + 32

def lambda_handler(event, context):
    logger.info("event before processing: {}".format(event))
    maps_url = 'N/A'

    for e in event:
        #e['foo'] = 'addedByLambda'
        if 'location' in e:
            lat = e['location']['lat']
            lon = e['location']['lon']
            maps_url = "http://maps.google.com/maps?q={},{}".format(lat,lon)

        if 'temperature' in e:
            e['temperature_f'] = c_to_f(e['temperature'])

        logger.info("maps_url: {}".format(maps_url))
        e['maps_url'] = maps_url

    logger.info("event after processing: {}".format(event))

    return event
```

## Lambda function example 2

A useful technique is to compress and serialize message payloads to reduce transport and
storage costs. In this second example, the Lambda function assumes that the message payload
represents a JSON original, which has been compressed and then base64-encoded (serialized) as a
string. It returns the original JSON.

```
import base64
import gzip
import json
import logging
import sys

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

def decode_to_bytes(e):
    return base64.b64decode(e)

def decompress_to_string(binary_data):
    return gzip.decompress(binary_data).decode('utf-8')

def lambda_handler(event, context):
    logger.info("event before processing: {}".format(event))

    decompressed_data = []

    for e in event:
        binary_data = decode_to_bytes(e)
        decompressed_string = decompress_to_string(binary_data)

        decompressed_data.append(json.loads(decompressed_string))

    logger.info("event after processing: {}".format(decompressed_data))

    return decompressed_data
```
