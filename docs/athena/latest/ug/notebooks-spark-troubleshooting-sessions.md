# Troubleshoot session errors

Use the information in this section to troubleshoot session issues.

When a custom configuration error occurs during a session start, the Athena for Spark
console shows an error message banner. To troubleshoot session start errors, you can check
session state change or logging information.

## View session state change information

You can get details about a session state change from the Athena notebook editor or
from the Athena API.

###### To view session state information in the Athena console

1. In the Athena notebook editor, from the **Session** menu on
   the upper right, choose **View details**.
2. View the **Current session** tab. The **Session
   information** section shows you information like session ID,
   workgroup, status, and state change reason.

The following screen capture example shows information in the **State
change reason** section of the **Session
information** dialog box for a Spark session error in Athena.

![Viewing session state change information in the Athena for Spark console.](images/notebooks-spark-custom-jar-cfg-1.jpeg)

###### To view session state information using the Athena API

- In the Athena API, you can find session state change information in the
  `StateChangeReason` field of [SessionStatus](../APIReference/API_SessionStatus.md "../APIReference/API_SessionStatus.md")
  object.

###### Note

After you manually stop a session, or if the session stops after an idle timeout
(the default is 20 minutes), the value of **StateChangeReason**
changes to **`Session was terminated per request`**.

## Use logging to troubleshoot session start errors

Custom configuration errors that occur during a session start are logged by [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md"). In your CloudWatch Logs, search for error messages from
`AthenaSparkSessionErrorLogger` to troubleshoot a failed session
start.

For more information about Spark logging, see [Log Spark application events in Athena](notebooks-spark-logging.md "notebooks-spark-logging.md").

For more information about troubleshooting sessions in Athena for Spark, see [Troubleshoot session errors](notebooks-spark-troubleshooting-sessions.md "notebooks-spark-troubleshooting-sessions.md").

## Specific session issues

Use the information in this section to troubleshoot some specific session
issues.

If you receive the error message **`Session in unhealthy state. Please
 create a new session`**, terminate your existing session and create
a new one.

When you open a notebook, you may see the following error message:

```
A connection to the notebook server could not be established.
The notebook will continue trying to reconnect.
Check your network connection or notebook server configuration.
```

#### Cause

When Athena opens a notebook, Athena creates a session and connects to the
notebook using a pre-signed notebook URL. The connection to the notebook
uses the WSS ([WebSocket
Secure](https://en.wikipedia.org/wiki/WebSocket "https://en.wikipedia.org/wiki/WebSocket")) protocol.

The error can occur for the following reasons:

- A local firewall (for example, a company-wide firewall) is
  blocking WSS traffic.
- Proxy or anti-virus software on your local computer is blocking
  the WSS connection.

#### Solution

Assume you have a WSS connection in the `us-east-1` Region like
the following:

```
wss://94c2bcdf-66f9-4d17-9da6-7e7338060183.analytics-gateway.us-east-1.amazonaws.com/
api/kernels/33c78c82-b8d2-4631-bd22-1565dc6ec152/channels?session_id=
7f96a3a048ab4917b6376895ea8d7535
```

To resolve the error, use one of the following strategies.

- Use wild card pattern syntax to allow list WSS traffic on port
  `443` across AWS Regions and AWS accounts.

```
wss://*amazonaws.com
```

- Use wild card pattern syntax to allow list WSS traffic on port
  `443` in one AWS Region and across AWS accounts
  in the AWS Region that you specify. The following example uses
  `us-east-1`.

```
wss://*analytics-gateway.us-east-1.amazonaws.com
```
