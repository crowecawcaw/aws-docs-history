

# Sign-in session management
<a name="oauth-sign-in-session-management"></a>

## Configurable sign-in sessions
<a name="oauth-sign-in-session-configurable"></a>

Previously, IAM roles had a fixed 12-hour maximum authentication duration for AWS CLI and OAuth-based access. With sign-in sessions, authentication duration is configurable at the role or user level, up to 90 days.

Access tokens remain short-lived (one hour), and refresh tokens rotate continuously. A longer sign-in session does not create long-lived AWS credentials. This makes it a safer alternative to long-lived access keys for workloads that run for extended periods.

## Availability
<a name="oauth-sign-in-session-availability"></a>

Configuration is available on IAM roles and IAM users. Sign-in sessions are supported for the AWS CLI, the AWS MCP Server, and other OAuth-enabled applications, including AI agents.

AWS Management Console sessions are not supported and continue to follow their existing session duration limits.

## How sign-in sessions work
<a name="oauth-sign-in-session-how-it-works"></a>

Each time you run `aws login`, AWS Sign-In creates a sign-in session with a unique session ID. The session ID ties together every access token, refresh token, and AWS credential pair issued from that login.

During the session, AWS Sign-In issues short-lived OAuth access tokens that expire after one hour. When an access token expires, the application automatically uses a refresh token to obtain a new one, with no user interaction. The refresh token rotates continuously throughout the sign-in session.

## Sign-in session duration compared to IAM role maximum session duration
<a name="oauth-sign-in-session-vs-role-max-duration"></a>

Sign-in session duration controls how long the authentication session backing the OAuth flow remains active (authentication continuity). IAM role maximum session duration controls how long temporary AWS STS credentials remain valid after a role is assumed.

The two are independent. A single sign-in session can span many AWS STS credential issuances and expirations over its lifetime.

## Configuring sign-in session duration
<a name="oauth-sign-in-session-configuring"></a>

Sign-in session duration is configured on an IAM role or IAM user. The default for existing roles remains 12 hours. New accounts and Starter Home customers have a default of 90 days for supported developer and agentic experiences.

A new duration applies to sign-in sessions established after the change. Existing active sessions retain their current expiration.

To configure sign-in session duration on a role, see [Update the sign-in duration for a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-settings.html#id_roles_update-signin-duration).

## Using sign-in sessions with the AWS CLI
<a name="oauth-sign-in-session-using-cli"></a>

After sign-in session duration is configured for your IAM role, new sessions established through `aws login` use the configured duration.

After authentication, the AWS CLI holds a refresh token that automatically renews your access token every hour. You can keep using the AWS CLI for the duration of your sign-in session without reauthenticating. For example, you can run the following commands.

```
aws s3 ls
aws ec2 describe-instances
```

The refresh token is stored securely and encrypted at rest. It is never exposed directly to the AWS CLI or SDK. The AWS CLI receives only short-lived credentials on demand.

## Using sign-in sessions with MCP servers
<a name="oauth-sign-in-session-using-mcp"></a>

For MCP clients, sign-in sessions work automatically after the duration is configured on your IAM role. The next time a user authorizes an MCP client through AWS Sign-In, the session lasts for the configured duration. No changes are required to the agent or MCP server configuration.

## Managing active sign-in sessions
<a name="oauth-sign-in-session-managing"></a>

You can use the AWS CLI to list, inspect, and revoke active sign-in sessions.

To list active sessions for a role, run the following command.

```
aws signin list-sessions --principal-arn arn:aws:iam::123456789012:role/DeveloperRole
```

To get details for a specific session, run the following command.

```
aws signin get-session --session-arn arn:aws:signin:us-east-1:123456789012:session/abc123-example
```

To revoke a specific session, run the following command.

```
aws signin batch-revoke-sessions --session-arns arn:aws:signin:us-east-1:123456789012:session/abc123-example
```

**Note**  
When a sign-in session is revoked, revocation might take up to one hour to take effect. After revocation, the session can no longer be used to obtain new access tokens, and users or applications must reauthenticate. Revocation applies only to the targeted session and does not affect other active sessions for the same role.

## Governance and organizational controls
<a name="oauth-sign-in-session-governance"></a>

You can govern sign-in session duration using IAM policies and service control policies (SCPs).

### Using IAM policies with sign-in sessions
<a name="oauth-sign-in-session-iam-policies"></a>

Sign-in sessions introduce the condition key `signin:MaxSigninSessionDuration`, a numeric value in seconds that restricts the maximum duration that can be requested when a sign-in session is established.

The following policy denies `signin:CreateOAuth2Token` when a role requests a sign-in session longer than 24 hours.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "signin:CreateOAuth2Token",
      "Resource": "*",
      "Condition": {
        "NumericGreaterThan": {
          "signin:MaxSigninSessionDuration": "86400"
        }
      }
    }
  ]
}
```

### Organizational guardrails with SCPs
<a name="oauth-sign-in-session-scps"></a>

You can use the `signin:MaxSigninSessionDuration` condition key in service control policies (SCPs) to set an organization-wide ceiling without changing the duration configured on individual roles.

The following SCP ensures no sign-in session can exceed 12 hours.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "signin:CreateOAuth2Token",
      "Resource": "*",
      "Condition": {
        "NumericGreaterThan": {
          "signin:MaxSigninSessionDuration": "43200"
        }
      }
    }
  ]
}
```

SCPs act as guardrails. They do not change the duration configured on the role, but they prevent sessions that would exceed the organizational threshold from being established.

### Session duration precedence
<a name="oauth-sign-in-session-precedence"></a>

Sign-in session duration takes precedence over existing session duration limits for supported AWS CLI and OAuth-based authentication flows. This includes authentication performed through an external identity provider (IdP) such as Okta or Microsoft Entra ID.

AWS Management Console sessions follow a different precedence model. For console access, AWS continues to honor the session duration specified through custom claims provided by the external IdP. Extended sign-in session durations do not apply to AWS Management Console sessions.