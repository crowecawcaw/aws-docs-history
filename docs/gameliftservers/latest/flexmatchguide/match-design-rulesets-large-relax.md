# Relax large match

requirements

As with small matches, you can use expansions to relax match requirements over
time when no valid matches are possible. With large matches, you have the option to
relax either the latency rules or the team player counts.

If you're using automatic match backfill for large matches, avoid relaxing your
team player counts too quickly. FlexMatch starts generating backfill requests only
after a game session starts, which may not happen for several seconds after a match
is created. During that time, FlexMatch can create multiple partially filled new game
sessions, especially when the player count rules are lowered. As a result, you end
up with more game sessions than you need and players spread too thinly across them.
Best practice is to give the first step in your player count expansion a longer wait
time, long enough for your game session to start. Since backfill requests are given
higher priority with large matches, incoming players will be slotted into existing
games before new game are started. You may need to experiment to find the ideal wait
time for your game.

Here's an example that gradually lowers the Yellow team's player count, with a
longer initial wait time. Keep in mind that wait times in rule set expansions are
absolute, not compounded. So the first expansion occurs at five seconds, and the
second expansion occurs five seconds later, at ten seconds.

```
"expansions": [{
        "target": "teams[Yellow].minPlayers",
        "steps": [{
            "waitTimeSeconds": 5,
            "value": 8
        }, {
            "waitTimeSeconds": 10,
            "value": 5
        }]
    }]
```
