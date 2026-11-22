

# Design interactions in a distributed system to mitigate or withstand failures

 Distributed systems connect their components over networks, and networks lose packets, add latency, and fail in ways a single machine never does. A component that assumes every call succeeds passes its own failure on to everything that depends on it, and a small impairment spreads outward until the whole workload is affected. Designing each interaction to expect failure is what keeps one struggling dependency from taking the rest of the system down with it. 

 This capability covers how an organization designs the interactions between distributed components to withstand and recover from failure: degrading gracefully when a dependency is unhealthy, throttling requests to protect capacity, controlling retries and timeouts so clients do not deepen an impairment, failing fast and managing queue backlogs, removing local state so nodes stay interchangeable, and preparing emergency levers that shed non-critical load during an incident. The result is a lower mean time to recovery and a higher mean time between failures. 


|  REL05: How do you design interactions in a distributed system to mitigate or withstand failures?  | 
| --- | 
|  [REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies](rel05-bp01.md)  | 
|  [REL05-BP02 Throttle requests](rel05-bp02.md)  | 
|  [REL05-BP03 Control and limit retry calls](rel05-bp03.md)  | 
|  [REL05-BP04 Fail fast and limit queues](rel05-bp04.md)  | 
|  [REL05-BP05 Set client timeouts](rel05-bp05.md)  | 
|  [REL05-BP06 Make systems stateless where possible](rel05-bp06.md)  | 
|  [REL05-BP07 Implement emergency levers](rel05-bp07.md)  | 

## Capability intent
<a name="rel05-intent"></a>
+  Every component keeps delivering its core function when a dependency is unhealthy, returning a reduced but predictable response rather than an error. 
+  Requests above tested capacity are throttled, and per-client rate limits contain a single noisy consumer, so a spike does not exhaust shared resources. 
+  Retries use exponential backoff with jitter and a bounded attempt limit, and calls across a process boundary carry explicit connection and request timeouts. 
+  Services fail fast under contention and manage queue backlogs, so they process relevant work rather than stale requests. 
+  Compute nodes hold no local session state, so any node can serve any request and the fleet scales and replaces nodes without an availability impact. 
+  Pre-tested emergency levers let responders shed non-critical function or absorb a demand spike while critical functions keep running. 

## Common issues to watch for
<a name="rel05-issues"></a>
+  A component returns an error on any dependency failure, even when partial results would still serve the customer, so losing one enhancement fails the entire response. 
+  Retries run without backoff, jitter, or an attempt cap, and at several layers at once, turning a brief impairment into a self-sustaining retry storm. 
+  Calls cross a process boundary with no timeout or a framework default, so a slow dependency holds threads and connections until the caller is exhausted too. 
+  Queues have no dead letter queue, no alarm on message age, and no backlog strategy, so consumers fall behind and spend capacity on requests clients already abandoned. 
+  Session data lives on the node that handled the first request, which forces sticky sessions and blocks horizontal scaling and node replacement. 
+  Emergency levers are designed but never exercised, so responders cannot trust them during a real incident. 