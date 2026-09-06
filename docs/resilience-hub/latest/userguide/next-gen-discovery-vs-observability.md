

# How dependency discovery differs from observability tools
<a name="next-gen-discovery-vs-observability"></a>

Dependency discovery focuses on **resilience validation** rather than operational observability:


| Capability | Observability tools (X-Ray, CloudWatch) | Next generation Resilience Hub dependency discovery | 
| --- | --- | --- | 
| Setup | Requires SDK instrumentation or agents | No agents or code changes – agentless | 
| Focus | Performance monitoring, latency debugging | Resilience validation, failure testing | 
| Discovery | Reactive – discovers failures during incidents | Proactive – discovers dependencies before incidents | 
| Classification | No criticality classification | Hard/soft classification | 
| Time to value | Days or weeks of instrumentation | Minutes to enable | 