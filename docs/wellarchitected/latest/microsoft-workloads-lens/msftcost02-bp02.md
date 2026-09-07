

# MSFTCOST02-BP02 Automate stop and start schedules
<a name="msftcost02-bp02"></a>

 Leverage the Instance Scheduler on AWS to reduce the use of Amazon EC2 and Amazon Relational Database Service instances that do not need to run continuously. The Instance Scheduler helps reduce operational costs by stopping and starting resources as needed. 

 **Desired outcome:** Achieve significant cost reduction in non-production environments by implementing automated start/stop schedules for EC2 instances and RDS databases that are only required during business hours (for example, 8 AM - 6 PM on weekdays), while ensuring zero impact to business operations and development activities during working hours. 

 **Common anti-patterns:** 
+  Always-On Resources: Keeping all development, testing, and staging environments running 24/7, even when they're not actively used, resulting in unnecessary costs and resource waste. 
+  Manual Start/Stop Management: Relying on developers or operations teams to manually start and stop instances based on their work schedules, leading to inconsistent resource management, potential delays in availability, and increased risk of human error. 

 **Benefits of establishing this best practice:** 
+  Cost Optimization: Significant reduction in operational costs by automatically shutting down non-essential resources during off-hours, weekends, and holidays, directly impacting the organization's cloud spending. 
+  Operational Efficiency: Elimination of manual intervention for resource management, allowing IT teams to focus on more strategic tasks while ensuring consistent and reliable resource availability when needed. 
+  Environmental Impact: Reduced energy consumption and carbon footprint by minimizing unnecessary compute resource usage, supporting organizational sustainability goals and responsible cloud computing practices. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Begin by identifying and tagging non-production resources suitable for automated scheduling. Configure AWS Instance Scheduler with appropriate start/stop periods aligned with business hours and team schedules. Implement a gradual rollout strategy, starting with a small subset of resources to validate functionality. Establish monitoring mechanisms to track schedule execution and create override procedures for exceptional situations. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Identify and tag non-production resources for scheduling 

1.  Install and configure AWS Instance Scheduler 

1.  Define business hours and create scheduling periods 

1.  Test schedule on pilot group of resources 

1.  Monitor and validate functionality 

1.  Roll out to remaining resources 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Automate stop and start schedules](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/windows-ec2-schedules.html) 

 **Related tools:** 
+  [Instance Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/) 