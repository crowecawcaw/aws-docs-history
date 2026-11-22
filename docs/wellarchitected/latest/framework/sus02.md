

# Optimize resource provisioning

 Optimizing resource provisioning means that you allocate only the resources needed for your workloads, reducing waste and improving efficiency. This section covers using reserved capacity for predictable workloads, implementing elasticity through auto-scaling, event-driven invocation, and serverless technologies for variable workloads, dynamically provisioning development environments to eliminate idle resources during non-working hours, and matching resource allocation precisely to business requirements to avoid over-provisioning. 


|  SUS02: How do you provision resources to match workload demand and avoid waste?  | 
| --- | 
|  [SUS02-BP01 Implement elasticity for variable workloads](sus02-bp01.md)  | 
|  [SUS02-BP02 Provision development, build, and test resources dynamically](sus02-bp02.md)  | 
|  [SUS02-BP03 Match resource use to business need](sus02-bp03.md)  | 
|  [SUS02-BP04 Define the baseload for predictable and steady-state workloads](sus02-bp04.md)  | 

## Capability intent
<a name="sus02-intent"></a>
+  Capacity tracks actual demand, scaling out during peaks and scaling in during quiet periods without manual intervention, so resources spend most of their time serving requests rather than sitting idle. 
+  Work is triggered by events rather than discovered by polling, so components consume resources only when there is something to process instead of running continuously to check whether there is. 
+  Non-production environments exist only while they are actively in use, provisioned and torn down automatically so idle development capacity does not accumulate. 
+  Service-level objectives reflect real business requirements rather than assumed maximums, and the workload applies deliberate trade-offs in precision, timeliness, and processing to reduce consumption. 
+  Predictable, steady-state workloads run on capacity matched precisely to their needs, with price commitments and Capacity Reservations chosen independently so one does not force the other. 
+  Undifferentiated capacity management is shifted to managed and serverless services wherever they can run it more efficiently than a single workload can alone. 

## Common issues to watch for
<a name="sus02-issues"></a>
+  Teams provision for peak load and leave that capacity running even when demand is low, so idle resources consume energy for work that rarely arrives. 
+  Scaling policies use a metric that lags real demand, such as average CPU on a memory-bound workload, so they scale late and then overshoot, or oscillate and waste resources. 
+  Components poll a queue, table, or partner endpoint on a fixed schedule regardless of whether work has arrived, so the workload consumes resources at a constant rate while doing nothing most of the time. 
+  Synchronous request chains hold compute open while downstream calls complete, so provisioned capacity is spent waiting on other components rather than doing work. 
+  Non-production environments run permanently because teardown depends on someone remembering, leaving orphaned build agents and idle test stacks. 
+  Service-level objectives are set to the theoretical maximum, so every layer is provisioned to defend a precision, latency, or availability target no user asked for. 
+  A single provisioning strategy is applied to every workload regardless of its demand pattern or business criticality. 
+  Financial commitment and capacity reservation are coupled, such as buying a zonal reservation for a compute-flexible workload, which forces idle capacity when the workload moves. 