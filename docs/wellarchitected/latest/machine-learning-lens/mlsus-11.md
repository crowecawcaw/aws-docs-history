# MLSUS-11: Align SLAs with sustainability goals

Define service level agreements (SLAs) that support your
sustainability goals while meeting your business requirements.
Define SLAs to meet your business requirements, not exceed them.
Make trade-offs that significantly reduce environmental impacts
in exchange for acceptable decreases in service levels.

## Implementation plan

- **Queue incoming requests and
  process them asynchronously** - If your users can
  tolerate some latency, deploy your model on
  [serverless](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md")
  or
  [asynchronous
  endpoints](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md") to
  [reduce
  resources that are idle between tasks and minimize the
  impact of load spikes](../sustainability-pillar/optimize-software-and-architecture-for-asynchronous-and-scheduled-jobs.md "../sustainability-pillar/optimize-software-and-architecture-for-asynchronous-and-scheduled-jobs.md"). These options will
  automatically scale the instance or endpoint count to zero
  when there are no requests to process, so you only
  maintain an inference infrastructure when your endpoint is
  processing requests.
- **Adjust availability** -
  If your users can tolerate some latency in the rare case
  of a failover, don't provision extra capacity. If an
  outage occurs or an instance fails, Amazon SageMaker AI
  [automatically
  attempts to distribute your instances across Availability
  Zones](../../../sagemaker/latest/dg/deployment-best-practices.md#deployment-best-practices-availability-zones "../../../sagemaker/latest/dg/deployment-best-practices.md#deployment-best-practices-availability-zones"). Adjusting availability is an example of a
  [conscious
  trade off](../sustainability-pillar/sustainability-as-a-non-functional-requirement.md "../sustainability-pillar/sustainability-as-a-non-functional-requirement.md") you can make to meet your sustainability
  targets.
- **Adjust response time** -
  When you don't need real-time inference, use
  [SageMaker AI
  Batch Transform](../../../sagemaker/latest/dg/batch-transform.md "../../../sagemaker/latest/dg/batch-transform.md"). Unlike a persistent endpoint,
  clusters are decommissioned when batch transform jobs
  finish so you don't continuously maintain an inference
  infrastructure.

## Documents

- [Amazon SageMaker AI Asynchronous inference](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md")
- [Amazon SageMaker AI Batch Transform](../../../sagemaker/latest/dg/batch-transform.md "../../../sagemaker/latest/dg/batch-transform.md")
- [Optimize
  software and architecture for asynchronous and scheduled
  jobs](../sustainability-pillar/optimize-software-and-architecture-for-asynchronous-and-scheduled-jobs.md "../sustainability-pillar/optimize-software-and-architecture-for-asynchronous-and-scheduled-jobs.md")
- [Best
  practices for deploying models on SageMaker AI Hosting
  Services](../../../sagemaker/latest/dg/deployment-best-practices.md "../../../sagemaker/latest/dg/deployment-best-practices.md")
- [Align
  SLAs with sustainability goals](../sustainability-pillar/align-slas-with-sustainability-goals.md "../sustainability-pillar/align-slas-with-sustainability-goals.md")
- [Sustainability
  as a non-functional requirement](../sustainability-pillar/sustainability-as-a-non-functional-requirement.md "../sustainability-pillar/sustainability-as-a-non-functional-requirement.md")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 3, deployment and
  monitoring](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/")

## Videos

- [AWS re:Invent 2021 - Architecting for sustainability](https://youtu.be/3-Zq2W1-odU?t=1872 "https://youtu.be/3-Zq2W1-odU?t=1872") -
  Optimize capacity for Sustainability
