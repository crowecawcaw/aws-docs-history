# Integrate Amazon GameLift Servers with a Unity game client

project

###### Note

This topic provides information for an earlier version of the Amazon GameLift Servers plugin for Unity. Version 1.x
uses the server SDK for Amazon GameLift Servers 4.x or earlier. For documentation on the
latest plugin version, which uses server SDK 5.x and supports newer features such as Amazon GameLift Servers Anywhere and managed container hosting, see
[Amazon GameLift Servers plugin for Unity (server SDK 5.x)](unity-plug-in.md "unity-plug-in.md").

This topic helps you set up a game client to connect to Amazon GameLift Servers hosted game sessions through
a backend service. Use Amazon GameLift Servers APIs to initiate matchmaking, request game session placement,
and more.

Add code to the backend service project to allow communication with the Amazon GameLift Servers service. A
backend service handles all game client communication with the GameLift service. For more
information about backend services, see .

A backend server handles the following game client tasks:

- Customize authentication for your players.
- Request information about active game sessions from the Amazon GameLift Servers service.
- Create a new game session.
- Add a player to an existing game session.
- Remove a player from an existing game session.

###### Topics

- [Prerequisites](#integration-unity-client-sdk4-prereq "#integration-unity-client-sdk4-prereq")
- [Initialize a game client](#integration-unity-client-sdk4-initialize "#integration-unity-client-sdk4-initialize")
- [Create game session on a
  specific fleet](#integration-unity-client-sdk4-game-session "#integration-unity-client-sdk4-game-session")
- [Add players to game
  sessions](#integration-unity-client-sdk4-add-player "#integration-unity-client-sdk4-add-player")
- [Remove a player from a game
  session](#integration-unity-client-sdk4-remove-player "#integration-unity-client-sdk4-remove-player")

## Prerequisites

Before setting up game server communication with the Amazon GameLift Servers client, complete the
following tasks:

- [Set up an AWS user account](setting-up-aws-login.md "setting-up-aws-login.md")
- [Install and set up the plugin](unity-plug-in-sdk4.md#unity-plug-in-sdk4-install "unity-plug-in-sdk4.md#unity-plug-in-sdk4-install")
- [Integrate Amazon GameLift Servers with a Unity game server
  project](integration-unity-server-sdk4.md "integration-unity-server-sdk4.md")
- [Deploy hosting fleets for Amazon GameLift Servers](fleets-intro.md "fleets-intro.md")

## Initialize a game client

###### Note

This topic refers to Amazon GameLift Servers plugin for Unity version 1.0.0,
which uses server SDK 4.x or earlier.

Add code to initialize a game client. Run this code on launch, it's necessary for
other Amazon GameLift Servers functions.

1. Initialize `AmazonGameLiftClient`. Call
   `AmazonGameLiftClient` with either a default client configuration
   or a custom configuration. For more information on how to configure a client,
   see [Set up the Amazon GameLift Servers API](gamelift-sdk-client-api.md#gamelift-sdk-client-api-initialize "gamelift-sdk-client-api.md#gamelift-sdk-client-api-initialize").
2. Generate a unique player id for each player to connect to a game session. For
   more information see [Generate player IDs](player-sessions-player-identifiers.md "player-sessions-player-identifiers.md").

The following examples shows how to set up an Amazon GameLift Servers client.

```
public class GameLiftClient
{
    private GameLift gl;
    //A sample way to generate random player IDs.
    bool includeBrackets = false;
    bool includeDashes = true;
    string playerId = AZ::Uuid::CreateRandom().ToString<string>(includeBrackets, includeDashes);


    private Amazon.GameLift.Model.PlayerSession psession = null;
    public AmazonGameLiftClient aglc = null;

    public void CreateGameLiftClient()
    {
        //Access Amazon GameLift Servers service by setting up a configuration.
        //The default configuration specifies a location.
        var config = new AmazonGameLiftConfig();
        config.RegionEndpoint = Amazon.RegionEndpoint.USEast1;

        CredentialProfile profile = null;
        var nscf = new SharedCredentialsFile();
        nscf.TryGetProfile(profileName, out profile);
        AWSCredentials credentials = profile.GetAWSCredentials(null);
        //Initialize Amazon GameLift Servers Client with default client configuration.
        aglc = new AmazonGameLiftClient(credentials, config);

    }
}

```

## Create game session on a

specific fleet

###### Note

This topic refers to Amazon GameLift Servers plugin for Unity version 1.0.0,
which uses server SDK 4.x or earlier.

Add code to start new game sessions on your deployed fleets and make them available to
players. After Amazon GameLift Servers has created the new game session and returned
a `GameSession`, you can add players to it.

- Place a request for a new game session.
  - If your game uses fleets, call `CreateGameSession()` with a
    fleet or alias ID, a session name, and maximum number of concurrent
    players for the game.
  - If your game uses queues, call
    `StartGameSessionPlacement()`.

The following example shows how to create a game session.

```
public Amazon.GameLift.Model.GameSession()
{
    var cgsreq = new Amazon.GameLift.Model.CreateGameSessionRequest();
    //A unique identifier for the alias with the fleet to create a game session in.
    cgsreq.AliasId = aliasId;
    //A unique identifier for a player or entity creating the game session
    cgsreq.CreatorId = playerId;
    //The maximum number of players that can be connected simultaneously to the game session.
    cgsreq.MaximumPlayerSessionCount = 4;

    //Prompt an available server process to start a game session and retrieves connection information for the new game session
    Amazon.GameLift.Model.CreateGameSessionResponse cgsres = aglc.CreateGameSession(cgsreq);
    string gsid = cgsres.GameSession != null ? cgsres.GameSession.GameSessionId : "N/A";
    Debug.Log((int)cgsres.HttpStatusCode + " GAME SESSION CREATED: " + gsid);
    return cgsres.GameSession;
}
```

## Add players to game

sessions

###### Note

This topic refers to Amazon GameLift Servers plugin for Unity version 1.0.0,
which uses server SDK 4.x or earlier.

After Amazon GameLift Servers has created the new game session and returned
a `GameSession` object, you can add players to it.

1. Reserve a player slot in a game session by creating a new player session. Use
   `CreatePlayerSession` or `CreatePlayerSessions` with
   the game session ID and a unique ID for each player.
2. Connect to the game session. Retrieve the `PlayerSession` object to
   get the game session's connection information. You can use this information to
   establish a direct connection to the server process:
   1. Use the specified port and either the DNS name or IP address of the
      server process.
   2. Use the DNS name and port of your fleets. The DNS name and port are
      required if your fleets have TLS certificate generation enabled.
   3. Reference the player session ID. The player session ID is required if
      your game server validates incoming player connections.

The following examples demonstrates how to reserve a player spot in a game session.

```
public Amazon.GameLift.Model.PlayerSession CreatePlayerSession(Amazon.GameLift.Model.GameSession gsession)
{
    var cpsreq = new Amazon.GameLift.Model.CreatePlayerSessionRequest();
    cpsreq.GameSessionId = gsession.GameSessionId;
    //Specify game session ID.
    cpsreq.PlayerId = playerId;
    //Specify player ID.
    Amazon.GameLift.Model.CreatePlayerSessionResponse cpsres = aglc.CreatePlayerSession(cpsreq);
    string psid = cpsres.PlayerSession != null ? cpsres.PlayerSession.PlayerSessionId : "N/A";
    return cpsres.PlayerSession;
}
```

The following code illustrates how to connect a player with the game session.

```
public bool ConnectPlayer(int playerIdx, string playerSessionId)
{
    //Call ConnectPlayer with player ID and player session ID.
    return server.ConnectPlayer(playerIdx, playerSessionId);
}
```

## Remove a player from a game

session

###### Note

This topic refers to Amazon GameLift Servers plugin for Unity version 1.0.0,
which uses server SDK 4.x or earlier.

You can remove the players from the game session when they leave the game.

1. Notify the Amazon GameLift Servers service that a player has disconnected from the server
   process. Call `RemovePlayerSession` with the player's session
   ID.
2. Verify that `RemovePlayerSession` returns `Success`.
   Then, Amazon GameLift Servers changes the player slot to be available, which Amazon GameLift Servers can assign to a
   new player.

The following example illustrates how to remove a player session.

```
public void DisconnectPlayer(int playerIdx)
{
    //Receive the player session ID.
    string playerSessionId = playerSessions[playerIdx];
    var outcome = GameLiftServerAPI.RemovePlayerSession(playerSessionId);
    if (outcome.Success)
    {
        Debug.Log (":) PLAYER SESSION REMOVED");
    }
    else
    {
        Debug.Log(":(PLAYER SESSION REMOVE FAILED. RemovePlayerSession()
        returned " + outcome.Error.ToString());
    }
}
```
