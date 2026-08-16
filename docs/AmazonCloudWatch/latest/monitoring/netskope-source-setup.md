# Source configuration for Netskope

## Integrating with Netskope

Netskope is a cloud-native Security Service Edge (SSE) and SASE platform that
provides real-time data and threat protection for cloud services, websites, and
private applications. CloudWatch Pipeline uses the Netskope REST API v2 endpoints to
retrieve security events and alerts from your Netskope tenant. The REST API v2
provides access to security event and alert logs through dedicated endpoints for
each log type: application, page, network, infrastructure, audit, incident,
endpoint, and alert. Alert logs cover threat detections and policy violations
across alert types such as DLP, malware, malsite, policy, compromised credential,
and UBA.

## Authenticating with Netskope

To read Netskope event and alert logs, the pipeline needs to authenticate with
your tenant using a REST API v2 token issued through a Service Account under the
RBACv3 framework. Follow these steps to create a Service Account and generate an
API token:

1. Log in to your Netskope Admin Console at
   https://<your-tenant>.goskope.com.
2. Navigate to **Settings** >
   **Administration** >
   **Administrators & Roles**.
3. Choose the **Roles** tab, then choose
   **Create Role**.
4. Enter a Role Name (for example, "CloudWatch-API-Role") and configure
   the following functional area permissions:

   - **Steering**: Application Events,
     Page Events, Network Events, Infrastructure Events, Incident Events,
     Endpoint Events, Alerts — all set to View.
   - **Administration**: Audit Log —
     set to View.
   - **Access Control**:
     Infrastructure — set to View.
   - **DLP**: DLP Incident — set to
     View.

5. Choose **Save** to create the
   role.
6. Choose the **Administrators** tab, then
   choose the **Service Accounts**
   button.
7. Choose **New Service Account** and
   configure:

   - **Service Account Name**: Enter a
     descriptive name (for example,
     "CloudWatch-Collector").
   - **Role**: Select the role created
     in step 5 (for example,
     "CloudWatch-API-Role").
   - **Expire In**: Set an appropriate
     expiration period (for example, 365 days).

8. Choose **Create**. A dialog displays the
   generated REST API token. Copy this token immediately — it will not be shown
   again.
9. In AWS Secrets Manager, create a secret and store the API
   token.

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read event and alert logs from Netskope, choose
Netskope as the data source. Fill in the required information such as your tenant
hostname and the AWS Secrets Manager secret ARN for your credentials where api\_token is
stored. After you create the pipeline, data will be available in the selected CloudWatch Logs
log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and transforms the following
events that map to Authentication (3002), Entity Management (3004), Account Change
(3001), Network Activity (4001), Detection Finding (2004), Data Security Finding
(2006), File Hosting Activity (6006), and Device Inventory Info (5001). Events that
are not listed but pulled are not mapped to OCSF and will be forwarded to the sink
as raw logs.

**Authentication (3002)** contains the following
events from two event types:

Application Events, using the "activity" field. The supported activity values
are:

- Login Attempt
- Login Failed
- Login Successful
- Logout
- Other Events which contain the keyword "login"

Audit Events, using the "audit\_log\_event" field. The supported audit\_log\_event
values are:

- Login Failed
- Login Successful
- Logout Successful
- SSO Login Failed
- SSO Login Successful
- SSO Login Successful by Netskope Support
- SSO Login Failed by Netskope Support
- Admin logged out because of successive login failures

**Entity Management (3004)** contains the following
events from Audit Events:

- Created new inline policy
- Set dedicated egress ip policy
- Created new rbi template
- Created new tunnel group
- Created new introspection policy
- Next Gen CASB API instance created
- Created a new Next Gen CASB API policy
- Next Gen CASB API retroscan created
- Edited inline policy
- Update default actions for inline policies
- Edited rbi template
- Edited tunnel group
- Edit introspection policy record
- Next Gen CASB API instance updated
- Edited Next Gen CASB API policy
- Next Gen CASB API retroscan edited
- Deleted inline policy
- Deleted rbi template
- Deleted tunnel group
- Deleted introspection policy
- Next Gen CASB API instance deleted
- Deleted Next Gen CASB API policy
- Next Gen CASB API retroscan deleted
- Pushed inline policy
- Pushed rbi template
- Pushed tunnel groups
- Applied Phoenix policy record(s)
- Pushed Introspection policies
- Pushed Next Gen CASB API policies
- Next Gen CASB API retroscan stopped
- Next Gen CASB API retroscan paused

**Account Change (3001)** contains the following
events from Audit Events:

- Created new admin
- Added SSO Admin
- Created new support admin
- Enabled admin
- Password Change Failed Attempt
- Password Change Successful
- Reset password
- Disabled admin
- Deleted admin
- Deleted Netskope SSO admin
- Enabled Netskope Support SSO
- Disabled Netskope Support SSO
- Unlocked admin
- Edited SSO Admin Record
- Edit admin record
- Updated admin settings

**Network Activity (4001)** contains the following
events:

Network Events are categorized using the record\_type="network" and "action"
fields. The supported "action" values are:

- Allow
- Block
- Bypass
- Closed
- Idle Timeout
- Proceed

All events with the value of /record\_type = "connection" are also included.

**Detection Finding (2004)** contains the following
events:

Alerts are categorized using the "alert\_type" and "alert" fields, where the
"alert" field value is set to "yes". The supported "alert\_type" values are:

- Compromised Credential
- Malsite
- Malware
- Policy
- UBA
- C2

**Data Security Finding (2006)** contains the
following events:

- /record\_type = "alert" and /alert\_type = "DLP"
- /record\_type = "incident"
- /record\_type = "epdlp" and /type = "endpoint"

**File Hosting Activity (6006)** contains the
following events:

Application Events are categorized using the "activity" field, with the "alert"
field value set to "no". The supported activity values are:

- Browser File Upload
- Attach
- Create
- Download
- Download All
- Download Installer
- Edit
- Quick Edit
- Insert
- Delete
- Delete All
- Copy
- Move
- Preview
- Formshare
- File Share Access
- Upload
- Share
- Post
- View
- Archive
- Bluetooth File Transfer
- Detach
- Print
- Publish

**Device Inventory Info (5001)** contains the
following events:

All infrastructure logs with record\_type="infrastructure".
