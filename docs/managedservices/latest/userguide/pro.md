# Use AMS SSP to provision Amazon Managed Service for Prometheus in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Managed Service for Prometheus (AMP) capabilities directly in your AMS managed account. Amazon Managed Service for Prometheus is a serverless, Prometheus-compatible monitoring service for container metrics that makes it easier to securely monitor container environments at scale. With Amazon Managed Service for Prometheus, you can use the same open-source Prometheus data model and query language that you use today to monitor the performance of your containerized workloads, and also enjoy improved scalability, availability, and security without having to manage the underlying infrastructure.

Amazon Managed Service for Prometheusautomatically scales the ingestion, storage, and querying of operational metrics as workloads scale up and down. It integrates with AWS security services to enable fast and secure access to data. For more information, see [What is Amazon Managed Service for Prometheus?](../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md "../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md")

## Amazon Managed Service for Prometheus in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon Managed Service for Prometheus in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account: `customer-prometheus-console-role`. After it's
provisioned in your account, you must onboard the `customer-prometheus-console-role` role in your federation solution.

**Q: What are the restrictions to using Amazon Managed Service for Prometheus in my AMS account?**

All features are supported.

**Q: What are the prerequisites or dependencies to using Amazon Managed Service for Prometheus in my AMS account?**

There are no prerequisites or dependencies to get started with Amazon Managed Service for Prometheus. However, depending on your specific use case, you might require access to other AWS services.
