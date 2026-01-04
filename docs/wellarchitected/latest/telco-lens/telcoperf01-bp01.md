# TELCOPERF01-BP01 Use Edge locations to deploy latency

sensitive telco network workloads such as RAN and user-plane nodes

Deploying latency-sensitive telco network workloads like Radio Access Network (RAN) and
user plane nodes in edge locations is recommended. Placing these components closer to the
end users at the edge of the network minimizes latency and improves performance for real-time,
latency-critical applications and services.

**Desired outcome:**

- Place latency-sensitive telco workloads like Radio Access Network (RAN) and user plane
  nodes closer to end users at the network edge.
- Minimize latency and improve performance for real-time, latency-critical telco
  applications and services.
- Enhance the overall user experience by providing faster response times.

**Common anti-patterns:**

- Deploying telco workloads in centralized data centers without considering proximity to
  end users.
- Failing to use edge computing capabilities to offload latency-sensitive tasks.
- Neglecting to optimize network infrastructure for low-latency requirements.

**Benefits of establishing this best practice:**

- Reduced latency for critical telco services like voice, video, and real-time data
  processing.
- Improved quality of experience (QoE) for end users by providing faster response times.
- Ability to scale edge resources independently to handle localized traffic spikes.
- Enhanced resilience through distributed architecture and reduced single points of
  failure.
- Reduced bandwidth consumption and costs by processing data closer to the source.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Deploying latency-sensitive telco network workloads like Radio Access Network (RAN) and
user-plane nodes in edge locations is a crucial strategy for optimizing network performance
and improving user experience. By placing these components closer to the end users at the edge
of the network, telco operators can minimize latency and verify that critical services like
voice, video, and real-time data processing are delivered with low latency and high
responsiveness.

Edge computing solutions like AWS Wavelength and AWS Local Zones provide the infrastructure
to host these latency-sensitive telco workloads close to the end users. By leveraging these
services, telco operators can offload compute-intensive tasks to the edge, reducing the need
to backhaul traffic to centralized data centers and maintaining that end users experience the
best possible service.

When implementing this best practice, telco operators should carefully assess the
specific latency requirements of their services and the geographic distribution of their
customer base. This will inform the selection of appropriate edge locations and the workloads
that should be deployed at the edge versus in centralized data centers.

### Implementation steps

- Identify the telco workloads and services that have the most stringent latency
  requirements, such as RAN and user-plane functions.
- Analyze the geographic distribution of your customer base and the locations where
  these latency-sensitive services are consumed.
- Evaluate the availability of AWS Wavelength Zones and AWS Local Zones that can host
  these workloads closer to the end users.
- Use Amazon EC2 instances in the selected AWS Wavelength Zones or AWS Local Zones to deploy
  the identified latency-sensitive telco workloads, verifying they are optimized for
  low-latency performance.
- Configure AWS Auto Scaling to automatically scale the EC2 instances hosting the
  latency-sensitive workloads based on traffic patterns and resource utilization.
- Use Amazon CloudWatch to monitor the performance of the edge-deployed workloads and trigger
  auto scaling or relocation of resources as needed to maintain optimal user experience.

## Resources

**Key AWS services:**

- [AWS Wavelength](https://aws.amazon.com/wavelength/ "https://aws.amazon.com/wavelength/")
- [AWS Local
  Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/")
