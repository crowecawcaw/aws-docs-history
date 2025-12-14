# Design principles

The AWS Well-Architected Framework identifies the following general
design principles to facilitate good design in the cloud for games
workloads:

- **Understand player behavior and usage
  patterns to evolve the game and help protect players:**
  To drive improvement continually to your game and effectively
  manage the player experience, it is important to have visibility
  into how players interact with game itself and with the rest of
  the players. This assists you understand how to improve the
  game, manage costs, and monitor and react to unauthorized usage
  activity that poses risks to the player experience.
- **Use technologies that simplify game
  operations and increase development speed:** Prioritize
  the adoption of technologies that can improve speed and reduce
  the operational overhead of delivering new features and
  improvements to players. Games are hits-driven and there are
  many choices for players to consider, so moving quickly and
  adapting to change is critical for the success of a game.
  Consider whether you are comfortable operating your own software
  or if you would prefer adopting a comparable managed service
  from AWS, AWS Partners, or both.
- **Optimize your architecture to improve
  metrics that reflect actual player experience:** As you
  adapt and evolve your architecture over time, think about how
  these improvements and changes will impact player experience.
  Games workloads should be able to withstand and minimize the
  impact of failures to block widespread disruptions to gameplay.
  Game features and systems that aren't critically dependent on
  each other should be de-coupled to reduce the impact of failures
  and isolate player impacting issues.
- **Design infrastructure to meet peak
  player concurrency and dynamically scale as needed:**
  Infrastructure should be designed to scale to meet player
  demand. Metrics, such as player session concurrency and number
  of logins, can be used to preemptively scale before systems
  become overloaded. Reactive system utilization metrics, such as
  CPU and memory consumption, can be used to scale after systems
  become overloaded. By dynamically scaling your infrastructure,
  you can reduce the costs of operating your game.
- **Implement runbooks to improve game
  operations:** Operational runbooks should be used to
  consistently manage recurring game operations tasks. Runbooks
  should exist for common game operations workflows such as
  investigating and responding to player reports, managing
  infrastructure pre-scaling activities to prepare for anticipated
  large-scale events like new season launches and game content
  releases, and to address typical game maintenance activities.
