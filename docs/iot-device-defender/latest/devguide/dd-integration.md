# Using AWS IoT Device Defender with other AWS services

## Using AWS IoT Device Defender with devices running AWS IoT Greengrass

AWS IoT Greengrass provides pre-built integration with AWS IoT Device Defender to monitor device behaviors on an
ongoing basis.

- [Integrate Device
  Defender with AWS IoT Greengrass V1](../../../greengrass/v1/developerguide/device-defender-connector.md "../../../greengrass/v1/developerguide/device-defender-connector.md")
- [Integrate Device
  Defender with AWS IoT Greengrass V2](../../../greengrass/v2/developerguide/device-defender-component.md "../../../greengrass/v2/developerguide/device-defender-component.md")

## Using AWS IoT Device Defender with FreeRTOS and embedded

devices

To use AWS IoT Device Defender on a FreeRTOS device, your device must have the [FreeRTOS Embedded C SDK](https://github.com/aws/amazon-freertos "https://github.com/aws/amazon-freertos") or the [AWS IoT Device Defender library](../../../embedded-csdk/latest/lib-ref/libraries/aws/device-defender-for-aws-iot-embedded-sdk/docs/doxygen/output/html/index.md "../../../embedded-csdk/latest/lib-ref/libraries/aws/device-defender-for-aws-iot-embedded-sdk/docs/doxygen/output/html/index.md") installed. The FreeRTOS Embedded C SDK includes
the AWS IoT Device Defender library. For information about how to integrate AWS IoT Device Defender with
your FreeRTOS devices, see the following demos:

- [AWS IoT Device Defender for FreeRTOS standard metrics and custom metrics demos](https://freertos.org/iot-device-defender-demo.html "https://freertos.org/iot-device-defender-demo.html")
- [Using MQTT
  agent to submit metrics to AWS IoT Device Defender](https://freertos.org/iot-device-defender/demo-with-mqtt-agent.html "https://freertos.org/iot-device-defender/demo-with-mqtt-agent.html")
- [Using the
  MQTT core library to submit metrics to AWS IoT Device Defender](../../../freertos/latest/userguide/dd-demo.md "../../../freertos/latest/userguide/dd-demo.md")

To use AWS IoT Device Defender on an embedded device without FreeRTOS, your device must have the [AWS IoT
Embedded C SDK](../../../iot/latest/developerguide/iot-embedded-c-sdk.md "../../../iot/latest/developerguide/iot-embedded-c-sdk.md") or [AWS IoT Device Defender library](../../../embedded-csdk/latest/lib-ref/libraries/aws/device-defender-for-aws-iot-embedded-sdk/docs/doxygen/output/html/index.md "../../../embedded-csdk/latest/lib-ref/libraries/aws/device-defender-for-aws-iot-embedded-sdk/docs/doxygen/output/html/index.md"). The AWS IoT Embedded C SDK includes the
AWS IoT Device Defender library. For information about how to integrate AWS IoT Device Defender with your
embedded devices, see the following demos, [AWS IoT Device Defender for AWS IoT Embedded SDK standard and custom metrics demos](https://github.com/aws/aws-iot-device-sdk-embedded-C/blob/main/docs/doxygen/demos/defender_demo.dox "https://github.com/aws/aws-iot-device-sdk-embedded-C/blob/main/docs/doxygen/demos/defender_demo.dox").

## Using AWS IoT Device Defender with AWS IoT Device Management

You can use AWS IoT Device Management fleet indexing to index, search, and aggregate your AWS IoT Device Defender detect
violations.

###### Note

The fleet indexing feature to support indexing AWS IoT Device Defender violations data is in preview
release for AWS IoT Device Management and is subject to change.

- [Managing fleet
  indexing](../../../iot/latest/developerguide/managing-fleet-index.md "../../../iot/latest/developerguide/managing-fleet-index.md")
- [Query
  syntax](../../../iot/latest/developerguide/query-syntax.md "../../../iot/latest/developerguide/query-syntax.md")
