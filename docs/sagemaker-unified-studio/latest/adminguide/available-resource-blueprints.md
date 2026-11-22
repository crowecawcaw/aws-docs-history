

# Available resource blueprints

This topic lists the resource blueprints that are available for on-demand deployment. Before project members can deploy these blueprints, an administrator must set up a role to provision blueprint resources in the project. For more information, see [Configure a provisioning role for resource blueprints](resource-blueprint-provisioning-role.md).

The following table lists the available resource blueprints and, for each one, the domain types that support it, the project configurations it is compatible with, and whether a VPC is required.


| Blueprint | Domain type support | Compatible with | VPC required | 
| --- | --- | --- | --- | 
| DataLake | Identity Center-based | Projects with project profiles | No | 
| EmrOnEc2 | IAM-based, Identity Center-based | Projects with or without project profiles | Yes | 
| EmrOnEks | IAM-based, Identity Center-based | Projects with or without project profiles | Yes | 
| EmrServerless | IAM-based, Identity Center-based | Projects with or without project profiles | Yes | 
| Lakehouse Catalog | Identity Center-based | Projects with project profiles | No | 
| MLExperiments | Identity Center-based | Projects with project profiles | No | 
| MLflowApp | Identity Center-based | Projects with project profiles | No | 
| QuickSight | Identity Center-based | Projects with project profiles | No | 
| RedshiftServerless | IAM-based, Identity Center-based | Projects with or without project profiles | Yes | 
| S3Bucket | IAM-based, Identity Center-based | Projects with or without project profiles | No | 
| S3TableCatalog | IAM-based, Identity Center-based | Projects without project profiles | No | 
| SageMakerAIDomain | Identity Center-based | Projects with project profiles | No | 
| Workflows | Identity Center-based | Projects with project profiles | No | 
+ **Projects with project profiles** – Project profiles that use either the managed Tooling blueprint or a custom Tooling blueprint.
+ **Projects with or without project profiles** – Project profiles that use the managed Tooling blueprint, the ToolingLite blueprint, or a custom Tooling blueprint.
+ **Projects without project profiles** – Project profiles are not used, and the environment blueprint configuration refers to the ToolingLite blueprint.

For the full list of blueprints that Amazon SageMaker Unified Studio supports, see [Supported blueprints](supported-blueprints.md).