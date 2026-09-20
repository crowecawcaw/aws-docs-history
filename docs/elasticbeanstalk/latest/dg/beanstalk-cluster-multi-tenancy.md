

# Multi-tenancy for Beanstalk Cluster environments
<a name="beanstalk-cluster-multi-tenancy"></a>

Beanstalk Cluster environments that use the same subnets run on the same Amazon EKS cluster, so they share compute infrastructure. Elastic Beanstalk separates them on that shared cluster: each environment's application runs in its own partition of the cluster, and Elastic Beanstalk blocks network traffic between environments by default. This topic describes the separation you get, how to widen or tighten it, and which requirements a shared cluster cannot satisfy.

Isolation between Beanstalk Cluster environments has two independent dimensions. Network isolation controls which environments can send traffic to an environment's application. Compute isolation controls whether an environment's application replicas share nodes with other environments. You can configure either one without the other.

## Choosing an isolation boundary
<a name="beanstalk-cluster-multi-tenancy-boundary"></a>

Decide how strong a boundary an environment needs before you create it, because the choice is made through the subnets you assign and you cannot change the subnets of an existing environment. Two boundaries are available, and they correspond to the two multi-tenancy models that Amazon EKS documents.


| Boundary | How you get it | What it separates | 
| --- | --- | --- | 
| Shared cluster (soft multi-tenancy) | Create the environments with the same set of subnets. This is the default when environments share a VPC configuration. | Each environment's application runs in its own partition of the cluster with network traffic between environments blocked by default. The environments share the cluster itself, and share nodes unless you configure dedicated nodes. | 
| Separate clusters (hard multi-tenancy) | Create the environments with different sets of subnets. Elastic Beanstalk then creates a separate cluster for each set. | Nothing is shared. Separate clusters have separate control planes, separate nodes, and no network path between the applications running on them. | 

A shared cluster provides logical separation between environments, enforced by configuration that Elastic Beanstalk applies to the cluster. A separate cluster provides infrastructure separation. Amazon EKS documents the cluster as the construct that provides a strong security boundary, because a workload that gained access to a node could reach the credentials and data of anything else running on that node. Logical separation within a cluster is soft multi-tenancy; a cluster for each tenant is hard multi-tenancy. For the general guidance this reflects, see [Tenant isolation](https://docs.aws.amazon.com/eks/latest/best-practices/tenant-isolation.html) in the *Amazon EKS Best Practices Guide*.

**Important**  
Use separate subnet sets, and therefore separate clusters, when environments run workloads that must not share infrastructure. Examples include environments that belong to different end customers of your business, environments that run code you do not control, and environments in the scope of a compliance regime that requires infrastructure separation. The controls described in the rest of this topic separate environments on a shared cluster, but they do not make a shared cluster equivalent to separate clusters.

Separate clusters cost more and use capacity less efficiently, because each cluster is billed separately and nodes cannot be shared across clusters. A shared cluster is the right choice for environments that one team owns and operates together, such as the services that make up a single application. Separating production from development is a common reason to use different subnet sets even when nothing requires it. For how Elastic Beanstalk groups environments onto clusters, see [Environment grouping](beanstalk-cluster-concepts.md#beanstalk-cluster-clusters-sharing). For the subnet settings themselves, see [Configuring networking for Beanstalk Cluster environments](configuring-cluster-networking.md).

## Network isolation on a shared cluster
<a name="beanstalk-cluster-clusters-isolation"></a>

Elastic Beanstalk blocks network traffic between Beanstalk Cluster environments on a shared cluster by default. No configuration is required to get this, and there is no option that turns it off. An environment's application replicas cannot receive traffic from another environment's application copies on any port unless you permit it with one of the options in this section.

Elastic Beanstalk permits its own operational components to reach your application, so that health reporting, log collection, and metric-based scaling continue to work.

Traffic that reaches an environment through its load balancer is unaffected. Blocking applies to traffic sent from one environment's application replicas directly to another's, not to traffic that arrives from outside the cluster. Requests that reach your application through its Application Load Balancer are delivered normally, including requests that another environment sends to that load balancer's public endpoint.

### Permitting environments to communicate
<a name="beanstalk-cluster-multi-tenancy-groups"></a>

Three options in the `aws:elasticbeanstalk:eks:environment` namespace permit traffic between environments on a shared cluster. Each takes a comma-separated list. Names are limited to the characters `a-z`, `A-Z`, `0-9`, and `-`; they must start with a letter and be 4 to 40 characters long. Changing any of them does not interrupt the environment.


| Option | Effect | Use it when | 
| --- | --- | --- | 
| ingress-groups | Joins the environment to one or more named groups. Every environment in a group can send traffic to every other environment in that group, in both directions. An environment can belong to more than one group. | A set of environments all need to call each other, such as the services of one application. | 
| ingress-allowlist-environments | Permits the named environments to send traffic to this environment. The permission is one way: naming an environment here does not let this environment call it. | An environment serves an internal API that specific other environments call. | 
| ingress-allowlist-groups | Permits every environment in the named groups to send traffic to this environment, one way, without joining those groups. | An environment serves a set of callers that already share a group, and must not gain access to them in return. | 

Set `ingress-groups` on each environment that joins the group; group membership is not configured from one place. An environment leaves a group when you remove the group from its `ingress-groups` value or terminate the environment. Set the allowlist options on the environment that *receives* the traffic, naming the callers you want to permit.

The two mechanisms combine. An environment can join a group for the services it works with as a peer and separately allowlist a caller that must reach it one way. For how to set configuration options on an environment, see [Configuration options](command-options.md).

Permitting traffic does not configure discovery. Your application still needs to know what address to call, which you supply the same way you supply any other setting, through an environment property. Elastic Beanstalk does not inject the addresses of the environments you permit.

## Dedicated nodes for an environment
<a name="beanstalk-cluster-multi-tenancy-nodes"></a>

By default, Elastic Beanstalk schedules application replicas from any environment onto the shared node capacity of the cluster, so copies from different environments can run on the same node. To keep an environment's application replicas on nodes that no other environment uses, set the `node-pool` option in the `aws:elasticbeanstalk:eks:environment` namespace to a name of your choice.

Elastic Beanstalk then reserves a set of nodes for that name and schedules only application replicas from environments with the same `node-pool` value onto them. Environments that set no value, or a different value, cannot be placed on those nodes.

**Important**  
Environments that share a `node-pool` value share nodes with each other. To give a single environment nodes that nothing else uses, give it a value that no other environment uses.

Changing `node-pool` restarts the environment's application replicas so that Elastic Beanstalk can reschedule them onto the correct nodes. Dedicated nodes also reduce the effect one environment's resource use has on another, because the environments no longer compete for the same node's CPU and memory. Dedicated nodes are independent of network isolation: environments can run on separate nodes and still be permitted to communicate, or share nodes and be blocked from communicating.

Reserve `node-pool` for a requirement that is specifically about node capacity. If your goal is to separate environments from each other, giving them different subnets is simpler and separates the cluster as well as the nodes.

## What a shared cluster does not separate
<a name="beanstalk-cluster-multi-tenancy-limits"></a>

Understand these limits before you place environments with different security or compliance requirements on the same cluster. Each of them is a consequence of the environments sharing a cluster, and each is removed by giving the environments different subnets so that Elastic Beanstalk creates separate clusters.
+ **Outbound traffic is not restricted.** The default separation blocks traffic that arrives at an environment. It does not restrict where an environment's application can send traffic. An application can reach any destination its network configuration and its IAM permissions allow, including the internet and other AWS services. There is no option that restricts outbound traffic from a Beanstalk Cluster environment.
+ **The cluster's control plane is shared.** Every environment on the cluster is served by one Amazon EKS control plane, and its Kubernetes version is fixed for the life of the cluster. Elastic Beanstalk operates the control plane and you do not configure it, but it is not duplicated per environment.
+ **Nodes are shared unless you configure dedicated nodes.** Without `node-pool`, application replicas from different environments run on the same nodes and draw on the same CPU and memory. Elastic Beanstalk does not reserve node capacity per environment.
+ **Cluster-wide failures affect every environment on the cluster.** If Elastic Beanstalk stops managing a cluster because its infrastructure no longer matches the expected configuration, updates fail for every environment on that cluster until the drift is resolved. Recovery is per cluster rather than per environment: revert the change that caused it, and Elastic Beanstalk resumes managing the cluster and all of its environments. See [Cluster configuration drift](beanstalk-cluster-concepts.md#beanstalk-cluster-clusters-drift).

Application-level protections are your responsibility in either boundary. Network separation between environments does not authenticate callers, encrypt traffic between environments, or restrict what an application does with the credentials it holds. Give each environment its own application role so that its AWS permissions are scoped to it, and treat permitted traffic between environments as traffic your application must still authorize. See [Application permissions](beanstalk-cluster-permissions.md#beanstalk-cluster-permissions-application).

## Matching a requirement to a control
<a name="beanstalk-cluster-multi-tenancy-choosing"></a>


| Requirement | Control | 
| --- | --- | 
| Environments must not share infrastructure | Create them with different sets of subnets, so that Elastic Beanstalk creates a separate cluster for each. Decide this before creating the environments; you cannot change the subnets afterward. | 
| Environments must not reach each other over the network | No configuration. This is the default on a shared cluster. | 
| A set of environments must call each other | Set ingress-groups to the same group name on each of them. | 
| One environment must accept calls from specific others, but not the reverse | Set ingress-allowlist-environments, or ingress-allowlist-groups, on the environment that receives the traffic. | 
| An environment's application replicas must not share nodes with other environments | Set node-pool to a value that no other environment uses. | 
| An environment's outbound traffic must be restricted | Not available through a configuration option. Restrict it in the application, or through the network configuration of the subnets you assign to the environment. | 