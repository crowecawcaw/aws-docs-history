# Delete a container group definition for an Amazon GameLift Servers

container fleet

You have several options for deleting a container group definition. When you delete a
container group definition, this action also deletes all the container definitions in the
container group.

Container group definitions can have multiple versions. Container group versions have the
same name, but have a different version number. Container group definition ARNs specify both the
name and version.

You can specify a container group definition version when retrieving, updating, or deleting
a container group definition, or when creating or updating a container fleet. Each container
group definition has a version property. In addition, the definition's ARN value specifies the
version number.

There are several ways to delete container group definitions:

- You can delete all versions of a specific definition.
- You can delete one particular version of a specific definition.
- You can keep some number of newest versions and delete the older versions of a specific
  definition. For example, you might delete all versions older than version 5.
  You can delete a container group definition version only if it's not being used in a
  container fleet.

**To delete a container group definition**

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), select
the AWS Region where you want to create the container group.

Open the console’s left navigation bar and choose **Managed containers: Group
definitions**. On the Container group definitions page, select the definition
you want to modify and choose **Delete**.

You're prompted to select the type of deletion you want to make and specify
additional settings depending on the delete type.

AWS CLI

- To delete a container group definition, use the
  `delete-container-group-definition` CLI command and provide values for
  the type of delete you want to do. For more information about this command, see [delete-container-group-definition](../../../cli/latest/reference/gamelift/delete-container-group-definition.md "../../../cli/latest/reference/gamelift/delete-container-group-definition.md") in the _AWS CLI
  Command Reference_.

This example illustrates a request to delete all versions of game server container
group definition older than version 5.

###### Example

```
aws gamelift delete-container-group-definition \
    --name MyAdventureGameContainerGroup \
    --version-count-to-retain 5 \
```
