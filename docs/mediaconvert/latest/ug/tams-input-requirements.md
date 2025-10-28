# Requirements for TAMS inputs

To process content from TAMS servers with MediaConvert, you need the following:

**TAMS server**

A TAMS server that implements the BBC TAMS API specification and is accessible from MediaConvert using HTTPS protocol. The server must support the required API endpoints for sources, flows, and segments. Provide only the base server URL (such as `https://tams-server.example.com/api`) without source IDs or query parameters.

For more information about the BBC TAMS specification, see: [https://bbc.github.io/tams/main/index.html](https://bbc.github.io/tams/main/index.html "https://bbc.github.io/tams/main/index.html")

**EventBridge connection**

An Amazon EventBridge connection configured with OAuth credentials for your TAMS server. The connection must include the required OAuth scopes: `tams-api/read`, `tams-api/write`, and `tams-api/delete`.

For information about EventBridge connections, see the [EventBridge user guide](../../../eventbridge/latest/userguide/eb-connections.md "../../../eventbridge/latest/userguide/eb-connections.md").

**Valid source ID**

A UUID that identifies a valid multi-format source on your TAMS server. The source must contain video, audio, or combined flows with segments available for the specified time range.

**IAM permissions**

Your MediaConvert service role must have permissions to access the specified EventBridge connection. Add the following permissions to your service role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ConnectionPermissions",
 "Effect": "Allow",
 "Action": [
 "events:RetrieveConnectionCredentials"
 ],
 "Resource": "arn:aws:events:us-west-2:111122223333:connection/*"
 },
 {
 "Sid": "SecretsManagerPermissions",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret"
 ],
 "Resource": "arn:aws:secretsmanager:us-west-2:111122223333:secret:events!connection/*"
 }
 ]
}`

```

**Under 10,000 segments**

Each TAMS flow can contain a maximum of 10,000 segments. If your time range includes more segments, the job fails with an error. Consider using shorter time ranges or multiple jobs for longer content.

**No input clipping**

You cannot specify input clipping settings on TAMS inputs. MediaConvert automatically calculates precise clipping parameters based on segment boundaries and your specified time range.

**Zero-based timecode**

The timecode source must be set to **Zero-based** or left unspecified. Other timecode sources interfere with the automatic clipping calculations.
