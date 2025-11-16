# User background sessions

User background sessions enable long-running analytics and machine learning flows to continue even after
the user has logged off from their notebook interface. This capability is implemented through EMR Serverless integration with IAM Identity Center's trusted identity
propagation feature. This section explains the configuration options and behaviors for user background sessions.

###### Note

User background sessions apply to Spark workloads initiated through notebook interfaces like Amazon SageMaker Unified Studio. Enabling or disabling this feature
affects only new Livy sessions; existing active Livy sessions are not impacted.

## Configure user background sessions

User background sessions must be enabled at two levels for proper functionality:

1. **IAM Identity Center instance level** – typically configured by IdC administrators
2. **EMR Serverless application level** – configured by EMR Serverless application administrators

### Enable user background sessions for EMR Serverless applications

To enable user background sessions for an EMR Serverless application, you must set the `userBackgroundSessionsEnabled` parameter
to `true` in the `identityCenterConfiguration` when creating or updating an application.

**Prerequisites**

- Your IAM role that is used to create/update the EMR Serverless application must have the `sso:PutApplicationSessionConfiguration` permission. This
  permission allows EMR Serverless to enable User background sessions at EMR Serverless managed IdC application level.
- Your EMR Serverless application must use release label 7.8 or later and must be Trusted-Identity Propagation enabled.

**To enable user background sessions using the AWS CLI**

```
aws emr-serverless create-application \
    --name "my-analytics-app" \
    --type "SPARK" \
    --release-label "emr-7.8.0" \
    --identity-center-configuration '{"identityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-1234567890abcdef", "userBackgroundSessionsEnabled": true}'
```

**To update an existing application:**

```
aws emr-serverless update-application \
    --application-id `applicationId` \
    --identity-center-configuration '{"identityCenterInstanceArn": "arn:aws:sso:::instance/ssoins-1234567890abcdef", "userBackgroundSessionsEnabled": true}'
```

### Configuration Matrix

The effective user background session configuration depends on both the EMR Serverless application setting and the IAM Identity Center
instance-level settings:

| User Background Session Configuration Matrix | IAM Identity Center userBackgroundSession Enabled | EMR Serverless userBackgroundSessionsEnabled     | Behavior |
| -------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ | -------- |
| Yes                                          | TRUE                                              | User background sessions enabled                 |
| Yes                                          | FALSE                                             | Session expires with user logout                 |
| No                                           | TRUE                                              | Application creation/update fails with Exception |
| No                                           | FALSE                                             | Session expires with user logout                 |

## Default user background session duration

By default, all user background sessions have a duration limit of 7 days in IAM Identity Center. Administrators can modify this duration in the IAM Identity Center console. This setting
applies at the IAM Identity Center instance level, affecting all supported IAM Identity Center applications within that instance.

- Duration can be set to any value from 15 minutes up to 90 days.
- This setting is configured in the IAM Identity Center console under **Settings** → **Authentication** → **Configure** (Non-Interactive
  Jobs section)

###### Note

EMR Serverless Livy sessions have a separate maximum duration limit of 24 hours. Sessions will terminate when either
the Livy session limit or the user background session duration is reached, whichever comes first.

## Impact of disabling user background sessions

When user background sessions are disabled in IAM Identity Center:

Existing Livy sessions

Continue to run without interruption if they were started with user background sessions enabled. These sessions will
continue using their existing background session tokens until they terminate naturally or are explicitly stopped.

New Livy sessions

Will use the standard trusted identity propagation flow and will terminate when the user logs out or their interactive
session expires (such as when closing a Amazon SageMaker Unified Studio JupyterLab notebook).

## Changing user background sessions duration

When the duration setting for user background sessions is modified
in IAM Identity Center:

Existing Livy sessions

Continue to run with the same background session duration with which they were started.

New Livy sessions

Will use the new session duration for background sessions.

## Considerations

### Session Termination Conditions

When using user background sessions, a Livy session will continue running until one of the following occurs:

- The user background session expires (based on IdC configuration, up to 90 days)
- The user background session is manually revoked by an administrator
- The Livy session reaches its idle timeout (default: 1 hour after the last executed statement)
- The Livy session reaches its maximum duration (24 hours)
- The user explicitly stops or restarts the notebook kernel

#### Data Persistence

When using user background sessions:

- Users cannot reconnect to their notebook interface to view results once they have logged out
- Configure your Spark statements to write results to persistent storage (such as Amazon S3) before execution completes

#### Cost Implications

- Jobs will continue to run to completion even after users end their Amazon SageMaker Unified Studio JupyterLab session and will incur charges
  for the entire duration of the completed run.
- Monitor your active background sessions to avoid unnecessary costs from forgotten
  or abandoned sessions.

#### Feature Availability

User background sessions for EMR Serverless are available for:

- Spark engine only (Hive engine is not supported)
- Livy interactive sessions only (batch jobs and streaming jobs are not supported)
- EMR Serverless release labels 7.8 and later
