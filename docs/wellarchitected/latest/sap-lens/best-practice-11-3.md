# Best Practice 11.3 – Define an

approach to restore service availability

Restoring availability assumes that for a particular failure scenario, some loss of
service will occur. The restore approach should examine the amount of time needed to
restore service, and the actions required to meet the availability goal.

**Suggestion 11.3.1 – Enable instance recovery for EC2
instances**

AWS provides two modes of instance recovery: simplified (on by default) and
Amazon CloudWatch action-based (configurable). Both modes monitor an Amazon EC2 instance and automatically
recover the instance if it becomes impaired due to an underlying hardware failure. This
feature can remove the need for manual intervention, but startup, application restart, and
load times should be factored into the recovery time objective (RTO).

CloudWatch action-based alarms are customizable, which can help you to control the recovery
time of an instance for standalone instances.

If you intend to use a clustering solution to protect against hardware failure, you
should evaluate if instance recovery is compatible with the cluster solution.

- AWS Documentation: [Amazon EC2 Instance Recovery](../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md "../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md")
- SAP on AWS Documentation: [Technical requirements for high availability clusters](../../../sap/latest/sap-netweaver/technical-requirements.md "../../../sap/latest/sap-netweaver/technical-requirements.md")

**Suggestion 11.3.2 – Have a strategy to rebuild EC2 instances using
AMIs and infrastructure as code**

The benefit of infrastructure as code (IaC) is the ability to build and tear down
entire environments programmatically. If architected for resiliency, an environment can be
implemented in minutes using [CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") templates or [AWS Systems Manager automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md"). Automation is critical for maintaining high
availability and fast recovery.

You should evaluate the following AWS services as part of your strategy:

- AWS Service: [EC2 Image
  Builder](https://aws.amazon.com/image-builder/ "https://aws.amazon.com/image-builder/")
- AWS Service: [AWS Launch Wizard for SAP](../../../launchwizard/latest/userguide/launch-wizard-sap.md "../../../launchwizard/latest/userguide/launch-wizard-sap.md")
- AWS Service: [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- SAP on AWS Blog: [DevOps for SAP](https://aws.amazon.com/blogs/awsforsap/category/devops/ "https://aws.amazon.com/blogs/awsforsap/category/devops/")

**Suggestion 11.3.3 – Understand Amazon EBS failures**

Failure of one or more EBS volumes could impact the availability and durability of
your SAP workload. Therefore, you should understand the Amazon EBS failure rates, notification
mechanisms, and recovery options.

- AWS Documentation: [Amazon EBS Durability](https://aws.amazon.com/ebs/features/#Amazon_EBS_availability_and_durability "https://aws.amazon.com/ebs/features/#Amazon_EBS_availability_and_durability")
- AWS Documentation: [Monitor the status of your volumes](../../../AWSEC2/latest/UserGuide/monitoring-volume-status.md "../../../AWSEC2/latest/UserGuide/monitoring-volume-status.md")
- AWS Service: [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/ "https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/")
- AWS Documentation: [Volume
  recovery using Amazon EBS Snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md")

**Suggestion 11.3.4 – Have a strategy for reacting to AWS Personal
Health Dashboard notifications**

You should have a strategy for receiving and actioning notifications from your AWS
Personal Health Dashboard. This could include using CloudWatch to start Amazon SNS or
integration with your ITSM tools via the [AWS Health
API](../../../health/latest/ug/health-api.md "../../../health/latest/ug/health-api.md").

**Suggestion 11.3.5 – Ensure that you are protected against accidental
or malicious events impacting availability**

You should consider the following approaches for ensuring that you are protected
against accidental or malicious events that could impact the availability of your SAP
workload.

- Implement a [principle of least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") and enforce separation of duties within AWS
  Identity and Access Management.
- Follow the guidance in AWS Knowledge Center article: [How do I protect my data against accidental EC2 instance termination?](https://aws.amazon.com/premiumsupport/knowledge-center/accidental-termination/ "https://aws.amazon.com/premiumsupport/knowledge-center/accidental-termination/")
- Follow the [Best
  practices for Amazon EC2.](../../../AWSEC2/latest/UserGuide/ec2-best-practices.md "../../../AWSEC2/latest/UserGuide/ec2-best-practices.md")
- You should also follow the security guidance in [Security]: [Best Practice 8.3 - Secure your data recovery mechanisms
  to protect against threats.](best-practice-8-3.md "best-practice-8-3.md")

**Suggestion 11.3.6 – Identify dependencies beyond the SAP workload in
AWS**

Understand the underlying dependencies for your SAP business processes, including
shared services and supporting components or systems. Some examples include Active
Directory, DNS, identity providers, SaaS services, and on-premises systems. Assess the
impact of failure and the required mitigations.
