# Use AMS SSP to provision Amazon DevOps Guru in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon DevOps Guru capabilities directly in your AMS managed account. Amazon DevOps Guru is a fully managed operations service that makes it easy for developers and operators to improve the performance and availability of their applications. DevOps Guru lets you offload the administrative tasks associated with identifying operational issues so that you can quickly implement recommendations to improve your application. DevOps Guru creates reactive insights you can use to improve your application now. It also creates proactive insights to help you avoid operational issues that might affect your application in the future. DevOps Guru applies machine learning to analyze your operational data and application metrics and events to identify behaviors that deviate from normal operating patterns. You are notified when DevOps Guru detects an operational issue or risk. For each issue, DevOps Guru presents intelligent recommendations to address current and predicted future operational issues.

To learn more, see
[What is Amazon DevOps Guru](../../../devops-guru/latest/userguide/welcome.md "../../../devops-guru/latest/userguide/welcome.md").

## Amazon DevOps Guru in AWS Managed Services FAQ

**Q: How do I request access to Amazon DevOps Guru in my AMS account?**

To request access, submit a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account:
`customer_devopsguru_role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon DevOps Guru in my AMS account?**

There are no restrictions. Full functionality of Amazon DevOps Guru is available in your AMS account.

**Q: What are the prerequisites or dependencies to using Amazon DevOps Guru in my AMS account?**

There are no prerequisites. DevOps Guru leverages the following AWS services: Amazon CloudWatch Logs, RDS Insights, AWS X-Ray, AWS Lambda, and AWS CloudTrail.
