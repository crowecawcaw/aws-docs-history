# Source configuration for Jamf Pro

## Integrating with Jamf Pro

CloudWatch Pipeline uses the Jamf Pro API to retrieve device inventory and management data. The API provides endpoints for querying computer, mobile device, and user information for security monitoring and compliance.

To integrate CloudWatch Pipelines with Jamf Pro, complete the following high-level steps:

- Create an API Client in the Jamf Pro console with appropriate permissions.
- Note the Client ID and Client Secret.
- Store the credentials in AWS Secrets Manager.
- Create a CloudWatch pipeline with Jamf Pro as the data source.
- Verify that data is flowing into the pipeline.

## Prerequisites

Before you begin, make sure you have the following:

- An active Jamf Pro instance (cloud or on-premises)
- An API Client configured with read permissions for computers, mobile devices, and users
- An AWS account with permissions to create and manage CloudWatch Pipelines
- An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager

## Authenticating with Jamf Pro

Jamf Pro uses OAuth 2.0 Client Credentials for API authentication. The pipeline uses the Client ID and Client Secret to obtain access tokens for API requests.

## Configure Authentication for Jamf Pro

To configure authentication credentials for the pipeline:

1. Log in to Jamf Pro and navigate to Settings > System > API Roles and Clients.
2. Create a new API Client with the required permissions (Read Computers, Read Mobile Devices, Read Users).
3. Note the Client ID and Client Secret provided.
4. Store the `client_id` and `client_secret` in AWS Secrets Manager.

## Configuring the CloudWatch Pipeline

To configure the pipeline, choose Jamf Pro as the data source. Provide the `hostname`, `client_id`, and `client_secret`. After you create and activate the pipeline, device inventory data from Jamf Pro will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports the following OCSF event classes:

- **Device Inventory Info [5001]** – Computer and mobile device inventory
