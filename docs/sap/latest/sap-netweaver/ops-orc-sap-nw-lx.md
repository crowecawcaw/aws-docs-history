# Operations

## Tagging AWS resources

A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value, both defined by you. Adding tags to various AWS resources will make managing SAP environments more efficient, and help you search for resources quickly. Many Amazon EC2 API calls can be used in conjunction with a special tag filter. For more information, see [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md"). The following are some examples of how you can use tags for your operational needs.

- You can tag your Amazon EBS volumes to identify their environment and use the same tags to create backup policies. For instance, Environment=DEV/QAS/PRD.
- You can use similar tags (DEV/QAS/PRD) for Amazon EC2 instances and use them for patching your OS or running scripts to stop/start applications or Amazon EC2 instances.

## Monitoring

AWS provides multiple native services to monitor and manage your SAP environment. [CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") and [CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") can be used to monitor your underlying infrastructure and APIs. CloudWatch provides ready-to-use KPIs for CPU, disk utilization, and enables you to create custom metrics for KPIs that you want to monitor. CloudTrail allows you to log the API calls made to your AWS infrastructure components.

## Operating system maintenance

In general, operating system maintenance across large estates of Amazon EC2 instances can be managed by using:

- Tools specific to the operating system, like Oracle Enterprise Manager
- Third-party products, such as those available on AWS Marketplace.
- AWS Systems Manager

_The following are some key operating system maintenance tasks_

**Patching**

You can follow SAP recommended patching process to update your landscape on AWS. With [AWS Systems Manager Patch Manager](../../../systems-manager/latest/userguide/systems-manager-patch.md "../../../systems-manager/latest/userguide/systems-manager-patch.md"), you can roll out OS patches according to your corporate policies. It has multiple benefits:

- Scheduling based on tags
- Defining patch baselines
- Auto-approving patches with lists of approved and rejected patches

AWS Systems Patch Manager integrates with IAM, CloudTrail, and CloudWatch Events to provide a secure patching experience that includes event notifications and the ability to audit usage. For details about the process, see [How Patch Manager operations work](../../../systems-manager/latest/userguide/patch-manager-how-it-works.md "../../../systems-manager/latest/userguide/patch-manager-how-it-works.md"). Third-party products are available on [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

**Maintenance Windows**

[AWS Systems Manager Maintenance Windows](../../../systems-manager/latest/userguide/systems-manager-maintenance.md "../../../systems-manager/latest/userguide/systems-manager-maintenance.md") lets you define a schedule to perform potentially disruptive actions on your instances, such as patching an operating system, updating drivers, installing software or patches.

**Administrator access**

For administrative purposes, you can access the backend of your SAP systems via SSH or AWS Systems Manager Session Manager.

## Automation

AWS Systems Manager Automation simplifies common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources. For more information, see [AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md").

**Automation using Infrastructure-as-Code with AWS CloudFormation**

We recommend following the principle of Infrastructure-as-Code (IaC) for automating and maintaining your workloads on AWS. [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") provides a common language for you to describe and provision all the infrastructure resources in your cloud environment in a repeatable and automated manner.

## Cost optimization

We recommend cost optimization as an ongoing process. There are many AWS services that help with budgeting, cost control and optimization. For more details, see [Cost Optimization Pillar - AWS Well-Architected Framework](../../../wellarchitected/latest/cost-optimization-pillar/welcome.md "../../../wellarchitected/latest/cost-optimization-pillar/welcome.md")
