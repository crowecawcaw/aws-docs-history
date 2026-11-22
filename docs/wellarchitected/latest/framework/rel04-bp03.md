

# REL04-BP03 Do constant work

 Systems can fail when load changes suddenly and by a large amount. A constant-work design performs the same amount of work regardless of conditions. A surge in failures or demand does not create a matching surge in the system's work. Because the system behaves the same in normal and failure modes, large and rapid changes do not threaten its stability. 

 **Desired outcome:** 
+  Your critical control systems perform a constant amount of work regardless of how many items succeed or fail. 
+  Your payloads are fixed in size and independent of the current success or failure count. 
+  Your systems behave the same under normal and failure conditions and do not spike in load when state changes sharply. 

 **Common anti-patterns:** 
+  A health check system scales its work with the number of failures, so it is overwhelmed exactly when many components fail at once. 
+  Teams design control systems that emit updates only on change, which produces a flood of updates during a large-scale event. 
+  A system does little work in the normal case and far more work during failure, which is bimodal behavior. 
+  Payload size grows with the number of monitored resources or with the number of state changes. 

 **Benefits of establishing this best practice:** 
+  Control systems stay stable during large-scale failure events because their workload does not spike. 
+  Capacity planning is simpler because the system's load is predictable and flat. 
+  The failure-mode path is already exercised during normal operation, so there are no untested surge behaviors. 
+  Rapid, large changes in the monitored population do not threaten the system that observes them. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Many control systems perform work proportional to change. A health checker that sends a notification for each server that changes state does not do much when the failure rate is low. During a large-scale event, when half the fleet changes state at once, that same design must suddenly do far more work, when the rest of the system is already under stress. This pattern is called *bimodal behavior*. 

 Constant work removes the coupling between change and load. Instead of emitting deltas, the system processes a full snapshot of current state on a fixed cadence, whether or not anything changed. Consider a system that monitors 100,000 servers. If it represents each server's health as a single bit, a full snapshot is a 12.5 KB payload. That payload is the same size whether zero servers or all of them are unhealthy. The work is flat. A large, rapid change is no longer a threat because it does not change how much the system does. Amazon Route 53 applies this pattern to endpoint health checks, which routes traffic reliably even when many endpoints change state together. 

 Constant work spends resources continuously, including when little is happening, so at low scale it can look wasteful compared to change-driven approaches. You pay a steady, predictable cost to remove an unpredictable spike. That trade is worth making for control-plane and critical-path systems whose failure would amplify an incident. It is less compelling for systems where load and failure rate are already decoupled. Constant work also pairs naturally with static stability, where a system holds a known-good state rather than reacting to every change. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Find load that scales with failure:** Identify control systems whose work grows with the number of failures or state changes, such as health checkers, configuration propagators, and notification systems. These are the systems where a large event produces a work spike. 

1.  **Send full-state snapshots of fixed size:** Replace delta or change-based updates with a full snapshot that is the same size every cycle, and represent state as compactly as possible. For 100,000 monitored servers, one bit per server keeps the payload at 12.5 KB whether none or all are unhealthy. 

1.  **Process on a fixed cadence:** Run and publish on a steady interval that does not depend on how much has changed, so the system does the same work during quiet and busy periods. 

1.  **Buffer output through a durable intermediary:** Place a queue, stream, or durable store between the producer and its consumers so the constant-work output is decoupled from consumer availability. See REL04-BP02 for loosely coupled patterns. 

1.  **Test under large-scale change:** Exercise the system by flipping a large fraction of state at once, and confirm the work performed and the payload size stay constant. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL11-BP05 Use static stability to prevent bimodal behavior](rel11-bp05.md) 
+  [REL04-BP02 Implement loosely coupled dependencies](rel04-bp02.md) 
+  [REL04-BP04 Make mutating operations idempotent](rel04-bp04.md) 

 **Related documents:** 
+  [The Amazon Builders' Library: Reliability, constant work, and a good cup of coffee](https://builder.aws.com/content/3F05oqNtNUWxHJ5r6L6I2HrH4rI/reliability-constant-work-and-a-good-cup-of-coffee) 
+  [The Amazon Builders' Library: Challenges with distributed systems](https://builder.aws.com/content/3F08f7GPFiZMCgXD8gny6OjxR0Z/challenges-with-distributed-systems) 