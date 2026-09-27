

# Source configuration for Google Workspace
<a name="google-workspace-source-config"></a>

## Supported API and platform versions
<a name="google-workspace-supported-versions"></a>


| Component | Version | Notes | 
| --- | --- | --- | 
| Admin SDK Reports API | v1 | Activity reports for all supported applications | 
| Alert Center API | v1beta1 | Security alerts and investigation data | 
| OCSF Schema | v1.5.0 | Open Cybersecurity Schema Framework mapping | 
| OAuth 2.0 | 2 | Service account authentication with a JSON Web Token (JWT) | 

## Prerequisites
<a name="google-workspace-prerequisites"></a>

Before you begin, make sure you have the following:
+ An active Google Workspace subscription. Individual applications and reports can require specific Google Workspace editions. For more information, see [Known platform limitations](google-workspace-pipeline-setup.md#google-workspace-limitations).
+ A Google Cloud project.
+ A Google Cloud service account with domain-wide delegation enabled.
+ An administrator email address available for impersonation.
+ The Admin SDK Reports API enabled in the Google Cloud console.
+ The Alert Center API enabled in the Google Cloud console.
+ Super-admin access to the Google Admin console for domain-wide delegation authorization.
+ An AWS account with permissions to create and manage CloudWatch pipelines. For more information, see [API caller permissions](pipeline-iam-reference.md#api-caller-permissions).
+ An AWS account with permissions to create and update secrets in AWS Secrets Manager, and a source role that can retrieve the stored credentials. For more information, see [Third-party sources (API Pull)](pipeline-iam-reference.md#third-party-api-pull).
+ An AWS account with permissions to create and manage CloudWatch Logs log groups. For more information, see [CloudWatch Logs API operations and required permissions for actions](permissions-reference-cw.md#cwl-permissions-table).
+ The service account JSON key file that you create during Google Workspace configuration.

## Configure Google Workspace
<a name="google-workspace-product-configuration"></a>

1. Navigate to the [Google Cloud console](https://console.cloud.google.com/), log in to your Google account, and choose your organization name in the navigation bar.

1. In the **Select a resource** window, choose **New Project**.

1. In the **New Project** window, enter your project name, and choose **Create**.

1. In the Google Cloud console, open the menu in the upper-left corner.

1. Navigate to **APIs & Services** > **Library**.

1. Choose the search bar.

1. Search for and select **Admin SDK API**. Repeat this step for **Google Workspace Alert Center API**.

1. For both the Admin SDK API and Google Workspace Alert Center API, choose **Enable**.

1. Navigate to **IAM & Admin** > **Service Accounts**.

1. Choose **Create Service Account**.

1. Name your service account, choose **Create and Continue**, and then choose **Done**.

1. On the **Service Accounts** page, choose your new service account.

1. On the service account details page, create a JSON key:

   1. Choose the **Keys** tab, and then choose **Add Key**.

   1. Choose **Create new key**.

   1. Select **JSON**, and then choose **Create**.

   1. Save the JSON key file to a secure directory. You use the credentials from this file when you configure the pipeline.

1. Navigate to the [Google Admin console](https://admin.google.com/), and then navigate to **Security** > **Access and data control** > **API controls**.

1. Under **Domain wide delegation**, choose **Manage Domain Wide Delegation**.

1. Choose **Add new** to add a new client ID.

1. In the **Add a new client ID** window, complete the following steps:

   1. For **Client ID**, enter the value of the `client_id` key from the service account JSON key file.

   1. For **OAuth scopes**, add the following comma-delimited scopes:
      + [Admin Audit Read Only](https://www.googleapis.com/auth/admin.reports.audit.readonly)
      + [Alerts](https://www.googleapis.com/auth/apps.alerts)

   1. Choose **Authorize**.

## Integrating with Google Workspace
<a name="google-workspace-integration"></a>

1. **Store credentials in AWS Secrets Manager**

   1. Open the AWS Secrets Manager console.

   1. Choose **Store a new secret** > **Other type of secret**.

   1. Add the following key-value pairs:
      + `private_key` – The `private_key` value from the service account JSON key file.
      + `client_email` – The `client_email` value from the service account JSON key file.
      + `subject` – The administrator email address to impersonate.

   1. Name the secret, for example, `google-workspace/pipeline-credentials`.

1. **Create the destination CloudWatch Logs log group**

   1. Open the CloudWatch console.

   1. Navigate to **Logs** > **Log groups** > **Create log group**.

   1. Choose a descriptive name, for example, `/aws/cloudwatch/pipelines/google-workspace`.

1. **Create the source IAM role**

   Create an IAM role with the required permissions. For information about the required policies and permissions, see [CloudWatch pipelines IAM policies and permissions](pipeline-iam-reference.md).

1. **Create the CloudWatch pipeline**

   1. Open the CloudWatch console, and navigate to **Pipelines**.

   1. Choose **Google Workspace** as the data source.

   1. Configure authentication with `client_email`, `private_key` from AWS Secrets Manager, and `subject`, which is the administrator email address to impersonate.

   1. Select the destination log group.

   For the complete pipeline YAML configuration and parameter reference, see [CloudWatch pipelines configuration for Google Workspace](google-workspace-pipeline-setup.md).

1. **Add the CloudWatch Logs resource policy**

   The resource policy behavior depends on whether the log group is new or already exists:
   + **New log group (first-time use)** – The resource policy is created automatically. No action is required.
   + **Existing log group (reusing)** – If the selected log group already has a resource policy, the console displays the following warning:

     *Resource Policy Detected: The log group you selected already has a resource policy. Please verify that this policy includes permissions for pipelines to write to the destination log group. You may need to modify the existing resource policy to add the necessary permissions.*

     In this case, add the [CloudWatch Logs resource policy](pipeline-iam-reference.md#resource-policies) within 5 minutes of pipeline creation, before the pipeline becomes active. Review and update the existing resource policy to make sure that it includes the required pipeline write permissions.
**Note**  
If you create the pipeline using the AWS CLI or API, a resource policy is never created automatically, regardless of whether the log group is new or existing. You must create the [CloudWatch Logs resource policy](pipeline-iam-reference.md#resource-policies) manually before the pipeline becomes active.

1. **Verify data flow**

   1. Wait a few minutes for the initial data pull.

   1. Check the destination log group for incoming events.

   1. Monitor [pipeline metrics](pipelines-metrics.md) for successful ingestion.

## Authenticating with Google Workspace
<a name="google-workspace-authentication"></a>

Google Workspace uses OAuth 2.0 with service account authentication and domain-wide delegation. The pipeline performs the following actions:

1. Signs a JWT with the service account private key.

1. Exchanges the JWT for an access token through Google's OAuth endpoint.

1. Impersonates the specified administrator account to access organization-wide data.

## Supported Open Cybersecurity Schema Framework event classes
<a name="google-workspace-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0. Each application maps to one or more OCSF event classes.


| Event type | Application ID | OCSF class | Description | 
| --- | --- | --- | --- | 
| [Login Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/login) | login | Authentication (3002), Account Change (3001), Detection Finding (2004), Base Event (0) | User authentication attempts, MFA challenges, login success or failure, suspicious login flags, and password changes | 
| [SAML Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/saml) | saml | Authentication (3002) | SAML-based SSO authentication attempts for federated applications | 
| [Token Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/token) | token | API Activity (6003), User Access Management (3005) | OAuth token grants, revocations, and third-party application access | 
| [Drive Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/drive) | drive | File Hosting Activity (6006) | File sharing, downloads, deletions, and permission changes | 
| [Gmail Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/gmail) | gmail | Email Activity (4009) | Message delivery events, including messages sent and received | 
| [Context-Aware Access](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/context-aware-access) | context\_aware\_access | Detection Finding (2004) | Zero-trust policy enforcement events, including access denials, warn-mode events, and policy evaluation errors | 
| [Rules Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/rules) | rules | Detection Finding (2004), Data Security Finding (2006) | DLP and activity rules triggered by Google's built-in rule engine | 
| [Access Transparency](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/access-transparency) | access\_transparency | API Activity (6003) | Google employee access to customer data, available with the Frontline Plus, Enterprise Plus, Education Standard, Education Plus, and Enterprise Essentials Plus editions | 
| [User Accounts Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/user-accounts) | user\_accounts | Account Change (3001) | 2-step verification enrollment or disablement and recovery information changes | 
| [LDAP Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/ldap) | ldap | API Activity (6003), Authentication (3002) | LDAP authentication operations against Secure LDAP | 
| [Takeout Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/takeout) | takeout | Web Resources Activity (6001) | Bulk data export and download operations through Google Takeout | 
| [Vault Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/vault) | vault | Entity Management (3004) | eDiscovery and retention operations for compliance monitoring | 
| [Directory Sync Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/directory-sync) | directory\_sync | Entity Management (3004) | Active Directory and LDAP directory synchronization operations | 
| [Alert Center](https://developers.google.com/workspace/admin/alertcenter/reference/rest/v1beta1/alerts) | Not applicable | Detection Finding (2004) | Security alerts, including phishing reclassifications, government-backed attack warnings, leaked passwords, and suspicious sharing | 

### Ingestion-only event types
<a name="google-workspace-ingestion-only-events"></a>

The following event types are ingested for completeness but do not have OCSF class mappings:


| Event type | Application ID | Description | 
| --- | --- | --- | 
| [Calendar Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/calendar) | calendar | Calendar ACL changes and event modifications | 
| [Chat Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/chat) | chat | Space management, uploads, and message operations | 
| [Meet Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/meet) | meet | Video call events and abuse reports | 
| [Chrome Activity](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/chrome) | chrome | ChromeOS logins, unsafe browsing events, and device management | 