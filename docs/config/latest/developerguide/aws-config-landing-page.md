# Managing and Viewing AWS Resource Configurations with

AWS Config

AWS Config allows you to assess, audit, and evaluate the configurations of AWS resources.

_AWS resources_ are entities that you create and manage using the
AWS Management Console, the AWS Command Line Interface (CLI), the AWS SDKs, or AWS partner tools. Examples of AWS
resources include Amazon EC2 instances, security groups, Amazon VPCs, and Amazon Elastic Block Store. AWS Config refers to
each resource using its unique identifier, such as the resource ID or an [Amazon Resource Name (ARN)](../../../general/latest/gr/glos-chap.md#ARN "../../../general/latest/gr/glos-chap.md#ARN").

Some common use cases include:

- **Cloud administrator**: You can track and manage resource configurations to help ensure compliance, troubleshoot issues, and maintain an understanding of your AWS environment
- **Security analyst**: You can evaluate resource configurations against desired states to help identify vulnerabilities and assess security posture.
- **Compliance officer**: You can continuously audit and monitor resource configurations to help ensure adherence to organizational policies and industry standards.

###### Topics

- [Supported Resource Types](resource-config-reference.md "resource-config-reference.md")
- [Resource Coverage by Region Availability](what-is-resource-config-coverage.md "what-is-resource-config-coverage.md")
- [Recording AWS Resources](select-resources.md "select-resources.md")
- [Recording Third-Party Resources (AWS CLI)](customresources.md "customresources.md")
- [Recording Software Configurations](recording-managed-instance-inventory.md "recording-managed-instance-inventory.md")
- [Looking up Resources](looking-up-discovered-resources.md "looking-up-discovered-resources.md")
- [Viewing Resources](evaluate-config_view-compliance.md "evaluate-config_view-compliance.md")
- [Viewing Compliance History](view-manage-resource-console.md "view-manage-resource-console.md")
- [Querying Compliance History](quering-resource-compliance-history.md "quering-resource-compliance-history.md")
- [Tagging Your Resources](tagging.md "tagging.md")
