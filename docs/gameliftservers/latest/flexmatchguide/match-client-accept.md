

# Request player acceptance
<a name="match-client-accept"></a>

If you're using a matchmaker that has player acceptance turned on, add code to your client service to manage the player acceptance process. The process of managing player acceptances is identical for games that use FlexMatch with Amazon GameLift Servers-managed hosting and for games that use FlexMatch as a standalone solution.

**Request player acceptance for a proposed match:**

1. **Detect when a proposed match needs player acceptance.** Monitor the matchmaking ticket to detect when the status changes to `REQUIRES_ACCEPTANCE`. A change to this status triggers the FlexMatch event `MatchmakingRequiresAcceptance`.

1. **Get acceptances from all players.** Create a mechanism to present the proposed match details to every player in the matchmaking ticket. Players must be able to indicate that they either accept or reject the proposed match. You can retrieve match details by calling [DescribeMatchmaking](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeMatchmaking.html). Players have a limited time to respond before the matchmaker withdraws the proposed match and moves on.

1. **Report player responses to FlexMatch.** Report player responses by calling [AcceptMatch](https://docs.aws.amazon.com/gamelift/latest/apireference/API_AcceptMatch.html) with either accept or reject. All players in a matchmaking request must accept the match for it to go forward.

1. **Handle tickets with failed acceptances.** A request fails when any player in the proposed match either rejects the match or fails to respond by the acceptance time limit. Tickets for players who did accept the match are automatically returned to the ticket pool. Tickets for players who did not accept the match move to FAILURE status and are no longer processed. For tickets with multiple players, if any players in the ticket did not accept the match, the entire ticket fails.