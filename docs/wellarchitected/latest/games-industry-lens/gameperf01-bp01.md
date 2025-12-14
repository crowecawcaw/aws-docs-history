# GAMEPERF01-BP01 Evaluate game server resource requirements and

scalability needs

Evaluate server requirements against your scalability needs to verify that you are selecting a hosting option that both meets your requirements and provides optimal performance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When selecting the appropriate hosting option for your game
servers, consider the following factors:

**Game server resource
requirements**

Assess the CPU, memory, network, and storage requirements of your
game server processes to determine what your game consumes.
Do not overlook networking; each frame requires CPU cycles to
receive player actions, update the state of the game, and send it
back to the player. Offloading packet processing can free up CPU
for core game functions. Networking is the foundation for smooth
and responsive game play so testing it early in the process
defines a baseline performance profile for a game.

A first person shooter game might have high actions per second
which the CPU needs to quickly move off to the network which may
favor compute optimized C family instances, while a turn-based
strategy game which can spend more CPU cycles processing per turn
may need increased memory from R family instances to locally store
and update the state of the game on the server before sending it
back to players. Use a data-driven approach like
[the
Utilization Saturation and Errors (USE) Method](https://www.brendangregg.com/usemethod.html "https://www.brendangregg.com/usemethod.html") to make well
informed architectural choices.

**Scalability and elasticity**

Evaluate how quickly and smoothly each hosting option can scale to
meet player demand without compromising performance. Consider the
level of automation and flexibility required for your game's
workload to maintain a smooth gaming experience during peak times.
A game server might scale quickly by increasing utilization
through adding additional game server processes on the same
instance, where a game backend may scale slower based on the
rising active user count and games being played. Your fleet should
scale with demand to minimize cost while facilitating minimal wait
time for the players to get into game. Review Amazon EC2 Spot
Instance Advisor to gain insight into cost effective available
capacity for game server fleets.

### Implementation steps

- Evaluate game server resource requirements for CPU, memory,
  network, and storage to select suitable instance types,
  considering game-specific performance needs such as high
  network throughput for FPS games or memory optimization for
  turn-based strategy games.
- Compare different hosting options such as containers,
  instances, bare-metal, and managed services by analyzing
  performance data using frameworks like the USE method. Use
  these insights to make better decisions about your system
  architecture.
- Design fleets for scalability and elasticity, leveraging
  tools like EC2 Spot Instance Advisor to optimize costs while
  facilitating quick scaling to meet player demand during peak
  times.
