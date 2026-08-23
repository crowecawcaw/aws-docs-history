# Source configuration for Salesforce RTEM

## Prerequisites

Before you begin, make sure you have the following:

- A Salesforce account with the Event Monitoring feature enabled
- An AWS account with [permissions](pipeline-iam-reference.md#api-caller-permissions "pipeline-iam-reference.md#api-caller-permissions") to create and manage CloudWatch Pipelines
- An AWS account with permissions to create and manage Amazon S3 buckets, AWS Secrets Manager secrets, and IAM roles

## Integrating with Salesforce RTEM

To integrate Salesforce RTEM with CloudWatch Logs, you must configure a pipeline. First, set up a Salesforce account and an AWS Secrets Manager secret with required authentication credentials to receive data from Salesforce. Then, configure the CloudWatch pipeline to ingest the data from your source into CloudWatch Logs.

Salesforce RTEM streams 19 default [RTEM channels](https://developer.salesforce.com/docs/platform/pub-sub-api/guide/supported-event-types.html "https://developer.salesforce.com/docs/platform/pub-sub-api/guide/supported-event-types.html") plus optional CDC and custom Platform Events through the [Pub/Sub API](https://developer.salesforce.com/docs/platform/pub-sub-api/overview "https://developer.salesforce.com/docs/platform/pub-sub-api/overview"), which delivers logs directly to the configured sink (CloudWatch Logs).

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
   - Move these OAuth Scopes from Available to Selected: `Full access (full)`, `Perform requests at any time (refresh_token, offline_access)`, `Access Pub/Sub API (pubsub_api)`
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
   - **System Permissions > Edit** – enable: **API Enabled**, **View Real-Time Event Monitoring Data**.
   - **Save**, then **Manage Assignments > Add Assignment** > select the Run-As user > **Assign**.

6. **Enable Event Storage and Streaming**

If storage is not enabled for an event type, the Pub/Sub API subscription connects but receives zero events silently.

    * **Setup > Event Manager**.
    * For each event type, choose the dropdown > **Enable Storage and Streaming**.

7. **Find Your Organization ID**

    * **Setup > Company Information**.
    * Copy the **Salesforce.com Organization ID** (15 or 18 character alphanumeric, for example, `00D5e000003TIrB`).

8. **Store Credentials in AWS Secrets Manager**

    * In AWS Secrets Manager, choose **Store a new secret** > **Other type of secret**.
    * Add key/value pairs: `client_id` = Consumer Key, `client_secret` = Consumer Secret.
    * Name the secret (for example, `salesforce-credentials`) and copy the ARN.

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read data from Salesforce, choose `salesforce_rtem` as the data source. Provide the `instance_url`, `org_id`, and use the `client_id` and `client_secret`. After creating the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and transforms the following events. Events not listed are not mapped to OCSF and are forwarded to the sink as raw logs.

### Authentication (3002)

Covers the following [events](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_objects_monitoring.htm "https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_objects_monitoring.htm"):

- LoginEventStream
- LoginAsEventStream
- LogoutEventStream

### File Hosting Activity (6006)

Covers the following [event](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_fileevent.htm "https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_fileevent.htm"):

- FileEvent

### API Activity (6003)

Covers the following [events](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_objects_monitoring.htm "https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_objects_monitoring.htm"):

- BulkApiEventStream
- ApiEventStream

### Datastore Activity (6005)

Covers the following [events](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_objects_monitoring.htm "https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_objects_monitoring.htm"):

- ReportEvent
- ListViewEventStream
