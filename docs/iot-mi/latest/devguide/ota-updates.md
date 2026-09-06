

# Over-the-Air updates
<a name="ota-updates"></a>

## OTA architecture overview
<a name="ota-updates-architecture-overview"></a>

The Over-the-Air (OTA) update process involves several components working together to deliver firmware updates to your devices. The following diagram illustrates how an OTA update request is handled through the interaction between End device SDK, Hub SDK and the feature.

![Current architecture to ingest AWS IoT data with AWS IoT Analytics](http://docs.aws.amazon.com/iot-mi/latest/devguide/images/iot-managedintegrations-sdk-ota-arch.png)


The OTA update architecture consists of the following components:
+ **Customer**: Uploads job documents to a S3 bucket and initiates updates via API
+ **OTA Service**: Handles job creation, validation, and management
+ **AWS IoT Jobs**: Manages job execution and delivery to devices
+ **Devices**: Receive and apply updates using Harmony SDK