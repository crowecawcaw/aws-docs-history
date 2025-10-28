# Game and player sessions in

the Amazon GameLift Servers console

You can use the Amazon GameLift Servers console to work with games sessions and player sessions. For more
information about game sessions and player sessions, see [How players connect to games](game-sessions-intro.md "game-sessions-intro.md"). The Amazon GameLift Servers console provides information and tools to
help you investigate issues with your game sessions.

What you can do:

- Explore game session and player session activity that is hosted on a specific fleet.
- Look up game session activity for a specific player across multiple fleets.
- Shut down a specific game session.

## View game session detail

Game session and player session data is organized by the fleet that hosts the game
session.

###### To access game session and player session information

1. In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"),
   open the left navigation pane. Select a hosting solution type and open the
   **Fleets** page. For example:
   - **Hosting**, **Anywhere**, **Fleets**
   - **Hosting**, **Managed EC2**, **Fleets**
   - **Hosting**, **Managed containers**, **Fleets**

2. Each **Fleets** page displays the list of fleets for your
   currently selected AWS Region. Choose the fleet that you want to view game
   session data for.
3. In the fleet's detail page, open the **Game sessions** tab. This
   tab lists all game sessions that were hosted on the fleet, along with summary
   information. You can adjust the table content as needed using the **Preferences**
   tool (see the ![Gear icon representing settings or configuration options.](images/settings.png)
   icon in the upper right corner of the table). Custom preferences are saved to your AWS
   account user and are automatically applied whenever you view this page.
4. Choose a game session from the list to view additional information.
5. If the game session includes player session data, choose **View player
   sessions** to open the player sessions lookup tool with the game
   session ID automatically filled in.

The **Game sessions** detail include the following information:

- **Status** – Game session status.
  - **Activating** – The instance is initiating a
    game session.
  - **Active** – A game session is running and
    available to receive players, depending on the session's [player creation
    policy](../../../gamelift/latest/apireference/API_GameSession.md "../../../gamelift/latest/apireference/API_GameSession.md").
  - **Terminated** – the game session has
    ended.

- **ARN** – The Amazon Resource Name of the game
  session.
- **Name** – Name generated for the game session.
- **Location** – The location that Amazon GameLift Servers hosted the game
  session in.
- **Creation time** – Date and time that Amazon GameLift Servers created
  the stream session.
- **Ending time** – Date and time that the game session
  ended.
- **DNS name** – The host name of the game
  session.
- **IP address** – IP address specified for the game
  session.
- **Port** – Port number used to connect to
  the game session.
- **Creator ID** – A unique identifier of the player
  that initiated the game session.
- **Player session creation policy** – Indicates if the
  game session is accepting new players.
- **Game scaling protection policy** – The type of game
  session protection to set on all new instances that Amazon GameLift Servers starts in the
  fleet.

###### Game data

Game property data, formatted as a string, to send to your game session on
start.

###### Game properties

Game property data, formatted as key/value pairs, to send to your game session on
start.

###### Matchmaking data

If the game session was created with FlexMatch, matchmaking data describes
information about the matchmaking configuration and rule set. This includes each
match's player attributes and team assignments. Data is in JSON format. For more
information about FlexMatch matchmaking, see [Build a
matchmaker](../flexmatchguide/matchmaker-build.md "../flexmatchguide/matchmaker-build.md").
