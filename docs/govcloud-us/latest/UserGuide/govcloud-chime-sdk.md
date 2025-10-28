# Amazon Chime SDK in AWS GovCloud (US)

With the Amazon Chime SDK, you can quickly add voice, video, and screen sharing into
your websites and mobile applications. Built-in machine learning provides noise and echo
reduction to improve audio quality, and background replacement and blur to help improve
visual privacy. Innovate faster by using the Amazon Chime SDK communication building
blocks for secure customer communications that scale up or down to meet demand.

## How Amazon Chime SDK differs for

AWS GovCloud (US)

- WebRTC media sessions (meetings-chime)
  - Sessions can be hosted in AWS GovCloud (US) Regions only
  - The nearest AWS Region can be discovered via [https://nearest-us-gov-media-region.l.chime.aws](https://nearest-us-gov-media-region.l.chime.aws "https://nearest-us-gov-media-region.l.chime.aws")
  - Live transcription only uses Amazon Transcribe in the
    AWS GovCloud (US-West) Region
  - Live transcription does not support Amazon Transcribe Medical

- The following Amazon Chime SDK features are not supported:
  - Media Pipelines (media-pipelines-chime)
  - PSTN Audio (service.chime)
  - SIP Trunking (service.chime)
  - Messaging (messaging-chime)
  - Identity (identity-chime)
  - Console

- Amazon Chime SDK in AWS GovCloud (US) is in a separate AWS partition from
  other AWS Regions. Therefore, it does not support cross-partition integration
  with other AWS services, such as Amazon CloudWatch, Amazon EventBridge, Amazon Simple Notification Service, Amazon Simple Queue Service and
  Amazon Transcribe.

## Documentation for Amazon Chime SDK

[Amazon Chime SDK
documentation](../../../chime-sdk/index.md "../../../chime-sdk/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

Amazon Chime SDK metadata is not permitted to contain export-controlled data. This
metadata includes all configuration data that you enter or parameters that you supply in
API requests.

Do not enter export-controlled data in the following fields:

- External Meeting Id
- External User Id
- Tags
