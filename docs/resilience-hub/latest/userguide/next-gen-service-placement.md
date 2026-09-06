

# Service placement: same account vs. different account
<a name="next-gen-service-placement"></a>

**Same account as system (simple):** The system and service are in the same AWS account. A single invoker role covers everything. This approach is best for small teams and single-account workloads.

**Different account than system (enterprise):** The system is in a central account and services are in spoke accounts. This approach requires cross-account roles or AWS Organizations. It is best for large organizations with distributed ownership.