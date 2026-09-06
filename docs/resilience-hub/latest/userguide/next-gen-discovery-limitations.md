

# Coverage and known limitations
<a name="next-gen-discovery-limitations"></a>

Dependency discovery covers all DNS queries made through Route 53 resolvers in your VPC, including both IPv4 and IPv6 queries, and queries from Amazon EC2, Amazon ECS, Amazon EKS, and VPC-connected Lambda. The following known limitations apply:


| Limitation | Impact | Workaround | 
| --- | --- | --- | 
| Non-VPC Lambda | Lambda functions without VPC connectivity are not covered | Connect Lambda functions to VPC | 
| Direct IP connections | Connections made by IP address (not DNS) are not discovered | No workaround | 
| Infrequent dependencies | Dependencies called less than once per hour may be missed in initial discovery | 35-day lookback catches most; very rare calls may not appear | 
| Kubernetes shared tenancy | Multi-tenant Amazon EKS clusters may attribute dependencies to the wrong service | Verify compute resource attribution is correctly mapping resources to services | 