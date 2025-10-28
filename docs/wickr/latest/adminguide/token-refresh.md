This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Grace period for token refresh

Occasionally, there may be instances where identity providers encounter temporary
or extended outages, which may lead to your users being logged out unexpectedly due
to a failed refresh token for their client session. To prevent this problem, you can
establish a grace period that allows your users to remain signed in even if their
client refresh token fails during such outages.

Here are the available options for the grace period:

- No grace period (default): Users will be signed out immediately after a
  refresh token failure.
- 30 minute grace period: Users can stay signed in for up to 30 minutes
  after a refresh token failure.
- 60 minute grace period: Users can stay signed in for up to 60 minutes
  after a refresh token failure.
