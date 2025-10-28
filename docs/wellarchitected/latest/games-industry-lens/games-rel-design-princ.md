# Design principles

In addition to the design principles in the AWS Well-Architected Framework whitepaper,
the following are design principles that can help you increase reliability in the cloud
for games workloads:

**Agree on the peak player concurrency and system scalability
targets required to meet business projections:** Prior to launching a game and
during live game operations, develop estimates for the number of concurrent players
expected at peak, and to establish target goals for system scalability to meet these
projections. This helps create a baseline for your game’s reliability. Define scaling
policies to accommodate changes in demand automatically without impact availability, such
as by ensuring that your scaling systems gracefully manage active player sessions.

**Measure your reliability and the impact on player
experience:** Define key performance indicators (KPIs) that represent the
health of your game. Monitor the impact of changes in infrastructure and game features on
your reliability.
