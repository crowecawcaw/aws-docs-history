# REL07-BP02 Obtain resources upon detection of impairment to a

workload

Scale resources reactively when necessary if availability is
impacted, to restore workload availability.

You first must configure health checks and the criteria on these
checks to indicate when availability is impacted by lack of
resources. Then, either notify the appropriate personnel to manually
scale the resource, or start automation to automatically scale it.

Scale can be manually adjusted for your workload (for example,
changing the number of EC2 instances in an Amazon EC2 Auto Scaling group, or
modifying throughput of a DynamoDB table through the AWS Management Console or AWS CLI). However, automation should be used
whenever possible (refer to **Use automation
when obtaining or scaling resources**).

**Desired outcome:** Scaling activities (either automatically or manually) are initiated to restore availability upon detection of a failure or degraded customer experience.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement observability and monitoring across all components in your workload, to monitor customer experience and detect failure. Define the procedures, manual or automated, that scale the required resources. o For more information, see [REL11-BP01 Monitor all components of the workload to detect failures](rel_withstand_component_failures_monitoring_health.md "rel_withstand_component_failures_monitoring_health.md").

### Implementation steps

- Define the procedures, manual or automated, that scale the required resources.
  - Scaling procedures depend on how the different components within your workload are designed.
  - Scaling procedures also vary depending on the underlying technology utilized.
    - Components using AWS Auto Scaling can use scaling plans to configure a set of instructions for scaling your resources. If you work with AWS CloudFormation or add tags to AWS resources, you can set up scaling plans for different sets of resources per application. Amazon EC2 Auto Scaling provides recommendations for scaling strategies customized to each resource. After you create your scaling plan, Amazon EC2 Auto Scaling combines dynamic scaling and predictive scaling methods together to support your scaling strategy. For more detail, see [How scaling plans work](../../../autoscaling/plans/userguide/how-it-works.md "../../../autoscaling/plans/userguide/how-it-works.md").
    - Amazon EC2 Auto Scaling verifies that you have the correct number of Amazon EC2 instances available to handle the load for your application. You create collections of EC2 instances, called Amazon EC2 Auto Scaling groups. You can specify the minimum and maximum number of instances in each Amazon EC2 Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes below or above these limits. For more detail, see [What is Amazon EC2 Auto Scaling?](../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md "../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md")
    - Amazon DynamoDB auto scaling uses the Application Auto Scaling service to dynamically adjust provisioned throughput capacity on your behalf, in response to actual traffic patterns. This allows a table or a global secondary index to increase its provisioned read and write capacity to handle sudden increases in traffic, without throttling. For more detail, see [Managing throughput capacity automatically with DynamoDB auto scaling](../../../amazondynamodb/latest/developerguide/AutoScaling.md "../../../amazondynamodb/latest/developerguide/AutoScaling.md").

## Resources

**Related best practices:**

- [REL07-BP01 Use automation when obtaining or scaling resources](rel_adapt_to_changes_autoscale_adapt.md "rel_adapt_to_changes_autoscale_adapt.md")
- [REL11-BP01 Monitor all components of the workload to detect failures](rel_withstand_component_failures_monitoring_health.md "rel_withstand_component_failures_monitoring_health.md")

**Related documents:**

- [AWS Auto Scaling: How Scaling Plans Work](../../../autoscaling/plans/userguide/how-it-works.md "../../../autoscaling/plans/userguide/how-it-works.md")
- [Managing
  Throughput Capacity Automatically with DynamoDB Auto
  Scaling](../../../amazondynamodb/latest/developerguide/AutoScaling.md "../../../amazondynamodb/latest/developerguide/AutoScaling.md")
- [What
  Is Amazon EC2 Auto Scaling?](../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md "../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md")
