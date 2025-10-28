# Add a destination for your

Sidewalk end device

AWS IoT Core for Amazon Sidewalk destinations describe the AWS IoT rule that processes a device's data for
use by other AWS services and applications. Use AWS IoT rules to process the data and
device messages and route it to other services.

Because most Sidewalk devices don't send data to AWS IoT Core for Amazon Sidewalk in a format that can
be used by AWS services, an AWS IoT rule must process it first. The AWS IoT rule contains
the SQL statement that interprets the device's data and the topic rule actions that send
the result of the SQL statement to the services that will use it.

The AWS IoT rule processes binary messages received from a device and converts the
messages to other formats that make other services easy to use them. Destinations
associate your Sidewalk end device with the rule that processes the device data
to send to other AWS services. For more information about rules, see [Rules for
AWS IoT](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md") in the _AWS IoT Core documentation_.

## How to create and use a

destination

1. Create an AWS IoT rule and an IAM role for the destination. The AWS IoT rule
   specifies the rules that will process the device's data and routes it for
   use by other AWS services and your applications. The IAM role grants
   permission to access the rule.
2. Create a destination for your Sidewalk devices using the
   `CreateDestination` API operation. Specify the destination
   name, rule name, role name, and any optional parameters. The API will return
   a unique identifier for the destination, which you can specify when adding
   your end device to AWS IoT Core for Amazon Sidewalk.

The following shows how to create a destination, and an AWS IoT rule and IAM role for
the destination.

###### Topics

- [Create a destination for your
  Sidewalk device](iot-sidewalk-destination-create.md "iot-sidewalk-destination-create.md")
- [Create an IAM role and IoT rule
  for your destination](sidewalk-destination-rule-role.md "sidewalk-destination-rule-role.md")
