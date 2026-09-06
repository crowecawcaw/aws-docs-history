

# Document history for user guide
<a name="doc-history"></a>

The following table describes the documentation for this release of AWS Elemental MediaConnect. For notification about updates to this documentation, you can subscribe to an RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Recovery latency mode](using-mediaconnect-router.md) | You can now choose a recovery latency mode for the router fabric on each router output.  | August 10, 2026 | 
| [Router input content quality EventBridge event](monitoring-eventbridge-events-router-input-content-quality.md) | You can now subscribe to EventBridge events for content quality changes on router inputs. | June 29, 2026 | 
| [Content quality analysis for router inputs](monitor-content-quality-analysis.md) | You can now use MediaConnect content quality analysis to monitor your router inputs more effectively. | June 29, 2026 | 
| [Limits for API requests](quotas.md#limits-api) | Updated the high-frequency API list to include router-related APIs | May 1, 2026 | 
| [Added router resources to supported tagging list](tagging.md) | Added router inputs, router outputs, and router network interfaces to the list of resources that support tagging. | May 1, 2026 | 
| [NDI® output timecode source](outputs-using-ndi.md) | You can now control how MediaConnect generates timecodes for NDI output frames. Choose between preserving embedded timecodes from the source transport stream or using the UTC system time. | April 22, 2026 | 
| [NDI® sources](sources-using-ndi.md) | You can now receive video and audio from NDI® senders in your network and convert this content into transport streams for broader distribution. | January 26, 2026 | 
| [Updated AWS managed policy](security-iam-awsmanpol.md) | AWS Elemental MediaConnect has updated the [AWSMediaConnectServicePolicy](https://docs.aws.amazon.com/mediaconnect/latest/ug/security-iam-awsmanpol.html#security-iam-awsmanpol-AWSMediaConnectServicePolicy). | November 19, 2025 | 
| [MediaConnect router](using-mediaconnect-router.md) | A new feature has been released called MediaConnect router. MediaConnect router enables you to manage video and audio routing both within the AWS Cloud and over the public internet.  | November 17, 2025 | 
| [Unified maintenance chapter](maintenance.md) | Expanded the maintenance chapter to cover both flows and router I/Os in a single location. | June 25, 2025 | 
| [Source peer IP address](source-ip-address.md) | You can now view the current and historical peer IP addresses for your flow sources. | April 21, 2025 | 
| [Output peer IP address](output-ip-address.md) | You can now view the current and historical peer IP addresses for your flow outputs. | April 21, 2025 | 
| [NDI® outputs](outputs-using-ndi.md) | You can now use NDI® outputs to send content from your MediaConnect flow to your NDI environment. | March 24, 2025 | 
| [AWS managed policy - New policy](security-iam-awsmanpol.md) | The AWSElementalMediaConnectReadOnlyAccess policy has been created. | February 12, 2025 | 
| [AWS managed policy - New policy](security-iam-awsmanpol.md) | The AWSElementalMediaConnectFullAccess policy has been created. | February 12, 2025 | 
| [Content quality EventBridge events](monitoring-eventbridge-events-content-quality.md) | A new content quality monitoring EventBridge event has been added to MediaConnect. | January 27, 2025 | 
| [Content quality analysis](monitor-content-quality-analysis.md) | You can now use MediaConnect content quality analysis to monitor your source streams more effectively.  | January 3, 2025 | 
| [AWS Elemental MediaConnect Gateway](gateway.md) | MediaConnect Gateway now supports Source Specific Multicast (SSM) for ingress bridges. This enables you to specify a source IP address in addition to the multicast IP when creating or updating an ingress bridge source. | December 13, 2024 | 
| [Output disabling](outputs-remove.md) | You can now disable a flow's outputs. A disabled output will stop streaming content and will not incur data transfer costs. | July 12, 2024 | 
| [Source stream monitoring: Additional fields](monitor-with-source-stream-monitoring.md) | Additional information about MediaConnect flow source streams can be viewed using source metadata monitoring in the MediaConnect console and API. Source metadata monitoring displays media information about the transport stream and its programs. | June 18, 2024 | 
| [Workflow monitor](monitor-with-workflow-monitor.md) | Analyze AWS media services and create signal maps, visualizations of the media workflow, between those services. Use the signal maps to generate monitoring alarms and notifications using CloudWatch, EventBridge, and CloudFormation. | April 11, 2024 | 
| [Updated MediaConnect Gateway operating system recommendation](gateway-prerequisites.md#system-requirements-os) | The recommended OS for MediaConnect Gateway has been updated from RHEL 8 to Ubuntu 20.04. | March 11, 2024 | 
| [Source stream monitoring: Console](monitor-with-source-stream-monitoring.md) | Detailed information about MediaConnect flow source streams can be viewed using source metadata monitoring in the MediaConnect console. Source metadata monitoring displays media information about the transport stream and its programs. | March 8, 2024 | 
| [Source stream monitoring: API](monitor-with-source-stream-monitoring.md) | Detailed information about MediaConnect flow source streams can be viewed using the source metadata monitoring API. Source metadata monitoring displays media information about the transport stream and its programs. | December 22, 2023 | 
| [VSF TR-07 support](reference-media-standards.md) | The supported media standards reference section has been updated to reflect MediaConnect's implementation of the Video Services Forum's TR-07 (Transport of JPEG XS Video in MPEG-2 Transport Stream over IP). | December 8, 2023 | 
| [Limits for API requests](quotas.md#limits-api) | Added limits for API requests per second | November 2, 2023 | 
| [AWS Elemental Link UHD devices with MediaConnect](flows-create-standard-source.md#flows-create-standard-source-console) | You can now use AWS Elemental Link UHD devices and the Zixi push protocol as a source for MediaConnect flows. | September 11, 2023 | 
| [MediaConnect high resolution metrics](monitor-with-cloudwatch.md) | MediaConnect metrics can now be viewed in intervals as short as one second. | June 22, 2023 | 
| [Supported media standards reference](reference-media-standards.md) | This guide has been updated to include a reference list of media industry standards that are supported by MediaConnect. | June 9, 2023 | 
| [SRT failover](source-failover.md) | You can now enable source failover and add a second source to flows with SRT (listener or caller) sources. | May 1, 2023 | 
| [Failover support table](source-failover.md#source-failover-table) | A new table has been added that defines which source protocols can support failover. | May 1, 2023 | 
| [MediaConnect Gateway metrics](monitor-with-cloudwatch-metrics-gateway-health.md) | The user guide has been updated to include new CloudWatch metrics for the MediaConnect Gateway feature. | April 13, 2023 | 
| [AWS Elemental MediaConnect Gateway](gateway.md) | A new feature has been released called MediaConnect Gateway. MediaConnect Gateway in an on-premises implementation of MediaConnect. | April 13, 2023 | 
| [AWS service-linked role - New role](using-service-linked-roles.md) | The AWSServiceRoleForMediaConnect role has been created.  | April 13, 2023 | 
| [AWS managed policy - New policy](security-iam-awsmanpol.md) | The MediaConnectGatewayInstanceRolePolicy has been created. | April 13, 2023 | 
| [AWS managed policy - New policy](security-iam-awsmanpol.md) | The AWSMediaConnectServicePolicy has been created. | April 13, 2023 | 
| [Updated the IAM guidance for MediaConnect](security-iam.md) | Updated guide to align with the IAM best practices. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). | February 14, 2023 | 
| [Health EventBridge events](monitoring-with-cloudwatch-events.md) | New flow, source, and output health monitoring EventBridge events have been added to MediaConnect.  | February 8, 2023 | 
| [Color support for CDI protocols](protocol-color.md) | A new table has been added that defines color space, bit depth, and chroma sampling support for CDI protocols. | November 4, 2022 | 
| [MediaConnect Alerts: stream errors](monitor-flow-health.md#monitor-flow-health-stream-alerts) | The user guide has been updated to include information about stream error Alerts. | October 27, 2022 | 
| [SRT caller sources and outputs](protocols.md) | You can now use the SRT caller protocol for sources and outputs.  | September 19, 2022 | 
| [Source and output protocol table](protocols.md#protocol-table) | A new table has been added that defines which protocols can be used for sources, outputs, or both. | August 5, 2022 | 
| [Maintenance EventBridge event](monitoring-cloudwatch-events-flow-maintenance.md) | The user guide has been updated to include a new EventBridge event for MediaConnect maintenance. | August 1, 2022 | 
| [Maintenance CloudWatch metrics](monitor-with-cloudwatch-metrics-flow-health.md#monitor-with-cloudwatch-metrics-flow-health-maintenance) | The user guide has been updated to include new CloudWatch metrics for MediaConnect maintenance. | August 1, 2022 | 
| [SRT password encryption](encryption-srt-password.md) | Documentation for SRT password encryption has been added to the guide. | May 31, 2022 | 
| [Source failover](source-failover.md) | When you enable source failover, you can now specify one of two sources as the primary source. You can choose between two failover modes to prevent any disruption to the video stream. | June 11, 2021 | 
| [CDI workflows](use-cases-cdi.md) | MediaConnect now supports JPEG XS for AWS Cloud Digital Interface (AWS CDI) uncompressed workflows.  | May 17, 2021 | 
| [Listener address](output-ip-address.md) | For flows that use listener protocols, you can now easily locate an output's outbound IP address for a private internet. | April 14, 2021 | 
| [SRT-listener sources and outputs](protocols.md) | You can now use the SRT-listener protocol for sources and outputs.  | March 16, 2021 | 
| [Reservations](reservations.md) | You can now purchase reservations, which provide a disconted hourly rate in exchange for a commitment to use a specific amount of outbound bandwidth each month over the course of a specified duration. | September 30, 2020 | 
| [Disabling entitlements](entitlements-disable.md) | You can now disable an entitlement to temporarily stop streaming content to the subscriber’s flow. When you're ready to reinstate access, you can enable the entitlement. | July 24, 2020 | 
| [Source health metrics](monitor-source-health.md) | In the MediaConnect console, you can view Amazon CloudWatch metrics that show the health of the source over a period of time.  | May 11, 2020 | 
| [VPC outputs](outputs-add-vpc.md) | You can now add an output to send content from your AWS Elemental MediaConnect flow to your VPC without going over the public internet. | April 7, 2020 | 
| [VPC sources](vpc-interfaces.md) | You can now connect your VPC to your AWS Elemental MediaConnect flow and send content to your flow without going over the public internet. | March 31, 2020 | 
| [Source failover](source-failover.md) | You can now enable source failover and add a second (redundant) source to your flow. | March 13, 2020 | 
| [Service quotas (outputs)](quotas.md) | You can now add up to 50 outputs to each transport stream flow. | February 7, 2020 | 
| [Sharing the entitlement data transfer fee with the subscriber](entitlements-grant.md) | When you grant an entitlement, you can now specify the percentage of the entitlement data transfer fee that you want the subscriber to be responsible for. | September 16, 2019 | 
| [RIST sources and outputs](protocols.md) | You can now use the RIST protocol for sources and outputs. | September 11, 2019 | 
| [Zixi pull outputs](outputs-add.md) | You can now add outputs that use the Zixi pull protocol. | July 26, 2019 | 
| [SPEKE support](encryption-speke-set-up.md) | You can now encrypt the contents of your entitlements using (SPEKE). | June 25, 2019 | 
| [Service quotas (flows)](quotas.md) | You can now request an increase to the quota of 20 flows per AWS Region. | March 14, 2019 | 
| [New service and guide](what-is.md) | This is the initial release of the media ingest and transport service, AWS Elemental MediaConnect, and the *AWS Elemental MediaConnect User Guide*. | November 27, 2018 | 

**Note**  
The AWS Media Services are not designed or intended for use with applications or in situations requiring fail‐safe performance, such as life safety operations, navigation or communication systems, air traffic control, or life support machines in which the unavailability, interruption or failure of the services could lead to death, personal injury, property damage or environmental damage.