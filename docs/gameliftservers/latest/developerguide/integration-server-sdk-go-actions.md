

# Go server SDK for Amazon GameLift Servers -- Actions
<a name="integration-server-sdk-go-actions"></a>

Use the server SDK 5.x reference to integrate your multiplayer game for hosting with Amazon GameLift Servers. For guidance about the integration process, see [Add Amazon GameLift Servers to your game server with the server SDK](gamelift-sdk-server-api.md).

`GameLiftServerAPI.go` defines the Go server SDK actions.

[Go server SDK for Amazon GameLift Servers -- Data types](integration-server-sdk-go-datatypes.md)

**Topics**
+ [Go server SDK for Amazon GameLift Servers -- Data types](integration-server-sdk-go-datatypes.md)
+ [GetSdkVersion()](#integration-server-sdk-go-getsdkversion)
+ [InitMetrics()](#integration-server-sdk-go-initmetrics)
+ [InitMetricsFromEnvironment()](#integration-server-sdk-go-initmetricsfromenv)
+ [InitSDK()](#integration-server-sdk-go-initsdk)
+ [ProcessReady()](#integration-server-sdk-go-processready)
+ [ProcessEnding()](#integration-server-sdk-go-processending)
+ [ActivateGameSession()](#integration-server-sdk-go-activategamesession)
+ [UpdatePlayerSessionCreationPolicy()](#integration-server-sdk-go-updateplayersessioncreationpolicy)
+ [GetGameSessionId()](#integration-server-sdk-go-getgamesessionid)
+ [GetTerminationTime()](#integration-server-sdk-go-getterm)
+ [AcceptPlayerSession()](#integration-server-sdk-go-acceptplayersession)
+ [RemovePlayerSession()](#integration-server-sdk-go-removeplayersession)
+ [DescribePlayerSessions()](#integration-server-sdk-go-describeplayersessions)
+ [StartMatchBackfill()](#integration-server-sdk-go-startmatchbackfill)
+ [StopMatchBackfill()](#integration-server-sdk-go-stopmatchbackfill)
+ [GetComputeCertificate()](#integration-server-sdk-go-getcomputecertificate)
+ [GetFleetRoleCredentials()](#integration-server-sdk-go-getfleetrolecredentials)
+ [ListContainersNetworkInfo()](#integration-server-sdk-go-listcontainersnetworkinfo)
+ [Destroy()](#integration-server-sdk-go-destroy)

## GetSdkVersion()
<a name="integration-server-sdk-go-getsdkversion"></a>

Returns the current version number of the SDK built into the server process.

### Syntax
<a name="integration-server-sdk-go-getsdkversion-syntax"></a>

```
func GetSdkVersion() (string, error)
```

### Return value
<a name="integration-server-sdk-go-getsdkversion-return"></a>

If successful, returns the current SDK version as a string. The returned string includes the version number (example `5.0.0`). If not successful, returns an error message such as `common.SdkVersionDetectionFailed`.

### Example
<a name="integration-server-sdk-go-getsdkversion-example"></a>

```
version, err := server.GetSdkVersion()
```

## InitMetrics()
<a name="integration-server-sdk-go-initmetrics"></a>

Initializes metrics collection for the Amazon GameLift Servers SDK. This method sets up metrics reporting to help monitor server performance and health. Call this method after [InitSDK()](#integration-server-sdk-go-initsdk) but before [ProcessReady()](#integration-server-sdk-go-processready).

### Syntax
<a name="integration-server-sdk-go-initmetrics-syntax"></a>

```
func InitMetrics() error
func InitMetrics(metricsParameters MetricsParameters) error
```

### Parameters
<a name="integration-server-sdk-go-initmetrics-parameter"></a>

MetricsParameters (optional)  
A `MetricsParameters` object that configures metrics collection. If not provided, default metrics configuration is used. The MetricsParameters structure contains the following fields:  
+ `StatsdHost` - The hostname or IP address of the StatsD server.
+ `StatsdPort` - The port number for the StatsD server.
+ `CrashReporterHost` - The hostname or IP address of the crash reporter service.
+ `CrashReporterPort` - The port number for the crash reporter service.
+ `FlushIntervalMs` - The interval in milliseconds for flushing metrics data.
+ `MaxPacketSize` - The maximum size of metrics packets in bytes.
For more information about the MetricsParameters structure, see [Server SDK 5.x for C\# data types](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk5-csharp-datatypes.html).

### Return value
<a name="integration-server-sdk-go-initmetrics-return"></a>

If successful, returns `nil` error to indicate that metrics collection has been initialized successfully.

### Example
<a name="integration-server-sdk-go-initmetrics-example"></a>

Initialize metrics with default configuration:

```
err := server.InitMetrics()
```

Initialize metrics with custom configuration:

```
metricsParams := MetricsParameters{
    StatsdHost:        "localhost",
    StatsdPort:        8125,
    CrashReporterHost: "localhost",
    CrashReporterPort: 9125,
    FlushIntervalMs:   5000,
    MaxPacketSize:     1024,
}

err := server.InitMetrics(metricsParams)
```

## InitMetricsFromEnvironment()
<a name="integration-server-sdk-go-initmetricsfromenv"></a>

Initializes metrics collection for the Amazon GameLift Servers SDK using configuration from environment variables. This method sets up metrics reporting using default settings derived from the runtime environment.

Call this method after [InitSDK()](#integration-server-sdk-go-initsdk) but before [ProcessReady()](#integration-server-sdk-go-processready).

### Syntax
<a name="integration-server-sdk-go-initmetricsfromenv-syntax"></a>

```
func InitMetricsFromEnvironment() error
```

### Return value
<a name="integration-server-sdk-go-initmetricsfromenv-return"></a>

If successful, returns `nil` error to indicate that metrics collection has been initialized successfully using environment configuration.

### Example
<a name="integration-server-sdk-go-initmetricsfromenv-example"></a>

```
err := server.InitMetricsFromEnvironment()
```

## InitSDK()
<a name="integration-server-sdk-go-initsdk"></a>

Initializes the Amazon GameLift Servers SDK. Call this method on launch before any other initialization related to Amazon GameLift Servers occurs. This method sets up communication between the server and the Amazon GameLift Servers service.

### Syntax
<a name="integration-server-sdk-go-initsdk-syntax"></a>

```
func InitSDK(params ServerParameters) error 
```

### Parameters
<a name="integration-server-sdk-go-initsdk-parameter"></a>

[ServerParameters](integration-server-sdk-go-datatypes.md#integration-server-sdk-go-dataypes-serverparameters)  
To initialize a game server on an Amazon GameLift Servers Anywhere fleet, construct a `ServerParameters` object with the following information:  
+ The URL of the WebSocket used to connect to your game server. 
+ The ID of the process used to host your game server. 
+ The ID of the compute hosting your game server processes. 
+ The ID of the Amazon GameLift Servers fleet containing your Amazon GameLift Servers Anywhere compute.
+ The authorization token generated by the Amazon GameLift Servers operation. 
To initialize a game server on an Amazon GameLift Servers managed EC2 fleet, construct a `ServerParameters` object with no parameters. With this call, the Amazon GameLift Servers agent sets up the compute environment and automatically connects to the Amazon GameLift Servers service for you. 

### Return value
<a name="integration-server-sdk-go-initsdk-return"></a>

If successful, returns `nil` error to indicate that the server process is ready to call [ProcessReady()](#integration-server-sdk-go-processready). 

**Note**  
If calls to `InitSDK()` are failing for game builds deployed to Anywhere fleets, check the `ServerSdkVersion` parameter used when creating the build resource. You must explicitly set this value to the server SDK version in use. The default value for this parameter is 4.x, which is not compatible. To resolve this issue, create a new build and deploy it to a new fleet.

### Example
<a name="integration-server-sdk-go-initsdk-example"></a>

Amazon GameLift Servers Anywhere example

```
//Define the server parameters
serverParameters := ServerParameters {
  WebSocketURL: "wss://us-west-1.api.amazongamelift.com",
  ProcessID: "PID1234",
  HostID: "HardwareAnywhere",
  FleetID: "aarn:aws:gamelift:us-west-1:111122223333:fleet/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
  AuthToken: "1111aaaa-22bb-33cc-44dd-5555eeee66ff"
}

//Call InitSDK to establish a local connection with the Amazon GameLift Servers Agent to enable further communication.
err := server.InitSDK(serverParameters)
```

Amazon GameLift Servers managed EC2 example

```
//Define the server parameters
serverParameters := ServerParameters {}

//Call InitSDK to establish a local connection with the Amazon GameLift Servers Agent to enable further communication.
err := server.InitSDK(serverParameters)
```

## ProcessReady()
<a name="integration-server-sdk-go-processready"></a>

Notifies Amazon GameLift Servers that the server process is ready to host game sessions. Call this method after invoking [InitSDK()](#integration-server-sdk-go-initsdk). This method should be called only one time per process.

### Syntax
<a name="integration-server-sdk-go-processready-syntax"></a>

```
func ProcessReady(param ProcessParameters) error
```

### Parameters
<a name="integration-server-sdk-go-processready-parameter"></a>

**ProcessParameters**  
A [ProcessParameters](integration-server-sdk-go-datatypes.md#integration-server-sdk-go-dataypes-process) object communicates the following information about the server process:  
+ The names of the callback methods implemented in the game server code that the Amazon GameLift Servers service invokes to communicate with the server process.
+ The port number that the server process is listening on.
+ The [LogParameters](integration-server-sdk-go-datatypes.md#integration-server-sdk-go-dataypes-log) data type containing the path to any game session-specific files that you want Amazon GameLift Servers to capture and store.

### Return value
<a name="integration-server-sdk-go-processready-return"></a>

Returns an error with an error message if the method fails. Returns `nil` if the method is successful.

### Example
<a name="integration-server-sdk-go-processready-example"></a>

This example illustrates both the [ProcessReady()](#integration-server-sdk-go-processready) call and delegate function implementations.

```
// Define the process parameters
processParams := ProcessParameters {
  OnStartGameSession: gameProcess.OnStartGameSession,
  OnUpdateGameSession: gameProcess.OnGameSessionUpdate,
  OnProcessTerminate: gameProcess.OnProcessTerminate,
  OnHealthCheck: gameProcess.OnHealthCheck,
  Port: port,
  LogParameters: LogParameters {    // logging and error example
    []string {"C:\\game\\logs", "C:\\game\\error"}
  }
}

err := server.ProcessReady(processParams)
```

## ProcessEnding()
<a name="integration-server-sdk-go-processending"></a>

Notifies Amazon GameLift Servers that the server process is terminating. Call this method after all other cleanup tasks (including shutting down the active game session) and before terminating the process. Depending on the result of `ProcessEnding()`, the process exits with success (0) or error (-1) and generates a fleet event. If the process terminates with an error, the fleet event generated is `SERVER_PROCESS_TERMINATED_UNHEALTHY`.

### Syntax
<a name="integration-server-sdk-go-processending-syntax"></a>

```
func ProcessEnding() error
```

### Return value
<a name="integration-server-sdk-go-processending-return"></a>

Returns a 0 error code or a defined error code.

### Example
<a name="integration-server-sdk-go-processending-example"></a>

```
// operations to end game sessions and the server process
defer func() {
  err := server.ProcessEnding()
  server.Destroy()
  if err != nil {
    fmt.Println("ProcessEnding() failed. Error: ", err)
    os.Exit(-1)
  } else {
    os.Exit(0)
  }
}
```

## ActivateGameSession()
<a name="integration-server-sdk-go-activategamesession"></a>

Notifies Amazon GameLift Servers that the server process has activated a game session and is now ready to receive player connections. This action is called as part of the `onStartGameSession()` callback function, after all game session initialization.

### Syntax
<a name="integration-server-sdk-go-activategamesession-syntax"></a>

```
func ActivateGameSession() error
```

### Return value
<a name="integration-server-sdk-go-activategamesession-return"></a>

Returns an error with an error message if the method fails.

### Example
<a name="integration-server-sdk-go-activategamesession-example"></a>

This example shows `ActivateGameSession()` called as part of the `onStartGameSession()` delegate function. 

```
func OnStartGameSession(GameSession gameSession) {
  // game-specific tasks when starting a new game session, such as loading map   
  // Activate when ready to receive players   
  err := server.ActivateGameSession();
}
```

## UpdatePlayerSessionCreationPolicy()
<a name="integration-server-sdk-go-updateplayersessioncreationpolicy"></a>

Updates the current game session's ability to accept new player sessions. A game session can be set to either accept or deny all new player sessions.

### Syntax
<a name="integration-server-sdk-go-updateplayersessioncreationpolicy-syntax"></a>

```
func UpdatePlayerSessionCreationPolicy(policy model.PlayerSessionCreationPolicy) error
```

### Parameters
<a name="integration-server-sdk-go-updateplayersessioncreationpolicy-parameter"></a>

**playerSessionCreationPolicy**  
String value that indicates whether the game session accepts new players.   
Valid values include:  
+ **`model.AcceptAll`** – Accept all new player sessions.
+ **`model.DenyAll`** – Deny all new player sessions.

### Return value
<a name="integration-server-sdk-go-updateplayersessioncreationpolicy-return"></a>

Returns an error with an error message if failure occurs.

### Example
<a name="integration-server-sdk-go-updateplayersessioncreationpolicy-example"></a>

This example sets the current game session's join policy to accept all players.

```
err := server.UpdatePlayerSessionCreationPolicy(model.AcceptAll)
```

## GetGameSessionId()
<a name="integration-server-sdk-go-getgamesessionid"></a>

Retrieves the ID of the game session hosted by the active server process.

### Syntax
<a name="integration-server-sdk-go-getgamesessionid-syntax"></a>

```
func GetGameSessionID() (string, error)
```

### Parameters
<a name="integration-server-sdk-go-getgamesessionid-parameter"></a>

This action has no parameters.

### Return value
<a name="integration-server-sdk-go-getgamesessionid-return"></a>

If successful, returns the game session ID and nil error. For idle processes that aren't yet activated with a game session, the call returns an empty string and `nil` error.

### Example
<a name="integration-server-sdk-go-getgamesessionid-example"></a>

```
gameSessionID, err := server.GetGameSessionID()
```

## GetTerminationTime()
<a name="integration-server-sdk-go-getterm"></a>

Returns the time that a server process is scheduled to be shut down if a termination time is available. A server process takes this action after receiving an `onProcessTerminate()` callback from Amazon GameLift Servers. Amazon GameLift Servers calls `onProcessTerminate()` for the following reasons: 
+ When the server process has reported poor health or hasn't responded to Amazon GameLift Servers.
+ When terminating the instance during a scale-down event.
+ When an instance is terminated due to a [spot-instance interruption](spot-tasks.md).

### Syntax
<a name="integration-server-sdk-go-getterm-syntax"></a>

```
func GetTerminationTime() (int64, error)
```

### Return value
<a name="integration-server-sdk-go-getterm-return"></a>

If successful, returns the timestamp in epoch seconds that the server process is scheduled to shut down and a `nil` error termination. The value is the termination time, expressed in elapsed ticks from `0001 00:00:00`. For example, the date time value `2020-09-13 12:26:40 -000Z` is equal to `637355968000000000` ticks. If no termination time is available, returns an error message.

### Example
<a name="integration-server-sdk-go-getterm-example"></a>

```
terminationTime, err := server.GetTerminationTime()
```

## AcceptPlayerSession()
<a name="integration-server-sdk-go-acceptplayersession"></a>

Notifies Amazon GameLift Servers that a player with the specified player session ID has connected to the server process and needs validation. Amazon GameLift Servers verifies that the player session ID is valid. After the player session is validated, Amazon GameLift Servers changes the status of the player slot from `RESERVED` to `ACTIVE`. 

### Syntax
<a name="integration-server-sdk-go-acceptplayersession-syntax"></a>

```
func AcceptPlayerSession(playerSessionID string) error
```

### Parameters
<a name="integration-server-sdk-go-acceptplayersession-parameter"></a>

`playerSessionId`  
Unique ID issued by Amazon GameLift Servers when a new player session is created.

### Return value
<a name="integration-server-sdk-go-acceptplayersession-return"></a>

Returns a generic outcome consisting of success or failure with an error message. 

### Example
<a name="integration-server-sdk-go-acceptplayersession-example"></a>

This example handles a connection request that includes validating and rejecting non-valid player session IDs. 

```
func ReceiveConnectingPlayerSessionID(conn Connection, playerSessionID string) {
    err := server.AcceptPlayerSession(playerSessionID)
    if err != nil {
        connection.Accept()
    } else {
        connection.Reject(err.Error())
    }
}
```

## RemovePlayerSession()
<a name="integration-server-sdk-go-removeplayersession"></a>

Notifies Amazon GameLift Servers that a player has disconnected from the server process. In response, Amazon GameLift Servers changes the player slot to available. 

### Syntax
<a name="integration-server-sdk-go-removeplayersession-syntax"></a>

```
func RemovePlayerSession(playerSessionID string) error
```

### Parameters
<a name="integration-server-sdk-go-removeplayersession-parameter"></a>

**`playerSessionId`**  
Unique ID issued by Amazon GameLift Servers when a new player session is created.

### Return value
<a name="integration-server-sdk-go-removeplayersession-return"></a>

Returns a generic outcome consisting of success or failure with an error message.

### Example
<a name="integration-server-sdk-go-removeplayersession-example"></a>

```
err := server.RemovePlayerSession(playerSessionID)
```

## DescribePlayerSessions()
<a name="integration-server-sdk-go-describeplayersessions"></a>

Retrieves player session data which includes settings, session metadata, and player data. Use this method to get information about the following:
+ A single player session
+ All player sessions in a game session
+ All player sessions associated with a single player ID

### Syntax
<a name="integration-server-sdk-go-describeplayersessions-syntax"></a>

```
func DescribePlayerSessions(req request.DescribePlayerSessionsRequest) (result.DescribePlayerSessionsResult, error) {
	return srv.describePlayerSessions(&req)
}
```

### Parameters
<a name="integration-server-sdk-go-describeplayersessions-parameter"></a>

**[DescribePlayerSessionsRequest](integration-server-sdk-go-datatypes.md#integration-server-sdk-go-dataypes-playersessions)**  
A `DescribePlayerSessionsRequest` object describes which player sessions to retrieve.

### Return value
<a name="integration-server-sdk-go-describeplayersessions-return"></a>

If successful, returns a `DescribePlayerSessionsResult` object that contains a set of player session objects that fit the request parameters.

### Example
<a name="integration-server-sdk-go-describeplayersessions-example"></a>

This example requests all player sessions actively connected to a specified game session. By omitting *NextToken* and setting the *Limit* value to 10, Amazon GameLift Servers returns the first 10 player session records matching the request.

```
// create request
describePlayerSessionsRequest := request.NewDescribePlayerSessions() 
describePlayerSessionsRequest.GameSessionID, _ = server.GetGameSessionID() // get ID for the current game session
describePlayerSessionsRequest.Limit = 10                                 // return the first 10 player sessions
describePlayerSessionsRequest.PlayerSessionStatusFilter = "ACTIVE"         // Get all player sessions actively connected to the game session

describePlayerSessionsResult, err := server.DescribePlayerSessions(describePlayerSessionsRequest)
```

## StartMatchBackfill()
<a name="integration-server-sdk-go-startmatchbackfill"></a>

Sends a request to find new players for open slots in a game session created with FlexMatch. For more information, see [FlexMatch backfill feature](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-backfill.html).

This action is asynchronous. If new players are matched, Amazon GameLift Servers delivers updated matchmaker data using the callback function `OnUpdateGameSession()`.

A server process can have only one active match backfill request at a time. To send a new request, first call [StopMatchBackfill()](#integration-server-sdk-go-stopmatchbackfill) to cancel the original request.

### Syntax
<a name="integration-server-sdk-go-startmatchbackfill-syntax"></a>

```
func StartMatchBackfill(req request.StartMatchBackfillRequest) (result.StartMatchBackfillResult, error)
```

### Parameters
<a name="integration-server-sdk-go-startmatchbackfill-parameter"></a>

**[StartMatchBackfillRequest](integration-server-sdk-go-datatypes.md#integration-server-sdk-go-dataypes-startmatchbackfillrequest)**  
A StartMatchBackfillRequest object communicates the following information:  
+ A ticket ID to assign to the backfill request. This information is optional; if no ID is provided, Amazon GameLift Servers generates one.
+ The matchmaker to send the request to. The full configuration ARN is required. This value is in the game session's matchmaker data.
+ The ID of the game session to backfill.
+ The available matchmaking data for the game session's current players.

### Return value
<a name="integration-server-sdk-go-startmatchbackfill-return"></a>

Returns a `StartMatchBackfillResult` object with the match backfill ticket ID, or failure with an error message. 

### Example
<a name="integration-server-sdk-go-startmatchbackfill-example"></a>

```
// form the request
startBackfillRequest := request.NewStartMatchBackfill()
startBackfillRequest.RequestID = "1111aaaa-22bb-33cc-44dd-5555eeee66ff"          // optional
startBackfillRequest.MatchmakingConfigurationArn = "arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MyMatchmakerConfig"
var matchMaker model.MatchmakerData
if err := matchMaker.UnmarshalJSON([]byte(gameSession.MatchmakerData)); err != nil {    
    return
}
startBackfillRequest.Players = matchMaker.Players
res, err := server.StartMatchBackfill(startBackfillRequest)

// Implement callback function for backfill
func OnUpdateGameSession(myGameSession model.GameSession) {
    // game-specific tasks to prepare for the newly matched players and update matchmaker data as needed
}
```

## StopMatchBackfill()
<a name="integration-server-sdk-go-stopmatchbackfill"></a>

Cancels an active match backfill request. For more information, see [FlexMatch backfill feature](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-backfill.html).

### Syntax
<a name="integration-server-sdk-go-stopmatchbackfill-syntax"></a>

```
func StopMatchBackfill(req request.StopMatchBackfillRequest) error
```

### Parameters
<a name="integration-server-sdk-go-stopmatchbackfill-parameter"></a>

**[StopMatchBackfillRequest](integration-server-sdk-go-datatypes.md#integration-server-sdk-go-dataypes-stopmatchbackfillrequest)**  
A StopMatchBackfillRequest object that identifies the matchmaking ticket to cancel:   
+ The ticket ID assigned to the backfill request.
+ The matchmaker the backfill request was sent to.
+ The game session associated with the backfill request.

### Return value
<a name="integration-server-sdk-go-stopmatchbackfill-return"></a>

Returns a generic outcome consisting of success or failure with an error message.

### Example
<a name="integration-server-sdk-go-stopmatchbackfill-example"></a>

```
stopBackfillRequest := request.NewStopMatchBackfill()  // Use this function to create request
stopBackfillRequest.TicketID = "1111aaaa-22bb-33cc-44dd-5555eeee66ff"
stopBackfillRequest.MatchmakingConfigurationArn = "arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MyMatchmakerConfig"
                
//error
err := server.StopMatchBackfill(stopBackfillRequest)
```

## GetComputeCertificate()
<a name="integration-server-sdk-go-getcomputecertificate"></a>

Retrieves the path to the TLS certificate used to encrypt the network connection between the game server and your game client. You can use the certificate path when you register your compute device to a Amazon GameLift Servers Anywhere fleet. For more information, see [RegisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html).

### Syntax
<a name="integration-server-sdk-go-getcomputecertificate-syntax"></a>

```
func GetComputeCertificate() (result.GetComputeCertificateResult, error)
```

### Return value
<a name="integration-server-sdk-go-getcomputecertificate-return"></a>

Returns a `GetComputeCertificateResult` object that contains the following: 
+  CertificatePath: The path to the TLS certificate on your compute resource. When using an Amazon GameLift Servers managed fleet, this path contains: 
  + `certificate.pem`: The end-user certificate. The full certificate chain is the combination of `certificateChain.pem` appended to this certificate.
  + `certificateChain.pem`: The certificate chain that contains the root certificate and intermediate certificates.
  + `rootCertificate.pem`: The root certificate.
  + `privateKey.pem`: The private key for the end-user certificate.
+ ComputeName: The name of your compute resource.

### Example
<a name="integration-server-sdk-go-getcomputecertificate-example"></a>

```
tlsCertificate, err := server.GetFleetRoleCredentials(getFleetRoleCredentialsRequest)
```

## GetFleetRoleCredentials()
<a name="integration-server-sdk-go-getfleetrolecredentials"></a>

Retrieves the service role credentials that you create to extend permissions to your other AWS services to Amazon GameLift Servers. These credentials allow your game server to use your AWS resources. For more information, see [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md).

### Syntax
<a name="integration-server-sdk-go-getfleetrolecredentials-syntax"></a>

```
func GetFleetRoleCredentials(
  req request.GetFleetRoleCredentialsRequest,
) (result.GetFleetRoleCredentialsResult, error) {
  return srv.getFleetRoleCredentials(&req)
}
```

### Parameters
<a name="integration-server-sdk-go-getfleetrolecredentials-parameters"></a>

[GetFleetRoleCredentialsRequest](integration-server-sdk-go-datatypes.md#integration-server-sdk-go-dataypes-getfleetrolecredentialsrequest)  
Role credentials that extend limited access to your AWS resources to the game server.

### Return value
<a name="integration-server-sdk-go-getfleetrolecredentials-return"></a>

Returns a `GetFleetRoleCredentialsResult` object that contains the following: 
+ AssumedRoleUserArn - The Amazon Resource Name (ARN) of the user that the service role belongs to. 
+ AssumedRoleId - The ID of the user that the service role belongs to. 
+ AccessKeyId - The access key ID to authenticate and provide access to your AWS resources. 
+ SecretAccessKey - The secret access key ID for authentication. 
+ SessionToken - A token to identify the current active session interacting with your AWS resources. 
+ Expiration - The amount of time until your session credentials expire.

### Example
<a name="integration-server-sdk-go-getfleetrolecredentials-example"></a>

```
// form the customer credentials request
getFleetRoleCredentialsRequest := request.NewGetFleetRoleCredentials()
getFleetRoleCredentialsRequest.RoleArn = "arn:aws:iam::123456789012:role/service-role/exampleGameLiftAction"

credentials, err := server.GetFleetRoleCredentials(getFleetRoleCredentialsRequest)
```

## ListContainersNetworkInfo()
<a name="integration-server-sdk-go-listcontainersnetworkinfo"></a>

Retrieves network information for all containers running on the same instance, including each container's name, ID, local IP address, and container group type. Use this information to enable game server processes to discover and communicate with other containers that are running on the same instance.

This action is supported only on container fleets. When called from any other compute type, it returns an `UnsupportedComputeTypeException` error. Amazon GameLift Servers obtains the network information from a discovery server that runs locally on the instance.

### Syntax
<a name="integration-server-sdk-go-listcontainersnetworkinfo-syntax"></a>

```
func ListContainersNetworkInfo() (result.ListContainersNetworkInfoResult, error)
```

### Return value
<a name="integration-server-sdk-go-listcontainersnetworkinfo-return"></a>

If successful, returns a `ListContainersNetworkInfoResult` object that contains the following:
+ `ContainersNetworkInfo` - A list of `ContainerNetworkInfo` entries, with one entry for each container running on the instance. Each entry contains the following:
  + `ContainerName` - The name of the container.
  + `ContainerID` - The unique identifier of the container.
  + `IPAddress` - The local IP address of the container on the instance.
  + `ContainerGroupType` - The type of container group that the container belongs to. Valid values are `GAME_SERVER` and `PER_INSTANCE`.

### Example
<a name="integration-server-sdk-go-listcontainersnetworkinfo-example"></a>

```
networkInfo, err := server.ListContainersNetworkInfo()
if err != nil {
  fmt.Println("ListContainersNetworkInfo() failed. Error: ", err)
  return
}

for _, container := range networkInfo.ContainersNetworkInfo {
  fmt.Printf("Container %s (%s) at %s, group type %s\n",
    container.ContainerName, container.ContainerID, container.IPAddress, container.ContainerGroupType)
}
```

## Destroy()
<a name="integration-server-sdk-go-destroy"></a>

Frees the Amazon GameLift Servers game server SDK from memory. As a best practice, call this method after `ProcessEnding()` and before terminating the process. If you're using an Anywhere fleet and you're not terminating server processes after every game session, call `Destroy()` and then `InitSDK()` to reinitialize before notifying Amazon GameLift Servers that the process is ready to host a game session with `ProcessReady()`.

### Syntax
<a name="integration-server-sdk-go-destroy-syntax"></a>

```
func Destroy() error {
	return srv.destroy()
}
```

### Return value
<a name="integration-server-sdk-go-destroy-return"></a>

Returns an error with an error message if the method fails.

### Example
<a name="integration-server-sdk-go-destroy-example"></a>

```
// operations to end game sessions and the server process
defer func() {
  err := server.ProcessEnding()
  server.Destroy()
  if err != nil {
    fmt.Println("ProcessEnding() failed. Error: ", err)
    os.Exit(-1)
  } else {
    os.Exit(0)
  }
}
```