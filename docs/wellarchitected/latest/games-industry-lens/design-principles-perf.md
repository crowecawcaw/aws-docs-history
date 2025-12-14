# Design principles

In addition to the design principles in the AWS Well-Architected
Framework whitepaper, the following design principles can achieve
performance efficiency for your games:

- **Measure game performance from
  end-to-end:** It is important to measure performance
  as it is perceived from the perspective of your players. This
  means you should measure the performance of the game client,
  your game infrastructure, and the internet connectivity that
  connects your players to the infrastructure. This will assist
  in understanding where you can make performance improvements
  within your architecture.
- **Optimize your architecture to improve
  metrics that reflect actual player experience:** As
  you adapt and evolve your architecture over time, think about
  how these improvements and changes will impact player
  experience. Games workloads should be able to withstand and
  minimize the impact of failures to block widespread
  disruptions to gameplay. Game features and systems that aren't
  critically dependent on each other should be de-coupled to
  reduce the blast radius of failures and isolate player
  impacting issues.
- **Use technologies that simplify game
  operations and increase development
  speed:** Prioritize the adoption of technologies that
  can improve developer efficiency. Operational overhead during
  pre-production stages of development can be a distraction from
  improving gameplay. By leveraging managed services from AWS or
  AWS Partners, engineering can be reduced, which enables game
  developers to focus on the core game loop and player
  experience. Architecture and performance requirements may
  change and evolve throughout the game development life cycle
  and technology trade-offs should be considered at each phase.
- **Design infrastructure to meet peak
  player concurrency and dynamically scale as needed:**
  Infrastructure should be designed to scale to meet player
  demand. Metrics, such as player session concurrency and number
  of logins, can be used to preemptively scale before systems
  become overloaded. Reactive system utilization metrics, such
  as CPU and memory consumption, can be used to scale after
  systems become overloaded. By dynamically scaling your
  infrastructure, you can reduce the costs of operating your
  game.
