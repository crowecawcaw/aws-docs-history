

# Kubernetes attribution gaps
<a name="next-gen-troubleshoot-k8s-attribution"></a>

**Symptom:** Dependencies are discovered but attributed to the wrong service in a shared EKS cluster.

**Cause:** When multiple services share an EKS cluster, DNS queries are attributed at the node level, not the pod level.

**Solution:** Enhanced pod-level attribution is planned for a future release. Currently, review dependencies manually for shared clusters.