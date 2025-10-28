**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Data encryption

Amazon Pinpoint data is encrypted in transit and at rest. When you submit data to Amazon Pinpoint, it
encrypts the data as it receives and stores it. When you retrieve data from Amazon Pinpoint, it transmits
the data to you by using current security protocols.

## Encryption at rest

Amazon Pinpoint encrypts all the data that it stores for you. This includes configuration data, user
and endpoint data, analytics data, and any data that you add or import into Amazon Pinpoint. To encrypt
your data, Amazon Pinpoint uses internal AWS Key Management Service (AWS KMS) keys that the service owns and maintains on your
behalf. We rotate these keys on a regular basis. For information about AWS KMS, see the
[AWS Key Management Service Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").

## Encryption in transit

Amazon Pinpoint uses HTTPS and Transport Layer Security (TLS) 1.2 or later to communicate with your
clients and applications. To communicate with other AWS services, Amazon Pinpoint uses HTTPS and TLS 1.2.
In addition, when you create and manage Amazon Pinpoint resources by using the console, an AWS SDK, or
the AWS Command Line Interface, all communications are secured using HTTPS and TLS 1.2.

## Key management

To encrypt your Amazon Pinpoint data, Amazon Pinpoint uses internal AWS KMS keys that the service owns and
maintains on your behalf. We rotate these keys on a regular basis. You can't provision and use
your own AWS KMS or other keys to encrypt data that you store in Amazon Pinpoint.
