

# REL10-BP03 Use bulkhead architectures to limit scope of impact

 A failure in a shared component can spread to every request a workload handles. Bulkhead architectures, also called cell-based architectures, divide a workload into independent instances that each serve a subset of requests. Because the instances share no state, a failure is confined to one of them, so most requests continue unaffected. This containment works even for faults that would otherwise be hard to isolate. 

 **Desired outcome:** 
+  Your workload runs as multiple independent cells, each serving a subset of requests. 
+  A failure in one cell affects only the requests that cell handles, not the whole workload. 
+  Cells share no state, and cross-cell interactions are minimal. 
+  Each cell has a bounded maximum size, and you scale by adding cells rather than growing existing ones. 

 **Common anti-patterns:** 
+  Teams allow cells to grow without an upper bound. 
+  Teams deploy code changes to all cells at the same time. 
+  Cells share state or components beyond the routing layer. 
+  Teams add complex business or routing logic to the router layer. 
+  Designs allow frequent cross-cell interactions that couple cells together. 

 **Benefits of establishing this best practice:** 
+  Common failures, such as a bad deployment or a request that triggers a specific failure mode, stay contained within one cell. 
+  The workload gains fault isolation against failure types that are otherwise hard to contain. 
+  Scaling by adding cells keeps each fault domain small as demand grows. 
+  A simple router layer is straightforward to test and reason about, which reduces the risk of a workload-wide failure. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The *bulkhead* pattern takes its name from ship design, where a hull is divided into sealed sections so that a breach floods only one section rather than sinking the vessel. In technology, you use this pattern to create fault-isolated boundaries that restrict a failure to a limited set of components. Availability Zones and Regions are one form of this boundary, but you can extend the concept inside a single workload by running multiple independent copies of it. Each copy is a *cell*, or a self-contained instance that handles part of the traffic and shares nothing with its peers. When 10 cells serve the load and one cell fails, roughly 90 percent of requests are unaffected. 

 The partition key determines how requests map to cells, so it must align with the *grain* of the service. The grain is the natural way the workload subdivides with the fewest interactions across the divide. Customer ID and resource ID are common choices because they appear in nearly every request and rarely require one cell to talk to another. A poorly chosen key forces cross-cell interactions, and every such interaction reintroduces coupling between cells. Keep each upstream service on a single cell for the lifetime of the resource. Plan a migration path for the case where one tenant outgrows its cell. 

 The router layer is the one component cells cannot avoid sharing. A fault in the router affects every cell at once, so it must stay as simple and horizontally scalable as possible. Keep business logic out of it, and prefer a computationally cheap mapping from partition key to cell, such as a cryptographic hash combined with modular arithmetic. As Colm MacCárthaigh describes in [Reliability, constant work, and a good cup of coffee](https://builder.aws.com/content/3F05oqNtNUWxHJ5r6L6I2HrH4rI/reliability-constant-work-and-a-good-cup-of-coffee), simple designs that perform constant work are more reliable and easier to reason about. 

 Cell size is a reliability control. A cell that grows without limit becomes a large fault domain. Establish a maximum size through load testing that pushes a cell to its breaking point. Set a safe operating margin below it, and grow the overall workload by adding cells. Stagger deployments so a faulty change reaches one cell at a time, and deploy each cell across multiple Availability Zones for common disruptions. Where the resilience requirement justifies the added complexity, deploy cells across multiple Regions for rare Region-wide events. 

 The following figure shows a cell-based architecture: a thin routing layer presenting a single endpoint to clients, distributing requests by partition key to independent cells that each hold their own compute and data. 

![Architecture diagram of a cell-based workload: a thin routing layer presents a single endpoint and distributes requests by partition key to independent cells that each hold their own compute and data.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/cell-based-architecture.png)

*Cell-based architecture with a thin routing layer and independent cells*


### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose a partition key:** Select a key that aligns with the grain of the service and subdivides the workload with minimal cross-cell interaction, such as customer ID or resource ID. Make sure the key is present in every request, either directly or through a value from which it can be derived deterministically. 

1.  **Establish persistent cell mapping:** Map each upstream resource to a single cell for the lifetime of that resource, and prevent cells from sharing state or components. Plan a migration strategy for the case where a tenant or resource outgrows its cell and needs to move. 

1.  **Keep the router layer simple and scalable:** Distribute requests with a computationally efficient mapping, such as a cryptographic hash combined with modular arithmetic, and keep business logic out of the router. Design it to scale horizontally so it does not become a shared bottleneck or a single point of failure. 

1.  **Set a maximum cell size:** Determine the ceiling through [REL07-BP04 Load test your workload](rel07-bp04.md) that drives a cell to its breaking point, then establish a safe operating margin below it. Scale the workload by adding cells rather than by letting existing cells grow. 

1.  **Layer cells across Availability Zones and Regions:** Build cells on multiple Availability Zones to handle common disruptions, and extend to [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md) across Regions only when the resilience requirement justifies the additional complexity. Most workloads do not require a multi-Region cell design. 

1.  **Deploy code in staggered waves across cells:** Roll changes out to cells in stages rather than to all cells at once, so a faulty deployment or human error affects one cell instead of the whole workload. For patterns that make this repeatable, see [Automating safe, hands-off deployments](https://builder.aws.com/content/3ErTKQOTKc5NIw031UePBPxTQ6I/automating-safe-hands-off-deployments). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md) 
+  [REL10-BP02 Automate recovery for components constrained to a single location](rel10-bp02.md) 
+  [REL07-BP04 Load test your workload](rel07-bp04.md) 
+  [REL08-BP05 Deploy changes with automation](rel08-bp05.md) 
+  [REL11-BP05 Use static stability to prevent bimodal behavior](rel11-bp05.md) 

 **Related documents:** 
+  [Reliability, constant work, and a good cup of coffee](https://builder.aws.com/content/3F05oqNtNUWxHJ5r6L6I2HrH4rI/reliability-constant-work-and-a-good-cup-of-coffee) 
+  [Workload isolation using shuffle-sharding](https://builder.aws.com/content/3F06NpJ8YeoIGP8VHTw4n81pFn8/workload-isolation-using-shuffle-sharding) 
+  [Automating safe, hands-off deployments](https://builder.aws.com/content/3ErTKQOTKc5NIw031UePBPxTQ6I/automating-safe-hands-off-deployments) 
+  [Reducing the Scope of Impact with Cell-Based Architecture - Reducing the Scope of Impact with Cell-Based Architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Learn to create a robust, easy-to-scale architecture with cells (ARC335)](https://www.youtube.com/watch?v=OkT12t-fvRE) 
+  [AWS re:Invent 2023 - Resilient architectures at scale: Real-world use cases from Amazon.com (ARC305)](https://www.youtube.com/watch?v=fQgaR-iQrTY) 
+  [Back to Basics: Cell-Based Architecture](https://www.youtube.com/watch?v=RbD0uK1lmz4) 
+  [AWS re:Invent 2024 - SaaS meets cell-based architecture: A natural multi-tenant fit (SAS315)](https://www.youtube.com/watch?v=wYm_PJc2U8c) 