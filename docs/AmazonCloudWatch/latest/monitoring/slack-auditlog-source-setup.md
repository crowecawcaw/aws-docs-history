

# Source configuration for Slack Audit Log
<a name="slack-auditlog-source-setup"></a>

## Integrating with Slack Audit Log
<a name="slack-auditlog-integration"></a>

Slack is a cloud-based collaboration and messaging platform that enables team communication through channels, direct messages, file sharing, and integrations with external applications. CloudWatch pipelines use the Slack APIs (such as Events API and Audit Logs API) to retrieve information about user activities, messages, channel events, app interactions, and administrative actions across your Slack workspace. These APIs provide REST endpoints that allow access to event data, enabling the collection of communication and audit logs from your Slack environment for monitoring and analysis.

## Authenticating with Slack
<a name="slack-auditlog-authentication"></a>

To read Slack audit logs, the pipeline needs to authenticate with your Slack workspace. The plugin supports OAuth API token authentication. Follow these instructions to get started with Slack APIs:

1. Before creating an app, register for the Slack Developer Program by visiting: `https://api.slack.com/developer-program`.

1. Log in to the Slack API portal and navigate to "Your Apps" then "Create New App." Choose "From scratch" and provide an app name and workspace. After creation, note down the Client ID and Client Secret from the "Basic Information" section.

1. Configure OAuth scopes under "OAuth & Permissions." Add required scopes such as `auditlogs:read`, `channels:read`, `groups:read`, `users:read`, and `channels:history` depending on your use case. Install the app to your workspace by choosing the install button in the Slack API portal. After installation, copy the User OAuth Token (starts with `xoxp-`). The `auditlogs:read` scope requires a user OAuth token.

1. In AWS Secrets Manager, create a secret that will hold the Slack token obtained in step 3. The secret's value must be a JSON object with a key that stores the token. Pick any secret name and any key name you prefer, but remember both — the pipeline configuration references them together using the syntax `${{aws_secrets:<secret-name>:<key-name>}}`.

## Configuring the CloudWatch Pipeline
<a name="slack-auditlog-pipeline-config"></a>

When configuring the pipeline to read logs, choose Slack as the data source. Specify the range duration format (for example, PT21H for the last 21 hours) to control the time window of logs retrieved. After you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="slack-auditlog-ocsf-events"></a>

This integration supports OCSF schema version v1.5.0 and events that map to Web Resources Activity (6001), Authentication (3002), Entity Management (3004), Account Change (3001), User Access Management (3005), File Hosting Activity (6006), and Detection Finding (2004). These events are sourced from the Slack AuditLogs API. Events that are not listed are not mapped to OCSF and will be forwarded to the sink as raw logs.

**Web Resources Activity (6001)** contains the following event types:
+ private\_channel\_created
+ private\_channel\_archive
+ private\_channel\_converted\_to\_public
+ private\_channel\_deleted
+ private\_channel\_unarchive
+ public\_channel\_archive
+ public\_channel\_converted\_to\_private
+ public\_channel\_created
+ public\_channel\_deleted
+ public\_channel\_preview
+ public\_channel\_unarchive
+ file\_public\_link\_created
+ file\_public\_link\_revoked
+ huddle\_screenshare\_on
+ huddle\_ended
+ huddle\_knock\_accepted
+ huddle\_participant\_dropped
+ huddle\_participant\_joined
+ huddle\_participant\_left
+ huddle\_started
+ huddle\_screenshare\_off
+ huddle\_transcription\_cancelled
+ huddle\_transcription\_paused
+ huddle\_transcription\_resumed
+ huddle\_transcription\_started
+ huddle\_transcription\_start\_notification
+ slack\_ai\_huddle\_notes\_generated
+ list\_linksharing\_enabled
+ canvas\_linksharing\_enabled
+ list\_linksharing\_disabled
+ canvas\_linksharing\_disabled

**Entity Management (3004)** contains the following event types:
+ external\_shared\_channel\_invite\_accepted
+ external\_shared\_channel\_invite\_approved
+ external\_shared\_channel\_invite\_auto\_revoked
+ external\_shared\_channel\_invite\_created
+ external\_shared\_channel\_access\_upgraded
+ external\_shared\_channel\_disconnect\_and\_archived
+ external\_shared\_channel\_disconnected
+ external\_shared\_channel\_invite\_declined
+ external\_shared\_channel\_invite\_expired
+ external\_shared\_channel\_invite\_revoked
+ channels\_export\_completed
+ channels\_export\_deleted
+ channels\_export\_downloaded
+ channels\_export\_started
+ scheduled\_export\_completed
+ scheduled\_export\_deleted
+ scheduled\_export\_downloaded
+ scheduled\_export\_started
+ manual\_export\_completed
+ manual\_export\_deleted
+ manual\_export\_downloaded
+ manual\_export\_started
+ manual\_user\_export\_downloaded
+ manual\_user\_export\_completed
+ manual\_user\_export\_deleted
+ manual\_user\_export\_started
+ external\_shared\_channel\_connected

**Account Change (3001)** contains the following event types:
+ role\_change\_to\_owner
+ role\_change\_to\_admin
+ role\_change\_to\_guest
+ role\_change\_to\_user
+ role\_removed
+ role\_assigned
+ guest\_created
+ guest\_deactivated
+ guest\_reactivated
+ user\_created
+ user\_deactivated
+ user\_reactivated
+ user\_email\_updated
+ user\_profile\_updated
+ user\_profile\_deleted
+ guest\_expiration\_cleared
+ guest\_expiration\_set
+ guest\_expired
+ user\_force\_upgrade\_non\_compliant\_mobile\_app\_version
+ owner\_transferred
+ service\_owner\_transferred
+ user\_password\_reset\_requested
+ user\_password\_reset\_slack\_security
+ custom\_tos\_accepted
+ user\_session\_settings\_changed
+ role\_added\_to\_usergroup
+ role\_removed\_from\_usergroup

**Authentication (3002)** contains the following event types:
+ bulk\_session\_reset\_by\_admin
+ user\_session\_reset\_by\_admin
+ user\_logout\_non\_compliant\_mobile\_app\_version
+ user\_logout
+ user\_logout\_compromised
+ user\_login
+ user\_login\_failed
+ cli\_login
+ user\_sessions\_reset\_by\_anomaly\_event\_response
+ user\_session\_invalidated

**User Access Management (3005)** contains the following event types:
+ permissions\_assigned
+ user\_channel\_join
+ guest\_channel\_join
+ user\_added\_to\_usergroup
+ workflow\_trigger\_permission\_added
+ workflow\_trigger\_permission\_set
+ app\_resources\_granted
+ app\_resources\_added
+ app\_scopes\_expanded
+ permissions\_removed
+ user\_channel\_leave
+ guest\_channel\_leave
+ user\_removed\_from\_usergroup
+ workflow\_trigger\_permission\_removed
+ role\_modified\_on\_usergroup

**File Hosting Activity (6006)** contains the following event types:
+ file\_deleted
+ file\_download\_blocked
+ file\_downloaded
+ file\_shared
+ file\_uploaded

**Detection Finding (2004)** contains the following event types:
+ file\_malicious\_content\_detected
+ Anomaly