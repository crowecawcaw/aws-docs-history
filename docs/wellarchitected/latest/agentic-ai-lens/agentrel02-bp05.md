# AGENTREL02-BP05 Establish tiered human oversight and approval workflows

Uniform oversight either slows every routine action to a crawl or
lets a high-consequence decision slip through unchecked. Tiering
review to match the risk and reversibility of each action balances
throughput with appropriate governance.

**Desired outcome:**

- You have agent actions classified into tiers (autonomous,
  notify, and approve) based on impact and reversibility.
- You have a first-pass automated review layer that filters
  policy-violating actions before human reviewers see them.
- You log every oversight decision with reviewer identity,
  rationale, and timestamp for compliance and governance
  reporting.

**Common anti-patterns:**

- Applying uniform oversight regardless of risk, creating
  bottlenecks for routine tasks or letting high-consequence
  actions slip through unchecked.
- Skipping clear escalation criteria, so some high-risk actions
  proceed autonomously while some low-risk actions queue for
  review.
- Running approval workflows without timeouts or fallback, causing
  agents to stall indefinitely when reviewers are unavailable.

**Benefits of establishing this best
practice:**

- Appropriate governance for high-consequence actions without
  bottlenecks on routine work.
- Reduced risk from LLM stochasticity because irreversible or
  high-stakes decisions get human review.
- An audit trail for compliance through structured logging of
  oversight decisions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Risk classification is the first design choice. Categorize agent
actions into three tiers. Autonomous actions are low-risk and
reversible. Notify actions are medium-risk and proceed with
operator awareness. Approve actions are high-risk or irreversible
and require explicit human approval. Encode the classification as
Cedar policies through
[Amazon
Bedrock AgentCore Policy](../../../bedrock-agentcore/latest/devguide/policy.md "../../../bedrock-agentcore/latest/devguide/policy.md"), so tier enforcement happens at
the gateway boundary before the agent can execute. Policy-based
enforcement applies the classification at runtime rather than
relying on reference documentation alone.

Automated first-pass review reduces the load on human reviewers.
[Amazon
Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") intercepts agent outputs before they
reach reviewers, filtering content that violates predefined
policies. What reaches the human queue should be the genuinely
ambiguous cases, with policy violations filtered automatically.

Approval workflows need structure, not just a pause. A structured
review request should include the action description, the agent's
reasoning, an impact assessment, and the execution history so the
reviewer can decide quickly. Configure timeouts that escalate to
secondary reviewers or fall back to safe defaults when primary
reviewers are unavailable so the system handles reviewer
unavailability without blocking indefinitely. Log every decision
with reviewer identity, rationale, and timestamp, and monitor
approval queue depth through Amazon CloudWatch to detect when
reviews are accumulating. Development tools like
[Kiro](https://kiro.dev/autonomous-agent/ "https://kiro.dev/autonomous-agent/")
implement this progressive autonomy pattern directly. Supervised
mode reviews each action before it is applied, while autopilot
mode grants full autonomy for trusted workflows. The two modes
mirror the tiered oversight model at the development layer.

### Implementation steps

1. **Define a risk classification
   framework:** Categorize agent actions into
   autonomous, notify, and approve tiers based on impact and
   reversibility, and encode the classification as Cedar
   policies through
   [Amazon
   Bedrock AgentCore Policy](../../../bedrock-agentcore/latest/devguide/policy.md "../../../bedrock-agentcore/latest/devguide/policy.md").
2. **Configure Amazon Bedrock Guardrails
   as the automated first-pass layer:** Use
   [Amazon
   Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md") to filter policy-violating actions
   before human escalation.
3. **Build structured approval
   workflows:** Pause execution and route review
   requests to reviewers. Each request should include the
   action description, agent reasoning, impact assessment, and
   execution history.
4. **Configure timeouts and escalation
   paths:** Handle reviewer unavailability without
   blocking indefinitely, with escalation to secondary
   reviewers or safe default fallbacks.
5. **Log every oversight
   decision:** Capture reviewer identity, rationale,
   and timestamp so the audit trail supports compliance and
   governance reporting.

## Resources

**Related best practices:**

- [AGENTREL02-BP03
  Implement behavioral anomaly detection and monitoring](agentrel02-bp03.md "agentrel02-bp03.md")
- [AGENTREL02-BP04 Develop
  clear instruction protocols for agents](agentrel02-bp04.md "agentrel02-bp04.md")
- [AGENTSEC04-BP02
  Human-in-the-loop for critical decisions](agentsec04-bp02.md "agentsec04-bp02.md")
- [AGENTSUS03-BP01
  Maintain organizational skills and competencies](agentsus03-bp01.md "agentsus03-bp01.md")

**Related documents:**

- [Amazon
  Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md")
- [Human-in-the-loop
  (HITL) - Amazon Nova Act](../../../nova-act/latest/userguide/hitl.md "../../../nova-act/latest/userguide/hitl.md")
- [Amazon
  Bedrock AgentCore Policy](../../../bedrock-agentcore/latest/devguide/policy.md "../../../bedrock-agentcore/latest/devguide/policy.md")
- [Evaluating
  AI agents: Real-world lessons from building agentic systems at
  Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/ "https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/")

**Related tools:**

- [Kiro
  Autonomous Agent](https://kiro.dev/autonomous-agent/ "https://kiro.dev/autonomous-agent/")

**Related services:**

- [Amazon
  Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
