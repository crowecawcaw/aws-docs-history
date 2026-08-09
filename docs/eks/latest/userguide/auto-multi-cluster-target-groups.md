**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Configure multi-cluster target groups

By default, the Amazon EKS Auto Mode load balancer controller assumes full control over the target groups it configures. When a target group is registered with the controller, it deregisters any targets that aren’t currently in the cluster. This ensures the target group reflects the exact set of targets managed by that cluster.

Enabling **MultiCluster** support changes this behavior. A target group with MultiCluster support enabled can be associated with multiple Kubernetes clusters or support arbitrary targets from other sources. Each cluster registers and deregisters only the targets it owns, instead of deregistering targets that belong to other clusters or sources.

## How it works

When MultiCluster support is enabled, each cluster tracks the set of targets it manages and reconciles only those targets in the shared target group. Amazon EKS Auto Mode stores each cluster’s tracked targets in a Kubernetes `ConfigMap` named `eks-lbc-targets-<targetgroupbinding-name>`, in the same namespace as the load balancer resources.

###### Note

The upstream AWS Load Balancer Controller stores this state in a `ConfigMap` with the `aws-lbc-targets-` prefix. On Amazon EKS Auto Mode, the prefix is `eks-lbc-targets-` instead, so when following upstream guidance, inspect the `eks-lbc-targets-`
`ConfigMap`.

The load balancer distributes traffic equally across all registered targets. The controller doesn’t support weighted distribution across clusters. MultiCluster support works with both `ip` and `instance` target types.

## Enable MultiCluster support

Enable MultiCluster support using one of the following methods, depending on your resource type:

- **TargetGroupBinding** — set `spec.multiClusterTargetGroup: true`.
- **Ingress (ALB)** — add the annotation `alb.ingress.kubernetes.io/multi-cluster-target-group: "true"`.
- **Service (NLB)** — add the annotation `service.beta.kubernetes.io/aws-load-balancer-multi-cluster-target-group: "true"`.

## Considerations for Amazon EKS Auto Mode

The upstream [MultiCluster Target Groups](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/use_cases/multi_cluster/ "https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/use_cases/multi_cluster/") guide on the AWS Load Balancer Controller GitHub website walks through sharing one target group between two clusters. For a broader discussion of multi-cluster architectures, see [Building resilient multi-cluster applications with Amazon EKS](https://aws.amazon.com/blogs/blogs/networking-and-content-delivery/building-resilient-multi-cluster-applications-with-amazon-eks/ "https://aws.amazon.com/blogs/blogs/networking-and-content-delivery/building-resilient-multi-cluster-applications-with-amazon-eks/") on the AWS Blog. The same flow works on Amazon EKS Auto Mode with the following differences:

- The `TargetGroupBinding` custom resource is in the `eks.amazonaws.com/v1` API group, not `elbv2.k8s.aws/v1beta1`.
- The `IngressClass` controller is `eks.amazonaws.com/alb`.
- Don’t set the `alb.ingress.kubernetes.io/tags` annotation. The `AmazonEKSLoadBalancingPolicy` managed policy restricts `aws:TagKeys` to an allowlist, so custom tags cause an access denied error, and the controller can’t reconcile them off. This can cause the Ingress finalizer to become stuck on delete.
- All participating clusters must be in the same VPC, because a target group is scoped to a single VPC.

## Example

For a step-by-step walkthrough that shares a single target group between two clusters — one cluster owning the load balancer through an Ingress, and the other joining through a `TargetGroupBinding` — see [Share a target group across two clusters](auto-multi-cluster-target-groups-example.md "auto-multi-cluster-target-groups-example.md").
