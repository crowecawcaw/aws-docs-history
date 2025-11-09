# Foundations

| CMREL_1: Have you defined your message prioritization policy? |
| ------------------------------------------------------------- |
|                                                               |

Connected vehicles generate a large amount of data that is sent to the cloud via
messages. It's important to prioritize the message flow and handle different message
severities with different policies.

Connected vehicles generate a large amount of data that must be sent to the cloud via
messages. It's important to prioritize the message flow and handle different severities with
different policies.

**[CMREL\_BP1.1] Defining message tier matrix**

The connected mobility solution must classify messages from the vehicle fleet to the
cloud backend in at least two tiers, such as:

- High priority messages
- Low priority messages
  These two tiers must be processed using different approaches when it comes to resiliency
  as described in the following sections. The tier structure is multidimensional to account
  for messages that should be sent as soon as possible or not sent at all (urgency dimension),
  and for relevancy. In the urgency dimension are messages that pertain to GPS and ADAS
  messages that must be sent, even if they cannot be sent in real time (relevance dimension).
  Messages for emergency calls are also in this dimension. Lowest on the priority list (low
  urgency and low relevance) include telemetry messages that can be sent in batches on a given
  schedule.

**[CMREL\_BP1.2] Have a strategy for critical
functions**

Connected mobility should implement critical functions. such as emergency calls in
which messages from the vehicle must be delivered to the cloud no matter what, to overcome
transient failures in the connectivity as well as in the control plane. Those messages
should sit on top of the tier matrix (high relevance, high urgency). In such cases, you
should plan for redundancy for every physical or logical component of in-vehicle as well as
the communication layer with the cloud (such as SIM failure, modem failure, and telco
failure).

Consider building the control plane in multiple Regions and have the vehicles connect to
the first available endpoint for these critical functions.

| CMREL_2: How do you ensure that you do not overflow your communication channel<br>to the cloud? |
| ----------------------------------------------------------------------------------------------- |
|                                                                                                 |

Messaging from vehicles to the cloud is likely to be unpredictable, generating spikes
that might approach AWS service quotas. If proper measures are not taken, these spikes
could result in message throttling, application impairment, or both.

**[CMREL\_BP2.1] Guardrail chatty vehicles**

The connected mobility solution must tolerate anomalies in the message workflows
received from the vehicle fleet. The connected mobility control plane that receives messages
from the vehicle fleet must tolerate spikes in the vehicle's messaging flow throttling low
priority messages down to avoid exceeding service quotas and unwanted cost spikes. If
throttling of low priority messages is not enough to avoid exceeding a service quota,
messages must be classified in more than two tiers and a policy must be implemented to
throttle messages down when appropriate.

**[CMREL\_BP2.2] Avoid connection surge to the
cloud**

A vehicle’s side application and firmware must implement a randomized connection to the
backend cloud applications to avoid unnecessary peak traffic. Situations where the entire
fleet attempts the same operation at the same time must be avoided. Traffic generated from
low priority tier messages should be randomized. Navigating the tier structure bottom up,
trade off decision must be taken and implemented whether to randomize the traffic avoiding
connection peaks or increase a service quota (where applicable). The same randomized
behavior must be implemented on the cloud backend for messages that are being sent to the
vehicles.

| CMREL_3: Do you have a strategy in case connection certificates are unavailable<br>or accidentally deleted? |
| ----------------------------------------------------------------------------------------------------------- |
|                                                                                                             |

As a best practice, vehicles establish a connection to the backend by exchanging
certificates. The connected mobility control plane must store these certificates with the
highest level of durability, considering that installing new certificates to the client
likely requires the vehicles to be called back at the OEM or auto dealership. Backup
strategy must be built and emergency registration procedure must be available. Be sure to
test both the restore procedure and the emergency procedure with tabletop exercises.

**[CMREL\_BP3.1] Implement just-in-time provisioning and
registration**

When using AWS IoT Core to connect vehicles to the AWS Cloud, it’s a best practice to
implement just-in-time provisioning (JITP), just-in-time registration (JITR), or both. In
both cases, certificates are provisioned the first time devices connect to AWS IoT Core by
using a certificate template (JITP) or an AWS Lambda function (JITR). Using JITP and JITR can
help restore a compromised device registry.

**[CMREL\_BP3.2] Manual backup of the device
registry**

AWS IoT Core stores information about your devices in the device registry. It also
stores CA certificates, device certificates, and device shadow data. In the event of
hardware or network failures, this data is automatically replicated across Availability
Zones but not across Regions.

AWS IoT Core publishes MQTT events when the device registry is updated. You can use
these messages to back up your registry data and save it somewhere, like a DynamoDB table.
You are responsible for saving certificates that AWS IoT Core creates for you or those you
create yourself.

| CMREL_4: How is your connected mobility solution resilient to unintended<br>access? |
| ----------------------------------------------------------------------------------- |
|                                                                                     |

Every infrastructure is susceptible to unintended access and threat actors. Connected
mobility is no exception. Your connected mobility solution should implement the security by
design approach to reduce the scope of impact and mitigate and help prevent inadvertent
access. The solution should be resilient to events even if some functions are impaired by
these issues.

**[CMREL\_BP4.1] Implementing a layered approach**

An OEM can mitigate the negative impact of unintended access events on connected
vehicles by adopting a layered approach. In vehicle design, physical networks can be
separated by artificial layers. For example, you can create an engine control unit layer, an
in-vehicle communication network layer, and an external interfaces layer. The layer creation
will involve technologies such as gateways, firewalls, message authentication, encryption,
and intrusion detection and prevention systems. During vehicle manufacturing, several
practices can also be considered to identify and mitigate connected vehicle issues and
risks, including:

- Developing over-the-air (OTA) update capabilities for connected vehicle software and
  firmware.
- Conducting risk assessment and attack testing.
- Creating domain separation for in-vehicle networks.

Mission- and safety-critical components in a connected vehicle can be separated from
non-critical components, and given limited connectivity to external networks through a
few specific communication channels.

| CMREL_5: How do you mitigate the impact of impairments in the connection layer<br>between vehicles and the AWS Cloud? |
| --------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                       |

Connected mobility is a peculiar scenario in Internet of Things (IoT) given that the
things don’t have a reliable Local Area Network (LAN) to which they are connected. Vehicles
use mobile connectivity which is likely provided by a third party, and vehicles might move
to locations where the mobile connectivity is limited or not available at all.

**[CMREL\_BP5.1] Account for telco providers
outages**

Vehicles connect to the cloud control plane leveraging on telematic providers services
(telco), the connected mobility solution must account for failures in this transport layer.
The solution must be able to distinguish if a connection drop has been caused by the
vehicle, the telco, or the control plane in the cloud.

**[CMREL\_BP5.2] Implement in-vehicle
functionalities**

Connected mobility application reliability must also encompass the vehicle itself.
Vehicles might be operating in remote locations and deal with intermittent connectivity, or
loss in connectivity, due to a variety of external factors that are out of your connected
mobility application’s control. For example, if an ISP is interrupted for several hours, how
will the vehicle behave and respond to these long periods of potential network outage?
Implement a minimum set of embedded operations on the vehicle to make it more resilient to
the nuances of managing connectivity and communication to AWS control plane.

The vehicle must be able to operate without internet connectivity. You must implement
robust operations in your vehicle firmware and software to provide the basic capabilities.
Store important messages durably offline and, once reconnected, send those messages to the
AWS control plane. Implement exponential retry and back-off logic when connection attempts
fail.
