# Design interactions in a distributed system to mitigate or withstand failures

Distributed systems rely on communications networks to interconnect components (such as
servers or services). Your workload must operate reliably despite data loss or latency over
these networks. Components of the distributed system must operate in a way that does not
negatively impact other components or the workload. These best practices allow workloads to
withstand stresses or failures, more quickly recover from them, and mitigate the impact of
such impairments. The result is improved mean time to recovery (MTTR).

These best practices prevent failures and improve mean time
between failures (MTBF).

###### Best practices

- [REL05-BP01 Implement graceful degradation to transform
  applicable hard dependencies into soft dependencies](rel_mitigate_interaction_failure_graceful_degradation.md "rel_mitigate_interaction_failure_graceful_degradation.md")
- [REL05-BP02 Throttle requests](rel_mitigate_interaction_failure_throttle_requests.md "rel_mitigate_interaction_failure_throttle_requests.md")
- [REL05-BP03 Control and limit retry calls](rel_mitigate_interaction_failure_limit_retries.md "rel_mitigate_interaction_failure_limit_retries.md")
- [REL05-BP04 Fail fast and limit queues](rel_mitigate_interaction_failure_fail_fast.md "rel_mitigate_interaction_failure_fail_fast.md")
- [REL05-BP05 Set client timeouts](rel_mitigate_interaction_failure_client_timeouts.md "rel_mitigate_interaction_failure_client_timeouts.md")
- [REL05-BP06 Make systems stateless where possible](rel_mitigate_interaction_failure_stateless.md "rel_mitigate_interaction_failure_stateless.md")
- [REL05-BP07 Implement emergency levers](rel_mitigate_interaction_failure_emergency_levers.md "rel_mitigate_interaction_failure_emergency_levers.md")
