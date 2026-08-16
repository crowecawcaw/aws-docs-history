# Source configuration for Box

## Integrating with Box

CloudWatch Pipeline uses the Box Events API to retrieve audit logs, user activity, file operations, and security events. The Events API provides enterprise-level event data for security monitoring and compliance.

To integrate CloudWatch Pipelines with Box, complete the following high-level steps:

- Create a Box Custom App with Server Authentication (Client Credentials Grant) in the Box Developer Console.
- Note the Client ID, Client Secret, and Enterprise ID.
- Authorize the app in the Box Admin Console.
- Store the credentials in AWS Secrets Manager.
- Create a CloudWatch pipeline with Box as the data source.
- Verify that data is flowing into the pipeline.

## Prerequisites

Before you begin, make sure you have the following:

- A Box Enterprise account with admin access
- A Box Custom App configured with Server Authentication (Client Credentials Grant)
- The app authorized by a Box Admin in the Admin Console
- An AWS account with permissions to create and manage CloudWatch Pipelines
- An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager

## Authenticating with Box

Box uses OAuth 2.0 Client Credentials Grant for server-to-server authentication. The pipeline uses the Client ID and Client Secret to obtain access tokens for API requests.

## Configure Authentication for Box

To configure authentication credentials for the pipeline:

1. Log in to the Box Developer Console and create a Custom App with Server Authentication (Client Credentials Grant).
2. Note the Client ID and Client Secret from the app configuration.
3. Note your Enterprise ID from the Box Admin Console under Account & Billing.
4. Authorize the app in the Box Admin Console under Apps > Custom Apps.
5. Store the `client_id` and `client_secret` in AWS Secrets Manager.

## Configuring the CloudWatch Pipeline

To configure the pipeline, choose Box as the data source. Provide the `enterprise_id`, `client_id`, and `client_secret`. After you create and activate the pipeline, log data from Box will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports the following OCSF event classes:

- **Account Change [3001]** – Account and permission changes
- **Authentication [3002]** – Login and session events
- **Group Management [3006]** – Group membership changes
- **File Hosting Activity [6006]** – File uploads, downloads, and sharing
- **Entity Management [3004]** – User and collaboration management
- **Security Finding [2001]** – Security policy violations and shield events
- **User Inventory Info [5003]** – User inventory
- **Group Inventory Info [5004]** – Group and membership inventory
