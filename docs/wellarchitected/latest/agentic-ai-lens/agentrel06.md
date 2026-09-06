

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

## Maturity levels
<a name="maturity-levels-5"></a>

 These levels summarize what each stage of maturity looks like for legacy system integration as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Agents call legacy systems directly without adapter layers, so legacy error codes and protocol quirks leak into agent logic. There are no explicit fallbacks, so legacy outages cascade into complete agent failure. Retries are applied without idempotency, which can produce duplicate transactions, and disabling a problematic capability requires redeployment. Resilience is assumed rather than tested.  | 
|  2  |  Emerging  |  Integration adapters are introduced for the most critical legacy systems, exposing tool interfaces that translate to legacy protocols internally. One-time fallbacks are added after the first outages reveal the need, and retries start using idempotency keys for a small set of high-risk operations. Teams occasionally run manual failure tests before major releases. Telemetry on adapter health is partial and varies by system.  | 
|  3  |  Defined  |  Adapters are registered in [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) with a canonical error taxonomy, so agents handle legacy failures consistently. Each legacy dependency has a matched fallback strategy: cache-based for reference data, queue-based for transactional operations through [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html), and graceful degradation for real-time data. Idempotency is implemented through [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) conditional writes and TTL-based expiration, and capability toggling through [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies allows runtime control. [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) experiments run on a defined schedule.  | 
|  4  |  Proactive  |  Legacy integration health is monitored through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with alarms that trigger automatic cutoffs using [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) circuit breaker logic, and recovery probes re-enable access when systems recover. Idempotency keys propagate through multi-step workflows and are passed to external systems that support native idempotency. Fallback behaviors are tested alongside primary implementations, and fallback activation rates feed a continuous prioritization of legacy reliability investment. FIS experiments are part of CI/CD, and quarterly game days validate runbooks under realistic conditions.  | 
|  5  |  Optimized  |  Adapter patterns, fallback strategies, and idempotency mechanisms are standardized across the organization and continuously refined based on operational data. Capability toggles, fallback activation rates, and legacy health trends are integrated into decision-making for legacy modernization investment. Self-healing behavior (automatic cutoff, graceful degradation, and recovery) is the default, and game days rehearse multi-system failures rather than single-service outages. The organization publishes internal patterns for agent-to-legacy integration and shares benchmarks across teams.  | 

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
+ [Maturity levels](#maturity-levels-5)
+ [Common issues to watch for](#common-issues-to-watch-for-5)
+ [AGENTREL06-BP01 Develop agent-based integrations with existing or legacy systems](agentrel06-bp01.md)
+ [AGENTREL06-BP02 Establish fallback mechanisms for legacy system degradation](agentrel06-bp02.md)
+ [AGENTREL06-BP03 Regularly test degraded system performance](agentrel06-bp03.md)
+ [AGENTREL06-BP04 Implement idempotent task execution patterns](agentrel06-bp04.md)
+ [AGENTREL06-BP05 Implement dynamic capability toggling](agentrel06-bp05.md)