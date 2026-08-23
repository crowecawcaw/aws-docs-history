# Source configuration for Salesforce ELF

## Prerequisites

Before you begin, make sure you have the following:

- A Salesforce account with the EventLogFile feature enabled
- An AWS account with [permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions") to create and manage CloudWatch Pipelines
- An AWS account with permissions to create and manage Amazon S3 buckets, AWS Secrets Manager secrets, and IAM roles

## Integrating with Salesforce ELF

To integrate Salesforce ELF with CloudWatch Logs, you must configure a pipeline. First, set up a Salesforce account and an AWS Secrets Manager secret with required authentication credentials to receive data from Salesforce. Then, configure the CloudWatch pipeline to ingest the data from your source into CloudWatch Logs.

Salesforce ELF exports 50+ event types through [EventLogFile](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm") (CSV) and [SetupAuditTrail](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_setupaudittrail.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_setupaudittrail.htm") (JSON) using the Salesforce REST API, which delivers logs directly to the configured sink (CloudWatch Logs).

## Instructions to set up Salesforce account

1. **Create Salesforce Account**

   - Go to the [Salesforce developer sign-up page](https://developer.salesforce.com/signup "https://developer.salesforce.com/signup").
   - Register with your name, email, and a unique username (email format).
   - Verify your email and set your password.
   - Note your instance URL (for example, `https://yourorg-dev-ed.my.salesforce.com`) – this is the `instance_url` for pipeline configuration.

2. **Create an External Client App**

   - In **Setup**, search **External Client App Manager** in Quick Find.
   - Choose **New External Client App**.
   - Fill in **App Name** (for example, "CloudWatch-Collector") and **Contact Email**.
   - Under **API (Enable OAuth Settings)**, check **Enable OAuth**.
   - Set **Callback URL**: `https://login.salesforce.com/services/oauth2/callback`
   - Move these OAuth Scopes from Available to Selected: `Full access (full)`, `Manage user data through APIs (api)`, `Perform requests at any time (refresh_token, offline_access)`
   - Choose **Create**.

3. **Configure Policies**

   - Open your app in **External Client App Manager**.
   - **Policies** tab > **Edit**.
   - **Permitted Users**: Select "Admin approved users are pre-authorized" > **OK**.
   - **Select Profiles**: Add **System Administrator**.
   - Under **OAuth Flows and External Client App Enhancements**: Check **Enable Client Credentials Flow**.
   - **Run As (Username)**: Enter the System Administrator's username (find it under **Setup > Users**).
   - Choose **Save**.

4. **Get Consumer Key and Secret**

   - Open your app > **Settings** tab > **OAuth Settings**.
   - Choose **Consumer Key and Secret** button (verify identity by email code if prompted).
   - Copy **Consumer Key** (`client_id`) and **Consumer Secret** (`client_secret`).

5. **Create and Assign Permission Set**

   - **Setup > Permission Sets** > **New** (for example, "CloudWatch-Collector-Permissions").
   - **System Permissions > Edit** – enable: **API Enabled**, **View Event Log Files**, **View Setup and Configuration**.
   - **Save**, then **Manage Assignments > Add Assignment** > select the Run-As user > **Assign**.

6. **Enable Event Log File**

   - **Setup > Event Monitoring**.
   - Enable the **Generate event log files** toggle.

7. **Store Credentials in AWS Secrets Manager**

   - In AWS Secrets Manager, choose **Store a new secret** > **Other type of secret**.
   - Add key/value pairs: `client_id` = Consumer Key, `client_secret` = Consumer Secret.
   - Name the secret (for example, `salesforce-credentials`) and copy the ARN.

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read data from Salesforce, choose `salesforce_elf` as the data source. Provide the `instance_url`, `client_id`, and `client_secret`. After creating the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and transforms the following events. Events that are not listed but pulled are not mapped to OCSF and will be forwarded to the sink as raw logs.

### Account Change (3001)

Contains the following [events](https://docs.kratapps.com/setup-audit-trail/reference/ "https://docs.kratapps.com/setup-audit-trail/reference/"):

createduser, createdcustomersuccessuser, createdpartneruser, activateduser, unfrozeuser, changedpassword, resetpassword, deactivateduser, frozeuser, CSPUserDisabled, PRMUserDisabled, PermSetAssign, PermSetAssign\_HasExpiration, PermSetGroupAssign, PermSetLicenseAssign, addeduserpackagelicense, granteduserpackagelicense, enabledForIntegrations, loginasgrantedtopartnerbt, loginasgrantedtosfdc, PermSetUnassign, PermSetUnassign\_HasExpiration, PermSetGroupUnassign, PermSetLicenseUnassign, removeduserpackagelicense, revokeduserpackagelicense, disabledForIntegrations, loginasrevokedtopartnerbt, loginasrevokedtosfdc, insertTwoFactorInfo2, insertTwoFactorWebAuthN, insertAuthenticatorPairing, lightningloginenroll, insertTwoFactorTempCode, deleteTwoFactorInfo2, deleteTwoFactorWebAuthN, deleteAuthenticatorPairing, lightninglogincancel, unlockeduser

### Authentication (3002)

Contains the following [events](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm"):

- Login
- LoginAs
- Logout

### API Activity (6003)

Contains the following [events](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm"):

- ApiTotalUsage
- BulkApi
- BulkApi2
- CompositeApi
- CompositeApiSubrequest
- RestApi
- API
- ContinuationCalloutSummary
- ExternalCrossOrgCallout
- ExternalCustomApexCallout
- ExternalDataSourceCallout
- ExternalODataCallout
- NamedCredential
- MetadataApiOperation

### Datastore Activity (6005)

Contains the following [events](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm"):

- AsynchronousReportRun
- Dashboard
- DatabaseSave
- MultiblockReport
- Report
- ReportExport
- Search
- UniqueQuery

### Detection Finding (2004)

Contains the following [events](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm"):

- BlockedRedirect
- CorsViolation
- CspViolation
- HostnameRedirects
- InsecureExternalAssets
- InsufficientAccess
- TransactionSecurity

### Entity Management (3004)

Contains SetupAuditTrail events for entity creation, modification, deletion, and configuration changes. This includes a large number of Salesforce administrative actions such as creating/deleting Apex classes, custom fields, permission sets, profiles, workflows, and system configuration toggles.

### File Hosting Activity (6006)

Contains the following [events](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm"):

- ContentDistribution
- ContentDocumentLink
- ContentTransfer
- DocumentAttachmentDownloads

### HTTP Activity (4002)

Contains the following [event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_uri.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_uri.htm"):

- URI – user interaction with the web browser UI
