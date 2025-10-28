# Request matchmaking for players

Add code to your game backend service to manage matchmaking requests to a FlexMatch
matchmaker. The process of requesting FlexMatch matchmaking is identical for games that use
FlexMatch with Amazon GameLift Servers hosting and for games that use FlexMatch as a standalone
solution.

## To create a matchmaking request:

Call the Amazon GameLift Servers API [StartMatchmaking](../../../gamelift/latest/apireference/API_StartMatchmaking.md "../../../gamelift/latest/apireference/API_StartMatchmaking.md"). Each request must contain the following
information.

**Matchmaker**

The name of the matchmaking configuration to use for the request.
FlexMatch places each request into the pool for the specified
matchmaker, and the request is processed based on how the matchmaker
is configured. This includes enforcing a time limit, whether to
request player acceptance of matches, which queue to use when
placing a resulting game session, etc. Learn more about matchmakers
and rules sets in [Design a FlexMatch matchmaker](match-configuration.md "match-configuration.md").

**Ticket ID**

A unique ticket ID assigned to the request. Everything related to
the request, including events and notifications, will reference the
ticket ID.

**Player data**

List of players that you want to create a match for. If any of the
players in the request do not meet match requirements, based on the
match rules and latency minimums, the matchmaking request will never
result in a successful match. You can include up to ten players in a
match request. When there are multiple players in a request, FlexMatch
tries to create a single match and assign all players to the same
team (randomly selected). If a request contains too many players to
fit in one of the match teams, the request will fail to be matched.
For example, if you've set up your matchmaker to create 2v2 matches
(two teams of two players), you cannot send a matchmaking request
containing more than two players.

###### Note

A player (identified by their player ID) can only be included
in one active matchmaking request at a time. When you create a
new request for a player, any active matchmaking tickets with
the same player ID are automatically canceled.

For each listed player, include the following data:

- _Player ID_ – Each
  player must have a unique player ID, which you generate. See
  [Generate player IDs](../../../gamelift/latest/developerguide/player-sessions-player-identifiers.md "../../../gamelift/latest/developerguide/player-sessions-player-identifiers.md").

###### Important

When you create a new matchmaking request that contains a player ID that is already included in an existing active matchmaking request, the existing request is automatically cancelled. However, a `MatchmakingCancelled` event is not sent for the cancelled request. To monitor the status of existing matchmaking requests, use [DescribeMatchmaking](../../../gamelift/latest/apireference/API_DescribeMatchmaking.md "../../../gamelift/latest/apireference/API_DescribeMatchmaking.md") to poll the request status at infrequent intervals (30-60 seconds). The cancelled request will show a status of `CANCELLED` with the reason `Cancelled due to duplicate player`.

- _Player attributes_
  – If the matchmaker in use calls for player
  attributes, the request must provide those attributes for
  each player. The required player attributes are defined in
  the matchmaker's rule set, which also specifies the data
  type for the attribute. A player attribute is optional only
  when the rule set specifies a default value for the
  attribute. If the match request does not provide required
  player attributes for all players, the matchmaking request
  can never succeed. Learn more about matchmaker rule sets and
  player attributes in [Build a FlexMatch rule set](match-rulesets.md "match-rulesets.md") and [FlexMatch rule set examples](match-examples.md "match-examples.md").
- _Player latencies_ –
  If the matchmaker in use has a player latency rule, the request
  must report latency for each player. Player latency data is a
  list of one or more values per player. It represents the latency
  that the player experiences for regions in the matchmaker's
  queue. If no latency values for a player are included in the
  request, the player cannot be matched, and the request fails.
  To obtain accurate latency measurements,
  use Amazon GameLift Servers's UDP ping beacons. These endpoints enable you to measure
  actual UDP network latency between player devices and a
  potential hosting location, resulting in more accurate
  placement decisions than using ICMP pings. For more
  information on using UDP ping beacons to measure latency, refer to
  [UDP ping beacons](../developerguide/reference-udp-ping-beacons.md "../developerguide/reference-udp-ping-beacons.md").

## To retrieve match request details

After a match request is sent, you can view the request details by calling
[DescribeMatchmaking](../../../gamelift/latest/apireference/API_DescribeMatchmaking.md "../../../gamelift/latest/apireference/API_DescribeMatchmaking.md") with the request's ticket ID. This call returns
the request information, including current status. Once a request has been
successfully completed, the ticket also contains the information that a game
client needs to connect to the match.

## To cancel a match request

You can cancel a matchmaking request at any time by calling [StopMatchmaking](../../../gamelift/latest/apireference/API_StopMatchmaking.md "../../../gamelift/latest/apireference/API_StopMatchmaking.md") with the
request's ticket ID.
