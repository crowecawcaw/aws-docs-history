# Managing demand and supplying resources

Optimally matching supply to demand delivers the lowest cost for a
system. However, given the susceptibility of IoT workloads to data
bursts, solutions must be dynamically scalable and consider peak
capacity when provisioning resources. With the event driven flow
of data, you can choose to automatically provision your AWS
resources to match your peak capacity, and then scale up and down
during known low periods of traffic.

| IOTCOST04: How do you optimize cost by<br>matching the supply of resources with device demand? |
| ---------------------------------------------------------------------------------------------- |
|                                                                                                |

Serverless technologies, such as AWS Lambda and Amazon API Gateway, help you create a more scalable and resilient
architecture, and you only pay when your application uses those
services. AWS IoT Core, AWS IoT Device Management, AWS IoT Device Defender, and AWS IoT Greengrass are also managed services that
charge based on usage, not for idle compute capacity. The benefit
of managed services is that AWS manages the automatic provisioning
of your resources. If you use managed services, you are
responsible for monitoring and setting alerts for limit increases
for AWS services.

## IOTCOST04-BP01 Plan expected usage over time

When architecting to match supply against demand, proactively
plan your expected usage over time, and the limits that you are
most likely to exceed. Factor those limit increases into your
future planning.

**Level of risk exposed if this best
practice is not established:** Low

Prescriptive guidance

Evaluating new AWS features helps you optimize cost by analyzing
how your devices are performing. You can use this analysis to
make changes to how your devices communicate with your IoT.

To optimize the cost of your solution through changes to device
firmware, review the pricing components of AWS services, such as
AWS IoT, determine where you are below billing metering
thresholds for a given service, and then weigh the trade-offs
between cost and performance.

| IOTCOST05: How do you optimize payload<br>size between devices and your IoT system to save<br>cost? |
| --------------------------------------------------------------------------------------------------- |
|                                                                                                     |

IoT applications must balance the networking throughput that can
be realized by end devices with the most efficient way that data
should be processed by your IoT application. We recommend that
IoT deployments initially optimize data transfer based on the
device constraints. Begin by sending discrete data events from
the device to the cloud, making minimal use of batching multiple
events in a single message. Later, if necessary, you can use
serialization frameworks to compress the messages prior to
sending it to your IoT system.

From a cost perspective, the MQTT payload size is a critical
cost optimization element for AWS IoT Core. An IoT message is
billed in five KB increments, up to 128 KB. For this reason,
each MQTT payload size should be as close to possible to any
five KB. For example, a payload that is currently sized at 6 KB
is not as cost efficient as a payload that is ten KB because the
overall costs of publishing that message is identical despite
one message being larger than the other.

## IOTCOST05-BP01 Balance networking throughput against payload size to optimize efficiency

The specific use case drives the balance between frequency and
payload size. Consider and test different payload optimization
strategies. Additionally, consider trade-offs between
compression and processing overhead.

**Level of risk exposed if this best
practice is not established: Low**

**Prescriptive guidance**

- Shorten values while keeping them legible. If five digits of
  precision are sufficient, then you should not use 12 digits
  in the payload.
- Use serialization frameworks to compress payloads to smaller
  sizes if you do not require IoT rules engine payload
  inspection.
- Send data less frequently and aggregate messages together
  within the billable increments. For example, sending a
  single two KB message every second can be achieved at a
  lower IoT message cost by sending two separate two KB
  messages every other second.

This approach has tradeoffs that should be considered before
implementation. Adding complexity or delay in your devices may
unexpectedly increase processing costs. A cost optimization
exercise for IoT payloads should only happen after your solution
has been in production and you can use a data-driven approach to
determine the cost impact of changing the way data is sent to
AWS IoT Core.

| IOTCOST06: How do you optimize the costs<br>of storing the current state of your IoT device? |
| -------------------------------------------------------------------------------------------- |
|                                                                                              |

Well-Architected IoT applications have a virtual representation
of the device in the cloud. This virtual representation is
composed of a managed data store or specialized IoT application
data store. In both cases, your end devices must be programmed
in a way that efficiently transmits device state changes to your
IoT application. For example, your device should only send its
full device state if your firmware logic dictates that the full
device state may be out of sync and would be best reconciled by
sending all current settings. As individual state changes occur,
the device should optimize the frequency it transmits those
changes to the cloud.

In AWS IoT, device shadow and registry operations are metered in
one KB increments and billing is per million access and modify
operations. The shadow stores the desired or actual state of
each device and the registry is used to name and manage devices.

## IOTCOST06-BP01 Optimize shadow operations

Cost optimization processes for device shadows and registry
focus on managing how many operations are performed and the size
of each operation. If your operation is cost-sensitive to shadow
and registry operations, explore ways to optimize shadow
operations. For example, for the shadow you could aggregate
several reported fields together into one shadow message update
instead of sending each reported change independently. Grouping
shadow updates together reduces the overall cost of the shadow
by consolidating updates to the service.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance**

- **Use named shadows:**
  Separate logical elements, and reduce the size of updates.
- **Aggregate shadow updates:**
  Look for opportunities to put several reported fields
  together into one shadow message update instead of sending
  each reported change independently. Grouping shadow updates
  together reduces the overall cost of the shadow by
  consolidating updates to the service.
- **Send only what is needed, when it is
  needed:** For example, your device should only send
  its full device state if your firmware logic dictates that
  the full device state may be out of sync and would be best
  reconciled by sending all current settings. As individual
  state changes occur, the device should optimize the
  frequency it transmits those changes to the cloud.
- **Immutable data:** Use the
  [AWS IoT device registry](../../../iot/latest/developerguide/iot-thing-management.md "../../../iot/latest/developerguide/iot-thing-management.md") device attributes for immutable
  data such as a serial number.
- **Minimize the frequency of reads and
  writes:** Where possible, limit updates to device's
  shadow document to reduce the total metered operations.
- **Choose the right service:**
  Avoid using shadows as a guaranteed-delivery mechanism or
  for continuously fluctuating data. Consider MQTT Last Will
  and Testament (LWT) as a mitigation for the risk of loss of
  device communication instead of using shadows.
