# Integrate data into SiteWise Edge using an MQTT-enabled, V3 gateway

This tutorial guides you through integrating third-party devices and sensors that use MQTT messaging protocol with the AWS IoT SiteWise MQTT-enabled, V3 gateway. You will learn how to set up an AWS IoT SiteWise edge gateway to collect and monitor data from your MQTT-enabled devices. AWS IoT SiteWise enables you to collect, process, and monitor industrial equipment data. Use SiteWise Edge capabilities to optimize industrial IoT operations, and transform raw data into actionable insights.

In this tutorial, we use data from a wind farm demonstration to illustrate key concepts. After you become familiar with the process, you can repeat the tutorial with your own data.

After you complete this tutorial, you can do the following items:

- Set up and configure an MQTT-enabled, V3 gateway to receive data from industrial devices
- Process and validate incoming MQTT messages from your equipment at the edge
- View device data in AWS IoT SiteWise using a third-party visualization platform
- Send processed data from your edge gateway to the AWS Cloud to enable centralized storage and further analysis
  Additionally, you can leverage your edge gateway capabilities by connecting to other AWS IoT services to perform the following tasks:

- Configure AWS IoT rules to route data to services like [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"), [Amazon Timestream](https://aws.amazon.com/timestream/ "https://aws.amazon.com/timestream/"), and [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/").
- Use [AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/ "https://aws.amazon.com/iot-device-defender/") to remotely manage and update your gateway configurations.
- Implement secure device authentication and authorization using AWS IoT security features. For more information, see [AWS IoT security](../../../iot/latest/developerguide/iot-security.md "../../../iot/latest/developerguide/iot-security.md") in the _AWS IoT Developer Guide_.
- Create automated alerts and notifications based on equipment data. For more information, see [Rules for AWS IoT](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md") in the _AWS IoT Developer Guide_.

###### Note

This tutorial references third-party services, tools, and documentation. AWS isn't a vendor or supplier for any third-party products or services, and can't guarantee the accuracy of information from external providers. Evaluate and validate all third-party tools before deployment.

###### Topics

- [Prerequisites](#gateway-tutorial-prerequisites "#gateway-tutorial-prerequisites")
- [Step 1: Create an AWS IoT policy](#gateway-tutorial-create-iot-policy "#gateway-tutorial-create-iot-policy")
- [Step 2: Create and configure an AWS IoT thing](#gateway-tutorial-create-and-configure-aws-iot-thing "#gateway-tutorial-create-and-configure-aws-iot-thing")
- [Step 3: Configure your SiteWise Edge MQTT-enabled, V3 gateway](#gateway-tutorial-configure-your-edge-gateway "#gateway-tutorial-configure-your-edge-gateway")
- [Step 4: Install SiteWise Edge gateway software](#install-gateway-software "#install-gateway-software")
- [Step 5: Configure the EMQX broker to connect to external applications](#configure-emqx-broker-external-applications "#configure-emqx-broker-external-applications")
- [Step 6: Publish data with Mosquitto](#add-mqtt-data-source "#add-mqtt-data-source")
- [Step 7: Specify destinations](#specify-destinations "#specify-destinations")
- [Step 8: Specify path filters](#specify-path-filters "#specify-path-filters")
- [Step 9: Configure your AWS IoT resources](#configure-iot-resources "#configure-iot-resources")
- [Step 10: Visualize your data](#visualize-your-data "#visualize-your-data")
- [Step 11: Clean up resources after the tutorial](#tutorial-clean-up-resources "#tutorial-clean-up-resources")
- [Additional resources](#additional-resources "#additional-resources")

## Prerequisites

To complete this tutorial, you need the following:

- An AWS account. If you don't have one, see [Set up an AWS account](getting-started.md#set-up-aws-account "getting-started.md#set-up-aws-account").
- An AWS Identity and Access Management (IAM) user with administrator permissions. For more information, see [Identity and access management for AWS IoT SiteWise](security-iam.md "security-iam.md").
- The latest version of Python installed on your device.

###### Important

This tutorial requires the use of resources created in the [Ingest data](ingest-data-from-iot-things.md "ingest-data-from-iot-things.md") tutorial. You must complete it before proceeding with this tutorial.

## Step 1: Create an AWS IoT policy

This tutorial uses the AWS IoT policy you created in the [Ingest data](ingest-data-from-iot-things.md "ingest-data-from-iot-things.md") tutorial. This policy sets the security rules for your devices and creates a digital representation of your external devices and sensors in AWS IoT. The policy allows your third-party devices to send data to AWS IoT Core using MQTT (Message Queuing Telemetry Transport). For more information about MQTT messages, see [What is MQTT?](https://aws.amazon.com/what-is/mqtt/ "https://aws.amazon.com/what-is/mqtt/").

Console
Ensure completion of an AWS IoT policy. For detailed instructions, see [Step 1](ingest-data-from-iot-things.md#ingestion-tutorial-create-iot-policy "ingest-data-from-iot-things.md#ingestion-tutorial-create-iot-policy") in the [Ingest data](ingest-data-from-iot-things.md "ingest-data-from-iot-things.md") tutorial.

**To verify you have an active AWS IoT policy**

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. In the left navigation pane, choose **Securities**, then **Policies**.
3. Choose the policy you created. For example, `SiteWiseTutorialDevicePolicy`.
4. Confirm that the policy's status is listed as Active.

AWS CLI
Ensure completion of an AWS IoT policy. For detailed instruction, see [Step 1](ingest-data-from-iot-things.md#ingestion-tutorial-create-iot-policy "ingest-data-from-iot-things.md#ingestion-tutorial-create-iot-policy") in the [Ingest data](ingest-data-from-iot-things.md "ingest-data-from-iot-things.md") tutorial.

Use the following AWS CLI [get-policy](../../../cli/latest/reference/iot/get-policy.md "../../../cli/latest/reference/iot/get-policy.md") command in the _AWS CLI Command Reference_ to verify you have an active AWS IoT policy:

```
aws iot get-policy --policy-name "SiteWiseTutorialDevicePolicy"
```

This policy enables your AWS IoT devices to establish connections and to communicate with device shadows using MQTT messages. To interact with device
shadows, your AWS IoT things publish and receive MQTT messages on topics that start with `$aws/things/`thing-name`/shadow/`. This policy incorporates a thing policy variable known as `${iot:Connection.Thing.ThingName}`. This variable substitutes the connected
thing's name in each topic. The `iot:Connect` statement sets limitations on which devices can establish connections, ensuring that the thing policy variable can only substitute names starting with `SiteWiseTutorialDevice`.

For more information, see [Thing policy variables](../../../iot/latest/developerguide/iot-policy-variables.md "../../../iot/latest/developerguide/iot-policy-variables.md") in the _AWS IoT Developer Guide_.

###### Note

This policy applies to things whose names start with `SiteWiseTutorialDevice`. To use a different name for your things, you must update the policy accordingly.

## Step 2: Create and configure an AWS IoT thing

In this step, register your edge device as an AWS IoT thing and generate your thing’s certificates and keys needed for
secure communication with AWS IoT SiteWise Edge. This process establishes the foundation for your device to send third-party data through your MQTT-enabled, V3 gateway.

Console
Ensure completion of the creation and configuration steps for an AWS IoT thing. For detailed instructions, see [Step 2](ingest-data-from-iot-things.md#rule-tutorial-create-iot-thing "ingest-data-from-iot-things.md#rule-tutorial-create-iot-thing") in the [Ingest data](ingest-data-from-iot-things.md "ingest-data-from-iot-things.md") tutorial.

**To verify you have an active AWS IoT thing**

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. In the left navigation pane, choose **All devices**, then **Things**.
3. Choose the thing you created. For example, `SiteWiseTutorialDevice1`.
4. Under **Certificates**, confirm that the status is listed as active.

AWS CLI
Ensure completion of the creation and configuration steps for an AWS IoT thing. For detailed instructions, see [Step 2](ingest-data-from-iot-things.md#rule-tutorial-create-iot-thing "ingest-data-from-iot-things.md#rule-tutorial-create-iot-thing") in the [Ingest data](ingest-data-from-iot-things.md "ingest-data-from-iot-things.md") tutorial.

Use the following AWS CLI command to verify you have an active AWS IoT policy:

```
 aws iot describe-thing --thing-name "SiteWiseTutorialDevice1"
```

After completing these steps, you can securely connect your device to AWS IoT SiteWise Edge. You created a local directory to store your certificates and keys you generated for MQTT authentication. Your device is registered as an AWS IoT thing in the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/"), and your device is prepared to integrate data with SiteWise Edge. You can connect your industrial equipment or other devices to the AWS IoT platform and start ingesting data into SiteWise Edge.

## Step 3: Configure your SiteWise Edge MQTT-enabled, V3 gateway

In this step, create your AWS IoT SiteWise Edge MQTT-enabled, V3 gateway and configure it to receive data from the EMQX broker. The gateway acts as a bridge between your devices and AWS IoT. This allows you to process data locally at the edge before sending it to the AWS Cloud. This configuration reduces bandwidth and decreases cloud processing delays.

Console
**To create your AWS IoT SiteWise MQTT-enabled, V3 gateway**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and open the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation pane, choose **Edge gateways**, then choose **Create gateway**.
3. Under **Deployment target**, choose **Self-hosted gateway**.
4. Under Self-hosted gateway options, choose **MQTT-enabled, V3 gateway - _recommended_**.
5. Under **Gateway configuration**:
   1. In **Gateway name**, enter a name for your gateway. For example, `SiteWise Tutorial Device Gateway`.
   2. In **Greengrass device OS**, select the appropriate option for your device.

6. Under **Advanced configuration**:
   1. Choose **Default setup**.
   2. Enter a name for the Greengrass core device or use the name generated by AWS IoT SiteWise.

7. Choose **Create gateway**.
8. In the confirmation dialog, choose **Generate and download** to generate an installer for your SiteWise Edge gateway. For more information, see [Create a self-hosted SiteWise Edge gateway](create-gateway-ggv2.md#configure-gateway-console "create-gateway-ggv2.md#configure-gateway-console").

###### Warning

Store the installer file in a secure location. This file can't be regenerated, and is needed to complete the gateway setup in later steps.

AWS CLI
Use AWS CLI to create a self-hosted gateway. You need to provide a name for the gateway, specify the platform and gateway version. For more information, see [CreateGateway](../APIReference/API_CreateGateway.md "../APIReference/API_CreateGateway.md") in the _AWS IoT SiteWise API Reference_.

To use this example, replace the user input placeholders with your own information.

```
aws iotsitewise create-gateway \
    --gateway-name SiteWise Tutorial Device Gateway \
    --gateway-platform greengrassV2={coreDeviceThingName=`your-core-device-thing-name`, coreDeviceOperatingSystem=`LINUX_AMD64`} \
    --gateway-version `3` \
    [--cli-input-json `your-configuration`]
```

- `gateway-name` – A unique name for the gateway, for example, `SiteWise Tutorial Device Gateway`.
- `gateway-platform` – Enter `greengrassV2`. For more information, see [CreateGateway](../APIReference/API_CreateGateway.md "../APIReference/API_CreateGateway.md") in the _AWS IoT SiteWise API Reference_.
  - `coreDeviceThingName` – The name of the AWS IoT thing for your AWS IoT Greengrass V2 core device. For example, `SiteWiseTutorialDevice1`.
  - `coreDeviceOperatingSystem` – The operating system of the core device in AWS IoT Greengrass V2. Specifying the operating system is required for gateway-version 3. Options include: `LINUX_AARCH64`, `LINUX_AMD64`, and `WINDOWS_AMD64`.

- `gateway-version` – The version of the gateway.
  - Use `3` for the gateway version to create an MQTT-enabled, V3 gateway.

- `cli-input-json` – A JSON file containing request parameters.

Use the following AWS CLI command to verify that your gateway was created successfully:

```
aws iotsitewise describe-gateway --gateway-id `your-gateway-id`
```

## Step 4: Install SiteWise Edge gateway software

To install the gateway software, use the installer package that you downloaded in the previous step. The installation process configures the necessary components, starts the Greengrass core service, and registers your device with AWS IoT Greengrass. After installation is complete, verify that your gateway appears in the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/") under **Edge gateways** and that the Greengrass service is running properly on your device.

For detailed instructions, see [Install the AWS IoT SiteWise Edge
gateway software on your local device](install-gateway-software-on-local-device.md "install-gateway-software-on-local-device.md").

## Step 5: Configure the EMQX broker to connect to external applications

###### Note

You must have deployed your SiteWise Edge MQTT-enabled, V3 gateway before proceeding. The gateway provides the necessary infrastructure and security settings required for configuring the EMQX broker. The broker configuration will fail without an active gateway deployment.

Configure the EMQX broker to enable secure communication between your IoT devices and external applications. The EMQX broker functions as a central messaging hub that routes data between your IoT devices, gateway, and applications. The EMQX broker ensures reliable message delivery on your gateway and connected applications at the edge. For more information, see [Connect external applications
to the EMQX broker](connect-external-applications-emqx.md "connect-external-applications-emqx.md").

**To configure the EMQX broker**

1. Set up the EMQX broker. For detailed configuration instructions, follow Steps 1-14 in [Update the EMQX deployment configuration for authentication](configure-emqx-broker.md#update-emqx-broker-authentication "configure-emqx-broker.md#update-emqx-broker-authentication").
2. Set up MQTT topics for wind farm monitoring. For more information on MQTT requirements, see [MQTT topic
   requirements](connect-broker-payload-format.md#connect-broker-mqtt-requirements "connect-broker-payload-format.md#connect-broker-mqtt-requirements").
   1. CPU Usage: `SiteWiseTutorialDevice/cpu`
   2. Memory Usage: `SiteWiseTutorialDevice/memory`
   3. Timestamp: `SiteWiseTutorialDevice/timestamp`

3. Review your configuration and complete the deployment.
   1. Choose **Confirm** to save your settings.
   2. Choose **Next** until you reach the **Review** step.
   3. On the **Review** page, choose **Deploy**.
   4. Wait for the deployment to complete successfully before proceeding.

4. Prepare messages using the payload format to send to the EMQX broker. For more information about structuring payloads, see [Update the EMQX deployment configuration for authentication](configure-emqx-broker.md#update-emqx-broker-authentication "configure-emqx-broker.md#update-emqx-broker-authentication").
5. Implement the following security measures:
   1. Use Transport Layer Security (TLS) encryption (port 8833) to protect data in transit. For more information, see [Configure TLS for secure
      connections to the EMQX broker on AWS IoT SiteWise Edge](connect-app-to-broker.md#configure-tls-emqx-broker "connect-app-to-broker.md#configure-tls-emqx-broker").
   2. Set up username and password authentication to verify device identities. This security measure helps protect your data, and ensures only authorized devices can connect to your system. For more information, see [Enable username and
      password authentication](configure-emqx-broker.md#emqx-broker-username-password-auth "configure-emqx-broker.md#emqx-broker-username-password-auth").

EMQX allows you to create authorization rules based on identifiers such as username, IP address, or client ID. This is useful for controlling access to your data. For more information, see [Set up authorization rules for
AWS IoT SiteWise Edge in EMQX](authorization-rules-emqx-broker.md "authorization-rules-emqx-broker.md").

After successful deployment, your EMQX broker is configured and ready to securely connect with external applications.

###### Note

The payload format must follow a specific structure for AWS IoT SiteWise Edge to properly process and ingest your data. For more information about the required structure, see [JSON payload structure](connect-broker-payload-format.md#connect-broker-json-payload "connect-broker-payload-format.md#connect-broker-json-payload").

**Example: Add CPU, memory, and timestamp JSON payloads**

**CPU JSON payload**

```
{
  "propertyAlias": "SiteWiseTutorialDevice/cpu",
  "propertyValues": [
    {
      "quality": "GOOD",
      "timestamp": {
        "offsetInNanos": 0,
        "timeInSeconds": 1753206441
      },
      "value": {
        "integerValue": 45.2
      }
    }
  ]
}
```

**Memory JSON payload**

```
{
  "propertyAlias": "SiteWiseTutorialDevice/memory",
  "propertyValues": [
    {
      "quality": "GOOD",
      "timestamp": {
        "offsetInNanos": 0,
        "timeInSeconds": 1753206441
      },
      "value": {
        "integerValue": 67.8
      }
    }
  ]
}
```

**Timestamp JSON payload**

```
{
  "propertyAlias": "SiteWiseTutorialDevice/timestamp",
  "propertyValues": [
    {
      "quality": "GOOD",
      "timestamp": {
        "offsetInNanos": 0,
        "timeInSeconds": 1753206441
      },
      "value": {
        "integerValue": 23.5
      }
    }
  ]
}
```

###### Note

Each JSON payload must be published separately as an individual message. Don't combine multiple property values into a single message. Send each CPU, memory, and timestamp payload as its own distinct MQTT publication.

The payload defines the required JSON structure that your IoT devices must use to send device data through the EMQX broker to SiteWise Edge. This format ensures that AWS IoT SiteWise can identify your devices and process the sensor readings. After you implement these configurations and payload structures, your wind farm monitoring system is ready to collect and process data.

## Step 6: Publish data with Mosquitto

After creating your MQTT-enabled, V3 gateway, configure Eclipse Mosquitto to send test data to SiteWise Edge. Mosquitto is an open-source MQTT message broker that uses the MQTT protocol for lightweight messaging between devices. The Mosquitto client allows you to publish messages to MQTT topics, simulating data from wind farm sensors. Using Mosquitto, simulate device data without requiring any third-party services or additional equipment. For more information, see [documentation](https://mosquitto.org "https://mosquitto.org") on the official Eclipse Mosquitto website. In this tutorial, local data from the [Ingest data](ingest-data-from-iot-things.md "ingest-data-from-iot-things.md") tutorial and fictitious data are being used for demonstration purposes.

**Use Mosquitto CLI client to test the SiteWise Edge EMQX broker**

1. Install Mosquitto on your local device. For detailed instructions, see [Download Mosquitto](https://mosquitto.org/download/ "https://mosquitto.org/download/") on the official Eclipse Mosquitto website.
2. For more information about connecting external applications to transfer industrial data, see [Connect external applications
   to the EMQX broker](connect-external-applications-emqx.md "connect-external-applications-emqx.md").

###### Important

Ensure that the MQTT connection settings you configure here match the settings used in Mosquitto publish command. The host must be the IP address or hostname of your SiteWise Edge gateway. The port is typically 1883 (or 8883 if using SSL/TLS).

Use Mosquitto to publish test data. Open a command line and run the following commands:

**Example: CPU property**

```
mosquitto_pub -h localhost -p 1883 -t "SiteWiseTutorialDevice/cpu" -m '{
  "propertyAlias": "SiteWiseTutorialDevice/cpu",
  "propertyValues": [
    {
      "quality": "GOOD",
      "timestamp": {
        "timeInSeconds": 1753206441,
        "offsetInNanos": 0
      },
      "value": {
        "integerValue": 45.2
      }
    }
  ]
}'
```

**Example: Memory property**

```
mosquitto_pub -h localhost -p 1883 -t "SiteWiseTutorialDevice/memory" -m '{
  "propertyAlias": "SiteWiseTutorialDevice/memory",
  "propertyValues": [
    {
      "quality": "GOOD",
      "timestamp": {
        "timeInSeconds": 1753206441,
        "offsetInNanos": 0
      },
      "value": {
        "integerValue": 72.1
      }
    }
  ]
}'
```

**Example: Timestamp property**

```
mosquitto_pub -h localhost -p 1883 -t "SiteWiseTutorialDevice/timestamp" -m '{
  "propertyAlias": "SiteWiseTutorialDevice/timestamp",
  "propertyValues": [
    {
      "quality": "GOOD",
      "timestamp": {
        "timeInSeconds": 1753206441,
        "offsetInNanos": 0
      },
      "value": {
        "integerValue": 1683000000
      }
    }
  ]
}'
```

###### Note

The use of `localhost` as the EMQX broker address is for demonstration purposes only. In production environments or when connecting from external devices, you must use the appropriate EMQX broker address for your specific deployment configuration. For detailed connection instructions, see [Connect an application to the EMQX
broker on AWS IoT SiteWise Edge](connect-app-to-broker.md "connect-app-to-broker.md").

## Step 7: Specify destinations

In this step, specify destinations to determine where to direct your source data. Use AWS IoT SiteWise with Amazon S3 buffering as your destination. This option provides a scalable way to store and process your IoT data.

Console
**To add destinations**

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/") and select **Edge gateways**.
2. Under **SiteWise Tutorial Device Gateway**, choose **Add destinations**.
3. Under **Destination details**, choose **AWS IoT SiteWise buffered using Amazon S3**. To learn more about destination types, see [AWS IoT SiteWise gateway destinations](gw-destinations.md#source-destination "gw-destinations.md#source-destination").
4. Under **Destination name**, enter a name for your destination, for example, `SiteWise Tutorial S3 Destination`.
5. Under **S3 upload settings**, enter your S3 bucket location. For example, `s3://sitewise-tutorial-mqtt-data-[your-account-id]`. To learn more about Amazon S3, see [Creating, configuring, and working with Amazon S3 buckets](../../../AmazonS3/latest/userguide/creating-buckets-s3.md "../../../AmazonS3/latest/userguide/creating-buckets-s3.md") in the _Amazon Simple Storage Service User Guide_.
6. Under **Data upload frequency**, enter a value between 1 minute and 30 days. For example, `1 minute`.
7. Under **Data storage settings**:
   1. Deselect **Copy data to storage**. While this setting is recommended for production environments, you don't need it for this tutorial. When you deselect this option, the **Delete data from S3** option is automatically deselected.

8. Choose **Add destination**.

###### Note

This tutorial uses a 1-minute interval for testing. After you complete the tutorial, you can adjust this interval to match your production needs or delete it to avoid additional charges.

AWS CLI
**Example: Create a new AWS IoT SiteWise destination buffered using Amazon S3**

Use the [update-gateway-capability-configuration](../../../cli/latest/reference/iotsitewise/update-gateway-capability-configuration.md "../../../cli/latest/reference/iotsitewise/update-gateway-capability-configuration.md") in the _AWS CLI Command Reference_ to configure the publisher. Set the `capabilityNamespace` parameter to `iotsitewise:publisher:3`.

```
{
    "sources": [
      {
        "type": "MQTT"
      }
    ],
    "destinations": [
      {
        "type": "SITEWISE_BUFFERED",
        "name": "your-s3-destination-name",
        "config": {
          "targetBucketArn": "arn:aws:s3:::amzn-s3-demo-bucket/Optional/SomeFolder",
          "publishPolicy": {
            "publishFrequency": "1m",
            "localSizeLimitGB": 10
          },
          "siteWiseImportPolicy": {
            "enableSiteWiseStorageImport": true,
            "enableDeleteAfterImport": true,
            "bulkImportJobRoleArn": "arn:aws:iam::123456789012:role/your-role-name"
          }
        },
        "filters": [
          {
            "type": "PATH",
            "config": {
              "paths": [
                "#"
              ]
            }
          }
        ]
      }
    ]
  }

```

For more information about destinations, see [Add an AWS IoT SiteWise buffered destination using Amazon S3](destinations-buffered.md "destinations-buffered.md").

## Step 8: Specify path filters

In this step, configure path filters to specify which MQTT topics to monitor for your wind farm device data.

Path filters follow the MQTT topic wildcard specification, which supports two special characters:

- `+` – This symbol represents a single-level wildcard, which matches any string at a single level.
- `#` – This symbol represents a multi-level wildcard, which matches any number of levels in the topic hierarchy.

###### Note

For more information about other path filters, see [Special characters in path filter
names](gw-destinations.md#path-filters-special-characters "gw-destinations.md#path-filters-special-characters").

Console
**To configure your path filters**

Under **Path filters**:

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/") and select **Edge gateways**.
2. Under **SiteWise Tutorial Device Gateway**, choose **Add destinations**.
3. Choose **Add path filters** to enter the following path filters manually:
   - `SiteWiseTutorialDevice/#`
   - `windfarm/+/turbine/+/performance/#`
   - `cpu/+/idle-time`
   - `cpu/+/interruption-count/+`
   - `+/memory/consumption`
   - `timestamp/+/measurement`
   - `device/+/status/+`
   - `system/+/performance-log`

4. Choose **Add destination**.

For more information about best practices for path filters, see [Best practices for path filters](gw-destinations.md#create-effective-path-filters "gw-destinations.md#create-effective-path-filters").

AWS CLI
Use the following AWS CLI commands to configure your path filters:

**Example 1: Device data using wildcard**

```
{
 "destinations": [
   {
     "name": "All Device Data Destination"
   }
 ],
 "filters": [
   {
     "type": "PATH",
     "config": {
       "paths": [
         "SiteWiseTutorialDevice/#",
         "windfarm/+/turbine/+/performance/#"
       ]
     }
   }
 ]
}
```

This path filter configuration uses multi-level wildcards (#) to capture all data from the SiteWiseTutorialDevice and all performance data from any turbine in the wind farm.

**Example 2: CPU and memory performance**

```
{
 "destinations": [
   {
     "name": "Performance Metrics Destination"
   }
 ],
 "filters": [
   {
     "type": "PATH",
     "config": {
       "paths": [
         "cpu/+/idle-time",
         "+/memory/consumption",
         "cpu/+/interruption-count/+"
       ]
     }
   }
 ]
}

```

This example captures various CPU metrics (idle time and interruption count) and memory consumption data across devices.

**Example 3: Device diagnostics**

```
{
 "destinations": [
   {
     "name": "Device Diagnostics Destination"
   }
 ],
 "filters": [
   {
     "type": "PATH",
     "config": {
       "paths": [
        "device/+/status/+",
        "system/+/performance-log"
       ]
     }
   }
 ]
}

```

This configuration uses the `+` wildcard to capture diagnostic data from multiple devices, specifically system performance logs and device status updates.

These three path filters match the MQTT topics that you use to publish test data with Mosquitto. The filters ensure your SiteWise Edge gateway captures and processes the relevant MQTT messages. For more information on how to add path filters, see [Add path filters to AWS IoT SiteWise Edge
destinations](destinations-add-path-filters.md "destinations-add-path-filters.md").

## Step 9: Configure your AWS IoT resources

In this step, create the necessary AWS IoT SiteWise asset models and assets to represent your simulated third-party devices and enable data ingestion through your edge gateway.

Before starting this step, you should have completed steps 3 to 8 in the [Ingest data](ingest-data-from-iot-things.md "ingest-data-from-iot-things.md") tutorial. These steps establish the foundational components to integrate your third-party data through the MQTT-enabled V3 gateway. You also set up rules that define how your sensor data flows into AWS IoT SiteWise, and run a device client script that simulates industrial wind farm data.

**To validate your AWS IoT resource configuration**

1. Use the following AWS CLI command to verify you created and properly configured your SiteWise Tutorial Device Model and SiteWise Tutorial Device Fleet Model:

```
aws iotsitewise describe-asset-model --asset-model-id `your-device-model-id`
```

Use the following AWS CLI command to retrieve your asset models' ID:

```
aws iotsitewise list-asset-models
```

2. Use the following AWS CLI command to verify you created and properly configured your SiteWise Tutorial Device 1 asset and SiteWise Tutorial Device Fleet 1 asset:

```
aws iotsitewise describe-asset --asset-id `your-asset-id`
```

Use the following AWS CLI command to retrieve your assets' ID:

```
aws iotsitewise list-assets
```

## Step 10: Visualize your data

Set up the open-source version of Grafana to visualize your wind farm device data. Grafana is a visualization platform that displays your real-time operational data. These dashboards help you track operational efficiency and identify maintenance needs across your infrastructure. For more information about integration, see [Integrate AWS IoT SiteWise with Grafana](grafana-integration.md "grafana-integration.md").

**To setup Grafana**

1. For instructions to download and install the latest version of Grafana, see [Install Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/#install-grafana "https://grafana.com/docs/grafana/latest/setup-grafana/installation/#install-grafana") on the official Grafana website.
2. For detailed configuration instructions specific to your operating system, see [Configure Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#configure-grafana "https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#configure-grafana") on the official Grafana website.
3. Configure the AWS IoT SiteWise data source. This allows you to set up the AWS IoT SiteWise plugin on your Grafana server. For detailed instructions about how to use the plugin, see [Connect to an AWS IoT SiteWise data source](../../../grafana/latest/userguide/using-iotsitewise-in-AMG.md "../../../grafana/latest/userguide/using-iotsitewise-in-AMG.md") in the _Amazon Managed Grafana User Guide_.

###### Important

Ensure you have the latest version of Grafana for compatibility with the AWS IoT SiteWise data source.

After completing these steps, you can build and customize Grafana dashboards to display your wind farm's operational metrics. This enables you to track and analyze your wind farm performance at the edge in real time.

###### Note

While this tutorial uses the open-source version of Grafana, AWS also offers Amazon Managed Grafana for production environments. Amazon Managed Grafana is a fully managed service that eliminates the need to set up, configure, and maintain your own Grafana servers.

Consider upgrading to Amazon Managed Grafana when you're ready to scale your solution. For detailed instructions on how to connect your SiteWise data to Grafana, see the [Visualize and share data in Grafana](visualize-with-grafana.md "visualize-with-grafana.md") tutorial.

You have completed the tutorial. In this procedure, you configured AWS IoT SiteWise Edge to integrate third-party device data using an MQTT-enabled, V3 gateway. This setup allows you to collect, process, and visualize industrial equipment data at the edge, reducing latency and operational costs. By using the wind farm demo, you collected and processed operational metrics like CPU and memory usage data through your MQTT-enabled, V3 gateway.

To enhance your IoT solution, consider exploring advanced features like anomaly detection by leveraging [Detect anomalies with Lookout for Equipment](anomaly-detection.md "anomaly-detection.md"), or integrating with other AWS services like [Amazon Quick Suite](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md") in the _Amazon Quick Suite User Guide_ for advanced analytics.

## Step 11: Clean up resources after the tutorial

After you complete this tutorial about integrating data into AWS IoT SiteWise Edge, clean up your resources to avoid incurring additional charges.

###### To delete hierarchical assets in AWS IoT SiteWise

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation pane, choose **Assets**.
3. When you delete assets in AWS IoT SiteWise, you must first disassociate them.

Complete the following steps to disassociate your device assets from your device fleet
asset:

    1. Choose your device fleet asset (**SiteWise Tutorial Device Fleet 1**).
    2. Choose **Edit**.
    3. Under **Assets associated to this asset**, choose
     **Disassociate** for each device asset associated to this device
     fleet asset.
    4. Choose **Save**.


    ###### Note

     The device assets are no longer organized as a hierarchy now.

4. Choose your device asset (**SiteWise Tutorial Device 1**).
5. Choose **Delete**.
6. In the confirmation dialog, enter `Delete`, and then choose
   **Delete**.
7. Repeat steps 4 through 6 for each device asset and the device fleet asset
   (**SiteWise Tutorial Device Fleet 1**).

###### To delete hierarchical asset models in AWS IoT SiteWise

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. Delete your device and device fleet assets.
3. In the left navigation pane, choose **Models**.
4. Choose your device fleet asset model (**SiteWise Tutorial Device Fleet Model**). You can't delete a model if you have assets that were created from that model.

When deleting hierarchical asset models, start by deleting the parent asset model
first. 5. Choose **Delete**. 6. In the confirmation dialog, enter `Delete`, and then choose
**Delete**. 7. Repeat steps 4 through 6 for your device asset model
(**SiteWise Tutorial Device Model**).

###### To disable or delete a rule in AWS IoT Core

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. In the left navigation pane, choose **Message routing**, and then choose
   **Rules**.
3. Select your rule and choose **Delete**.
4. In the confirmation dialog, enter the name of the rule and then choose
   **Delete**.

###### To delete an Amazon S3 bucket

1. Navigate to the [Amazon S3 console](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose bucket**.
3. In the buckets list, select the option button next to the bucket you created, and then choose **Empty** at the top of the page.
4. In the confirmation dialog, confirm the deletion, and then choose **Empty**.
5. After the bucket is empty, choose **Delete** to delete the bucket.
6. In the confirmation dialog, enter the name of your bucket to confirm deletion.
7. Choose **Delete bucket**.

###### To delete a SiteWise Edge gateway

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation pane, choose **Edge gateways**.
3. Under Gateways, choose the gateway you created for this tutorial. For example, `SiteWise Tutorial Device Gateway`.
4. Choose **Delete**.
5. To confirm you want to delete the gateway, type `Delete` in the confirmation dialog, and then choose **Delete** in the window that appears.

###### To delete your IoT thing

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. In the left navigation pane, choose **Manage**, then choose **Things**.
3. Select the IoT thing you created for this tutorial. For example, `SiteWiseTutorialDevice1`.
4. Choose **Delete**.
5. In the confirmation dialog, enter the name of the thing, and then choose **Delete**.

**To uninstall AWS IoT Greengrass Core**

Uninstall the AWS IoT Greengrass Core software from your local device. For detailed instructions, see [Uninstall the AWS IoT Greengrass Core software](../../../greengrass/v2/developerguide/uninstall-greengrass-core-v2.md "../../../greengrass/v2/developerguide/uninstall-greengrass-core-v2.md") in the _AWS IoT Greengrass Developer Guide, Version 2_.

###### Important

Uninstalling Greengrass removes all local configurations and data. Ensure you've backed up any important information before proceeding.

**(Optional) To delete third-party resources**

After completing this tutorial, consider shutting down any external resources you created. This helps to prevent incurring charges from third-party providers.

## Additional resources

Refer to the following resources for more information:

- [Interact with other AWS services](interact-with-other-services.md "interact-with-other-services.md")
- [Use AWS IoT SiteWise Edge gateways](gateways.md "gateways.md")
- [Troubleshooting a SiteWise Edge gateway](troubleshooting-gateway.md "troubleshooting-gateway.md")
- [Security best practices for AWS IoT SiteWise](security-best-practices.md "security-best-practices.md")
- [AWS IoT pricing](https://aws.amazon.com/iot-sitewise/pricing/ "https://aws.amazon.com/iot-sitewise/pricing/")
- [Ingest data to AWS IoT SiteWise](industrial-data-ingestion.md "industrial-data-ingestion.md")
- [Use tags in AWS IoT SiteWise](tag-basics.md "tag-basics.md")
