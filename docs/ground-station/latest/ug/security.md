# Data encryption during transit for AWS Ground Station

AWS Ground Station provides encryption by default to protect your sensitive data during transit. Data
can be streamed between AWS Ground Station antenna locations and your Amazon EC2 instances in two ways,
depending on the mission profile configuration.

- AWS Ground Station Agent
- Dataflow endpoint

Each method of streaming data handles encrypting data in transit differently. The following
sections describe each method.

## AWS Ground Station Agent streams

AWS Ground Station Agent encrypts its streams using customer managed AWS KMS keys. The AWS Ground Station Agent running on
your Amazon EC2 instance will automatically decrypt the stream to provide decrypted data.

The AWS KMS key used for encrypting a stream is specified when creating a
`MissionProfile` in the
[streamsKmsKey](../APIReference/API_CreateMissionProfile.md#groundstation-CreateMissionProfile-request-streamsKmsKey "../APIReference/API_CreateMissionProfile.md#groundstation-CreateMissionProfile-request-streamsKmsKey") parameter. All permissions granting AWS Ground Station access to the keys are handled through the
AWS KMS key policy attached to `streamsKmsKey`.

##

Dataflow endpoint streams

Dataflow endpoint streams are encrypted using
[Datagram Transport Layer Security (DTLS)](https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security "https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security") . This is done using self-signed certificates, and doesn't require additional
configuration.
