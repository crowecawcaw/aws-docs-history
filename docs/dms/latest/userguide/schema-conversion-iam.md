# AWS IAM actions to API mapping for

DMS Schema Conversion and Common Studio Framework (CSF)

When setting up access control and writing IAM permissions policies for DMS Schema Conversion and
Common Studio Framework, it is important to understand how API actions map to IAM
permissions. While some actions share identical names across both interfaces, others
differ significantly.

The following table lists the correct mapping between API operations and IAM
actions:

| API to IAM Mapping                   | Service                               | API                                   | IAM                                  |
| ------------------------------------ | ------------------------------------- | ------------------------------------- | ------------------------------------ | ------------------------------------ |
| Common Studio Framework (CSF)        | CreateMigrationProject                | dms:CreateMigrationProject            |
| DeleteMigrationProject               | dms:DeleteMigrationProject            |                                       | ModifyMigrationProject               | dms:UpdateMigrationProject           |
| DescribeMigrationProjects            | dms:ListMigrationProjects             |                                       | CreateInstanceProfile                | dms:CreateInstanceProfile            |
| DeleteInstanceProfile                | dms:DeleteInstanceProfile             |                                       | ModifyInstanceProfile                | dms:UpdateInstanceProfile            |
| DescribeInstanceProfiles             | dms:ListInstanceProfiles              |                                       | CreateDataProvider                   | dms:CreateDataProvider               |
| DeleteDataProvider                   | dms:DeleteDataProvider                |                                       | ModifyDataProvider                   | dms:UpdateDataProvider               |
| DescribeDataProviders                | dms:ListDataProviders                 |
| DMS Schema Conversion                | ModifyConversionConfiguration         | dms:dms.UpdateConversionConfiguration |
| DescribeConversionConfiguration      | dms:DescribeConversionConfiguration   |                                       | StartMetadataModelImport             | dms:StartMetadataModelImport         |
| ExportMetadataModelAssessment        | dms:ExportMetadataModelAssessment     |                                       | StartMetadataModelConversion         | dms:StartMetadataModelConversion     |
| StartMetadataModelExportAsScript     | dms:StartMetadataModelExportAsScripts |                                       | StartMetadataModelExportToTarget     | dms:StartMetadataModelExportToTarget |
| StartExtensionPackAssociation        | dms:AssociateExtensionPack            |                                       | DescribeMetadataModelConversions     | dms:ListMetadataModelConversions     |
| DescribeMetadataModelExportsToTarget | dms:ListMetadataModelExports          |                                       | DescribeMetadataModelExportsAsScript | dms:ListMetadataModelExports         |
| DescribeMetadataModelImports         | dms:DescribeMetadataModelImports      |                                       | DescribeMetadataModelAssessments     | dms:ListMetadataModelAssessments     |
| DescribeExtensionPackAssociations    | dms:ListExtensionPacks                |
