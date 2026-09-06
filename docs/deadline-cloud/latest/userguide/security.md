

# Security in Deadline Cloud
<a name="security"></a>

Security in Deadline Cloud comes down to three questions: who can see and manage your farm, what the service and your jobs can do on your behalf, and how workloads stay separate from each other. For a map of the controls that answer each question and where to configure them, start with [Security controls in Deadline Cloud](security-controls.md). For hands-on guidance for each part of your farm, see [Security best practices for Deadline Cloud](security-best-practices.md).

**Topics**
+ [Security controls in Deadline Cloud](security-controls.md)
+ [Data flow, ports, and encryption in Deadline Cloud](security-data-flow.md)
+ [Security best practices for Deadline Cloud](security-best-practices.md)
+ [Verify the authenticity of downloaded software](verify-installer.md)
+ [Identity and Access Management in Deadline Cloud](security-iam.md)
+ [Data protection in Deadline Cloud](data-protection.md)
+ [Access AWS Deadline Cloud using an interface endpoint (AWS PrivateLink)](vpc-interface-endpoints.md)
+ [Restricted network environments](network-connectivity.md)
+ [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md)
+ [Compliance validation for Deadline Cloud](deadline-compliance.md)
+ [Resilience in Deadline Cloud](disaster-recovery-resiliency.md)
+ [Infrastructure security in Deadline Cloud](infrastructure-security.md)
+ [Configuration and vulnerability analysis in Deadline Cloud](vulnerability-analysis-and-management.md)

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Deadline Cloud, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/). AWS Deadline Cloud is in scope for SOC 1, 2, and 3 compliance. For more information, see [Compliance validation for Deadline Cloud](deadline-compliance.md).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company's requirements, and applicable laws and regulations. 