# Instance selection best practices for Amazon ECS Managed Instances

Selecting the right instance configuration for your Amazon ECS Managed Instances workloads is crucial for optimizing performance, cost, and resource utilization. Amazon ECS provides flexible instance selection options that allow you to balance your application requirements with cost efficiency. The following best practices help you make informed decisions about instance selection for your containerized workloads.

1. Use the Amazon ECS Managed Instances default capacity provider

Amazon ECS chooses the most cost-effective instances that meet the following task definition and service parameter requirements:

Task definition

    * operatingSystemFamily
    * cpuArchitecture
    * cpu
    * memory

Service definition

    * placementConstraints
    * placementStrategy

2. Use attribute-based selection for most workloads to provide flexibility and improve placement success rates

Attribute-based instance selection allows Amazon ECS to choose from a broader range of instance types that meet your specified requirements. This approach increases the likelihood of successful task placement and provides better cost optimization by allowing Amazon ECS to select the most cost-effective instances available at launch time. 3. Use specific instance types only when applications have specific hardware requirements

Reserve specific instance type selection for workloads that require particular hardware features, such as GPU acceleration, high-frequency processors, or specialized networking capabilities. For general-purpose applications, attribute-based selection typically provides better flexibility and cost optimization. 4. Choose balanced resources to avoid over-provisioning and unnecessary costs

Select instance configurations that closely match your application's CPU and memory requirements. Avoid significantly over-provisioning resources, as this leads to higher costs and reduced efficiency. Use monitoring data to understand your actual resource utilization patterns and adjust instance selection accordingly. 5. Mix instance types for applications with varying workloads to balance performance and cost

For applications with diverse performance requirements or varying workload patterns, consider using multiple capacity providers with different instance configurations. This approach allows you to optimize costs by using appropriate instance types for different components of your application while maintaining performance where needed. 6. When using an Amazon ECS Managed Instances capacity provider configured with `capacityOptionType=Reserved`, be aware that ECS services use a default deployment configuration of `minimumHealthyPercent=100%` and `maximumPercent=200%`, meaning ECS deployments attempt to start new tasks before stopping old ones and temporarily require up to 200% of your steady-state capacity. If your service consumes all available capacity in your EC2 Capacity Reservations at steady state, deployments will fail because there is no additional capacity available to launch new tasks during the deployment process. To avoid this, set `minimumHealthyPercent` to less than 100% (e.g., 75%) and consider setting `maximumPercent` to 100% to ensure the service stops tasks before starting new ones, allowing deployments to complete successfully by freeing capacity before launching replacement tasks. Additionally, consider monitoring your capacity utilization regularly to maintain headroom in your reservations to accommodate deployments and handle traffic spikes.
