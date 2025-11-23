# Understanding AWS License Manager license asset groups

License asset groups in AWS License Manager provide centralized license management across AWS regions and accounts within an organization, offering consolidated visibility, automated notifications, and comprehensive reporting for software license compliance.

## What are license asset groups

A license asset group is a container within AWS License Manager that consolidates licenses and their associated EC2 instances based on user-defined rules. These groups provide a unified view of your software licensing state across your entire AWS Organizations, regardless of which regions or accounts the licenses and instances reside in.

License asset groups work by applying rulesets that define which licenses and instances belong together. For example, you might create a "Windows Server" license asset group that tracks all Windows Server licenses and the EC2 instances running Windows Server across your organization. The group automatically discovers and includes relevant resources based on the rules you configure.

The system supports both AWS-managed rulesets for common software products like Microsoft Windows Server, SQL Server, Red Hat Enterprise Linux, Ubuntu Pro, and SUSE Enterprise Linux, as well as custom rulesets that you can create for your specific licensing needs.

## Key capabilities and components

### Centralized license visibility

License asset groups aggregate licensing information from multiple AWS regions into a single view. This cross-region visibility eliminates the need to check each region individually to understand your organization's software licensing state. The groups automatically discover software products running on your workloads using the AWS Systems Manager agent and consolidate this information for organization-wide visibility.

### Flexible rule-based organization

License asset groups use rulesets to define which licenses and instances they track and maintain. This flexible relationship between groups and rulesets allows you to organize your licenses in ways that match your business needs. You can use AWS-managed rulesets for widely adopted products or create custom rules for specialized software.

### Automated compliance monitoring

License asset groups provide automated license expiration notifications through Amazon SNS, helping you proactively manage license renewals. License consumption is tracked against defined usage dimensions such as vCPU, Sockets, Instance, or Core metrics, ensuring you maintain awareness of your licensing obligations.

## Integration with existing AWS services

License asset groups build upon existing AWS License Manager capabilities and integrate with several AWS services to provide comprehensive license management. The feature works alongside license configurations and automated discovery features you may already be using.

To enable software discovery, install the AWS Systems Manager agent on your EC2 instances. For multi-account scenarios, you need to configure cross-account discovery and ensure appropriate IAM permissions for License Manager operations across your organization.
