# Shut down a game session

Use the Amazon GameLift Servers console to shut down a specific game session. This feature gives you a
simple and fast method for locating a game session and sending a signal to terminate it.
Another termination method requires that you find the fleet instance where the game
session is running, remotely access the instance, and manually shut down the game
session.

You can shut down a game session for any reason. The most common reason is to resolve
a game session that's failing to shut down naturally. As a result, the hosting resource
for the game session can't be freed to host a new game session, and the fleet's hosting
capacity is degraded.

###### Note

This feature relies on certain configuration settings for your hosting solution.
It has the following limitations:

- The game session must be hosted on a fleet that's running a game server
  build with server SDK for Amazon GameLift Servers v5 or greater. If your game servers are deployed
  with an older version, you need to use remote access to delete the game
  session.
- If the game session is hosted on an Anywhere fleet, the fleet must be
  using the Amazon GameLift Servers Agent to manage game server processes.

###### To terminate a game session

1. In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"),
   open the left navigation pane. Select a hosting solution type and open the
   **Fleets** page. For example:
   - **Hosting**, **Anywhere**, **Fleets**
   - **Hosting**, **Managed EC2**, **Fleets**
   - **Hosting**, **Managed containers**, **Fleets**

2. Each **Fleets** page displays the list of fleets for your
   currently selected AWS Region. Choose the fleet that's hosting the game
   session that you want to terminate.
3. In the fleet's detail page, open the **Game sessions** tab.
   In the list of game sessions, select the one that you want to terminate, and
   choose the **Terminate** button.
4. In the **Terminate game session?** window, verify that you're
   shutting down the right game session and choose a termination method.
   - Normal game session shutdown – This option sends a signal to the server process that's
     hosting the game session to shut down. If your game server build was
     properly integrated for Amazon GameLift Servers, the server process initiates its game
     session shutdown sequence, notifies Amazon GameLift Servers that it's ending, and stops.
     Depending on your game design, the shutdown sequence might include steps
     to gracefully complete the game session, such as saving data and
     notifying active players. This method might require a small delay to
     complete the game session shutdown sequence.
   - Immediate game session shutdown – This option sends a signal to a process manager to
     shut down the server process that's hosting the game session. This
     option bypasses the normal game session shutdown. It's able to terminate
     the game session even when the server process is unable to
     respond.

5. Confirm game session termination. You can track the shutdown progress on the
   **Game sessions** console page. The game session status
   will change to "Terminating", and then to "Terminated" when shutdown is
   complete.
   **Related topics**

- You can also shutdown game sessions using the AWS SDK and the AWS CLI. For more details and examples, see the Amazon GameLift Servers API Reference topic
  [TerminateGameSession](../apireference/API_TerminateGameSession.md "../apireference/API_TerminateGameSession.md").
- For more information on game server integration and how a server process responds to signals from the Amazon GameLift Servers service, see
  [Add Amazon GameLift Servers to your game server with the server
  SDK](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md").
