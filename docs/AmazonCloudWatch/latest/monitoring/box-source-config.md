# Source configuration for Box

## Prerequisites

Before you begin, make sure you have the following:

- A Box Enterprise account with **admin** privileges. **Two-factor authentication (2FA)** must be enabled.
- A Box App configured with OAuth2 **Client Credentials Grant** (Server Authentication) in the Box Developer Console.
- A Box App authorized for authentication in the Box Admin Console
- An AWS account with permissions to create and manage CloudWatch Pipelines.
- An AWS account with required permissions to create, retrieve, and update secrets in AWS Secrets Manager.
- An AWS account with permissions to create and manage CloudWatch Logs log groups.

## Integrating with Box

To integrate Box with CloudWatch Pipelines, complete the following high-level steps:

- Create and configure a Custom App with Client Credentials Grant in the Box Developer Console.
- Verify 2FA and authorize the Custom App.
- Note the Client ID, Client Secret, and Enterprise ID.
- Store the client credentials in AWS Secrets Manager.
- Create a CloudWatch pipeline with Box as the data source.
- Verify data is flowing into the configured CloudWatch Logs log group.

## Authenticating with Box

To read the data, the pipeline needs to authenticate with your Box enterprise. Box uses OAuth2 Client Credentials Grant, which issues a short-lived access token (60 minutes) for server-to-server API access without user interaction.

## Configure Authentication for Box

To configure authentication credentials for the pipeline:

1. Log in to the [Box Developer Console](https://app.box.com/developers/console "https://app.box.com/developers/console") and create a **New App**.
2. Enter the App Name, choose **Client Credentials Grant** as the App Type, and choose **Create App**.
3. Navigate to **App Details > Access** panel, choose **Fetch Secret** and complete the 2FA verification.
4. Choose **Fetch Secret** again, and then copy the `Client ID` and `Client Secret` for later use.
5. Under App Access Level, select **App + Enterprise Access**. Keep the default selections for Application Scopes.
6. Navigate to **App Details > Status**, choose **Authorize**, and make sure the application is marked as Authorized.
7. Choose your profile icon and select **Copy Enterprise ID** for later use. Alternatively, you can find it in **Admin Console** > **Account & Billing** > **Enterprise ID**.
8. In AWS Secrets Manager, create a secret and store:

   - Client ID under the key `client_id`
   - Client Secret under the key `client_secret`

## Configuring the CloudWatch Pipeline

To configure the pipeline to read data, choose Box as the data source. Provide the required information such as the Enterprise ID (`enterprise_id`), Client ID (`client_id`), and Client Secret (`client_secret`). After you create and activate the pipeline, enterprise events and inventory data from Box will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and Box events that map to the following OCSF event classes.

###### Note

Events that do not match any OCSF event classes listed below are automatically passed through and sent directly to the configured sink in their original format without additional processing.

### Entity Management (3004)

**Enterprise Events** – Contains enterprise-wide administrative and security events including file operations, sharing changes, user management actions, Shield alerts, and application events.

### Account Change (3001)

**Users** – Provides user account inventory including profile information, status, storage usage, and role assignments.

### Group Management (3006)

- **Groups** – Contains group inventory with group type, membership visibility, and invitability settings.
- **Group Memberships** – Records user-to-group membership associations including role assignments (member, admin).
- **Group Collaborations** – Provides shared access grants (collaborations) between groups and content items including role and status.

### Base Event (0)

Events that do not map to a specific OCSF class are mapped to the Base Event class.
