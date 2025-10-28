# Resources synced from

AWS IoT SiteWise

This topic lists which assets you can sync from AWS IoT SiteWise to your
AWS IoT TwinMaker workspace.

###### Important

See [Differences between custom and default
workspaces](tm-sw-default-ws-diffs.md "tm-sw-default-ws-diffs.md")
for information about the differences between the custom and default workspaces.

## Custom and default workspaces

The following resources are synced and available in **both** custom and default workspaces:

**Asset Models**

AWS IoT TwinMaker creates a new component type for each asset model in
AWS IoT SiteWise.

- The component `TypeId` for the asset model will use
  one of the following patterns:
  - **Custom workspace -**
    `iotsitewise.assetmodel:`assetModelId``
  - **Default workspace -**
    `assetModelId`

- Each property in the asset model is a new property in the component type,
  with one of the following naming patterns:

      + **Custom workspace -**
      `Property_`propertyId``
      + **Default workspace -**
      ``propertyId``

  The property name in AWS IoT SiteWise is stored as
  the `displayName` in the property definition.

- Each hierarchy in the asset model is a new property of type
  `LIST` and the `nestedType` is
  `RELATIONSHIP` in the component type. The
  hierarchy is mapped to the property with a name prefixed by one
  of the following:
  - **Custom workspace -**
    `Hierarchy_hierarchyId`
  - **Default workspace -**
    `hierarchyId`

**Asset**

AWS IoT TwinMaker creates a new entity for each asset in AWS IoT SiteWise.

- The `entityId` is the same as the
  `assetId` in AWS IoT SiteWise.
- These entities have a single component called
  `sitewiseBase`, which has the component type
  corresponding to the asset model for this asset.
- Any asset level overrides, such as setting property alias or
  unit of measure, are reflected in the entity in AWS IoT TwinMaker.

## Default workspace only

The following assets are synced and **available in the default
workspace only**, `IoTSiteWiseDefaultWorkspace`.

**AssetModelComponents**

AWS IoT TwinMaker creates a new component type for each
`AssetModelComponents` in AWS IoT SiteWise.

- The component `TypeId` for the asset model uses the
  following pattern: `assetModelId`.
- Each property in the asset model is a new property in the
  component type, with the property name as
  `propertyId`. The property name in AWS IoT SiteWise is
  stored as the `displayName` in the property
  definition.
- Each hierarchy in the asset model is a new property of type
  `LIST` and the `nestedType` is
  `RELATIONSHIP` in the component type. The
  hierarchy is mapped to the property with a name prefixed by
  `hierarchyId`.

**AssetModelCompositeModel**

AWS IoT TwinMaker creates a new component type for each
`AssetModelCompositeModel` in AWS IoT SiteWise.

- The component `TypeId` for the asset model uses the
  following pattern:
  `assetModelId_assetModelCompositeModelId`.
- Each property in the asset model is a new property in the
  component type, with the property name as
  `propertyId`. The property name in AWS IoT SiteWise is
  stored as the `displayName` in the property definition.

**AssetCompositeModels**

AWS IoT TwinMaker creates a new composite component for each
`AssetCompositeModel` in AWS IoT SiteWise.

- The `componentName` is the same as the
  `assetModelCompositeModelId` in AWS IoT SiteWise.

## Resources not synced

The following resources are not synced:

**Non-synced assets and asset models**

- Alarm models will be synced as compositeModels, but
  corresponding data in the asset related to alarms are not
  synced.
- [AWS IoT SiteWise data streams](../../../iot-sitewise/latest/userguide/manage-data-streams.md "../../../iot-sitewise/latest/userguide/manage-data-streams.md") are not
  synced. Only properties modeled in the asset model are synced.
- Property values for attributes, measurements, transforms,
  aggregates, and metadata calculation such as formula and window
  are not synced. Only the metadata about the properties, such as
  alias, unit of measure, and data type are synced. The values can
  be queried using the regular AWS IoT TwinMaker data connector API, [GetPropertyValueHistory](../apireference/API_GetPropertyValueHistory.md "../apireference/API_GetPropertyValueHistory.md").

## Use synced entities and component

types in AWS IoT TwinMaker

Once assets are synced from AWS IoT SiteWise, the synced component types
are read only in AWS IoT TwinMaker. Any update or delete action must be done in
AWS IoT SiteWise, and those changes are synced to AWS IoT TwinMaker if the syncJob
is still active.

The synced entities and the AWS IoT SiteWise base component are also
read only in AWS IoT TwinMaker. You can add additional non-synced components to the synced
entity, as long as no entity-level attributes such as the description or
`entityName` are updated.

Some restrictions apply to how you can interact with synced entities. You can't
create child entities under a synced entity in the synced entity's hierarchy.
Additionally, you can't create non-synced component types that extend from a synced
component type.

###### Note

Additional components are deleted along with the entity if the asset is
deleted in AWS IoT SiteWise or if you delete the sync job.

You can use these synced entities in Grafana dashboards and add them as tags in
the scene composer like regular entities. You can also issue knowledge graph queries
for these synced entities.

###### Note

Synced entities without modification are not charged, but you are charged for
those entities if changes have been made in AWS IoT TwinMaker. For example, if you add a
non-synced component to a synced entity, that entity is now charged in AWS IoT TwinMaker.
For more information, see [AWS IoT TwinMaker
Pricing](https://aws.amazon.com/iot-twinmaker/pricing/ "https://aws.amazon.com/iot-twinmaker/pricing/").
