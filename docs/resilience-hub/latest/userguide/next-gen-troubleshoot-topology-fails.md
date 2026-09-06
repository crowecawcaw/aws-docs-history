

# Resources discovered but topology generation fails
<a name="next-gen-troubleshoot-topology-fails"></a>

**Symptom:** Resources appear in the list but topology shows no connections.

**Solutions:**
+ Verify the invoker role has `ReadOnlyAccess` (required for topology queries).
+ Check that resources are in a VPC (topology generation maps VPC-based connections).
+ For EKS resources, verify Kubernetes RBAC is configured.