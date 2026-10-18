

# Legacy system integration
<a name="agentrel06"></a>

 Agents that integrate with existing systems through adapter patterns and abstraction interfaces preserve legacy system stability while enabling automation of established workflows. These systems might not be optimized for agent interactions and might require support for protocols such as MCP or A2A. How do agents integrate effectively without impacting the reliability of established processes? 


|  AGENTREL06: How do agents integrate effectively with existing systems without impacting the reliability of established processes?  | 
| --- | 
|   | 

## Capability intent
<a name="capability-intent-5"></a>
+  Legacy systems are reached through adapter interfaces that expose agent-native tool contracts, so agents don't need to understand the protocols behind them. 
+  Legacy systems are protected from agent-native invocation patterns through rate limiting and access control applied at the adapter layer. 
+  Every legacy dependency has a defined fallback path, so legacy outages cause reduced capability rather than complete agent failure. 
+  Agent operations with side effects are idempotent, so retry-based recovery is safe and doesn't produce duplicate transactions or inconsistent state. 
+  Operators can disable and re-enable individual capabilities at runtime without redeployment, and each capability has a tested fallback behavior that activates when it is toggled off. 
+  Resilience mechanisms are exercised regularly through fault injection and game days, so gaps are discovered in testing rather than during production incidents. 

## Common issues to watch for
<a name="common-issues-to-watch-for-5"></a>
+  Agents couple directly to legacy interfaces without adapter layers, so legacy protocol changes ripple through agent code and every agent handles legacy error codes in its own way. 
+  Legacy dependencies are assumed to have the reliability of cloud-based services, so no fallback paths exist and a single legacy outage causes complete agent failure. 
+  Retries are applied without idempotency guarantees, so recovery from transient failures creates duplicate transactions, corrupted state, or silent inconsistency. 
+  Disabling a problematic capability requires code changes and redeployment, which extends time-to-remediation during incidents and discourages cutting off misbehaving features. 
+  Automatic cutoffs open on failure but never close after recovery because no probe re-enables access, leaving capability degraded long after the legacy system is healthy again. 
+  Resilience mechanisms are never exercised, so fallback paths, runbooks, and alerting are only tested for the first time during a real incident. 

**Topics**
+ [Capability intent](#capability-intent-5)
+ [Common issues to watch for](#common-issues-to-watch-for-5)
+ [AGENTREL06-BP01 Develop agent-based integrations with existing or legacy systems](agentrel06-bp01.md)
+ [AGENTREL06-BP02 Establish fallback mechanisms for legacy system degradation](agentrel06-bp02.md)
+ [AGENTREL06-BP03 Regularly test degraded system performance](agentrel06-bp03.md)
+ [AGENTREL06-BP04 Implement idempotent task execution patterns](agentrel06-bp04.md)
+ [AGENTREL06-BP05 Implement dynamic capability toggling](agentrel06-bp05.md)