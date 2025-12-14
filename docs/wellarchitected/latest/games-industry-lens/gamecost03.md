# Data transfer costs

| GAMECOST03: How are you optimizing the data transfer<br>costs for your game infrastructure? |
| ------------------------------------------------------------------------------------------- |
|                                                                                             |

Games can transfer a significant amount of data across the
internet between your players' game client devices and your game
infrastructure to provide the gameplay experience, as well as
between the components of your game infrastructure.

For example, data transfer occurs when players download game
content updates to their game clients, save their game progress
state to the cloud, engage in real-time multiplayer game
sessions with their friends, and when your game infrastructure
transfers data between Regions and Availability Zones. It is
important to understand where the data transfer occurs in your
game workload to optimize your architecture choices to reduce
this data transfer cost.

To optimize the data transfer costs for your game workload,
consider the following best practices:

###### Best practices

- [GAMECOST03-BP01 Choose the appropriate type of storage for user
  generated content to reduce costs](gamecost03-bp01.md "gamecost03-bp01.md")
- [GAMECOST03-BP02 Optimize databases for game backends](gamecost03-bp02.md "gamecost03-bp02.md")
