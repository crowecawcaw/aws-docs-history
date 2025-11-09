# Amazon Simple Notification Service endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, IPv6 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

Service endpoints allow you to connect to other AWS services. The following
endpoints support both standard and FIFO topics.

| Region Name                | Region         | Endpoint                                                                                    | Protocol                                  |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------- |
| US East (Ohio)             | us-east-2      | sns.us-east-2.amazonaws.com<br>sns-fips.us-east-2.api.aws<br>sns.us-east-2.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTP and HTTPS |
| US East (N. Virginia)      | us-east-1      | sns.us-east-1.amazonaws.com<br>sns-fips.us-east-1.api.aws<br>sns.us-east-1.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTP and HTTPS |
| US West (N. California)    | us-west-1      | sns.us-west-1.amazonaws.com<br>sns-fips.us-west-1.api.aws<br>sns.us-west-1.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTP and HTTPS |
| US West (Oregon)           | us-west-2      | sns.us-west-2.amazonaws.com<br>sns-fips.us-west-2.api.aws<br>sns.us-west-2.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTP and HTTPS |
| Africa (Cape Town)         | af-south-1     | sns.af-south-1.amazonaws.com<br>sns.af-south-1.api.aws                                      | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | sns.ap-east-1.amazonaws.com<br>sns.ap-east-1.api.aws                                        | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | sns.ap-south-2.amazonaws.com<br>sns.ap-south-2.api.aws                                      | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | sns.ap-southeast-3.amazonaws.com<br>sns.ap-southeast-3.api.aws                              | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | sns.ap-southeast-5.amazonaws.com<br>sns.ap-southeast-5.api.aws                              | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | sns.ap-southeast-4.amazonaws.com<br>sns.ap-southeast-4.api.aws                              | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | sns.ap-south-1.amazonaws.com<br>sns.ap-south-1.api.aws                                      | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | sns.ap-southeast-6.amazonaws.com<br>sns.ap-southeast-6.api.aws                              | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | sns.ap-northeast-3.amazonaws.com<br>sns.ap-northeast-3.api.aws                              | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | sns.ap-northeast-2.amazonaws.com<br>sns.ap-northeast-2.api.aws                              | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | sns.ap-southeast-1.amazonaws.com<br>sns.ap-southeast-1.api.aws                              | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | sns.ap-southeast-2.amazonaws.com<br>sns.ap-southeast-2.api.aws                              | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | sns.ap-east-2.amazonaws.com<br>sns.ap-east-2.api.aws                                        | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | sns.ap-southeast-7.amazonaws.com<br>sns.ap-southeast-7.api.aws                              | HTTP and HTTPS<br>HTTP and HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | sns.ap-northeast-1.amazonaws.com<br>sns.ap-northeast-1.api.aws                              | HTTP and HTTPS<br>HTTP and HTTPS          |
| Canada (Central)           | ca-central-1   | sns.ca-central-1.amazonaws.com<br>sns-fips.ca-central-1.api.aws<br>sns.ca-central-1.api.aws | HTTP and HTTPS<br>HTTPS<br>HTTP and HTTPS |
| Canada West (Calgary)      | ca-west-1      | sns.ca-west-1.amazonaws.com<br>sns-fips.ca-west-1.api.aws<br>sns.ca-west-1.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTP and HTTPS |
| Europe (Frankfurt)         | eu-central-1   | sns.eu-central-1.amazonaws.com<br>sns.eu-central-1.api.aws                                  | HTTP and HTTPS<br>HTTP and HTTPS          |
| Europe (Ireland)           | eu-west-1      | sns.eu-west-1.amazonaws.com<br>sns.eu-west-1.api.aws                                        | HTTP and HTTPS<br>HTTP and HTTPS          |
| Europe (London)            | eu-west-2      | sns.eu-west-2.amazonaws.com<br>sns.eu-west-2.api.aws                                        | HTTP and HTTPS<br>HTTP and HTTPS          |
| Europe (Milan)             | eu-south-1     | sns.eu-south-1.amazonaws.com<br>sns.eu-south-1.api.aws                                      | HTTP and HTTPS<br>HTTP and HTTPS          |
| Europe (Paris)             | eu-west-3      | sns.eu-west-3.amazonaws.com<br>sns.eu-west-3.api.aws                                        | HTTP and HTTPS<br>HTTP and HTTPS          |
| Europe (Spain)             | eu-south-2     | sns.eu-south-2.amazonaws.com<br>sns.eu-south-2.api.aws                                      | HTTP and HTTPS<br>HTTP and HTTPS          |
| Europe (Stockholm)         | eu-north-1     | sns.eu-north-1.amazonaws.com<br>sns.eu-north-1.api.aws                                      | HTTP and HTTPS<br>HTTP and HTTPS          |
| Europe (Zurich)            | eu-central-2   | sns.eu-central-2.amazonaws.com<br>sns.eu-central-2.api.aws                                  | HTTP and HTTPS<br>HTTP and HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | sns.il-central-1.amazonaws.com<br>sns.il-central-1.api.aws                                  | HTTP and HTTPS<br>HTTP and HTTPS          |
| Mexico (Central)           | mx-central-1   | sns.mx-central-1.amazonaws.com<br>sns.mx-central-1.api.aws                                  | HTTP and HTTPS<br>HTTP and HTTPS          |
| Middle East (Bahrain)      | me-south-1     | sns.me-south-1.amazonaws.com<br>sns.me-south-1.api.aws                                      | HTTP and HTTPS<br>HTTP and HTTPS          |
| Middle East (UAE)          | me-central-1   | sns.me-central-1.amazonaws.com<br>sns.me-central-1.api.aws                                  | HTTP and HTTPS<br>HTTP and HTTPS          |
| South America (São Paulo)  | sa-east-1      | sns.sa-east-1.amazonaws.com<br>sns.sa-east-1.api.aws                                        | HTTP and HTTPS<br>HTTP and HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | sns.us-gov-east-1.amazonaws.com<br>sns.us-gov-east-1.api.aws                                | HTTPS<br>HTTPS                            |
| AWS GovCloud (US-West)     | us-gov-west-1  | sns.us-gov-west-1.amazonaws.com<br>sns.us-gov-west-1.api.aws                                | HTTPS<br>HTTPS                            |

## Service quotas

The following quotas determine how many Amazon SNS resources you can create in your AWS
account, and they determine the rate at which you can issue Amazon SNS API requests.

### Amazon SNS resource

To request an increase, submit an [SNS quota increase
request](https://console.aws.amazon.com/servicequotas/home/services/sns/quotas "https://console.aws.amazon.com/servicequotas/home/services/sns/quotas").

| Resource                                          | Default                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Topics                                            | • Standard: 100,000 per account<br>• FIFO: 1,000 per account                                                                                                                                                                                                                                         |
| Subscriptions                                     | • Standard: 12,500,000 per topic<br>For Firehose delivery streams, 5 per topic, per<br>subscription owner<br>• FIFO: 100 per topic                                                                                                                                                                   |
| Pending subscriptions                             | 5,000 per account                                                                                                                                                                                                                                                                                    |
| Account spend threshold for SMS                   | 1.00 USD per account                                                                                                                                                                                                                                                                                 |
| Delivery rate for promotional SMS messages        | 20 messages per second                                                                                                                                                                                                                                                                               |
| Delivery rate for transactional SMS messages      | 20 messages per second                                                                                                                                                                                                                                                                               |
| Delivery rate for email messages                  | 10 messages per second. This is a hard limit and can't be<br>increased.                                                                                                                                                                                                                              |
| Maximum number of messages in PublishBatchRequest | 10 [PublishBatchRequestEntries](../../../sns/latest/api/API_PublishBatch.md "../../../sns/latest/api/API_PublishBatch.md")                                                                                                                                                                           |
| Subscription filter policies                      | • 200 filter policies per topic<br>• 10,000 filter policies per AWS<br>account                                                                                                                                                                                                                       |
| Message header                                    | The maximum header size is 16,384 bytes (16 KiB).                                                                                                                                                                                                                                                    |
| Message size                                      | The maximum message size is 262,144 bytes (256 KiB). To publish<br>messages larger than 256 KiB, you can check the [Amazon SNS Extended<br>Client Libraries](../../../sns/latest/dg/large-message-payloads.md "../../../sns/latest/dg/large-message-payloads.md"). The maximum payload size is 2 GB. |

### Amazon SNS API throttling

The following quotas throttle the rate at which you can issue Amazon SNS API
requests.

#### Hard

The following quotas cannot be increased.

| API                                | Transactions per second |
| ---------------------------------- | ----------------------- |
| AddPermission                      | 10                      |
| CheckIfPhoneNumberIsOptedOut       | 50                      |
| CreateSMSSandboxPhoneNumber        | 1                       |
| DeleteSMSSandboxPhoneNumber        | 1                       |
| GetSMSAttributes                   | 20                      |
| GetSMSSandboxAccountStatus         | 10                      |
| ListEndpointsByPlatformApplication | 30                      |
| ListOriginationNumbers             | 1                       |
| ListPhoneNumbersOptedOut           | 10                      |
| ListPlatformApplications           | 15                      |
| ListSMSSandboxPhoneNumbers         | 1                       |
| ListSubscriptions                  | 30                      |
| ListSubscriptionsByTopic           | 30                      |
| ListTagsForResource                | 10                      |
| ListTopics                         | 30                      |
| OptInPhoneNumber                   | 20                      |
| RemovePermission                   | 10                      |
| SetSMSAttributes                   | 1                       |
| Subscribe                          | 100                     |
| TagResource                        | 10                      |
| Unsubscribe                        | 100                     |
| UntagResource                      | 10                      |
| VerifySMSSandboxPhoneNumber        | 1                       |

#### Soft

The following quotas vary by AWS Region. The messages per second quota is
based on the number of messages published to an Amazon SNS region, per account,
combining [`Publish`](../../../sns/latest/api/API_Publish.md "../../../sns/latest/api/API_Publish.md") and [`PublishBatch`](../../../sns/latest/api/API_PublishBatch.md "../../../sns/latest/api/API_PublishBatch.md")
API requests including both standard and FIFO topic types. To request a soft
limit increase, submit an [SNS quota increase
request](https://console.aws.amazon.com/servicequotas/home/services/sns/quotas "https://console.aws.amazon.com/servicequotas/home/services/sns/quotas").

For example, if your regional quota is 30,000 messages per second, per
account, there are a few ways this quota can be reached:

- Using the `Publish` action at a rate of 30,000 API requests
  per second to publish 30,000 messages (one message per API
  request).
- Using the `PublishBatch` action at a rate of 3,000 API
  requests per second to publish 30,000 messages (10 messages per batch
  API request).
- Using the `Publish` action at a rate of 10,000 API requests
  per second to publish 10,000 messages (one message per API request) and
  the `PublishBatch` action at a rate of 2,000 API requests per
  second to publish 20,000 messages (10 messages per batch API request)
  for a total of 30,000 messages published per second.

| Publish API throttling per account                                                                                                                                                                                                                    | AWS Regions                | Standard topics            | FIFO topics\* |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | ------------- |
| US East (N. Virginia) Region                                                                                                                                                                                                                          | 30,000 messages per second | 30,000 messages per second |
| US West (Oregon) RegionEurope (Ireland) Region                                                                                                                                                                                                        | 9,000 messages per second  | 9,000 messages per second  |
| US East (Ohio) Region<br>US West (N. California) Region<br>Asia Pacific (Mumbai) Region<br>Asia Pacific (Seoul) Region<br>Asia Pacific (Singapore) Region<br>Asia Pacific (Sydney) Region<br>Asia Pacific (Tokyo) Region<br>Europe (Frankfurt) Region | 1,500 messages per second  | 3,000 messages per second  |
| All other supported Regions                                                                                                                                                                                                                           | 300 messages per second    | 3,000 messages per second  |

\*Amazon SNS FIFO per topic limits exceed the default per account limit when
`FifoThroughputScope` is set to `MessageGroup`. Amazon SNS
FIFO topics have a maximum per message group limit of 300 messages per second,
and Amazon SNS FIFO topics per topic throughput defaults to a limit of 3,000 messages
per second or 20MB per second, which ever comes first, when
`FifoThroughputScope` is set to `Topic`. Amazon SNS FIFO
topics can experience reduced throughput within a message group for cross
Regional deliveries due to the added latency between Regions, and the need to
maintain the strict order of messages.

| Other API throttling                                                                                                                                                                                                                                                                                                                                                                                                              | APIs                         | AWS Regions | Transactions per second |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------- | ----------------------- |
| ConfirmSubscription<br>CreatePlatformApplication<br>CreatePlatformEndpoint<br>CreateTopic<br>DeleteEndpoint<br>DeletePlatformApplication<br>DeleteTopic<br>GetEndpointAttributes<br>GetDataProtectionPolicy<br>GetPlatformApplicationAttributes<br>GetSubscriptionAttributes<br>GetTopicAttributes<br>SetEndpointAttributes<br>SetPlatformApplicationAttributes<br>SetSubscriptionAttributes<br>SetTopicAttributes                | US East (N. Virginia) Region | 3,000       |
| US West (Oregon) Region<br>Europe (Ireland) Region                                                                                                                                                                                                                                                                                                                                                                                | 900                          |
| US East (Ohio) Region<br>US West (N. California) Region<br>Asia Pacific (Mumbai) Region<br>Asia Pacific (Seoul) Region<br>Asia Pacific (Singapore) Region<br>Asia Pacific (Sydney) Region<br>Asia Pacific (Tokyo) Region<br>Europe (Frankfurt) Region                                                                                                                                                                             | 150                          |
| Africa (Cape Town) Region<br>Asia Pacific (Hong Kong) Region<br>Asia Pacific (Hyderabad)<br>Asia Pacific (Osaka) Region<br>Canada (Central) Region<br>China (Beijing) Region<br>China (Ningxia) Region<br>Europe (London) Region<br>Europe (Milan) Region<br>Europe (Paris) Region<br>Europe (Spain)<br>Europe (Stockholm) Region<br>Israel (Tel Aviv) Region<br>Middle East (Bahrain) Region<br>South America (São Paulo) Region | 30                           |
| PutDataProtectionPolicy                                                                                                                                                                                                                                                                                                                                                                                                           | All Commercial Regions       | 1           |

| Message Archiving and Replay | Policy                 | AWS Regions | Standard topics | FIFO topics |
| ---------------------------- | ---------------------- | ----------- | --------------- | ----------- |
| ArchivePolicy                | All Commercial Regions | N/A         | Yes             |
| AWS GovCloud (US) Regions    | N/A                    | Yes         |
| ReplayPolicy                 | All Commercial Regions | N/A         | Yes             |
| AWS GovCloud (US) Regions    | N/A                    | Yes         |
