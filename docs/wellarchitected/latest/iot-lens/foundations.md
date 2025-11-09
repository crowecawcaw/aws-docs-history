# Foundations

IoT devices should continue to operate in some capacity in the
face of network or cloud errors. Design device firmware to handle
intermittent connectivity or loss in connectivity in a way that is
sensitive to memory and power constraints. IoT cloud applications
must also be designed to handle remote devices that frequently
transition between being online and offline to maintain data
coherency and scale horizontally over time. Monitor overall IoT
utilization and create a mechanism to automatically increase
capacity to make sure that your application can manage peak IoT
traffic.

To help prevent devices from creating unnecessary peak traffic,
device firmware must be implemented that helps prevent the entire
fleet of devices from attempting the same operations at the same
time.

For example, if an IoT application is composed of alarm systems
and all the alarm systems send an activation event at 9am local
time, the IoT application is inundated with an immediate spike
from your entire fleet. Instead, you should incorporate a
randomization factor into those scheduled activities, such as
timed events and exponential backoff, to permit the IoT devices to
more evenly distribute their peak traffic within a window of time.

| IOTREL01: How do you make sure<br>that your device consistently keeps its<br>internal clock accurate? |
| ----------------------------------------------------------------------------------------------------- |
|                                                                                                       |

A secure device should have a valid certificate. IoT devices use a
server certificate to communicate to the cloud and the certificate
presented uses time for certificate validity. Having reliable and
accurate time is compulsory to be able to validate certificates.
Because IoT data is not ordered, including an accurate timestamp
with the data will enhance your analytic capabilities.

## IOTREL01-BP01 Use NTP to maintain time synchronization on devices

IoT devices need to have a client to keep track of time—either
using Real Time Clock (RTC) or Network Time Protocol (NTP) to
set the RTC on boot. Failure to provide accurate time to an IoT
device could help prevent it from being able to connect to the
cloud.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL01-BP01-01** _Prefer NTP to RTC when NTP
synchronization is available._

Many computers have an RTC peripheral that helps in keeping
time. Consider that RTC is prone to clock drift of about 1
second a day, which can result in the device going offline
because of certificate invalidity.

**Prescriptive guidance
IOTREL01-BP01-02** _Use Network Time Protocol
for connected applications._

- Select a safe, reliable NTP pool to use, and a one that
  addresses your security design
- Many operating systems include an NTP client to sync with an
  NTP server
- If the IoT device is using GNU/Linux, it is likely to
  include the NTPD daemon
- You can import an NTP client to your system if using
  FreeRTOS
- The device's software needs to include an NTP client and
  should wait until it has synchronized with an NTP server
  before attempting a connection with AWS IoT Core
- The system should provide a way for a user to set the
  device's time so that subsequent connections can succeed
- Use NTP to synchronize RTC on the device to help prevent the
  device from deviating from UTC
- Consider the following
  [The
  NTP Pool for vendors](https://www.pool.ntp.org/en/vendors.html "https://www.pool.ntp.org/en/vendors.html")
- [Chrony](https://chrony.tuxfamily.org/ "https://chrony.tuxfamily.org/")
  is a different implementation of NTP than what NTPD uses and
  it is able to synchronize the system clock faster and with
  better accuracy than NTPD. Chrony can be set up as a client
  and server.

## IOTREL01-BP02 Provide devices access to NTP servers

An NTP server should be available for clients to use for local
time. NTP servers are required by NTP clients to synchronize
device time and function properly.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL01-BP02-01** _Provide access to NTP
services._

- ntp.org can be used to synchronize your computer clocks.

- [Amazon
  Time Sync Service](https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-the-amazon-time-sync-service/ "https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-the-amazon-time-sync-service/"): a time synchronization service
  delivered over NTP, which uses a fleet of redundant
  satellite-connected and atomic clocks in each Region to
  deliver a highly accurate reference clock. This is natively
  accessible from Amazon EC2 instances and this can be pushed
  to edge devices.
- [Chrony](https://chrony.tuxfamily.org/ "https://chrony.tuxfamily.org/")
  is a different implementation of NTP than what NTPD uses and
  it is able to synchronize the system clock faster and with
  better accuracy than NTPD. Chrony can be set up as a server
  and client.

| IOTREL02: How do you manage service<br>quotas and limits for peaks in your IoT workload? |
| ---------------------------------------------------------------------------------------- |
|                                                                                          |

AWS IoT provides a set of soft and hard limits for different
dimensions of usage. AWS IoT outlines the data plane limits on
the IoT limits, see
[AWS service quotas](../../../general/latest/gr/aws_service_limits.md#limits_iot "../../../general/latest/gr/aws_service_limits.md#limits_iot"). Data plane operations (for example, MQTT
Connect, MQTT Publish, and MQTT Subscribe) are the primary
driver of your device connectivity. Therefore, it's important to
review the IoT limits and make sure that your application
adheres to any soft limits related to the data plane, while not
exceeding any hard limits that are imposed by the data plane.

## IOTREL02-BP01 Manage service quotas and

constraints

For cloud-based workload architectures, there are service quotas (which are also referred to as service limits). These quotas exist to help prevent accidentally provisioning more resources than you need and to limit request rates on API operations so as to protect services from abuse.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTREL02-BP01-01** _Follow the Reliability
Foundations Best Practices defined in the AWS Well-Architected
Framework._

The most important part of your IoT scaling approach is to make sure that you architect around any hard limits because exceeding limits that are not adjustable results in application errors, such as throttling and client errors. Hard limits are related to throughput on a single IoT connection. Consider restructuring your MQTT topics, or implementing cloud-side logic to aggregate or filter messages before delivering the messages to the interested devices.

Soft limits in AWS IoT traditionally correlate to account-level limits that are independent of a single device. For any account-level limits, you should calculate your IoT usage for a single device and then multiply that usage by the number of devices to determine the base IoT limits that your application will require for your initial product launch. AWS recommends that you have a ramp-up period where your limit increases align closely to your current production peak usage with an additional buffer. To make sure that the IoT application is not under provisioned:

- Consult published AWS IoT CloudWatch metrics for all limits:
  [AWS IoT metrics and dimensions](../../../iot/latest/developerguide/metrics_dimensions.md "../../../iot/latest/developerguide/metrics_dimensions.md")
- Monitor CloudWatch metrics in AWS IoT Core:
  [Logging
  and Monitoring](../../../iot/latest/developerguide/security-logging.md "../../../iot/latest/developerguide/security-logging.md")
- Alert on CloudWatch throttle metrics, which would signal if
  you need a limit increase.
- Set alarms for all thresholds in IoT, including MQTT
  connect, publish, subscribe, receive, and rule engine
  actions.
- Monitoring AWS IoT MQTT Traffic and Automating Quota and
  Throttling Notifications
- [Monitoring
  your IoT Fleet using CloudWatch](https://aws.amazon.com/blogs/iot/monitoring-your-iot-fleet-using-cloudwatch/ "https://aws.amazon.com/blogs/iot/monitoring-your-iot-fleet-using-cloudwatch/")
- Make sure that you request a limit increase in a timely
  fashion, before reaching 100% capacity. See the AWS
  documentation on Requesting a quota increase:
  [Requesting
  a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md")

In addition to data plane limits, the AWS IoT service has a
control plane for administrative APIs. The control plane manages
the process of creating and storing IoT policies and principals,
creating the thing in the registry, and associating IoT
principals including certificates and Amazon Cognito federated
identities. Because bootstrapping and device registration is
critical to the overall process, it's important to plan control
plane operations and limits. Control plane API calls are based
on throughput measured in requests per second. Control plane
calls are normally in the order of magnitude of tens of requests
per second. It is important for you to work backward from peak
expected registration usage to determine if any limit increases
for control plane operations are needed. Plan for sustained
ramp-up periods for onboarding devices so that the IoT limit
increases align with regular day-to-day data plane usage.

To protect against a burst in control plane requests, your
architecture should limit the access to these APIs to only
authorized users or internal applications. Implement back-off
and retry logic, and queue inbound requests to control data
rates to these APIs.

| IOTREL03: How do you design workloads to<br>operate efficiently within network bandwidth and storage<br>constraints? |
| -------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                      |

## IOTREL03-BP01 Down sample data to reduce storage requirements and network utilization

Data should be down sampled where possible to reduce storage in
the device and lower transmission costs and reduce network
pressure.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL03-BP01-01** _Use device edge software
capabilities for down sampling._

- Use compression as a means of down sampling data
  - Data transmitted to the cloud can be in JSON format, or
    in other formats such as Protocol Buffers.

- Using AWS IoT Greengrass for device software to down sample
  data.
  - Applications built using Components can be used on AWS IoT Greengrass to down sample the data before sending it
    to the cloud.
  - [ETL
    with AWS IoT Extract, Transform, Load with AWS IoT Greengrass Solution Accelerator](https://aws.amazon.com/iot/solutions/etl-accelerator/ "https://aws.amazon.com/iot/solutions/etl-accelerator/") helps to quickly
    set up an edge device with AWS IoT Greengrass to perform
    extract, transform, and load (ETL) functions on data
    gathered from local devices before being sent to AWS.

| IOTREL04: How do you optimize and<br>control message delivery frequency to IoT devices? |
| --------------------------------------------------------------------------------------- |
|                                                                                         |

Devices can be restricted in message processing capacity and
messages from the cloud might need to be throttled. The
cloud-side message delivery rate might need to be architected
based on the type of devices that are connected.

## IOTREL04-BP01 Target messages to relevant devices

Devices receive information from shadow updates, or from
messages published to topics they subscribe to. Some data are
relevant only to specific devices. In those cases, design your
workload to send messages to relevant devices only, and to
remove any data that is not relevant to those devices.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL04-BP01-01** _Preprocess data to support
the specific needs of the device._

- Use AWS Lambda to pre-process the data and hone-in
  specifically to attributes and variables that are needed by
  the device to act upon

## IOTREL04-BP02 Implement retry and back off logic to support throttling by device type

Retry and back off logic should be implemented in a controlled
manner so that when you need to alter throttling settings per
device type, you can easily do it. Using data storage of any
chosen kind gives you flexibility on what data to publish down
to the device.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL04-BP02-01** _Use storage mechanisms
that enable retry mechanisms._

- Using DynamoDB, you can hold data in key value format where
  device ID is the key. Retry logic can be applied to only
  certain device ID's.
- Using Amazon Relational Database Service, you
  have the flexibility to use a variety of database engines.
  The retry messages can have new real-time data augmented
  with historic data from previous device interactions stored
  in Amazon RDS.
- AWS IoT Events provides state machines with built-in timers
  to hold back data and retry based on timers.
