

# Agent Versioning
<a name="ap-agent-versioning"></a>

Every Finding carries `agent_version` — the exact semver of the agent module that produced it. Because Findings update in place, `audit_trail[]` records the version that wrote each update. If the reasoning improves after a rollback, the audit trail shows which version contributed which update.

Versioning does not prevent a flawed Finding from reaching an owner. It enables post-hoc identification of affected Findings, targeted re-runs of corrected reasoning, and owner communication where warranted.