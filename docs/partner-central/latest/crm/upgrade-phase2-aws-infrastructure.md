# Set up AWS infrastructure

The API version of the connector introduces a fundamental shift in how partners
authenticate and interact with AWS Partner Central data:

- **Amazon S3 version:** Partners maintained their own
  AWS accounts and accessed Amazon-owned Amazon S3 buckets where data was
  stored.
- **API version:** Direct Amazon S3 access is
  eliminated. Partners now authenticate via IAM roles and interact through APIs
  that enable real-time, bidirectional synchronization.
  This architectural change requires a Salesforce Administrator to work with an IT Cloud
  Admin to set up two new components: a Salesforce External Client App and AWS
  infrastructure components.

## Set up Salesforce External Client App

The API version requires a connected app in Salesforce because AWS must call
back into your Salesforce org via REST API to complete bidirectional synchronization.
The Amazon S3 version did not need this component because it only performed one-way batch
synchronization from Amazon S3 buckets using IAM credentials.

The connected app enables **OAuth 2.0 Client Credentials
flow**. EventBridge uses this authentication method to push updates from
AWS Partner Central back into your Salesforce org.

The Salesforce Administrator should follow the instructions in the [Set up External Client App on Salesforce](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/aws-infrastructure#task-1-:-set-up-external-client-app-on-salesforce "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/aws-infrastructure#task-1-:-set-up-external-client-app-on-salesforce") section to configure the
external client app.

## Set up AWS components

The AWS infrastructure for the API version includes:

- **EventBridge** for real-time event
  processing
- **IAM roles** for secure
  authentication

These components replace the Amazon S3 bucket access model used in the previous
version.

The IT Cloud Admin should deploy the CloudFormation template by following the
instructions in the [Set up AWS Components](https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/aws-infrastructure#task-2-:-set-up-aws-components "https://catalog.us-east-1.prod.workshops.aws/workshops/ea2a0910-436a-4a65-82c4-725657009443/en-US/aws-partner-crm-connector/aws-infrastructure#task-2-:-set-up-aws-components") section. The template provisions EventBridge
rules and IAM roles needed for API-based synchronization.
