# Failure management

| GAMEREL03: How do you persist game state during<br>infrastructure disruptions? |
| ------------------------------------------------------------------------------ |
|                                                                                |

As your game infrastructure experiences various operational events
over time, your game's architecture should be designed to maintain
continuity for player experiences and preserve game state during
infrastructure events. To handle these events, implement
monitoring, graceful shutdowns, and state persistence mechanisms
to verify smooth gameplay experiences for your players.

###### Best practices

- [GAMEREL03-BP01 Monitor game server disruptions, and use the
  data to improve hosting architecture to achieve reliability
  goals](gamerel03-bp01.md "gamerel03-bp01.md")
- [GAMEREL03-BP02 Implement loose coupling of game features to
  handle failures with minimal impact to player experience](gamerel03-bp02.md "gamerel03-bp02.md")
- [GAMEREL03-BP03 Monitor infrastructure events over time to
  measure impact on player behavior](gamerel03-bp03.md "gamerel03-bp03.md")
