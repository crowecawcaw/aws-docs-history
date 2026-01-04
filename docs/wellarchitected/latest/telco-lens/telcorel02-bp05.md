# TELCOREL02-BP05 Optimize failure recovery timers for the

shared tenancy and potential for transient network issues in cloud environments

Many telecom network function vendors implement health monitoring thresholds based on
on-premises architectural assumptions, where redundant network interfaces and multiple physical
network paths may exist between components. However, when these telecom network functions are
deployed in cloud environments, the underlying network is a shared resource with a single
connection. This can lead to frequent connection alarms and service disruptions due to transient
network issues or single point of failure events, even though the network function itself may
remain functional. It is recommended to proactively engage with telecom ISVs and Network
Function developers to optimize the timers and behaviors used for health monitoring and failure
recovery. This includes designing network architecture to be resilient to packet losses or
higher latencies over the underlying network.

**Desired outcome:**

- Verify the network functions can effectively detect, react, and recover from network
  issues and failures.
- Optimize the health monitoring and failure recovery timers to strike the right balance
  between prompt failure detection and resilience against false positives.
- Use cloud capabilities to supplement vendor-provided failure detection and
  recovery mechanisms.
- Maintain high availability and service continuity for critical telco network functions
  despite the dynamic and shared nature of the cloud infrastructure.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Work closely with network function vendors to optimize health monitoring and failure
recovery mechanisms for cloud-based deployments. Implement multi-layered monitoring,
dynamically adjust failure detection timers, and integrate vendor-provided recovery procedures
with cloud-based automation. Validate and test the failure recovery processes, then
continuously monitor performance and collaborate with vendors to further refine the
configurations over time.

### Implementation steps

- Collaborate with network function vendors:
  - Engage with the network function vendors to understand their default health
    monitoring and failure recovery mechanisms.
  - Work with the vendors to customize and optimize the monitoring and recovery
    timers based on the cloud solutions and NF failure modes.

- Implement multi-layered health monitoring:
  - Leverage Amazon CloudWatch to set up comprehensive monitoring of the network function
    instances, including resource utilization, network performance, and
    application-level metrics.
  - Configure Amazon CloudWatch alarms to detect anomalies and potential failure conditions,
    with customized thresholds and rules.
  - Implement AWS Lambda-based health check functions to perform more advanced
    application-level checks, accounting for the specific requirements of the telco
    network functions.

- Optimize failure detection timers:
  - Work with the network function vendors to fine-tune the health check intervals,
    failure detection thresholds, and recovery timeouts.
  - Balance the need for prompt failure detection with resilience against transient
    issues that can trigger false positives.
  - Use Amazon CloudWatch and AWS Lambda to implement dynamic timer adjustments based on
    observed patterns and cloud infrastructure conditions.

- Enhance failure recovery mechanisms:
  - Integrate the network function vendor-provided recovery procedures with
    AWS-native capabilities, such as Amazon EC2 Auto Scaling, Amazon EKS, and AWS Lambda.
  - Develop automated recovery workflows using AWS Step Functions or AWS Lambda to handle
    different types of failures and verify consistent, reliable recovery.
  - Implement rollback and self-healing mechanisms to verify that the network
    functions can recover to a known good state.

- Validate and test the failure recovery:
  - Use AWS Fault Injection Service to inject various types of failures and network issues into
    the environment.
  - Monitor the health monitoring and failure recovery mechanisms, and fine-tune
    the timers and thresholds based on the observed behavior.
  - Document the optimized health monitoring and recovery configurations, including
    vendor-specific customizations.

## Resources

**Key AWS services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/")
- [Amazon EKS](https://aws.amazon.com/pm/eks/ "https://aws.amazon.com/pm/eks/")
- [AWS Fault Injection Service](https://aws.amazon.com/fis/ "https://aws.amazon.com/fis/")
