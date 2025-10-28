# Differences between custom and default

workspaces

###### Important

New AWS IoT SiteWise features, such as [`CompositionModel`](../../../iot-sitewise/latest/userguide/custom-composite-models.md "../../../iot-sitewise/latest/userguide/custom-composite-models.md"), are only available in
`IoTSiteWiseDefaultWorkspace`. We encourage you to use a default
workspace instead of custom workspace.

When using the `IoTSiteWiseDefaultWorkspace`, there are a few notable
differences from using a custom workspace with asset sync.

- When you create a default workspace, the Amazon S3 location and IAM role are
  optional.

###### Note

You can use `UpdateWorkspace` to provide the Amazon S3 location and
IAM role.

- The `IoTSiteWiseDefaultWorkspace` doesn't have a resource count
  limit to sync AWS IoT SiteWise resources to AWS IoT TwinMaker.
- When you sync resources from AWS IoT SiteWise, their `SyncSource` will be
  `SITEWISE_MANAGED`. This includes `Entities` and
  `ComponentTypes`.
- New AWS IoT SiteWise features, such as `CompositionModel` are only available
  in the `IoTSiteWiseDefaultWorkspace`.
  There are a few limitations specific to `IoTSiteWiseDefaultWorkspace`,
  they are:

- The default workspace can't be deleted.
- To delete resources, you must delete the AWS IoT SiteWise resources first, then the
  corresponding resources in AWS IoT TwinMaker are deleted.
