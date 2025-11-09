# MIDACOST05-BP01 Implement a buffering or throttling approach

Implement balanced resource utilization that handles varying workload demands while
maintaining cost efficiency for manufacturing systems. This includes prioritizing critical
processes while queuing less time-sensitive tasks and implementing appropriate scaling
triggers aligned with production cycles.

**Desired outcome:** Balanced resource utilization that handles
varying workload demands while maintaining cost efficiency.

**Common anti-patterns:**

- Implementing throttling on time-critical manufacturing processes
- Using the same buffering strategy for all types of industrial data
- Overlooking real-time requirements of production monitoring systems
- Setting queue limits without considering production batch sizes
- Implementing aggressive throttling that impacts quality data collection
- Not accounting for upstream and downstream dependencies in manufacturing processes
- Using standard IT buffering patterns without adapting to manufacturing needs

**Benefits of establishing this best practice:**

- Controlled resource consumption
- Avoided system overload
- Optimized costs during peak periods
- Improved system stability

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- Documented critical and non-critical manufacturing processes
- Peak resource utilization patterns for different production phases
- Response time requirements for various manufacturing systems

Key decisions needed:

- Resource allocation priorities for critical vs. non-critical processes
- Throttling thresholds for different types of manufacturing workloads
- Queue configurations for deferrable processes
- Scaling triggers aligned with production cycles and peaks

Implement buffering and throttling mechanisms to manage cloud resource utilization
during manufacturing peaks. Design a system that prioritizes critical processes (for
example, real-time monitoring, quality control) for immediate resource access, while queuing
less time-sensitive tasks (for example, batch analytics, report generation). Use
auto-scaling for baseline capacity but implement throttling to help prevent non-critical
tasks from consuming resources needed for production-critical operations.

Consider the following:

- Using Spot Instances for interruptible, non-critical workloads
- Implementing reserved capacity for predictable, critical processes
- Using serverless technologies for sporadic, scalable tasks

Regularly review and adjust your buffering and throttling strategies based on changing
production patterns and business needs.

### Implementation steps

- Identify and categorize manufacturing workloads:
  - Critical real-time processes (for example, process control, safety systems)
  - Time-sensitive operations (for example, quality inspections, inventory
    updates)
  - Deferrable tasks (for example, long-term analytics, reporting)

- Design resource allocation strategies:
  - Priority-based access for critical systems
  - Queueing mechanisms for non-critical operations
  - Load balancing across production lines or facilities

- Implement OT-aware monitoring:
  - Set up real-time monitoring for critical production KPIs
  - Configure alerts based on manufacturing thresholds
  - Integrate with SCADA or MES for comprehensive visibility

- Establish OT-IT integrated scaling mechanisms:
  - Automatic scaling triggered by production volumes
  - Resource reservation for planned production increases
  - Gradual scale-down aligned with shift changes or maintenance windows

- Conduct regular performance and cost reviews:
  - Analyze resource utilization against production output
  - Identify opportunities for optimization without impacting OT
  - Adjust strategies based on changing manufacturing requirements

- Implement feedback loops with shop floor:
  - Gather input from operators on system performance
  - Align IT resource adjustments with production schedules
  - Continuously refine based on real-world manufacturing impact

## Key AWS services

- Amazon SQS
- Amazon Kinesis
- AWS Auto Scaling
- Amazon API Gateway

## Resources

**Related documents:**

- [Amazon Simple Queue Service](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md")
- [Amazon Kinesis Data Streams Developer Guide](../../../streams/latest/dev/introduction.md "../../../streams/latest/dev/introduction.md")
- [AWS Auto Scaling](../../../autoscaling/plans/userguide/what-is-aws-auto-scaling.md "../../../autoscaling/plans/userguide/what-is-aws-auto-scaling.md")
- [Throttle requests to your REST APIs for better throughput in API Gateway](../../../apigateway/latest/developerguide/api-gateway-request-throttling.md "../../../apigateway/latest/developerguide/api-gateway-request-throttling.md")
