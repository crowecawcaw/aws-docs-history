

# Stream session admin shell
<a name="troubleshoot-admin-shell-guide"></a>

Use the [CreateStreamSessionAdminShell](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionAdminShell.html) API to connect to the live runtime environment of your stream session. Use the terminal connection to troubleshoot application issues by inspecting logs, checking running processes, examining GPU utilization, and debugging your application state in real time.

**Important**  
The admin shell grants the same level of access as the applications running on the stream session, which can include user input, screen images, and application data files. Grant `gameliftstreams:CreateStreamSessionAdminShell` permissions only to trusted IAM identities.

## Prerequisites
<a name="troubleshoot-admin-shell-prerequisites"></a>

Before you connect to a stream session with the admin shell, install the AWS Systems Manager Session Manager plugin for the AWS Command Line Interface. The plugin is required to open terminal connections. For installation instructions, see [Install the Session Manager plugin for the AWS Command Line Interface](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html).

The code example below requires [jq](https://jqlang.github.io/jq/), a command-line JSON processor, to extract values from the API response.

The stream session must be in one of the following statuses: `ACTIVE`, `CONNECTED`, `PENDING_CLIENT_RECONNECTION`, or `RECONNECTING`.

## Connect using the Session Manager plugin for the AWS Command Line Interface
<a name="troubleshoot-admin-shell-connect"></a>

Use the AWS CLI to request admin shell access credentials, then use the [Session Manager plugin for the AWS Command Line Interface](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) to establish the terminal connection. Use the following code example to connect. Replace `STREAM_GROUP_ID`, `STREAM_SESSION_ID`, and `REGION` with your values.

**AWS Command Line Interface with Bash script**

```
#!/bin/bash
# GameLift Streams session with admin shell script
# This script sets up a terminal connection to an Amazon GameLift Streams session
# using the AWS Systems Manager Session Manager Plugin

# Stream group ARN or ID owning the session
STREAM_GROUP_ID="arn:aws:gameliftstreams:us-west-2:123456789012:streamgroup/sg-1AB2C3De4"

# Stream session ARN or ID to connect to
STREAM_SESSION_ID="arn:aws:gameliftstreams:us-west-2:123456789012:streamsession/sg-1AB2C3De4/44wOYoDXlRbtf"

# AWS Region where you created the stream group (primary location)
REGION="us-west-2"

# Request admin shell access
SESSION_ACCESS=$(aws gameliftstreams create-stream-session-admin-shell \
    --identifier "${STREAM_GROUP_ID}" \
    --stream-session-identifier "${STREAM_SESSION_ID}" \
    --region "${REGION}" \
    --output json)

# Extract session ID and connect using Session Manager plugin
SESSION_ID=$(echo "$SESSION_ACCESS" | jq -r .SessionId)

# Connect using the API response (the plugin extracts StreamUrl and TokenValue)
# The connection URL expires 60 seconds after the API response.
session-manager-plugin \
    "$SESSION_ACCESS" \
    "${REGION}" \
    "StartSession" \
    "" \
    "{\"Target\":\"$SESSION_ID\"}" \
    "https://ssm.${REGION}.api.aws"
```

**Tip**  
To find active stream sessions for a stream group, use the [ListStreamSessions](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessions.html) API operation or check the Amazon GameLift Streams console.

If you have trouble establishing a terminal connection, see [Stream session admin shell issues](#troubleshoot-admin-shell) for solutions to common errors.

## Stream session admin shell issues
<a name="troubleshoot-admin-shell"></a>

This section identifies potential causes and solutions for issues related to using the [CreateStreamSessionAdminShell](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionAdminShell.html) API to open a secure terminal connection into the live runtime environment of your stream session.

### Terminal connection is not yet available
<a name="troubleshoot-admin-shell-not-ready"></a>

If you call `CreateStreamSessionAdminShell` and receive a `StreamSessionAccessNotReadyException` (HTTP 409), the terminal connection to the live runtime environment of your Amazon GameLift Streams session cannot yet be provisioned.

To resolve this issue:
+ Wait a few seconds and retry the request. The terminal connection typically becomes available shortly after the stream session enters the `ACTIVE` state.
+ If the error persists after repeated retries, verify that the stream session is still in one of the following states: `ACTIVE`, `CONNECTED`, `PENDING_CLIENT_RECONNECTION`, or `RECONNECTING` by calling [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html).

### Access denied when creating an admin shell
<a name="troubleshoot-admin-shell-access-denied"></a>

If you call `CreateStreamSessionAdminShell` and receive an `AccessDeniedException` (HTTP 403) error, the calling IAM identity does not have the required permissions. To resolve this issue, verify that the IAM identity has the `gameliftstreams:CreateStreamSessionAdminShell` permission for the target stream group resource.

### Cannot connect to a stream session that is not active
<a name="troubleshoot-admin-shell-not-active"></a>

If you call `CreateStreamSessionAdminShell` and receive a `ResourceNotFoundException` (HTTP 404) or `ValidationException` (HTTP 400) error, verify that the stream group hosting the stream session is in `ACTIVE` state and the stream session is in one of the following states: `ACTIVE`, `CONNECTED`, `PENDING_CLIENT_RECONNECTION`, or `RECONNECTING`.

To resolve this issue:
+ Verify the stream group state by calling [GetStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamGroup.html).
+ Verify the stream session state by calling [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html).
+ If the session recently started, wait until the session status transitions to `ACTIVE` before requesting a terminal connection.

### StreamUrl has expired
<a name="troubleshoot-admin-shell-url-expired"></a>

If you connect to the WebSocket endpoint returned by `CreateStreamSessionAdminShell` and receive a connection error, the `StreamUrl` has expired. It is valid for 60 seconds after you receive it. If you do not establish the connection within that time, the URL expires.

To resolve this issue:
+ Call `CreateStreamSessionAdminShell` again to obtain a new `StreamUrl`, `SessionId`, and `TokenValue`.
+ Establish the connection within 60 seconds after receiving the response.

### Session Manager plugin is not installed
<a name="troubleshoot-admin-shell-plugin-missing"></a>

If you attempt to connect using the credentials returned by `CreateStreamSessionAdminShell` and the connection fails with a message indicating the Session Manager plugin is missing, you need to install the AWS Systems Manager Session Manager plugin for the AWS CLI.

To resolve this issue:
+ Install the Session Manager plugin for the AWS CLI. For installation instructions, see [Install the Session Manager plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) in the *AWS Systems Manager User Guide*.
+ Verify the plugin is installed by running `session-manager-plugin` from your terminal.

### Admin shell closes unexpectedly
<a name="troubleshoot-admin-shell-closes"></a>

If your terminal connection disconnects abruptly during use, it might have closed for one of the following reasons:
+ The terminal connection is scoped to the stream session lifecycle and ends when the stream session transitions to a `TERMINATED` or `ERROR` state.
+ The terminal connection exceeded its maximum duration of 30 minutes.
+ The terminal connection exceeded its idle timeout of 15 minutes.

To resolve this issue:
+ Verify that the stream session is not in a `TERMINATED` or `ERROR` state by calling [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html).
+ If the terminal connection timed out due to idle or maximum duration, call `CreateStreamSessionAdminShell` again to open a new terminal connection.
+ If the stream session has ended, start a new stream session to open a new terminal connection.