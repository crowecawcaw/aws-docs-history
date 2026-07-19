# How session credentials work

When you pass a `RoleArn` on [StartStreamSession](../apireference/API_StartStreamSession.md "../apireference/API_StartStreamSession.md"):

1. Amazon GameLift Streams validates that the role can be assumed. If the role's trust policy is
   misconfigured, `StartStreamSession` returns an error. See
   [Troubleshooting session credentials](session-credentials-troubleshooting.md "session-credentials-troubleshooting.md").
2. Amazon GameLift Streams invokes `AssumeRole` on your behalf and makes the resulting
   credentials available to your application.
3. Your application's AWS SDK automatically discovers and uses the credentials.
   Credentials are refreshed automatically for the lifetime of the session.
   If you do not pass a `RoleArn`, the session starts without access to your
   AWS resources.
