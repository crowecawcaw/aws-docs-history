

# Understanding resilience policies
<a name="next-gen-understanding-policies"></a>

Resilience policies define the resilience requirements for your application. Each policy specifies targets that Next generation Resilience Hub evaluates during failure mode assessments to determine whether your application meets your resilience goals.

Different stakeholders care about different aspects of resilience:
+ **Central SRE teams** focus on disaster recovery (RTO/RPO) and availability targets.
+ **Service teams** focus on operational performance (latency, error rates, throughput).
+ **Compliance teams** focus on data protection (RPO for data durability).

Modular policies let each stakeholder define their requirements independently, then apply them at the appropriate level of the application hierarchy.