

# Design principles
<a name="design-principles"></a>

The Agentic AI Lens is built on a set of design principles that reflect the unique characteristics of autonomous AI agents. These principles guide architectural decisions across all six pillars and provide a foundation for evaluating agentic AI system designs.
+ **Decompose agentic workloads into specialized, bounded agents:** Single-purpose agents with declared scope, explicit limits, and clear authority are easier to evaluate, secure, scale, evolve, and replace than monolithic ones. Decomposition is the foundation that every pillar's controls depend on.
+ **Make every agent action observable and traceable end-to-end:** Reasoning steps, tool calls, memory accesses, and inter-agent handoffs need a single trace fabric so the same telemetry can answer cost, latency, quality, security, and footprint questions. Observability of agentic behavior is qualitatively different from infrastructure monitoring.
+ **Treat agent behavior as code:** Prompts, tool catalogs, role definitions, model selections, and policies are versioned artifacts that go through peer review, testing, staged rollout, and rollback alongside the rest of the codebase.
+ **Pair autonomy with proportionate human oversight:** Define autonomy levels (observer, assistant, autonomous, orchestrator) and escalation paths up front. Human review depth scales with the consequence of the action, by design rather than by reaction.
+ **Ground autonomous behavior in explicit contracts:** Schemas, registries, structured success criteria, and confidence signals replace implicit assumptions about what an agent will do. What used to live inside a prompt becomes an enforceable interface.