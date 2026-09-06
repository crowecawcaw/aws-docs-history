

# Document History for the AWS Ground Station User Guide
<a name="doc-history"></a>

 The following table describes the important changes in each release of the AWS Ground Station User Guide. 

| Change | Description | Date | 
| --- |--- |--- |
| [New Feature](#doc-history) | Added documentation for Alpha-5 TLE satellite number support. AWS Ground Station now accepts TLE ephemerides with Alpha-5 encoded satellite numbers for satellite catalog numbers in the range 100,000–339,999. For more information, see [Provide TLE ephemeris data](https://docs.aws.amazon.com/ground-station/latest/ug/providing-tle-ephemeris-data.html). | May 28, 2026 | 
| [New Feature](#doc-history) | Added documentation for AWS Ground Station Dedicated Antennas. For more information, see [AWS Ground Station Dedicated Antennas](https://docs.aws.amazon.com/ground-station/latest/ug/dedicated-antennas.html). | April 14, 2026 | 
| [New Feature](#doc-history) | Added documentation for the UpdateContact API and contact versioning. For more information, see [Update contacts and contact versioning](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.versioning.html). | April 14, 2026 | 
| [New Feature](#doc-history) | Added documentation for the ListAntennas and ListGroundStationReservations APIs. For more information, see [AWS Ground Station Locations](https://docs.aws.amazon.com/ground-station/latest/ug/aws-ground-station-antenna-locations.html) and [View ground station reservations](https://docs.aws.amazon.com/ground-station/latest/ug/locations.reservations.html). | April 14, 2026 | 
| [Documentation Update](#doc-history) | Added additional functionality to the CancelContact API, and includes information on said functionality and metering implications. For more information see [Understand contact metering](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.metering.html). | December 10, 2025 | 
| [Documentation Update](#doc-history) | Clarified that CloudWatch metrics are emitted in the region associated with the contact's ground station. Fixed broken links. | December 2, 2025 | 
| [Updated AWS managed policy](#doc-history) |  AWS Ground Station has updated the managed policy `AWSGroundStationAgentInstancePolicy` to include additional permissions for retrieving task response URLs. For information, see [AWS Ground Station updates to AWS managed policies](https://docs.aws.amazon.com/ground-station/latest/ug/security-iam-awsmanpol.html#security-iam-awsmanpol-updates).  | November 13, 2025 | 
| [New Feature](#doc-history) |  Updated the user guide to include azimuth elevation ephemerides. For more information, see [Provide azimuth elevation ephemeris data](https://docs.aws.amazon.com/ground-station/latest/ug/providing-azimuth-elevation-ephemeris-data.html)  | October 22, 2025 | 
| [Documentation Update](#doc-history) | Cross-region data delivery no longer requires special configuration or approvals. For more information, see [Use cross-region data delivery](https://docs.aws.amazon.com/ground-station/latest/ug/dataflows.cross-region-data-delivery.html).  | September 11, 2025 | 
| [Documentation Update](#doc-history) | Added clarification on contact utilization of configured resources. | April 4, 2025 | 
| [New Feature](#doc-history) | Updated the user guide to include AWS Ground Station digital twin. | August 6, 2024 | 
| [Documentation Update](#doc-history) | Updated many sections of the user guide, including new diagrams, examples, and more. | July 18, 2024 | 
| [Documentation Update](https://docs.aws.amazon.com/ground-station/latest/ug/ground-station.rss) | Added RSS feed to User Guide. | July 18, 2024 | 
| [Documentation Update](https://docs.aws.amazon.com/ground-station/latest/gs-agent-ug) | Split AWS Ground Station Agent User Guide into a separate User Guide. | July 18, 2024 | 
| [New Feature](#doc-history) | Contacts can now be scheduled up to 30 seconds outside visibility time ranges. Visibility times are included in DescribeContact responses. | March 26, 2024 | 
| [Documentation Update](#doc-history) | Improved organization and added "EC2 Instance Selection and CPU Planning" section. | March 6, 2024 | 
| [Documentation Update](#doc-history) | Added new best practice to AWS Ground Station Agent User Guide for running services and processes alongside the AWS Ground Station Agent. | February 23, 2024 | 
| [Documentation Update](#doc-history) | Added Agent Release Notes page. | February 21, 2024 | 
| [Template Update](#doc-history) | Added support for separate public subnet in the DirectBroadcastSatelliteWbDigIfEc2DataDelivery template. | February 14, 2024 | 
| [Documentation Update](#doc-history) | Added referral to AWS User Notifications in monitoring documentation. | August 6, 2023 | 
| [Documentation Update](#doc-history) | Added instructions for tagging satellites with a name to be shown in the AWS Ground Station console. | July 26, 2023 | 
| [New Feature](#doc-history) | Added the AWS Ground Station Agent User Guide for the release of Wideband DigIF Data Delivery. | April 12, 2023 | 
| [New AWS managed policy](https://docs.aws.amazon.com/ground-station/latest/ug/security-iam-awsmanpol.html) | AWS Ground Station added a new policy named AWSGroundStationAgentInstancePolicy. | April 12, 2023 | 
| [New Feature](#doc-history) | Updated the user guide for release of CPE Preview. | November 9, 2022 | 
| [New AWS managed policy](https://docs.aws.amazon.com/ground-station/latest/ug/security-iam-awsmanpol.html) | AWS Ground Station added the AWSServiceRoleForGroundStationDataflowEndpointGroup service-linked-role (SLR) that includes a new policy named AWSServiceRoleForGroundStationDataflowEndpointGroupPolicy.  | November 2, 2022 | 
| [New Feature](#doc-history) | Updated the user guide to include integration with AWS CLI. | April 17, 2020 | 
| [New Feature](#doc-history) | Updated the user guide to include integration with CloudWatch Metrics. | February 24, 2020 | 
| [New Template](#doc-history) | Public Broadcast Satellites (AquaSnppJpss Template) added to the * AWS Ground Station User Guide*.  | February 19, 2020 | 
| [New Feature](#doc-history) | Updated the user guide to include cross-region data delivery. | February 5, 2020 | 
| [Documentation Update](#doc-history) | Updated examples and descriptions for monitoring AWS Ground Station with CloudWatch Events. | February 4, 2020 | 
| [Documentation Update](#doc-history) | Template locations have been updated and the Getting Started and Troubleshooting sections have been revised.  | December 19, 2019 | 
| [New Troubleshooting Section](#doc-history) | Troubleshooting section added to the *AWS Ground Station User Guide*.  | November 7, 2019 | 
| [New Getting Started Topic](#doc-history) | Updated the Getting Started topic, which includes the most current CloudFormation templates. | July 1, 2019 | 
| [Kindle Version](#doc-history) | Published Kindle version of the *AWS Ground Station User Guide*.  | June 20, 2019 | 
| [New service and guide](#doc-history) | This is the initial release of AWS Ground Station and the *AWS Ground Station User Guide*.  | May 23, 2019 | 