# Create an Amazon GameLift Servers Anywhere fleet

This topic describes how to create an Amazon GameLift Servers Anywhere fleet. With an Anywhere fleet, you
can use core Amazon GameLift Servers game session management features while hosting game sessions with your
own compute resources. Create an Anywhere fleet for your on-premises hardware or other
cloud-based resources.

Anywhere fleets are commonly used alongside Amazon GameLift Servers managed fleets in a hybrid hosting
solution. They also provide useful test environments when developing a game for hosting with
Amazon GameLift Servers. See these topics to learn more about when and how to incorporate Amazon GameLift Servers Anywhere
fleets into a game hosting solution:

- [Hybrid hosting](gamelift-intro-flavors.md#gamelift-intro-flavors-hosting-hybrid "gamelift-intro-flavors.md#gamelift-intro-flavors-hosting-hybrid")
- [Setting up a hosting fleet with Amazon GameLift Servers](fleets-intro.md "fleets-intro.md")
- [Set up for iterative development with Amazon GameLift Servers Anywhere](integration-dev-iteration.md "integration-dev-iteration.md")
  Because Anywhere fleets are self-managed, setting up a fleet requires some additional work. To get an Anywhere
  fleet ready to host game sessions and players, you need to complete the following tasks:

###### Topics

- [Before you start](#fleet-anywhere-start "#fleet-anywhere-start")
- [Create a custom location](#fleet-anywhere-location "#fleet-anywhere-location")
- [Create an Anywhere fleet](#fleet-anywhere-create "#fleet-anywhere-create")
- [Add a compute to the fleet](#fleet-anywhere-compute "#fleet-anywhere-compute")
- [Start a game server](#fleet-anywhere-process "#fleet-anywhere-process")

## Before you start

Before creating an Anywhere fleet, do the following tasks. For more detailed guidance, see the
[Development roadmap for hosting with Amazon GameLift Servers Anywhere](gamelift-roadmap-anywhere.md "gamelift-roadmap-anywhere.md") or [Development roadmap for hybrid hosting
with Amazon GameLift Servers](gamelift-roadmap-hybrid.md "gamelift-roadmap-hybrid.md").

- **Integrate your game server code with the Amazon GameLift Servers server
  SDK version 5.x (or higher).** You don't need to complete all game
  integration tasks, just those required for a game server build. A common
  practice is to set up your local machine as an Anywhere fleet and use a command
  line interface to test your game server integration (see [Set up local testing with Amazon GameLift Servers Anywhere](integration-testing.md "integration-testing.md")). You
  can incorporate additional components (such as an Amazon GameLift Servers enabled game client) as
  your develop them.
- **Package your game server software for installation onto
  your Anywhere fleet computes.** The package should include your
  integrated game server build and all support software needed to run your game
  server.
- **Decide whether to use the Amazon GameLift Servers Agent with your Anywhere
  fleet.** The Agent is an on-compute process management tool that
  automates some of the key tasks related to managing server processes and
  computes for use with Amazon GameLift Servers. For more information, see [Work with the Amazon GameLift Servers Agent](integration-dev-iteration-agent.md "integration-dev-iteration-agent.md").

## Create a custom location

Create a custom location to represent the physical location of your compute resources.
When creating an Anywhere fleet, you must have at least one custom location already defined.
You can create additional custom locations and add them to an existing fleet at any
time.

**To create a custom location**

Use either the Amazon GameLift Servers console or the AWS Command Line Interface (AWS CLI) to create a custom location.

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), use the navigation pane to open the
**Locations** page. Choose **Create
location** to open the Create dialog box.

1. In the dialog box, enter a **Location name**.
   As a best practice, use a name that describes a meaningful location for
   a set of compute resources. It might be geographic locations, a data
   center name, or other location identifier. Amazon GameLift Servers appends the name of
   your custom location with **custom-**.
2. (Optional) Add tags to your custom location. Each tag consists
   of a key and an optional value, both of which you define. Assign tags to
   AWS resources that you want to categorize in useful ways, such as by
   purpose, owner, or environment. Choose **Add new tag**
   for each tag that you want to add.
3. Choose **Create**.

AWS CLI
Create a custom location using the [`create-location`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-location.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-location.html") command. Provide a
`location-name` value, which must start with
`custom-`. As a best practice, use a name that describes a meaningful
location for a set of compute resources. It might be geographic locations, a
data center name, or other location identifier.

```
aws gamelift create-location \
    --location-name custom-`location-1`
```

Output

```
{
    "Location": {
        "LocationName": "custom-location-1",
        "LocationArn": "arn:aws:gamelift:us-east-1:111122223333:location/custom-location-1"
    }
}
```

## Create an Anywhere fleet

Create an Anywhere fleet for a set of compute resources that you own. A new Anywhere
fleet starts empty; you add computes to the fleet by registering them.

On creation, a new Anywhere fleet quickly moves through fleet statuses from
`NEW` to `ACTIVE`. You can add computes to the fleet after it
reaches `ACTIVE`.

**To create an Anywhere fleet**

Use either the Amazon GameLift Servers console or the AWS Command Line Interface (AWS CLI) to create an Anywhere fleet.

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), use the navigation pane to open the
**Fleets** page. Choose **Create
fleet** to start the fleet creation workflow.

**Step 1 Choose compute type**
Select the **Anywhere** option and choose **Next**.

**Step 2 Define fleet details**

In this step, specify some key fleet-wide settings.

1. Fill out the **Fleet details** section:
   1. Enter a fleet **Name**. We recommend using a
      fleet naming pattern that makes it easier to identify fleet
      types when viewing lists of fleets.
   2. Provide a short **Description** of the
      fleet.

2. Set these optional **Additional details**
   as needed. You can update these fleet settings
   later.
   1. When creating a fleet for production or pre-prod
      testing, use this setting to specify a per-hour
      **Cost** value for the fleet's
      computes. Amazon GameLift Servers can use this information during
      the game session placement process to select
      hosting resources based on cost.
   2. If you want to combine metric data for this fleet
      and others, specify a **Metric
      group** name. Use the same metric group
      name for all fleets that you want to combine
      together. View metrics for the metric group to see
      the aggregated data.

3. Add optional tags to your custom location. Each tag
   consists of a key and an optional value, both of which
   you define. Assign tags to AWS resources that you want
   to categorize in useful ways, such as by purpose, owner,
   or environment. Choose **Add new tag**
   for each tag that you want to add.
4. Choose **Next** to continue the
   workflow.

**Step 3 Select custom locations**

In this step, identify the physical location of the computes that
you plan to add to this fleet. You can specify one or more
locations now, and you can add or remove locations later as
needed.

1. In **Custom locations**, select one
   or more locations for the fleet's computes. The list
   includes all custom locations that have been defined in
   your currently selected AWS Region. To define a new
   custom location that you want to add to the fleet,
   choose **Create location**.
2. Choose **Next** to continue the
   workflow.

**Step 4 Review and create**

Review your settings before creating the fleet.

When you're ready to deploy the new fleet, choose
**Create**. Amazon GameLift Servers immediately begins the fleet
activation process, assigning a unique ID and placing the fleet in
`NEW` status. You can track the fleet's progress on
the **Fleets** page.

AWS CLI
Use the [`create-fleet`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet.html") command to create a fleet of
compute type `ANYWHERE`. Provide a name and at least one custom
location. Amazon GameLift Servers creates the Anywhere fleet resource in your current default
AWS Region (or you can add a --region tag to specify a different
AWS Region).

The following example request creates a new fleet with the minimal
required settings. Replace `FleetName`
and `custom-location` with your own
information.

```
aws gamelift create-fleet \
--name `FleetName` \
--compute-type ANYWHERE \
--locations "Location=`custom-location`"
```

Example response

```
{
    "FleetAttributes": {
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetArn": "arn:aws:gamelift:us-west-2:111122223333:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "Name": "HardwareAnywhere",
        "CreationTime": "2023-02-23T17:57:42.293000+00:00",
        "Status": "ACTIVE",
        "MetricGroups": [
            "default"
        ],
        "CertificateConfiguration": {
            "CertificateType": "DISABLED"
        },
        "ComputeType": "ANYWHERE"
    }
}
```

On creation, a new Anywhere fleet quickly moves to fleet status
`ACTIVE`. You can add computes to the fleet after it reaches
`ACTIVE`.

Notice that the response doesn't include the fleet locations. You can
retrieve full fleet details by calling
[`describe-fleet-attributes`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-attributes.html") and
[`describe-fleet-location-attributes`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-location-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-location-attributes.html").

## Add a compute to the fleet

To add a compute resource to a fleet and get it ready to host game sessions, do the
following tasks:

- Register the compute with the fleet. Registration tells Amazon GameLift Servers what physical
  hosting resources are part of the fleet.
- Request an authentication token for the compute. Each game server that runs on
  the compute needs this token to connect to the Amazon GameLift Servers service. Authentication
  tokens are temporary and must be regularly refreshed.

###### Note

If you're deploying your game server software with the Amazon GameLift Servers Agent, you can skip
this step. The Agent automatically registers each compute and maintains a valid
authentication token for the compute. See [Work with the Amazon GameLift Servers Agent](integration-dev-iteration-agent.md "integration-dev-iteration-agent.md").

You can register a compute and request an authentication token by using the AWS CLI
or making programmatic calls to the AWS SDK for Amazon GameLift Servers. These actions are not available
through the Amazon GameLift Servers console.

As a best practice, we recommend automating both of these tasks by adding a startup
script to each compute. The startup script automatically calls both the
`register-compute` and `get-compute-auth-token` commands. You
can also automate tasks to regularly refresh the auth token throughout the life of the
compute and deregister the compute on shut down.

Each of the startup actions returns compute-specific values that you need to store on
the compute. When a game server process launches on the compute, it must pass these
values as server parameters when initializing a connection with the Amazon GameLift Servers service (see
[ServerParameters](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-serverparameters "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-serverparameters") in the
server SDK reference). We recommend that you set these compute-specific values (or their
stored locations) as environment variables. If you're using the Amazon GameLift Servers Agent, this task
is handled for you. The compute-specific values are as follows:

- `register-compute` returns a value for
  `GameLiftServiceSdkEndpoint`. Set this value to the
  `webSocketUrl` server parameter.
- `compute-auth-token` returns the authentication token. Set this
  value to the `authToken` server parameter.

AWS CLI
The following instructions describe how manually submit each request using
the AWS CLI.

**To register a compute**

Call [`register-compute`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/register-compute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/register-compute.html") to register a compute.
Identify the ID of the fleet to add the compute to. Provide the following
compute information: a meaningful name, IP address, and location. The
compute's location must be a custom location that's already associated with
the fleet. If you want to use a different custom location, use the Amazon GameLift Servers
console to update the fleet or call the AWS CLI command [`create-fleet-locations`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet-locations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet-locations.html") to add a custom
location to the fleet.

In the following example, replace the placeholder values for your compute
and fleet. The `fleet-id` value is returned when you create an
Anywhere fleet. You can retrieve full fleet details by calling [`describe-fleet-attributes`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-attributes.html") and [`describe-fleet-location-attributes`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-location-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-location-attributes.html").

```
aws gamelift register-compute \
    --compute-name `HardwareAnywhere` \
    --fleet-id `arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa` \
    --ip-address `10.1.2.3` \
    --location `custom-location-1`
```

Example output

```
{
    "Compute": {
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetArn": "arn:aws:gamelift:us-west-2:111122223333:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "ComputeName": "HardwareAnywhere",
        "ComputeArn": "arn:aws:gamelift:us-west-2:111122223333:compute/HardwareAnywhere",
        "IpAddress": "10.1.2.3",
        "ComputeStatus": "Active",
        "Location": "custom-location-1",
        "CreationTime": "2023-02-23T18:09:26.727000+00:00",
        "GameLiftServiceSdkEndpoint": "wss://us-west-2.api.amazongamelift.com"
    }
}
```

**To request an authentication token**

Call [`get-compute-auth-token`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/get-compute-auth-token.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/get-compute-auth-token.html") to request a valid
authentication token. register a compute. Identify the fleet ID and compute
name.

In the following example, replace the placeholder values for your compute
and fleet. The `fleet-id` value is returned when you create an
Anywhere fleet. You can retrieve full fleet details by calling [`describe-fleet-attributes`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-attributes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-attributes.html"). To find compute
information, call [`list-compute`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-compute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-compute.html") with the fleet ID to see all computes
that are registered to the fleet.

```
aws gamelift get-compute-auth-token \
    --fleet-id `arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa` \
    --compute-name `HardwareAnywhere`
```

Example output

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "FleetArn": "arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "ComputeName": "HardwareAnywhere",
    "ComputeArn": "arn:aws:gamelift:us-east-1:111122223333:compute/HardwareAnywhere",
    "AuthToken": "0c728041-3e84-4aaa-b927-a0fb202684c0",
    "ExpirationTimestamp": "2023-02-23T18:47:54+00:00"
}
```

## Start a game server

After you've created an Anywhere fleet and added one or more computes to the fleet,
you're ready to start running your game servers.

**Step 1 Install your game server software**
Get your game server build and all dependent software installed onto each compute in your
Anywhere fleet. The game server build must be integrated with Amazon GameLift Servers server
SDK version 5.x (or higher) with the minimum required functionality to
communicate with the Amazon GameLift Servers service.

**Step 2 Get your computes ready to run a game server**

Ensure that each compute is registered and has a valid authentication
token. If you're using scripts to manage these tasks, make sure that the
scripts run on each compute before starting any game server processes.

If you've deployed the Amazon GameLift Servers Agent with your game server software, make
sure that the Agent executable launches.

**Step 3 Launch a game server process**
Run an instance of your game server executable on a compute. If your game server build is
properly integrated, the game server process calls the server SDK action
`InitSDK()` with a set of valid server parameters. When the
server process is ready to host a game session, it calls
`ProcessReady()`.

###### Note

If you deployed your game server software with the Amazon GameLift Servers Agent, you
can skip this step. The Agent automatically launches game server
processes based on the runtime instructions you provide.

You can monitor progress by viewing server process metrics for activating
and active server processes. See [Amazon GameLift Servers metrics for fleets](monitoring-cloudwatch.md#gamelift-metrics-fleet "monitoring-cloudwatch.md#gamelift-metrics-fleet"). If your game server process
fails to initialize, verify that the process is retrieving the right server
parameter values for the compute it's running on.
