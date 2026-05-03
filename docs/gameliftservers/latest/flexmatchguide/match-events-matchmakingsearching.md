# MatchmakingSearching

Ticket has been entered into matchmaking. This includes new requests and requests that
were part of a proposed match that failed.

**Resource:** ConfigurationArn

**Detail:** type, tickets, estimatedWaitMillis,
gameSessionInfo

###### Note

The `estimatedWaitMillis` value is reported in
_seconds_, not milliseconds. When available, the value is an
integer representing seconds; otherwise it is the string
`"NOT_AVAILABLE"`. This value matches the
`EstimatedWaitTime` field returned by the [DescribeMatchmaking](../../../gamelift/latest/apireference/API_DescribeMatchmaking.md "../../../gamelift/latest/apireference/API_DescribeMatchmaking.md") API,
which is also in seconds. If your application already interprets this value as
seconds, no change is needed.

## Example

```
{
  "version": "0",
  "id": "cc3d3ebe-1d90-48f8-b268-c96655b8f013",
  "detail-type": "GameLift Matchmaking Event",
  "source": "aws.gamelift",
  "account": "123456789012",
  "time": "2017-08-08T21:15:36.421Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:gamelift:us-west-2:123456789012:matchmakingconfiguration/SampleConfiguration"
  ],
  "detail": {
    "tickets": [
      {
        "ticketId": "ticket-1",
        "startTime": "2017-08-08T21:15:35.676Z",
        "players": [
          {
            "playerId": "player-1"
          }
        ]
      }
    ],
    "estimatedWaitMillis": "NOT_AVAILABLE",
    "type": "MatchmakingSearching",
    "gameSessionInfo": {
      "players": [
        {
          "playerId": "player-1"
        }
      ]
    }
  }
}
```
