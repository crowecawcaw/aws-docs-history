

# Coverage and known limitations

Dependency discovery covers all DNS queries made through Route 53 resolvers in your VPC, including both IPv4 and IPv6 queries, from Amazon EC2, Amazon ECS, Amazon EKS, and Lambda functions connected to a VPC. It also covers Lambda functions that aren't connected to a VPC, in every Region where dependency discovery is available.

For Lambda functions connected to a VPC, dependency discovery attributes queries based on the Region. In the following Regions, it attributes the queries of supported functions to the services that include the function. Support can vary between functions in the same VPC:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Asia Pacific (Tokyo)
+ Asia Pacific (Seoul)
+ Asia Pacific (Sydney)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (Milan)
+ South America (São Paulo)

In these Regions, dependency discovery attributes the queries of unsupported functions to their VPC. In other Regions, it attributes the queries of every function connected to a VPC to its VPC. These queries appear on every service that includes that VPC.

The following table lists known limitations of dependency discovery and their workarounds.


| Limitation | Impact | Workaround | 
| --- | --- | --- | 
| Lambda history | Lambda function dependencies are discovered from the time Lambda support became available in your Region, or from the time you enable dependency discovery, whichever is later. The 35-day lookback doesn't include earlier Lambda queries. | No workaround is available. | 
| Lambda functions connected to a VPC | In the Regions listed above, dependency discovery attributes the queries of some functions connected to a VPC to their VPC. In other Regions, it does this for every function connected to a VPC. These dependencies appear on every service that includes the VPC. | Include the VPC only in services that use it | 
| Lambda functions with custom DNS | Dependency discovery doesn't cover queries from a Lambda function if its code sends them directly to a DNS server's IP address, or if its VPC's DHCP options set lists DNS servers other than the Amazon-provided DNS server | Use the Amazon-provided DNS server. Route 53 Resolver forwarding rules are supported. | 
| Direct IP connections | Connections made by IP address (not DNS) are not discovered | No workaround is available. | 
| Infrequent dependencies | Dependencies called less than once per hour may be missed in initial discovery | 35-day lookback catches most; very rare calls may not appear | 
| Kubernetes shared tenancy | Multi-tenant Amazon EKS clusters may attribute dependencies to the wrong service | Verify compute resource attribution is correctly mapping resources to services | 