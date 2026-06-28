# SAP workload tags

Use the following tables for migration plans using MAP 2.0 for SAP Migration.

SAP workload tags with short ID| Source | Destination | Tag key | Tag value |
| --- | --- | --- | --- |
| On-premises | AWS | `map-migrated` | `sap`5-digit MPE ID`` |

SAP workload tags with long ID| Source | Destination | Tag key | Tag value |
| --- | --- | --- | --- |
| On-premises | AWS | `map-migrated` | `sap`10 alphanumeric MPE ID characters`` |

###### Note

The prefix for SAP workload tags is `sap`. Do not use this tag for migration
plans that are not part of MAP 2.0 for SAP. Use uppercase letters for the alphanumeric MPE IDs
(long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md "mpe-length.md").

Ensure you define the MAP tags as part of your infrastructure definition when using the AWS Launch Wizard for SAP to deploy your SAP workloads. For more information about the AWS Launch Wizard for SAP, see [Deploy an SAP application with AWS Launch Wizard](../../../launchwizard/latest/userguide/launch-wizard-sap-deploying.md "../../../launchwizard/latest/userguide/launch-wizard-sap-deploying.md") in the _AWS Launch Wizard user guide_. For a complete list of services included in MAP 2.0 for
SAP, see the MAP 2.0 Included Services list: **https://s3-us-west-2.amazonaws.com/map-2.0-customer-documentation/included-services/MAP\_Included\_Services\_List.pdf**.
