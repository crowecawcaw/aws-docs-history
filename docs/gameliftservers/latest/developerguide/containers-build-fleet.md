# Create an Amazon GameLift Servers managed container fleet

Create an Amazon GameLift Servers managed container fleet to deploy and host your containerized game
server in the AWS Cloud. When you create a container fleet, specify container group
definitions that specify one or more container images (at least one that includes your game
server build) and configuration settings.

When you create a new managed container fleet resource, you immediately initiate the first
phase of fleet creation. Managed fleet creation passes through several phases as Amazon GameLift Servers
provisions an EC2 instance, installs a runtime environment, deploys your container groups onto
the instance, and begins launching game server processes. Depending on the runtime environment
your game server build requires, Amazon GameLift Servers deploys the latest version of the Amazon Machine Image
(AMI) at the time of fleet creation (and all future instances in the fleet will use the same
version). You can monitor a fleet's status in the console or using the AWS Command Line Interface (AWS CLI). When a
fleet is ready to host game sessions, the status changes to `ACTIVE`. For help with
fleet creation issues, see [Debug Amazon GameLift Servers fleet issues](fleets-creating-debug.md "fleets-creating-debug.md").

You can opt to create an empty container fleet and and then add or update the fleet's
container group definitions later. If you create a fleet without a container group definition,
the fleet will not reach active status.

###### Note

As a best practice, we recommend replacing your fleets every 30 days to
maintain a secure and up-to-date runtime environment for your hosted game servers. This
requires creating a new fleet and migrating player traffic to it. For more guidance, see
[Security best practices for Amazon GameLift Servers](security-best-practices.md "security-best-practices.md").

Use the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/") or the AWS Command Line Interface
(AWS CLI) to create a container fleet.

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"),
select the AWS Region where you want to create the fleet. The container group
definitions must be in the same region where you want to create the fleet.

Open the console’s left navigation bar and choose **Managed containers:
Fleets**. On the Fleets page, choose **Create container
fleet**.

###### Step 1: Define managed container fleet details

1. In the **Container fleet details** section, enter a fleet
   description.
2. Specify an **IAM role** for the fleet. This role has permissions
   that Amazon GameLift Servers must have to manage the container fleet on your behalf. For help creating
   the required service role, see [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md "setting-up-role.md").
3. Choose a **Log configuration** option. The CloudWatch option is
   selected by default. Provide the required information based on your selected
   option.
4. Add container groups to the fleet. This is an optional step. You can choose to
   create a fleet without a container group with a plan to add them later. A fleet
   without any container groups won't deploy any fleet instances and can't host any games
   yet, but the fleet resource is created.
   - Select a game server container group definition. Optionally specify the
     version of the definition that you want to deploy. If you don’t specify the
     version number, Amazon GameLift Servers automatically uses the latest version.
   - Optionally add a per-instance container group definition and version. If you
     don’t specify the version number, Amazon GameLift Servers automatically uses the latest
     version.

5. In the **Additional details**, you can set some optional
   customizations. None of these settings are required to create the container
   fleet.

###### Step 2: Define instance details

1. In **Instance deployment**, select one or more remote locations
   to deploy instances to. The home Region is automatically selected (this is the Region
   that you're creating the fleet in). If you select additional locations, fleet
   instances are also deployed in these locations.

###### Important

To use Regions that aren't enabled by default, enable them in your AWS account.

    * Fleets with Regions that aren't enabled that you created before February 28, 2022 are
     not affected by this requirement.
    * To create new multi-location fleets or to update existing multi-location fleets, first enable any
     Regions or Local Zones that you choose to use.For more

information about Regions that aren't enabled by default and how to enable them, see
[Managing AWS Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in the
_AWS General Reference_. See
[Getting started with Local Zones](../../../local-zones/latest/ug/getting-started.md "../../../local-zones/latest/ug/getting-started.md") in the
_AWS Local Zones User Guide_. 2. Select an **Instance configuration** for the fleet. The console
automatically calculates the minimum vCPU and memory required (based on the total
limits you set for each container group). It filters the complete list of available
instance types base on resource requirements and the locations you entered. You can
add additional filters as needed.

For more information about choosing an instance type, see [Configure a container fleet](containers-design-fleet.md#containers-design-fleet-config "containers-design-fleet.md#containers-design-fleet-config"). The size of the instance type you
choose will impact how game server container groups are packed onto each fleet
instance. Depending on your choice, consider reviewing your setting for desired
game server container groups per instance.

###### Step 4: Review and create

- Review your fleet configuration settings.

You can update the fleet's metadata and configuration at any time, regardless of
fleet status. For more information, see [Update an Amazon GameLift Servers fleet configuration](fleets-editing.md "fleets-editing.md"). You can update fleet capacity after the fleet has
reached ACTIVE status. For more information, see [Scaling game hosting capacity with Amazon GameLift Servers](fleets-manage-capacity.md "fleets-manage-capacity.md"). You can
also add or remove remote locations.

When you're finished reviewing, choose **Create**.

If your request is successful, the console displays the detail page for the new
fleet resource. Initially the status is `NEW`, as Amazon GameLift Servers starts the fleet
creation process. You can track the new fleet's status on the
**Fleets** page. A fleet is ready to host game sessions when it
reaches status `ACTIVE`.

AWS CLI
To create a container fleet with the AWS CLI, open a command line window and use the
`create-container-fleet` command. For more information about this command,
see [`create-container-fleet`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-container-fleet.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-container-fleet.html") in the _AWS CLI Command
Reference_.

The example `create-container-fleet` request shown below creates a new
container fleet with the following characteristics:

- The ContainerGroupsConfiguration specifies a game server container group
  definition only: `MyAdventureGameContainerGroup`. The number of game server
  container groups that will be deployed to each fleet instance is calculated by
  Amazon GameLift Servers.
- The fleet uses c5.large On-Demand instances by default.
- By default, the fleet opens a set of connection ports and inbound permissions
  ports as calculated by Amazon GameLift Servers. It deploys container groups to the following locations:

```
aws gamelift create-container-fleet \
    --fleet-role-arn arn:aws:iam::MyAccount:role/MyContainersRole \
    --game-server-container-group-definition-name "rn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:2" \

```

If the create-fleet request is successful, Amazon GameLift Servers returns a set of fleet attributes
that includes the configuration settings you requested and a new container fleet ID. Amazon GameLift Servers
then sets the fleet status and location statuses to **New**
and initiates the fleet activation process. You can track the fleet's status and view
other fleet information using these CLI commands:

- [describe-fleet-events](../../../cli/latest/reference/gamelift/describe-fleet-events.md "../../../cli/latest/reference/gamelift/describe-fleet-events.md")
- [describe-container-fleet](../../../cli/latest/reference/gamelift/describe-container-fleet.md "../../../cli/latest/reference/gamelift/describe-container-fleet.md")
- [describe-fleet-capacity](../../../cli/latest/reference/gamelift/describe-fleet-capacity.md "../../../cli/latest/reference/gamelift/describe-fleet-capacity.md")
- [describe-fleet-port-settings](../../../cli/latest/reference/gamelift/describe-fleet-port-settings.md "../../../cli/latest/reference/gamelift/describe-fleet-port-settings.md")
- [describe-fleet-utilization](../../../cli/latest/reference/gamelift/describe-fleet-utilization.md "../../../cli/latest/reference/gamelift/describe-fleet-utilization.md")
- [describe-fleet-location-capacity](../../../cli/latest/reference/gamelift/describe-fleet-location-capacity.md "../../../cli/latest/reference/gamelift/describe-fleet-location-capacity.md")
- [describe-fleet-location-utilization](../../../cli/latest/reference/gamelift/describe-fleet-location-utilization.md "../../../cli/latest/reference/gamelift/describe-fleet-location-utilization.md")

You can change the fleet's capacity and other configuration settings as needed using
these commands:

- [update-container-fleet](../../../cli/latest/reference/gamelift/update-container-fleet.md "../../../cli/latest/reference/gamelift/update-container-fleet.md")
- [update-fleet-capacity](../../../cli/latest/reference/gamelift/update-fleet-capacity.md "../../../cli/latest/reference/gamelift/update-fleet-capacity.md")
- [update-fleet-port-settings](../../../cli/latest/reference/gamelift/update-fleet-port-settings.md "../../../cli/latest/reference/gamelift/update-fleet-port-settings.md")
- [create-fleet-locations](../../../cli/latest/reference/gamelift/create-fleet-locations.md "../../../cli/latest/reference/gamelift/create-fleet-locations.md")
- [delete-fleet-locations](../../../cli/latest/reference/gamelift/delete-fleet-locations.md "../../../cli/latest/reference/gamelift/delete-fleet-locations.md")
