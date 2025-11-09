# Failure management

| IOTREL10: How do you implement your IoT<br>workload to withstand component and system faults? |
| --------------------------------------------------------------------------------------------- |
|                                                                                               |

Understanding and predicting the fault scenarios in the system
helps you to architect for failure conditions and use service
features to handle them. Therefore, the handling of such predicted
system faults and recovering from them should be architected into
the system.

## IOTREL10-BP01 Use cloud service capabilities to handle component failures

An IoT design consists of device software, connectivity and
control services, and analytics services. Test the entire IoT
landscape for resiliency, starting with device firmware, data
flow, the cloud services used, and error handling. Vendors have
services integrated with each other to provide a simplified
integration and fault handling.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTREL10-BP01-01** _Understand and apply the
standard libraries available to manage your device firmware or
software._

- Devices can be built on
  [FreeRTOS](https://aws.amazon.com/freertos/ "https://aws.amazon.com/freertos/")
  which provides connectivity, messaging, power management and
  device management libraries that are tested for reliability
  and designed for ease of use.
- AWS provides IoT device SDKs and Mobile SDKs, comprised of
  open-source libraries, developer guides, sample apps, and
  porting guides to help you build IoT solutions with AWS IoT
  and your choice of hardware systems.

**Prescriptive guidance
IOTREL10-BP01-02** _Use log levels appropriate
to the lifecycle stage of your workload._

- AWS IoT logs can be set up per region and per account with
  the logging level set to DEBUG during product development
  phase to provide insights on data flow and resources used.
  This data can be used to improve the IoT system security and
  performance.
- [AWS IoT Secure Tunneling](https://aws.amazon.com/blogs/iot/securing-amazon-freertos-devices-at-scale-with-infineon-optiga-trust-x/ "https://aws.amazon.com/blogs/iot/securing-amazon-freertos-devices-at-scale-with-infineon-optiga-trust-x/") can be used to test and debug
  devices that are behind a restrictive firewall in the field.

| IOTREL11: How do you verify that your<br>IoT device operates with intermittent connectivity to the<br>cloud? |
| ------------------------------------------------------------------------------------------------------------ |
|                                                                                                              |

IoT solution reliability must also encompass the device itself.
Devices may be deployed in remote locations and deal with
intermittent connectivity, or loss in connectivity, due to a
variety of external factors that are out of your IoT
application's control.

For example, if an ISP is interrupted for several hours, how
will the device behave and respond to these long periods of
potential network outage? Implement a minimum set of embedded
operations on the device to make it more resilient to the
nuances of managing connectivity and communication to AWS IoT Core.

## IOTREL11-BP01 Implement device logic to automatically reconnect to the cloud

Your IoT device will likely become disconnected due to
networking issues, power loss, or other unforeseen situations.
This might be true of a single device, or for your entire fleet
of devices. Whether a single device or the entire fleet becomes
disconnected, the following best practices will make sure that
the entire fleet is able to automatically reconnect.

**Level of risk exposed if this best
practice is not established:** Medium

Prescriptive guidance IOTREL11-BP01-01 _Use an
exponential backoff with jitter and retry logic to connect
remote devices to the cloud._

Consider implementing a retry mechanism for IoT device software.
The retry mechanism should have exponential backoff with a
randomization factor built in to avoid retries from multiple
devices occurring simultaneously. Implementing retry logic with
exponential backoff with jitter allows the IoT devices to more
evenly distribute their traffic and help prevent them from
creating unnecessary peak traffic.

**Prescriptive guidance
IOTREL11-BP01-02** _Use device edge software
and the SDK to use built in exponential backoff
logic._

- Exponential backoff logic is included in the AWS SDK,
  including the AWS IoT Device SDK, and edge software, such as
  AWS IoT Greengrass Core and FreeRTOS.
- [AWS SDK handles the exponential backoff](../../../general/latest/gr/api-retries.md "../../../general/latest/gr/api-retries.md")
- [AWS IoT Device SDK C: MQTT](../../../freertos/latest/lib-ref/c-sdk/mqtt/mqtt_config.md "../../../freertos/latest/lib-ref/c-sdk/mqtt/mqtt_config.md") uses IOT-MQTT-RETRY-MS-CEILING
  for setting maximum retry interval limit.

## IOTREL11-BP02 Design devices to use multiple methods of communication

Devices hardware can be designed to make use of multiple
networking interfaces. Consider a device that provides multiple
network interface types when selecting device hardware according
to the needs of your IoT application.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL11-BP02-01** _Establish alternate
network channels to meet requirements._

- Have a separate failover network channel to deliver critical
  messages to AWS IoT. Failover channels can include Wi-Fi,
  cellular networks, or a wireless personal network.
- For low latency workload, use
  [AWS Wavelength](https://aws.amazon.com/wavelength/ "https://aws.amazon.com/wavelength/") for 5G devices and
  [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/") to keep your cloud services closer to the
  user.

## IOTREL11-BP03 Automate alerting for devices that are unable to reconnect

In the event that devices are unable to reconnect, fleet
operators are to be automatically notified to begin
troubleshooting the device and to re-establish device
connectivity.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL11-BP03-01** _Implement logic in the
cloud to notify the device operator if a device has not
connected for an extended period of time._

- [Lifecycle
  events](../../../iot/latest/developerguide/life-cycle-events.md "../../../iot/latest/developerguide/life-cycle-events.md") can be enabled to monitor device lifecycle
  events, including connect and disconnect events.
- AWS IoT Fleet Indexing can be used to identify device
  connectivity status
- AWS IoT Events can be used to monitor devices remotely.
- Remote monitoring using AWS IoT Events:
  [CloudWatch
  Metrics connector](../../../greengrass/v1/developerguide/cloudwatch-metrics-connector.md "../../../greengrass/v1/developerguide/cloudwatch-metrics-connector.md")

| IOTREL12: How do you verify that<br>required data is transmitted to the cloud after a device has<br>been disconnected? |
| ---------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                        |

Your IoT device must be able to operate without internet
connectivity. To make sure that required data is not lost when
devices become disconnected from the cloud, they should store
important messages durably offline and, once reconnected, send
those messages to AWS IoT Core. Connection to the cloud can be
intermittent and devices should be designed to handle this.
Choose devices with firmware designed for intermittent cloud
connection and that have the ability to store data on the device
if you cannot afford to lose the data.

## IOTREL12-BP01 Provide adequate device storage for offline operations

Store important messages durably offline and, once reconnected,
send those messages to the cloud. Device hardware should have
capabilities to store data locally for a finite period to help
prevent loss of information.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL12-BP01-01** _Use the device edge
software capabilities for storing data locally._

- Design your edge applications according to your device
  constraints to store and forward critical data when devices
  become disconnected from the cloud.
  - If your device has sufficient storage available, your
    application may implement a local cache of messages
    written to disk to make sure that data is not lost when
    the device is operating in a disconnected state.
  - To make sure that the disk is not accidentally filled
    with this persisted data, design your application to
    make use of only a set amount of total disk space, and
    consider implementing a FIFO overwrite strategy.
  - When the device comes back online, a background process
    should be implemented to transmit data that was stored
    locally to the cloud, emptying the local cache as
    messages are successfully published to the cloud.

- If using AWS IoT Greengrass for device software, AWS IoT Greengrass components can help collect, process, and export
  data streams, including when devices are offline.
  - Messages collected on the device are queued and
    processed in FIFO order.
  - By default, AWS IoT Greengrass Core stores unprocessed
    messages destined for AWS Cloud targets in memory.
  - Configure AWS IoT Greengrass to cache messages to the
    local file system so that they persist across core
    restarts.
  - AWS IoT Greengrass stream manager makes it easier and
    more reliable to transfer high-volume IoT data to the
    AWS Cloud.
  - [Configure
    AWS IoT Greengrass core](../../../greengrass/v1/developerguide/gg-core.md "../../../greengrass/v1/developerguide/gg-core.md")
  - [Manage
    data streams on AWS IoT Greengrass Core](../../../greengrass/v1/developerguide/stream-manager.md "../../../greengrass/v1/developerguide/stream-manager.md")
  - [AWS IoT Greengrass Developer Guide](../../../greengrass/v1/developerguide/what-is-gg.md "../../../greengrass/v1/developerguide/what-is-gg.md")
  - [Run
    Lambda functions on the AWS IoT Greengrass core](../../../greengrass/v1/developerguide/lambda-functions.md "../../../greengrass/v1/developerguide/lambda-functions.md")
  - The ETL with AWS IoT Greengrass solution accelerator
    (For more information, see
    [Unlock
    the value of embedded security IP to build secure IoT
    products at scale](https://aws.amazon.com/blogs/iot/unlock-the-value-of-embedded-security-ip-to-build-secure-iot-products-at-scale/ "https://aws.amazon.com/blogs/iot/unlock-the-value-of-embedded-security-ip-to-build-secure-iot-products-at-scale/"))helps to quickly set up an edge
    device with AWS IoT Greengrass to perform extract,
    transform, and load (ETL) functions on data gathered
    from local devices before being sent to AWS.

**Prescriptive guidance
IOTREL12-BP01-02** _Consider using AWS IoT SiteWise for data coming from disparate industrial
equipment._

AWS IoT SiteWise Edge software collects local equipment data and
sends it to AWS IoT SiteWise in the cloud. You can use SiteWise
Edge gateways to collect data from multiple OPC Unified
Architecture (UA) servers and publish it to AWS IoT SiteWise.
The SiteWise Edge gateway runs on either AWS IoT Greengrass V2
or Siemens Industrial Edge can be used to cache data locally in
the event of intermittent network connectivity. You can
configure the maximum disk buffer size used for caching data. If
the cache size exceeds the maximum disk buffer size, the
connector discards the earliest data from the queue. For more
information, see
[Use
AWS IoT SiteWise Edge gateways](../../../iot-sitewise/latest/userguide/gateways-ggv2.md "../../../iot-sitewise/latest/userguide/gateways-ggv2.md").

## IOTREL12-BP02 Synchronize device states upon connection to the cloud

IoT devices are not always connected to the cloud. Design a
mechanism to synchronize device states every time the device has
access to the cloud. Synchronizing the device state to the cloud
allows the application to get and update device state easily, as
the application doesn't have to wait for the device to come
online.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL12-BP02-01** _Use a digital devices
state representation to synchronize device state using the below
capabilities._

- AWS provides device shadow capabilities that can be used to
  synchronize device state when the device connects to the
  cloud. The AWS IoT Device Shadow service maintains a shadow
  for each device that you connect to AWS IoT and is supported
  by the AWS IoT Device SDK, AWS IoT Greengrass core, and
  FreeRTOS.
- [Synchronizing
  device shadows](../../../iot/latest/developerguide/using-device-shadows.md "../../../iot/latest/developerguide/using-device-shadows.md") - Device SDKs and the AWS IoT Core
  take care of synchronizing property values between the
  connected device and its device shadow in AWS IoT Core.
- [AWS IoT Greengrass](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md") – AWS IoT Greengrass core software
  provides local shadow synchronization of devices and these
  shadows can be configured to sync with cloud.
- [FreeRTOS](../../../greengrass/latest/developerguide/security.md "../../../greengrass/latest/developerguide/security.md") -
  The FreeRTOS device shadow API operations define functions
  to create, update, and delete AWS IoT Device Shadow services.

**Prescriptive guidance
IOTREL12-BP02-02** _Use MQTT Persistent
Sessions._

MQTT's persistent session feature allows a client to retain its
subscriptions, undelivered messages, and other session data
across different connections. If a device (client) disconnects
and later reconnects, it can pick up where it left off without
having to re-subscribe or miss critical messages.

| IOTREL13: How do you remotely adjust<br>message frequency to your IoT devices? |
| ------------------------------------------------------------------------------ |
|                                                                                |

Because IoT is an event-driven workload, your application code
must be resilient to handling known and unknown errors that can
occur as events are permeated through your application. A
well-architected IoT application has the ability to log and
retry errors in data processing. An IoT application will archive
data in its raw format. By archiving data, valid and invalid, an
architecture can more accurately restore data to a given point
in time.

## IOTREL13-BP01 Configure cloud services to reliably handle message processing

When devices send an unexpected influx of messages, or when your
device fleet grows, it becomes necessary to add error handling
to support the reliable delivery of messages in your IoT
applications.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL13-BP01-01** _Configure error actions
with IoT Rules Engine._

With the IoT rules engine, an application can enable an IoT
error action. If a problem occurs when invoking an action, the
rules engine will invoke the error action. This allows you to
capture, monitor, alert, and eventually retry messages that
could not be delivered to their primary IoT action. We recommend
that an IoT error action is configured with a different AWS
service from the primary action. Use durable storage for error
actions such as Amazon SQS or Amazon Kinesis.

Beginning with the rules engine, your application logic should
initially process messages from a queue and validate that the
schema of that message is correct. Your application logic should
catch and log any known errors and optionally move those
messages to their own dead-letter queue (DLQ) for further
analysis. Have a catch-all IoT rule that uses Amazon Data Firehose to transfer raw and unformatted messages into
long-term storage in Amazon S3, or Amazon Redshift for data
warehousing.

## IOTREL13-BP02 Send logs directly to the cloud

It is common for device developers to log application errors at
the edge, but that increases the complexity for reliably
troubleshooting device issues, especially as device fleets
increase in size. Storing log files on the device itself then
requires a specialized process to request a device to transmit
logs, which it may not be able to accomplish during failure
states, or to open remote access to the device to access those
logs. Instead, transmit logs as events to the cloud and automate
alerts based on those log events to improve reliability of your
IoT applications.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL13-BP02-01** _Use MQTT to send log
messages to the cloud._

Regardless of the underlying cause for device failures, if the
device can communicate to your cloud application, it should send
diagnostic information about the hardware failure to AWS IoT Core using a diagnostics topic. If the device loses connectivity
because of the hardware failure, use Fleet Indexing with
connectivity status to track the change in connectivity status.
If the device is offline for extended periods of time, trigger
an alert that the device may require remediation.

## IOTREL13-BP03 Design devices to allow for remote configuration of message publication frequency

Devices may be developed with initial assumptions around how
frequently messages need to be delivered, such as at a rate of
1Hz (1 message per second). When the device is deployed into its
destination environment, whether that is in a smart home
setting, or a remote industrial asset, the network variability
and other challenges may then require the need to alter this
publication frequency. Planning ahead to allow for this type of
configuration to be remotely managed will help with the
reliability aspect of your IoT architecture.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL13-BP03-01** _Use either AWS IoT Jobs or
AWS IoT device shadows to allow for the remote configuration of
message publication frequency._

AWS IoT Jobs can be used to push remote configuration changes to
devices. AWS IoT device shadows can also be used to maintain
device configuration. AWS IoT device SDKs provide support for
integration with both of these features.

| IOTREL14: How do you plan for disaster<br>recovery in your IoT workloads? |
| ------------------------------------------------------------------------- |
|                                                                           |

When companies run their core production operations and
cybersecurity functions in the cloud, it is important to design
resilience at the edge & cloud in IoT systems. IoT
implementations must allow for loss of internet connectivity,
local data storage and processing.

## IOTREL14-BP01 Design server software to initiate communication only with devices that are online

Communication should be server initiated with devices that are
online rather than client-server requests. It enables you to
design client software to accept commands from the server.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance IOTREL14-
BP01-01** _Design client software to accept
commands from the server._

- FreeRTOS provides pub/sub and shadow library to connected
  devices.
- AWS IoT Core provides device shadow capability to persist
  device states.
- AWS IoT Device Registry contains a list of devices connected
  to AWS IoT Core. AWS IoT Device Registry lets you manage
  devices by grouping them.

## IOTREL14-BP02 Implement multi-Region support for IoT applications and devices

Cloud service providers have the same service in multiple
Regions. You can use this architecture to divert device data to
a Regional endpoint that is in not down. Data consumers should
be enabled in all Regions that consume the diverted device data.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL14-BP02-01** _Architect device software
to reach multiple Regions in case one is not
available._

- AWS IoT is available in multiple Regions with different
  endpoints. If an endpoint is not available, divert device
  traffic to a different endpoint.
- AWS IoT configurable endpoints can be used with Amazon Route 53 to divert IoT traffic to a new Regional endpoint.
- AWS IoT Configurable Endpoints:
  [Domain
  configurations](../../../iot/latest/developerguide/iot-custom-endpoints-configurable.md "../../../iot/latest/developerguide/iot-custom-endpoints-configurable.md")

**Prescriptive guidance
IOTREL14-BP02-02** _Enable device
authentication certificates in multiple Regions._

- AWS IoT provides devices with authentication certificates to
  verify on connection. Deploy the device certificates in the
  Regions where the device will connect.
- Setup the cloud side IoT data consumers to accept and
  process data in multiple Regions.
- AWS IoT device registration:
  [Simplify
  IoT device registration and easily move devices between AWS accounts with AWS IoT Core Multi-Account
  Registration](https://aws.amazon.com/blogs/iot/simplify-multi-account-device-provisioning-and-certificate-authority-registration-using-aws-iot-core/ "https://aws.amazon.com/blogs/iot/simplify-multi-account-device-provisioning-and-certificate-authority-registration-using-aws-iot-core/").

**Prescriptive guidance
IOTREL14-BP02-03** _Use device services in all
Regions the device connects to._

- AWS IoT Rules Engine diverts device data to use multiple
  services. Set up AWS IoT Rules Engine in the respective
  Regions to divert traffic to the appropriate services.
- [Rules
  for AWS IoT](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md")

## IOTREL14-BP03 Use edge devices to store and analyze data

Edge storage can provide additional storage for device data.
Data can be stored at the edge during large-scale network events
and streamed later, when network is available.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL14-BP03-01** _Use an edge device as a
connection point to store and analyze data._

- AWS IoT Greengrass can be used for local processing for
  serverless functions, containers, messaging, storage, and
  machine learning inference.
- Data can be stored in AWS IoT Greengrass and sent to the
  network when it's available.
- [AWS IoT Greengrass features](https://aws.amazon.com/greengrass/features/ "https://aws.amazon.com/greengrass/features/") and components such a Stream
  Manager can be used to help design resilient solutions at
  the edge.
