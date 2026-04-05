# Connect to containers

For Amazon GameLift Servers container fleets, you can access game server containers running on a fleet
instance. Use container access to troubleshoot game sessions, inspect logs, and debug runtime
issues.

## Connect to a container

###### Before you start:

Connect to the fleet instance. For instructions, see
[Connect to fleet instances](fleets-remote-access.md "fleets-remote-access.md").

Run the following command to list running containers on the instance:

```
sudo docker ps
```

The output lists all containers running on the instance, including game server
containers and internal Amazon GameLift Servers containers. Look for containers with your game server image
to identify the game server containers.

**Example output:**

```
CONTAINER ID   IMAGE                  COMMAND                  CREATED      STATUS
b9676e9489f5   game-server-container  "/bin/sh -c ./$GAME_…"   2 days ago   Up 2 days
1d1c8443efe2   support-container      "/bin/sh -c ./$SUPPO…"   2 days ago   Up 2 days
```

To connect to a game server container, use the container short ID from the
`CONTAINER ID` column. This gives you full read and write access to the
container filesystem.

```
sudo docker exec -it `container-short-id` sh
```

## Connect to a container through the console

You can connect to game server containers from the Amazon GameLift Servers console using Amazon EC2 Systems Manager (SSM).
This method provides secure access without requiring additional setup or credential
management. You can connect to a container from either the
**Computes** tab or the
**Game sessions** tab on the fleet details page.

1. In the Amazon GameLift Servers console, choose **Managed containers**
   from the navigation pane, and then **Fleets**.
2. Choose the fleet ID that contains the container or game session you want to access.
3. On the fleet details page, choose one of the following tabs:
   - **Computes** – Lists the containers
     running on the fleet. Select the container you want to connect to.
   - **Game sessions** – Lists the game
     sessions for the fleet. Select the game session to connect to the container hosting
     it.

4. Choose **Connect**. Copy the command displayed to
   connect to the container, then choose **Connect**
   again.
5. In the connection dialog, choose **Run** to create a
   new SSM session. The system authenticates your session through AWS Key Management
   Service (AWS KMS) and opens a terminal in your browser.
6. Once you have connected to the instance, paste the docker command from step 4 and
   execute it on the instance to access the container.

## Connect to container hosting a game session

To connect to the game server container hosting a specific game session, follow these steps.

1. **Get the compute name.** Call
   [describe-game-sessions](../../../cli/latest/reference/gamelift/describe-game-sessions.md "../../../cli/latest/reference/gamelift/describe-game-sessions.md")
   to get the `ComputeName` for the game session.

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

Note the `ComputeName` value from the response (for example,
`62c5ff7f7a9a445d84877074c80aeafc`). 2. **Get compute access and container attributes.** Call
[get-compute-access](../../../cli/latest/reference/gamelift/get-compute-access.md "../../../cli/latest/reference/gamelift/get-compute-access.md")
with the fleet ID and compute name.

The response includes the following fields:

    * `ContainerIdentifiers` – The `ContainerName` and `ContainerRuntimeId` for each container.
    * `GameServerContainerGroupDefinitionArn` – The ARN of the container group definition.
    * `Credentials` – Temporary credentials to connect to the instance.

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

3. **Connect to the instance.** Use the credentials from
   step 2 to connect to the fleet instance. For detailed instructions, see
   [Connect to fleet instances](fleets-remote-access.md "fleets-remote-access.md").
4. **Find the game server container name.** Call
   [describe-container-group-definition](../../../cli/latest/reference/gamelift/describe-container-group-definition.md "../../../cli/latest/reference/gamelift/describe-container-group-definition.md")
   using the `GameServerContainerGroupDefinitionArn` from step 2 to identify the
   game server container name.

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

Note the `GameServerContainerDefinition.ContainerName`
value (for example, `game-server`). 5. **Identify the game server container runtime ID.**
Using the game server container name from the previous step, find the matching entry
in the `ContainerIdentifiers` from the `get-compute-access`
response in step 2. Note the `ContainerRuntimeId` value. 6. **Connect to the container.** Use the
`ContainerRuntimeId` as the container ID and run
the following command:

```
sudo docker exec -it 02accb92cd9bef3373300e7151d5c2b3dcca3b06eff1bb4e345085fc008d4678 sh
```
