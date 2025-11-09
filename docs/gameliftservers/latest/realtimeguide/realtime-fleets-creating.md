# Create a hosting fleet for Amazon GameLift Servers Realtime

When you're ready to deploy Realtime servers for your game, create an Amazon GameLift Servers managed EC2 fleet. This topic assumes you've completed the following steps:

- Created a Realtime script that's configured for your game. See [Customize an Amazon GameLift Servers Realtime script](realtime-script.md "realtime-script.md").
- Uploaded your Realtime script to Amazon GameLift Servers. See [Upload a script for Amazon GameLift Servers Realtime servers](realtime-script-uploading.md "realtime-script-uploading.md").
  **To create a managed EC2 fleet**

Use either the Amazon GameLift Servers console or the AWS Command Line Interface (AWS CLI) to create a managed EC2 fleet. If you're exploring the Realtime servers feature or want to get your servers
up and running fast, follow the guidance for a minimal fleet configuration.

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), use the navigation pane to open the
**Managed EC2, Fleets** page. Choose **Create
managed EC2 fleet** to start the fleet creation workflow.

**Step 1 Define managed EC2 fleet details**

###### For a minimal fleet configuration:

- Provide a fleet name.
- Specify a Realtime script to deploy.
- Skip the Additional details and Tags sections to use default settings.

1. In the **Fleet details** section:
   1. Enter a fleet **Name**. Fleet names are descriptive only, useful for
      sorting or filtering a list of fleets. They don't need to be unique.
   2. Provide a short fleet **Description** to include any custom information
      you want to capture about the fleet.
   3. Select **Binary type, Script**, and use the
      dropdown list to choose a Realtime server script that you've previously
      uploaded to Amazon GameLift Servers.

2. Set **Additional details** as
   needed.
   1. If your game server needs to access other AWS
      resources in your account, specify an IAM
      **Instance role** with the
      necessary permissions. For more information,
      including how to authorize other server-side
      applications (such as CloudWatch agent), see
      [Communicate with other AWS resources from your fleets](../../../gameliftsevers/latest/developerguide/gamelift-sdk-server-resources.md "../../../gameliftsevers/latest/developerguide/gamelift-sdk-server-resources.md").
      This setting can't be changed after you create the
      fleet.

   You must create the role before you create a fleet that uses
   it. In addition, to create a fleet with an instance role, your
   AWS user must have IAM `PassRole` permission. See
   [IAM permission examples for Amazon GameLift Servers](../../../gameliftsevers/latest/developerguide/gamelift-iam-policy-examples.md "../../../gameliftsevers/latest/developerguide/gamelift-iam-policy-examples.md"). 2. Turn on the **Generate a TLS
   certificate** option to set up
   authentication and encryption for your game. Game
   clients use this certificate to authenticate a game
   server when connecting and encrypt all client/server
   communication. For each instance in a TLS-enabled
   fleet, Amazon GameLift Servers also creates a new DNS entry with the
   certificate. This setting can't be changed after you
   create the fleet. 3. Amazon GameLift Servers emits metric data for each individual fleet. If you want to combine metric data for multiple fleets,
   specify a **Metric group** name. Use the same metric group
   name for all fleets that you want to combine
   metrics for. Use CloudWatch to view the aggregated metric group data.

3. Add **Tags** to the fleet
   resource. Each tag consists of a key and an optional value,
   both of which you define. Assign tags to AWS resources
   that you want to categorize, such as by
   purpose, owner, or environment. Choose **Add new
   tag** for each tag that you want to add.
4. Choose **Next** to continue the
   workflow.

**Step 2 Define instance details**

In this step, select the type of hardware resources to use for
your game servers and specify where you want to deploy them. By
choosing multiple locations, you can deploy your game server to a
wider geographical location, which puts them closer to your players
and minimizes latency. All EC2 instances in a fleet must be the same
type. Not all instance types are available in all locations.

###### For a minimal fleet configuration:

- Start with deploying to the home location only. You
  don't need to add remote locations for initial
  development and testing.
- Set fleet type set to "On-Demand". Spot fleets require
  additional setup work.
- Set instance type to "c5.large". This commonly used
  instance type is available in all AWS Regions. You can
  optimize your hardware usage later.

1. In **Instance deployment**, specify fleet
   locations and type.
   1. Select one or more additional
      **Locations** where you want to
      deploy fleet instances. These remote locations are
      added to the fleet's home location (which is
      pre-selected), which is the AWS Region where
      you're creating this fleet. You can select remote
      locations from all AWS Regions and Local Zones
      that Amazon GameLift Servers supports.

   To learn more about supported locations, including
   how to use an AWS Region that isn't enabled by
   default, see
   [Amazon GameLift Servers service locations](../../../gameliftsevers/latest/developerguide/gamelift-regions.md "../../../gameliftsevers/latest/developerguide/gamelift-regions.md") for managed EC2
   hosting. Also review Amazon GameLift Servers [quotas](https://aws.amazon.com/general/latest/gr/gamelift.html#limits_gamelift "https://aws.amazon.com/general/latest/gr/gamelift.html#limits_gamelift") on locations per fleet. 2. Choose to use either **On-demand** or
   **Spot** instances for this fleet. For
   more information about fleet types, see
   [On-Demand Instances versus Spot Instances](../developerguide/gamelift-compute.md#gamelift-compute-spot "../developerguide/gamelift-compute.md#gamelift-compute-spot").

2. Choose an Amazon EC2 **Instance configuration**
   that meets your needs and is available in all your selected
   locations. This list is filtered based on your current
   location and fleet type selections. You can filter it
   further by other factors such as instance type family and
   architecture. After you create the fleet, you can't change
   the instance type.

Some locations have limited instance type options.
If your preferred instance type is not available for all
locations, choose the location availability value to view
full details. To accommodate all locations, you might need
to create separate fleets with different instance types.

For more information about choosing an instance type, see
[Instance types](../developerguide/gamelift-compute.md#gamelift-compute-instance "../developerguide/gamelift-compute.md#gamelift-compute-instance"). 3. Choose **Next** to continue the
workflow.

**Step 3 Configure runtime**

In this step, describe how you want each instance in the fleet to
run Realtime server processes. Enter a separate server process line item
for each executable to run on an instance, and decide how many of
each server process to run concurrently. Open ports on each instance
to allow players to connect directly to game servers. You can update
these fleet settings at any time.

###### For a minimal fleet configuration:

- Define a single server process line item for your game
  server script. If your game server requires other
  processes to be running, create a definition for each of
  these as well.
- Use the default number of concurrent processes (1) for
  each line item.
- Skip game session activation settings.
- Specify a single port number.
- Skip game session resource settings.

1. Create a **Runtime configuration** to
   instruct Amazon GameLift Servers on how to run server processes on each
   instance in the fleet. You can change a fleet's runtime
   configuration at any time after deployment.
   1. Enter the **Launch path** to an
      your Realtime script file. Realtime servers run
      on Linux instances, so the path to the server script
      is always `/local/game`. Example:
      `MyRealtimeLaunchScript.js`.
   2. Specify the number of **Concurrent
      processes** to run on each instance. For
      a game server executable, each process can host one
      game session, so concurrent processes determines the
      number of game sessions the instance can host
      simultaneously.

   Review the Amazon GameLift Servers
   [quotas](../../../general/latest/gr/gamelift.md#limits_gamelift "../../../general/latest/gr/gamelift.md#limits_gamelift") on server processes per instance.
   These quotas apply to the total concurrent processes
   for all configurations. If you configure the fleet
   to exceed them, the fleet can't activate.

2. Use the **Game session activation**
   defaults or customize them for your game. If the runtime
   configuration calls for multiple concurrent game server
   process per instance, these settings determine how quickly
   new game sessions can start up.
   1. Set **Max concurrent game
      session activation** to limit the number
      of game servers on an instance that are preparing a
      new game session. This setting is useful when
      launching multiple new game sessions is
      resource-intensive and might impact the performance
      of other running game sessions.
   2. Set the **New activation
      timeout** to reflect the maximum amount
      of time a new game session should take to complete
      activation and report ready to host players. Amazon GameLift Servers
      terminates a game session activation if it exceeds
      this value.

3. Open **EC2 port settings** to allow
   inbound traffic to access server processes on the fleet.
   These settings aren't required to create a fleet, but you do
   need set them before players can connect to game sessions on
   the fleet.

For each port setting, choose the
**Type** of data transfer protocol to
use for communication between your game client and game
server. Provide a **Port range** (in format
`nnnnn[-nnnnn]`) and an **IP address
range** using CIDR notation (such as
`0.0.0.0/0` which allows access to
anyone).

If you need to set multiple non-consecutive ranges, create
multiple port settings. 4. Specify optional **Game session resource
settings**. You can update these settings any
time after deployment.

    1. Turn **Game scaling protection
     policy** on or off for all instances in
     the fleet. During a scale-down event, Amazon GameLift Servers won't
     terminate protected fleet instances if they're
     hosting active game sessions.
    2. Set a maximum **Resource creation
     limit** if you want to restrict the
     number of game sessions that one player can create
     during a specified time span.

5. Choose **Next** to continue the
   workflow.

**Step 5 Review and create**

Review your settings before creating the fleet. Although some
settings can be updated later (see
[Update an Amazon GameLift Servers fleet configuration](../developerguide/fleets-editing.md "../developerguide/fleets-editing.md")), changes to the following
settings aren't allowed after the fleet has been created:

- Game server binary: To deploy an update to your Realtime server
  script, you must create a new fleet.
- Additional options, including instance role and TLS
  certificate generation.
- Instance details, including fleet type (Spot or On-Demand)
  and EC2 instance type.

When you're ready to deploy the new fleet, choose
**Create**. Amazon GameLift Servers immediately begins the fleet
activation process, assigning a unique ID and placing the fleet in
`NEW` status. Track the fleet's progress from the
**Fleets** page.View the details page for the
fleet and go to the **Events** tab.

You can adjust a fleet's hosting capacity after the fleet reaches
ACTIVE status. Amazon GameLift Servers initially deploys a fleet with a single
instance in each fleet location. and you adjust capacity by adding
instances to each location. For more information, see
[Scaling game hosting capacity with Amazon GameLift Servers](../../../https:/docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-manage-capacity.md "../../../https:/docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-manage-capacity.md").

AWS CLI
Use the [`create-fleet`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet.html") command to create a fleet of compute
type `EC2`. Amazon GameLift Servers creates the fleet resource in your current default
AWS Region (or you can add a --region tag to specify a different
AWS Region).

**Create a minimal managed fleet**

The following example request creates a new fleet with the minimal settings
that are required to deploy a fleet with running game servers that game clients
can connect to. The new fleet has these characteristics:

- It specifies a Realtime server script, which is uploaded to Amazon GameLift Servers
  and in `READY` status.
- Is uses c5.large On-Demand Instances.
- It sets the fleet's home AWS Region to `us-west-2` and
  deploys instances to that Region only.
- Based on the runtime configuration, each instance in the fleet runs
  one game server process, which means that each instance can host
  only one game session at a time. By default, game session activation
  timeout is set to 300 seconds, with no limit on the number of
  concurrent activations.
- Players can connect to game servers using port
  `33435`.
- All other features are either turned off or use default
  settings.

```
aws gamelift create-fleet \
    --name MinimalRealtimeFleet123 \
    --description "A basic test fleet" \
    --region us-west-2 \
    --ec2-instance-type c5.large \
    --fleet-type ON_DEMAND \
    --script-id script-1111aaaa-22bb-33cc-44dd-5555eeee66ff \
    --runtime-configuration "ServerProcesses=[{LaunchPath=/local/game/megafrograce.js, ConcurrentExecutions=1}]" \
    --ec2-inbound-permissions "FromPort=33435,ToPort=33435,IpRange=0.0.0.0/0,Protocol=UDP"
```

**Create a fully configured managed
fleet**

The following example request creates a production fleet with settings for all
optional features. The new fleet has these characteristics:

- It specifies a Realtime server script, which has been uploaded to
  Amazon GameLift Servers and is in `READY` status.
- It uses c5.large On-Demand Instances with the operating system that
  matches the selected game build.
- It sets the fleet's home AWS Region to `us-west-2` and
  deploys instances to the home Region and one remote location
  `sa-east-1`.
- Based on the runtime configuration:
  - Each compute in the fleet runs 10 game server processes with
    the same launch parameters, which means that each compute can
    host up to 10 game sessions simultaneously.
  - On each compute, only two game sessions can be activating at
    the same time. Activating game sessions must be ready to host
    players within 300 seconds (5 minutes) or be terminated.

- Players can connect to game servers using a port in the following
  range `33435 to 33535`.
- It generates a TLS certificate for encrypted communication between
  game client and server.
- All game sessions in the fleet have game session protection turned
  on.
- Individual players are limited to creating three new game sessions
  within a 15-minute period.
- Metrics for this fleet are included in the metric group
  `AMERfleets`, which (for this example) aggregates metrics
  for a group of fleets in North, Central, and South America.

```
aws gamelift create-fleet \
    --name ProdRealtimeFleet123 \
    --description "A fully configured prod fleet" \
    --ec2-instance-type c5.large \
    --region us-west-2 \
    --locations "Location=sa-east-1" \
    --fleet-type ON_DEMAND \
    --script-id script-1111aaaa-22bb-33cc-44dd-5555eeee66ff \
    --certificate-configuration "CertificateType=GENERATED" \
    --runtime-configuration "GameSessionActivationTimeoutSeconds=300, MaxConcurrentGameSessionActivations=2, ServerProcesses=[{LaunchPath=/local/game/megafrograce.js, ConcurrentExecutions=10}]" \
    --new-game-session-protection-policy "FullProtection" \
    --resource-creation-limit-policy "NewGameSessionsPerCreator=3, PolicyPeriodInMinutes=15" \
    --ec2-inbound-permissions "FromPort=33435,ToPort=33535,IpRange=0.0.0.0/0,Protocol=UDP" \
    --metric-groups  "AMERfleets"
```

If the create-fleet request is successful, Amazon GameLift Servers returns a set of fleet
attributes that includes the configuration settings you requested and a new
fleet ID. Amazon GameLift Servers then initiates the fleet activation process and sets the fleet
status and the location statuses to **New**. You
can track the fleet's status and view other fleet information using these CLI
commands:

- [describe-fleet-events](../../../cli/latest/reference/gamelift/describe-fleet-events.md "../../../cli/latest/reference/gamelift/describe-fleet-events.md")
- [describe-fleet-attributes](../../../cli/latest/reference/gamelift/describe-fleet-attributes.md "../../../cli/latest/reference/gamelift/describe-fleet-attributes.md")
- [describe-fleet-capacity](../../../cli/latest/reference/gamelift/describe-fleet-capacity.md "../../../cli/latest/reference/gamelift/describe-fleet-capacity.md")
- [describe-fleet-port-settings](../../../cli/latest/reference/gamelift/describe-fleet-port-settings.md "../../../cli/latest/reference/gamelift/describe-fleet-port-settings.md")
- [describe-fleet-utilization](../../../cli/latest/reference/gamelift/describe-fleet-utilization.md "../../../cli/latest/reference/gamelift/describe-fleet-utilization.md")
- [describe-runtime-configuration](../../../cli/latest/reference/gamelift/describe-runtime-configuration.md "../../../cli/latest/reference/gamelift/describe-runtime-configuration.md")
- [describe-fleet-location-attributes](../../../cli/latest/reference/gamelift/describe-fleet-location-attributes.md "../../../cli/latest/reference/gamelift/describe-fleet-location-attributes.md")
- [describe-fleet-location-capacity](../../../cli/latest/reference/gamelift/describe-fleet-location-capacity.md "../../../cli/latest/reference/gamelift/describe-fleet-location-capacity.md")
- [describe-fleet-location-utilization](../../../cli/latest/reference/gamelift/describe-fleet-location-utilization.md "../../../cli/latest/reference/gamelift/describe-fleet-location-utilization.md")

You can change the fleet's capacity and other configuration settings as needed
using these commands:

- [update-fleet-attributes](../../../cli/latest/reference/gamelift/update-fleet-attributes.md "../../../cli/latest/reference/gamelift/update-fleet-attributes.md")
- [update-fleet-capacity](../../../cli/latest/reference/gamelift/update-fleet-capacity.md "../../../cli/latest/reference/gamelift/update-fleet-capacity.md")
- [update-fleet-port-settings](../../../cli/latest/reference/gamelift/update-fleet-port-settings.md "../../../cli/latest/reference/gamelift/update-fleet-port-settings.md")
- [update-runtime-configuration](../../../cli/latest/reference/gamelift/update-runtime-configuration.md "../../../cli/latest/reference/gamelift/update-runtime-configuration.md")
- [create-fleet-locations](../../../cli/latest/reference/gamelift/create-fleet-locations.md "../../../cli/latest/reference/gamelift/create-fleet-locations.md")
- [delete-fleet-locations](../../../cli/latest/reference/gamelift/delete-fleet-locations.md "../../../cli/latest/reference/gamelift/delete-fleet-locations.md")
