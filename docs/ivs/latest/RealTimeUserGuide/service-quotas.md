# IVS Service Quotas | Real-Time Streaming

The following are service quotas and limits for Amazon Interactive Video Service (IVS)
real-time endpoints, resources, and other operations. Service quotas (also known as limits)
are the maximum number of service resources or operations for your AWS account. That is,
these limits are per AWS account, unless noted otherwise in the table. Also see [AWS Service
Quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

You use an endpoint to connect programmatically to an AWS service. Also see [AWS Service
Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

All quotas are enforced on a per-account basis in a specific AWS region.

## Service Quota Increases

For quotas that are adjustable, you can request a rate increase through the [AWS console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). Use the
console to view information about service quotas too.

API call rate quotas are not adjustable.

## API Call Rate Quotas

| Operation Type                            | Operation                    | Default    |
| ----------------------------------------- | ---------------------------- | ---------- | ------------------------------------------------------------------------------------------------------ |
| Composition                               | `GetComposition`             | 5 TPS      |
| Composition                               | `ListCompositions`           | 5 TPS      |
| Composition                               | `StartComposition`           | 5 TPS      |
| Composition                               | `StopComposition`            | 5 TPS      |
| IngestConfiguration                       | `CreateIngestConfiguration`  | 5 TPS      |
| IngestConfiguration                       | `DeleteIngestConfiguration`  | 5 TPS      |
| IngestConfiguration                       | `GetIngestConfiguration`     | 5 TPS      |
| IngestConfiguration                       | `ListIngestConfigurations`   | 5 TPS      |
| IngestConfiguration                       | `UpdateIngestConfiguration`  | 5 TPS      |
| MediaEncoder                              | `CreateEncoderConfiguration` | 5 TPS      |
| MediaEncoder                              | `DeleteEncoderConfiguration` | 5 TPS      |
| MediaEncoder                              | `GetEncoderConfiguration`    | 5 TPS      |
| MediaEncoder                              | `ListEncoderConfigurations`  | 5 TPS      |
| PublicKey                                 | `DeletePublicKey`            | 3 TPS      |
| PublicKey                                 | `GetPublicKey`               | 3 TPS      |
| PublicKey                                 | `ImportPublicKey`            | 3 TPS      |
| PublicKey                                 | `ListPublicKeys`             | 3 TPS      |
| Stage                                     | `CreateParticipantToken`     | 50 TPS     |
| Stage                                     | `CreateStage`                | 5 TPS      |
| Stage                                     | `DeleteStage`                | 5 TPS      |
| Stage                                     | `DisconnectParticipant`      | 5 TPS      |
| Stage                                     | `GetParticipant`             | 5 TPS      |
| Stage                                     | `GetStage`                   | 5 TPS      |
| Stage                                     | `GetStageSession`            | 5 TPS      |
| Stage                                     | `ListStages`                 | 5 TPS      |
| Stage                                     | `UpdateStage`                | 5 TPS      |
| Stage                                     | `ListParticipants`           | 5 TPS      |
| Stage                                     | `ListParticipantEvents`      | 5 TPS      |
| Stage                                     | `ListStageSessions`          | 5 TPS      |
| StorageConfiguration                      | `CreateStorageConfiguration` | 5 TPS      |
| StorageConfiguration                      | `DeleteStorageConfiguration` | 5 TPS      |
| StorageConfiguration                      | `GetStorageConfiguration`    | 5 TPS      |
| StorageConfiguration                      | `ListStorageConfigurations`  | 5 TPS      |
| Tags                                      | `ListTagsForResource`        | 10 TPS     |
| Tags                                      | `TagResource`                | 10 TPS     |
| Tags                                      | `UntagResource`              | 10 TPS     | ## Other Quotas                                                                                        |
| Resource or Feature                       | Default                      | Adjustable | Description                                                                                            |
| ---                                       | ---                          | ---        | ---                                                                                                    |
| Composition destinations                  | 2                            | No         | Maximum number of Destination objects in a Composition resource.                                       |
| Composition: max duration                 | 24                           | No         | Maximum amount of time a composition can exist, in hours.                                              |
| Compositions                              | 20                           | Yes        | Maximum concurrent Composition resources per account.                                                  |
| Compositions per stage                    | 5                            | Yes        | Maximum concurrent Composition resources per stage.                                                    |
| Concurrent participant replications       | 5                            | No         | Maximum number of concurrent replications per participant across all stages in an AWS Region.          |
| Concurrent publishers                     | 1,000                        | Yes        | Maximum number of participants who can be publishing across all stages in an AWS Region.               |
| Concurrent subscriptions                  | 20,000                       | Yes        | Maximum number of simultaneous publisher-to-subscriber connections across all stages in an AWS Region. |
| EncoderConfigurations                     | 20                           | Yes        | Maximum number of EncoderConfiguration resources per account.                                          |
| IngestConfigurations                      | 100                          | Yes        | Maximum number of IngestConfiguration resources per account.                                           |
| Participant download bitrate              | 8.5 Mbps                     | No         | Maximum aggregate download bitrate across all of a participant’s subscriptions.                        |
| Participant publish bitrate               | 8.5 Mbps                     | No         | Maximum bits per second that can be streamed to a stage.                                               |
| Participant publish or subscribe duration | 24                           | No         | Maximum length of time a participant can publish or remain subscribed to a stage, in hours.            |
| Participant publish resolution            | 720p                         | No         | Maximum resolution of video published by participants.                                                 |
| PublicKeys                                | 3                            | No         | Maximum number of public keys, per AWS Region.                                                         |
| Stage participants (publishers)           | 12                           | No         | Maximum number of participants who can be publishing to a stage at once.                               |
| Stage participants (subscribers)          | 10,000                       | Yes        | Maximum number of participants who can be subscribing to a stage at once.                              |
| Stages                                    | 1,000                        | Yes        | Maximum number of stages, per AWS Region.                                                              |
| StorageConfigurations                     | 5                            | Yes        | Maximum number of StorageConfiguration resources per account.                                          |
