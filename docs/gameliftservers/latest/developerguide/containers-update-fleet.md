# Update an Amazon GameLift Servers managed container fleet

You can update most of the properties of a managed container fleet, including the container
group definitions. Depending on the settings being updated, a fleet update might initiate a new
fleet deployment. In a fleet deployment, all instances in the fleet are removed and replaced
with instances with the new configuration. Settings that require a deployment include:

- Container group definitions, including updates to container images
- Connection port ranges and inbound permissions
- Log configuration
  You can track the status of fleet deployments in the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/") or the AWS Command Line Interface (AWS CLI) to create a
  container fleet.

###### Note

You can't update a fleet's runtime environment. At fleet creation, the fleet's Amazon
Machine Image (AMI) is set to the latest available version of the Linux AMI. All container
images that are deployed to this fleet must be compatible with this version. To change the
fleet's AMI or upgrade to a newer version, you must create a new fleet. As a best practice, we
recommend replacing your fleets every 30 days to maintain a secure and up-to-date
runtime environment for your hosted game servers. For more guidance, see [Security best practices for Amazon GameLift Servers](security-best-practices.md "security-best-practices.md").

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"),
select the AWS Region where you want to create the fleet. The container group
definitions must be in the same region where you want to create the fleet.

Open the console’s left navigation bar and choose **Managed containers:
Fleets**. On the managed container fleets page, select a fleet from the list
and choose **Edit**.

1. Update container fleet settings as needed. When you're finished, choose
   **Create**.
2. If your updates require a fleet deployment, you're asked to specify deployment
   options as follows:
   - Game session protection. You can choose to protect fleet instances that have
     active game sessions (safe deployment). With this setting, the fleet instances
     aren't replaced until after the game sessions end. Alternatively, you can choose
     to replace fleet instances regardless of game session activity (unsafe
     deployment). Unsafe deployments are useful during development and testing phases
     in order to reduce deployment time.
   - Minimum healthy percentage. You can manage how quickly the fleet's instances
     are replaced. Use this setting to maintain a minimal amount of healthy tasks the
     during deployment. A low value prioritizes deployment speed, while a high value
     ensures that game server availability remains high throughout the deployment.
   - Deployment failure strategy. Decide what actions to take if a deployment
     fails. A deployment failure means that some of the updated containers have
     failed status checks and are considered impaired. You can set deployments to
     automatically roll back all fleet instances to the previously deployed state.
     Alternatively you can choose to maintain some of the impaired fleet instances
     for use in debugging.

If your request is successful, the console displays the
**Deployments** tab for the managed container fleet. Use this tab to
track the status of each deployment. If you start a new deployment for the fleet, this
action automatically cancels any deployment that is currently in process for the fleet.

AWS CLI
To create a container fleet with the AWS CLI, open a command line window and use the
`update-container-fleet` command. For more information about this command,
see [`update-container-fleet`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-container-fleet.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-container-fleet.html") in the _AWS CLI Command
Reference_.

The following example updates an existing container fleet with the following
characteristics:

- It updates the game server container group definition to use version 2.
- It specifies safe deployment options.

```
{
  "DeploymentConfiguration": {
    "ImpairmentStrategy": "ROLLBACK",
    "MinimumHealthyPercentage": 75,
    "ProtectionStrategy": "WITH_PROTECTION"
  },
  "FleetId": "containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
  "GameServerContainerGroupDefinitionName": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:2"
}
```
