

# Cost allocation tags in Amazon MWAA
<a name="cost-allocation-tags"></a>

A cost allocation tag is a key-value pair that you attach to an Amazon MWAA environment. After you activate a tag, AWS groups the environment's charges under that tag in your cost reports. You can then attribute the cost of each environment to a team, project, or cost center.

**Topics**
+ [Adding and activating cost allocation tags](#cost-allocation-tags-adding)
+ [Viewing costs by tag](#cost-allocation-tags-viewing)
+ [Limitations](#cost-allocation-tags-limitations)
+ [Related resources](#cost-allocation-tags-related)

## Adding and activating cost allocation tags
<a name="cost-allocation-tags-adding"></a>

You tag your environments with the key that you want to report on, and then activate that key as a cost allocation tag. You activate a key one time for your organization, in the AWS Billing and Cost Management console of your management account.

**To track Amazon MWAA costs with tags**

1. Tag your environments with the key that you want to report on, such as `CostCenter` or `Team`. You can add tags when you create an environment, or add them to an existing environment, by using the [Amazon MWAA console](https://console.aws.amazon.com/mwaa/home), the [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/mwaa/tag-resource.html), or the [TagResource](https://docs.aws.amazon.com/mwaa/latest/API/API_TagResource.html) API operation.

1. Open the [Cost allocation tags](https://console.aws.amazon.com/billing/home#/tags) page in the AWS Billing and Cost Management console of your management account, select your tag key, and then choose **Activate**. For more information about activating cost allocation tags, see [Activating user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the *AWS Billing and Cost Management User Guide*.

1. In AWS Cost Explorer, for **Group by**, select your tag key. Your cost reports now group each environment's charges by the tag key.

To stop tracking costs with a tag, deactivate the tag key in the AWS Billing and Cost Management console.

**Note**  
Tag keys and values are case sensitive. Activating or deactivating a tag applies only to usage that you incur afterward, and does not change cost data from earlier billing periods. After you activate a tag, it can take up to 24 hours for it to appear in your cost reports.

## Viewing costs by tag
<a name="cost-allocation-tags-viewing"></a>

When you group your costs by a tag in AWS Cost Explorer or the AWS Cost and Usage Report, each tagged environment contributes its cost to that tag. After you onboard an environment, a single tag on the environment covers the cost of the environment and all of its components: its workers, its schedulers, and its web servers.

After you onboard an environment, grouping by resource in AWS Cost Explorer also aggregates these costs. Amazon MWAA attributes the usage for the environment, its workers, its schedulers, and its web servers to the single environment Amazon Resource Name (ARN), rather than to a separate resource for each component. Before onboarding, each additional worker and web server appears as its own resource in a per-resource view. After onboarding, they appear as a single line under the environment ARN.

The following chart compares an environment's cost before and after onboarding:
+ Before onboarding, Amazon MWAA reports the cost as separate amounts for the environment, its additional workers, its additional schedulers, and its additional web servers.
+ After onboarding, Amazon MWAA reports the same total cost as a single amount that it attributes to the environment ARN.

The chart shows these amounts as two stacked columns of equal height, because onboarding changes how Amazon MWAA attributes the cost, not the cost itself. The column for the day before onboarding has four segments: environment, additional worker, additional scheduler, and additional web server. The column for the day after has a single segment for the environment ARN. The dates and amounts are illustrative, not actual costs.

![Four separate cost amounts before onboarding and one combined amount after, shown as stacked columns.](https://docs.aws.amazon.com/mwaa/latest/userguide/images/metering-consolidation-before-after.png)


## Limitations
<a name="cost-allocation-tags-limitations"></a>

Environments that you create after this cost-tracking model is available are onboarded automatically.

To fully onboard an existing environment, update the environment. The update onboards the environment and all of its components. For more information, see [Update an Amazon MWAA environment](update-environment.md).

If you don't update the environment, Amazon MWAA still migrates the workers and web servers of recently created or recently updated environments to the new model as it replaces them. Environments that haven't been updated in a long time don't migrate their workers and web servers automatically. To migrate them, update the environment.

Until you onboard a component, Amazon MWAA reports the component's usage under its own resource rather than under the environment. As a result, a tag on the environment doesn't include that component's cost.

## Related resources
<a name="cost-allocation-tags-related"></a>

For more information about cost allocation tags, see the following resources.
+ For more information about filtering and grouping your costs by tag in AWS Cost Explorer, see [Filtering the data that you want to view](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html) in the *AWS Cost Management User Guide*.
+ For more information about how AWS uses tags to categorize your costs, see [Use cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing and Cost Management User Guide*.