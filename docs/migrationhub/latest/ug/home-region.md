AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Managing your AWS Migration Hub home Region

The data stored in the AWS Migration Hub (Migration Hub) home Region provides a single repository of
discovery and migration planning information for your entire migration portfolio. The data
stored in the home Region from the discovery and migration tools is used to track the
progress of your migrations regardless of the migrating application’s target Region. For supported regions, see [AWS Migration Hub endpoints and quotas](../../../general/latest/gr/migrationhubn.md "../../../general/latest/gr/migrationhubn.md") in the _Amazon Web Services General Reference_.

You can view discovered data and track the progress of your migrations in the Migration Hub
console in your home Region. The console gives you detailed visibility into discovered data
and migration status, regardless of whether you are moving applications into one AWS
Region or many.

From the console in your Migration Hub home Region, you can track your migration into any AWS
Region, giving you a single view of migrations into multiple AWS Regions.

For example, let's say you choose to set US West (Oregon) Region as your Migration Hub home Region. You
perform discovery of your data centers. Then you analyze and identify your applications. You
then use AWS Application Migration Service (Application Migration Service) to migrate into the US West (Oregon) Region and the
Europe (Frankfurt) Region. You track your Application Migration Service migrations at the application level in the
Migration Hub console.

Throughout all of the migration steps in the example, your migration team uses Migration Hub in
only one AWS Region – the home Region you chose, which is the
US West (Oregon) Region.

You must choose a home Region before you can perform any write action from the console,
AWS SDKs, or AWS CLI. The following topics describe how to choose and change the home
Region for your AWS account.

###### Topics

- [Choose an AWS Migration Hub home Region](select-home-region.md "select-home-region.md")
- [Changing your AWS Migration Hub home Region](change-home-region.md "change-home-region.md")
- [Discovery with AWS Migration Hub requires the home Region](home-region-with-discovery.md "home-region-with-discovery.md")
- [Migration progress is stored in the AWS Migration Hub home
  Region](migration-reporting.md "migration-reporting.md")
- [Working with the AWS Migration Hub home Region
  APIs](#using-migration-hub-apis "#using-migration-hub-apis")

## Working with the AWS Migration Hub home Region

APIs

You can call the AWS Migration Hub, AWS Application Discovery Service, and AWS Migration Hub home Region APIs from within
your home Region _only_. API calls for write actions
(create, notify, associate, disassociate, import, or put) originating from outside your
home Region are rejected, except for the ability to register your agents and collectors.
API calls for read actions (list, describe, stop, and delete) are permitted outside of
your home Region.

###### Note

You can register agents and collectors outside your home Region. However, the
`StartDataCollection` API call in AWS Application Discovery Service prevents you from
enabling data collection from outside the home Region.

The [AWS Migration Hub Home
Region APIs](../../../migrationhub-home-region/latest/APIReference/Welcome.md "../../../migrationhub-home-region/latest/APIReference/Welcome.md") are available specifically for working with your Migration Hub home
Region. The following is a general description of each API:

- [CreateHomeRegionControl](../../../migrationhub-home-region/latest/APIReference/API_CreateHomeRegionControl.md "../../../migrationhub-home-region/latest/APIReference/API_CreateHomeRegionControl.md") – This API sets up the home Region.
  It applies to the calling account only.
- [GetHomeRegion](../../../migrationhub-home-region/latest/APIReference/API_GetHomeRegion.md "../../../migrationhub-home-region/latest/APIReference/API_GetHomeRegion.md") – Returns the calling account’s home Region,
  if configured. This API is used by other AWS services to determine the
  regional endpoint for calling AWS Application Discovery Service and Migration Hub.

You must call `GetHomeRegion` at least once before you call any
other Application Discovery Service and Migration Hub APIs, to obtain the account's Migration Hub home Region.

- [DeleteHomeRegionControl](../../../migrationhub-home-region/latest/APIReference/API_DeleteHomeRegionControl.md "../../../migrationhub-home-region/latest/APIReference/API_DeleteHomeRegionControl.md") – This operation deletes the Migration Hub
  home Region configuration for the calling account. The operation does not delete
  discovery or migration tracking data in the home Region.

To change your Migration Hub home Region, use this operation, followed by the
`CreateHomeRegionControl` operation.

- [DescribeHomeRegionControls](../../../migrationhub-home-region/latest/APIReference/API_DescribeHomeRegionControls.md "../../../migrationhub-home-region/latest/APIReference/API_DescribeHomeRegionControls.md") – This API permits filtering on
  the `ControlId`, `HomeRegion`, and
  `RegionControlScope` fields.

For more information, see the [AWS Migration Hub Home
Region API reference](../../../migrationhub-home-region/latest/APIReference/Welcome.md "../../../migrationhub-home-region/latest/APIReference/Welcome.md").
