# AGENTREL02-BP04 Develop clear instruction protocols for agents

Ad-hoc prompts interpreted slightly differently by each model call
produce unpredictable behavior, and the problem multiplies in
multi-agent workflows. Standardized instruction templates, versioned
prompts, and explicit handoff schemas reduce ambiguity and make
regressions traceable to a specific version.

**Desired outcome:**

- You have a canonical system prompt template that every agent
  follows, covering role, capabilities, constraints, output
  format, and escalation behavior.
- You version prompt templates centrally and log the version used
  on every invocation.
- You have explicit handoff schemas for multi-agent delegation so
  receiving agents get unambiguous instructions.

**Common anti-patterns:**

- Running ad-hoc prompting without standardized formats, producing
  inconsistent interpretation of objectives across agents.
- Omitting explicit handoff procedures for multi-agent
  orchestration, leaving downstream agents to guess their role.
- Skipping prompt versioning, so rolling back a problematic change
  requires archaeology rather than a configuration flip.

**Benefits of establishing this best
practice:**

- Predictable behavior through standardized instruction formats
  that reduce ambiguity.
- Reliable multi-agent orchestration through explicit handoff
  procedures and context preservation.
- Faster debugging and refinement through consistent patterns you
  can test systematically.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Define one structure that every system prompt follows. This
structure should cover role definition, capability description,
constraint specification, output format requirements, and
escalation behavior. Make the template the starting point for any
new agent. When every agent inherits the same structure, reviewers
can check the important parts at a glance and regressions are more
visible because the diffs are small.

Template storage is where versioning happens. Store prompts in a
versioned configuration store so changes don't require
redeployment. Assign version identifiers to every template and log
the version used in every invocation through
[Amazon
Bedrock model invocation logging](../../../bedrock/latest/userguide/model-invocation-logging.md "../../../bedrock/latest/userguide/model-invocation-logging.md"). When a regression
appears, the version ID on the failing trace tells you exactly
which template is to blame.

Handoffs need their own schema. For multi-agent orchestration, an
explicit handoff message should carry the task identifier, task
type, message body, execution context, deadline, and callback
mechanism. Use
[Amazon
Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md") to manage discovery and
invocation with well-defined interface contracts. Validate new
prompt versions offline using
[Amazon
Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") to compare agent behavior
before migration, and run contract tests in CI/CD including
adversarial cases designed to expose prompt injection
vulnerabilities.

### Implementation steps

1. **Define a canonical system prompt
   template:** Establish a common structure for role,
   capabilities, constraints, output format, and escalation
   behavior that every agent inherits.
2. **Store prompt templates in a
   versioned configuration store:** Centralize
   management so prompt updates don't require redeployment.
3. **Design explicit handoff message
   schemas:** Define a canonical handoff message
   format for multi-agent delegation with task identifiers,
   message bodies, and callback mechanisms.
4. **Use AgentCore Evaluations to compare
   prompt versions:** Run
   [Amazon
   Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md") on candidate versions
   before migrating production traffic.
5. **Run automated contract tests in
   CI/CD:** Include adversarial prompt injection
   detection so protocol regressions don't ship.

## Resources

**Related best practices:**

- [AGENTREL02-BP01 Design
  agents for specific and atomic tasks](agentrel02-bp01.md "agentrel02-bp01.md")
- [AGENTREL02-BP03
  Implement behavioral anomaly detection and monitoring](agentrel02-bp03.md "agentrel02-bp03.md")
- [AGENTREL02-BP05
  Establish tiered human oversight and approval workflows](agentrel02-bp05.md "agentrel02-bp05.md")

**Related documents:**

- [Amazon
  Bedrock AgentCore Evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md")
- [Build
  reliable AI agents with Amazon Bedrock AgentCore
  Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/ "https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/")
- [Amazon
  Bedrock AgentCore Gateway](../../../bedrock-agentcore/latest/devguide/gateway.md "../../../bedrock-agentcore/latest/devguide/gateway.md")
- [Amazon
  Bedrock model invocation logging](../../../bedrock/latest/userguide/model-invocation-logging.md "../../../bedrock/latest/userguide/model-invocation-logging.md")

**Related services:**

- [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/")
