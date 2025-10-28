# REL 4. How do you design interactions in a distributed system to prevent

failures?

Distributed systems rely on communications networks to interconnect components, such as servers or services. Your workload must operate reliably despite data loss or latency in these networks. Components of the distributed system must operate in a way that does not negatively impact other components or the workload. These best practices prevent failures and improve mean time between failures (MTBF).

###### Best practices

- [REL04-BP01 Identify the kind of distributed systems you depend
  on](rel_prevent_interaction_failure_identify.md "rel_prevent_interaction_failure_identify.md")
- [REL04-BP02 Implement loosely coupled dependencies](rel_prevent_interaction_failure_loosely_coupled_system.md "rel_prevent_interaction_failure_loosely_coupled_system.md")
- [REL04-BP03 Do constant work](rel_prevent_interaction_failure_constant_work.md "rel_prevent_interaction_failure_constant_work.md")
- [REL04-BP04 Make mutating operations idempotent](rel_prevent_interaction_failure_idempotent.md "rel_prevent_interaction_failure_idempotent.md")
