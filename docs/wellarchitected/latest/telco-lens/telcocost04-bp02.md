# TELCOCOST04-BP02 Use ETSI ENI based architectures to implement intelligent network

slicing

The European Telecommunications Standards Institute (ETSI) Experiential Networked
Intelligence (ENI) is an architectural framework that defines standards for cognitive network
management and implementation of 5G use cases based on environmental context and user
requirements. It allows Telcos to take advantage of cloud-based technologies like network
slicing, service mesh, and microservices to build more agile and automated networks.

**Desired outcome:**

- Improve network resource utilization and efficiency through dynamic, context-aware
  network slicing.
- Enhance the customer experience by automatically allocating network resources based
  on user and application requirements.
- Achieve cost savings by right-sizing network capacity to match evolving demands.

**Common anti-patterns:**

- Static, one-size-fits-all network provisioning without considering variable user and
  application needs.
- Lack of real-time visibility into network conditions and user/application demands.
- Inability to rapidly adapt network resource allocation in response to changing
  requirements.

**Benefits of establishing this best practice:**

- Optimized network resource utilization and efficiency.
- Improved customer experience through tailored network capabilities.
- Reduced network operating costs by aligning capacity with actual demands.
- Increased network agility and responsiveness to evolving requirements.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

The European Telecommunications Standards Institute (ETSI) Experiential Networked
Intelligence (ENI) architecture provides a framework for implementing intelligent,
context-aware network slicing. By using the key components of the ENI architecture,
such as the policy management function and the context awareness function, telecoms can
build cloud-based, microservices-based network slicing solutions that dynamically allocate
resources based on user and application needs.

This approach enables telecoms to improve network resource utilization and
cost-effectiveness by right-sizing network capacity to match actual demands, rather than
provisioning for peak requirements. Additionally, the context-aware nature of the ENI
architecture allows the network to automatically adapt to changing conditions, user
behavior, and application requirements, enhancing the overall customer experience.

### Implementation steps

- Familiarize yourself with the ETSI ENI architecture and its key components, such
  as the Policy Management Function (PMF) and the Context Awareness Function (CAF).
- Design your network slicing architecture using the ETSI ENI principles, including
  the use of microservices, service mesh, and cloud-based technologies.
- Use AWS services like Amazon EKS, AWS App Mesh, and AWS Lambda to implement
  the ENI-based network slicing components.
- Develop policies and rules within the PMF to dynamically allocate network
  resources based on user and application requirements.
- Use the CAF to gather contextual information about network conditions, user
  behavior, and application demands to drive intelligent resource allocation.
- Continuously monitor the performance and cost-effectiveness of your ENI-based
  network slicing implementation and adjust as needed.

## Resources

**Key AWS services:**

- [Amazon EKS](https://aws.amazon.com/pm/eks/ "https://aws.amazon.com/pm/eks/")
- [AWS App Mesh](https://aws.amazon.com/app-mesh/ "https://aws.amazon.com/app-mesh/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
