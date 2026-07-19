# Prerequisites

Before you can use session credentials, you need:

- A stream group created after July 16, 2026. Stream groups created before this date
  do not support session credentials. To use this feature, create a new stream group.
- An IAM role with a name starting with `GameLiftStreams-` (for example,
  `GameLiftStreams-MyAppRole`), in the same AWS account as your stream group,
  with a trust policy that allows Amazon GameLift Streams to assume it.
- An `iam:PassRole` permission in the IAM policy of the principal that calls
  [StartStreamSession](../apireference/API_StartStreamSession.md "../apireference/API_StartStreamSession.md").
