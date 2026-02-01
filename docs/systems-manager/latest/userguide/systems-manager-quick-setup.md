• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# AWS Systems Manager Quick Setup

Use Quick Setup, a tool in AWS Systems Manager, to quickly configure frequently used Amazon Web Services services
and features with recommended best practices. Quick Setup simplifies setting up services,
including Systems Manager, by automating common or recommended tasks. These tasks include, for
example, creating required AWS Identity and Access Management (IAM) instance profile roles and setting up
operational best practices, such as periodic patch scans and inventory collection. There is
no cost to use Quick Setup. However, costs can be incurred based on the type of services you
set up and the usage limits with no fees for the services used to set up your service. To
get started with Quick Setup, open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/quick-setup "https://console.aws.amazon.com/systems-manager/quick-setup"). In the navigation pane, choose
**Quick Setup**.

###### Note

If you were directed to Quick Setup to help you configure your instances to be managed by
Systems Manager, complete the procedure in [Set up Amazon EC2 host management using
Quick Setup](quick-setup-host-management.md "quick-setup-host-management.md").

## What are the benefits of Quick Setup?

Benefits of Quick Setup include the following:

- **Simplify service and feature
  configuration**

Quick Setup walks you through configuring operational best practices and
automatically deploys those configurations. The Quick Setup dashboard displays a
real-time view of your configuration deployment status.

- **Deploy configurations automatically across multiple
  accounts**

You can use Quick Setup in an individual AWS account or across multiple
AWS accounts and AWS Regions by integrating with AWS Organizations. Using Quick Setup
across multiple accounts helps to ensure that your organization maintains
consistent configurations.

- **Eliminate configuration drift**

Configuration drift occurs whenever a user makes any change to a service or
feature that conflicts with the selections made through Quick Setup. Quick Setup
periodically checks for configuration drift and attempts to remediate it.

## Who should use Quick Setup?

Quick Setup is most beneficial for customers who already have some experience with the
services and features they're setting up, and want to simplify their setup process. If
you're unfamiliar with the AWS service you're configuring with Quick Setup, we recommend
that you learn more about the service. Review the content in the relevant User Guide
before you create a configuration with Quick Setup.

## Availability of Quick Setup in

AWS Regions

In the following AWS Regions, you can use all Quick Setup configuration types for an
entire organization, as configured in AWS Organizations, or for only the organizational accounts
and Regions you choose. You can also use Quick Setup with just a single account in these
Regions.

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Stockholm)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- South America (São Paulo)

In the following Regions, only the [Host
Management](quick-setup-host-management.md "quick-setup-host-management.md") configuration type is available for individual accounts:

- Europe (Milan)
- Asia Pacific (Hong Kong)
- Middle East (Bahrain)
- China (Beijing)
- China (Ningxia)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)

For a list of all supported Regions for Systems Manager, see the **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.
