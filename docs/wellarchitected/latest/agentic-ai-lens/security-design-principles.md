

# Design principles
<a name="security-design-principles"></a>

In addition to the lens-level design principles, the security best practices in this lens are represented by at least one of the following principles:
+ **Treat every input as untrusted and every output as potentially harmful:** Multi-layer validation, prompt injection defenses, and output filtering apply to user inputs, memory reads, tool I/O, and agent-to-agent messages alike. The agent itself is not a trust boundary.
+ **Give each agent its own identity and the minimum privileges to do its job:** Per-agent authentication, dynamic permission boundaries, and scoped credentials per session limit what any single agent or compromised session can reach.
+ **Partition memory, tools, and channels along trust boundaries:** Sessions, users, tenants, and agents get separate namespaces, integrity checks on stored state, and authenticated and encrypted communication so contamination cannot move laterally.
+ **Layer guardrails between intent and action:** Pre-execution input filters, runtime alignment controls, and post-execution output filters keep agent behavior aligned even when prompts or contexts are adversarial. Critical actions stay gated behind human approval.
+ **Continuously test the security posture:** AI-aware vulnerability scanning, multi-agent red-team simulations, and runtime threat detection run as part of the lifecycle, not as one-time exercises.