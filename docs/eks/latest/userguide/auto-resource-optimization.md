

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Rightsize workloads with resource optimization

**Preview release**  
EKS Auto Mode resource optimization is in preview release for Amazon EKS and is subject to change.

EKS Auto Mode resource optimization is a capability of EKS Auto Mode. It recommends CPU and memory requests for your workloads based on the usage it observes for each container. For each workload, you choose whether resource optimization only reports recommendations or also applies them to running Pods. For example, you can rightsize every application namespace without editing Pod templates or creating drift in your GitOps tools.

Teams usually set CPU and memory requests when they first deploy a workload and rarely revisit them. EKS Auto Mode provisions EC2 instances to fit those requests. When requests are higher than a workload needs, you run more or larger instances than the workload uses. With resource optimization, requests follow what each workload actually uses.

## How resource optimization works
<a name="auto-ro-how-it-works"></a>

You turn on resource optimization by creating a `ClusterResourceOptimizationPolicy` in your cluster. The policy selects which namespaces and workloads resource optimization manages, and sets a mode for them:

 `Recommend` (default)  
Resource optimization collects usage and produces recommendations. It doesn’t change any Pod.

 `Apply`   
Resource optimization also resizes running Pods to match its recommendations.

A policy that doesn’t set `mode` uses `Recommend`. Creating a policy doesn’t change any Pod until you set `mode: Apply`.

For each workload that a policy selects, resource optimization creates a `ResourceOptimization` object (short name `ro`) in the workload’s namespace. This object holds the workload’s recommendations, its status, and the policy that supplied each setting. You don’t create or edit these objects. Resource optimization removes them when no policy selects the workload.

### How changes are applied
<a name="auto-ro-how-changes-apply"></a>

In `Apply` mode, resource optimization resizes Pods in place through the Kubernetes Pod `resize` subresource, without recreating them. It never edits the Deployment or StatefulSet Pod template. The Pod template in your cluster matches the one in your source repository. GitOps tools such as Argo CD and Flux don’t detect drift and have nothing to revert.

New Pods that the workload creates, for example during a scale-out, a node consolidation, or a rollout, start at the recommended size rather than the size in the Pod template. For exceptions, such as workloads with no requests or resources that a Horizontal Pod Autoscaler scales on, see [How resource optimization works with autoscalers and workload types](auto-ro-workloads.md).

For more information about how resource optimization handles resizes that don’t fit on the current node, see [How resource optimization applies changes to Pods](auto-ro-resize.md).

### How recommendations are sized
<a name="auto-ro-profile"></a>

Recommendations follow an optimization profile. This preview includes one profile, `Balanced`:
+ For CPU, resource optimization sizes the request so that the 95th percentile of the container’s observed usage is about 87% of the request.
+ For memory, it sizes the request so that the 95th percentile of observed usage is about 70% of the request. Memory gets more headroom than CPU because a container that runs out of memory is stopped, while a container that runs short of CPU is only throttled.
+ Recommendations stay within a band that’s shared across the containers in a Pod: from half of the smallest request declared in the Pod template to twice the largest declared limit. If a container declares no limit, the band has no upper bound, and recommendations can grow to the largest size that your NodePools can fit. For details, see [EKS Auto Mode resource optimization resource reference](auto-ro-reference.md) and [How resource optimization works with autoscalers and workload types](auto-ro-workloads.md).

Resource optimization needs about 12 hours of usage history for a container before it produces the first recommendation. Until then, the container keeps the request declared in its Pod template.

## Requirements and scope
<a name="auto-ro-requirements"></a>
+  **Cluster**: An EKS Auto Mode cluster running Kubernetes version 1.36 or later. Resource optimization is available on every such cluster, including existing ones. You don’t need to update the cluster or call an EKS API to use it.
+  **Workloads**: Deployments and StatefulSets.
+  **Resources**: CPU and memory. Resource optimization doesn’t size GPUs or ephemeral storage, and it doesn’t change replica counts.
+  **Namespaces**: Resource optimization never manages workloads in the `kube-system`, `kube-public`, or `kube-node-lease` namespaces, even if a policy selects them.
+  **Pricing**: Resource optimization is available at no additional charge.
+  ** AWS Regions**: US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Frankfurt), Europe (Ireland), Asia Pacific (Seoul), and Asia Pacific (Tokyo).

## Preview considerations
<a name="auto-ro-considerations"></a>

Review these behaviors before you set `mode: Apply` on production workloads:
+  **No automatic rollback**: If an applied recommendation degrades a workload, resource optimization doesn’t revert it. To stop further changes to that workload, opt it out or set its policy to `Recommend`. For instructions, see [Opt out a single workload](auto-ro-enable.md#auto-ro-enable-opt-out) and [Stop resizing but keep recommendations](auto-ro-enable.md#auto-ro-enable-pause).
+  **Applied values stay in place**: Deleting a policy, switching to `Recommend`, or opting a workload out stops future changes only. Running Pods keep the CPU and memory that resource optimization last applied. To return Pods to the values in the Pod template, restart the workload, for example with `kubectl rollout restart`. For StatefulSets that use the `OnDelete` update strategy, see [Opt out a single workload](auto-ro-enable.md#auto-ro-enable-opt-out).
+  **No cost or savings figures**: Resource optimization doesn’t report estimated savings in this preview. To measure the cost effect of rightsizing, use AWS Cost Explorer or your existing cost tools.
+  **Console access**: There is no resource optimization page in the Amazon EKS console. The Kubernetes resource viewer shows `ClusterResourceOptimizationPolicy` and `ResourceOptimization` objects as read-only. For more information, see [View Kubernetes resources in the AWS Management Console](view-kubernetes-resources.md).

## Topics
<a name="auto-ro-topics"></a>
+  [Turn on and configure EKS Auto Mode resource optimization](auto-ro-enable.md) 
+  [How resource optimization policies select and combine](auto-ro-policies.md) 
+  [How resource optimization works with autoscalers and workload types](auto-ro-workloads.md) 
+  [How resource optimization applies changes to Pods](auto-ro-resize.md) 
+  [EKS Auto Mode resource optimization resource reference](auto-ro-reference.md) 
+  [Troubleshoot EKS Auto Mode resource optimization](auto-ro-troubleshoot.md) 