

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Comparing EKS Capability for ACK to self-managed ACK
<a name="ack-comparison"></a>

The EKS Capability for ACK provides the same functionality as self-managed ACK controllers, but with significant operational advantages. For a general comparison of EKS Capabilities vs self-managed solutions, see [EKS Capabilities considerations](capabilities-considerations.md). This topic focuses on ACK-specific differences.

## Differences from upstream ACK
<a name="_differences_from_upstream_ack"></a>

The EKS Capability for ACK is based on upstream ACK controllers but differs in IAM integration.

 **IAM Capability Role**: The capability uses a dedicated IAM role with a trust policy that allows the `capabilities.eks.amazonaws.com` service principal, not IRSA (IAM Roles for Service Accounts). You can attach IAM policies directly to the Capability Role with no need to create or annotate Kubernetes service accounts or configure OIDC providers. A best practice for production use cases is to configure service permissions using `IAMRoleSelector`. See [Configure ACK permissions](ack-permissions.md) for more details.

 **Session tags**: The managed capability automatically sets session tags on all AWS API requests, enabling fine-grained access control and auditing. Tags include `eks:eks-capability-arn`, `eks:kubernetes-namespace`, and `eks:kubernetes-api-group`. This differs from self-managed ACK, which does not set these tags by default. See [Configure ACK permissions](ack-permissions.md) for details on using session tags in IAM policies.

 **Resource tags**: The capability applies different default tags to AWS resources than self-managed ACK. The capability uses `eks:` prefixed tags (such as `eks:kubernetes-namespace`, `eks:eks-capability-arn`) instead of the `services.k8s.aws/` tags used by self-managed ACK. See [ACK considerations for EKS](ack-considerations.md) for the complete list of default resource tags.

 **Resource compatibility**: ACK custom resources work identically to upstream ACK with no changes to your ACK resource YAML files. The capability uses the same Kubernetes APIs and CRDs, so tools like `kubectl` work the same way. The capability supports only controllers and resources that are generally available (GA) in upstream ACK. The capability does not include controllers that are in preview upstream. A controller’s status can change from preview to GA upstream over time, and the capability can then begin managing it automatically. If you run a self-managed preview controller alongside the capability, review [Preview controllers and automatic promotion](#ack-preview-promotion) before you migrate.

For complete ACK documentation and service-specific guides, see the [ACK documentation](https://aws-controllers-k8s.github.io/docs/) on the ACK website.

## Migration path
<a name="ack-migration-path"></a>

You can migrate from self-managed ACK to the managed capability with minimal disruption to your AWS resources. There are two approaches:
+  [Coexist with self-managed controllers (recommended)](#ack-migration-coexist) - Create the capability with the services that you self-manage turned off, then migrate one service at a time. This is the recommended approach.
+  [Lease-based handover](#ack-migration-lease) - Create the capability with all services enabled, and use Kubernetes leader election to control when each handover happens.

**Important**  
Before you enable a service in the capability, grant the IAM Capability Role permissions that are equivalent to the permissions that your self-managed controller for that service uses today. The capability authenticates with a dedicated Capability Role through the `capabilities.eks.amazonaws.com` service principal, rather than through the mechanism your self-managed controllers use today, such as IRSA or EKS Pod Identity (see [Configure ACK permissions](ack-permissions.md)). If the Capability Role is missing permissions, the capability adopts your resources. It then fails to reconcile them and logs `AccessDenied` errors.  
With the recommended approach, you can grant these permissions one service at a time, because the capability doesn’t adopt resources of a service that is turned off. With the lease-based approach, grant them for every service before you create the capability.

When the capability adopts a resource, it applies its own default resource tags (`eks:` prefixed) in place of the `services.k8s.aws/` tags used by self-managed ACK (see [ACK considerations for EKS](ack-considerations.md)). Expect a one-time set of tagging API calls against your adopted resources, and update any cost-allocation or policy tooling that keys on the `services.k8s.aws/` tag prefix. This applies to both approaches.

### Coexist with self-managed controllers (recommended)
<a name="ack-migration-coexist"></a>

In this approach, you create the capability with `disabledServices` listing every ACK service that you currently run yourself. The capability doesn’t install custom resource definitions (CRDs) for those services and doesn’t run controllers for them, so it can’t contend with your self-managed controllers or adopt their resources. You then migrate one service at a time, on your own schedule, and you don’t need to change the leader election configuration of your self-managed controllers at all.

The steps use the S3 controller (`ack-s3-controller`) as an example.

1. Determine which ACK services you currently run self-managed.

1. Create the ACK capability with those services turned off (see [Create an ACK capability](create-ack-capability.md)). For example, if you self-manage S3, EC2, and IAM:

   ```
   aws eks create-capability \
     --region {{region-code}} \
     --cluster-name {{my-cluster}} \
     --capability-name my-ack \
     --type ACK \
     --role-arn {{arn:aws:iam::111122223333:role/ACKCapabilityRole}} \
     --delete-propagation-policy RETAIN \
     --configuration '{"ack": {"disabledServices": ["s3", "ec2", "iam"]}}'
   ```

   Your self-managed controllers keep reconciling your resources, unaffected.

1. For the service that you want to migrate, scale its self-managed controller down to zero replicas **before** you turn the service on in the capability:

   ```
   kubectl scale deployment ack-s3-controller \
     --namespace ack-system --replicas=0
   ```

1. Turn the service on in the capability by removing it from `disabledServices`. Specify the complete list of services that you want to remain turned off. If this service was the only one turned off, specify an empty list:

   ```
   aws eks update-capability \
     --region {{region-code}} \
     --cluster-name {{my-cluster}} \
     --capability-name my-ack \
     --configuration '{"ack": {"disabledServices": ["ec2", "iam"]}}'
   ```

   The capability installs the service’s CRDs, starts its controller, and adopts your existing resources.

1. Verify that the capability has taken over reconciliation for that service. Confirm that resources report a `Synced` condition of `True` and that the capability is not reporting `AccessDenied` errors.

1. Remove the self-managed controller for that service:

   ```
   helm uninstall ack-s3-controller --namespace ack-system
   ```

1. Repeat the previous steps for each remaining service.

**Important**  
Scale the self-managed controller down before you turn the service on in the capability. If both run at the same time, both reconcile the same resources, because by default a self-managed controller’s lease and the capability’s lease aren’t in the same namespace. If you would rather not scale down first, configure leader election as described in [Lease-based handover](#ack-migration-lease) so that the two coordinate instead.

**Note**  
To roll a service back, add it to `disabledServices` again and scale your self-managed controller back up.

**Note**  
When the capability turns a service on, it reconciles that service’s CRDs to the versions that the capability ships. If you installed a newer or modified CRD for that service, the capability updates it, which can overwrite changes that you made. If the difference can’t be applied safely, the capability reports an error for that service and doesn’t reconcile it until the CRD is compatible. If you need to keep a specific CRD version for a service, leave that service in `disabledServices` and continue to manage it yourself.

### Lease-based handover
<a name="ack-migration-lease"></a>

In this approach, you create the capability with all services enabled and rely on Kubernetes leader election to control the handover: the self-managed controller and the capability contend for the same lease, so only one of them reconciles a given resource at any time. For this to work, both must share a lease in the same namespace. The capability does not forcibly take the lease from a running self-managed controller, so you control when the handover happens by scaling the self-managed controller down.

Use this approach if you need the capability’s controller to be running and waiting before you scale your own controller down, rather than accepting a brief period in which neither reconciles.

Complete the following steps to migrate. The steps use the S3 controller (`ack-s3-controller`) as an example. Repeat them for each self-managed ACK controller that you want to migrate to the capability, substituting the corresponding controller name and Helm chart.

**Note**  
With this approach, running a controller self-managed alongside the capability is intended as a temporary state during migration, not as a long-term configuration. While both run, an interruption on either side (such as a capability deployment or an upgrade of the self-managed controller) can release the lease and let the other side acquire it, causing reconciliation to switch unexpectedly between them. Complete the migration for each controller rather than running it self-managed alongside the capability indefinitely. To keep a service self-managed for the long term, turn it off in the capability instead, as described in [Coexist with self-managed controllers (recommended)](#ack-migration-coexist).

1. Enable leader election on your self-managed ACK controller and move its lease to `kube-system`:

   ```
   helm upgrade --install ack-s3-controller \
     oci://public.ecr.aws/aws-controllers-k8s/s3-chart \
     --namespace ack-system \
     --set leaderElection.enabled=true \
     --set leaderElection.namespace=kube-system
   ```

   You must set both values. In the ACK Helm charts, the `--leader-election-namespace` flag is only applied when `leaderElection.enabled` is `true`, and leader election is disabled by default. Setting `leaderElection.namespace` alone has no effect. The controller continues to run without a lease, and both controllers reconcile the same resources at the same time after the capability is created. This applies to every ACK service controller chart, not only S3.

   This moves the controller’s lease to `kube-system`, allowing the managed capability to coordinate with it.

1. Create the ACK capability on your cluster (see [Create an ACK capability](create-ack-capability.md)). The capability starts up and contends for the lease, but the self-managed controller still holds it. Your self-managed controller keeps reconciling your resources, and the capability waits for leadership rather than forcing a takeover.

1. When you are ready to begin the migration, scale the self-managed controller down to zero replicas. This releases the lease so that the capability can acquire leadership and take over reconciliation:

   ```
   kubectl scale deployment ack-s3-controller \
     --namespace ack-system --replicas=0
   ```

   After you scale the self-managed controller down, the capability acquires the lease and begins reconciliation, usually within a short time. Scaling the self-managed controller back up does not return the lease to it, because the capability continues to hold and renew the lease. To return reconciliation to the self-managed controller, scale it back up to at least one replica and then delete the ACK capability. After you delete the capability, the self-managed controller reacquires the lease and resumes reconciliation.

1. Verify that the capability is healthy and has taken over reconciliation of your resources. Confirm that resources report a `Synced` condition of `True` and that the capability is not logging `AccessDenied` errors.

1. After you have confirmed the capability is managing your resources correctly, remove the self-managed controller:

   ```
   helm uninstall ack-s3-controller --namespace ack-system
   ```

This approach allows both controllers to coexist safely during migration. The managed capability adopts resources previously managed by self-managed controllers after you release the lease, ensuring continuous reconciliation without conflicts.

## Preview controllers and automatic promotion
<a name="ack-preview-promotion"></a>

The capability supports only controllers that are GA in upstream ACK. A controller that is in preview today can be promoted to GA upstream later. When that happens, the capability begins managing that controller automatically, without any action on your part.

This creates a risk if you run a self-managed preview controller on a cluster that also uses the capability for other controllers. You might run the preview controller as a single replica with leader election disabled, because there is no other controller to coordinate with. When that controller is promoted to GA, the capability begins managing it. At that point, two reconcilers act on the same resources with no shared lease to coordinate them. The result is the same double-reconciliation conflict that the migration steps are designed to prevent. Both reconcilers issue competing AWS API calls and write conflicting updates to the custom resource status.

To avoid this, before you run a self-managed preview controller alongside the capability:
+ Enable leader election on the self-managed preview controller and point its lease at `kube-system`, using the same `leaderElection.enabled=true` and `leaderElection.namespace=kube-system` settings shown in the migration steps. This ensures that if the controller is promoted and the capability takes it over, the two coordinate through a shared lease rather than reconciling in parallel.
+ Track the upstream GA status of any preview controllers you depend on, and plan to migrate them following the [migration path](#ack-comparison) when they are promoted. You can check the current status of each controller on the [ACK services page](https://aws-controllers-k8s.github.io/docs/services/) on the ACK website.

## Next steps
<a name="_next_steps"></a>
+  [Create an ACK capability](create-ack-capability.md) - Create an ACK capability resource
+  [ACK concepts](ack-concepts.md) - Understand ACK concepts and resource lifecycle
+  [Configure ACK permissions](ack-permissions.md) - Configure IAM and permissions