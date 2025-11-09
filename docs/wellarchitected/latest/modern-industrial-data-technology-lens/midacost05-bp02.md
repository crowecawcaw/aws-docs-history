# MIDACOST05-BP02 Implement dynamic resource provisioning

Enable automated resource scaling that matches manufacturing workload demands while
optimizing costs. This includes implementing warm pools for faster scaling, considering
application warm-up times, and aligning scaling policies with production schedules and peak
processing times.

**Desired outcome:** Automated resource scaling that matches
manufacturing workload demands while optimizing costs.

**Common anti-patterns:**

- Implementing automatic scaling without considering production schedule requirements
- Setting scaling thresholds without consulting manufacturing operations teams
- Using the same scaling policies for both production and non-production workloads
- Neglecting warm-up times for manufacturing applications when scaling
- Implementing aggressive scale-in policies that could impact production monitoring
- Not accounting for data retention requirements when scaling storage resources
- Ignoring the impact of scaling on integrated manufacturing systems
- Setting up dynamic provisioning without consideration for compliance requirements

**Benefits of establishing this best practice:**

- Optimized resource utilization
- Reduced manual intervention
- Cost-efficient scaling
- Improved responsiveness

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- Detailed production schedules and patterns
- Peak resource usage data by workload type
- System warm-up and response time requirements

Key decisions needed:

- Scaling thresholds for different manufacturing workloads
- Resource retention periods based on production needs
- Performance impact limits for critical systems
- Cost optimization targets by workload type

Design your manufacturing workloads to automatically adjust resource provisioning
based on current demand and production schedules. Implement a data-driven approach that
correlates IT resource needs with manufacturing operations, providing appropriate safeguards
for critical production systems and consideration for startup times and warm pools.

### Implementation steps

1. Define scaling metrics:
   - Production demand indicators
   - Resource utilization thresholds
   - Cost constraints

2. Configure auto scaling policies:
   - Scale-out conditions
   - Scale-in conditions
   - Cool-down periods

3. Implement monitoring.
4. Set up cost tracking.
5. Perform regular policy review and optimization.

## Key AWS services

- AWS Auto Scaling
- Amazon EC2 Auto Scaling
- AWS Lambda
- Amazon CloudWatch

## Resources

**Related documents:**

- [AWS Auto Scaling](../../../autoscaling/plans/userguide/what-is-aws-auto-scaling.md "../../../autoscaling/plans/userguide/what-is-aws-auto-scaling.md")
- [Amazon EC2 Auto Scaling User Guide](../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md "../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md")
- [AWS Lambda: Configuring reserved concurrency for a function](../../../lambda/latest/dg/configuration-concurrency.md "../../../lambda/latest/dg/configuration-concurrency.md")
- [AWS Lambda: Configuring provisioned concurrency for a function PDF RSS](../../../lambda/latest/dg/provisioned-concurrency.md "../../../lambda/latest/dg/provisioned-concurrency.md")
- [Amazon CloudWatch: Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
- [Predictive scaling for Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.md")
