# Add optional elements

In addition to these minimum requirements, you can configure your matchmaker with the
following additional options. If you are using FlexMatch with a Amazon GameLift Servers hosting solution,
many features are built in. If you're using FlexMatch as a standalone matchmaking service,
you might want to build these features into your system.

###### Player Acceptance

You can configure a matchmaker to require that all players who are selected for a
match must accept participation. If your system requires acceptance, all players
must be given the option to accept or reject a proposed match. A match must receive
acceptances from all players in the proposed match before it can be completed. If
any player rejects or fails to accept a match, the proposed match is discarded and
the tickets are handled as follows. Tickets where all players in the ticket accepted
the match are returned to the matchmaking pool for continued processing. Tickets
where at least one player rejected the match or failed to respond are put into a
failure status and are no longer processed. Player acceptance requires a time limit;
all players must accept a proposed match within the time limit for the match to
continue.

###### Backfill Mode

Use FlexMatch backfill to keep your game sessions filled with well-matched new
players throughout the life span of the game session. When handling backfill
requests, FlexMatch uses the same matchmaker as was used to match the original players.
You can customize how backfill tickets are prioritized with tickets for new matches,
putting backfill tickets to either the front or end of the line. This means that, as
new players enter the matchmaking pool, they are more or less likely to be placed in
an existing game than in a newly formed game.

Manual backfill is available whether your game uses FlexMatch with managed Amazon GameLift Servers hosting
or with other hosting solutions. Manual backfill gives you the flexibility to decide
when to trigger a backfill request. For example, you may want to add new players only
during certain phases of your game or only when certain conditions exist.

Automatic backfill is available only for games that use managed Amazon GameLift Servers hosting. With
this feature enabled, if a game session starts with open player slots, Amazon GameLift Servers begins
automatically generating backfill requests for it. This feature allows you to set up
matchmaking so that new games are started with a minimum number of players and then
quickly filled as new players enter the matchmaking pool. You can turn off automatic
backfill at any time during the game session life span.

###### Game Properties

For games that use FlexMatch with Amazon GameLift Servers managed hosting, you can provide additional
information to be passed to a game server whenever a new game session is requested.
This can be a useful way to pass game mode configurations that are needed to start a
game session for the type of matches being created. All game sessions for matches
that are created by a matchmaker receive the same set of game properties. You can
vary game property information by creating different matchmaking
configurations.

###### Reserved Player Slots

You can designate that certain player slots in each match be reserved and filled
at a later time. This is done by configuring the "additional player count" property
of a matchmaking configuration.

###### Custom Event Data

Use this property to include a set of custom information in all
matchmaking-related events for the matchmaker. This feature can be useful for
tracking certain activity unique to your game, including tracking performance of
your matchmakers.
