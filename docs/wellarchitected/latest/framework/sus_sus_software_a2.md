# SUS03-BP01 Optimize software and architecture for asynchronous

and scheduled jobs

Use efficient software and architecture patterns such as queue-driven to
maintain consistent high utilization of deployed resources.

**Common anti-patterns:**

- You overprovision the resources in your cloud workload to meet unforeseen spikes in demand.
- Your architecture does not decouple senders and receivers of asynchronous messages by a messaging component.

**Benefits of establishing this best practice:**

- Efficient software and architecture patterns minimize the unused resources in your workload and improve the overall efficiency.
- You can scale the processing independently of the receiving of asynchronous messages.
- Through a messaging component, you have relaxed availability requirements that you can meet with fewer resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Use efficient architecture patterns such as [event-driven architecture](https://aws.amazon.com/event-driven-architecture/ "https://aws.amazon.com/event-driven-architecture/") that result in
even utilization of components and minimize overprovisioning in your workload. Using
efficient architecture patterns minimizes idle resources from lack of use due to changes
in demand over time.

Understand the requirements of your workload components and adopt architecture patterns
that increase overall utilization of resources. Retire components that are no longer required.

### Implementation steps

- Analyze the demand for your workload to determine how to respond to those.
- For requests or jobs that don’t require synchronous responses, use queue-driven
  architectures and auto scaling workers to maximize utilization. Here are some
  examples of when you might consider queue-driven architecture:

| Queuing mechanism                                                                                                                                                                                                                                                                                                | Description                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| [AWS Batch job queues](../../../batch/latest/userguide/job_queues.md "../../../batch/latest/userguide/job_queues.md")                                                                                                                                                                                            | AWS Batch jobs are submitted to a job queue where<br>they reside until they can be scheduled to run in a<br>compute environment. |
| [Amazon Simple Queue Service and Amazon EC2 Spot Instances](https://aws.amazon.com/blogs/compute/running-cost-effective-queue-workers-with-amazon-sqs-and-amazon-ec2-spot-instances/ "https://aws.amazon.com/blogs/compute/running-cost-effective-queue-workers-with-amazon-sqs-and-amazon-ec2-spot-instances/") | Pairing Amazon SQS and Spot Instances to build fault tolerant and efficient architecture.                                        |

- For requests or jobs that can be processed anytime, use scheduling mechanisms
  to process jobs in batch for more efficiency. Here are some examples of scheduling
  mechanisms on AWS:

| Scheduling mechanism                                                                                                                                                                            | Description                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Amazon EventBridge Scheduler](https://aws.amazon.com/blogs/compute/introducing-amazon-eventbridge-scheduler/ "https://aws.amazon.com/blogs/compute/introducing-amazon-eventbridge-scheduler/") | A capability from [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") that allows you to create, run, and manage scheduled tasks at scale. |
| [AWS Glue time-based schedule](../../../glue/latest/dg/monitor-data-warehouse-schedule.md "../../../glue/latest/dg/monitor-data-warehouse-schedule.md")                                         | Define a time-based schedule for your crawlers and jobs in AWS Glue.                                                                                                                   |
| [Amazon Elastic Container Service (Amazon ECS) scheduled tasks](../../../AmazonECS/latest/developerguide/scheduled_tasks.md "../../../AmazonECS/latest/developerguide/scheduled_tasks.md")      | Amazon ECS supports creating scheduled tasks. Scheduled tasks use Amazon EventBridge rules to run tasks either on a schedule or in a response to an EventBridge event.                 |
| [Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/ "https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/")                 | Configure start and stop schedules for your Amazon EC2 and Amazon Relational Database Service instances.                                                                               |

- If you use polling and webhooks mechanisms in your architecture, replace those with events.
  Use [event-driven architectures](../../../lambda/latest/operatorguide/event-driven-architectures.md "../../../lambda/latest/operatorguide/event-driven-architectures.md") to build highly efficient workloads.
- Leverage [serverless on AWS](https://aws.amazon.com/serverless/ "https://aws.amazon.com/serverless/") to eliminate over-provisioned infrastructure.
- Right size individual components of your architecture to prevent idling resources waiting for input.
  - You can use the [Rightsizing Recommendations in AWS Cost Explorer](../../../cost-management/latest/userguide/ce-rightsizing.md "../../../cost-management/latest/userguide/ce-rightsizing.md") or [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/") to identify rightsizing opportunities.
  - For more detail, see [Right Sizing: Provisioning Instances to Match Workloads](../../../whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.md "../../../whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.md").

## Resources

**Related documents:**

- [What
  is Amazon Simple Queue Service?](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md")
- [What
  is Amazon MQ?](../../../amazon-mq/latest/developer-guide/welcome.md "../../../amazon-mq/latest/developer-guide/welcome.md")
- [Scaling
  based on Amazon SQS](../../../autoscaling/ec2/userguide/as-using-sqs-queue.md "../../../autoscaling/ec2/userguide/as-using-sqs-queue.md")
- [What
  is AWS Step Functions?](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md")
- [What
  is AWS Lambda?](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md")
- [Using
  AWS Lambda with Amazon SQS](../../../lambda/latest/dg/with-sqs.md "../../../lambda/latest/dg/with-sqs.md")
- [What
  is Amazon EventBridge?](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md")
- [Managing Asynchronous Workflows with a REST API](https://aws.amazon.com/blogs/architecture/managing-asynchronous-workflows-with-a-rest-api/ "https://aws.amazon.com/blogs/architecture/managing-asynchronous-workflows-with-a-rest-api/")

**Related videos:**

- [AWS re:Invent 2023 - Navigating the journey to serverless event-driven architecture](https://www.youtube.com/watch?v=hvGuqHp051c "https://www.youtube.com/watch?v=hvGuqHp051c")
- [AWS re:Invent 2023 - Using serverless for event-driven architecture & domain-driven design](https://www.youtube.com/watch?v=3foMZJSPMI4 "https://www.youtube.com/watch?v=3foMZJSPMI4")
- [AWS re:Invent 2023 - Advanced event-driven patterns with Amazon EventBridge](https://www.youtube.com/watch?v=6X4lSPkn4ps "https://www.youtube.com/watch?v=6X4lSPkn4ps")
- [AWS re:Invent 2023 - Sustainable architecture: Past, present, and future](https://www.youtube.com/watch?v=2xpUQ-Q4QcM "https://www.youtube.com/watch?v=2xpUQ-Q4QcM")
- [Asynchronous Message Patterns | AWS Events](https://www.youtube.com/watch?v=-yJqBuwouZ4 "https://www.youtube.com/watch?v=-yJqBuwouZ4")

**Related examples:**

- [Event-driven architecture with AWS Graviton Processors and Amazon EC2 Spot Instances](https://catalog.workshops.aws/well-architected-sustainability/en-US/2-software-and-architecture/event-driven-architecture-with-graviton-spot "https://catalog.workshops.aws/well-architected-sustainability/en-US/2-software-and-architecture/event-driven-architecture-with-graviton-spot")
