# Add FlexMatch to an Amazon GameLift Servers-hosted game server

When Amazon GameLift Servers creates a match, it generates a set of match result data that describes key
matchmaking details, including team assignments. A game server uses this data, as well as
other game session information, when starting a new game session to host the match.

###### For game servers that are hosted with Amazon GameLift Servers

The Amazon GameLift Servers prompts a game server process to start a game session. It delivers a [GameSession](../apireference/API_GameSession.md "../apireference/API_GameSession.md") object that describes the type of game session to create and
includes player-specific information, including match data.

###### For game servers that are hosted on other solutions

After successfully fulfilling a matchmaking request, Amazon GameLift Servers emits an event that
includes the match results. You can use this data with your own hosting solution to
start a game session for the match.

## About matchmaker data

Match data includes the following information:

- A unique match ID
- The ID of the matchmaking configure that was used to create the match
- The players selected for the match
- Team names and team assignments
- Player attribute values that were used to form the match. Attributes might
  also provide information that directs how a game session is set up. For example,
  the game server might assign characters to players based on player attributes,
  or choose a game map preference that is common to all players.
  Or your game might unlock certain features or levels based on the
  average player skill level.

Match data doesn't include the player latency. If you need latency data on current
players, such as for match backfill, we recommend getting fresh data.

###### Note

Matchmaker data specifies the full matchmaking configuration ARN, which identifies
the configuration name, AWS account, and Region. For games hosting with Amazon GameLift Servers, if
you 're using match backfill, you need the configuration name only. The
configuration name is the string that follows ":matchmakingconfiguration/". In the
following example, the matchmaking configuration name is
"MyMatchmakerConfig".

This JSON example shows a typical matchmaker data set. It describes a two-player game,
with players matched based on skill ratings and highest level attained.

```
{
	"matchId":"1111aaaa-22bb-33cc-44dd-5555eeee66ff",
	"matchmakingConfigurationArn":"arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MyMatchmakerConfig",
	"teams":[
	   {"name":"attacker",
		"players":[
           {"playerId":"4444dddd-55ee-66ff-77aa-8888bbbb99cc",
			"attributes":{
				"skills":{
					"attributeType":"STRING_DOUBLE_MAP",
					"valueAttribute":{"Body":10.0,"Mind":12.0,"Heart":15.0,"Soul":33.0}}
			}
		}]
	},{
		"name":"defender",
		"players":[{
			"playerId":"3333cccc-44dd-55ee-66ff-7777aaaa88bb",
			"attributes":{
				"skills":{
					"attributeType":"STRING_DOUBLE_MAP",
					"valueAttribute":{"Body":11.0,"Mind":12.0,"Heart":11.0,"Soul":40.0}}
			}
		}]
	}]
}
```
