# AWS IoT SiteWise in AWS GovCloud (US)

AWS IoT SiteWise is a managed service that you can use to collect, model, analyze, and
visualize data from industrial equipment at scale. With AWS IoT SiteWise Monitor, you can
quickly create web applications for non-technical users to view and analyze your industrial
data in real time. With AWS IoT SiteWise gateways, you can view and process your data on
your local devices.

AWS IoT SiteWise is only supported in the AWS GovCloud (US-West) Region.

###### Note

The SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use SiteWise Monitor,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[SiteWise Monitor availability change](../../../iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.md "../../../iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.md").

## How AWS IoT SiteWise differs for

AWS GovCloud (US)

- The alarm configuration and notification features in
  AWS IoT SiteWise Monitor portals are currently not supported.
- Partner data sources on AWS IoT SiteWise gateways are not currently supported.
- The following endpoints are not supported:

      + The endpoint for the control plane API operations that you use to
       manage asset models and assets:
       `model.iotsitewise.region.amazonaws.com`.
      + The endpoint for the control plane API operations that you use to
       manage tags, storage configurations, and account configurations:
       `iotsitewise.region.amazonaws.com`.
      + The endpoint for the control plane API operations that you use to
       manage gateways: `edge.iotsitewise.region.amazonaws.com`.
      + The metadata bulk import and export operations are not available in the AWS GovCloud (US-West) region.

  For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").

## Documentation for AWS IoT SiteWise

[AWS IoT SiteWise
documentation](../../../iot-sitewise/index.md "../../../iot-sitewise/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Data source names
- Metric definitions
- Transform definitions
- Amazon S3 bucket names for the [exporting data
  to Amazon S3](../../../iot-sitewise/latest/userguide/manage-data-storage.md "../../../iot-sitewise/latest/userguide/manage-data-storage.md") feature
- IAM roles for the [exporting data
  to Amazon S3](../../../iot-sitewise/latest/userguide/manage-data-storage.md "../../../iot-sitewise/latest/userguide/manage-data-storage.md") feature
- AWS KMS keys
