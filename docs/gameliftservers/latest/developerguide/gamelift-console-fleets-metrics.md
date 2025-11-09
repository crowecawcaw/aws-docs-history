# Fleet details in the Amazon GameLift Servers console

Access a **Fleet** detail page from the dashboard or the
**Fleets** page by choosing the fleet name.

On the fleet details page you can take the following actions:

- Update a fleet's attributes, port settings, and runtime configuration.
- Add or remove fleet locations.
- Change fleet capacity settings.
- Set or change target-tracking auto scaling.
- Delete a fleet.

## Details

###### Fleet settings

- **Fleet ID** – An identifier assigned to the fleet.
  This ID is unique within the AWS Region where the fleet is created.
- **Fleet name** – A friendly name given to the
  fleet.
- **ARN** – A unique identifier assigned to this fleet.
  A fleet's ARN identifies it as an Amazon GameLift Servers resource and specifies the region and
  AWS account.
- **Description** – A short identifiable description of
  the fleet.
- **Status** – Current status of the fleet, which may be
  **New**, **Downloading**,
  **Building**, and **Active**.
- **Creation time** – The date and time when the fleet
  was created.

###### Note

A fleet displays a warning icon for fleets that were created more than 90
days ago. As a best practice, we recommend replacing fleets every 30 days to
maintain a secure and up-to-date runtime environment for your hosted game
servers. For guidance, see [Security best practices for Amazon GameLift Servers](security-best-practices.md "security-best-practices.md").

- **Compute type** – The type of compute
  used to host your games. A fleet can be a **Managed
  EC2**, **Managed container**, or **Anywhere** fleet.
- **Operating system** – The Amazon Machine Image (AMI)
  that's deployed to every instance in the fleet. The AMI version is the latest
  version available at the time the fleet was created.
- **Certificate type** – The status of the fleet's
  ability to use a TLS certificate for authenticating a game server and encrypting
  all client/server communication.
- **Fleet type** – The availability of the
  instances used to host your games, which can potentially impact hosting costs. A
  fleet can use **On-Demand** (always available) or
  **Spot** (availability varies) instances.
- **EC2 instance type** – Amazon EC2 [instance type](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") selected for
  the fleet when it was created.
- **Instance role ARN** – An AWS IAM role that manages
  access to your other AWS resources, if one was provided during fleet
  creation.
- **Instance role credentials provider** – An AWS IAM
  role that manages access to your other AWS resources, if one was provided
  during fleet creation.
- **Metric group name** – The group used to aggregate
  metrics for multiple fleets.
- **Game scaling protection policy** –
  Indicates whether the fleet's game session protection is enabled, which
  prevents active game sessions from ending prematurely during a scale-down event.
- **Maximum game sessions per player** – The maximum
  number of sessions a player can create during the **Policy
  period**.
- **Policy period** – The length of time used to limit a
  player's number of sessions created.

###### Build details

The **Build details** section displays the build
hosted on the fleet. Select the build name to see the full build detail page.

###### Runtime configuration

The **Runtime configuration** section displays the
server processes to launch on each instance. It includes the path for the game
server executable and optional launch parameters.

###### Game session activation

The **Game session activation** section displays the number of
server processes that launch at the same time and how long to wait for the process
to activate before terminating it.

###### EC2 port settings

The **Ports** section displays the fleet's connection
permissions, including IP address and port setting ranges.

## Metrics

The **Metrics** tab displays a graphical representation of fleet
metrics over time. For more information about using metrics in Amazon GameLift Servers, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

## Events

The **Events** tab provides a log of all events that have occurred on
the fleet, including the event code, message, and time stamp. See [Event](../../../gamelift/latest/apireference/API_Event.md "../../../gamelift/latest/apireference/API_Event.md") descriptions in the
Amazon GameLift Servers API Reference.

## Scaling

The **Scaling** tab contains information about fleet
capacity, including the current status and capacity changes over time. It also provides
tools to update capacity limits and manage auto scaling.

###### Scaling capacity

View current fleet capacity settings for each fleet location. For more information
about changing limits and capacity, see [Scaling game hosting capacity with Amazon GameLift Servers](fleets-manage-capacity.md "fleets-manage-capacity.md").

- **AWS Location** – Name of a location
  where fleet instances are deployed.
- **Status** – Hosting status of the fleet
  location. Location status must be `ACTIVE` to be able to host
  games.
- **Min size** – The smallest number of
  instances that must be deployed in the location.
- **Desired instances** – The target number
  of active instances to maintain the location. When active instances and desired
  instances aren't' the same, a scaling event is started to start or shut down
  instances as needed until active instances equals desired instances.
- **Max size** – The most instances that can
  be deployed in the location.
- **Available** – The service limit on
  instances minus the number of instances in use. This value tells you the maximum
  number of instances that you can add to the location.

###### Auto scaling policies

This section covers information about auto scaling policies that are applied to
the fleet. You can set up or update a target-based policy. The fleet's rule-based
policies, which must be defined using the AWS SDK or CLI, are displayed here. For
more information about scaling, see [Auto-scale fleet capacity with Amazon GameLift Servers](fleets-autoscaling.md "fleets-autoscaling.md").

###### Scaling history

View graphs of capacity changes over time.

## Locations

The **Locations** tab lists all locations where fleet
instances are deployed. Locations include the fleet's home Region and any remote
locations that have been added. You can add or remove locations directly in this
tab.

- **Location** – Name of a location where
  fleet instances are deployed.
- **Status** – Hosting status of the fleet
  location. Location status tracks the process of activating the first instances
  in the location. Location status must be `ACTIVE` to be able to host
  games.
- **Active instances** – The number of
  instances with server processes running on the fleet location.
- **Active servers** – The number of game
  server processes able to host game sessions in the fleet location.
- **Game sessions** – The number of game
  sessions active on instances in the fleet location.
- **Player sessions** – The number of player
  sessions, which represent individual players, that are participating in game
  sessions that are active in the fleet location.

## Game sessions

The **Game sessions** tab lists past and present game
sessions hosted on the fleet, including some detail information. Choose a game session
ID to access additional game session information, including player sessions. For more
information about player sessions, see [Game and player sessions in
the Amazon GameLift Servers console](gamelift-console-game-player-sessions-metrics.md "gamelift-console-game-player-sessions-metrics.md").
