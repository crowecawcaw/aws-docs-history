# Detection

| CMSEC_9: How do you monitor your in-vehicle software, components, and network<br>for threats? |
| --------------------------------------------------------------------------------------------- |
|                                                                                               |

Monitoring in-vehicle activity from threats, vulnerabilities, and fraud is becoming
increasingly important as vehicles become connected. Standards like [ISO 21434](https://www.iso.org/standard/70918.html "https://www.iso.org/standard/70918.html") and regulations like
[UNR 155](https://unece.org/transport/documents/2021/03/standards/un-regulation-no-155-cyber-security-and-cyber-security "https://unece.org/transport/documents/2021/03/standards/un-regulation-no-155-cyber-security-and-cyber-security") have provisions for monitoring vehicles and systems where detecting,
reporting, refining, and analyzing vehicle related data is a requirement. Monitoring
in-vehicle events that may have security implications requires providing solutions both
on-board and off-board the vehicle. Before data collection, you must understand the sources
of data that you need to collect from. You then develop the people, processes, and
technology to address the data collection, ingestion, enrichment, and analysis of that data.
You can then understand the threat landscape, use threat intelligence to proactively address
risks, and monitor and analyze threats from collected data. The final step, triaging and
incident response will be covered in the "Incident Response" section.

Data collection requires the ability to gather and record data from the vehicle and vehicle environments. Some vehicle data may be stored
locally at smaller volumes and for specific use cases (e.g., crash event data) but is usually sent to an off-board system for refinement and analysis.
The collection of this data may require onboard components depending upon how much processing capability you want to implement onboard before
sending the data off-board.

Ingestion requires sending data to an off-board service.
Oftentimes this is referred to as a VSIEM (Vehicle Security
Information Event Management System) or VSOC (Vehicle Security
Operation Center). This data stream will be sent to other
backend systems for enrichment and refinement.

**[CMSEC\_BP9.1] Collect and detect events using onboard components in
the vehicle.**

You must decide how you will collect data from the vehicle,
and how much processing of security events will be done at the
vehicle edge. It is recommended that you implement software
that can detect vehicle attacks and raise an event to an IDS
manager on the ECU. There may be some filtering by the IDS
manager at this stage depending upon vehicle software and
hardware capability. The events will then be passed to local
event memory for storage, where it can be analyzed by an
authorized user with a diagnostic tool. The majority of the
event data should be sent to the VSOC system from the vehicle
gateway for further refinement of raw logs sent from the
vehicle.

**[CMSEC\_BP9.2] Ingest and enrich data by preparing, moving,
aggregating, normalizing, transforming, and analyzing the vehicle data.**

There are several mechanisms to send your vehicle data to the cloud (see [Design principles](design-principles-sec.md "design-principles-sec.md")). As mentioned in
the [Identity and access management](identity-and-access-management.md "identity-and-access-management.md") section, we recommend using unique vehicle
identities and sending data using secure protocols (see data protection).

You must take a wide a range of actions on your data in order to provide valuable capability
to VSOC analysts. The typical pattern is to ingest, store, process, analyze/train, and then
visualize the data. At the same time, this flow can include response and remediation in
parallel, which is covered in the [Incident response](incident-response.md "incident-response.md") section of the pillar. In order to build out detection
capabilities, you need to:

**Ingest**: You can use [AWS IoT Fleetwise](https://aws.amazon.com/iot-fleetwise/ "https://aws.amazon.com/iot-fleetwise/") to send vehicle telemetry in [VSS
format, a COVESA specification](https://covesa.github.io/vehicle_signal_specification/introduction/overview/ "https://covesa.github.io/vehicle_signal_specification/introduction/overview/") standard for vehicle data that currently supports
CAN and OBD-II, or with any data logger in the vehicle. You may also send raw vehicle data
using protocols like HTTP or MQTT and build proprietary ingestion schemes on top of these
protocols. You also want to use Amazon CloudWatch metrics, which allows you to capture message broker metrics such as
number of connections and other metrics related to AWS IoT Core. [AWS IoT Device Defender](../../../iot/latest/developerguide/device-defender.md "../../../iot/latest/developerguide/device-defender.md") can capture cloud-side
metrics, which are agentless metrics generated from IoT devices. You can also capture
device-side metrics which are metrics generated from agents installed on the ECU.

**Store:** AWS provides the ability to easily securely send
vehicle data to AWS. You can use [AWS IoT Core Rules](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md") that can send
vehicle logs to over [20 different services](../../../iot/latest/developerguide/iot-rule-actions.md "../../../iot/latest/developerguide/iot-rule-actions.md").
Commonly you will use IoT Core Rules to route vehicle data to [Amazon S3,](https://aws.amazon.com/pm/serv-s3/?trk=fecf68c9-3874-4ae2-a7ed-72b6d19c8034&sc_channel=ps&ef_id=CjwKCAjwl6OiBhA2EiwAuUwWZV9VeHMVbNw33crX1g54M7QdP12Xdc1Z9O-QWw5Tym30ddped2s9jhoCvsYQAvD_BwE:G:s&s_kwcid=AL!4422!3!536452728638!e!!g!!amazon%20s3!11204620052!112938567994 "https://aws.amazon.com/pm/serv-s3/?trk=fecf68c9-3874-4ae2-a7ed-72b6d19c8034&sc_channel=ps&ef_id=CjwKCAjwl6OiBhA2EiwAuUwWZV9VeHMVbNw33crX1g54M7QdP12Xdc1Z9O-QWw5Tym30ddped2s9jhoCvsYQAvD_BwE:G:s&s_kwcid=AL!4422!3!536452728638!e!!g!!amazon%20s3!11204620052!112938567994") which is an object storage service that offers industry-leading
scalability, data availability, security, and performance. It is important to define storage
requirements based on your organization and risk determinations. AWS provides [_storage lifecycle_](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") mechanisms in Amazon S3 to define data
lifecycle policies based on your retention and cost requirements. Customers can also use
[Amazon Security Lake](https://aws.amazon.com/security-lake/ "https://aws.amazon.com/security-lake/") to centralize security
logs from AWS and custom sources like the vehicle, charging stations, and more in an
open-source standard format called [OCSF](../../../security-lake/latest/userguide/open-cybersecurity-schema-framework.md "../../../security-lake/latest/userguide/open-cybersecurity-schema-framework.md"). Security Lake enables both the centralization of log data and helps customers extract
valuable insights quicker from normalizing to the open standard.

**Process:** You can then process and normalize that data in
any way that fits your business case. AWS provides a service called [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/") to normalize, prepare, and integrate this
data into a catalog for analysis. This allows customers to build schemas and normalize data
to fit their needs.

**Analyze:** You can then run machine learning and analytics on
this data to understand vehicle related baselines and build models for detection using
services like [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/"). Amazon SageMaker AI allows you
to build, train, and deploy machine learning (ML) models for any use case with fully managed
infrastructure, tools, and workflows.

**Visualize:** VSIEMs and VSOC can be used to identify security
patterns based on the data and analytics that are run on the large data sets. Selecting the
right visualization tool and strategy is an important aspect of identifying security trends
and KPIs. AWS provides a number of services to help with visualizing vehicle security
patterns in a detailed graph and report. [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/") is a cloud-native serverless business intelligence service that provides
data visuals, interactive dashboards, and data analytics powered by ML. [Amazon Managed Grafana](https://aws.amazon.com/grafana/ "https://aws.amazon.com/grafana/") is a fully managed service for
open-source Grafana, a popular open-source analytics service for querying, visualizing, and
understanding your metrics no matter where they are stored. [AWS OpenSearch](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/") with Kibana gives you the ability to
aggregate logs from all your systems and applications, analyze these logs, and create
visualizations for application and infrastructure monitoring, faster troubleshooting,
security analytics, and more.

You can build a pipeline for vehicle data using the AWS services highlighted above. You can
also consider adopting partner services from [Argus Cyber
Security](https://aws.amazon.com/marketplace/seller-profile?id=c18d1099-5095-4d06-aee4-571c7fa75620 "https://aws.amazon.com/marketplace/seller-profile?id=c18d1099-5095-4d06-aee4-571c7fa75620") or [Upstream Security](https://upstream.auto/ "https://upstream.auto/").

| CMSEC_10: How do you correlate events from vehicles, backend systems,<br>suppliers, vendors, and AWS Partners to generate actionable findings? |
| ---------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                |

Organizations must integrate data from many data sources as inputs to VSOCs. It is necessary
to gather information feeds from many relevant data sources that may be relevant when
analyzing vehicle logs and determining vulnerabilities. Correlation requires trained
expertise, proper tooling, and the correct data sources and learning models to provide
accurate true positive results from different vehicle scenarios. Based on the analysis
results, you can use runbooks to guide your response and recovery on the fleet or vehicle,
which is covered in the incident response section of the security pillar.

Analyzing baselines and threat intelligence feeds can provide information that a VSOC analyst can use to build common detection patterns that are
likely to occur. As the threat intelligence data is constantly changing and new threats and vulnerabilities emerge, it is important to provide a
mechanism to continuously monitor for false positives and improve rules based on new data. Organizations should focus on building monitoring
capability around the highest risks to safety and security, the scope of a possible security issue, and the plausibility of the security issue.

**[CMSEC\_BP10.1] Gather relevant supplier, vendor, production, API, and
partner data to enhance detection mechanisms by adding further context.**

A vehicle environment contains several different systems that interact with the vehicle and
consumer. Log sources should be collected from any relevant system that can provide
important security and operational insights related to the connected vehicle. Data collected
from backend systems, companion APIs, charging stations, diagnostics databases, AUTOSAR XML
databases, production data, partners, and other custom databases that are relevant to a
connected mobility system. This data can also be stored in Amazon S3 or Amazon Security Lake in OCSF
format.

The goal is to correlate data and build rules based on the models that are trained on
this data. Lastly, correlating findings requires the ability to utilize threat intelligence
and threat hunting resources to inform your environment and your baselines, and this can be
done by integrating threat intelligence and vulnerability feeds to Amazon SageMaker AI mentioned above.
The data can then be integrated into Amazon OpenSearch Service for analytics and uncovering insights, or to
a central IT SOC on AWS or an AWS Partner such as [Datadog](https://www.datadoghq.com/ "https://www.datadoghq.com/"), [Sumo Logic](https://www.sumologic.com/ "https://www.sumologic.com/"), [New Relic](https://newrelic.com/ "https://newrelic.com/"), [Honeycomb](https://www.honeycomb.io/ "https://www.honeycomb.io/"), or [Splunk](https://www.splunk.com/ "https://www.splunk.com/")**.** Amazon OpenSearch Service makes it possible for you to perform interactive log
analytics, real-time application monitoring, website search, and usage of [Security Analytics
for OpenSearch](../../../opensearch-service/latest/developerguide/security-analytics.md "../../../opensearch-service/latest/developerguide/security-analytics.md") that provides out of the box security visibility. These tools can
provide the ability to detect suspicious vehicle interactions. Commands from a vehicle might
be anomalous, or a vehicle may be communicating to a backend system that it shouldn't or
usually does not communicate to.

It is also important to collect logs from applications that interact with vehicles such
as companion or fleet applications. You can use API logs to determine issues such as an
unauthorized user gaining access to vehicles they are not authorized to interact with. You
can collect logs from sources like [Amazon API Gateway](../../../apigateway/latest/developerguide/view-cloudwatch-log-events-in-cloudwatch-console.md "../../../apigateway/latest/developerguide/view-cloudwatch-log-events-in-cloudwatch-console.md") and AWS IoT Core.

As previously stated, you can build a pipeline to gather relevant data to enhance detection
using the AWS services highlighted above. You can also consider adopting partner services
from [Argus Cyber
Security](https://aws.amazon.com/marketplace/seller-profile?id=c18d1099-5095-4d06-aee4-571c7fa75620 "https://aws.amazon.com/marketplace/seller-profile?id=c18d1099-5095-4d06-aee4-571c7fa75620") or [Upstream Security](https://upstream.auto/ "https://upstream.auto/").

| CMSEC_11: How do you monitor and detect unauthorized use of vehicle credentials<br>and identities? |
| -------------------------------------------------------------------------------------------------- |
|                                                                                                    |

You should be monitoring your ECUs for security best practices continuously. Due to the volume of ECUs and client certificates,
it is important to monitor certificate and CA expiration and revocation. Organizations must monitor ECU permissions to detect overly
permissive actions, and follow best practices when developing authentication and authorization mechanisms. It is also important to
track changes in vehicle patterns that are significantly anomalous and deviating from known expected baselines.

**[CMSEC\_BP11.1] Detect security posture deviations and anomalous
behavior**

Monitoring certificate expiry and revocation can be a challenging process. Organizations must
create processes and policies around the distribution and management of CAs and client
certificates. [AWS IoT Device Defender Audit](../../../iot/latest/developerguide/device-defender-audit-checks.md "../../../iot/latest/developerguide/device-defender-audit-checks.md")
provides the ability to monitor CA and client certificates that are nearing expiration (30
days) or that have been revoked. Organizations must detect overly permissive ECUs and scope
down permissions as needed. AWS IoT Device Defender Audit can help to identify overly permissive policies
that may be granting access to a broad set of resources instead of just a few.

Finally, organizations must build out vehicle baselines and automated alerting on
anomalous behavior. Baselines might include expected number of connections, expected
subscribed topics, expected protocols, expected payloads, and more. If a vehicle is
deviating from those, such as sending suspicious commands, these should be detected. [AWS IoT Device Defender
Detect](../../../iot/latest/developerguide/device-defender-detect.md "../../../iot/latest/developerguide/device-defender-detect.md") can help with the creation of rules or ML baselines to detect anomalous
traffic based on pre-defined or custom metrics specific to your fleets, or even a group of
devices in a profile.

For example, AWS IoT Device Defender Detect can provide you with visibility into ECU behavior such as the
ECU failing authorization to multiple topics which may indicate the ECU trying to gain
access to a topic that it is not authorized to publish or subscribe to. You can then trigger
an [Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") which allows you to watch CloudWatch metrics and to receive
notifications when the metrics fall outside of the levels (high or low thresholds) that you
configure.

Alarms can send [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") notifications, which is
a web service that coordinates and manages the delivery or sending of messages to
subscribing endpoints or clients. Detect and Rule based findings integrate with [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/"), which is a cloud security posture
management service that performs security best practice checks, aggregates alerts, and
enables automated remediation.

| CMSEC_12: How do you stay current and monitor on new threats and<br>vulnerabilities after concept and design phase? |
| ------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                     |

Organizations must continually ingest data from the vehicle and internal systems, as well as
public and private data sources. Vehicles have several potential vulnerabilities that are
unlike traditional IT systems. Defining a threat intelligence process and collecting data
from a wide range of relevant sources will provide information on expected and emerging
threats and vulnerabilities.

While protecting software and firmware from vulnerabilities is important, vehicle
security programs must also consider emerging threats such as sensor fusion risks to the
vehicle. An organization should develop mechanisms to consume a large variety of threat
intelligence as well as share and collaborate across a sharing body such as [Auto-ISAC](https://automotiveisac.com/ "https://automotiveisac.com/") to share learnings in a timely manner.

**[CMSEC\_BP12.1] Subscribe to threat intelligence feeds from many
different sources to detect threats and vulnerabilities**

You should analyze threat intelligence feeds from several data sources both public and private, beyond what is coming off of the vehicle or
what is in your environment. This can include things like governments, vendors, information sharing bodies, peers, suppliers, open-source
intelligence, and more. You may subscribe to specific vulnerability feeds regarding specific software and firmware running on the vehicle to
address emerging threats and further enhance detection baselines to respond when emerging threats and vulnerabilities are known. It is important
to maintain an inventory of embedded software and firmware, as well as operating systems, packages, and libraries that are used per vehicle model
and type so that you are aware of what is relevant to your environment based on threat intelligence feeds.
