**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Comparing EKS Capability for kro to self-managed kro

The EKS Capability for kro provides the same functionality as self-managed kro, but with significant operational advantages.
For a general comparison of EKS Capabilities vs self-managed solutions, see [EKS Capabilities considerations](capabilities-considerations.md "capabilities-considerations.md").

The EKS Capability for kro uses the same upstream kro controllers and is fully compatible with upstream kro.
ResourceGraphDefinitions, CEL expressions, and resource composition work identically.
For complete kro documentation and examples, see the [kro documentation](https://kro.run/docs/overview "https://kro.run/docs/overview").

## Migration path

You can migrate from self-managed kro to the managed capability with zero downtime.

###### Important

Before migrating, ensure your self-managed kro controller is running the same version as the EKS Capability for kro.
Check the capability version in the EKS console or using `aws eks describe-capability`, then upgrade your self-managed installation to match.
This prevents compatibility issues during the migration.

1. Update your self-managed kro controller to use `kube-system` for leader election leases:

```
helm upgrade --install kro \
  oci://ghcr.io/awslabs/kro/kro-chart \
  --namespace kro \
  --set leaderElection.namespace=kube-system
```

This moves the controller’s lease to `kube-system`, allowing the managed capability to coordinate with it. 2. Create the kro capability on your cluster (see [Create a kro capability](create-kro-capability.md "create-kro-capability.md")) 3. The managed capability recognizes existing ResourceGraphDefinitions and instances, taking over reconciliation 4. Gradually scale down or remove self-managed kro deployments:

```
helm uninstall kro --namespace kro
```

This approach allows both controllers to coexist safely during migration.
The managed capability automatically adopts ResourceGraphDefinitions and instances previously managed by self-managed kro, ensuring continuous reconciliation without conflicts.

## Next steps

- [Create a kro capability](create-kro-capability.md "create-kro-capability.md") - Create a kro capability resource
- [kro concepts](kro-concepts.md "kro-concepts.md") - Understand kro concepts and resource composition
