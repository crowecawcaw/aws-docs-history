

# Enhance workload efficiency

 This capability covers best practices to enhance workload efficiency. The cloud is inherently flexible, and you can provision resources as needed. Be intentional about your choices and usage of AWS services, resources, and features. It is important that you continually evaluate your design decisions, and explore opportunities to maximize efficiency and decommission unused resources. 


|  SUS03: How do you improve the resource efficiency of your workload?  | 
| --- | 
|  [SUS03-BP01 Optimize workloads for high resource usage efficiency](sus03-bp01.md)  | 
|  [SUS03-BP02 Flatten demand peaks for consistently high resource utilization](sus03-bp02.md)  | 
|  [SUS03-BP03 Use the most resource-efficient computational approach](sus03-bp03.md)  | 
|  [SUS03-BP04 Use purpose-built, energy efficient hardware tailored to your workload](sus03-bp04.md)  | 

## Capability intent
<a name="sus03-intent"></a>
+  Workloads meet business requirements using the minimum resources necessary, with capacity right-sized to real demand and unused resources decommissioned. 
+  You measure resource usage efficiency continuously across compute, storage, and networking. You validate each optimization against a baseline. 
+  Your architecture shapes demand through buffering, batching, and throttling. A smaller, steadier fleet of resources runs at higher utilization instead of standing idle between peaks. 
+  The computational approach and resources match the actual complexity or simplicity of the problem. 
+  Workload components run on services suited to their specific mix of resource demands, such as compute, memory, and networking. They use energy-efficient processors and purpose-built accelerators where the software stack supports them. 

## Common issues to watch for
<a name="sus03-issues"></a>
+  Teams pick general-purpose services and leave default settings in place. 
+  Teams overprovision to cater to rare peaks or theoretical requirements rather than observed demand, and do not measure utilization. 
+  Teams treat optimization as a project with an end date. Gains erode as demand and features change. Right-sizing skips validation. 
+  Efficiency work focuses only on compute, leaving storage and networking unexamined. 
+  Teams use AI and machine learning extensively to solve problems that a less resource-intensive approach or a smaller machine learning model could solve. 