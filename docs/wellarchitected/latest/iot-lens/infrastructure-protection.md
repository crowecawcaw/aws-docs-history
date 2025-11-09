# Infrastructure protection

Design time is the ideal phase for considering security
requirements for infrastructure protection across the entire
lifecycle of your device and solution. By considering your devices
as an extension of your infrastructure, you can take into account
how the entire device lifecycle impacts your design for
infrastructure protection. From a cost standpoint, changes made in
the design phase are less expensive than changes made later. From
an effectiveness standpoint, data loss mitigations implemented at
design time are likely to be more comprehensive than mitigations
retrofitted. Therefore, planning the device and solution security
lifecycle at design time reduces business risk and provides an
opportunity to perform upfront infrastructure security analysis
before launch.

One way to approach the device security lifecycle is through
supply chain analysis. The IoT supply chain includes the actors,
processes and assets that participate in the realization (For
example, development, design, maintenance, and patch management)
of any IoT device.

For example, even a modestly sized IoT device manufacturer or
solution integrator has a large number of suppliers that make up
its supply chain, whether directly or indirectly. To maximize
solution lifetime and reliability, make sure that you are
receiving authentic components.

Software is also part of the supply chain. The production firmware
image for a device includes drivers and libraries from many
sources including silicon partners, open-source aggregation sites
such as GitHub and SourceForge, previous first-party products, and
new code developed by internal engineering.

To understand the downstream maintenance and support for
first-party firmware and software, you must analyze each software
provider in the supply chain to determine if it offers support and
how it delivers patches. This analysis is especially important for
connected devices. Software bugs are expected and considered a
normal part of development. Software bugs represent a risk to your
customers especially when a vulnerable device can be accessed
remotely. Your IoT device manufacturer or solution engineering
team must learn about and patch bugs in a timely manner to reduce
these risks.

All of the infrastructure protection capabilities available for
securing AWS services should be applied to the cloud-hosted
components of the IoT application. There are integration points
where AWS IoT Core interacts with other AWS services such as AWS Lambda functions which define specific processing for the IoT
application. Using the AWS IoT rules engine implies the definition
of rules that are analyzed and then trigger downstream actions to
other AWS services based on the messages sent over the MQTT topic
stream. Since AWS IoT communicates to your other AWS resources,
configure the right service role permissions for your application.
The same applies for connected devices with AWS IoT Greengrass for
cloud services the device needs to talk to.

AWS offers flexible ways and design patterns to establish a secure
connection to the AWS environment from the edge. When choosing a
secure connection to the AWS environment, take into consideration
the use case requirements such as latency and data locality to
make sure that the chosen connection solution meets your
performance and compliance requirements. Use AWS Systems Manager
to carry out routine management tasks on edge computing resources.

IoT devices are often deployed behind restricted firewalls at
remote sites. Use secure tunneling for AWS IoT Device Management
to access IoT devices for troubleshooting, configuration updates,
and other operational tasks. Consider using AWS IoT Greengrass for
secure remote application management. Take advantage of
on-premises managed infrastructure solutions such as AWS Outposts,
AWS Storage Gateway, AWS Snow Family to simplify management and
monitoring.

| IOTSEC07: What infrastructure protection<br>configuration has been defined for your AWS organization and<br>accounts? |
| --------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                       |

All infrastructure protection controls that are used to secure
your AWS organization and AWS accounts are applicable to IoT
applications running in those accounts. IoT applications typically
use a wide range of serverless technologies as well as
cloud-hosted databases. Securing the network connectivity and
access to these resources directly impacts the security of your
IoT applications.

In addition to those controls, additional consideration should be
placed on securing the infrastructure in which or around where IoT
devices are deployed and operated. This includes the management of
the hardware, firmware, and software installed and running in the
IoT devices themselves.

## IOTSEC07-BP01 Configure cloud infrastructure to have secure communications

Limit the communications paths and protocols used by the
solution to only those which are necessary for the applications.
For example, consider using only MQTT publish or subscribe
communications when communicating with IoT devices. In addition,
if possible, IoT devices should only connect out-bound to
trusted and verified and authenticated service endpoints and not
set up processes which listen for connections.

When it is necessary for IoT devices to listen for connection
requests, the sources of these connections should be strictly
limited. Any connecting client which is connecting to the device
must be authenticated before the device communicates with that
client. This applies whether or not the device itself is acting
as a proxy for clients which connect to it. Authentication
processing at the device is a device-specific design decision
and brings additional complications such as how to authenticate,
using what identity provider, and so on. This further supports
the recommendation for devices to avoid listening for connection
requests.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC07-BP01-01** _Use only MQTT
publish/subscribe in IoT devices when possible._

Configure devices to use MQTT communications and use the IoT
Device Client or other MQTT client software to enable this
communication.

**Prescriptive guidance
IOTSEC07-BP01-02** _Design IoT devices and
solutions so that devices only connect and do not listen for
connections._

Refrain from creating server-type applications running on IoT
devices. If necessary for handling local administration or
configuration types of activities, consider only enabling such
activities based on being placed into a maintenance mode and
then stopping these applications during normal operation.

**Prescriptive guidance
IOTSEC07-BP01-03** _When listening for
connections in IoT devices, authenticate connecting
clients._

Require authentication by any connecting entity which connects
to the device. Be sure that there are no default credentials
(passwords, keys, or tokens) which could become compromised and
then used to access other devices. Authentication processing at
the device is a device-specific design decision and brings
additional complications such as how to authenticate, using what
identity provider, and so on. This further supports the
recommendation for devices to avoid listening for connection
requests. To enable local administration, initial installation
or provisioning should not rely on default credentials.

For example, local initial installation or provisioning on first
start or after factory reset may require a local administrator
to create a set of credentials or authenticate with a separate
identity provider.

**Prescriptive guidance
IOTSEC07-BP01-04** _For sizeable data
transfers like large file transfer, use encrypted HTTPS or SFTP
communications with an IoT device as the connecting client._

Use TCP protocols which are set up for handling bulk or
large data transfers for performing those tasks. Connect from
the IoT device to the remote system in order to put to or pull
from files from that remote system. Verify the contents of those
files using digital signatures or file hashes retrieved through
a separate channel.

## IOTSEC07-BP02 Define networking configuration which restricts communications to only those ports and protocols which are required

Restrict the possible communications protocols, paths, and ports
on which IoT devices can communicate. Also, configure network
communications so that there are separate network zones, with
only the allowed protocols, ports, and connection initiation
paths defined between these zones.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC07-BP02-01** _Use a minimum number of
protocols for device communication._

If only MQTT communications is required, restrict communications
to only the IP port used for those communications. Consider
using a protocol-aware firewall to restrict traffic to only that
type of protocol. If HTTPS communications is also necessary,
enable only the two protocols/ports.

**Prescriptive guidance
IOTSEC07-BP02-02** _Configure network zones
which have strict protection for inbound/outbound communications
and connection initiation._

Configure network zoning using virtual or physical network
connections. Use virtual network connection configuration to
restrict connection initiation direction., Allow only outbound
connections from IoT devices and restrict inbound
connections from outside the local network.

## IOTSEC07-BP03 Log and monitor network configuration changes and network communication

The ability to monitor and log communications assists in
verifying that only the expected communications is taking place
in the infrastructure. Also, having network logs allows for
forensic analysis and problem determination if and when a
problem is suspected or identified.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC07-BP03-01** _Set up network logging at
network zone connection points_

Use network routers or switches and firewalls between network
zones. Set up network logging on those devices and appliances.

**Prescriptive guidance
IOTSEC07-BP03-02** _Send logs to a centralized
logging infrastructure to enable remote problem determination
and forensic analysis._

Centralize logs to offload the logs from the remote devices and
appliances. This also allows for network communications analysis
across the overall solution in addition to looking at individual
network zone activity. Centralized logging solutions are
available on AWS. For example,
[Amazon OpenSearch Service Centralized Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/ "https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/") is a
centralized log management solution. Also,
[Amazon
Security Lake](https://aws.amazon.com/security-lake/ "https://aws.amazon.com/security-lake/") can be used to understand, review, and act
on security-related events in your computing environment.

| IOTSEC08: How is the infrastructure into<br>which your IoT devices are deployed managed and<br>maintained? |
| ---------------------------------------------------------------------------------------------------------- |
|                                                                                                            |

After initial installation and configuration of an IoT solution,
including the IoT devices, the solution components, networking
configuration, and IoT devices themselves will still require
ongoing maintenance and management. IoT devices should have a
defined method for managing and maintaining their firmware,
software, and configuration. This also includes maintaining or
updating the identity of the devices, Also, the devices must be
able to authenticate on connection start up as well as verify
the identity of the endpoints which they connect to and
communicate with.

## IOTSEC08-BP01 Define an automated and monitored mechanism for deploying, managing, and maintaining networks to which IoT devices are connected

Having an automated and monitored mechanism for deploying
network configuration allows for making changes to this network
configuration depending on conditions. For example, if there is
an issue or event detected in some portion of the network, that
network zone could be isolated/quarantined until the situation
is resolved. Conversely, separate network zones could be
protected from issues or events, at the expense of some
degradation in connectivity for a limited time, if an issue or
event on that network zone is detected.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC08-BP01-01** _Use virtual network
configurations to enable remote management of network
configurations._

In IIOT environments, enable remote management of network
configuration. By enabling remote management of network
configuration, the network can be adjusted over time to meet the
needs of the solution or situation. Be aware, however, that such
capability also comes with an added risk in that the remote
configuration method itself must be protected. Consider using
Amazon VPC, AWS Virtual Private Network, AWS Direct Connect, and
Amazon Outposts to configure network connectivity.

## IOTSEC08-BP02 Define an automated and monitored mechanism for deploying, managing, and maintaining network configurations for IoT devices

Having an automated and monitored mechanism for deploying,
managing, and maintaining network configuration in IoT devices
allows for making changes to this network configuration
depending on conditions. For example, if there is an issue or
event in some portion of the network, the network configuration
in the device could be adjusted until the situation is resolved.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC08-BP02-01** _Use IoT Jobs to schedule
and run management and update activities in IoT
devices._

IoT Jobs allows actions to be carried out in IoT devices based
on both a schedule and the set of devices to which the jobs
apply.

**Prescriptive guidance
IOTSEC08-BP02-02** _Use IoT Secure Tunneling
sparingly to remotely access a device to take some corrective
action._

IoT Secure Tunneling allows for direct interaction with the
device. However, this should be used only as a last resort since
it implies that a human would be remotely attaching to and
interacting with the device. Using specific remote command and
control mechanisms is preferred to relying on opening up a
secure tunnel through which a human operate would remotely
access a device to perform some action. Remote command and
control allow for much better input/output parameter checking
for the operations being requested.

| IOTSEC09: What processes are used to<br>manage and maintain the hardware or software deployed and<br>configured in your IoT devices? |
| ------------------------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                      |

After initial installation and configuration of the hardware,
firmware, and software into the IoT device, usually at device
manufacturing time, there are often new vulnerabilities
discovered in the hardware, firmware, or software which has been
embedded into those devices. There should be some means of
updating the firmware or software in the devices so that a
vulnerability, if deemed to be serious enough, can be remediated
or mitigated. There are several ways to go about managing and
maintaining the firmware or software which range in their cost
and convenience.

Using an automated, repeatable, and monitored mechanism which
has minimal manual (human) intervention lowers the cost of each
deployment and reduces the potential of human error.

## IOTSEC09-BP01 Manage and maintain IoT Device software using an automated, monitored, and audited mechanism

Having an automated, monitored, and audited mechanism for
deploying, managing, and maintaining device software in IoT
devices allows for making changes to this device software over
time. The device software installed in each device should be
maintained using a software bill of materials (SBOM). New
features and fixes or updates can be applied to the device
which extend its useful lifetime, address security
vulnerabilities, or enable the device to perform more actions.
Use
[AWS IoT Device Management Software Package Catalog (SPC)](../../../iot/latest/developerguide/software-package-catalog.md "../../../iot/latest/developerguide/software-package-catalog.md") to
aid in maintaining device software inventories.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC09-BP01-01** _Use IoT AWS IoT Greengrass and
AWS IoT Greengrass component deployments to update software in IoT edge
devices._

IoT AWS IoT Greengrass supports a runtime environment in which
concurrent components can be started, stopped, and updated.
Communications is supported between components. This allows for
complex parallel processing of multiple tasks within the device.
IoT AWS IoT Greengrass has extensive support for defining and managing
components and component versions as well as managing the
deployment of those components into fleets of IoT AWS IoT Greengrass
devices.

**Prescriptive guidance
IOTSEC09-BP01-02** _Use IoT Jobs to schedule
and run management and update activities in IoT
devices._

IoT Jobs allows actions to be carried out in IoT devices based
on both a schedule and the set of devices to which the jobs
apply.

**Prescriptive guidance
IOTSEC09-BP01-03** _Use IoT Secure Tunneling
sparingly to remotely access a device to take some corrective
action._

IoT Secure Tunneling allows for direct interaction with the
device. However, this should be used only as a last resort since
it implies that a human would be remotely attaching to and
interacting with the device. Using specific remote command and
control mechanisms is preferred to relying on opening up a
secure tunnel through which a human operate would remotely
access a device to perform some action. Remote command and
control allow for much better input/output parameter checking
for the operations being requested.

## IOTSEC09-BP02 Manage IoT device configuration using automated and controlled mechanisms

In addition to managing the networking configuration and
firmware or software in the IoT devices, the configuration
settings in the device must also be managed and updated. Like
updating the firmware or software, this should be done using an
automated, monitored, and audited mechanism.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC09-BP02-01** _Use IoT AWS IoT Greengrass and
AWS IoT Greengrass component deployments to update configuration in IoT
devices._

IoT AWS IoT Greengrass supports a runtime environment in which
concurrent components can be started, stopped, and updated.
Communications is supported between components. This allows for
complex parallel processing of multiple tasks within the device.
IoT AWS IoT Greengrass has extensive support for defining and managing
components and component versions as well as managing the
deployment of those components into fleets of IoT AWS IoT Greengrass
devices. One aspect of component management is the configuration
of the components themselves. This can be used to update
configuration in the IoT devices.

**Prescriptive guidance
IOTSEC09-BP02-02** _Use IoT Jobs to schedule
and run management and update activities in IoT
devices._

IoT Jobs allows actions to be carried out in IoT devices based
on both a schedule and the set of devices to which the jobs
apply.

**Prescriptive guidance
IOTSEC09-BP02-03** _Use IoT Secure Tunneling
sparingly to remotely access a device to take some corrective
action._

IoT Secure Tunneling allows for direct interaction with the
device. However, this should be used only as a last resort since
it implies that a human would be remotely attaching to and
interacting with the device. Using specific remote command and
control mechanisms is preferred to relying on opening up a
secure tunnel through which a human operate would remotely
access a device to perform some action. Remote command and
control allow for much better input or output parameter checking
for the operations being requested.
