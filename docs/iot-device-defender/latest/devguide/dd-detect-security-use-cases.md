# Security use cases

This section describes the different types of attacks that threaten your device fleet and
the recommended metrics you can use to monitor for these attacks. We recommend using metric
anomalies as a starting point to investigate security issues, but you should not base your
determination of any security threats solely on a metric anomaly.

To investigate an anomaly alarm, correlate the alarm details with other contextual information
such as device attributes, device metric historical trends, Security Profile metric
historical trends, custom metrics, and logs to determine if a security threat is
present.

## Cloud-side use cases

Device Defender can monitor the following use cases on the AWS IoT cloud side.

**Intellectual property theft:**
Intellectual property theft involves stealing a person's or companies' intellectual properties, including trade secrets, hardware, or software.
It often occurs during the manufacturing stage of devices. Intellectual property theft can come in the form of piracy, device theft, or device certificate theft.
Cloud-based intellectual property theft can occur due to the presence of policies that permit unintended access to IoT resources. You
should review your [IoT policies](../../../iot/latest/developerguide/iot-policies.md "../../../iot/latest/developerguide/iot-policies.md") and turn on [Audit overly permissive checks](../../../iot/latest/developerguide/device-defender-audit-checks.md "../../../iot/latest/developerguide/device-defender-audit-checks.md") to identify overly permissive policies.

| **Related metrics:**                                                                                                                                                                                               | Metric                                                                                                                                                                                                              | Rationale |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [Source IP](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-ip-address "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-ip-address")                                 | If device is stolen, then its source IP address would fall<br>outside of the normally expected IP address range for<br>devices circulated in a normal supply chain.                                                 |
| [Number of messages received](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received") | Because an attacker may use a device in cloud-based IP<br>theft, metrics related to message counts or message<br>sizes sent to the device from AWS IoT cloud can spike up,<br>indicating a possible security issue. |
| [Message size](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received")                |

**MQTT-based data exfiltration:**
Data exfiltration occurs when a malicious actor carries out an unauthorized data transfer from
an IoT deployment or from a device. The attacker launches this type of
attacks through MQTT against cloud-side data sources.

| **Related metrics:**                                                                                                                                                                                               | Metric                                                                                                                                                                                                               | Rationale |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [Source IP](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-ip-address "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-ip-address")                                 | If a device is stolen, then its source IP address would fall<br>outside of the normally expected IP address range for<br>devices circulated in a standard supply chain.                                              |
| [Number of messages received](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received") | Because an attacker may use a device in a MQTT-based data exfiltration, metrics related to message counts or message sizes sent to the device from AWS IoT cloud can spike up, indicating a possible security issue. |
| [Message size](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received")                |

**Impersonation:**
An impersonation attack is where attackers pose as known or trusted entities in an effort to
access AWS IoT cloud-side services, applications, data, or engage in command and
control of IoT devices.

| **Related metrics:**                                                                                                                                                                                                   | Metric                                                                                                                                                                                                                                                                                                                                             | Rationale |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [Authorization failures](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-auth-failures "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-auth-failures")                  | When attackers pose as trusted entities by using<br>stolen identities, connectivity related metrics often spike,<br>as the credentials may no longer be valid or may be used by<br>a trusted device already. Anomalous behaviors in<br>authorization failures, connection attempts, or disconnects<br>point to a potential impersonation scenario. |
| [Connection attempts](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-num-connection-attempts "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-num-connection-attempts") |
| [Disconnects](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-num-disconnects "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-num-disconnects")                         |

**Cloud Infrastructure abuse:**
Abuse to AWS IoT cloud services occurs when publishing or subscribing to topics with a high
message volume or with messages in large sizes. Overly permissive policies or device vulnerability exploit for command and control can also cause cloud infrastructure abuse.
One of the main objectives of this attack is to increase your AWS bill. You should review your [IoT policies](../../../iot/latest/developerguide/iot-policies.md "../../../iot/latest/developerguide/iot-policies.md") and turn on [Audit overly permissive checks](../../../iot/latest/developerguide/device-defender-audit-checks.md "../../../iot/latest/developerguide/device-defender-audit-checks.md") to identify overly permissive policies.

| **Related metrics:**                                                                                                                                                                                               | Metric                                                                                                                                                                    | Rationale |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [Number of messages received](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received") | The objective of this attack is to increase your<br>AWS bill, metrics that monitor activities like message<br>count, messages received and message size will spike<br>up. |
| [Number of messages sent](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-sent "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-sent")             |
| [Message size](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-messages-received")                |
| [Source IP](../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-ip-address "../../../iot/latest/developerguide/detect-cloud-side-metrics.md#detect-ip-address")                                 | Suspicious source IP lists may appear, from which attackers generate their messaging volume.                                                                              |

## Device-side use cases

Device Defender can monitor the following use cases on your device side.

**Denial-of-service attack:**
A denial-of-service (DoS) attack is aimed at shutting down a device or network, making the
device or network inaccessible to their intended users. DoS attacks block
access by flooding the target with traffic, or sending it requests that
start a system slow-down or cause the system to fail. Your IoT devices can
be used in DoS attacks.

| **Related metrics:**                                                                                                                                                                                                          | Metric                                                                                                                                                                                                                                                                                                                                       | Rationale |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [Packets out](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-packets-out "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-packets-out")                              | DoS attacks typically involve higher rates of outbound<br>communication from a given device, and depending on the<br>type of DoS attack, there could be an increase in either<br>or both of the numbers of packets out and bytes<br>out.                                                                                                     |
| [Bytes out](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-bytes-out "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-bytes-out")                                    |
| [Destination IP](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-destination-ip-addresses "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-destination-ip-addresses")         | If you define the IP addresses/CIDR ranges<br>your devices should communicate with,<br>then an anomaly in destination IP can indicate unauthroized<br>IP communication from your devices.                                                                                                                                                    |
| [Listening TCP ports](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-listening-tcp-ports "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-listening-tcp-ports")              | A DoS attack usually requires a larger command and control infrastructure where malware installed on<br>your devices receives commands and information about who to attack and when to attack.<br>Therefore, in order to receive such information,<br>the malware would typically listen on ports that aren't normally used by your devices. |
| [Listening TCP port count](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-num-listening-tcp-ports "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-num-listening-tcp-ports") |
| [Listening UDP ports](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-listening-udp-ports "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-listening-udp-ports")              |
| [Listening UDP port count](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-num-listening-udp-ports "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-num-listening-udp-ports") |

**Lateral threat escalation:**

Lateral threat escalation usually begins with an attacker gaining access
to one point of a network, for example a connected device. The attacker then
tries to increase their level of privileges, or their access to other
devices through methods such as stolen credentials or vulnerability
exploits.

| **Related metrics:**                                                                                                                                                                                                  | Metric                                                                                                                                                                                                                                                                                                       | Rationale |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| [Packets out](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-packets-out "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-packets-out")                      | In typical situations, the attacker would have to run<br>a scan on the local area network in order to perform<br>reconnaisance and identify the available devices in<br>order to narrow down their attack target selection. This<br>kind of scan could result in a spike of bytes and<br>packets out counts. |
| [Bytes out](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-bytes-out "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-bytes-out")                            |
| [Destination IP](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-destination-ip-addresses "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-destination-ip-addresses") | If a device is supposed to communicate with a known<br>set of IP addresses or CIDRs, you can identify if it<br>attempts to communicate with an abnormal IP address,<br>which would often be a private IP address on the local<br>network in a lateral threat escalation use case.                            |
| [Authorization failures](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-auth-failures "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-auth-failures")               | As the attacker tries to increase their level of priviledges across an IoT network,<br>they may use stolen credentials that have been revoked or have expired,<br>which would cause increased authorization failures.                                                                                        |

**Data exfiltration or surveillance:**

Data exfiltration occurs when malware or a malicious actor carries out an
unauthorized data transfer from a device or a network endpoint. Data
exfiltration normally serves two purposes for the attacker, obtaining data
or intellectual property, or conducting reconnaissance of a network.
Surveillance means that malicious code is used to monitor user activities
for the purpose of stealing credentials and gathering information. The
metrics below can provide a starting point of investigating either type of
attacks.

| **Related metrics:**                                                                                                                                                                                                  | Metric                                                                                                                                                                                                                                                                                                                                                                                                                               | Rationale |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| [Packets out](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-packets-out "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-packets-out")                      | When data exfiltration or surveillance attacks occur,<br>the attacker would often mirror the data being sent from<br>the device rather than simply redirecting the data,<br>which would be identified by the defender when they<br>don't see the intended data coming. Such mirrored data<br>would increase the total amount of data sent from the<br>device significantly, resulting in a spike of packets<br>and bytes out counts. |
| [Bytes out](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-bytes-out "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-all-bytes-out")                            |
| [Destination IP](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-destination-ip-addresses "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-destination-ip-addresses") | When an attacker is using a<br>device in data exfiltration or surveilance attacks, the<br>data would have to be sent to an abnormal IP address<br>controlled by the attacker. Monitoring the destination<br>IP can help identify such an attack.                                                                                                                                                                                     |

**Cryptocurrency mining**

Attackers leverage processing power from devices to mine cryptocurrency.
Crypto-mining is a computationally intensive process, typically requiring
network communication with other mining peers and pools.

| **Related metrics:**                                                                                                                                                                                                  | Metric                                                                                                                                                                                                                                                    | Rationale |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [Destination IP](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-destination-ip-addresses "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-destination-ip-addresses") | Network communication is typically a requirement<br>during cryptomining. Having a tightly controlled list of<br>IP addresses the device should communicate with can help<br>identify unintended communication on a device, like<br>cryptocurrency mining. |
| CPU usage [custom metric](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-listening-tcp-ports "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-listening-tcp-ports")  | Cryptocurrency mining requires<br>intensive computation resulting in high utilization of<br>the device CPU. If you choose to collect and monitor<br>this metric, a higher-than-normal CPU usage could be an<br>indicator of crypto-mining<br>activities.  |

**Command and control, malware and ransomware**

Malware or ransomware restricts your control over your devices, and limits
your device functionality. In the case of a ransomware attack, data access
would be lost due to encryption the ransomware uses.

| **Related metrics:**                                                                                                                                                                                                          | Metric                                                                                                                                                                                                                                                                                    | Rationale |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [Destination IP](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-destination-ip-addresses "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-destination-ip-addresses")         | Network or remote attacks represent a large portion of<br>attacks on IoT devices. A tightly controlled list of IP<br>addresses the device should communicate with can help<br>identify abnormal destination IPs resulted from a<br>malware or ransomware attack.                          |
| [Listening TCP ports](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-listening-tcp-ports "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-listening-tcp-ports")              | Several malware attacks involve starting a<br>command-and-control server that sends commands to<br>execute on a device. This type of server is critical to<br>a malware or ransomware operation and can be identified<br>by tightly monitoring the open TCP/UDP ports and port<br>counts. |
| [Listening TCP port count](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-num-listening-tcp-ports "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-num-listening-tcp-ports") |
| [Listening UDP ports](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-listening-udp-ports "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-listening-udp-ports")              |
| [Listening UDP port count](../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-num-listening-udp-ports "../../../iot/latest/developerguide/detect-device-side-metrics.md#detect-num-listening-udp-ports") |
