# FlexMatch matchmaking process

This topic describes the sequence of events in a basic matchmaking scenario, including the interactions between the various
your game components and the FlexMatch service.

**Step 1: Request matchmaking for players**

A player using your game client clicks a "Join Game" button. This action
causes your client matchmaking service to send a matchmaking request to
FlexMatch. The request identifies the FlexMatch matchmaker to use when fulfilling
the request. The request also includes player information that your custom
matchmaker requires, such as skill level, play preferences, or geographic
latency data. You can make matchmaking requests for one player or multiple
players.

**Step 2: Add requests to the matchmaking pool**

When FlexMatch receives the matchmaking request, it generates a matchmaking
ticket and adds it to the matchmaker's ticket pool. The ticket remains in
the pool until it is matched or a maximum time limit is reached. Your client
matchmaking service is periodically notified about matchmaking events,
including changes in ticket status.

**Step 3: Build a match**

Your FlexMatch matchmaker continually runs the following process on all
tickets in its pool:

1. The matchmaker sorts the pool by ticket age, then begins building
   a potential match starting with the oldest ticket.
2. The matchmaker adds a second ticket to the potential match and
   evaluates the result against your custom matchmaking rules. If the
   potential match passes evaluation, the ticket's players are assigned
   to a team.
3. The matchmaker adds the next ticket in sequence and repeats the
   evaluation process. When all player slots have been filled, the
   match is ready.

Matchmaking for large matches (41 to 200 players) uses a modified version
of the process described above so that it can build matches in a reasonable
time frame. Instead of evaluating each ticket individually, the matchmaker
divides a pre-sorted ticket pool into potential matches, and then balances
each match based on a player characteristic that you've specified. For
example, a matchmaker might pre-sort tickets based on similar low-latency
locations, and then use post-match balancing to make sure that the teams are
evenly matched by player skill.

**Step 4: Report matchmaking results**

When an acceptable match is found, all matched tickets are updated and a
successful matchmaking event is generated for each matched ticket.

- FlexMatch as a standalone service: Your game receives match results
  in a successful matchmaking event. Result data includes a list of
  all matched players and their team assignments. If your match
  requests contain player latency info, the results also suggest an
  optimal geographic location for the match.
- FlexMatch with a Amazon GameLift Servers hosting solution: Match results are
  automatically passed to a Amazon GameLift Servers queue for game session placement.
  The matchmaker determines which queue is used for game session
  placement.

**Step 5: Start a game session for the match**

After a proposed match is successfully formed, a new game session is
started. Your game servers must be able to use the matchmaking result data,
including player IDs and team assignments, when setting up a game session
for the match.

- FlexMatch as a standalone service: Your custom match placement
  service gets match result data from successful matchmaking events,
  and connects to your existing game session placement system to
  locate an available hosting resource for the match. After a hosting
  resource is found, the match placement service coordinates with your
  existing hosting system to start a new game session and acquire
  connection information.
- FlexMatch with a Amazon GameLift Servers hosting solution: The game session queue
  locates the best available game server for the match. Depending on
  how the queue is configured, it tries to place the game session with
  the lowest-cost resources and where players will experience low
  latency (if player latency data is provided). Once the game session
  is successfully placed, the Amazon GameLift Servers service prompts the game server to
  start a new game session, passing on the matchmaking results and
  other optional game data.

**Step 6: Connect players to the match**

After a game session is started, players connect to the session, claim
their team assignment, and begin gameplay.

- FlexMatch as a standalone service: Your game uses the existing game
  session management system to provide connection information back to
  players.
- FlexMatch with a Amazon GameLift Servers hosting solution: On a successful game session
  placement, FlexMatch updates all of the matched tickets with game
  session connection information and a player session ID.
