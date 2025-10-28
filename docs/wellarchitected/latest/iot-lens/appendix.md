# Appendix: Best practices by pillar

## Operational excellence

**IOTOPS01: How do you evaluate governance and compliance requirements?**

- IOTOPS01-BP01 Conduct an OT and IT cybersecurity risk assessment using a common framework
- IOTOPS01-BP02 Evaluate if OT and IT teams use separate policies and controls to manage cybersecurity risks or if they use the same policy

**IOTOPS02: Is there a central cloud center of excellence (CCoE) with equivalent representation from OT and IT in industrial organizations?**

- IOTOPS02-BP01 Consolidate resources into centers of excellence to bring focus to new or transforming enterprises

**IOTOPS03: Do you organize the fleet to quickly identify devices?**

- IOTOPS03-BP01 Use static and dynamic device hierarchies to support fleet operations
- IOTOPS03-BP02 Use index and search services to enable rapid identification of target devices

**IOTOPS04: How do you verify that newly provisioned devices have the required operational prerequisites?**

- IOTOPS04-BP01 The device management processes should be automated, data-driven, and based on previous, current, and expected device behavior

**IOTOPS05: How do you govern device fleet provisioning process?**

- IOTOPS05-BP01 Document how devices join your fleet from manufacturing to provisioning
- IOTOPS05-BP02 Use programmatic techniques to provision devices at scale
- IOTOPS05-BP03 Use device level features to enable re-provisioning

**IOTOPS06: How do you implement observability for your IoT system?**

- IOTOPS06-BP01 Implement monitoring to capture logs and metrics
- IOTOPS06-BP02 Capture and monitor application performance at the edge
- IOTOPS06-BP03 Monitor the status of your IoT devices
- IOTOPS06-BP04 Use device state management services to detect status and connectivity patterns

**IOTOPS07: How do you assess whether your IoT application meets your operational goals?**

- IOTOPS07-BP01 Enable appropriate responses to events
- IOTOPS07-BP02 Use data-driven auditing metrics to detect if any of your IoT devices might have been broadly accessed

**IOTOPS08: How do you segment your device operations in your IoT application?**

- IOTOPS08-BP01 Use static and dynamic device attributes to identify devices with anomalous behavior

**IOTOPS09: How do you evolve your IoT application with minimum impact to downstream IoT devices?**

- IOTOPS09-BP01 Run ops metrics analysis across business teams, document learnings and define action items for future firmware deployments

**IOTOPS10: How do you verify that you are ready to support the operations of devices in your IoT workload?**

- IOTOPS10-BP01 Train team members supporting your IoT workloads on the lifecycle of IoT applications and your business objectives

## Security

**IOTSEC01: How do you associate IoT identities and permissions with your devices?**

- IOTSEC01-BP01 Assign unique identities to each IoT device

**IOTSEC02: How do you secure your devices and protect device credentials?**

- IOTSEC02-BP01 Use a separate hardware or a secure area on your devices to store credentials
- IOTSEC02-BP02 Use a trusted platform module (TPM) to implement cryptographic controls
- IOTSEC02-BP03 Use protected boot and persistent storage encryption

**IOTSEC03: How do you authenticate and authorize user access to your IoT application?**

- IOTSEC03-BP01 Implement authentication and authorization for users accessing IoT resources
- IOTSEC03-BP02 Decouple access to your IoT infrastructure from the IoT applications

**IOTSEC04: How do you apply least privilege to principals that interact with your IoT application?**

- IOTSEC04-BP01 Assign least privilege access to devices

**IOTSEC05: How do you manage device certificates, including installation, validation, revocation, and rotation?**

- IOTSEC05-BP01 Perform certificate lifecycle management

**IOTSEC06: How do you analyze application and device logs and metrics to detect security issues?**

- IOTSEC06-BP01 Collect and analyze logs and metrics to capture authorization errors and failures to enable appropriate response
- IOTSEC06-BP02 Send alerts when security events, misconfiguration, and behavior violations are detected
- IOTSEC06-BP03 Alert on non-compliant device configurations and remediate using automation

**IOTSEC07: What infrastructure protection configuration has been defined for your AWS organization and accounts?**

- IOTSEC07-BP01 Configure cloud infrastructure to have secure communications
- IOTSEC07-BP02 Define networking configuration which restricts communications to only those ports and protocols which are required
- IOTSEC07-BP03 Log and monitor network configuration changes and network communication

**IOTSEC08: How is the infrastructure into which your IoT devices are deployed managed and maintained?**

- IOTSEC08-BP01 Define an automated and monitored mechanism for deploying, managing, and maintaining networks to which IoT devices are connected
- IOTSEC08-BP02 Define an automated and monitored mechanism for deploying, managing, and maintaining network configurations for IoT devices

**IOTSEC09: What processes are used to manage and maintain the hardware or software deployed and configured in your IoT devices?**

- IOTSEC09-BP01 Manage and maintain IoT Device software using an automated, monitored, and audited mechanism
- IOTSEC09-BP02 Manage IoT device configuration using automated and controlled mechanisms

**IOTSEC10: How do you make sure that device data is protected at rest and in transit?**

- IOTSEC10-BP01 Use encryption to protect IoT data in transit and at rest
- IOTSEC10-BP02 Use data classification strategies to categorize data access based on levels of sensitivity
- IOTSEC10-BP03 Protect your IoT data in compliance with regulatory requirements

**IOTSEC11: How do you plan the security lifecycle of your IoT devices?**

- IOTSEC11-BP01 Build incident response mechanisms to address security events at scale
- IOTSEC11-BP02 Require timely vulnerability notifications and software updates from your providers

**IOTSEC12: How do you develop, maintain, manage, and deploy application code to your IoT devices and gateways?**

- IOTSEC12-BP01 Manage IoT device and gateway source code using source code management tools
- IOTSEC12-BP02 Use static code analysis tools and code scanning to check IoT application code
- IOTSEC12-BP03 Deploy IoT applications using IaC, CI/CD pipelines, and build and deploy automation

**IOTSEC13: How do you identify and remediate risks in IoT device firmware, IoT application code, and depended-upon packages or libraries?**

- IOTSEC13-BP01 Use code and package scanning tools during development to identify potential risks during development
- IOTSEC13-BP02 Deploy updates to IoT device firmware or software to address identified issues
- IOTSEC13-BP03 Identify IoT devices which require updates and schedule updates to those devices

**IOTSEC14: How do you govern the security of your IoT applications?**

- IOTSEC14-BP01 Establish a security governance team for your IoT applications or extend the security governance team for the organization
- IOTSEC14-BP02 Define security policy so that it can be written into verifiable checks using policy as code techniques
- IOTSEC14-BP03 Implement a risk assessment and risk management process

**IOTSEC15: What regulations apply to your IoT applications and how do you show compliance with these regulations?**

- IOTSEC15-BP01 Identify the set of relevant regulations for your IoT applications
- IOTSEC15-BP02 Set up logging and monitoring to support audit checks for compliance
- IOTSEC15-BP03 Implement automated compliance checking using compliance as code

## Reliability

**IOTREL01: How do you make sure that your device consistently keeps its internal clock accurate?**

- IOTREL01-BP01 Use NTP to maintain time synchronization on devices
- IOTREL01-BP02 Provide devices access to NTP servers

**IOTREL02: How do you manage service quotas and limits for peaks in your IoT workload?**

- IOTREL02-BP01 Manage service quotas and constraints

**IOTREL03: How do you design workloads to operate efficiently within network bandwidth and storage constraints?**

- IOTREL03-BP01 Down sample data to reduce storage requirements and network utilization

**IOTREL04: How do you optimize and control message delivery frequency to IoT devices?**

- IOTREL04-BP01 Target messages to relevant devices
- IOTREL04-BP02 Implement retry and back off logic to support throttling by device type

**IOTREL05: How do you manage data ingestion and processing throughput for IoT workloads to other applications?**

- IOTREL05-BP01 Decouple IoT applications from the Connectivity Layer through an Ingestion Layer

**IOTREL06: How do you facilitate reliable processing and delivery of IoT messages across your workload?**

- IOTREL06-BP01 Dynamically scale cloud resources based on the utilization

**IOTREL07: How do you provision storage strategies for IoT data in the cloud?**

- IOTREL07-BP01 Store data before processing
- IOTREL07-BP02 Implement storage redundancy and failover mechanisms for IoT data perpersistence

**IOTREL08: How do you update device firmware on your IoT device?**

- IOTREL08-BP01 Use a mechanism to deploy and monitor firmware updates
- IOTREL08-BP02 Configure firmware rollback capabilities in devices
- IOTREL08-BP03 Implement support for incremental updates to target device groups
- IOTREL08-BP04 Implement dynamic configuration management for devices

**IOTREL09: How do you perform functional testing for your IoT solution?**

- IOTREL09-BP01 Implement device simulation to synthesize the entire flow of IoT data

**IOTREL10: How do you implement your IoT workload to withstand component and system faults?**

- IOTREL10-BP01 Use cloud service capabilities to handle component failures

**IOTREL11: How do you verify that your IoT device operates with intermittent connectivity to the cloud?**

- IOTREL11-BP01 Implement device logic to automatically reconnect to the cloud
- IOTREL11-BP02 Design devices to use multiple methods of communication
- IOTREL11-BP03 Automate alerting for devices that are unable to reconnect

**IOTREL12: How do you verify that required data is transmitted to the cloud after a device has been disconnected?**

- IOTREL12-BP01 Provide adequate device storage for offline operations
- IOTREL12-BP02 Synchronize device states upon connection to the cloud

**IOTREL13: How do you remotely adjust message frequency to your IoT devices?**

- IOTREL13-BP01 Configure cloud services to reliably handle message processing
- IOTREL13-BP02 Send logs directly to the cloud
- IOTREL13-BP03 Design devices to allow for remote configuration of message publication frequency

**IOTREL14: How do you plan for disaster recovery in your IoT workloads?**

- IOTREL14-BP01 Design server software to initiate communication only with devices that are online
- IOTREL14-BP02 Implement multi-Region support for IoT applications and devices
- IOTREL14-BP03 Use edge devices to store and analyze data

## Performance efficiency

**IOTPERF01: How do your architectural decisions adapt to device hardware resources?**

- IOTPERF01-BP01 Optimize for device hardware resources utilization

**IOTPERF02: How do you measure and maintain the performance of your IoT solution?**

- IOTPERF02-BP01 Implement comprehensive monitoring solutions to collect performance data from your IoT devices
- IOTPERF02-BP02 Evaluate the runtime performance of your application

**IOTPERF03: Does transmitted content include auditable metadata?**

- IOTPERF03-BP01 Add timestamps to each published message

**IOTPERF04: Is there a mechanism for payload filtering or stream prioritization?**

- IOTPERF04-BP01 Have mechanisms to prioritize specific payload types

**IOTPERF05: How do you optimize telemetry data ingestion?**

- IOTPERF05-BP01 Identify the ingestion mechanisms that best fit your use case
- IOTPERF05-BP02 Optimize data sent from devices to backend services

**IOTPERF06: How do you efficiently make sure stored data is usable by business?**

- IOTPERF06-BP01 Store data in different tiers following formats, access patterns and methods

**IOTPERF07: How do you provide optimal connectivity for edge devices communicating to cloud infrastructure?**

- IOTPERF07-BP01 Optimize network topology for distributed devices
- IOTPERF07-BP02 Perform timely connectivity verification for devices

**IOTPERF08: How do you make sure application operates within its scaling limits?**

- IOTPERF08-BP01 Load test your IoT applications
- IOTPERF08-BP02 Monitor and manage your IoT service quotas using available tools and metrics

**IOTPOTPERF09: How do you maintain visibility over the distributed infrastructure deployed?**

- IOTPERF09-BP01 Have device inventory in the IoT system that centralizes device configuration and diagnostics

## Cost optimization

**IOTCOST01: How do you choose cost-efficient tools for data aggregation of your IoT workloads?**

- IOTCOST01-BP01 Use a data lake for raw telemetry data
- IOTCOST01-BP02 Provide a self-service interface for end users to search, extract, manage, and update IoT data
- IOTCOST01-BP03 Track and manage the utilization of data sources
- IOTCOST01-BP04 Aggregate data at the edge where possible

**IOTCOST02: How do you optimize cost of raw telemetry data?**

- IOTCOST02-BP01 Use lifecycle policies to archive your data
- IOTCOST02-BP02 Evaluate storage characteristics for your use case and align with the right services
- IOTCOST02-BP03 Store raw archival data on cost effective services

**IOTCOST03: How do you optimize cost of interactions between devices and your IoT cloud solution?**

- IOTCOST03-BP01 Select services to optimize cost
- IOTCOST03-BP02 Implement and configure telemetry to reduce data transfer costs
- IOTCOST03-BP03 Use shadow only for slow changing data
- IOTCOST03-BP04 Group and tag IoT devices and messages for cost allocation
- IOTCOST03-BP05 Implement and configure device messaging to reduce data transfer costs

**IOTCOST04: How do you optimize cost by matching the supply of resources with device demand?**

- IOTCOST04-BP01 Plan expected usage over time

**IOTCOST05: How do you optimize payload size between devices and your IoT system to save cost?**

- IOTCOST05-BP01 Balance networking throughput against payload size to optimize efficiency

**IOTCOST06: How do you optimize the costs of storing the current state of your IoT device?**

- IOTCOST06-BP01 Optimize shadow operations

## Sustainability

**IOTSUS01: How do you optimize software and firmware to reduce device's carbon footprint?**

- IOTSUS01-BP01 Eliminate unnecessary modules, libraries, and processes
- IOTSUS01-BP02 Use AWS IoT features to optimize network usage and power consumption
- IOTSUS01-BP03 Use a hardware watchdog to restart your device automatically
- IOTSUS01-BP04 Implement resilient and scalable system behavior for clients communicating with the cloud

**IOTSUS02: How do you incorporate optimized cloud services in your architecture to minimize your carbon footprint?**

- IOTSUS02-BP01 Use the Basic Ingest feature in AWS IoT Core
- IOTSUS02-BP02 Choose an appropriate Quality of Service(QoS) level

**IOTSUS03: How do you pick the right hardware components?**

- IOTSUS03-BP01 Source sustainable components to help reduce environmental harm and encourage eco-friendly IoT products
- IOTSUS03-BP02 Consider the manufacturing and distribution footprint of your device
- IOTSUS03-BP03 Use benchmarks to help you make a processor choice
- IOTSUS03-BP04 Optimize your device based on real-world testing
- IOTSUS03-BP05 Use sensors with built-in event detection capabilities
- IOTSUS03-BP06 Use hardware acceleration for video encoding and decoding
- IOTSUS03-BP07 Use HSMs to accelerate cryptographic operations and save power
- IOTSUS03-BP08 Use low-power location tracking

**IOTSUS04: How do you minimize power usage and wastage?**

- IOTSUS04-BP01 Use energy harvesting technologies to power your device
- IOTSUS04-BP02 Implement tickless operation and low-power modes
- IOTSUS04-BP03 Allow applications or software running on devices to dynamically adjust settings based on requirements and available resources

**IOTSUS05: How do you educate users to encourage lower carbon footprint of their devices?**

- IOTSUS05-BP01 Create detailed documentation
- IOTSUS05-BP02 Promote responsible disposal, repairability, and transfer of ownership for IoT devices to minimize environmental impact
- IOTSUS05-BP03 Identify when devices in the field can or should be retired
