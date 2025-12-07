# Data encryption in Amazon Nova Act

## Encryption at rest

Nova Act stores data at rest using Amazon DynamoDB and Amazon Simple Storage Service (Amazon S3). The data at rest is encrypted using AWS encryption solutions by default. Nova Act encrypts your data using AWS owned encryption keys from AWS Key Management Service. You do not need to take any action to protect the AWS managed keys that encrypt your data. For more information, see AWS owned keys in the AWS KMS Developer Guide.

Key considerations:

- Nova Act temporarily stores Agent Trajectory data, which includes the input prompt, screenshots, and agent response to maintain historical context while executing a workflow.
- If you wish to persist the Agent Trajectory Data indefinitely, you may opt into the service writing this data to an S3 bucket that you own and control. We strongly encourage you to enable encryption on this S3 bucket.
- The following data is not encrypted by default:
  - WorkflowDefinition Names
  - Workflow Run Ids

## Encryption in transit

All communication between customers and the Nova Act AWS service, as well as between Nova Act and its downstream dependencies, is protected using TLS 1.2 or higher connections.

## Key management

All AWS KMS keys are managed by the Nova Act service. At this time, there is no support for customer-managed keys (CMK), but is expected to be added in the subsequent release.

## Internetwork traffic policy (VPC and PrivateLink)

PrivateLink is not yet supported by Nova Act, but this functionality is expected to be added in a subsequent release.
