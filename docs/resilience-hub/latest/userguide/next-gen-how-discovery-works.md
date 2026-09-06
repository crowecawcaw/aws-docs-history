

# How dependency discovery works
<a name="next-gen-how-discovery-works"></a>

Dependency discovery analyzes Route 53 DNS resolver query logs to identify every domain name that your service's compute resources resolve. This reveals the full set of external dependencies without requiring any agents, code changes, or instrumentation.


| Feature | Detail | 
| --- | --- | 
| Lookback window | 35 days of historical DNS query data | 
| Continuous monitoring | Ongoing discovery summarized by hour | 
| Supported dependency types | AWS services, internal endpoints, third-party endpoints | 
| Attribution | Dependencies are attributed to specific compute resources within your service | 
| Setup | No agents or code changes required – enable in minutes | 