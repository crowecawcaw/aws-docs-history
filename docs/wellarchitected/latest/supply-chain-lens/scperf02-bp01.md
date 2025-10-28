# SCPERF02-BP01 Use serverless compute to run tasks

Choosing the correct compute power for the workload provides
smooth performance of the application, not only for the end users
also for the solution developer community to maintain the software
stacks across various infrastructures.

**Desired outcome:** Smooth
performance that elastic in nature with low upkeep.

**Benefits of establishing this best
practice:** Improved user experience, maintenance of
software stack, and scalability.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Some supply chain services computing workloads, like supplier
data visibility, are typically loosely coupled and can benefit
from event-driven architectures using the scaling capacity of
AWS serverless compute options like AWS Lambda and AWS Fargate,
combined with messaging services including Amazon SQS and Amazon EventBridge to decouple components. These serverless solutions
minimize the overhead of capacity management, automatically
scaling in or out to meet demands. Where scale is the primary
factor, AWS serverless container compute engine AWS Fargate, can
be used with both Amazon Elastic Container Service (Amazon ECS)
and Amazon Elastic Kubernetes Service (Amazon EKS), removing the
overhead of managing and provisioning compute resources.

### Implementation steps

1. Identify supply chain workloads that are suitable for
   serverless architectures, focusing on event-driven and
   loosely coupled processes.
2. Implement AWS Lambda functions for lightweight,
   short-duration tasks such as data processing and API
   integrations.
3. Deploy AWS Fargate for containerized workloads that
   require more control over the runtime environment while
   maintaining serverless benefits.
4. Integrate messaging services like Amazon SQS and Amazon EventBridge to decouple components and enable asynchronous
   processing.
5. Configure auto-scaling policies to automatically adjust
   compute resources based on demand patterns and workload
   requirements.
6. Monitor performance metrics and optimize function
   configurations to facilitate efficient resource
   utilization and cost-effectiveness.
