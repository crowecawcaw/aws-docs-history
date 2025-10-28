# Use tags in AWS IoT SiteWise

Use tags to categorize your AWS IoT SiteWise resources by purpose, owner, environment, or any other
classification for your use case. When you have many resources of the same type, you can
quickly identify a specific resource based on its tags.

Each tag is made up of a key and an optional value that you specify. For example, you can
establish a series of tags for your asset models to track them according to the industrial
processes they support. It's recommended to develop a tailored set of tag keys for each type
of resource you manage. Using a consistent set of tag keys can makes it easier manage
resources.

## Tag with the AWS Management Console

The **Tag Editor** in the AWS Management Console provides a central, unified way for
you to create and manage your tags for resources from all AWS services. For more
information, see [Getting started with Tag
Editor](../../../tag-editor/latest/userguide/gettingstarted.md "../../../tag-editor/latest/userguide/gettingstarted.md") in the _Tagging AWS Resources and Tag Editor User
Guide_.

## Tag with the AWS IoT SiteWise API

The AWS IoT SiteWise API also uses tags. Before you create tags, be aware of tagging restrictions.
For more information, see [Tag
naming and usage conventions](../../../general/latest/gr/aws_tagging.md#tag-conventions "../../../general/latest/gr/aws_tagging.md#tag-conventions") in the _AWS General Reference_.

- To add tags when you create a resource, define them in the `tags`
  property of the resource.
- To add tags to an existing resource, or to update tag values, use the [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
  operation.
- To remove tags from a resource, use the [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") operation.
- To retrieve the tags that are associated with a resource, use the [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") operation, or describe the resource and inspect its
  `tags` property.

The following table lists resources you can tag using the AWS IoT SiteWise API and their
corresponding `Create` and `Describe` operations.

| Taggable AWS IoT SiteWise resources | Resource                                                                                                                            | Create operation                                                                                                  | Describe operation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Asset model or component model      | [CreateAssetModel](../APIReference/API_CreateAssetModel.md "../APIReference/API_CreateAssetModel.md")                               | [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md")       |
| Asset                               | [CreateAsset](../APIReference/API_CreateAsset.md "../APIReference/API_CreateAsset.md")                                              | [DescribeAsset](../APIReference/API_DescribeAsset.md "../APIReference/API_DescribeAsset.md")                      |
| SiteWise Edge gateway               | [CreateGateway](../APIReference/API_CreateGateway.md "../APIReference/API_CreateGateway.md")                                        | [DescribeGateway](../APIReference/API_DescribeGateway.md "../APIReference/API_DescribeGateway.md")                |
| Portal                              | [CreatePortal](../APIReference/API_CreatePortal.md "../APIReference/API_CreatePortal.md")                                           | [DescribePortal](../APIReference/API_DescribePortal.md "../APIReference/API_DescribePortal.md")                   |
| Project                             | [CreateProject](../APIReference/API_CreateProject.md "../APIReference/API_CreateProject.md")                                        | [DescribeProject](../APIReference/API_DescribeProject.md "../APIReference/API_DescribeProject.md")                |
| Dashboard                           | [CreateDashboard](../APIReference/API_CreateDashboard.md "../APIReference/API_CreateDashboard.md")                                  | [DescribeDashboard](../APIReference/API_DescribeDashboard.md "../APIReference/API_DescribeDashboard.md")          |
| Access policy                       | [CreateAccessPolicy](../APIReference/API_CreateAccessPolicy.md "../APIReference/API_CreateAccessPolicy.md")                         | [DescribeAccessPolicy](../APIReference/API_DescribeAccessPolicy.md "../APIReference/API_DescribeAccessPolicy.md") |
| Time series                         | [BatchPutAssetPropertyValue](../APIReference/API_BatchPutAssetPropertyValue.md "../APIReference/API_BatchPutAssetPropertyValue.md") | [DescribeTimeSeries](../APIReference/API_DescribeTimeSeries.md "../APIReference/API_DescribeTimeSeries.md")       | For `BatchPutAssetPropertyValue`, you can configure your data sources to send industrial data to AWS IoT SiteWise before you create asset models and assets. AWS IoT SiteWise automatically creates data streams to receive streams of raw data from your equipment. For more information, see [Managing data ingestion](data-streams.md "data-streams.md"). Use the following operations to view and manage tags for resources that support tagging: <br>• [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") – Adds tags to a resource, or updates an existing tag's value. <br>• [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") – Lists the tags for a resource. <br>• [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") – Removes tags from a resource. Add or remove tags from a resource at any time. To update the value of an existing tag key, add a new tag with the same key and your desired new value to the resource. This action replaces the old value with the new one. While it's possible to assign an empty string as a tag value, you can't assign a null value. Deleting a resource also removes any tags linked to it. |
