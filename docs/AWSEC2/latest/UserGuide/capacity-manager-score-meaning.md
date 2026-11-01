

# What the scores mean
<a name="capacity-manager-score-meaning"></a>

Each score is a ratio of how much capacity an instance type and Availability Zone combination holds right now against the amount you asked for. Scores reflect capacity at a single point in time, and no score — including High — guarantees that a launch will succeed.
+ **High** — The combination holds several times your request. Proceed.
+ **Medium** — The combination can cover your request with little to spare. Treat it as workable rather than safe. A launch can still fail.
+ **Low** — The combination holds less than you asked for, though some capacity is likely still available.

Because every score is relative to your ask, the same instance type and Availability Zone combination can score differently for different amounts: asking for 50 instances might score High where asking for 5,000 scores Low, for the same combination at the same moment.

Low per-combination scores with a High aggregate is the system working as intended, not a contradiction. It means no single instance type and Availability Zone combination can carry your request, but your options together can — the case for staying flexible rather than committing to one combination.

**Important**  
Treat scores as guidance, not commitments, because Amazon EC2 capacity is dynamic and demand changes. Even at High, insufficient capacity errors remain possible. For critical workloads, use Capacity Reservations or Future-dated Capacity Reservations for capacity assurance, regardless of score.