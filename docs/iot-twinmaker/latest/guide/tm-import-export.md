# AWS IoT TwinMaker bulk operations

Use a metadataTransferJob to transfer and manage your AWS IoT TwinMaker resources at scale. A metadataTransferJob
allows you to perform bulk operations and transfer resources between AWS IoT TwinMaker and AWS IoT SiteWise and Amazon S3.

You can use bulk operations in the following scenarios:

- Mass migration of assets and data between accounts, for example migrating from
  a development account to a production account.
- Large scale asset management, such as uploading, and editing AWS IoT assets at
  scale.
- Mass import of your assets into AWS IoT TwinMaker and AWS IoT SiteWise.
- Bulk import of AWS IoT TwinMaker entities from existing ontology files such as
  `revit` or `BIM` files.

###### Topics

- [Key concepts and terminology](#tm-import-export-terminology "#tm-import-export-terminology")
- [Performing bulk import and export operations](tm-import-export-api.md "tm-import-export-api.md")
- [AWS IoT TwinMaker metadata transfer job schema](tm-import-export-schema.md "tm-import-export-schema.md")

## Key concepts and terminology

AWS IoT TwinMaker bulk operations use the following concepts and terminology:

- **Import**: The action of moving resources into an AWS IoT TwinMaker
  workspace. For example, from a local file, a file in an Amazon S3 bucket, or from AWS IoT SiteWise to
  an AWS IoT TwinMaker workspace.
- **Export**: The action of moving resources from an AWS IoT TwinMaker
  workspace to a local machine or an Amazon S3 bucket.
- **Source**: The starting location from where you want to move
  resources.

For example, an Amazon S3 bucket is an import source, and an AWS IoT TwinMaker workspace is an
export source.

- **Destination**: The desired location where you want to move your
  resources to.

For example, an Amazon S3 bucket is an export destination, and an AWS IoT TwinMaker workspace is
an import destination.

- **AWS IoT SiteWise Schema**: A schema used to import and export
  resources to and from AWS IoT SiteWise.
- **AWS IoT TwinMaker Schema**: A schema used to import and export
  resources to and from AWS IoT TwinMaker.
- **AWS IoT TwinMaker top-level resources**: Resources used in existing APIs.
  Specifically, an **Entity** or a **ComponentType**.
- **AWS IoT TwinMaker sub-level resources**: Nested resource types used
  in metadata definitions. Specifically, a **Component**.
- **Metadata**: Key information required to successfully
  import or export AWS IoT SiteWise and AWS IoT TwinMaker resources.
- **metadataTransferJob**: The object created when you run
  `CreateMetadataTransferJob`.

### AWS IoT TwinMaker metadataTransferJob functionality

This topic explains the behavior AWS IoT TwinMaker follows when you run a bulk operation–
how a metadataTransferJob is processed. It also explains how to define a schema with the
metadata required to transfer your resources. AWS IoT TwinMaker bulk operations support the following
functionality:

- **Top-level resource create or replace:**
  AWS IoT TwinMaker will create new resources or replace all existing resources that are uniquely
  identified by a resource ID.

For example, if an entity exists in the system, the entity definition will be
replaced by the new one defined in the template under the `Entity` key.

- **Sub-resource create or replace:**

From the EntityComponent level, you can only create or replace a component. The
entity must already exist, otherwise, the action will produce a ValidationException.

From the property or relationship level, you can only create or replace a property
or relationship, and the containing EntityComponent must already exist.

- **Sub-resource delete:**

AWS IoT TwinMaker also supports sub-resource deletion. A sub-resource can be a component,
property, or relationship.

If you want to delete a component, you must do it from the entity level.

If you want to delete a property or relationship, you must do it from the Entity
or EntityComponent level.

To delete a sub-resource, you update the higher level resource and omit the definition
of the sub-resource.

- **No top-level resource deletion:** AWS IoT TwinMaker will
  never delete top-level resources. A top-level resource refers to an entity or
  ComponentType.
- **No sub-resource Definitions for the same top-level resource
  in one template:**

You can't provide the full entity definition and sub-resource (like property) definition of the same entity in the same template.

If an entityId is used in Entity, you cannot use the same ID in Entity, EntityComponent, property, or relationship.

If an entityId or componentName combination is used in EntityComponent, you cannot use the same combination in EntityComponent, property, or relationship.

If an entityId, componentName, propertyName combination is used in property or relationship, you cannot use the same combination in the property or relationship.

- **ExternalId is optional for AWS IoT TwinMaker:** The ExternalId
  can be used to help you identify your resources.
