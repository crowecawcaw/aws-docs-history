# CloudTrail event logs in Security Lake

AWS CloudTrail provides you with a history of AWS API calls for your account, including
API calls made using the AWS Management Console, the AWS SDKs, the command line tools, and certain
AWS services. CloudTrail also allows you to identify which users and accounts called AWS
APIs for services that support CloudTrail, the source IP address that the calls were made
from, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

Security Lake can collect logs associated with CloudTrail management events and CloudTrail data events for
S3 and Lambda. CloudTrail management events, S3 data events, and Lambda data events are three
separate sources in Security Lake. As a result, they have different values for [`sourceName`](../APIReference/API_AwsLogSourceConfiguration.md#securitylake-Type-AwsLogSourceConfiguration-sourceName "../APIReference/API_AwsLogSourceConfiguration.md#securitylake-Type-AwsLogSourceConfiguration-sourceName") when you add one of these as an ingested log
source. Management events, also known as control plane events, provide insight into
management operations that are performed on resources in your AWS account. CloudTrail data
events, also known as data plane operations, show the resource operations performed on
or within resources in your AWS account. These operations are often high-volume
activities.

To collect CloudTrail management events in Security Lake, you must have at least one CloudTrail
multi-Region organization trail that collects read and write CloudTrail management events.
Logging must be enabled for the trail. If you do have logging configured in the other
services, you don't need to change your logging configuration to add them as log sources
in Security Lake. Security Lake pulls data directly from these services through an independent and
duplicated stream of events.

A multi-Region trail delivers log files from multiple Regions to a single Amazon Simple Storage Service
(Amazon S3) bucket for a single AWS account. If you already have a multi-Region trail
managed through CloudTrail console or AWS Control Tower, no further action is required.

- For information about creating and managing a trail through CloudTrail, see [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the
  _AWS CloudTrail User Guide_.
- For information about creating and managing a trail through AWS Control Tower, see
  [Logging
  AWS Control Tower actions with AWS CloudTrail](../../../controltower/latest/userguide/logging-using-cloudtrail.md "../../../controltower/latest/userguide/logging-using-cloudtrail.md") in the _AWS Control Tower User
  Guide_.
  When you add CloudTrail events as a source, Security Lake immediately starts collecting your CloudTrail
  event logs. It consumes CloudTrail management and data events directly from CloudTrail through an
  independent and duplicated stream of events.

Security Lake doesn't manage your CloudTrail events or affect your existing CloudTrail configurations. To
manage access and retention of your CloudTrail events directly, you must use the CloudTrail service
console or API. For more information, see [Viewing events with
CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_.

The following list provides GitHub repository links to the mapping reference for how
Security Lake normalizes CloudTrail events to OCSF.

###### **GitHub OCSF repository for CloudTrail events**

- Source version 1 [(v1.0.0-rc.2)](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.0.0-rc.2/CloudTrail "https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.0.0-rc.2/CloudTrail")
- Source version 2 [(v1.1.0)](https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/CloudTrail "https://github.com/ocsf/examples/tree/main/mappings/markdown/AWS/v1.1.0/CloudTrail")
