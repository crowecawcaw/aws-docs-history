# Getting started with SSP mode in AMS

Self-service provisioning is one of the AMS modes for multi-account landing zone (MALZ) that you can employ. For more information, see
[Modes overview](ams-modes-ug.md "ams-modes-ug.md").

To provide self-service provisioning capabilities, AMS has created elevated IAM roles with permission boundaries to limit unintended changes
from direct AWS service access. The roles don't prevent all changes and you must adhere to your internal controls and compliance policies, and
validate that all AWS services being used meet the required certifications. This is the self-service provisioning mode.
For details on AWS compliance requirements, see
[AWS Compliance](https://aws.amazon.com/compliance/ "https://aws.amazon.com/compliance/").

To add a self-service provisioning service to your multi-account landing zone Application account,
use the **Management | AWS service | Self-provisioned service | Add** change type (CT), either the review-required CT or
automated CT, as instructed for the service.

###### Note

To request that AMS provide an additional self-service provisioning service, file a service request.
