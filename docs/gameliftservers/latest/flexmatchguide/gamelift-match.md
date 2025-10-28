# How Amazon GameLift Servers FlexMatch works

This topic provides an overview of the Amazon GameLift Servers FlexMatch service, including the core components
of a FlexMatch system and how they interact.

You can use FlexMatch with games that use Amazon GameLift Servers managed hosting or with games that use
another hosting solution. Games that are hosted on Amazon GameLift Servers servers, including Amazon GameLift Servers Realtime, use the
integrated Amazon GameLift Servers service to automatically locate available game servers and start game
sessions for the matches. Games that use FlexMatch as a standalone service, including Amazon GameLift Servers
FleetIQ, must coordinate with the existing hosting system to assign hosting resources and
start game sessions for the matches.

For detailed guidance on setting up FlexMatch for your games, see [Getting started with FlexMatch](match-getting-started.md "match-getting-started.md").

## Matchmaking components

A FlexMatch matchmaking system includes some or all of the following components.

###### Amazon GameLift Servers components

These are Amazon GameLift Servers resources that control how the FlexMatch service performs matchmaking
for your game. They are created and maintained using Amazon GameLift Servers tools, including the
console and the AWS CLI or, alternatively, programmatically using the AWS SDK
for Amazon GameLift Servers.

- **FlexMatch matchmaking configuration (also called a
  matchmaker)** – A matchmaker is a set of configuration
  values that customizes the matchmaking process for your game. A game can have
  multiple matchmakers, each configured for different game modes or experiences as
  needed. When your game sends a matchmaking request to FlexMatch, it specifies which
  matchmaker to use.
- **FlexMatch matchmaking rule set** – A rule
  set contains all the information that is needed to evaluate players for a
  potential matches and approve or reject. The rule set defines a match's team
  structure, declares the player attributes that are used for evaluation, and
  provides rules that describe the criteria for an acceptable match. Rules can
  apply to individual players, teams, or the entire match. For example, a rule
  might require that every players in the match choose the same game map, or it
  might require that all teams have similar player skill average.
- **Amazon GameLift Servers game session queue (for FlexMatch with Amazon GameLift Servers managed
  hosting only)** – A game session queue locates available
  hosting resources and starts a new game session for the match. The queue's
  configuration determines where Amazon GameLift Servers looks for available hosting resources and
  how to select the best available host for a match.

###### Custom components

The following components encompass functionality that's required for a complete
FlexMatch system that you must implement based on the architecture of your game.

- **Player interface for matchmaking** –
  This interface enables players to join a match. At a minimum, it initiates a
  matchmaking request through the client matchmaking service component and
  provides player-specific data, such as skill level and latency data, as needed
  for the matchmaking process.

###### Note

As a best practice, communication with the FlexMatch service should be done
by a backend service, not from a game client.

- **Client matchmaking service** – This
  service fields the player join requests from the player interface, generates
  matchmaking requests, and sends them to the FlexMatch service. For requests in
  process, it monitors matchmaking events, tracks matchmaking status, and takes
  action as needed. Depending on how you manage game session hosting in your game,
  this service may return game session connection information back to players.
  This component uses the AWS SDK with the Amazon GameLift Servers API to communicate with the
  FlexMatch service.
- **Match placement service (for FlexMatch as a standalone
  service only)** – This component works with your existing
  game hosting system to locate available hosting resources and start new game
  sessions for matches. The component must get the matchmaking results and extract
  the information needed to start a new game session, including player IDs,
  attributes, and team assignments for all players in the match.
