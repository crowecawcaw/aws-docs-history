# Logging server messages for Amazon GameLift Servers Realtime

You can capture a variety of custom server messages from your Amazon GameLift Servers Realtime servers and save them
to game session log files. When a game session ends, Amazon GameLift Servers automatically uploads the session
logs to Amazon Simple Storage Service (Amazon S3). This topic provides instructions on how to add log messaging to
your server scripts and then access game session logs from Amazon S3 storage. You can also
configure logging levels to manage the volume of log messages that your servers generate.

###### Important

There is a limit on the size of a log file per game session (see
[Amazon GameLift Servers endpoints and quotas](../../../general/latest/gr/gamelift.md "../../../general/latest/gr/gamelift.md")
in the _AWS General Reference_). When a game session ends, Amazon GameLift Servers uploads the server
logs to Amazon Simple Storage Service (Amazon S3). Amazon GameLift Servers will not upload logs that exceed the limit. Logs can grow very
quickly and exceed the size limit. You should monitor your logs and limit the log output to
necessary messages only.

## Logging messages in your server

script

You can output custom messages in the [script for
your Amazon GameLift Servers Realtime](realtime-script.md "realtime-script.md"). Use the following steps to send server messages to a log
file:

1. Create a variable to hold the reference to the logger object.

```
var logger;
```

2. In the `init()` function, get the logger from the session object
   and assign it to your logger variable.

```
function init(rtSession) {
    session = rtSession;
    logger = session.getLogger();
}
```

3. Call the appropriate function on the logger to output a message.

**Debug messages**

```
logger.debug("This is my debug message...");
```

**Informational messages**

```
logger.info("This is my info message...");
```

**Warning messages**

```
logger.warn("This is my warn message...");
```

**Error messages**

```
logger.error("This is my error message...");
```

**Fatal error messages**

```
logger.fatal("This is my fatal error message...");
```

**Customer experience fatal error
messages**

```
logger.cxfatal("This is my customer experience fatal error message...");
```

For an example of the logging statements in a script, see [Amazon GameLift Servers Realtime script example](realtime-script.md#realtime-script-examples "realtime-script.md#realtime-script-examples").

The output in the log files indicates the type of message (`DEBUG`,
`INFO`, `WARN`, `ERROR`, `FATAL`,
`CXFATAL`), as shown in the following lines from an example log:

```

09 Sep 2021 11:46:32,970 [INFO] (gamelift.js) 215: Calling GameLiftServerAPI.InitSDK...
09 Sep 2021 11:46:32,993 [INFO] (gamelift.js) 220: GameLiftServerAPI.InitSDK succeeded
09 Sep 2021 11:46:32,993 [INFO] (gamelift.js) 223: Waiting for Realtime server to start...
09 Sep 2021 11:46:33,15 [WARN] (index.js) 204: Connection is INSECURE. Messages will be sent/received as plaintext.
```

## Accessing server logs

When a game session ends, Amazon GameLift Servers automatically stores the logs in Amazon S3 and retains them
for 14 days. You can use the [GetGameSessionLogUrl API call](../../../gamelift/latest/apireference/API_GetGameSessionLogUrl.md "../../../gamelift/latest/apireference/API_GetGameSessionLogUrl.md") to get the location of the logs for a game
session. Use URL returned by the API call to download the logs.

## Adjusting the logging level

Logs can grow very quickly and exceed the size limit. You should monitor your logs and
limit the log output to necessary messages only. For Amazon GameLift Servers Realtime, you can adjust the logging
level by providing a parameter in your fleet's runtime configuration in the form
`loggingLevel:`LOGGING_LEVEL`, where
 `LOGGING_LEVEL`` is one of the following
values:

1. `debug`
2. `info`
   _(default)_
3. `warn`
4. `error`
5. `fatal`
6. `cxfatal`

This list is ordered from least severe (`debug`) to most severe
(`cxfatal`). You set a single `loggingLevel` and the server
will only log messages at that severity level or a higher severity level. For example,
setting `loggingLevel:error` will make all of the servers in your fleet only
write `error`, `fatal`, and `cxfatal` messages to the
log.

You can set the logging level for your fleet when you create it or after it is
running. Changing your fleet's logging level after it is running will only affect logs
for game sessions created after the update. Logs for any existing game sessions won't be
affected. If you don't set a logging level when you create your fleet, your servers will
set the logging level to `info` by default. Refer to the following sections
for instructions to set the logging level.

###### Setting the logging level when creating a Amazon GameLift Servers Realtime fleet (Console)

Follow the instructions at [Create a hosting fleet for Amazon GameLift Servers Realtime](realtime-fleets-creating.md "realtime-fleets-creating.md") to create your fleet, with the following
addition:

- In the **Process management** step, under
  **Server process allocation**,
  provide the logging level
  key-value pair (such as `loggingLevel:error`) as a value for
  **Launch parameters**. Use a non-alphanumeric character
  (except comma) to separate the logging level from any additional parameters (for example,
  `loggingLevel:error +map Winter444`).

###### Setting the logging level when creating a Amazon GameLift Servers Realtime fleet (AWS CLI)

Follow the instructions at [Create a hosting fleet for Amazon GameLift Servers Realtime](realtime-fleets-creating.md "realtime-fleets-creating.md") to create your fleet, with the following
addition:

- In the argument to the `--runtime-configuration` parameter for
  `create-fleet`, provide the logging level key-value pair (such as
  `loggingLevel:error`) as a value for `Parameters`. Use a
  non-alphanumeric character (except comma) to separate the logging level from any additional
  parameters. See the following example:

```
--runtime-configuration "GameSessionActivationTimeoutSeconds=60,
                    MaxConcurrentGameSessionActivations=2,
                    ServerProcesses=[{LaunchPath=/local/game/myRealtimeLaunchScript.js,
                                    Parameters=**loggingLevel:error** +map Winter444,
                                    ConcurrentExecutions=10}]"
```

###### Setting the logging level for a running Amazon GameLift Servers Realtime fleet (Console)

Follow the instructions at
[Update an Amazon GameLift Servers fleet configuration](../developerguide/fleets-editing.md "../developerguide/fleets-editing.md") to update your fleet using the Amazon GameLift Servers Console,
with the following addition:

- On the **Edit fleet** page, under **Server process allocation**,
  provide the logging level
  key-value pair (such as `loggingLevel:error`) as a value for
  **Launch parameters**. Use a non-alphanumeric character
  (except comma) to separate the logging level from any additional parameters (for example,
  `loggingLevel:error +map Winter444`).

###### Setting the logging level for a running Amazon GameLift Servers Realtime fleet (AWS CLI)

Follow the instructions at [Update an Amazon GameLift Servers fleet configuration](../developerguide/fleets-editing.md "../developerguide/fleets-editing.md") to update your fleet using the AWS CLI, with the
following addition:

- In the argument to the `--runtime-configuration` parameter for
  `update-runtime-configuration`,
  provide the logging level key-value pair (such as
  `loggingLevel:error`) as a value for `Parameters`. Use a
  non-alphanumeric character (except comma) to separate the logging level from any additional
  parameters. See the following example:

```
--runtime-configuration "GameSessionActivationTimeoutSeconds=60,
                    MaxConcurrentGameSessionActivations=2,
                    ServerProcesses=[{LaunchPath=/local/game/myRealtimeLaunchScript.js,
                                    Parameters=**loggingLevel:error** +map Winter444,
                                    ConcurrentExecutions=10}]"
```
