# Debug managed EC2 fleets for Amazon GameLift Servers Realtime

This topic provides guidance on how to resolve issues with your Amazon GameLift Servers managed EC2 fleets for Realtime servers. For general troubleshooting help
with managed EC2 fleets, see also [Debug Amazon GameLift Servers fleet issues](../developerguide/fleets-creating-debug.md "../developerguide/fleets-creating-debug.md") .

**Zombie game sessions: They start and run a game, but they never end.**

You might observe this issues as any of the following scenarios:

- Script updates are not picked up by the fleet's Realtime
  servers.
- The fleet quickly reaches maximum capacity and does not scale down
  when player activity (such as new game session requests) decreases.

This is almost certainly a result of failing to successfully call
`processEnding` in your Realtime script. Although the fleet
goes active and game sessions are started, there is no method for stopping
them. As a result, the Realtime server that is running the game session is
never freed up to start a new one, and new game sessions can only start when
new Realtime servers are spun up. In addition, updates to the Realtime
script do not impact already- running game sessions, only ones.

To prevent this from happening, scripts need to provide a mechanism to
trigger a `processEnding` call. As illustrated in the [Amazon GameLift Servers Realtime script example](realtime-script.md#realtime-script-examples "realtime-script.md#realtime-script-examples"), one way is to program an
idle session timeout where, if no player is connected for a certain amount
of time, the script will end the current game session.

However, if you do fall into this scenario, there are a couple workarounds
to get your Realtime servers unstuck. The trick is to trigger the
Realtime server processes—or the underlying fleet
instances—to restart. In this event, Amazon GameLift Servers automatically closes
the game sessions for you. Once Realtime servers are freed up, they can
start new game sessions using the latest version of the Realtime script.

There are a couple of methods to achieve this, depending on how pervasive
the problem is:

- Scale the entire fleet down. This method is the simplest to do but
  has a widespread effect. Scale the fleet down to zero instances,
  wait for the fleet to fully scale down, and then scale it back up.
  This will wipe out all existing game sessions, and let you start
  fresh with the most recently updated Realtime script.
- Remotely access the instance and restart the process. This is a
  good option if you have only a few processes to fix. If you are
  already logged onto the instance, such as to tail logs or debug,
  then this may be the quickest method. See
  [Remotely connect to Amazon GameLift Servers fleet instances](../developerguide/fleets-remote-access.md "../developerguide/fleets-remote-access.md").

If you opt not to include way to call `processEnding` in your Realtime
script, there are a couple of tricky situations that might occur even when the fleet
goes active and game sessions are started. First, a running game session does not end.
As a result, the server process that is running that game session is never free to start
a new game session. Second, the Realtime server does not pick up any script updates.
