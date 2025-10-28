# Work with the Amazon GameLift Servers Agent

The Amazon GameLift Servers Agent oversees the running of game server processes on your Amazon GameLift Servers fleets. The
Agent is deployed to each compute in a fleet, and it provides automated process management,
hosting management, and logging for the compute. To use the Agent, you must have your game
server build integrated with the server SDK for Amazon GameLift Servers version 5.x or later.

The Amazon GameLift Servers Agent is externally available for use with Amazon GameLift Servers fleets that are not managed EC2
fleets. (Managed EC2 fleets handle the Agent's tasks automatically.) You can opt to run
Amazon GameLift Servers fleets, including Anywhere fleets, with or without the Agent. Without the Agent, you
must provide an alternative solution to completing the required tasks.

When deployed to a compute, the Amazon GameLift Servers Agent should be launched before any game server
processes are started. On launch, the Agent completes the following tasks:

- Registers the compute with an Amazon GameLift Servers Anywhere fleet using the [RegisterCompute](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md") API.
- Calls the [GetComputeAuthToken](../apireference/API_GetComputeAuthToken.md "../apireference/API_GetComputeAuthToken.md") API to fetch an authorization token and stores it for use
  by server processes that are running on the compute.
- Sets the WebSocket URL environment variable for the compute, and establishes a
  WebSocket connection to the Amazon GameLift Servers service.
- Requests the latest version of the fleet's runtime configuration from the Amazon GameLift Servers
  service.
- Starts and stops server processes according to the runtime configuration
  instructions.
  Source code and build instructions for the Amazon GameLift Servers Agent are available in the [Amazon GameLift Servers Agent](https://github.com/aws/amazon-gamelift-agent "https://github.com/aws/amazon-gamelift-agent") GitHub.

## About the Agent

The Amazon GameLift Servers Agent is designed to handle the following tasks for your fleets:

**Process management**

- Starts new server processes as defined in runtime instructions. The Agent might use a custom
  runtime configuration that is deployed with the Agent. Alternatively, you can
  provide a `RuntimeConfiguration` as part of your fleet definition.
  This approach has an advantage in that you can modify the fleet's runtime
  configuration at any time. The Agent periodically requests updated runtime
  configurations from the Amazon GameLift Servers service.
- Monitors server process activations and terminates processes when they don't activate in
  time.
- Sends heartbeats to Amazon GameLift Servers. If the Agent fails to send heartbeats, the compute might be marked
  as stale.
- Reports to Amazon GameLift Servers when a server process ends. Amazon GameLift Servers uses this information to monitor game
  server availability for game session placement.
- Emits fleet events for server processes, including:
  - `SERVER_PROCESS_INVALID_PATH`: The game server process
    launch parameters were incorrectly configured.
  - `SERVER_PROCESS_TERMINATED_UNHEALTHY`: The game server
    process did not report a valid health check within 3 minutes of
    activating and was therefore terminated.
  - `SERVER_PROCESS_FORCE_TERMINATED`: The game server process
    did not exit cleanly after `OnProcessTerminate()` was sent
    within 30 seconds.
  - `SERVER_PROCESS_CRASHED`: A game server process crashed for
    some reason.

**Compute management**

- Receives messages from the Amazon GameLift Servers service to shut down the compute.
- Prompts the compute to be terminated by Amazon GameLift Servers.

**Logging**

- Uploads logs to an Amazon S3 bucket in your AWS account.
