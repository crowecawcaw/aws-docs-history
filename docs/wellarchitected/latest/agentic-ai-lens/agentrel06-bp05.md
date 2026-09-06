

# AGENTREL06-BP05 Implement dynamic capability toggling
<a name="agentrel06-bp05"></a>

 Taking an entire agent offline to fix one misbehaving feature is disproportionate. Feature flags at the gateway boundary let operators disable the affected capability immediately, keeping the rest of the agent usable while fixes or investigations proceed. 

 **Desired outcome:** 
+  You have capability toggles that disable specific tools or features without redeploying the agent. 
+  You have fallback behaviors defined for each capability so agents continue operating when a feature is disabled. 
+  You monitor toggle state and fallback usage so capabilities exhibiting silent degradation surface through elevated fallback rates. 

 **Common anti-patterns:** 
+  Requiring redeployment to disable problematic capabilities, extending time to remediation. 
+  Implementing toggles without fallback behaviors, so disabling a capability triggers agent failures rather than reduced functionality. 
+  Omitting user-facing communication when features are unavailable, leaving users confused about current capability. 

 **Benefits of establishing this best practice:** 
+  Capability-specific issues get remediated quickly without full agent redeployment. 
+  Overall agent functionality survives capability toggles through graceful fallbacks. 
+  New capabilities can be rolled out gradually and rolled back immediately when problems appear. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Gateway-level toggling is the control point. [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies can enable or disable specific tool access for agents without redeployment, providing immediate control over which capabilities are available. Policy updates propagate quickly, so the toggle can be flipped while an incident is still active rather than waiting for a deployment window. For more granular runtime toggling within agent logic, use a managed configuration service with local caching and configurable polling intervals so agents respond to changes within seconds. 

 Fallback behaviors are what make toggling safe. Define what the agent does when a capability is disabled. Examples include semantic search falling back to keyword search, complex reasoning falling back to simpler rules, and real-time data falling back to cached values. Document fallback behaviors alongside capability definitions so operators know the impact of flipping each toggle. Treat fallback paths as first-class code and test them alongside the primary implementations so they actually work when you need them. 

 Monitoring makes the system self-aware. Track capability toggle state and fallback usage through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). Alarms on fallback rates that exceed baseline signal capabilities experiencing issues even when not explicitly toggled off, giving operators early warning before users report problems. This turns the toggle mechanism from a manual lever into a proactive detection surface. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement capability toggling through AgentCore Policy:** Use Cedar policies in [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to control tool access at the gateway boundary. 

1.  **Define and implement fallback behaviors for each capability:** Document the reduced-capability behavior that activates when a toggle is flipped. 

1.  **Test fallback paths alongside primary implementations:** Validate that fallbacks produce acceptable results, not just that they don't error. 

1.  **Monitor toggle state and fallback usage:** Track both through [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). 

1.  **Configure alarms on elevated fallback rates:** Detect capabilities experiencing issues before users report them. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTREL06-BP01 Develop agent-based integrations with existing or legacy systems](agentrel06-bp01.html) 
+  [AGENTREL06-BP02 Establish fallback mechanisms for legacy system degradation](agentrel06-bp02.html) 
+  [AGENTREL06-BP04 Implement idempotent task execution patterns](agentrel06-bp04.html) 
+  [AGENTREL08-BP01 Establish consistent configuration management practices](agentrel08-bp01.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Secure AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 