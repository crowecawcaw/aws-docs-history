

# How session credentials work
<a name="session-credentials-how-it-works"></a>

When you pass a `RoleArn` on [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html):

1. Amazon GameLift Streams validates that the role can be assumed. If the role's trust policy is misconfigured, `StartStreamSession` returns an error. See [Troubleshooting session credentials](session-credentials-troubleshooting.md).

1. Amazon GameLift Streams invokes `AssumeRole` on your behalf and makes the resulting credentials available to your application.

1. Your application's AWS SDK automatically discovers and uses the credentials. Credentials are refreshed automatically for the lifetime of the session.

If you do not pass a `RoleArn`, the session starts without access to your AWS resources.