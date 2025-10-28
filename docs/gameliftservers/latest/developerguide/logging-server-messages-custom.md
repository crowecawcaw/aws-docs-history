# Logging server messages (custom

servers)

You can capture custom server messages from your Amazon GameLift Servers custom servers in log files. To
learn about logging for Amazon GameLift Servers Realtime, see [Logging server messages (Amazon GameLift Servers Realtime)](logging-server-messages-rts.md "logging-server-messages-rts.md").

###### Important

There is a limit on the size of a log file per game session (see
[Amazon GameLift Servers endpoints and quotas](../../../general/latest/gr/gamelift.md "../../../general/latest/gr/gamelift.md")
in the _AWS General Reference_). When a game session ends, Amazon GameLift Servers uploads the server
logs to Amazon Simple Storage Service (Amazon S3). Amazon GameLift Servers will not upload logs that exceed the limit. Logs can grow very
quickly and exceed the size limit. You should monitor your logs and limit the log output to
necessary messages only.

## Configuring logging for custom

servers

With Amazon GameLift Servers custom servers, you write your own code to perform logging, which you
configure as part of your server process configuration. Amazon GameLift Servers uses your logging
configuration to identify the files that it must upload to S3 at the end of each game
session.

The following instructions show how to configure logging using simplified code
examples:

C++

###### To configure logging (C++)

1. Create a vector of strings that are directory paths to game server
   log files.

```
std::string serverLog("serverOut.log");        // Example server log file
std::vector<std::string> logPaths;
logPaths.push_back(serverLog);
```

2. Provide your vector as the [LogParameters](integration-server-sdk-cpp-ref-datatypes.md#integration-server-sdk-cpp-ref-dataypes-log "integration-server-sdk-cpp-ref-datatypes.md#integration-server-sdk-cpp-ref-dataypes-log") of your [ProcessParameters](integration-server-sdk-cpp-ref-datatypes.md#integration-server-sdk-cpp-ref-dataypes-process "integration-server-sdk-cpp-ref-datatypes.md#integration-server-sdk-cpp-ref-dataypes-process") object.

```
Aws::GameLift::Server::ProcessParameters processReadyParameter = Aws::GameLift::Server::ProcessParameters(
    std::bind(&Server::onStartGameSession, this, std::placeholders::_1),
    std::bind(&Server::onProcessTerminate, this),
    std::bind(&Server::OnHealthCheck, this),
    std::bind(&Server::OnUpdateGameSession, this),
    listenPort,
    **Aws::GameLift::Server::LogParameters(logPaths));**
```

3. Provide the [ProcessParameters](integration-server-sdk-cpp-ref-datatypes.md#integration-server-sdk-cpp-ref-dataypes-process "integration-server-sdk-cpp-ref-datatypes.md#integration-server-sdk-cpp-ref-dataypes-process") object when you call [ProcessReady()](integration-server-sdk-cpp-ref-actions.md#integration-server-sdk-cpp-ref-processready "integration-server-sdk-cpp-ref-actions.md#integration-server-sdk-cpp-ref-processready").

```
Aws::GameLift::GenericOutcome outcome =
   Aws::GameLift::Server::ProcessReady(processReadyParameter);
```

For a more complete example, see [ProcessReady()](integration-server-sdk-cpp-ref-actions.md#integration-server-sdk-cpp-ref-processready "integration-server-sdk-cpp-ref-actions.md#integration-server-sdk-cpp-ref-processready").

C#

###### To configure logging (C#)

1. Create a list of strings that are directory paths to game server
   log files.

```
List<string> logPaths = new List<string>();
logPaths.Add("C:\\game\\serverOut.txt");     // Example of a log file that the game server writes
```

2. Provide your list as the [LogParameters](integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-log "integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-log") of your [ProcessParameters](integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-process "integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-process") object.

```
var processReadyParameter = new ProcessParameters(
    this.OnGameSession,
    this.OnProcessTerminate,
    this.OnHealthCheck,
    this.OnGameSessionUpdate,
    port,
    **new LogParameters(logPaths));**
```

3. Provide the [ProcessParameters](integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-process "integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-process") object when you call [ProcessReady()](integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-processready "integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-processready").

```
var processReadyOutcome =
   GameLiftServerAPI.ProcessReady(processReadyParameter);
```

For a more complete example, see [ProcessReady()](integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-processready "integration-server-sdk-csharp-ref-actions.md#integration-server-sdk-csharp-ref-processready").

## Writing to logs

Your log files exist after your server process has started. You can write to the logs
using any method to write to files. To capture all of your server's standard output and
error output, remap the output streams to log files, as in the following
examples:

C++

```
std::freopen("serverOut.log", "w+", stdout);
std::freopen("serverErr.log", "w+", stderr);
```

C#

```
Console.SetOut(new StreamWriter("serverOut.txt"));
Console.SetError(new StreamWriter("serverErr.txt"));
```

## Accessing server logs

Log access varies by fleet type:

### Managed EC2 fleets

When a game session ends, Amazon GameLift Servers automatically stores the logs in an S3 bucket and
retains them for 14 days. To get the location of the logs for a game session, you can
use the [GetGameSessionLogUrl](../../../gamelift/latest/apireference/API_GetGameSessionLogUrl.md "../../../gamelift/latest/apireference/API_GetGameSessionLogUrl.md") API operation. To download the logs, use the URL that
the operation returns.

Alternatively, you can set up your own logging solution by configuring your game server
to send logs directly to your preferred logging service or storage location. For more information, see [Communicate with other AWS resources from
your fleets](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").

### Container fleets

Container fleets capture standard output and error streams from all containers. You can
configure logging using one of these options:

- Save container output as CloudWatch log streams in a specified log group
- Save container output to an S3 storage bucket
- Turn off logging (container output isn't saved)

For detailed information about configuring logging options when creating container fleets, see [LogConfiguration](../apireference/API_CreateContainerFleet.md#gameliftservers-CreateContainerFleet-request-LogConfiguration "../apireference/API_CreateContainerFleet.md#gameliftservers-CreateContainerFleet-request-LogConfiguration") in the Amazon GameLift Servers API Reference.
