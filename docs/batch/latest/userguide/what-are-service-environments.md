# What are service environments in

AWS Batch

A service environment is a AWS Batch resource that contains the configuration parameters
required to integrate AWS Batch with SageMaker AI. Service environments enable AWS Batch to submit and
manage SageMaker Training jobs while providing AWS Batch's queuing, scheduling, and priority
management capabilities.

Service environments address common challenges that data science teams face when managing
machine learning workloads. Organizations often limit the number of instances available for
training models to prevent accidental overspending, meet budget constraints, save costs with
reserved instances, or use specific instance types for workloads. However, data scientists
may want to run more workloads concurrently than is possible with their allocated instances,
requiring manual coordination to decide which workloads run when.

This coordination challenge impacts organizations of all sizes, from teams with just a few
data scientists to large-scale operations. As organizations grow, the complexity increases,
requiring more time to manage workload coordination and often necessitating infrastructure
administrator involvement. These manual efforts waste time and reduce instance efficiency,
resulting in real costs for customers.

With service environments, data scientists and ML engineers can submit SageMaker Training
jobs with priorities to configurable queues, ensuring workloads run automatically without
intervention as soon as resources are available. This integration leverages AWS Batch's
extensive queuing and scheduling capabilities, enabling customers to customize their queuing
and scheduling policies to match their organization's goals.

## How service environments work with

other AWS Batch components

Service environments integrate with other AWS Batch components to enable SageMaker Training
job queuing:

- **Job queues** - Service environments are
  associated with job queues to enable the queue to process service jobs for
  SageMaker Training job
- **Service jobs** - When you submit a service job
  to a queue associated with a service environment, AWS Batch uses the environment's
  configuration to submit the corresponding SageMaker Training job
- **Scheduling policies** - Service environments
  work with AWS Batch scheduling policies to prioritize and manage the execution
  order of SageMaker Training jobs

This integration allows you to leverage AWS Batch's mature queuing and scheduling
capabilities while maintaining the full functionality and flexibility of SageMaker Training
jobs.

## Best practices for service

environments

Service environments provide capabilities for managing SageMaker Training jobs at scale.
Following these best practices helps you optimize cost, performance, and operational
efficiency while avoiding common configuration issues that can impact your machine
learning workflows.

When planning service environment capacity, consider the specific quotas and limits
that apply to SageMaker Training job queuing. Each service environment has a maximum capacity
limit expressed in number of instances, which directly controls how many SageMaker Training
jobs can run concurrently. Understanding these limits helps prevent resource contention
and ensures predictable job execution times.

Optimal service environment performance depends on understanding the unique
characteristics of SageMaker Training job scheduling. Unlike traditional containerized jobs,
service jobs transition through a `SCHEDULED` state while SageMaker AI acquires and provisions the
necessary training instances. This means job start times can vary significantly based on
instance availability and regional capacity.

###### Important

Service environments have specific quotas that can impact your ability to scale
SageMaker Training workloads. You can create up to 50 service environments per account,
with each job queue supporting only one associated service environment.
Additionally, the Service Request Payload for individual jobs is limited to 10 KiB,
and the `SubmitServiceJob` API is limited to 5 transactions per second per account.
Understanding these limits during capacity planning prevents unexpected scaling
constraints.

Effective monitoring of service environments requires attention to both AWS Batch and
SageMaker AI service metrics. [Job state transitions](service-job-status.md "service-job-status.md") provide valuable insights into system
performance, particularly the time spent in `SCHEDULED` state, which indicates capacity
availability patterns. Service environments maintain their own lifecycle states similar
to compute environments, transitioning through `CREATING`, `VALID`, `INVALID`, and `DELETING`
states that should be monitored for operational health. Organizations with mature
monitoring practices typically track queue depth, job completion rates, and instance
utilization patterns to optimize their service environment configurations over
time.
