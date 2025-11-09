# User background sessions for AWS Glue ETL

User background sessions enable long-running analytics and machine learning workloads to continue even
after the user has logged off from their notebook interface. This capability is implemented through AWS Glue's
trusted identity propagation feature. The following page explains the configuration options and
behaviors for user background sessions.

###### Note

User background sessions apply to AWS Glue interactive sessions initiated through notebook interfaces
like SageMaker Unified Studio. Enabling or disabling this feature affects only new interactive sessions;
existing active sessions are not impacted.

## Configure user background sessions

User background sessions must be enabled at two levels for proper functionality:

1. IAM Identity Center instance level (configured by IdC administrators)
2. AWS Glue Identity Center configuration level (configured by AWS Glue administrators)

### Enable user background sessions for AWS Glue

To enable user background sessions for AWS Glue, you must set the `userBackgroundSessionsEnabled` parameter
to `true` in the Identity Center configuration when creating or updating the configuration.

Prerequisites

- Your IAM role that is used to create/update the AWS Glue Identity Center configuration must have the
  `sso:PutApplicationSessionConfiguration` permission. This permission allows AWS Glue to enable user
  background sessions at the AWS Glue-managed IdC application level.
- Your AWS Glue interactive sessions must use AWS Glue version 5.0 or later and must be Trusted Identity
  Propagation enabled.

To enable user background sessions using the AWS CLI:

```
aws glue create-glue-identity-center-configuration \
    --instance-arn "arn:aws:sso:::instance/ssoins-1234567890abcdef" \
    --user-background-sessions-enabled
```

To update an existing configuration:

```
aws glue update-glue-identity-center-configuration \
    --user-background-sessions-enabled
```

#### Configuration matrix

The effective user background session configuration depends on both the AWS Glue configuration setting and
the IAM Identity Center instance-level settings:

| IAM Identity Center userBackgroundSession Enabled? | AWS Glue userBackgroundSessionsEnabled | Behavior                              |
| -------------------------------------------------- | -------------------------------------- | ------------------------------------- |
| Yes                                                | TRUE                                   | User background sessions enabled      |
| Yes                                                | FALSE                                  | Session expires with user logout      |
| No                                                 | TRUE                                   | Session creation fails with Exception |
| No                                                 | FALSE                                  | Session expires with user logout      |

## Default user background session duration

By default, all user background sessions have a duration limit of 7 days in IAM Identity Center.
Administrators can modify this duration in the IAM Identity Center console. This setting applies at the
IAM Identity Center instance level, affecting all supported IAM Identity Center applications within that
instance.

- Duration can be set to any value from 15 minutes up to 90 days
- This setting is configured in the IAM Identity Center console under Settings → Authentication →
  Configure (Non-Interactive Jobs section)

###### Note

AWS Glue interactive sessions have a separate idle timeout limit of 48 hours by default. Sessions
will terminate when either the AWS Glue session idle timeout or the user background session duration is
reached, whichever comes first.

## Impact of disabling user background sessions

When user background sessions are disabled at the AWS Glue configuration level:

- **Existing interactive sessions:** Continue to run without interruption if they were started with user
  background sessions enabled. These sessions will continue using their existing background session tokens
  until they terminate naturally or are explicitly stopped.
- **New interactive sessions:** Will use the standard trusted identity propagation flow and will terminate
  when the user logs out or their interactive session expires (such as when closing a SageMaker Unified
  Studio JupyterLab notebook).

### Changing user background sessions duration

When the duration setting for user background sessions is modified in IAM Identity Center:

- **Existing interactive sessions:** Continue to run with the same background session duration with which
  they were started
- **New interactive sessions:** Will use the new session duration for background sessions

## Runtime considerations

### Session termination conditions

When using user background sessions, a AWS Glue interactive session will continue running until one of the
following occurs:

- The user background session expires (based on IdC configuration, up to 90 days)
- The user background session is manually revoked by an administrator
- The AWS Glue interactive session reaches its idle timeout (default: 48 hours after the last executed
  statement)
- The user explicitly stops or restarts the notebook kernel

### Data persistence

When using user background sessions:

- Users cannot reconnect to their notebook interface to view results once they have logged out
- Configure your Spark statements to write results to persistent storage (such as Amazon S3) before
  execution completes

### Cost implications

- Jobs will continue to run to completion even after users end their SageMaker Unified Studio JupyterLab
  session and will incur charges for the entire duration of the completed run
- Monitor your active background sessions to avoid unnecessary costs from forgotten or abandoned sessions

### Feature availability

User background sessions for AWS Glue are available for:

- AWS Glue interactive sessions only (AWS Glue jobs and streaming jobs are not supported)
- AWS Glue version 5.0 and later
- Trusted Identity Propagation enabled configurations only
