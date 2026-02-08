# MSFTPERF01-BP02 Consider Amazon managed container orchestrator

services to run containers on AWS

Amazon Elastic Kubernetes Service (EKS), Amazon Elastic Container Service (ECS), and AWS Fargate support both Linux and Windows
containers. Either running cross-platform .NET on Linux or .NET
Framework on Windows, you can run your Microsoft
container-compatible workload taking advantage of the benefits of
the managed service, improving performance efficiency.

**Desired outcome:** Achieve improved
performance efficiency and operational simplicity for Microsoft
workloads by leveraging managed container orchestration services
that provide automated scaling, resource optimization, and reduced
infrastructure management overhead while supporting both Windows and
Linux container deployments.

**Common anti-patterns:**

- Running containerized Microsoft applications on self-managed
  container platforms without leveraging AWS managed services,
  increasing operational complexity and missing optimization
  opportunities.
- Choosing container orchestration without considering workload
  characteristics, leading to over-engineered solutions for simple
  applications or under-powered platforms for complex distributed
  systems.
- Implementing containers without proper resource allocation and
  scaling policies, resulting in performance issues or resource
  waste.
- Microsoft workloads on self-managed container orchestration
  platforms may limit the availability of AWS services and
  features that are designed to simplify the deployment and
  management of these workloads.

**Benefits of establishing this best
practice:**

- Enhanced scalability and resource utilization through managed
  container orchestration that automatically optimizes resource
  allocation and scaling based on workload demands.
- Reduced operational overhead through AWS-managed control planes,
  automated updates, and integrated monitoring capabilities.
- Improved deployment flexibility supporting both Windows and
  Linux containers for different Microsoft workload components.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing managed container orchestration for Microsoft
workloads requires careful evaluation of your application
architecture and container requirements. Choose the appropriate
service based on your complexity needs and operational
preferences, then configure for optimal performance and
efficiency.

### Implementation steps

1. Assess your Microsoft applications for containerization
   readiness and determine Windows versus Linux container
   requirements.
2. Choose between EKS, ECS, or Fargate based on complexity,
   control requirements, and operational preferences.
3. Configure container resource allocation, scaling policies,
   and networking for optimal performance.
4. Implement container image optimization and security scanning
   processes.
5. Set up monitoring and logging integration with Amazon CloudWatch Container Insights.
6. Establish CI/CD pipelines for automated container deployment
   and updates.

## Resources

**Related documents:**

- [Windows
  in Kubernetes](https://kubernetes.io/docs/concepts/windows/ "https://kubernetes.io/docs/concepts/windows/")
- [Deploy
  Windows nodes on EKS clusters](../../../eks/latest/userguide/windows-support.md "../../../eks/latest/userguide/windows-support.md")
- [Launching
  an Amazon ECS Windows container instance](../../../AmazonECS/latest/developerguide/launch_window-container_instance.md "../../../AmazonECS/latest/developerguide/launch_window-container_instance.md")
- [Windows
  Containers Isolation Modes](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container "https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container")
- [Windows
  containers on AWS](https://aws.amazon.com/blogs/containers/tag/windows/ "https://aws.amazon.com/blogs/containers/tag/windows/")

**Related tools:**

- [Amazon Elastic Kubernetes Service Documentation](../../../eks.md "../../../eks.md")
- [Amazon Elastic Container Service Documentation](../../../ecs.md "../../../ecs.md")
- [Simplify
  compute management with AWS Fargate](../../../eks/latest/userguide/fargate.md "../../../eks/latest/userguide/fargate.md")
