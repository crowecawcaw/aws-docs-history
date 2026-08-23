# Source configuration for Jamf Pro

## Prerequisites

Before you begin, make sure you have the following:

- An active Jamf Pro tenant (Jamf Cloud or on-premises) with API access enabled.
- A Jamf Pro user account with API role permissions to access the Computer Inventory endpoint, or an API Client configured with the required OAuth2 scopes.
- An AWS account with [permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions") to create and manage CloudWatch Pipelines.
- An AWS account with required [permissions](../../../secretsmanager/latest/userguide/auth-and-access.md#reference_iam-permissions "../../../secretsmanager/latest/userguide/auth-and-access.md#reference_iam-permissions") to create, retrieve, and update secrets in AWS Secrets Manager.
- An AWS account with permissions to create and manage CloudWatch Logs log groups.

## Integrating with Jamf Pro

To integrate Jamf Pro with CloudWatch Pipelines, complete the following high-level steps:

- Create an API Client (OAuth2) in the Jamf Pro Console with the required scopes.
- Note the Client ID and Client Secret.
- Identify your Jamf Pro instance URL.
- Store the credentials in AWS Secrets Manager.
- Create a CloudWatch pipeline with Jamf Pro as the data source.
- Verify data is flowing into the configured CloudWatch Logs log group.

## Authenticating with Jamf Pro

To read the data, the pipeline needs to authenticate with your Jamf Pro tenant. Jamf Pro uses OAuth2 Client Credentials flow, which exchanges a Client ID and Client Secret for a short-lived bearer token (valid for 20 minutes) used for all subsequent API calls.

## Configure Authentication for Jamf Pro

To configure authentication credentials for the pipeline:

1. Log in to the Jamf Pro Console and navigate to **Settings > System > API Roles and Clients**.
2. Choose **New API Role** and create a role with the following privileges:

   - Read Computers
   - Read Computer Inventory Collection

3. Choose **API Clients** > **New API Client**.
4. Assign the API Role created above to the client.
5. Enable the client and note the following credentials:

   - **Client ID**
   - **Client Secret**

6. Identify your **Jamf Pro instance URL** based on your deployment:

   - Jamf Cloud: `https://<instance_name>.jamfcloud.com`
   - On-premises: `https://<your-jamf-server-url>`

7. In AWS Secrets Manager, create a secret and store:

   - Client ID under the key `client_id`
   - Client Secret under the key `client_secret`

For more information, see [Jamf Pro API Overview](https://developer.jamf.com/jamf-pro/docs/jamf-pro-api-overview "https://developer.jamf.com/jamf-pro/docs/jamf-pro-api-overview") on the Jamf developer website.

## Configuring the CloudWatch Pipeline

To configure the pipeline to read data, choose Jamf Pro as the data source. Provide the required information such as the Jamf Pro hostname (`hostname`), Client ID (`client_id`), and Client Secret (`client_secret`). After you create and activate the pipeline, computer inventory data from Jamf Pro will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and Jamf Pro events that map to Device Inventory Info (5001).

### Device Inventory Info (5001)

**[Computer Inventory](https://developer.jamf.com/jamf-pro/reference/get_v3-computers-inventory "https://developer.jamf.com/jamf-pro/reference/get_v3-computers-inventory")** – Contains structured per-device records for managed Macs including hardware specifications, OS version, security posture (FileVault/SIP/Gatekeeper status), installed software, last contact time, and assigned user information.

###### Note

Events that do not match any OCSF event classes listed above – such as custom or newly introduced Jamf Pro event types that have not yet been mapped – are automatically passed through and sent directly to the configured sink in their original format without additional processing.
