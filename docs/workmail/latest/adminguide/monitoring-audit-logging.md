# Monitoring Amazon WorkMail audit logs

You can use audit logs to monitor access to your Amazon WorkMail Organization’s mailboxes.
Amazon WorkMail logs five types of audit events and these events can be published to CloudWatch Logs,
Amazon S3, or Amazon Firehouse. You can use audit logs to monitor user interaction with
your Organization’s mailboxes, authentication attempts, access control rule
evaluation, and perform availability provider calls to external systems and monitor events with personal access tokens. For
information about configuring audit logging, see [Enabling audit logging](audit-logging.md "audit-logging.md").

The following sections describe the audit events logged by Amazon WorkMail, when the events
are transmitted, and information about the event fields.

## Mailbox access logs

Mailbox access events provide information about what action was taken (or
attempted) on which mailbox object. A mailbox access event is generated for
every operation that you attempt to run on an item or folder in a mailbox. These
events are useful for auditing access to mailbox data.

| Field            | Description                                                                                                                                                                                                                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| event_timestamp  | When the event happened, in milliseconds since Unix<br>epoch.                                                                                                                                                                                                                                                                  |
| request_id       | The ID that uniquely identifies the request.                                                                                                                                                                                                                                                                                   |
| organization_arn | The ARN of the & Amazon WorkMail Organization to which the<br>authenticated user belongs.                                                                                                                                                                                                                                      |
| user_id          | The ID of the authenticated user.                                                                                                                                                                                                                                                                                              |
| impersonator_id  | The ID of the impersonator. Present only if the<br>impersonation feature was used for the request.                                                                                                                                                                                                                             |
| protocol         | The protocol used. The protocol can be:<br>`AutoDiscover`, `EWS`,<br>`IMAP`, `WindowsOutlook`,<br>`ActiveSync`, `SMTP`,<br>`WebMail`, `IncomingEmail`, or<br>`OutgoingEmail`.                                                                                                                                                  |
| source_ip        | The source IP address of the request.                                                                                                                                                                                                                                                                                          |
| user_agent       | The user agent that made the request.                                                                                                                                                                                                                                                                                          |
| action           | The action taken on the object, which can be:<br>`read`, `read_hierarchy`,<br>`read_summary`, `read_attachment`,<br>`read_permissions`, `create`,<br>`update`, `update_permissions`,<br>`update_read_state`, `delete`,<br>`submit_email_for_sending`,<br>`abort_sending_email`, `move`,<br>`move_to`, `copy`, or<br>`copy_to`. |
| owner_id         | The ID of the user that owns the object being acted<br>upon.                                                                                                                                                                                                                                                                   |
| object_type      | The object type, which can be: Folder, Message, or<br>Attachment.                                                                                                                                                                                                                                                              |
| item_id          | The ID that uniquely identifies the message that's the<br>subject of the event or that contains the attachment that's<br>the subject of the event.                                                                                                                                                                             |
| folder_path      | The path of the folder being acted upon or the path of the<br>folder containing the item being acted upon.                                                                                                                                                                                                                     |
| folder_id        | The ID that uniquely identifies the folder that's the<br>subject of the event or contains the object that's the<br>subject of the event.                                                                                                                                                                                       |
| attachment_path  | The path of display names to the affected<br>attachment.                                                                                                                                                                                                                                                                       |
| action_allowed   | Whether the action was allowed. Can be true or<br>false.                                                                                                                                                                                                                                                                       |

## Access control logs

Access control events are generated whenever an access control rule is
evaluated. These logs are useful for auditing forbidden access, or debugging
access control configurations.

| Field            | Description                                                                                                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| event_timestamp  | When the event happened, in milliseconds since Unix<br>epoch.                                                                                                          |
| request_id       | The ID that uniquely identifies the request.                                                                                                                           |
| organization_arn | The ARN of the WorkMail Organization to which the<br>authenticated user belongs.                                                                                       |
| user_id          | The ID of the authenticated user.                                                                                                                                      |
| impersonator_id  | The ID of the impersonator. Present only if the<br>impersonation feature was used for the request.                                                                     |
| protocol         | The protocol used, which can be:<br>`AutoDiscover`, `EWS`,<br>`IMAP`, `WindowsOutlook`,<br>`ActiveSync`, `SMTP`,<br>`WebMail`, `IncomingEmail`, or<br>`OutgoingEmail`. |
| source_ip        | The source IP address of the request.                                                                                                                                  |
| scope            | The scope of the rule, which can be:<br>`AccessControl`,<br>`DeviceAccessControl`, or<br>`ImpersonationAccessControl`.                                                 |
| rule_id          | The ID of the matched access control rule. When there are no rules matched, \*rule_id<br>• is not available.                                                           |
| access_granted   | Whether access was allowed. Can be true or false.                                                                                                                      |

## Authentication logs

Authentication events contain information about authentication
attempts.

###### Note

Authentication events are not generated for authentication events through
the Amazon WorkMail WebMail application.

| Field                    | Description                                                                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| event_timestamp          | When the event happened, in milliseconds since Unix<br>epoch.                                                                                                          |
| request_id               | The ID that uniquely identifies the request.                                                                                                                           |
| organization_arn         | The ARN of the WorkMail Organization to which the<br>authenticated user belongs.                                                                                       |
| user_id                  | The ID of the authenticated user.                                                                                                                                      |
| user                     | The username that the authentication was attempted<br>with.                                                                                                            |
| protocol                 | The protocol used, which can be:<br>`AutoDiscover`, `EWS`,<br>`IMAP`, `WindowsOutlook`,<br>`ActiveSync`, `SMTP`,<br>`WebMail`, `IncomingEmail`, or<br>`OutgoingEmail`. |
| source_ip                | The source IP address of the request.                                                                                                                                  |
| user_agent               | The user agent that made the request.                                                                                                                                  |
| method                   | The auth method. Currently, only basic is<br>supported.                                                                                                                |
| auth_successful          | Whether the auth attempt was successful. Can be true or<br>false.                                                                                                      |
| auth_failed_reason       | The reason for auth failure. Present only if auth<br>failed.                                                                                                           |
| personal_access_token_id | The ID of the personal access token used for authentication.                                                                                                           |

## Personal access token logs

A personal access token (PAT) event is generated for every attempt in creating or deleting a personal access token. Personal access token events provide information about whether users successfully create personal access tokens. The personal access token logs are useful for auditing end users creating and deleting their own PATs.
User login with personal access tokens will generate events in the existing Authentication logs. For more information, see [Authentication logs](monitoring-audit-logging.md#authentication-log "monitoring-audit-logging.md#authentication-log") .

| Field            | Description                                                                   |
| ---------------- | ----------------------------------------------------------------------------- |
| event_timestamp  | When the event happened, in milliseconds since Unix epoch.                    |
| request_id       | The ID that uniquely identifies the request.                                  |
| organization_arn | The ARN of the WorkMail Organization to which the authenticated user belongs. |
| user_id          | The ID of the authenticated user.                                             |
| user             | The username of the user who took this action.                                |
| protocol         | The protocol used through the action took place, which can be: webapp         |
| source_ip        | The source IP address of the request.                                         |
| user_agent       | The user agent that made the request.                                         |
| action           | The action of the personal access token, which can be: create or delete.      |
| name             | The name of the personal access token.                                        |
| expires_time     | The date when the personal access token expires.                              |
| scopes           | The scopes of the personal access token permissions on mailbox.               |

## Availability provider logs

Availability provider events are generated for every availability request Amazon WorkMail
does on your behalf to your configured availability provider. These events are
useful for debugging your availability provider configuration.

| Field                         | Description                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- |
| event_timestamp               | When the event happened, in milliseconds since Unix<br>epoch.                                                 |
| request_id                    | The ID that uniquely identifies the request.                                                                  |
| organization_arn              | The ARN of the WorkMail Organization to which the<br>authenticated user belongs.                              |
| user_id                       | The ID of the authenticated user.                                                                             |
| type                          | The type of availability provider being invoked, which can<br>be: `EWS` or `LAMBDA`.                          |
| domain                        | The domain for which availability is obtained.                                                                |
| function_arn                  | The ARN of the invoked Lambda, if type is LAMBDA.<br>Otherwise, this field is not present.                    |
| ews_endpoint                  | The<br>EWS endpoint is type is EWS. Otherwise,<br>this field is not present.                                  |
| error_message                 | The message describing the cause of the failure. If the<br>request was successful, this field is not present. |
| availability_event_successful | Whether the availability request was served<br>successfully.                                                  |
