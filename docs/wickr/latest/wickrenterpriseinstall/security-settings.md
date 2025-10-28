This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Security settings

AWS Wickr Enterprise provides configuration settings to enforce an enhanced security
context for your deployment. This higher security standard is applied at the pod and container
level, and is required for compliance with the Security Technical Implementation Guide
(STIG).

Set the following configuration parameters to enforce the enhanced security context:

```
podSecurityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
containerSecurityContext:
  allowPrivilegeEscalation: false
  capabilities:
    drop: ["ALL"]
```

###### Warning

For Opensearch, this security configuration disables the `fsgroup-volume`
initContainer that updates permissions on the persistent storage, which can cause compatibility
issues related to permissions.
