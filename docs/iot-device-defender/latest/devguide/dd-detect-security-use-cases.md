

# Security use cases
<a name="dd-detect-security-use-cases"></a>

**Note**  
The AWS IoT Device Defender detect feature is no longer available to new customers. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

This section describes the different types of attacks that threaten your device fleet and the recommended metrics you can use to monitor for these attacks. We recommend using metric anomalies as a starting point to investigate security issues, but you should not base your determination of any security threats solely on a metric anomaly. 

To investigate an anomaly alarm, correlate the alarm details with other contextual information such as device attributes, device metric historical trends, Security Profile metric historical trends, custom metrics, and logs to determine if a security threat is present.

## Cloud-side use cases
<a name="Cloud-side-threats"></a>

Device Defender can monitor the following use cases on the AWS IoT cloud side.

**Intellectual property theft:**  
Intellectual property theft involves stealing a person's or companies' intellectual properties, including trade secrets, hardware, or software. It often occurs during the manufacturing stage of devices. Intellectual property theft can come in the form of piracy, device theft, or device certificate theft. Cloud-based intellectual property theft can occur due to the presence of policies that permit unintended access to IoT resources. You should review your [IoT policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) and turn on [Audit overly permissive checks](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit-checks.html) to identify overly permissive policies.  


****Related metrics:****  

<table>
<thead>
  <tr><th>Metric</th><th> Rationale </th></tr>
</thead>
<tbody>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-ip-address">Source IP</a> </td><td>If device is stolen, then its source IP address would fall outside of the normally expected IP address range for devices circulated in a normal supply chain.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-messages-received">Number of messages received</a></td><td rowspan="2">Because an attacker may use a device in cloud-based IP theft, metrics related to message counts or message sizes sent to the device from AWS IoT cloud can spike up, indicating a possible security issue.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-messages-received">Message size</a> </td></tr>
</tbody>
</table>


**MQTT-based data exfiltration: **  
Data exfiltration occurs when a malicious actor carries out an unauthorized data transfer from an IoT deployment or from a device. The attacker launches this type of attacks through MQTT against cloud-side data sources.  


****Related metrics:****  

<table>
<thead>
  <tr><th>Metric</th><th> Rationale </th></tr>
</thead>
<tbody>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-ip-address">Source IP</a> </td><td>If a device is stolen, then its source IP address would fall outside of the normally expected IP address range for devices circulated in a standard supply chain. </td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-messages-received">Number of messages received</a></td><td rowspan="2">Because an attacker may use a device in a MQTT-based data exfiltration, metrics related to message counts or message sizes sent to the device from AWS IoT cloud can spike up, indicating a possible security issue.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-messages-received">Message size</a> </td></tr>
</tbody>
</table>


**Impersonation:**  
An impersonation attack is where attackers pose as known or trusted entities in an effort to access AWS IoT cloud-side services, applications, data, or engage in command and control of IoT devices.   


****Related metrics:****  

<table>
<thead>
  <tr><th>Metric</th><th> Rationale </th></tr>
</thead>
<tbody>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-auth-failures">Authorization failures</a> </td><td rowspan="3">When attackers pose as trusted entities by using stolen identities, connectivity related metrics often spike, as the credentials may no longer be valid or may be used by a trusted device already. Anomalous behaviors in authorization failures, connection attempts, or disconnects point to a potential impersonation scenario.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-num-connection-attempts">Connection attempts</a> </td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-num-disconnects">Disconnects</a> </td></tr>
</tbody>
</table>


**Cloud Infrastructure abuse:**  
Abuse to AWS IoT cloud services occurs when publishing or subscribing to topics with a high message volume or with messages in large sizes. Overly permissive policies or device vulnerability exploit for command and control can also cause cloud infrastructure abuse. One of the main objectives of this attack is to increase your AWS bill. You should review your [IoT policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) and turn on [Audit overly permissive checks](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit-checks.html) to identify overly permissive policies.  


****Related metrics:****  

<table>
<thead>
  <tr><th>Metric</th><th> Rationale </th></tr>
</thead>
<tbody>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-messages-received">Number of messages received</a></td><td rowspan="3">The objective of this attack is to increase your AWS bill, metrics that monitor activities like message count, messages received and message size will spike up.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-messages-sent">Number of messages sent</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-messages-received">Message size</a> </td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-cloud-side-metrics.html#detect-ip-address">Source IP</a> </td><td>Suspicious source IP lists may appear, from which attackers generate their messaging volume.</td></tr>
</tbody>
</table>


## Device-side use cases
<a name="Device-side-threats"></a>

Device Defender can monitor the following use cases on your device side.

**Denial-of-service attack:**  
A denial-of-service (DoS) attack is aimed at shutting down a device or network, making the device or network inaccessible to their intended users. DoS attacks block access by flooding the target with traffic, or sending it requests that start a system slow-down or cause the system to fail. Your IoT devices can be used in DoS attacks.  


****Related metrics:****  

<table>
<thead>
  <tr><th>Metric</th><th> Rationale </th></tr>
</thead>
<tbody>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-all-packets-out">Packets out</a> </td><td rowspan="2">DoS attacks typically involve higher rates of outbound communication from a given device, and depending on the type of DoS attack, there could be an increase in either or both of the numbers of packets out and bytes out.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-all-bytes-out">Bytes out</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-destination-ip-addresses">Destination IP</a> </td><td>If you define the IP addresses/CIDR ranges your devices should communicate with, then an anomaly in destination IP can indicate unauthroized IP communication from your devices.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-listening-tcp-ports">Listening TCP ports</a></td><td rowspan="4">A DoS attack usually requires a larger command and control infrastructure where malware installed on your devices receives commands and information about who to attack and when to attack. Therefore, in order to receive such information, the malware would typically listen on ports that aren't normally used by your devices.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-num-listening-tcp-ports">Listening TCP port count</a> </td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-listening-udp-ports">Listening UDP ports</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-num-listening-udp-ports">Listening UDP port count</a> </td></tr>
</tbody>
</table>


**Lateral threat escalation:**  
Lateral threat escalation usually begins with an attacker gaining access to one point of a network, for example a connected device. The attacker then tries to increase their level of privileges, or their access to other devices through methods such as stolen credentials or vulnerability exploits.  


****Related metrics:****  

<table>
<thead>
  <tr><th>Metric</th><th> Rationale </th></tr>
</thead>
<tbody>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-all-packets-out">Packets out</a> </td><td rowspan="2">In typical situations, the attacker would have to run a scan on the local area network in order to perform reconnaisance and identify the available devices in order to narrow down their attack target selection. This kind of scan could result in a spike of bytes and packets out counts.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-all-bytes-out">Bytes out</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-destination-ip-addresses">Destination IP</a> </td><td>If a device is supposed to communicate with a known set of IP addresses or CIDRs, you can identify if it attempts to communicate with an abnormal IP address, which would often be a private IP address on the local network in a lateral threat escalation use case.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-auth-failures">Authorization failures</a> </td><td>As the attacker tries to increase their level of priviledges across an IoT network, they may use stolen credentials that have been revoked or have expired, which would cause increased authorization failures.</td></tr>
</tbody>
</table>


**Data exfiltration or surveillance:**  
Data exfiltration occurs when malware or a malicious actor carries out an unauthorized data transfer from a device or a network endpoint. Data exfiltration normally serves two purposes for the attacker, obtaining data or intellectual property, or conducting reconnaissance of a network. Surveillance means that malicious code is used to monitor user activities for the purpose of stealing credentials and gathering information. The metrics below can provide a starting point of investigating either type of attacks.  


****Related metrics:****  

<table>
<thead>
  <tr><th>Metric</th><th> Rationale </th></tr>
</thead>
<tbody>
  <tr><td> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-all-packets-out">Packets out</a></td><td rowspan="2">When data exfiltration or surveillance attacks occur, the attacker would often mirror the data being sent from the device rather than simply redirecting the data, which would be identified by the defender when they don't see the intended data coming. Such mirrored data would increase the total amount of data sent from the device significantly, resulting in a spike of packets and bytes out counts.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-all-bytes-out">Bytes out</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-destination-ip-addresses">Destination IP</a> </td><td>When an attacker is using a device in data exfiltration or surveilance attacks, the data would have to be sent to an abnormal IP address controlled by the attacker. Monitoring the destination IP can help identify such an attack.</td></tr>
</tbody>
</table>


**Cryptocurrency mining**  
Attackers leverage processing power from devices to mine cryptocurrency. Crypto-mining is a computationally intensive process, typically requiring network communication with other mining peers and pools.  


****Related metrics:****  

<table>
<thead>
  <tr><th>Metric</th><th> Rationale </th></tr>
</thead>
<tbody>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-destination-ip-addresses">Destination IP</a> </td><td>Network communication is typically a requirement during cryptomining. Having a tightly controlled list of IP addresses the device should communicate with can help identify unintended communication on a device, like cryptocurrency mining.</td></tr>
  <tr><td>CPU usage <a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-listening-tcp-ports">custom metric</a></td><td>Cryptocurrency mining requires intensive computation resulting in high utilization of the device CPU. If you choose to collect and monitor this metric, a higher-than-normal CPU usage could be an indicator of crypto-mining activities.</td></tr>
</tbody>
</table>


**Command and control, malware and ransomware**  
Malware or ransomware restricts your control over your devices, and limits your device functionality. In the case of a ransomware attack, data access would be lost due to encryption the ransomware uses.  


****Related metrics:****  

<table>
<thead>
  <tr><th>Metric</th><th> Rationale </th></tr>
</thead>
<tbody>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-destination-ip-addresses">Destination IP</a> </td><td>Network or remote attacks represent a large portion of attacks on IoT devices. A tightly controlled list of IP addresses the device should communicate with can help identify abnormal destination IPs resulted from a malware or ransomware attack.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-listening-tcp-ports">Listening TCP ports</a></td><td rowspan="4">Several malware attacks involve starting a command-and-control server that sends commands to execute on a device. This type of server is critical to a malware or ransomware operation and can be identified by tightly monitoring the open TCP/UDP ports and port counts.</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-num-listening-tcp-ports">Listening TCP port count</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-listening-udp-ports">Listening UDP ports</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/iot/latest/developerguide/detect-device-side-metrics.html#detect-num-listening-udp-ports">Listening UDP port count</a></td></tr>
</tbody>
</table>
