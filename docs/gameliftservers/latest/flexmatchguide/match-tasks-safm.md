# Roadmap: Create a standalone matchmaking solution with FlexMatch

This topic outlines the complete integration process for implementing FlexMatch as a
standalone matchmaking service. Use this process if your multiplayer game is hosted using
peer-to-peer, custom-configured on-premises hardware, or other cloud compute primitives.
This process is also for use with Amazon GameLift Servers FleetIQ, which is a hosting optimization solution for
games that are hosted on Amazon EC2. If you're hosting your game using Amazon GameLift Servers managed hosting
(including Amazon GameLift Servers Realtime), see [Roadmap: Add matchmaking to a Amazon GameLift Servers hosting solution](match-tasks.md "match-tasks.md").

Before you start integration, you must have an AWS account and set up access permissions
for the Amazon GameLift Servers service. For details, see [Set up an AWS account for FlexMatch](match-getting-started.md#match-setting-up "match-getting-started.md#match-setting-up"). All essential tasks related to creating and managing
Amazon GameLift Servers FlexMatch matchmakers and rule sets can be done using the Amazon GameLift Servers console.

1. **Create a FlexMatch matchmaking rule set.** Your custom
   rule set provides complete instructions for how to construct a match. In it, you
   define the structure and size of each team. You also provide a set of requirements
   that a match must meet to be valid, which FlexMatch uses to include or exclude players
   in a match. These requirements might apply to individual players. You can also
   customize the FlexMatch algorithm in the rule set, such as to build large matches with
   up to 200 players. See these topics:
   - [Build a FlexMatch rule set](match-rulesets.md "match-rulesets.md")
   - [FlexMatch rule set examples](match-examples.md "match-examples.md")

2. **Set up notifications for matchmaking events.** Use
   notifications to track FlexMatch matchmaking activity, including the status of pending
   match requests. This is the mechanism that's used to deliver the results of a
   proposed match. Since matchmaking requests are asynchronous, you need a way to track
   the status of requests. Using notifications is the preferred option for this. See
   these topics:
   - [Set up FlexMatch event notifications](match-notification.md "match-notification.md")
   - [FlexMatch matchmaking events](match-events.md "match-events.md")

3. **Set up a FlexMatch matchmaking configuration.** Also
   called a matchmaker, this component receives matchmaking requests and processes
   them. You configure a matchmaker by specifying a rule set, notification target, and
   maximum wait time. You can also enable optional features. See these topics:
   - [Design a FlexMatch matchmaker](match-configuration.md "match-configuration.md")
   - [Create a matchmaking configuration](match-create-configuration.md "match-create-configuration.md")

4. **Build a client matchmaking service.** Create or
   expand a game client service with functionality to build and send matchmaking
   requests to FlexMatch. To build matchmaking requests, this component must have
   mechanisms to get the player data required by the matchmaking rule set and,
   optionally, regional latency information. It must also have a method for creating
   and assigning unique ticket IDs for each request. You might also choose to build a
   player acceptance workflow that requires players to opt in to a proposed match. This
   service must also monitor matchmaking events to get match results and initiate game
   session placement for successful matches. See this topic:
   - [Add FlexMatch to a game client](match-client.md "match-client.md")

5. **Build a match placement service.** Create a
   mechanism that works with your existing game hosting system to locate available
   hosting resources and start new game sessions for successful matches. This component
   must be able to use match results information to get an available game server and
   start a new game session for the match. You might also want to implement a workflow
   to make match backfill requests, which uses matchmaking to fill open slots in
   matched game sessions that are already running.
