

# Design interactions in a distributed system to prevent failures

 Distributed systems connect components over networks that lose packets, add latency, and partition without warning. A workload has to keep working when a dependency slows down, returns an error, or delivers the same message twice. The way components talk to each other decides whether one component's trouble stays contained or spreads across the workload, so the interaction design is where reliability is won or lost. 

 This capability covers how an organization designs the interactions between the components of a distributed system to prevent failures: classifying each dependency by its communication style, decoupling components through published interfaces and durable intermediaries, designing control systems to perform a constant amount of work, and making mutating operations idempotent so retries and duplicate delivery do not corrupt state. 


|  REL04: How do you design interactions in a distributed system to prevent failures?  | 
| --- | 
|  [REL04-BP01 Identify the kind of distributed systems you depend on](rel04-bp01.md)  | 
|  [REL04-BP02 Implement loosely coupled dependencies](rel04-bp02.md)  | 
|  [REL04-BP03 Do constant work](rel04-bp03.md)  | 
|  [REL04-BP04 Make mutating operations idempotent](rel04-bp04.md)  | 

## Capability intent
<a name="rel04-intent"></a>
+  Every dependency is classified as synchronous, asynchronous, or batch, and its error handling, timeouts, and retries match that style. 
+  Components interact through published interfaces or durable intermediaries, so a failure in one component stays contained at a single boundary. 
+  Synchronous calls have explicit timeouts and fail fast, rather than waiting indefinitely or chaining the availability of several dependencies. 
+  Critical control systems perform a constant amount of work, so a large, rapid change in demand or failures does not create a matching spike in load. 
+  Mutating operations are idempotent, so clients can retry and consumers can absorb duplicate delivery without producing duplicate side effects. 

## Common issues to watch for
<a name="rel04-issues"></a>
+  A workload waits indefinitely for a dependency response, so clients time out without knowing whether the request was received. 
+  Teams chain synchronous dependencies, so every system in the path must be available for a single request to succeed. 
+  Teams assume exactly-once delivery, so duplicate messages create duplicate records, double charges, or other unintended side effects. 
+  Components share a database or make direct point-to-point calls, which reintroduces tight coupling and blocks independent scaling. 
+  A control system scales its work with the number of failures, so it is overwhelmed exactly when many components fail at once. 
+  Batch jobs run without a scheduler, which allows concurrent runs of the same job to corrupt output. 