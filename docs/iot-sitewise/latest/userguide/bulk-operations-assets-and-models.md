# Bulk operations with assets and models

To work with a large number of assets or asset models, use bulk operations to bulk import and export resources
to a different location. For example, you can create a data file that defines assets or asset models in an Amazon S3
bucket, and use bulk import to create or update them in AWS IoT SiteWise. Alternatively, if you have a large number of assets
or asset models in AWS IoT SiteWise, you can export them to Amazon S3.

###### Note

You perform bulk operations in AWS IoT SiteWise by calling operations in the AWS IoT TwinMaker API. You can do this without
setting up AWS IoT TwinMaker or creating an AWS IoT TwinMaker workspace. All you need is an Amazon S3 bucket where you can place your
AWS IoT SiteWise content.

###### Topics

- [Key concepts and terminology](#bulk-operations-terminology "#bulk-operations-terminology")
- [Supported functionality](#bulk-operations-functionality "#bulk-operations-functionality")
- [Bulk operation prerequisites](bulk-operations-prereqs.md "bulk-operations-prereqs.md")
- [Run a bulk import job](running-bulk-operations-import.md "running-bulk-operations-import.md")
- [Run a bulk export job](running-bulk-operations-export.md "running-bulk-operations-export.md")
- [Jobs progress tracking and error handling](jobs-progress-error-handling.md "jobs-progress-error-handling.md")
- [Import metadata examples](bulk-operations-import-metadata-example.md "bulk-operations-import-metadata-example.md")
- [Export metadata examples](bulk-operations-export-filter-examples.md "bulk-operations-export-filter-examples.md")
- [AWS IoT SiteWise metadata transfer job schema](bulk-operations-schema.md "bulk-operations-schema.md")

## Key concepts and terminology

AWS IoT SiteWise bulk import and export features rely on the following concepts and terminology:

- **Import**: The action of moving assets or asset models from a file in an Amazon S3 bucket to
  AWS IoT SiteWise.
- **Export**: The action of moving assets or asset models from AWS IoT SiteWise to an Amazon S3
  bucket.
- **Source**: The starting location of where you want to move content from.

For example, an Amazon S3 bucket is an import source, and AWS IoT SiteWise is an export source.

- **Destination**: The desired location of where you want to move your content to.

For example, an Amazon S3 bucket is an export destination, and AWS IoT SiteWise is an import destination.

- **AWS IoT SiteWise Schema**: This schema is used to import and export metadata from AWS IoT SiteWise.
- **Top-level resource:** An AWS IoT SiteWise resource that you can individually create or update,
  such as an asset or asset model.
- **Sub-resource:** A nested AWS IoT SiteWise resource within a top-level resource. Examples include
  properties, hierarchies, and composite models.
- **Metadata**: Key information required to import or export resources successfully.
  Examples of metadata are definitions of assets and asset models.
- **metadataTransferJob**: The object created when you run
  `CreateMetadataTransferJob`.

## Supported functionality

This topic explains what you can do when you run a bulk operation. Bulk operations support the following
functionality:

- **Top-level resource creation:** When you import an asset or asset model that
  doesn't define an ID, or whose ID doesn't match that of an existing one, then it will be created as a new
  resource.
- **Top-level resource replacement:** When you import an asset or asset model
  whose ID matches one that already exists, then it will replace the existing resource.
- **Subresource creation, replacement, or deletion:** When your import replaces
  a top-level resource such as an asset or asset model, then the new definition replaces all sub-resources, such
  as properties, hierarchies, or composite models.

For example, if you update an asset model during a bulk import, and the updated version defines a property
that wasn't present on the original, then a new property is created. If it defines a property that already
exists, then the existing property will be updated. If the updated asset model omits a property that was
present on the original, then the property is deleted.

- **No top-level resource deletion:** Bulk operations don't delete an asset or
  asset model. Bulk operations only create or update them.
