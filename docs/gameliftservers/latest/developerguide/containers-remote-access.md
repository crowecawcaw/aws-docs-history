

# Connect to containers
<a name="containers-remote-access"></a>

For Amazon GameLift Servers container fleets, you can access game server containers running on a fleet instance. Use container access to troubleshoot game sessions, inspect logs, and debug runtime issues.

## Connect to a container
<a name="containers-remote-access-connect"></a>

**Before you start:**  
Connect to the fleet instance. For instructions, see [Connect to fleet instances](fleets-remote-access.md).

Run the following command to list running containers on the instance:

```
sudo docker ps
```

The output lists all containers running on the instance, including game server containers and internal Amazon GameLift Servers containers. Look for containers with your game server image to identify the game server containers.

**Example output:**

```
CONTAINER ID   IMAGE                  COMMAND                  CREATED      STATUS
b9676e9489f5   game-server-container  "/bin/sh -c ./$GAME_…"   2 days ago   Up 2 days
1d1c8443efe2   support-container      "/bin/sh -c ./$SUPPO…"   2 days ago   Up 2 days
```

To connect to a game server container, use the container short ID from the `CONTAINER ID` column. This gives you full read and write access to the container filesystem.

```
sudo docker exec -it {{container-short-id}} sh
```

## Connect to a container through the console
<a name="containers-remote-access-console"></a>

You can connect to game server containers from the Amazon GameLift Servers console using Amazon EC2 Systems Manager (SSM). This method provides secure access without requiring additional setup or credential management. You can connect to a container from either the **Computes** tab or the **Game sessions** tab on the fleet details page.

1. In the Amazon GameLift Servers console, choose **Managed containers** from the navigation pane, and then **Fleets**.

1. Choose the fleet ID that contains the container or game session you want to access.

1. On the fleet details page, choose one of the following tabs:
   + **Computes** – Lists the containers running on the fleet. Select the container you want to connect to.
   + **Game sessions** – Lists the game sessions for the fleet. Select the game session to connect to the container hosting it.

1. Choose **Connect**. Copy the command displayed to connect to the container, then choose **Connect** again.

1. In the connection dialog, choose **Run** to create a new SSM session. The system authenticates your session through AWS Key Management Service (AWS KMS) and opens a terminal in your browser.

1. Once you have connected to the instance, paste the docker command from step 4 and execute it on the instance to access the container.

## Connect to container hosting a game session
<a name="containers-remote-access-game-session"></a>

To connect to the game server container hosting a specific game session, follow these steps.

1. **Get the compute name.** Call [describe-game-sessions](https://docs.aws.amazon.com/cli/latest/reference/gamelift/describe-game-sessions.html) to get the `ComputeName` for the game session.

   **Request**

   ```
   aws gamelift describe-game-sessions \
       --fleet-id fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa \
       --game-session-id arn:aws:gamelift:us-west-2::gamesession/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa/gs-1111aaaa-2222-3333-4444-5555bbbb66cc
   ```

   **Response**

   ```
   {
     "GameSessions": [
       {
         "GameSessionId": "arn:aws:gamelift:us-west-2::gamesession/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa/gs-1111aaaa-2222-3333-4444-5555bbbb66cc",
         "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
         "ComputeName": "62c5ff7f7a9a445d84877074c80aeafc",
         "Status": "ACTIVE",
         . . .
       }
     ]
   }
   ```

   Note the `ComputeName` value from the response (for example, `62c5ff7f7a9a445d84877074c80aeafc`).

1. **Get compute access and container attributes.** Call [get-compute-access](https://docs.aws.amazon.com/cli/latest/reference/gamelift/get-compute-access.html) with the fleet ID and compute name.

   The response includes the following fields:
   + `ContainerIdentifiers` – The `ContainerName` and `ContainerRuntimeId` for each container.
   + `GameServerContainerGroupDefinitionArn` – The ARN of the container group definition.
   + `Credentials` – Temporary credentials to connect to the instance.

   **Request**

   ```
   aws gamelift get-compute-access \
       --fleet-id fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa \
       --compute-name 62c5ff7f7a9a445d84877074c80aeafc
   ```

   **Response**

   ```
   {
     "ComputeName": "62c5ff7f7a9a445d84877074c80aeafc",
     "ContainerIdentifiers": [
       {
         "ContainerName": "game-server",
         "ContainerRuntimeId": "02accb92cd9bef3373300e7151d5c2b3dcca3b06eff1bb4e345085fc008d4678"
       }
     ],
     "Credentials": {
       "AccessKeyId": "ASIAIOSFODNN7EXAMPLE",
       "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
       "SessionToken": "AQoDYXdzEJr...<remainder of session token>"
     },
     "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
     "GameServerContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2::containergroupdefinition/MyGameServerGroup"
   }
   ```

1. **Connect to the instance.** Use the credentials from step 2 to connect to the fleet instance. For detailed instructions, see [Connect to fleet instances](fleets-remote-access.md).

1. **Find the game server container name.** Call [describe-container-group-definition](https://docs.aws.amazon.com/cli/latest/reference/gamelift/describe-container-group-definition.html) using the `GameServerContainerGroupDefinitionArn` from step 2 to identify the game server container name.

   **Request**

   ```
   aws gamelift describe-container-group-definition \
       --name arn:aws:gamelift:us-west-2::containergroupdefinition/MyGameServerGroup
   ```

   **Response**

   ```
   {
     "ContainerGroupDefinition": {
       "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:123456789012:containergroupdefinition/MyGameServerGroup:3",
       "Name": "MyGameServerGroup",
       "ContainerGroupType": "GAME_SERVER",
       "GameServerContainerDefinition": {
         "ContainerName": "game-server",
         . . .
       },
       . . .
     }
   }
   ```

   Note the `GameServerContainerDefinition.ContainerName` value (for example, `game-server`).

1. **Identify the game server container runtime ID.** Using the game server container name from the previous step, find the matching entry in the `ContainerIdentifiers` from the `get-compute-access` response in step 2. Note the `ContainerRuntimeId` value.

1. **Connect to the container.** Use the `ContainerRuntimeId` as the container ID and run the following command:

   ```
   sudo docker exec -it 02accb92cd9bef3373300e7151d5c2b3dcca3b06eff1bb4e345085fc008d4678 sh
   ```

## View container port mappings
<a name="containers-remote-access-port-mappings"></a>

Port mappings show how container ports map to connection ports on your fleet instances. Each container port that accepts inbound traffic is assigned a connection port on the instance. You can check port mappings to discover which connection ports map to your container ports or to troubleshoot connection issues. You can view port mappings in the Amazon GameLift Servers console, or use the AWS CLI or AWS SDK.

### View port mappings in the console
<a name="containers-remote-access-port-mappings-console"></a>

In the Amazon GameLift Servers console, choose **Managed containers** from the navigation pane, and then **Fleets**. Choose a fleet to open the fleet details page. You can view port mappings in the following locations:
+ **Instance details page** – Shows port mappings for the per-instance container group on the selected instance.
+ **Compute details page** – Shows port mappings for the game server container group on the selected compute.

Both pages include a search field to filter port mappings by container name.

### View port mappings with the AWS CLI
<a name="containers-remote-access-port-mappings-cli"></a>

Use the `describe-container-group-port-mappings` command to retrieve port mappings for a container group on a fleet instance. Specify the container group type and either a `--compute-name` (for game server groups) or an `--instance-id` (for per-instance groups). Optionally, include the `--container-name` parameter to filter results to a specific container.

**Example: Game server container group**

The following command retrieves port mappings for the game server container group on a specific compute.

```
aws gamelift describe-container-group-port-mappings \
    --fleet-id fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa \
    --container-group-type GAME_SERVER \
    --compute-name 62c5ff7f7a9a445d84877074c80aeafc
```

If successful, Amazon GameLift Servers returns a response like the following:

```
{
  "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
  "Location": "us-west-2",
  "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:123456789012:containergroupdefinition/MyGameServerGroup",
  "ContainerGroupType": "GAME_SERVER",
  "ComputeName": "62c5ff7f7a9a445d84877074c80aeafc",
  "InstanceId": "i-1234567890abcdef0",
  "ContainerGroupPortMappings": [
    {
      "ContainerName": "MyGameServer",
      "ContainerRuntimeId": "a1b2c3d4e5f6",
      "ContainerPortMappings": [
        {
          "ContainerPort": 7777,
          "ConnectionPort": 1025,
          "Protocol": "UDP"
        },
        {
          "ContainerPort": 8080,
          "ConnectionPort": 1026,
          "Protocol": "TCP"
        }
      ]
    }
  ]
}
```

**Example: Per-instance container group**

The following command retrieves port mappings for the per-instance container group on a specific instance.

```
aws gamelift describe-container-group-port-mappings \
    --fleet-id fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa \
    --container-group-type PER_INSTANCE \
    --instance-id i-1234567890abcdef0
```

If successful, Amazon GameLift Servers returns a response like the following:

```
{
  "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
  "Location": "us-west-2",
  "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:123456789012:containergroupdefinition/MyPerInstanceGroup",
  "ContainerGroupType": "PER_INSTANCE",
  "InstanceId": "i-1234567890abcdef0",
  "ContainerGroupPortMappings": [
    {
      "ContainerName": "MySupportContainer",
      "ContainerRuntimeId": "f6e5d4c3b2a1",
      "ContainerPortMappings": [
        {
          "ContainerPort": 8443,
          "ConnectionPort": 2025,
          "Protocol": "TCP"
        }
      ]
    }
  ]
}
```