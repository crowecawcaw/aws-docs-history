# TELCOREL02-BP03 Implement a flexible network function (NF)

design to leverage available infrastructure resources for autoscaling

Designing a flexible network function design enables the telecom network to dynamically
scale its resources based on the availability of suitable instance types in the deployment
region. This approach avoids issues like `Insufficient Capacity Error` that can occur when
the required instance type is not available, by using alternative instance types that
can be provisioned. The architecture should be able to automatically adapt to the most
suitable instance types that are present, allowing the network to scale up or down as needed
without being constrained by the availability of a specific instance configuration.

**Desired outcome:**

- Improving the probability of a successful on-demand scale-out in case of traffic surge
  or failover trigger.
- Network functions can scale seamlessly by utilizing the most suitable instance types
  that are available in the deployment region.
- Remove the risk of scaling failures due to `Insufficient Capacity Error` when
  the preferred instance type is not available.
- Verifies continued service availability and responsiveness by maintaining the ability
  to scale the network functions as needed.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

To build a flexible and scalable telecom network architecture, a modular and
containerized approach to network functions is recommended. This involves decomposing network
functions into independently scalable components, packaged as container images, and
orchestrating them on a Kubernetes-based solution. Dynamic scaling and efficient resource
utilization are enabled using a Kubernetes cluster autoscaler, which provisions appropriate
instance types based on component requirements. Flexible scaling policies, comprehensive
monitoring, failover mechanisms, and thorough documentation verify the network can adapt to
changing demands, optimize resource utilization, and maintain overall resilience and
reliability.

### Implementation steps

- Design a modular and containerized network function architecture:
  - Use a microservices-based approach to decompose network functions into smaller,
    independently scalable components.
  - Package each network function component as a container image to enable
    flexibility in deployment and scaling.

- Implement Kubernetes-based orchestration for network functions:
  - Deploy the network function components on Amazon EKS.
  - Integrate the Karpenter open-source Kubernetes cluster autoscaler with your EKS
    cluster.
  - Configure Karpenter to automatically provision the appropriate instance types
    based on the resource requirements of the network function components.

- Monitor resource utilization and scaling events:
  - Use Amazon CloudWatch to monitor the performance and resource utilization of the network
    function components.
  - Analyze scaling events, instance provisioning, and capacity fluctuations to
    optimize the scaling policies and Karpenter configurations.

- Implement failover and self-healing mechanisms:
  - Configure Kubernetes health checks and readiness probes to detect and replace
    unhealthy network function instances.

- Document scaling procedures and best practices:
  - Maintain comprehensive documentation on the flexible network function
    architecture, scaling policies, and Karpenter configuration.
  - Establish guidelines for updating the scaling policies and Karpenter
    configurations as the instance type availability changes over time.

## Resources

**Key AWS services:**

- [Amazon EKS (Elastic Kubernetes Service)](https://aws.amazon.com/pm/eks/ "https://aws.amazon.com/pm/eks/")
- [Karpenter
  (open-source Kubernetes cluster autoscaler)](../../../eks/latest/userguide/autoscaling.md "../../../eks/latest/userguide/autoscaling.md")
- [Amazon CloudWatch for monitoring and
  observability](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
