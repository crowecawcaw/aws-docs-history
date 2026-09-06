

# AWS IoT SiteWise in AWS GovCloud (US)
<a name="govcloud-iotsitewise"></a>

AWS IoT SiteWise is a managed service that you can use to collect, model, analyze, and visualize data from industrial equipment at scale. With AWS IoT SiteWise Monitor, you can quickly create web applications for non-technical users to view and analyze your industrial data in real time. With AWS IoT SiteWise gateways, you can view and process your data on your local devices.

**Note**  
The SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025. If you would like to use SiteWise Monitor, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 

## How AWS IoT SiteWise differs
<a name="govcloud-diffs-14"></a>

The following differences apply to AWS IoT SiteWise:
+ The alarm configuration and notification features in AWS IoT SiteWise Monitor portals are currently not supported.
+ Partner data sources on AWS IoT SiteWise gateways are not currently supported.
+ The following endpoints are not available:
  + The endpoint for the control plane API operations that you use to manage asset models and assets: `model.iotsitewise.region.amazonaws.com`.
  + The endpoint for the control plane API operations that you use to manage tags, storage configurations, and account configurations: `iotsitewise.region.amazonaws.com`.
  + The endpoint for the control plane API operations that you use to manage gateways: `edge.iotsitewise.region.amazonaws.com`.
  + The metadata bulk import and export operations are not available in the AWS GovCloud (US-West) region.

  For more information, see [Service Endpoints](using-govcloud-endpoints.md).

## Documentation
<a name="govcloud-docs-53"></a>
+  [AWS IoT SiteWise documentation](https://docs.aws.amazon.com/iot-sitewise/index.html) 

## Export-controlled content
<a name="govcloud-itar-content-92"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Data source names
+ Metric definitions
+ Transform definitions
+ Amazon S3 bucket names for the [exporting data to Amazon S3](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-data-storage.html) feature
+ IAM roles for the [exporting data to Amazon S3](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-data-storage.html) feature
+ AWS KMS keys