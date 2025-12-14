# Change management

| GAMEREL02: How do you scale your stateful games to<br>accommodate changes in demand? |
| ------------------------------------------------------------------------------------ |
|                                                                                      |

As your player demand fluctuates over time, your game
infrastructure should be able to adaptively scale to handle these
changing requirements. While it is difficult to predict the
popularity of a game ahead of time, design an architecture
approach that allows for addition and removal of infrastructure
capacity to accommodate fluctuations in player population.

###### Best practices

- [GAMEREL02-BP01 Implement a scaling strategy that incorporates
  the state of active player game sessions](gamerel02-bp01.md "gamerel02-bp01.md")
- [GAMEREL02-BP02 Support the use of multiple EC2 instance types
  for your game](gamerel02-bp02.md "gamerel02-bp02.md")
