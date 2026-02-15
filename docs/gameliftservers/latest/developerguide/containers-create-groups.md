# Create a container group definition for an Amazon GameLift Servers

container fleet

A container group definition describes how to deploy your containerized game server
applications to a container fleet. It's a blueprint that tells Amazon GameLift Servers what container images to
deploy to the fleet and how to run them. When you create a container fleet, you specify the
container group definitions to deploy to the fleet. For more information about container groups,
see [Container fleet components](containers-howitworks.md#containers-howitworks-components "containers-howitworks.md#containers-howitworks-components").

## Before you start

Tips on what to do before you start creating a container group definition:

- Finalize your container images and push them to an Amazon Elastic Container Registry (Amazon ECR) repository in the
  same AWS Region where you plan to create the container group. Amazon GameLift Servers captures a snapshot
  of each image at the time you create container group definition, and uses the snapshot
  when deploying to a container fleet. See [Build a container image for Amazon GameLift Servers](containers-prepare-images.md "containers-prepare-images.md").
- Create your container definitions as JSON files. A container group definition includes
  one or more container definitions. You can use the JSON files if you create a container
  group definition using the AWS CLIfor Amazon GameLift Servers.
- Verify that your AWS user has IAM permissions to access the Amazon ECR repository. See
  [IAM permission examples for Amazon GameLift Servers](gamelift-iam-policy-examples.md "gamelift-iam-policy-examples.md").

## Create a game server container group definition

A game server container group runs your game server software. A game server container
group has one game server container, which runs the game server executable. It can also have
one or more support containers to run additional software to support your game server. (These
are sometimes referred to as “sidecar” containers.)

This topic describes how to create a simple game server container group definition using
the Amazon GameLift Servers console or AWS CLI tools. For more detailed information on optional features, see
[Customize an Amazon GameLift Servers container fleet](containers-design-fleet.md "containers-design-fleet.md").

###### Note

You can change most container group definition and container definition settings after
creating them. If you make changes to a container definition, Amazon GameLift Servers captures a new snapshot
of the updated container images.

**To create a simple game server container group
definition:**

The following instructions describe how to create a container group definition with the
minimal required parameters and using the Amazon GameLift Servers default values.

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), select
the AWS Region where you want to create the container group.

Open the console’s left navigation bar and choose **Managed containers: Group
definitions**. On the Container groups definition page, choose
**Create group definition**.

###### Step 1: Define container group definition details

1. Enter a container group definition name. The name must be unique to the
   AWS account and Region.
2. Select the **Game server** container group type.
3. For **Total memory limit**, enter the maximum memory resources to
   make available for all containers in the container group. For help calculating this
   value, see [Set resource limits](containers-design-fleet.md#containers-design-fleet-limits "containers-design-fleet.md#containers-design-fleet-limits").
4. For **Total vCPU limit**, enter the maximum computing power to make
   available for all containers in the container group. For help calculating this
   value, see [Set resource limits](containers-design-fleet.md#containers-design-fleet-limits "containers-design-fleet.md#containers-design-fleet-limits").

###### Step 2: Add container definitions

At minimum, a game server container group has one game server container. In the
console, the first container definition you create is the game server container. This
step describes how to define the minimum required settings for a game server container
definition.

1. Enter a container definition **Name**. Each container defined for
   the group must have a unique name value.
2. Link to a container image with your game server build. Enter the **Amazon ECR
   image URI** for a container image in a public or private repository. You
   can use any of the following formats:
   - Image URI only: `[AWS account].dkr.ecr.[AWS Region].amazonaws.com/[repository
ID]`
   - Image URI + digest: `[AWS account].dkr.ecr.[AWS Region].amazonaws.com/[repository
ID]@[digest]`
   - Image URI + tag: `[AWS account].dkr.ecr.[AWS Region].amazonaws.com/[repository
ID]:[tag]`

3. Specify the Amazon GameLift Servers **Server SDK version** that the game server
   build uses. For a container fleet, this value must be 5.2.0 or greater.
4. In **Internal container port range**, set the protocol and
   define a port range. The range size must be greater than the number of concurrent
   game server processes that will run in this container. If the game server container
   runs only one server process per container, this port range only needs a few ports.
   For more details, see [Configure network connections](containers-design-fleet.md#containers-custom-network "containers-design-fleet.md#containers-custom-network").
5. Add more containers as needed to run additional support software. Additional
   containers are automatically designated support containers. A game server container
   group can have only one game server containers and up to eight support containers.
   Provide the following minimal required settings:
   - Container definition **Name**
   - **ECR image URI**.
   - **Internal container ports** (Include this only if the container
     has processes that need network access.)

###### Step 3: Configure dependencies

- If your container group definition has more than one container, you can optionally set dependencies
  between the containers. For more information, see
  [Set container dependencies](containers-design-fleet.md#containers-design-fleet-dependencies "containers-design-fleet.md#containers-design-fleet-dependencies").

###### Step 3: Review and create

1. Review all your container group definition settings. Use **Edit** to make
   changes to any section, including each of your container definitions for the
   group.
2. When you're finished reviewing, choose **Create**.

If your request is successful, the console displays the detail page for the new
container group definition resource. Initially the status is `COPYING`,
as Amazon GameLift Servers starts taking snapshots of all the container images for the group. When
this phase is complete, the container group definition status changes to
`READY`. A container group definition must be in `READY`
status before you can create a container fleet with it.

AWS CLI
When you use the AWS CLI to create a container group definition, maintain your
container definition configurations in a separate `JSON` file. You can
reference the file in your CLI command. See [Create a container definition JSON
file](#containers-definitions-create "#containers-definitions-create") for schema examples.

**Create a container group definition**

To create a new container group definition, use the `create-container-group-definition`
CLI command. For more information about this command, see
[create-container-group-definition](../../../cli/latest/reference/gamelift/create-container-group-definition.md "../../../cli/latest/reference/gamelift/create-container-group-definition.md") in the _AWS CLI
Command Reference_.

This example illustrates a request for a game server container group
definition. It assumes that you’ve created a JSON file with the container
definitions for this group.

```
aws gamelift create-container-group-definition \
    --name MyAdventureGameContainerGroup \
    --operating-system AMAZON_LINUX_2023 \
    --container-group-type GAME_SERVER \
    --total-memory-limit-mebibytes 4096 \
    --total-vcpu-limit 1 \
    --game-server-container-definition file://MyAdventureGameContainers.json
```

## Create a container definition `JSON`

file

When you create a container group definition, you also define the containers for the
group. A container definition specifies the Amazon ECR repository where the container image is
stored, and optional configurations for network ports, limits for CPU and memory usage, and
other settings. We recommend creating a single `JSON` file with the configurations
for all the containers in a container group. Maintaining a file is useful for storing,
sharing, version tracking these critical configurations. If you use the AWS CLI to create
your container group definitions, you can reference the file in the command.

###### To create a container definition

1. Create and open a new `.JSON` file. For example:

```
``[~/work/glc]$` vim SimpleServer.json`
```

2. Create a separate container definition for each of the containers for the group. Copy the
   following example content and modify it as needed for your containers. For details
   on the syntax of a container definition, see [ContainerDefinitionInput](../apireference/API_ContainerDefinitionInput.md "../apireference/API_ContainerDefinitionInput.md") in the _Amazon GameLift Servers API
   Reference_.
3. Save the file locally so that you can refer to it in an AWS CLI command.

###### Example

This example describes the essential container for your game server container group.
The essential replica container includes your game server application, the Amazon GameLift Servers Agent,
and can include other supporting software for your game hosting. The definition must
include a name, image URI, and a port configuration. This example also sets some
container-specific resource limits.

```
  {
    "ContainerName": "MyAdventureGameServer",
    "ImageUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/gl-containers:myadventuregame-server",
    "PortConfiguration": {
      "ContainerPortRanges": [
        {
          "FromPort": 2000,
          "Protocol": "TCP",
          "ToPort": 2010
        }
      ]
    },
    "ServerSdkVersion": "5.2.0"
  }
```
