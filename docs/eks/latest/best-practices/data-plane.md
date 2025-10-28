# EKS Data Plane

To operate high-available and resilient applications, you need a
highly-available and resilient data plane. An elastic data plane ensures
that Kubernetes can scale and heal your applications automatically. A
resilient data plane consists of two or more worker nodes, can grow and
shrink with the workload, and automatically recover from failures.

You have multiple choices for worker nodes with EKS:
[EKS Auto Mode managed nodes](../userguide/automode.md "../userguide/automode.md"),
[EC2 Instances](../userguide/worker.md "../userguide/worker.md") and
[Fargate](../userguide/fargate.md "../userguide/fargate.md").

EKS Auto Mode offers the easiest path to a resilient data plane. Auto Mode extends AWS
management of Kubernetes clusters beyond the cluster itself, to allow AWS to also set up
and manage the infrastructure that enables the smooth operation of your workloads. Auto Mode
automatically scales the data plane up or down as Kubernetes scales Pods and works to
continually ensure that the Nodes in your cluster are sized appropriately and cost-effectively
for the currently running workloads.

If you choose EC2 instances, you can manage the worker nodes yourself or
use
[EKS
managed node groups](../userguide/managed-node-groups.md "../userguide/managed-node-groups.md"). You can have a cluster with a mix of Auto Mode, managed,
self-managed worker nodes, and Fargate.

Fargate runs each Pod in an isolated compute environment. Each Pod
running on Fargate gets its own worker node. Fargate automatically
scales the data plane as Kubernetes scales pods. You can scale both the
data plane and your workload by using the
[horizontal
pod autoscaler](../userguide/horizontal-pod-autoscaler.md "../userguide/horizontal-pod-autoscaler.md").

The preferred way to scale EC2 worker nodes (if not using EKS Auto Mode where this is performed
automatically by AWS) is by using
[Karpenter](https://karpenter.sh/ "https://karpenter.sh/"),
[Kubernetes
Cluster Autoscaler](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md "https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/cloudprovider/aws/README.md"), or
[EC2
Auto Scaling groups](../../../autoscaling/ec2/userguide/AutoScalingGroup.md "../../../autoscaling/ec2/userguide/AutoScalingGroup.md").

## Recommendations

### Spread worker nodes and workloads across multiple AZs

You can protect your workloads from failures in an individual AZ by
running worker nodes and Pods in multiple AZs. You can control the AZ
the worker nodes are created in using the subnets you create the nodes
in.

The recommended method for spreading pods across AZs is to use
[Topology
Spread Constraints for Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/#spread-constraints-for-pods "https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/#spread-constraints-for-pods"). Auto-scaling capabilities like EKS Auto Mode and Karpenter are
aware of topology spread constraints and will automatically launch Nodes in the correct
AZs to allow your constraints to be met.

The deployment below spreads pods across AZs if possible, letting those
pods run anyway if not:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-server
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-server
  template:
    metadata:
      labels:
        app: web-server
    spec:
      topologySpreadConstraints:
        - maxSkew: 1
          whenUnsatisfiable: ScheduleAnyway
          topologyKey: topology.kubernetes.io/zone
          labelSelector:
            matchLabels:
              app: web-server
      containers:
      - name: web-app
        image: nginx
        resources:
          requests:
            cpu: 1
```

###### Note

`kube-scheduler` is only aware of topology domains via nodes that exist with those labels. If the above deployment is deployed to a cluster with nodes only in a single zone, all of the pods will schedule on those nodes as `kube-scheduler` isn’t aware of the other zones. For this topology spread to work as expected with the scheduler, nodes must already exist in all zones. The `minDomains` property of a topology spread constraints
is used to inform the scheduler of the number of eligible domains, even if there is a Node running there to avoid this issue.

###### Warning

Setting `whenUnsatisfiable` to `DoNotSchedule` will cause pods to be unschedulable if the topology spread constraint can’t be fulfilled. It should only be set if its preferable for pods to not run instead of violating the topology spread constraint.

On older versions of Kubernetes, you can use pod anti-affinity rules to
schedule pods across multiple AZs. The manifest below informs Kubernetes
scheduler to _prefer_ scheduling pods in distinct AZs.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-server
  labels:
    app: web-server
spec:
  replicas: 4
  selector:
    matchLabels:
      app: web-server
  template:
    metadata:
      labels:
        app: web-server
    spec:
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - web-server
              topologyKey: failure-domain.beta.kubernetes.io/zone
            weight: 100
      containers:
      - name: web-app
        image: nginx
```

###### Warning

Do not require that pods be scheduled across distinct AZs otherwise, the number of pods in a deployment will never exceed the number of AZs.

### Ensure ability to launch Nodes in each AZ when using EBS volumes

If you use Amazon EBS to provide Persistent Volumes, then you need to ensure that the pods
and associated EBS volume are located in the same AZ. A Pod cannot
access EBS-backed persistent volumes located in a different AZ.
The Kubernetes
[scheduler
knows which AZ a worker node](https://kubernetes.io/docs/reference/kubernetes-api/labels-annotations-taints/#topologykubernetesiozone "https://kubernetes.io/docs/reference/kubernetes-api/labels-annotations-taints/#topologykubernetesiozone") is located in from the labels that are on the Node and
will always schedule a Pod that requires an EBS volume in the same AZ as the volume.
However, if there are no worker nodes available in the AZ where the volume is located, then the Pod cannot be scheduled.

If using EKS Auto Mode or Karpenter you will need to ensure that your NodeClass selects subnets
in each AZ. If using Managed Node Groups, you need to ensure that you have a Node Group in each AZ.

An EBS storage capability is built into EKS Auto Mode, but if using Karpenter or Managed Node Groups
the [EBS CSI](../userguide/ebs-csi.md "../userguide/ebs-csi.md") will also need to be installed.

### Use EKS Auto Mode to manage worker nodes

EKS Auto Mode streamlines EKS management by providing production-ready
clusters with minimal operational overhead. Auto Mode is responsible for
scaling the number of Nodes up or down depending on the Pods that are
running in the cluster. Nodes are kept up to date with software patches
and fixes automatically, with the updates being performed in accordance with
the configured [NodePool](../userguide/create-node-pool.md#_disruption "../userguide/create-node-pool.md#_disruption")
disruption settings and Pod Disruption Budgets.

### Run the Node Monitoring Agent

The [Node Monitoring Agent](../userguide/node-health.md "../userguide/node-health.md") monitors
and reacts to Node health issues by publishing Kubernetes events and updating the status condition
on Nodes. The Node Monitoring Agent is included with EKS Auto Mode Nodes, and can be installed
as an EKS Addon for Nodes that aren’t managed by Auto Mode.

EKS Auto Mode, Managed Node Groups, and Karpenter all have the ability to detect fatal Node conditions
reported by the Node Monitoring Agent and repair those Nodes automatically when those conditions occur.

### Implement QoS

For critical applications, consider defining `requests`=`limits` for
the container in the Pod. This will ensure that the container will not
be killed if another Pod requests resources.

It is a best practice to implement CPU and memory limits for all
containers as it prevents a container inadvertently consuming system
resources impacting the availability of other co-located processes.

### Configure and Size Resource Requests/Limits for all Workloads

Some general guidance can be applied to sizing resource requests and
limits for workloads:

- Do not specify resource limits on CPU. In the absence of limits, the
  request acts as a weight on
  [how
  much relative CPU time containers get](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#how-pods-with-resource-limits-are-run "https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#how-pods-with-resource-limits-are-run"). This allows your workloads to
  use the full CPU without an artificial limit or starvation.
- For non-CPU resources, configuring `requests`=`limits` provides
  the most predictable behavior. If `requests`!=`limits`, the
  container also has its
  [QOS](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/#qos-classes "https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/#qos-classes")
  reduced from Guaranteed to Burstable making it more likely to be evicted
  in the event of
  [node
  pressure](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/ "https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/").
- For non-CPU resources, do not specify a limit that is much larger than
  the request. The larger `limits` are configured relative to
  `requests`, the more likely nodes will be overcommitted leading to
  high chances of workload interruption.
- Correctly sized requests are particularly important when using a node
  auto-scaling solution like
  [Karpenter](https://aws.github.io/aws-eks-best-practices/karpenter/ "https://aws.github.io/aws-eks-best-practices/karpenter/") or
  [Cluster
  AutoScaler](https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/ "https://aws.github.io/aws-eks-best-practices/cluster-autoscaling/"). These tools look at your workload requests to determine the
  number and size of nodes to be provisioned. If your requests are too
  small with larger limits, you may find your workloads evicted or OOM
  killed if they have been tightly packed on a node.

Determining resource requests can be difficult, but tools like the
[Vertical
Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler "https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler") can help you "right-size" the requests by observing
container resource usage at runtime. Other tools that may be useful for
determining request sizes include:

- [Goldilocks](https://github.com/FairwindsOps/goldilocks "https://github.com/FairwindsOps/goldilocks")
- [Parca](https://www.parca.dev/ "https://www.parca.dev/")
- [Prodfiler](https://prodfiler.com/ "https://prodfiler.com/")
- [rsg](https://mhausenblas.info/right-size-guide/ "https://mhausenblas.info/right-size-guide/")

### Configure resource quotas for namespaces

Namespaces are intended for use in environments with many users spread
across multiple teams, or projects. They provide a scope for names and
are a way to divide cluster resources between multiple teams, projects,
workloads. You can limit the aggregate resource consumption in a
namespace. The
[`ResourceQuota`](https://kubernetes.io/docs/concepts/policy/resource-quotas/ "https://kubernetes.io/docs/concepts/policy/resource-quotas/")
object can limit the quantity of objects that can be created in a
namespace by type, as well as the total amount of compute resources that
may be consumed by resources in that project. You can limit the total
sum of storage and/or compute (CPU and memory) resources that can be
requested in a given namespace.

If resource quota is enabled for a namespace for compute resources like
CPU and memory, users must specify requests or limits for each container
in that namespace.

Consider configuring quotas for each namespace. Consider using
`LimitRanges` to automatically apply preconfigured limits to
containers within a namespaces.

### Limit container resource usage within a namespace

Resource Quotas help limit the amount of resources a namespace can use.
The
[`LimitRange`
object](https://kubernetes.io/docs/concepts/policy/limit-range/ "https://kubernetes.io/docs/concepts/policy/limit-range/") can help you implement minimum and maximum resources a container
can request. Using `LimitRange` you can set a default request and
limits for containers, which is helpful if setting compute resource
limits is not a standard practice in your organization. As the name
suggests, `LimitRange` can enforce minimum and maximum compute
resources usage per Pod or Container in a namespace. As well as, enforce
minimum and maximum storage request per PersistentVolumeClaim in a
namespace.

Consider using `LimitRange` in conjunction with `ResourceQuota` to
enforce limits at a container as well as namespace level. Setting these
limits will ensure that a container or a namespace does not impinge on
resources used by other tenants in the cluster.

### Use NodeLocal DNSCache

You can improve the Cluster DNS performance by running
[NodeLocal
DNSCache](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/ "https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/"). This feature runs a DNS caching agent on cluster nodes as a
DaemonSet. All the pods use the DNS caching agent running on the node
for name resolution instead of using `kube-dns` Service. This feature is automatically
included in EKS Auto Mode.

### Configure auto-scaling CoreDNS

Another method of improving Cluster DNS performance is by
enabling the built-in [auto-scaling of CoreDNS Pods](../userguide/coredns-autoscaling.md "../userguide/coredns-autoscaling.md").

This feature continuously monitors the cluster state, including the number of nodes and
CPU cores. Based on that information, the controller will dynamically adapt
the number of replicas of the CoreDNS deployment in an EKS cluster.
