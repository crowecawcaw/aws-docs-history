

# ADVPERF02-BP02 Consider containerization for scalability, low latency, and cost optimization
<a name="advperf02-bp02"></a>

 Use containers to run advertising workloads at scale with low latency and lower infrastructure cost. Containers start faster than virtual machines, run at higher density on shared hosts, and isolate processes from each other. They also support microservices patterns, so each component of an advertising workload scales independently. 

 **Desired outcome:** 
+  Your advertising workloads run in containers orchestrated on AWS, delivering faster startup times, higher resource utilization, and predictable performance at scale. 
+  Container-based microservices replace tightly coupled monolithic components, enabling independent scaling of each workload layer without cascading dependencies. 
+  Container images are pre-built with dependencies to minimize startup latency during scale-out events. 

 **Common anti-patterns:** 
+  Running ad tech workloads on full virtual machines where guest OS overhead consumes resources that could be allocated to bid processing or model inference. 
+  Keeping monolithic application architectures that force the entire workload to scale as a single unit, even when only one component (the bid request handler or audience lookup service) is under load. 
+  Using large, general-purpose container images with unnecessary dependencies that slow down startup times and reduce scaling responsiveness. 

 **Benefits of establishing this best practice:** 
+  Containerization reduces infrastructure cost per workload unit by removing guest OS overhead and increasing host density. 
+  Faster container startup times mean your scaling response is measured in seconds rather than minutes, directly improving your ability to absorb burst traffic without dropped requests. 
+  Process isolation reduces noisy-neighbor interference on multitenant hosts, delivering more consistent latency under mixed workload conditions. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Containers share the host OS kernel and start only the processes they need. They start in seconds rather than the minute or more a VM takes. During a live-event traffic spike, the difference between a 10-second scale-out and a 60-second scale-out determines whether bid requests are dropped or absorbed. 

 Resource utilization gains compound with scale. On a host running multiple containerized ad-serving components, container isolation keeps one component's CPU or memory spike from degrading others. Virtual machines on the same host cannot match this granularity. Higher container density per host, combined with auto scaling, reduces the number of hosts you pay for at baseline while keeping burst capacity available. 

 Decomposition pays off when components have different load curves. A targeting change drives audience lookup while request handling stays flat, and a creative refresh drives request handling while audience lookup stays flat. When curves differ, separating the components lets each carry its own capacity and turns one oversized fleet into several right-sized ones. When curves move together, separation adds network hops and operational surface for no scaling benefit. Draw the boundaries along load patterns, not organizational structure. 

 The second reason to decompose is isolation. Independent components mean one component's spike doesn't consume another's capacity, but their effects remain coupled. A starved audience-lookup service still produces late bids from a healthy request handler, so the auction fails anyway. Isolation buys diagnosability and targeted remediation, not immunity from cascading failure. 

 Elasticity in practice lags what the metrics suggest, because containers do work at startup before they serve traffic. A container that resolves dependencies, loads models, or warms caches during startup isn't handling requests during that interval. The effective scale-out time is provisioning time plus warm-up time. Move that work into the image build to shorten the interval. If you leave it at startup, your metrics report a faster scale-out than the auction sees. Startup work runs on every scale-out, so front-load it into the image. 

 Density is a cost decision with a latency consequence. Running more components per host reduces the baseline host count. It also puts latency-sensitive and batch work on shared resources, where batch bursts become bid-path jitter. A scheduler cannot decide which components can safely share a host. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Containerize your advertising workload components:** Package each advertising service (bid request handler, audience lookup, creative serving, frequency cap checker, bid response assembler) as a separate container image. Pre-install all dependencies at image build time so containers are immediately ready to serve traffic when they start. Use multi-stage Docker builds to keep production images minimal. 

1.  **Deploy and orchestrate containers on Amazon EKS:** Deploy your containerized services on Amazon EKS with node groups sized for your baseline workload. Configure pod anti-affinity rules to distribute replicas across Availability Zones for high availability. Enable EKS managed node groups to simplify node lifecycle management. 

1.  **Configure the Horizontal Pod Autoscaler (HPA) per service:** Define HPA policies for each advertising service based on the metric most relevant to that service's load (CPU utilization for compute-bound services, custom metrics for queue-depth-driven services). Set target utilization at 65% or lower to leave headroom for burst absorption before new pods become available. 

1.  **Decompose monolithic bidding platform into containerized microservices:** Identify the components of your bidding platform that scale independently (bid request ingestion, real-time data enrichment, auction logic, response serialization) and decompose them into separate containerized services. Define service contracts (APIs) between components and implement health checks for each service independently. 

1.  **Use container image pull-through caching:** Configure [Amazon ECR](https://aws.amazon.com/ecr/) pull-through cache rules to cache container images at the regional level, reducing image pull latency during rapid scale-out events when many new containers start simultaneously. This is particularly relevant during live event traffic spikes when dozens of new bid server containers start within seconds of each other. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP03 Consider low-latency node provisioning tools to improve startup and scaling time](advperf02-bp03.md) 

 **Related documents:** 
+  [Amazon ECS vs Amazon EKS: making sense of AWS container services](https://aws.amazon.com/blogs/containers/amazon-ecs-vs-amazon-eks-making-sense-of-aws-container-services/) 
+  [Under the hood: Lazy Loading Container Images with Seekable OCI and AWS Fargate](https://aws.amazon.com/blogs/containers/under-the-hood-lazy-loading-container-images-with-seekable-oci-and-aws-fargate/) 

 **Related services:** 
+  [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) 
+  [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) 
+  [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) 