# Incident response

Being prepared for incident response in IoT requires planning on
how you will deal with two types of incidents in your IoT
workload. The first type of incident is an attempt by a threat
actor to access an individual IoT device to disrupt the
performance or change the device's behavior. The second incident
is a broad event, such as network outages or DDoS attacks. In both
scenarios, the architecture of your IoT application and
infrastructure plays a large role in determining how quickly you
will be able to detect and diagnose incidents, correlate the data
across the incident, and then subsequently apply runbooks to
respond and recover the affected devices in an automated, reliable
fashion.

For IoT applications, follow the following best practices for
incident responses:

- Organize sets of IoT devices into different groups based on
  device attributes such as location and hardware version.
- Enable searching of IoT devices by dynamic attributes, such as
  connectivity status, firmware version, application status, and
  device health.
- Stage OTA updates for IoT devices and deploy to devices in
  waves over a period of time. Deployment rollouts should be
  monitored and aborted if devices fail to maintain the
  appropriate KPIs.
- Test and verify that the update process is resilient to
  errors, and devices can recover and roll back from a failed
  software update.
- Keep detailed logs, metrics, and device telemetry for IoT
  devices that contain contextual information about how a device
  is currently performing and has performed over a period of
  time.
- Montor the overall health of your fleet using fleet-wide
  metrics. Alert when operational KPIs are not met for a period
  of time.
- Quarantine IoT devices that deviate from expected behavior.
  Inspect and analyze the device for potential compromise of the
  device by hardware tampering, firmware modification or
  application code modification.
- Test incident response procedures on a periodic basis.

Implement a strategy in which your Information Security team can
quickly identify the devices that need remediation. Make sure that
the Information Security team has runbooks that consider firmware
versioning and patching for device updates. Create automated
processes that proactively apply security patches to vulnerable
devices as they come online.

Implement a monitoring solution in the operations technology (OT),
IoT and IIoT environments to create an industrial network traffic
baseline and monitor for anomalies and any deviation from the
baseline. Collect security logs and analyze them in real-time
using dedicated tools, for example, security information and event
management (SIEM) class solutions such as within a security
operation center (SOC). AWS works with a number of OT Intrusion
Detection System (IDS) and SIEM partners that can be found on AWS Marketplace.

At a minimum, your security team should be able to detect an
incident on a specific device based on the device logs and current
device behavior. After an incident is identified, the next phase
is to quarantine the device. To implement this with AWS IoT
services, you can use AWS IoT Thing Groups with more restrictive
IoT policies along with enabling custom group logging for those
devices. This allows you to only enable features that relate to
troubleshooting, as well as gather more data to understand root
cause and remediation. Lastly, after an incident has been
resolved, you must be able to deploy a firmware and software
update to the device to return it to a known good state.

| IOTSEC11: How do you plan the security lifecycle of your IoT devices? |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                       | The security lifecycle of your IoT devices includes everything, from how you choose your suppliers, contract manufacturers, and other outsourced relationships to how you manage security in your third-party firmware and manage security events over time. With visibility into the full spectrum of actors and activities in your hardware and software supply chain, you can be better prepared to respond to compliance questions, detect and mitigate events, and avoid common security risks related to third-party components. ## IOTSEC11-BP01 Build incident response mechanisms to address security events at scale There are several formalized incident management methodologies in common use. The processes involved in monitoring and managing incident response can be extended to IoT devices. For instance, AWS IoT Device Management capabilities provide fleet analysis and activity tracking to identify potential issues, in addition to mechanisms to enable an effective response. **Level of risk exposed if this best practice is not established:** Medium **Prescriptive guidance IOTSEC11-BP01-01** _Make sure that IoT devices are searchable by using a device management solution._ Devices should be grouped by dynamic attributes, such as connectivity status, firmware version, application status, and device health. **Prescriptive guidance IOTSEC11-BP01-02** _Quarantine any device that deviates from expected behavior._ Inspect the device for potential issues in the configurations, firmware or applications using device logs or metrics. If a risk or anomaly is detected, the device can be diagnosed remotely provided that capability exists. For example, Configure AWS IoT Secure Tunneling to remotely diagnose a fleet of devices. If remote diagnosis is not sufficient or available, the other option is to push a security patch, application or firmware upgrade while the device is quarantined. When sending code to devices, the best practice is to sign the firmware or software and to verify the signature at the device prior to applying the update or code. This allows devices to detect if the code has been modified in transit. For example, With Code Signing for AWS IoT, you can sign code that you create for IoT devices supported by Amazon FreeRTOS and AWS IoT device management. In addition, the signed code can be valid for a limited amount of time to avoid further manipulation. **Prescriptive guidance IOTSEC11-BP01-03** _Over the air (OTA) update should be configured and staged for deployment activation during regular maintenance._ Whether it's a security patch or a firmware update, an update to a config file on a device, or a factory reset, you need to know which devices in your fleet have received and processed any of your updates, either successfully or unsuccessfully. In addition, a staged rollout is recommended to reduce the scope of a bad update. Rollouts should be able to be aborted with devices returning to a failsafe condition on a failed update. For example, you can use AWS IoT Jobs to roll out OTA updates of security patches and device configurations in a staged manner with required rollout and abort configuration settings. ## IOTSEC11-BP02 Require timely vulnerability notifications and software updates from your providers Components in a device bill of materials (BOM), such as secure elements (SEs) or a trusted platform module (TPM) for key or certificate storage, can make use of updatable software components. Some of this software might be contained in the Board Support Package (BSP) assembled for your device. You can help to mitigate device-side security issues quickly by knowing where the security-sensitive software components are within your device software stack, and by understanding what to expect from component suppliers with regard to security notifications and updates. **Level of risk exposed if this best practice is not established:** Medium **Prescriptive guidance IOTSEC11-BP02-01** _Make sure that your IoT device manufacturer provides security-related notifications to you, and provides software updates in a timely manner to reduce the associated risks of operating hardware or software with known security vulnerabilities._ Ask your suppliers about their product conformance to the [Common Criteria for Information Technology Security Evaluation](https://www.commoncriteriaportal.org/index.cfm "https://www.commoncriteriaportal.org/index.cfm"). In addition, use AWS Partner Device Catalog where you can find devices and hardware to help you explore, build, and go to market with your IoT solutions. |
