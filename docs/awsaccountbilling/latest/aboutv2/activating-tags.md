# Activating user-defined cost allocation tags

For tags to appear on your billing reports, you must activate them. Your
user-defined cost allocation tags represent the tag key, which you activate in the
Billing and Cost Management console. Once you activate or deactivate the tag key, it will affect all tag
values that share the same tag key. A tag key can have multiple tag values. You can
also use the `UpdateCostAllocationTagsStatus` API operation to activate
your tags in bulk. For more information, see the [AWS Billing and Cost Management API Reference](../../../aws-cost-management/latest/APIReference/API_UpdateCostAllocationTagsStatus.md "../../../aws-cost-management/latest/APIReference/API_UpdateCostAllocationTagsStatus.md").

###### To activate your tag keys

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost allocation tags**.
3. Select the tag keys that you want to activate.
4. Choose **Activate**.
   After you create and apply user-defined tags to your resources, it can take up to
   24 hours for the tag keys to appear on your cost allocation tags page for activation. It
   can then take up to 24 hours for tag keys to activate.

For an example of how tag keys appear in your billing report with cost allocation
tags, see [Viewing a cost allocation report](configurecostallocreport.md#allocation-viewing "configurecostallocreport.md#allocation-viewing").

## About the

`awsApplication` tag

The `awsApplication` tag will be automatically added to all
resources that are associated with applications that are set up in AWS Service Catalog AppRegistry.
This tag is automatically activated for you as a cost allocation tag. Use this
tag to analyze the costs trends for your application and its resources.

You can deactivate the `awsApplication` tag, but this will affect
the cost reporting for the application. If you deactivate the tag, it won’t be
automatically activated again. To manually activate the tag, use the Billing
console or the [UpdateCostAllocationTagsStatus](../../../aws-cost-management/latest/APIReference/API_UpdateCostAllocationTagsStatus.md "../../../aws-cost-management/latest/APIReference/API_UpdateCostAllocationTagsStatus.md") API operation.

The `awsApplication` tag doesn’t count towards your cost allocation
tag quota. For more information about quotas and restrictions for cost
allocation tags, see [Quotas and restrictions](billing-limits.md "billing-limits.md"). For more information about AppRegistry, see the
[AWS Service Catalog AppRegistry Administrator Guide](../../../servicecatalog/latest/arguide/overview-appreg.md#ar-user-tags "../../../servicecatalog/latest/arguide/overview-appreg.md#ar-user-tags").
