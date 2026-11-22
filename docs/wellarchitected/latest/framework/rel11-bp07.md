

# REL11-BP07 Architect your product to meet availability targets and uptime service level agreements (SLAs)

 If you publish or privately commit to an availability target or uptime SLA, build your architecture and operations to support it from the start. Define the target during design, and let it drive the technology choices and trade-offs. 

 **Desired outcome:** 
+  Each workload has a defined availability target and SLA for its performance metrics. 
+  Those targets are set during design and used to guide architectural decisions and trade-offs. 
+  You monitor and report against the targets so you can confirm the workload meets them. 
+  Dependency SLAs are accounted for, and dependencies are chosen with availability equal to or greater than the workload's target. 

 **Common anti-patterns:** 
+  Teams design and deploy workloads without setting any availability target or SLA. 
+  Teams set SLA metrics high without a business rationale. 
+  Teams set SLAs without accounting for the SLAs of underlying dependencies. 
+  Teams design applications without considering the shared responsibility model for resilience. 

 **Benefits of establishing this best practice:** 
+  Designing to explicit resilience targets keeps the workload aligned with business objectives and customer expectations. 
+  Targets give the design process a concrete basis for evaluating technologies and trade-offs. 
+  Monitoring against a defined SLA turns availability from an assumption into a measured fact. 
+  Accounting for dependency SLAs prevents a workload from promising more availability than its dependencies can deliver. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Consider resilience targets at the beginning of the design process due to their significant impact. A workload derives its requirements from business, operational, and financial objectives, and the availability target translates those objectives into a number the architecture must hit. Set the target during design, and use it as the yardstick for trade-offs between complexity, performance, scaling, and cost. Each workload gets its own target, because a batch reporting system and a payment path have very different tolerances for downtime. 

 Availability composes across dependencies. A workload can be no more available than the dependencies it must call to serve a request, and calling several dependencies multiplies their individual failure rates into a lower combined availability. This is why dependency selection is an availability decision: choose dependencies whose availability goals equal or exceed your own, and reduce the number of hard dependencies on the request path. Loose coupling lets a workload keep functioning when a dependency is impaired. Reducing control plane dependencies during recovery, along with static stability for mission-critical paths, further limits the impact of a dependency failure. 

 Three factors determine availability in a distributed system: failures should happen less often (longer mean time between failures), be detected faster (shorter mean time to detection), and be repaired faster (shorter mean time to repair). Targets should account for all three factors. Observability and instrumentation act directly on the second and third factors, which is why they are prerequisites for meeting an SLA. 

 The shared responsibility model for resilience defines where your obligations begin. AWS operates the resilience of the cloud infrastructure, and you architect for the resilience of what you build on it. Ground your target in the published SLAs of the services you depend on, and in design patterns that raise the maximum achievable availability, such as cell-based architecture and multi-location deployment. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Review and document the workload design:** Capture how the design handles resilience by answering a fixed set of questions. Where are control planes used? How is fault tolerance implemented? What are the patterns for scaling, redundancy, and high availability? What are the data consistency and availability requirements? Where is resource sparing or static stability needed, and what are the service dependencies? 

1.  **Define SLA metrics with stakeholders:** Work with business and operational stakeholders to set SLA metrics based on the workload architecture, and factor in the SLAs of every dependency the workload uses. 

1.  **Optimize the architecture to meet the target:** Once the SLA target is set, adjust the architecture, such as adding redundancy, loose coupling, or static stability, until the design can meet it. 

1.  **Implement operations to reduce MTTD and MTTR:** Put operational changes, process automation, and runbooks in place that shorten detection and repair times, since both directly affect achievable availability. 

1.  **Monitor and report against the SLA:** After deployment, monitor the workload and report on its availability against the defined target so deviations are caught and corrected. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL11-BP01 Monitor all components of the workload to detect failures](rel11-bp01.md) 
+  [REL11-BP03 Automate healing on all layers](rel11-bp03.md) 
+  [REL13-BP01 Define recovery objectives for downtime and data loss](rel13-bp01.md) 
+  [REL03-BP01 Choose how to segment your workload](rel03-bp01.md) 
+  [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md) 

 **Related documents:** 
+  [Availability and recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-availability-and-recovery-objectives.html) 
+  [Availability with redundancy](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-redundancy.html) 
+  [Measuring availability](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/measuring-availability.html) 
+  [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) 
+  [AWS infrastructure](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/aws-infrastructure.html) 
+  [Shared Responsibility Model for Resiliency](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/shared-responsibility-model-for-resiliency.html) 
+  [Static stability using Availability Zones](https://builder.aws.com/content/3K9SiqiJ369TGkkGzqPM95BuYWI/static-stability-using-availability-zones) 
+  [Guidance for cell-based architecture on AWS](https://docs.aws.amazon.com/solutions/cell-based-architecture-on-aws/) 
+  [Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/operational-excellence.html) 
+  [AWS Service Level Agreements](https://aws.amazon.com/legal/service-level-agreements/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 