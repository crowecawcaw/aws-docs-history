# How Amazon GameLift Servers Realtime servers work

A Realtime server acts as a stateless relay server, where the server relays packets
of messages and game data between the game clients that are connected to the game. The
Realtime server doesn't evaluate messages, process data, or perform any gameplay
logic. Each game client maintains its own view of the game state and provides updates to
other players through the relay server. Each game client is responsible for
incorporating these updates and reconciling its own game state.

You set up Realtime servers by uploading a Realtime servers script to Amazon GameLift Servers and
deploying it to a managed EC2 hosting fleet. The Realtime script is a custom
configuration for your game. Amazon GameLift Servers uses the script's instructions to manage the tasks of
setting up and running game servers for your players.

The default Realtime script is a set of JavaScript code. You configuration it for
use with your game client. Amazon GameLift Servers defines a set of server-side callbacks for Realtime
scripts. Implement these callbacks to add event-driven functionality to your server. For
example, you can:

- Authenticate a player when a game client tries to connect to the
  server.
- Validate whether a player can join a group upon request.
- Determine when to deliver messages from a certain player or to a target
  player, or perform additional processing in response.
- Notify all players when a player leaves a group or disconnects from the
  server.
- View the content of game session objects or message objects, and use the
  data.
  You can add custom logic for game session management by building it into the
  Realtime script. You can write code to access server-specific objects, add
  event-driven logic using callbacks, or add logic based on non-event scenarios. For
  example, you might add game logic to build a stateful game with a server-authoritative
  view of the game state.

A key advantage of Amazon GameLift Servers Realtime is the ability to update your scripts at any time. When you
update a script, Amazon GameLift Servers distributes the new version to all hosting resources within
minutes. After Amazon GameLift Servers deploys the new script, all new game sessions created after that
point will use the new script version. (Existing game sessions will continue to use the
original version.)

## How Realtime clients and servers

interact

During a game session, game clients interact by sending messages to the Realtime
server through a backend service. The backend service then relays the messages among
connected game clients to exchange activity, game state, and relevant game data. If
you've added custom game logic to the Realtime script, a Realtime server might
implement callbacks to start event-driven responses.

###### Communication protocol

Realtime servers and connected game clients communicate through two channels: a
TCP connection for reliable delivery, and a UDP channel for fast delivery. When
creating messages, game clients choose which protocol to use depending on the nature
of the message. Message delivery is set to UDP by default. If a UDP channel isn't
available, Amazon GameLift Servers sends messages using TCP as a fallback.

###### Message content

Message content consists of two elements: a required operation code (opCode) and
an optional payload. A message's opCode identifies a particular player activity or
game event, and the payload provides additional data related to the operation code.
Both of these elements are developer-defined. Your game client acts based on the
opCodes in the messages that it receives.

###### Player groups

Amazon GameLift Servers Realtime provides functionality to manage groups of players. By default, Amazon GameLift Servers places
all players who connect to a game session into an "all players" group. In addition,
developers can set up other groups for their games, and players can be members of
multiple groups simultaneously. Group members can send messages and share game data
with all players in the group. For example, if your gameplay relies on teams, you
can use player groups to enable communication within team members as well as
game-wide.

###### Encryption with TLS certificates

With Amazon GameLift Servers Realtime, server authentication and data packet encryption are built into the
service. You can choose to turn on these security features when you enable TLS
certificate generation. When a game client tries to connect with a Realtime
server, the server automatically responds with the TLS certificate, which the client
validates. Amazon GameLift Servers encrypts TCP (WebSockets) traffic using TLS 1.2 and UDP traffic
using DTLS 1.2.
