# User background

sessions

User background sessions continue even when the user is no longer active. These allow for
long-running jobs that can continue even after the user has logged off. This can be enabled
through SageMaker AI's trusted identity propagation. The following page explains the configuration
options and behaviors for user background sessions.

###### Note

- Existing active user sessions are not impacted when trusted identity propagation is
  enabled. The default duration applies only to new user sessions or restarted
  sessions.
- User background sessions apply to any long-running SageMaker AI workflows or jobs with
  persistent states. This includes, but is not limited to, any SageMaker AI resources that
  maintain execution status or require ongoing monitoring. For example, SageMaker Training,
  Processing, and Pipelines execution jobs.

###### Topics

- [Configure user background
  session](#configure-user-background-sessions "#configure-user-background-sessions")
- [Default user background session
  duration](#default-user-background-session-duration "#default-user-background-session-duration")
- [Impact of disabling trusted identity propagation in Studio](#user-background-session-impact-disable-trustedidentitypropagation-studio "#user-background-session-impact-disable-trustedidentitypropagation-studio")
- [Impact of disabling user background sessions in the IAM Identity Center console](#user-background-session-impact-disable-trustedidentitypropagation-identity-center "#user-background-session-impact-disable-trustedidentitypropagation-identity-center")
- [Runtime
  considerations](#user-background-session-runtime-considerations "#user-background-session-runtime-considerations")

## Configure user background

session

Once trusted identity propagation for Amazon SageMaker Studio is enabled, default duration
limits can be configured through the [user background sessions
in the IAM Identity Center](../../../singlesignon/latest/userguide/user-background-sessions.md "../../../singlesignon/latest/userguide/user-background-sessions.md").

## Default user background session

duration

By default, all user background sessions have a duration limit of 7 days. Administrators
can [modify this duration in
the IAM Identity Center console](../../../singlesignon/latest/userguide/user-background-sessions.md "../../../singlesignon/latest/userguide/user-background-sessions.md"). This setting applies at the IAM Identity Center instance level, affecting all
supported IAM Identity Center applications and Studio domains within that instance.

When trusted identity propagation is enabled, administrators in the SageMaker AI console will
find a banner with the following information:

- The duration limit for user background sessions
- A link to the IAM Identity Center console where administrators can change this
  configuration
  - The duration can be set to any value from 15 minutes up to 90 days

An error message will occur when a user background session has expired. You can use the
link to the IAM Identity Center console to update the duration.

## Impact of disabling trusted identity propagation in Studio

If an administrator disables trusted identity propagation, after initially enabling it,
in the SageMaker AI console:

- Existing jobs continue to run without interruption when user background sessions are
  enabled.
- When user background sessions are disabled, any long-running SageMaker AI workflows or jobs
  with persistent states will switch to using interactive sessions. This includes, but is
  not limited to, any SageMaker AI resources that maintain execution status or require ongoing
  monitoring. For example, Amazon SageMaker Training and Processing jobs.
- Users can restart expired jobs from checkpoints.
- New jobs run with IAM role credentials and do not propagate the identity
  context.

## Impact of disabling user background sessions in the IAM Identity Center console

When the user background session is **disabled** for the
IAM Identity Center instance, the SageMaker AI job uses user interactive sessions. When using interactive
sessions, a SageMaker AI job will fail within 15 minutes when:

- The user logs out
- The interactive session is revoked by the administrator

When the user background session is **enabled** for the
IAM Identity Center instance, the SageMaker AI job uses user background sessions. When using interactive sessions,
a SageMaker AI job will fail within 15 minutes when:

- The user background session expires
- The user background session is manually revoked by an administrator

The following provides example behavior with SageMaker Training jobs. When an administrator
enables trusted identity propagation but disables [user background
sessions](../../../singlesignon/latest/userguide/user-background-sessions.md "../../../singlesignon/latest/userguide/user-background-sessions.md") in the IAM Identity Center console:

- If a user stays logged in, their Training jobs created while background sessions are
  disabled fallback to the interactive session.
- If the user logs off, the session expires and Training jobs depending on the
  interactive session will fail.
- Users can restart their Training job from the last checkpoint. The session duration
  is determined by what is set for the interactive session duration in the IAM Identity Center
  console.
- If a user disables background sessions **after**
  starting a job, the job will continue to use its existing background sessions. In other
  words, SageMaker AI will not create any new background sessions.

The same behavior applies if background sessions are enabled at the IAM Identity Center instance level
but disabled specifically for the Studio application using [IAM Identity Center APIs](../../../singlesignon/latest/APIReference/welcome.md "../../../singlesignon/latest/APIReference/welcome.md").

## Runtime

considerations

When an administrator sets `MaxRuntimeInSeconds` for long-running Training or
Processing jobs that is lower than the user background session duration, SageMaker AI runs the job for
the minimum of either `MaxRuntimeInSeconds` or user background session duration.
For more information about `MaxRuntimeInSeconds`, see [CreateTrainingJob](../APIReference/API_CreateTrainingJob.md#sagemaker-CreateTrainingJob-request-StoppingCondition "../APIReference/API_CreateTrainingJob.md#sagemaker-CreateTrainingJob-request-StoppingCondition"). See [user background sessions
in the IAM Identity Center](../../../singlesignon/latest/userguide/user-background-sessions.md "../../../singlesignon/latest/userguide/user-background-sessions.md") for information on how to set the runtime.
