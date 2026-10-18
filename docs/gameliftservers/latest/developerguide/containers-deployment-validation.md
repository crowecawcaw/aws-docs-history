

# Validate and troubleshoot container fleet deployments
<a name="containers-deployment-validation"></a>

A *fleet deployment*, called a *deployment* in this topic, is the process that Amazon GameLift Servers uses to replace the containers on a container fleet's instances with containers that use the fleet's new settings, such as a new container group definition version. Instead of replacing every running container at once, a deployment first verifies that the new containers can host game sessions and then replaces the rest gradually to catch bad changes before they deploy to the entire fleet. A container fleet starts a deployment in three situations:
+ **When you create a fleet with a container group definition.** If your [CreateContainerFleet](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerFleet.html) request includes a game server container group definition, fleet creation starts a deployment that installs your containers on the fleet's new instances. If you create a fleet without a container group definition, no instances are deployed and the fleet has no deployment until you add a game server container group definition.
+ **When you update the fleet's container group definitions or other container settings.** [UpdateContainerFleet](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerFleet.html) starts a deployment when the update changes the containers that the fleet runs, for example when you specify a new game server container group definition version. An update that doesn't change any of these settings doesn't start a deployment. For information about which settings start a deployment, see [Update an Amazon GameLift Servers managed container fleet](containers-update-fleet.md).
+ **When you add locations to an active fleet.** Amazon GameLift Servers starts a deployment in the new locations using the fleet's configured container group definitions. Existing locations aren't redeployed. You can't add locations while another deployment is in progress.

To see the details of a deployment, call [DescribeFleetDeployment](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetDeployment.html), which returns a [FleetDeployment](https://docs.aws.amazon.com/gamelift/latest/apireference/API_FleetDeployment.html) object. It includes the deployment ID, status, and configuration, along with the container group definition versions being deployed and the rollback versions. The fleet's `DeploymentDetails.LatestDeploymentId` property identifies its most recent deployment.

**Note**  
Deployments apply to managed container fleets only.

## Configure a deployment
<a name="containers-deployment-validation-config"></a>

A deployment's [DeploymentConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeploymentConfiguration.html) is the set of rules that control how the deployment proceeds across the fleet and what happens if it fails. For information about each setting's values and defaults, see [DeploymentConfiguration](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeploymentConfiguration.html) in the *Amazon GameLift Servers API Reference*.

You set the deployment configuration when you call `UpdateContainerFleet` or edit the fleet in the console. `CreateContainerFleet` doesn't accept a deployment configuration, so a fleet's first deployment always uses the default values.

## How Amazon GameLift Servers validates a deployment
<a name="containers-deployment-validation-howitworks"></a>

When a deployment starts, Amazon GameLift Servers first validates the game server container groups in each of the fleet's locations. It runs the new containers on a small part of the fleet's existing capacity and checks that they become healthy. A new game server container group is *healthy* when a game server container calls `ProcessReady()` to report that it's ready to host game sessions.

This initial validation checks game server container groups. If your fleet also uses a per-instance container group definition, Amazon GameLift Servers updates those groups after updating the game server groups. Amazon GameLift Servers checks per-instance groups separately before the deployment completes; they don't use the game server's `ProcessReady()` check.

Validation fails if a new game server container group doesn't become healthy before Amazon GameLift Servers stops waiting. For information about common reasons and how to investigate them, see [Debug an impaired deployment](#containers-deployment-validation-debug).

If validation fails, Amazon GameLift Servers applies the deployment's `ImpairmentStrategy` and sets the deployment status to `IMPAIRED` (for `MAINTAIN`) or `ROLLBACK_IN_PROGRESS` (for `ROLLBACK`). Only after validation succeeds in a location does Amazon GameLift Servers replace the remaining containers that are running your game servers there.

### How long validation takes
<a name="containers-deployment-validation-timeouts"></a>

Validation takes longer when the capacity that Amazon GameLift Servers uses for validation is hosting protected game sessions. The fleet's `NewGameSessionProtectionPolicy` determines the default protection for new game sessions. Valid values are `NoProtection` and `FullProtection`. The deployment's `ProtectionStrategy` determines whether the deployment honors that protection. Valid values are `WITH_PROTECTION` and `IGNORE_PROTECTION`.

When the fleet has `NewGameSessionProtectionPolicy` set to `FullProtection` and the deployment has `ProtectionStrategy` set to `WITH_PROTECTION`, Amazon GameLift Servers allows a longer validation timeout for protected game sessions to end. With any other combination, it uses a shorter timeout.

**Important**  
If your new containers never become healthy, and the fleet uses `FullProtection` with a `WITH_PROTECTION` deployment, the deployment can stay in `IN_PROGRESS` status until protected game sessions end before it reports a failure. To get a faster signal, deploy new container images with `IGNORE_PROTECTION` while you're testing them, or cancel the deployment yourself. For instructions on canceling a deployment, see [Cancel a deployment by starting a new one](#containers-deployment-validation-cancel).  
If you protect individual game sessions with [UpdateGameSession](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSession.html) on a fleet whose `NewGameSessionProtectionPolicy` is `NoProtection`, Amazon GameLift Servers doesn't extend its wait for them. If those game sessions don't end in time, validation can fail even though the new configuration is working.

## Track deployment status
<a name="containers-deployment-validation-status"></a>

To track a deployment in the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/), open the fleet and choose the **Deployments** tab. To track it with the AWS Command Line Interface (AWS CLI), use [list-fleet-deployments](https://docs.aws.amazon.com/cli/latest/reference/gamelift/list-fleet-deployments.html) to find a deployment ID, and then [describe-fleet-deployment](https://docs.aws.amazon.com/cli/latest/reference/gamelift/describe-fleet-deployment.html) for the detail of a single deployment.

For information about deployment status values and what each one means, see [DeploymentStatus](https://docs.aws.amazon.com/gamelift/latest/apireference/API_FleetDeployment.html#gameliftservers-Type-FleetDeployment-DeploymentStatus) in the *Amazon GameLift Servers API Reference*.

## Debug an impaired deployment
<a name="containers-deployment-validation-debug"></a>

An impaired deployment means that the new containers didn't become healthy during validation: no game server container called `ProcessReady()` before Amazon GameLift Servers stopped waiting, often because a container exited or failed to start. The cause is usually in the container image or the game server. Find out why the container exited or why the game server never reported ready.

### Review the fleet event log
<a name="containers-deployment-validation-debug-events"></a>

The fleet event log records what Amazon GameLift Servers observed during the deployment. View it on the fleet's **Events** tab in the console, or call [describe-fleet-events](https://docs.aws.amazon.com/cli/latest/reference/gamelift/describe-fleet-events.html). The following event codes are relevant to a failed deployment:
+ `GAME_SERVER_CONTAINER_GROUP_CRASHED` and `PER_INSTANCE_CONTAINER_GROUP_CRASHED` – a container group exited or failed to start. When Amazon GameLift Servers has the container's exit code, it includes the code in the event message.
+ `GAME_SERVER_CONTAINER_GROUP_REPLACED_UNHEALTHY` and `INSTANCE_REPLACED_UNHEALTHY` – Amazon GameLift Servers replaced a container group or an instance that didn't become healthy. These can repeat across the fleet's locations while a deployment is failing.
+ `SERVER_PROCESS_MISCONFIGURED_CONTAINER_PORT` – a game server container used a port that doesn't match the ports declared in the container group definition.
+ `LOCATION_STATE_UPDATING` and `LOCATION_STATE_ACTIVE` – these bracket the deployment in each location, which helps you line up other events with the deployment that produced them.
+ `COMPUTE_LOG_UPLOAD_FAILED` – log collection for a container stopped working, so logs from that container might be incomplete or missing.

### Read the container logs
<a name="containers-deployment-validation-debug-logs"></a>

A container fleet's `LogConfiguration` sets where Amazon GameLift Servers sends each container's standard output: `CLOUDWATCH` (the default), `S3`, or `NONE`. Keep it set to `CLOUDWATCH` or `S3` so that container output is available when a deployment fails. When a container fails before your game server starts running, for example because the container's entry point refers to a file that isn't in the image, this output is the only record of the failure. For information about container logging, see [Logging differences: Managed EC2 vs Container fleets](logging-server-messages-ec2-vs-containers.md).

### Connect to an impaired container
<a name="containers-deployment-validation-debug-connect"></a>

If you deployed with the `MAINTAIN` impairment strategy, you can connect to a container that Amazon GameLift Servers kept and inspect it directly. Use this to check file permissions, confirm which files the image actually contains, and run the game server executable by hand to see what it reports. For instructions on connecting to a container, see [Connect to containers](containers-remote-access.md).

### Common deployment problems
<a name="containers-deployment-validation-debug-causes"></a>

The following symptoms are common in failed or slow deployments, along with their usual causes.

**The container starts and exits immediately, over and over.**  
If the container's entry point can't run, check the following:  
+ Verify that the launch script and game server executable are marked executable in the image.
+ Confirm that the executable's CPU architecture matches the fleet's instance type.
+ Check that the image contains the interpreter and shared libraries that the executable needs.
For information about building an image that Amazon GameLift Servers can run, see [Build a container image for Amazon GameLift Servers](containers-prepare-images.md).

**The deployment is slow but nothing is failing.**  
A `WITH_PROTECTION` deployment waits for protected game sessions to end, both during validation and when it replaces the fleet's containers. Check the fleet's active game sessions before you treat a long deployment as a failure. For information about validation wait times, see [How long validation takes](#containers-deployment-validation-timeouts).

## Cancel a deployment by starting a new one
<a name="containers-deployment-validation-cancel"></a>

To cancel a deployment and return the fleet to its previous configuration, call `UpdateContainerFleet` or edit the fleet in the console to start a new deployment that reverses the changes. The most common case is a new container group definition version, which the following procedure reverts. Amazon GameLift Servers records the versions that the fleet used when it was last active on the in-progress deployment as `RollbackGameServerBinaryArn` and `RollbackPerInstanceBinaryArn`, so you don't have to work out which version to go back to. If the deployment also changed other settings, such as the log configuration or the connection port range, set those back in the same `UpdateContainerFleet` request.

Before you begin, configure the AWS CLI for your account and identify the fleet's home AWS Region. This procedure requires an in-progress deployment and a previous container group definition version to restore. Use `list-fleet-deployments` to find the deployment ID. For instructions, see [Track deployment status](#containers-deployment-validation-status).

In the commands, replace {{fleet-id}} with your fleet ID, {{deployment-id}} with the in-progress deployment ID, and {{fleet-home-region}} with the fleet's home AWS Region.

**To replace an in-progress deployment with a previous container version (AWS CLI)**

1. Use the following AWS CLI command to get the version to return to:

   ```
   aws gamelift describe-fleet-deployment \
       --fleet-id {{fleet-id}} \
       --deployment-id {{deployment-id}} \
       --region {{fleet-home-region}}
   ```

   In the response, `RollbackGameServerBinaryArn` holds the game server container group definition version that the fleet used when it was last active. If the fleet has a per-instance container group, `RollbackPerInstanceBinaryArn` holds that version.

1. Use the following AWS CLI command to start a new deployment with that version. Replace {{rollback-game-server-cgd-arn}} with the `RollbackGameServerBinaryArn` value from step 1. If the fleet has a per-instance container group, also pass `--per-instance-container-group-definition-name` with the `RollbackPerInstanceBinaryArn` value.

   ```
   aws gamelift update-container-fleet \
       --fleet-id {{fleet-id}} \
       --game-server-container-group-definition-name {{rollback-game-server-cgd-arn}} \
       --region {{fleet-home-region}}
   ```

1. Confirm that the earlier deployment reports `CANCELLED` status and that the new deployment reports `COMPLETE` when it finishes.

**Note**  
Cancelling a deployment this way isn't an instant stop. The new deployment runs through the same steps as any other, including validation, so the fleet takes some time to settle. A version that the fleet ran successfully before usually validates quickly.

## Related topics
<a name="containers-deployment-validation-related"></a>

For more information, see the following topics.
+ [Update an Amazon GameLift Servers managed container fleet](containers-update-fleet.md)
+ [Connect to containers](containers-remote-access.md)
+ [Build a container image for Amazon GameLift Servers](containers-prepare-images.md)
+ [Logging differences: Managed EC2 vs Container fleets](logging-server-messages-ec2-vs-containers.md)
+ [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md)
+ [How containers work in Amazon GameLift Servers](containers-howitworks.md)