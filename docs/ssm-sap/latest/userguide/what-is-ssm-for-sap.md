# What is AWS Systems Manager for SAP?

AWS Systems Manager for SAP is an automation capability to manage and operate your SAP applications on AWS. It provides a seamless integration between AWS services and SAP applications running on AWS. Systems Manager for SAP is available to use with AWS APIs. For more information, see [Systems Manager for SAP API Reference Guide](../../../ssmsap/latest/APIReference/Welcome.md "../../../ssmsap/latest/APIReference/Welcome.md").

With Systems Manager for SAP, you can backup and restore SAP HANA databases on Amazon EC2 with AWS Backup. For more information, see [Get Started](get-started.md "get-started.md").

###### Topics

- [Features](#features-ssm-for-sap "#features-ssm-for-sap")
- [Supported Regions](#supported-regions "#supported-regions")
- [Related services](#related-services-ssm-for-sap "#related-services-ssm-for-sap")
- [Pricing](#pricing-ssm-for-sap "#pricing-ssm-for-sap")

## Features

AWS Systems Manager for SAP provides the following features for your SAP workloads running on Amazon EC2.

- Register and discover SAP applications
- List discovered SAP applications
- List configurations of discovered SAP applications
- Integration with AWS Backup – using https://console.aws.amazon.com/backup, enable automatic backup and restore operations of SAP HANA databases.
- Run configuration checks on your registered SAP applications to validate their setup and identify configuration issues.
- Integration with AWS EventBridge Scheduler – using [AWS EventBridge Scheduler](../../../scheduler/latest/UserGuide/what-is-scheduler.md "../../../scheduler/latest/UserGuide/what-is-scheduler.md"), schedule SAP management operations such as start, stop, and configuration check operations.

## Supported Regions

For more information on currently supported regions for AWS Systems Manager for SAP, see [Systems Manager for SAP endpoints and quotas](../../../general/latest/gr/ssm-sap.md "../../../general/latest/gr/ssm-sap.md").

###### Note

[Supported services by AWS Region](../../../aws-backup/latest/devguide/backup-feature-availability.md#supported-services-by-region "../../../aws-backup/latest/devguide/backup-feature-availability.md#supported-services-by-region") contains the currently supported Regions where SAP HANA database backups on Amazon EC2 instances are available with AWS Backup.

## Related services

The following services are related to AWS Systems Manager for SAP on AWS.

- [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md")
- [SAP HANA on AWS](../../../sap/latest/sap-hana/welcome.md "../../../sap/latest/sap-hana/welcome.md")
- [AWS Backint Agent for SAP HANA](../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md "../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md")
- [AWS EventBridge Scheduler](../../../scheduler/latest/UserGuide/what-is-scheduler.md "../../../scheduler/latest/UserGuide/what-is-scheduler.md")

## Pricing

AWS Systems Manager for SAP follows a simple pricing model where you pay only for the features you use. There are no upfront commitments or minimum fees

### Free Features

- SAP application registration and management
- Application-aware start and stop operations
- Basic application monitoring and insights

### Usage-Based Features

**SAP HANA Database Backup with AWS Backup integration**

- No additional charge for backup orchestration through Systems Manager for SAP
- Pay only for AWS Backup storage
- For AWS Backup pricing details, visit [AWS Backup pricing](https://aws.amazon.com/backup/pricing/ "https://aws.amazon.com/backup/pricing/")

**SAP Configuration Management**

- $0.25 USD per configuration check run per application in all AWS regions
- Run checks on-demand or on schedule
- Configuration check results are retained for 30 days

###### Example Pricing Scenario for Configuration Management

If you run three configuration checks weekly on two SAP HANA applications, your monthly cost would be $6.00 USD. This is calculated based on three checks per week, running on two applications, over four weeks, at $0.25 per check (3 checks × 2 applications × 4 weeks × $0.25 = $6.00).

### Additional Information

- No charge for registering SAP applications
- No minimum fees or upfront commitments required
