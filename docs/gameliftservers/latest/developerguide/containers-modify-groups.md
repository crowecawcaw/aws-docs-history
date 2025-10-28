# Update a container group definition for an Amazon GameLift Servers

container fleet

You can update most of the properties of a container group definition, including the
individual container definitions. Container group definitions have a version number. When you
update a container group definition, Amazon GameLift Servers saves the update and increments the definition's
version number. When configuring a container fleet, you can specify which version of a
container group definition to deploy.

After updating a container group definition, you can deploy the new version to a new or
existing container fleet.

## Update a game server container group definition

This topic describes how to update game server container group definition using the Amazon GameLift Servers
console or AWS CLI tools. For more detailed information on optional features, see [Customize an Amazon GameLift Servers container fleet](containers-design-fleet.md "containers-design-fleet.md").

**To update a container group definition:**

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), select
the AWS Region where you want to create the container group.

Open the console’s left navigation bar and choose **Managed containers:
Group definitions**. On the Container groups definition page, choose a
container group definition and version to update.

After you've saved your updates, you can use the new version to create a new
container fleets or you can deploy the updates to an existing container fleet.

###### Step 1: Define container group definition details

- You can update the total memory and vCPU limit settings.

###### Step 2: Add container definitions

You can make the following container definition updates:

- Update existing container definitions.
- Add new support container definitions.
- Remove support container definitions.

1. You can update the **ECR image URI**. Make sure to update the
   **Server SDK version** setting to match the new image.
2. You can update the **Internal container port range** as needed.
   Changes you make to these settings might impact a container fleet's connection port
   settings when these changes are deployed to a fleet. For more details, see [Configure network connections](containers-design-fleet.md#containers-custom-network "containers-design-fleet.md#containers-custom-network").

###### Step 3: Configure dependencies

- You can change dependencies as needed. For more information, see [Set container dependencies](containers-design-fleet.md#containers-design-fleet-dependencies "containers-design-fleet.md#containers-design-fleet-dependencies").

###### Step 3: Review and create

- Review your container group definition updates. Use **Edit** to make
  additional changes in any section. When you're finished, choose
  **Create** to generate a new version of the container group
  definition.

If your request is successful, the console displays the detail page for the new
container group definition resource. Initially the status is `COPYING`, as
Amazon GameLift Servers starts taking snapshots of all the container images for the group. When this
phase is complete, the container group definition status changes to
`READY`. A container group definition must be in `READY` status
before you can create a container fleet with it.

AWS CLI
When you use the AWS CLI to create or update a container group definition,
maintain your container definition configurations in a separate `JSON` file.
You can reference the file in your CLI command. See [Create a container definition JSON
file](containers-create-groups.md#containers-definitions-create "containers-create-groups.md#containers-definitions-create") for schema examples.

When updating a definition, you only need to specify the values you want to update.
Amazon GameLift Servers retains any values that you don't include in your update request. If you're
changing a container definition. However, when changing a container definition, provide
a complete set.

**To update a container group definition**

To update a new container group definition, use the
`update-container-group-definition` CLI command. For more information
about this command, see [update-container-group-definition](../../../cli/latest/reference/gamelift/update-container-group-definition.md "../../../cli/latest/reference/gamelift/update-container-group-definition.md") in the _AWS
CLI Command Reference_.

###### Example : game server container group

You can specify a container group definition version when retrieving,
updating, or deleting a container group definition, or when creating or updating
a container fleet. Each container group definition has a version property. In
addition, the and definition's ARN value specifies the version number.

This example illustrates a request for a change to a game server container
group definition. It assumes that you’ve created a JSON file with the container
definitions for this group. This example uses the ARN value for definition name,
and specifies that the update is to version 1.

```
aws gamelift update-container-group-definition \
    --name arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:1 \
    --operating-system AMAZON_LINUX_2023 \
    --container-group-type GAME_SERVER \
    --total-memory-limit-mebibytes 4096 \
    --total-vcpu-limit 1 \
    --container-definitions file://SimpleServer.json
```

## Clone a container group definition

You can use the Amazon GameLift Servers console to clone an existing container group definition.

###### To clone a container group

1. In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"),
   go to the left navigation pane and choose **Container groups**.
2. On the **Container groups** list page, select the existing container group
   that you want to clone. After you select a container group, the **Clone**
   button is active.
3. Choose **Clone**. This action opens the container group creation wizard with
   pre-filled settings.
4. Enter a new name for the cloned container group. Container group in the same region
   must have unique names.
5. Step through the container group and container definition pages, review, and
   **Create** the new container group.
