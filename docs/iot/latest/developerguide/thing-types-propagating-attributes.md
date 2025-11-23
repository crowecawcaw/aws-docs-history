# Adding propagating attributes for

message enrichment

In AWS IoT Core, you can enrich MQTT messages from devices by adding propagating
attributes, which are contextual metadata from thing attributes or connection details.
This process, known as message enrichment, can be helpful in various scenarios. For
example, you can enrich messages for every inbound publish operation without making any
device side changes or needing to use rules. By leveraging propagating attributes, you
can benefit from a more efficient and cost-effective way to enrich your IoT data without
the complexities of configuring rules or managing republishing configurations.

The message enrichment feature is available to AWS IoT Core customers who use [basic
ingest](iot-basic-ingest.md "iot-basic-ingest.md") and [message broker](mqtt.md "mqtt.md"). It's important to
note while publishing devices can use any MQTT version, subscribers (applications or
services consuming messages) must support [MQTT 5](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html "https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html") to
receive the enriched messages with propagating attributes. The enriched messages will be
added as MQTT 5 user properties to every message published from devices. If you
use[rules](iot-rules.md "iot-rules.md"), you can leverage the [get_user_properties](iot-sql-functions.md#iot-sql-function-get-user-properties "iot-sql-functions.md#iot-sql-function-get-user-properties") function to retrieve the enriched data for message
routing or processing based on the data.

In AWS IoT Core, you can add propagating attributes when you create or update a thing
type, by using the AWS Management Console or the AWS CLI.

###### Important

When adding propagating attributes, you must make sure that the client publishing
the message has been authenticated with a certificate. For more information, see
[Client authentication](client-authentication.md "client-authentication.md").

###### Note

If you attempt to test this feature using the MQTT test client within console, it may not work since this feature requires MQTT clients authenticated with an associated certificate.

## AWS Management Console

###### To add propagating attributes for message enrichment using the

AWS Management Console

1. Open the [AWS IoT home
   page](https://console.aws.amazon.com//iot/home#/home "https://console.aws.amazon.com//iot/home#/home") in the AWS IoT console. On the left navigation, from
   **Manage**, choose **All
   devices**. Then choose **Thing types**.
2. On the **Thing types** page, choose **Create
   thing type**.

To configure message enrichment by updating a thing type, choose a
thing type. Then on the thing type details page, choose
**Update**. 3. On the **Create thing type** page, choose or enter
the thing type information in **Thing type
properties**.

If you choose to update a thing type, you will see **Thing
type properties** after you choose **Update**
in the previous step. 4. In **Additional configuration**, expand
**Propagating attributes**. Then choose **Thing
attribute** and enter the thing attribute you want to populate
to the published MQTT5 messages. Using the console, you can add up to three
thing attributes.

On the **Propagating attributes** section, choose
**Connection attribute** and enter the attribute
type and optionally the attribute name. 5. Optionally, add tags. Then choose **Create thing
type**.

If you choose to update a thing type, choose **Update thing
type**.

## AWS CLI

1. To add propagating attributes for message enrichment by creating a new
   thing type using the AWS CLI, run the [**create-thing-type**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-type.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-type.html") command.
   An example command can be the following.

```
aws iot create-thing-type \
    --thing-type-name "LightBulb" \
    --thing-type-properties "{\"mqtt5Configuration\":{\"propagatingAttributes\":[{\"userPropertyKey\":\"iot:ClientId\", \"connectionAttribute\":\"iot:ClientId\"}, {\"userPropertyKey\":\"test\", \"thingAttribute\":\"A\"}]}}" \
```

The output of the command can look like the following.

```
{
	"thingTypeName": "LightBulb",
	"thingTypeArn": "arn:aws:iot:us-west-2:123456789012:thingtype/LightBulb",
	"thingTypeId": "ce3573b0-0a3c-45a7-ac93-4e0ce14cd190"
}
```

2. To configure message enrichment by updating a thing type using AWS CLI,
   run the [**update-thing-type**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing-type.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing-type.html") command.
   Note that you can only update `mqtt5Configuration` when you run this command.
   An example command can be the following.

```
aws iot update-thing-type \
    --thing-type-name "MyThingType" \
    --thing-type-properties "{\"mqtt5Configuration\":{\"propagatingAttributes\":[{\"userPropertyKey\":\"iot:ClientId\", \"connectionAttribute\":\"iot:ClientId\"}, {\"userPropertyKey\":\"test\", \"thingAttribute\":\"A\"}]}}" \
```

This command doesn't produce any output. 3. To describe a thing type, run the `describe-thing-type`
command. This command will produce an output with message enrichment
configuration information in the `thing-type-properties`
field. An example command can be the following.

```
aws iot describe-thing-type \
    --thing-type-name "LightBulb"
```

The output can look like the following.

```
{
	"thingTypeName": "LightBulb",
	"thingTypeId": "bdf72512-0116-4392-8d79-bf39b17ef73d",
	"thingTypeArn": "arn:aws:iot:us-east-1:123456789012:thingtype/LightBulb",
	"thingTypeProperties": {
		"mqtt5Configuration": {
			"propagatingAttributes": [
				{
					"userPropertyKey": "iot:ClientId",
					"connectionAttribute": "iot:ClientId"
				},
				{
					"userPropertyKey": "test",
					"thingAttribute": "attribute"
				}
			]
		}
	},
	"thingTypeMetadata": {
		"deprecated": false,
		"creationDate": "2024-10-18T17:37:46.656000+00:00"
	}
}
```

For more information, see [Thing types](thing-types.md "thing-types.md").
