

# Connect to a match
<a name="match-client-connect"></a>

Add code to your client service to handle a successfully formed match (status `COMPLETED` or event `MatchmakingSucceeded`). This includes notifying the match's players and handing off connection information to their game clients. 

For games that use Amazon GameLift Servers managed hosting, when a matchmaking request is successfully fulfilled, the game session connection information is added to the matchmaking ticket. Retrieve a completed matchmaking ticket by calling [DescribeMatchmaking](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeMatchmaking.html). Connection information includes the game session's IP address and port, as well as a player session ID for each player ID. Learn more in [GameSessionConnectionInfo](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameSessionConnectionInfo.html). Your game client can use this information to connect directly to the game session for the match. The connection request should include a player session ID and a player ID. This data associates the connected player to the game session's match data, which includes team assignments (see [GameSession](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameSession.html)). 

For games that use other hosting solutions, including Amazon GameLift Servers FleetIQ, you must build in a mechanism to enable match players to connect to the appropriate game session. 