

# Discovery not returning expected dependencies
<a name="next-gen-troubleshoot-missing-deps"></a>

**Symptom:** You enabled dependency discovery but don't see dependencies you know exist.

The following table lists possible causes and solutions.


| Cause | Solution | 
| --- | --- | 
| Dependency uses direct IP (not DNS) | Dependency discovery relies on DNS queries. Connections made by IP address are not discovered. Manually track IP-based dependencies. | 
| Compute resources not in a VPC | Non-VPC Lambda functions don't generate Route 53 resolver queries. Connect Lambda to a VPC or manually track dependencies. | 
| Dependency not called in 35-day window | Dependencies must have been called within the 35-day lookback period. Very infrequent calls may not appear. | 
| DNS resolution through non-Route 53 resolver | Custom DNS resolvers bypass Route 53 query logging. Ensure your VPC uses the default Route 53 resolver. | 