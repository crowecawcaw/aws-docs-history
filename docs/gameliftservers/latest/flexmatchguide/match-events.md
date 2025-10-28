# FlexMatch matchmaking events

Amazon GameLift Servers FlexMatch emits events for each matchmaking ticket as it is processed. You can publish
these events to an Amazon SNS topic, as described in [Set up FlexMatch event notifications](match-notification.md "match-notification.md"). These events are also emitted to Amazon CloudWatch Events in near real
time and on a best-effort basis.

This topic describes the structure of FlexMatch events and provides an example for each event
type. For more information on matchmaking ticket statuses, see [MatchmakingTicket](../../../gamelift/latest/apireference/API_MatchmakingTicket.md "../../../gamelift/latest/apireference/API_MatchmakingTicket.md") in the _Amazon GameLift Servers API Reference_.

###### Topics

- [MatchmakingSearching](match-events-matchmakingsearching.md "match-events-matchmakingsearching.md")
- [PotentialMatchCreated](match-events-potentialmatchcreated.md "match-events-potentialmatchcreated.md")
- [AcceptMatch](match-events-acceptmatch.md "match-events-acceptmatch.md")
- [AcceptMatchCompleted](match-events-acceptmatchcompleted.md "match-events-acceptmatchcompleted.md")
- [MatchmakingSucceeded](match-events-matchmakingsucceeded.md "match-events-matchmakingsucceeded.md")
- [MatchmakingTimedOut](match-events-matchmakingtimedout.md "match-events-matchmakingtimedout.md")
- [MatchmakingCancelled](match-events-matchmakingcancelled.md "match-events-matchmakingcancelled.md")
- [MatchmakingFailed](match-events-matchmakingfailed.md "match-events-matchmakingfailed.md")
