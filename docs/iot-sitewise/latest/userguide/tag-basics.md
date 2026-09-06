

# Use tags in AWS IoT SiteWise
<a name="tag-basics"></a>

Use tags to categorize your AWS IoT SiteWise resources by purpose, owner, environment, or any other classification for your use case. When you have many resources of the same type, you can quickly identify a specific resource based on its tags.

Each tag is made up of a key and an optional value that you specify. For example, you can establish a series of tags for your asset models to track them according to the industrial processes they support. It's recommended to develop a tailored set of tag keys for each type of resource you manage. Using a consistent set of tag keys can makes it easier manage resources.

## Tag with the AWS Management Console
<a name="tags-console"></a>

The **Tag Editor** in the AWS Management Console provides a central, unified way for you to create and manage your tags for resources from all AWS services. For more information, see [Getting started with Tag Editor](https://docs.aws.amazon.com/tag-editor/latest/userguide/gettingstarted.html) in the *Tagging AWS Resources and Tag Editor User Guide*.

## Tag with the AWS IoT SiteWise API
<a name="tags-api"></a>

The AWS IoT SiteWise API also uses tags. Before you create tags, be aware of tagging restrictions. For more information, see [Tag naming and usage conventions](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions) in the *AWS General Reference*.
+ To add tags when you create a resource, define them in the `tags` property of the resource.
+ To add tags to an existing resource, or to update tag values, use the [TagResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TagResource.html) operation.
+ To remove tags from a resource, use the [UntagResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UntagResource.html) operation.
+ To retrieve the tags that are associated with a resource, use the [ListTagsForResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListTagsForResource.html) operation, or describe the resource and inspect its `tags` property.

The following table lists resources you can tag using the AWS IoT SiteWise API and their corresponding `Create` and `Describe` operations.


**Taggable AWS IoT SiteWise resources**  

| Resource | Create operation | Describe operation | 
| --- | --- | --- | 
| Asset model or component model | [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html) | [DescribeAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html) | 
| Asset | [CreateAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAsset.html) | [DescribeAsset](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html) | 
| SiteWise Edge gateway | [CreateGateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateGateway.html) | [DescribeGateway](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGateway.html) | 
| Portal | [CreatePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreatePortal.html) | [DescribePortal](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePortal.html) | 
| Project | [CreateProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateProject.html) | [DescribeProject](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeProject.html) | 
| Dashboard | [CreateDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDashboard.html) | [DescribeDashboard](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDashboard.html) | 
| Access policy | [CreateAccessPolicy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAccessPolicy.html) | [DescribeAccessPolicy](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAccessPolicy.html) | 
| Time series | [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html) | [DescribeTimeSeries](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeTimeSeries.html) | 

For `[BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html)`, you can configure your data sources to send industrial data to AWS IoT SiteWise before you create asset models and assets. AWS IoT SiteWise automatically creates data streams to receive streams of raw data from your equipment. For more information, see [Managing data ingestion](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-streams.html).

Use the following operations to view and manage tags for resources that support tagging:
+ [TagResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TagResource.html) – Adds tags to a resource, or updates an existing tag's value.
+ [ListTagsForResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListTagsForResource.html) – Lists the tags for a resource.
+ [UntagResource](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UntagResource.html) – Removes tags from a resource.

Add or remove tags from a resource at any time. To update the value of an existing tag key, add a new tag with the same key and your desired new value to the resource. This action replaces the old value with the new one. While it's possible to assign an empty string as a tag value, you can't assign a null value.

Deleting a resource also removes any tags linked to it.