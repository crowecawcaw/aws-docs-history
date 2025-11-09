# How hosting with Amazon GameLift Servers works

Amazon GameLift Servers is a service that provides dedicated, low-cost servers, infrastructure provisioning, scaling, and session management for your session-based multiplayer games. The service offers flexible tools and features that you can customize for your games or use in collaboration with your own systems. Take advantage of Amazon GameLift Servers managed hosting so you can focus on creating gameplay experiences rather than managing server operations.

This topic describes the core components of a complete Amazon GameLift Servers hosting solution and how they work together to supply multiplayer game sessions to players.

## Core components of a game hosting solution

A complete Amazon GameLift Servers hosting solution consists of several essential components that work together to deliver multiplayer game experiences. Some of these components are built and managed by you, while others are provided by Amazon GameLift Servers and managed based on your configuration choices. Understanding how these components interact and their respective roles is crucial for developing an effective game hosting solution. The components include:

- Game client runs on player devices.
- Backend service enables game clients to communicate with Amazon GameLift Servers to get game session information
  and join games.
- Game server software runs on game hosting resources and hosts game sessions for a group of
  players.
- Placement system initiates game sessions and matches players to games.
- Game hosting fleets provide game servers in one or more geographic locations.
- Game hosting management system monitors game hosting status and manages capacity.

![Game architecture with managed Amazon GameLift Servers.](images/game_architecture.png)

### Game client

The game client is your game software that runs on a player's device. It initiates player placement into a game session by communicating with a backend service and connects directly to a game server to participate in gameplay.

###### Key functions for game hosting

- Send join requests to the backend service. Include relevant player data and game session data as part of the join request.
- Collect latency data for the game client and include that information in the join request.
- Receive game session connection information from the backend service and use it to connect to a game server.
- Handle session connection scenarios such as player verification, match acceptance for Amazon GameLift Servers FlexMatch, session interruptions, or disconnects.

###### Who builds it

You add game hosting functionality to your game client software and set up communication with the backend service.

### Backend service

The backend service is a coordination layer between game clients and the Amazon GameLift Servers
service. It controls all communication with the service to make requests for game
session placements and to retrieve game session and player session information. Use
of a backend service is a best practice that maintains secure communication with the
service on behalf of game clients and avoids having to share sensitive AWS
credentials and permissions with game clients.

Your backend service implements a player grouping strategy for your game sessions.
You have a lot of flexibility in how players end up in a game session. You might set
up a game session browser for players or support player-defined parties. Or you
might pool game session requests as they come in, form player groups (possibly with
pre-sorting), and start a game session for each group. With FlexMatch matchmaking, you
can form player matches and backfill existing matches.

###### Key functions for game hosting

- Authenticate communications from game clients.
- Make requests to Amazon GameLift Servers to start new game sessions, get game session information, or join existing game sessions. Include relevant game session and player data in requests as needed.
- Optionally create requests for player sessions to more closely monitor game session availability. Use player sessions to reserve game session slots, validate players when they connect, and track player disconnects.
- Respond to game clients with game session connection details and other information as requested.

###### Who builds it

You build the backend service in an environment that's managed by you to support your game requirements and implement how players get into games. Integrate the AWS SDK to make calls to the Amazon GameLift Servers service API. Optionally build your backend service on AWS using services such as AWS Lambda, Amazon Simple Storage Service (Amazon S3), and Amazon Cognito.

### Game server

The game server is your custom server software that manages game state, processes player actions, and synchronizes gameplay across multiple connected players. The game server maintains communication with the Amazon GameLift Servers service to manage game session hosting.

###### Key functions for game hosting

- Communicate with Amazon GameLift Servers to:
  - report status (ready to host sessions, ready to accept players, health status).
  - respond to service calls (start or end game sessions).

- Manage game session lifecycle to host one game session at a time per process.
- Coordinate with other AWS services for added functionality.
- Optionally validate new player connections.

###### Who builds it

You build your game server software. You integrate the server SDK for Amazon GameLift Servers and add functionality to establish a connection with the service and support game session management.

### Game hosting fleet

The hosting fleet is a collection of computing resources that run your game servers. Fleet resources can be distributed across multiple geographic locations to provide low-latency gameplay to players wherever they are. Each fleet resource runs one or more game server processes, which communicates directly with Amazon GameLift Servers. Each game server process can host one game session at a time.

Fleet characteristics and functionality vary based on the fleet's hosting type. Managed fleets deploy resources to the AWS Cloud and are managed by Amazon GameLift Servers. Anywhere fleets are customer-provided compute resources that are managed outside of Amazon GameLift Servers.

###### Key functions for game hosting

- Provision game server hosting resources.
  - Managed fleets deploy cloud-based Amazon EC2 instances with a wide range of configuration settings.
    A fleet configuration determines the computing power of each
    instance in the fleet, the physical location of instances, and other
    details. Managed fleets add or remove EC2 instances in response to
    capacity scaling
  - Anywhere fleet deployments are self-managed. The fleet can consist of physical hardware or other cloud resources, and be configured as needed.

- Install runtime environment and game server software.
  - Managed Amazon EC2 fleet instances are deployed with your game server build and an Amazon Machine Image (AMI) with a compatible runtime environment.
  - Managed container fleet instances are deployed with your game server build and a container-optimized AMI with Docker tools and other components to work with Amazon ECS.
  - Anywhere fleets are deployed with your chosen game server software and operating system.

- Manage game server process life cycle. Apply pre-configured runtime instructions to start and stop processes on each fleet resource.

###### Who builds it

This depends on the fleet's hosting type:

- Managed Amazon EC2 fleets: You upload your game server build to Amazon GameLift Servers, which stores it for deployment to fleet instances. Amazon GameLift Servers provides the fleet's AWS Cloud infrastructure. You configure the fleet and instruct it on how to run game servers on each fleet instance.
- Managed container fleets: You package your game server build and runtime instructions into a container image to store in Amazon ECR for deployment. Amazon GameLift Servers provides the fleet's AWS Cloud infrastructure. You provide a container architecture and configure the fleet to host your containers.
- Anywhere fleets: You provision all infrastructure and manage server software deployment. You create Anywhere fleets to connect your active game hosting resources with Amazon GameLift Servers.

### Game session placement system

The game session placement system locates available game servers to host new game sessions. The system uses real-time information about game server availability to make optimal placement decisions.

In Amazon GameLift Servers, the primary game session placement mechanism is the queue. A game
session queue uses algorithms, which you can configure, to place game sessions for
the best possible outcome. You can prioritize placements based on factors such as
lowest hosting cost and lowest player latency, and you can configure a queue to
search across multiple geographic locations. As an alternative to queues, you can
designate a specific fleet to host your game sessions.

###### Key functions for game hosting

- Process game session placement requests received from the backend service.
- Make placements based on real-time information about hosting resource availability.
- Use player latency data and other data to prioritize placement options (queues only)
- Prompt game server processes to start new game sessions.
- Update game session connection information after the game session is ready to accept players.
- Optionally set up FlexMatch matchmaking to create player matches and request game session placement for matches.

###### Who builds it

Amazon GameLift Servers supplies the placement system. You configure placement behavior through how your backend service makes placement requests and optionally by setting up game session queues and FlexMatch matchmakers. Use the Amazon GameLift Servers console, the AWS SDK, or the AWS CLI to create and configure queues and matchmakers for your game.

### Game hosting management system

The game hosting management system is the operational backbone that coordinates and monitors all aspects of your game hosting solution. This system provides the intelligence and automation that makes Amazon GameLift Servers' placement and scaling capabilities possible.

###### Key functions for game hosting

- Track the real-time status and availability of game server processes, game sessions, and player sessions across all fleets to support game session placement and automatic capacity scaling.
- Monitor fleet health and performance.
- Collect and analyze game hosting activity metrics.
- Provide capacity scaling tools, including automatic scaling based on player demand and fleet utilization.
- Manage updates to game server software and runtime instructions.

###### Who builds it

- Managed fleets: Amazon GameLift Servers provides availability tracking, metrics on game hosting activity and hardware performance, and capacity scaling tools. You use available AWS tools to manage game server software updates, modify runtime instructions, and customize your use of metrics (such as setting up CloudWatch for monitoring). You configure a custom scaling policy and modify as needed.
- Anywhere fleets: Amazon GameLift Servers provides availability tracking and game hosting activity metrics. You manage fleet configuration changes, including updates to game server software and runtime instructions. You create systems to monitor fleet performance and manage fleet capacity scaling.

## How the components work together

###### When a game hosting

compute is deployed

- **Game server software installed**: The compute is installed with
  a runtime environment and your game server build
- **Game server launches**: At least one instance of the game
  server executable is launched, with optional launch parameters, on the
  compute.
- **Game server connects to Amazon GameLift Servers**: As part of its startup actions, the game server process calls the server SDK to initialize a connection to the service.
- **Game server reports ready to host a game session**: The game server process completes startup actions, then calls the server SDK to report readiness. It begins reporting health status based on its configuration.
- **Amazon GameLift Servers tracks availability**: The service records the game server process's availability to game session placement. It also updates metrics for fleets, instances, and game sessions to track usage and capacity.
- **Game server waits for game session assignment**: The game server process maintains its idle status while it waits for a prompt to start a game session.

###### When a player wants to join a game

- **Player initiates a game**: A player launches your game client, authenticates with your backend service, and asks to join a game.
- **Backend service requests a game session**: Your backend service calls Amazon GameLift Servers to find or create a suitable game session, based on its player grouping strategy. The request might include player or game data for use in the game session.
- **Amazon GameLift Servers places the game session**: When starting a new game
  session, the placement system identifies an optimal location to host the session
  and selects an available game server process. The service prompts the selected
  process to start a new game session and passes any player or game data. If
  FlexMatch matchmaking is in use, the matchmaker first creates a match, then
  requests placement for the match.
- **Game server starts the game session**: The game server initiates steps to start a game session. When complete, it reports to Amazon GameLift Servers that it's ready to accept player connections.
- **Connection information delivered to game client**: After the
  game server updates its status, Amazon GameLift Servers provides the game session connection
  information. The backend service receives this information and delivers it to
  the game client.
- **Player connects to the game session**: The game client uses the connection information to connect directly to the game server and begin gameplay.
- **Amazon GameLift Servers monitors game session status**: The game server process reports health status, optional player connection status, and game session status to track ongoing game session availability.
- **Game server process shuts down**: The game server process ends
  the game session, reports status, and then shuts itself down.
