# AWS IoT FleetWise endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability](../../../iot-fleetwise/latest/developerguide/fleetwise-regions.md "../../../iot-fleetwise/latest/developerguide/fleetwise-regions.md") in the _AWS IoT FleetWise Developer Guide_.

## Service endpoints

| Region Name           | Region       | Endpoint                                                                     | Protocol       |
| --------------------- | ------------ | ---------------------------------------------------------------------------- | -------------- |
| US East (N. Virginia) | us-east-1    | iotfleetwise.us-east-1.amazonaws.com<br>iotfleetwise.us-east-1.api.aws       | HTTPS<br>HTTPS |
| Asia Pacific (Mumbai) | ap-south-1   | iotfleetwise.ap-south-1.amazonaws.com<br>iotfleetwise.ap-south-1.api.aws     | HTTPS<br>HTTPS |
| Europe (Frankfurt)    | eu-central-1 | iotfleetwise.eu-central-1.amazonaws.com<br>iotfleetwise.eu-central-1.api.aws | HTTPS<br>HTTPS |

## Service quotas

| Name                                                                                | Default                              | Adjustable                                                                                                                                                                                   | Description                                                                                               |
| ----------------------------------------------------------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Maximum size of a message                                                           | Each supported Region: 128 Kilobytes | No                                                                                                                                                                                           | The maximum message size that AWS IoT FleetWise can ingest or send to the vehicle.                        |
| Number of campaigns for each account in an AWS Region                               | Each supported Region: 20            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-17D821A8 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-17D821A8") | The maximum number of campaigns for each account in an AWS Region.                                        |
| Number of data dimensions for a state template in an AWS Region.                    | Each supported Region: 5             | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-6BE0F5F7 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-6BE0F5F7") | The maximum number of data dimensions for a state template in an AWS Region.                              |
| Number of decoder manifests for a model manifest for each account in an AWS Region. | Each supported Region: 100           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-9EE083E6 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-9EE083E6") | The maximum number of decoder manifests for a model manifest for each account in an AWS Region.           |
| Number of metadata dimensions for a state template in an AWS Region.                | Each supported Region: 5             | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-0FDD56E9 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-0FDD56E9") | The maximum number of metadata dimensions for a state template in an AWS Region.                          |
| Number of model manifests for each account in an AWS Region.                        | Each supported Region: 150           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-72103FA9 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-72103FA9") | The maximum number of model manifests for each account in an AWS Region.                                  |
| Number of nodes in a signal catalog for each account in an AWS Region               | Each supported Region: 5,000         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-FE285ED4 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-FE285ED4") | The maximum number of nodes in a signal catalog for each account in an AWS Region.                        |
| Number of partitions in a campaign configured to store and forward.                 | Each supported Region: 5             | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-A0A396E0 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-A0A396E0") | The maximum number of partitions that ingest data for each campaign configured to store and forward.      |
| Number of signal catalogs for each account in an AWS Region.                        | Each supported Region: 1             | No                                                                                                                                                                                           | The maximum number of signal catalogs for each account in an AWS Region.                                  |
| Number of signals for a state template in an AWS Region.                            | Each supported Region: 500           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-300E5FB4 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-300E5FB4") | The maximum number of signals in a state template in an AWS Region.                                       |
| Number of signals in a campaign for each account in an AWS Region.                  | Each supported Region: 500           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-86E70888 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-86E70888") | The maximum number of signals in a campaign for each account in an AWS Region.                            |
| Number of state templates for each account in an AWS Region.                        | Each supported Region: 20            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-9EDEDFF3 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-9EDEDFF3") | The maximum number of state templates for each account in an AWS Region.                                  |
| Number of state templates for each vehicle in an AWS Region.                        | Each supported Region: 20            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-03C735B1 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-03C735B1") | The maximum number of state templates for each vehicle in an AWS Region.                                  |
| Number of vehicles in a fleet for each account in an AWS Region.                    | Each supported Region: 2,000         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-85AC6579 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-85AC6579") | The maximum number of vehicles in a fleet for each account in an AWS Region.                              |
| Rate of API requests for each account in an AWS Region                              | Each supported Region: 20            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-6ED070A2 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-6ED070A2") | The maximum number of API requests that you can send per second for each account in an AWS Region.        |
| Rate of ingesting messages for each account in an AWS Region.                       | Each supported Region: 1,000         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-B91464DC "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-B91464DC") | The maximum number of messages AWS IoT FleetWise can ingest per second for each account in an AWS Region. |
| Rate of ingesting messages for each vehicle in an AWS Region.                       | Each supported Region: 1             | [Yes](https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-FDD53FA4 "https://console.aws.amazon.com/servicequotas/home/services/iotfleetwise/quotas/L-FDD53FA4") | The maximum number of messages AWS IoT FleetWise can ingest per second for each vehicle in an AWS Region. |

The following are service limits for data plane vision system data.

###### Note

Vision system data is in preview release and is subject to change.

| Name                       | Default | Adjustable | Description                                                                                                |
| -------------------------- | ------- | ---------- | ---------------------------------------------------------------------------------------------------------- |
| Rate of data               | 128     | Yes        | The maximum capacity in MB per second for messages and Amazon Ion<br>data ingested into AWS IoT FleetWise. |
| Size of Ion object         | 100     | No         | The maximum size in MB of a single Ion file ingested into<br>AWS IoT FleetWise.                            |
| Size of a signal sample    | 200     | No         | The maximum size in KB of metadata (typed data) provided in a signal<br>sample in an Ion file.             |
| Size of all signal samples | 2       | No         | The maximum size in MB of all metadata (typed data) provided across<br>all sample signals in an Ion file.  |
| Rate of structured data    | 10      | Yes        | The maximum capacity in MB per second of all metadata (typed data)<br>ingested across all Ion files.       |
| Rate of binary data        | 1,000   | Yes        | The maximum number of binary blobs per second ingested into<br>AWS IoT FleetWise.                          |

###### Note

AWS IoT FleetWise will drop messages from the vehicle if the ingest rate exceeds the default quota. Revisit your campaign and fleet definitions to adjust the expected number of messages. Any dropped messages cannot be recovered.
