# AWS License Manager

AWS Audit Manager provides a prebuilt AWS License Manager framework to assist you with your audit
preparation.

###### Topics

- [What is AWS License Manager?](#what-is-Licensemanager "#what-is-Licensemanager")
- [Using this framework](#framework-Licensemanager "#framework-Licensemanager")
- [Next steps](#next-steps-License-manager "#next-steps-License-manager")
- [Additional resources](#resources-License-manager "#resources-License-manager")

## What is AWS License Manager?

With AWS License Manager, you can manage your software licenses from various software vendors
(such as Microsoft, SAP, Oracle, or IBM) centrally across AWS and on-premises
environments. Having all your software licenses in one location allows for better control
and visibility and potentially helps you to limit licensing overages and reduce the risk
of non-compliance and misreporting issues.

The AWS License Manager framework is integrated with License Manager to aggregate license usage
information based on customer defined licensing rules.

## Using this framework

You can use the _AWS License Manager_ framework to help you
prepare for audits. This framework includes a prebuilt collection of controls with
descriptions and testing procedures. These controls are grouped according to customer
defined licensing rules. You can also customize this framework and its controls to support
internal audits with specific requirements.

Using the framework as a starting point, you can create an Audit Manager assessment and start
collecting evidence that’s relevant for your audit. After you create an assessment, Audit Manager
starts to assess your AWS resources. It does this based on the controls that are defined
in the AWS License Manager framework. When it's time for an audit, you—or a delegate of
your choice—can review the evidence that Audit Manager collected. Either, you can browse the
evidence folders in your assessment and choose which evidence you want to include in your
assessment report. Or, if you enabled evidence finder, you can search for specific
evidence and export it in CSV format, or create an assessment report from your search
results. Either way, you can use this assessment report to show that your controls are
working as intended.

The AWS License Manager framework details are as follows:

| Framework name in AWS Audit Manager | Number of automated controls | Number of manual controls | Number of control sets |
| ----------------------------------- | ---------------------------- | ------------------------- | ---------------------- |
| AWS License Manager                 | 27                           | 0                         | 6                      |

The controls in this AWS Audit Manager framework aren't intended to verify if your systems are
compliant with licensing rules. Moreover, they can't guarantee that you'll pass a
licensing usage audit.

## Next steps

For instructions on how to view detailed information about this framework, including the
list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md").

For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md").

For instructions on how to customize this framework to support your specific
requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md").

## Additional resources

###### License Manager links

- [AWS License Manager service
  page](https://aws.amazon.com/license-manager "https://aws.amazon.com/license-manager")
- [AWS License Manager user
  guide](../../../license-manager/latest/userguide/license-manager.md "../../../license-manager/latest/userguide/license-manager.md")

###### License Manager APIs

For this framework,
Audit Manager uses a custom activity called `GetLicenseManagerSummary` to collect
evidence. The `GetLicenseManagerSummary` activity calls the following three
License Manager APIs:

1. [ListLicenseConfigurations](../../../license-manager/latest/APIReference/API_ListLicenseConfigurations.md "../../../license-manager/latest/APIReference/API_ListLicenseConfigurations.md")
2. [ListAssociationsForLicenseConfiguration](../../../license-manager/latest/APIReference/API_ListAssociationsForLicenseConfiguration.md "../../../license-manager/latest/APIReference/API_ListAssociationsForLicenseConfiguration.md")
3. [ListUsageForLicenseConfiguration](../../../license-manager/latest/APIReference/API_ListUsageForLicenseConfiguration.md "../../../license-manager/latest/APIReference/API_ListUsageForLicenseConfiguration.md")

The data that’s returned is then converted into evidence and attached to the relevant
controls in your assessment.

For example: Let's say that you use two licensed products (_SQL
Server 2017_ and _Oracle Database Enterprise
Edition_). First, the `GetLicenseManagerSummary` activity calls the
[ListLicenseConfigurations](../../../license-manager/latest/APIReference/API_ListLicenseConfigurations.md "../../../license-manager/latest/APIReference/API_ListLicenseConfigurations.md") API, which provides details of license configurations
in your account. Next, it adds additional contextual data for each license configuration
by calling [ListUsageForLicenseConfiguration](../../../license-manager/latest/APIReference/API_ListUsageForLicenseConfiguration.md "../../../license-manager/latest/APIReference/API_ListUsageForLicenseConfiguration.md") and [ListAssociationsForLicenseConfiguration](../../../license-manager/latest/APIReference/API_ListAssociationsForLicenseConfiguration.md "../../../license-manager/latest/APIReference/API_ListAssociationsForLicenseConfiguration.md"). Finally, it converts the license
configuration data into evidence and attaches it to the respective controls in the
framework (_4.5 - Customer managed license for SQL Server
2017_ and _3.0.4 - Customer managed license for Oracle
Database Enterprise Edition_). If you’re using a licensed product that isn’t
covered by any of the controls in the framework, that license configuration data is
attached as evidence to the following control: _5.0 - Customer
managed license for other licenses_.
