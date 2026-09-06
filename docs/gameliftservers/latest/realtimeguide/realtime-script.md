

# Customize an Amazon GameLift Servers Realtime script
<a name="realtime-script"></a>

To use Amazon GameLift Servers Realtime servers for your game, you need to provide a script (in the form of JavaScript code) to configure and optionally customize how the Amazon GameLift Servers Realtime server runs and interacts with your game clients. When your script is ready, upload it to the Amazon GameLift Servers service (see [Upload a script for Amazon GameLift Servers Realtime servers](realtime-script-uploading.md)) and use it to create a fleet of game server hosts.

Start with the default Realtime script and configure it with the following functionality.

## Manage game session life-cycle (required)
<a name="realtime-script-init"></a>

At a minimum, a Realtime script must include the `Init()` function, which prepares the Realtime server to start a game session. It is also highly recommended that you also provide a way to terminate game sessions, to ensure that new game sessions can continue to be started on your fleet.

The `Init()` callback function, when called, is passed a Realtime session object, which contains an interface for the Realtime server. See [Amazon GameLift Servers Realtime interface](realtime-script-objects.md) for more details on this interface.

To gracefully end a game session, the script must also call the Realtime server's `session.processEnding` function. This requires some mechanism to determine when to end a session. The script example code illustrates a simple mechanism that checks for player connections and triggers game session termination when no players have been connected to the session for a specified length of time.

Amazon GameLift Servers Realtime with the most basic configuration--server process initialization and termination--essentially act as stateless relay servers. The Realtime server relays messages and game data between game clients that are connected to the game, but takes no independent action to process data or perform logic. You can optionally add game logic, triggered by game events or other mechanisms, as needed for your game.

## Add server-side game logic (optional)
<a name="realtime-script-logic"></a>

You can optionally add game logic to your Realtime script. For example, you might do any or all of the following. The script example code provides illustration. See [Script reference for Amazon GameLift Servers Realtime](realtime-script-ref.md). 
+ **Add event-driven logic.** Implement the callback functions to respond to client-server events. See [Script callbacks for Amazon GameLift Servers Realtime](realtime-script-callbacks.md) for a complete list of callbacks.
+ **Trigger logic by sending messages to the server.** Create a set of special operation codes for messages sent from game clients to the server, and add functions to handle receipt. Use the callback `onMessage`, and parse the message content using the `gameMessage` interface (see [gameMessage.opcode](realtime-script-objects.md#realtime-script-objects-gamemessageopcode)). 
+ Enable game logic to access your other AWS resources. For details, see [ Communicate with other AWS resources from your fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-sdk-server-resources.html).
+ Allow game logic to access fleet information for the instance it is running on. For details, see [ Get fleet data for an Amazon GameLift Servers instance](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-sdk-server-fleetinfo.html).

## Node.js runtime versions
<a name="realtime-script-nodejs"></a>

Amazon GameLift Servers Realtime servers support multiple Node.js runtime versions. You can specify the Node.js version when creating a script. The supported versions are:
+ **Node.js 10** (Default) - Runs on Amazon Linux 2. Node.js 10 will reach end of support on September 30, 2026. See more details in the [Node.js 10 FAQs](https://aws.amazon.com/gamelift/faq/nodejs10/). For migration guidance, see [Migrating from Node.js 10 to 24](https://docs.aws.amazon.com/gamelift/latest/realtimeguide/realtime-script.html#realtime-script-nodejs-migration). 
+ **Node.js 24** (Recommended) - Runs on Amazon Linux 2023.

To specify the Node.js version and add optional customizations like install scripts, see [Upload a script for Amazon GameLift Servers Realtime servers](realtime-script-uploading.md).

## Migrating from Node.js 10 to 24
<a name="realtime-script-nodejs-migration"></a>

To migrate existing Amazon GameLift Servers Realtime servers from Node.js 10 to 24:

1. **Review your fleets** - Check if you have existing fleets from scripts running on Node.js 10. You can identify affected fleets using several methods:
   + In the Amazon GameLift Servers console, navigate to the AWS Health Dashboard, look for the Node.js 10 end of support notification, and choose the **Affected resources** tab to see a list of your fleets using scripts with Node.js 10 runtime.
   + In the Amazon GameLift Servers console, navigate to **Managed EC2 fleets** and look for fleets created from scripts with Node.js 10 runtime. You can also check the Node.js version in the details page of each script resource, as well as identify fleets created with each script.

1. **Create a new script** - Create and upload your existing script and choose the new target `NodeJsVersion` i.e., `24.x` for Node.js 24. If there are any errors uploading or starting your script, follow these steps:

   1. Review the changes between Amazon Linux 2 and Amazon Linux 2023. For more information on Amazon Linux 2023 and the architectural differences with Amazon Linux 2, see [ Comparing AL2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

   1. Review the changes between Node.js versions. For more information on Node.js version changes, see [Node.js release notes](https://nodejs.org/en/about/releases/).

   1. Update your script. Make required changes to your scripts to work with the new target Node.js version and operating system.

   1. Upload your new script. Upload your new script to Amazon GameLift Servers. For more information, see [Upload a script for Amazon GameLift Servers Realtime servers](realtime-script-uploading.md).

1. **Create a test fleet with the new script** - We recommend this step to ensure there are no errors in initializing your script and activating the fleet. For help with fleet creation issues, see [ Debug fleet creation issues](https://docs.aws.amazon.com/gameliftservers/latest/realtimeguide/fleets-creating-debug-realtime.html).

1. **Review fleet events for errors** - If there are errors during fleet creation, you can look for the error messages on the **Events** tab on the Fleets view page. For more information about fleet events, see [ Event](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_Event.html) in the API Reference.

1. **(Optional) Update your script** - If you encountered errors during script or fleet creation, fix and update your script until your fleet activates and the Amazon GameLift Servers Realtime server launches as expected. For troubleshooting guidance, see [Troubleshooting Amazon GameLift Servers issues](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/troubleshooting-intro.html).

1. **(Optional) Create test game sessions** - After your test fleet is active, set your game backend to target your new fleet. We recommend that you create test game sessions to verify game client connectivity.

1. **Migrate your player traffic to your new production fleet** - If you have a game in production serving live player traffic, you can use Amazon GameLift Servers Queues and Aliases to migrate players to your new Node.js 24 runtime fleets. Use aliases to transfer players to a new fleet. When sending game session requests to Amazon GameLift Servers, specify a fleet alias instead of a fleet ID. For more information, see [ Create an alias](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/aliases-creating.html).

For information about Node.js version support and end-of-life schedules, see the [Node.js releases](https://nodejs.org/en/about/releases/).

## Amazon GameLift Servers Realtime script example
<a name="realtime-script-examples"></a><a name="realtime-script-examples-custom"></a>

This example illustrates a basic script needed to deploy Amazon GameLift Servers Realtime plus some custom logic. It contains the required `Init()` function, and uses a timer mechanism to trigger game session termination based on length of time with no player connections. It also includes some hooks for custom logic, including some callback implementations. 

```
// Example Realtime Server Script
'use strict';

// Example override configuration
const configuration = {
    pingIntervalTime: 30000,
    maxPlayers: 32
};

// Timing mechanism used to trigger end of game session. Defines how long, in milliseconds, between each tick in the example tick loop
const tickTime = 1000;

// Defines how to long to wait in Seconds before beginning early termination check in the example tick loop
const minimumElapsedTime = 120;

var session;                        // The Realtime server session object
var logger;                         // Log at appropriate level via .info(), .warn(), .error(), .debug()
var startTime;                      // Records the time the process started
var activePlayers = 0;              // Records the number of connected players
var onProcessStartedCalled = false; // Record if onProcessStarted has been called

// Example custom op codes for user-defined messages
// Any positive op code number can be defined here. These should match your client code.
const OP_CODE_CUSTOM_OP1 = 111;
const OP_CODE_CUSTOM_OP1_REPLY = 112;
const OP_CODE_PLAYER_ACCEPTED = 113;
const OP_CODE_DISCONNECT_NOTIFICATION = 114;

// Example groups for user-defined groups
// Any positive group number can be defined here. These should match your client code.
// When referring to user-defined groups, "-1" represents all groups, "0" is reserved.
const RED_TEAM_GROUP = 1;
const BLUE_TEAM_GROUP = 2;

// Called when game server is initialized, passed server's object of current session
function init(rtSession) {
    session = rtSession;
    logger = session.getLogger();
}

// On Process Started is called when the process has begun and we need to perform any
// bootstrapping.  This is where the developer should insert any code to prepare
// the process to be able to host a game session, for example load some settings or set state
//
// Return true if the process has been appropriately prepared and it is okay to invoke the
// GameLift ProcessReady() call.
function onProcessStarted(args) {
    onProcessStartedCalled = true;
    logger.info("Starting process with args: " + args);
    logger.info("Ready to host games...");

    return true;
}

// Called when a new game session is started on the process
function onStartGameSession(gameSession) {
    // Complete any game session set-up

    // Set up an example tick loop to perform server initiated actions
    startTime = getTimeInS();
    tickLoop();
}

// Handle process termination if the process is being terminated by Amazon GameLift Servers
// You do not need to call ProcessEnding here
function onProcessTerminate() {
    // Perform any clean up
}

// Return true if the process is healthy
function onHealthCheck() {
    return true;
}

// On Player Connect is called when a player has passed initial validation
// Return true if player should connect, false to reject
function onPlayerConnect(connectMsg) {
    // Perform any validation needed for connectMsg.payload, connectMsg.peerId
    return true;
}

// Called when a Player is accepted into the game
function onPlayerAccepted(player) {
    // This player was accepted -- let's send them a message
    const msg = session.newTextGameMessage(OP_CODE_PLAYER_ACCEPTED, player.peerId,
                                             "Peer " + player.peerId + " accepted");
    session.sendReliableMessage(msg, player.peerId);
    activePlayers++;
}

// On Player Disconnect is called when a player has left or been forcibly terminated
// Is only called for players that actually connected to the server and not those rejected by validation
// This is called before the player is removed from the player list
function onPlayerDisconnect(peerId) {
    // send a message to each remaining player letting them know about the disconnect
    const outMessage = session.newTextGameMessage(OP_CODE_DISCONNECT_NOTIFICATION,
                                                session.getServerId(),
                                                "Peer " + peerId + " disconnected");
    session.getPlayers().forEach((player, playerId) => {
        if (playerId != peerId) {
            session.sendReliableMessage(outMessage, playerId);
        }
    });
    activePlayers--;
}

// Handle a message to the server
function onMessage(gameMessage) {
    switch (gameMessage.opCode) {
      case OP_CODE_CUSTOM_OP1: {
        // do operation 1 with gameMessage.payload for example sendToGroup
        const outMessage = session.newTextGameMessage(OP_CODE_CUSTOM_OP1_REPLY, session.getServerId(), gameMessage.payload);
        session.sendGroupMessage(outMessage, RED_TEAM_GROUP);
        break;
      }
    }
}

// Return true if the send should be allowed
function onSendToPlayer(gameMessage) {
    // This example rejects any payloads containing "Reject"
    return (!gameMessage.getPayloadAsText().includes("Reject"));
}

// Return true if the send to group should be allowed
// Use gameMessage.getPayloadAsText() to get the message contents
function onSendToGroup(gameMessage) {
    return true;
}

// Return true if the player is allowed to join the group
function onPlayerJoinGroup(groupId, peerId) {
    return true;
}

// Return true if the player is allowed to leave the group
function onPlayerLeaveGroup(groupId, peerId) {
    return true;
}

// A simple tick loop example
// Checks to see if a minimum amount of time has passed before seeing if the game has ended
async function tickLoop() {
    const elapsedTime = getTimeInS() - startTime;
    logger.info("Tick... " + elapsedTime + " activePlayers: " + activePlayers);

    // In Tick loop - see if all players have left early after a minimum period of time has passed
    // Call processEnding() to terminate the process and quit
    if ( (activePlayers == 0) && (elapsedTime > minimumElapsedTime)) {
        logger.info("All players disconnected. Ending game");
        const outcome = await session.processEnding();
        logger.info("Completed process ending with: " + outcome);
        process.exit(0);
    }
    else {
        setTimeout(tickLoop, tickTime);
    }
}

// Calculates the current time in seconds
function getTimeInS() {
    return Math.round(new Date().getTime()/1000);
}

exports.ssExports = {
    configuration: configuration,
    init: init,
    onProcessStarted: onProcessStarted,
    onMessage: onMessage,
    onPlayerConnect: onPlayerConnect,
    onPlayerAccepted: onPlayerAccepted,
    onPlayerDisconnect: onPlayerDisconnect,
    onSendToPlayer: onSendToPlayer,
    onSendToGroup: onSendToGroup,
    onPlayerJoinGroup: onPlayerJoinGroup,
    onPlayerLeaveGroup: onPlayerLeaveGroup,
    onStartGameSession: onStartGameSession,
    onProcessTerminate: onProcessTerminate,
    onHealthCheck: onHealthCheck
};
```