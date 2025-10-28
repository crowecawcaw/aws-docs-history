# Add FlexMatch to a game client

This topic describes how to add FlexMatch matchmaking functionality to your client-side game
components.

We highly recommend that your game client make matchmaking requests through a
backend game service. By using this trusted source for your communication with the Amazon GameLift Servers service,
you can more easily protect against
hacking attempts and fake player data. If your game has a session directory service,
this is a good option for handling matchmaking requests. Using a backend game service for all calls to the
Amazon GameLift Servers service is a best practice when using FlexMatch with Amazon GameLift Servers hosting and as a standalone service.

Client-side updates are required whether you're using FlexMatch with Amazon GameLift Servers managed
hosting or as a standalone service with another hosting solution. Using the service API for Amazon GameLift Servers, which is part of
the AWS SDK, add the following functionality:

- Request matchmaking for one or multiple players (required). Depending on your matchmaking rule set,
  this request might require certain player-specific data, including player attributes and latency.
- Track the status of a matchmaking request (required). In general, this task requires setting up event notification.
- Request player acceptance for a proposed match (optional). This feature requires additional interaction with
  a player to display match details and allow them to accept or reject the match.
- Get game session connection information and join the game (required). After a game session has been started
  for the new match, retrieve connection information for the game session and use it to connect to the game session.

## Prerequisite client-side tasks

Before you can add client-side functionality to your game, you need to do these tasks:

- **Add the AWS SDK to your backend service.**
  Your backend service uses functionality in the Amazon GameLift Servers API, which is part of the
  AWS SDK. See [Amazon GameLift Servers
  SDKs for client services](../../../gamelift/latest/developerguide/gamelift-supported.md#gamelift-supported-clients "../../../gamelift/latest/developerguide/gamelift-supported.md#gamelift-supported-clients") to learn more about the AWS SDK and
  download the latest version. For API descriptions and functionality, see
  [Amazon GameLift Servers FlexMatch API reference (AWS SDK)](reference-awssdk-flex.md "reference-awssdk-flex.md").
- **Set up a matchmaking ticket system.** All
  matchmaking requests must have a unique ticket ID. Create a mechanism to
  generate unique ticket IDs and assign them to match requests. A ticket ID can
  use any string format, up to a maximum of 128 characters.
- **Collect information about your matchmaker.**
  Get the following information from your matchmaking configuration and rule set.
  - Name of the matchmaking configuration resource.
  - The list of player attributes, which are defined in the rule
    set.

- **Retrieve player data.** Set up a way to get
  relevant data for each player to include in your matchmaking requests. You need
  the player ID and player attribute values. If your rule set has latency rules or
  you want to use latency data when placing game sessions, collect latency data
  for each geographic location where the player is likely be slotted into a
  game.
  To obtain accurate latency measurements, use Amazon GameLift Servers's
  UDP ping beacons. These endpoints enable you to measure actual UDP network latency
  between player devices and each of the potential hosting locations,
  resulting in more accurate placement decisions than using ICMP pings. For
  more information on using UDP ping beacons to measure latency, refer to [UDP ping beacons](../developerguide/reference-udp-ping-beacons.md "../developerguide/reference-udp-ping-beacons.md").
