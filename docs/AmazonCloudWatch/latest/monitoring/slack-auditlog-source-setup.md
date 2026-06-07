# Source configuration for Slack Audit Log

## Integrating with Slack Audit Log

Slack is a cloud-based collaboration and messaging platform that enables team
communication through channels, direct messages, file sharing, and integrations
with external applications. CloudWatch pipelines use the Slack APIs (such as Events API
and Audit Logs API) to retrieve information about user activities, messages, channel
events, app interactions, and administrative actions across your Slack workspace.
These APIs provide REST endpoints that allow access to event data, enabling the
collection of communication and audit logs from your Slack environment for monitoring
and analysis.

## Authenticating with Slack

To read Slack audit logs, the pipeline needs to authenticate with your Slack
workspace. The plugin supports OAuth API token authentication. Follow these
instructions to get started with Slack APIs:

1. Before creating an app, register for the Slack Developer Program by
   visiting: `https://api.slack.com/developer-program`.
2. Log in to the Slack API portal and navigate to "Your Apps" then
   "Create New App." Choose "From scratch" and provide an app name and
   workspace. After creation, note down the Client ID and Client Secret from
   the "Basic Information" section.
3. Configure OAuth scopes under "OAuth & Permissions." Add required
   scopes such as `auditlogs:read`, `channels:read`,
   `groups:read`, `users:read`, and
   `channels:history` depending on your use case. Install the app
   to your workspace by choosing the install button in the Slack API portal.
   After installation, copy the User OAuth Token (starts with
   `xoxp-`). The `auditlogs:read` scope requires a
   user OAuth token.
4. In AWS Secrets Manager, create a secret that will hold the Slack token obtained
   in step 3. The secret's value must be a JSON object with a key that stores
   the token. Pick any secret name and any key name you prefer, but remember
   both — the pipeline configuration references them together using the syntax
   `${{aws_secrets:<secret-name>:<key-name>}}`.

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read logs, choose Slack as the data source.
Specify the range duration format (for example, PT21H for the last 21 hours) to
control the time window of logs retrieved. Once you create the pipeline, data will
be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and events that map to
Web Resources Activity (6001), Authentication (3002), Entity Management (3004),
Account Change (3001), User Access Management (3005), File Hosting Activity (6006),
and Detection Finding (2004), and these events are sourced from the Slack AuditLogs
API. Events that are not listed are not mapped to OCSF and will be forwarded to the
sink as raw logs.

**Web Resources Activity (6001)** contains the
following event types:

- private_channel_created
- private_channel_archive
- private_channel_converted_to_public
- private_channel_deleted
- private_channel_unarchive
- public_channel_archive
- public_channel_converted_to_private
- public_channel_created
- public_channel_deleted
- public_channel_preview
- public_channel_unarchive
- file_public_link_created
- file_public_link_revoked
- huddle_screenshare_on
- huddle_ended
- huddle_knock_accepted
- huddle_participant_dropped
- huddle_participant_joined
- huddle_participant_left
- huddle_started
- huddle_screenshare_off
- huddle_transcription_cancelled
- huddle_transcription_paused
- huddle_transcription_resumed
- huddle_transcription_started
- huddle_transcription_start_notification
- slack_ai_huddle_notes_generated
- list_linksharing_enabled
- canvas_linksharing_enabled
- list_linksharing_disabled
- canvas_linksharing_disabled

[Show moreShow less](# "#")
**Entity Management (3004)** contains the following
event types:

- external_shared_channel_invite_accepted
- external_shared_channel_invite_approved
- external_shared_channel_invite_auto_revoked
- external_shared_channel_invite_created
- external_shared_channel_access_upgraded
- external_shared_channel_disconnect_and_archived
- external_shared_channel_disconnected
- external_shared_channel_invite_declined
- external_shared_channel_invite_expired
- external_shared_channel_invite_revoked
- channels_export_completed
- channels_export_deleted
- channels_export_downloaded
- channels_export_started
- scheduled_export_completed
- scheduled_export_deleted
- scheduled_export_downloaded
- scheduled_export_started
- manual_export_completed
- manual_export_deleted
- manual_export_downloaded
- manual_export_started
- manual_user_export_downloaded
- manual_user_export_completed
- manual_user_export_deleted
- manual_user_export_started
- external_shared_channel_connected

[Show moreShow less](# "#")
**Account Change (3001)** contains the following
event types:

- role_change_to_owner
- role_change_to_admin
- role_change_to_guest
- role_change_to_user
- role_removed
- role_assigned
- guest_created
- guest_deactivated
- guest_reactivated
- user_created
- user_deactivated
- user_reactivated
- user_email_updated
- user_profile_updated
- user_profile_deleted
- guest_expiration_cleared
- guest_expiration_set
- guest_expired
- user_force_upgrade_non_compliant_mobile_app_version
- owner_transferred
- service_owner_transferred
- user_password_reset_requested
- user_password_reset_slack_security
- custom_tos_accepted
- user_session_settings_changed
- role_added_to_usergroup
- role_removed_from_usergroup

[Show moreShow less](# "#")
**Authentication (3002)** contains the following
event types:

- bulk_session_reset_by_admin
- user_session_reset_by_admin
- user_logout_non_compliant_mobile_app_version
- user_logout
- user_logout_compromised
- user_login
- user_login_failed
- cli_login
- user_sessions_reset_by_anomaly_event_response
- user_session_invalidated

**User Access Management (3005)** contains the
following event types:

- permissions_assigned
- user_channel_join
- guest_channel_join
- user_added_to_usergroup
- workflow_trigger_permission_added
- workflow_trigger_permission_set
- app_resources_granted
- app_resources_added
- app_scopes_expanded
- permissions_removed
- user_channel_leave
- guest_channel_leave
- user_removed_from_usergroup
- workflow_trigger_permission_removed
- role_modified_on_usergroup

[Show moreShow less](# "#")
**File Hosting Activity (6006)** contains the
following event types:

- file_deleted
- file_download_blocked
- file_downloaded
- file_shared
- file_uploaded

**Detection Finding (2004)** contains the following
event types:

- file_malicious_content_detected
- Anomaly
