

# Managing Service Quotas tags
<a name="sq_tags_managing-console"></a>

You can manage Service Quotas tags by using the AWS Management Console, the AWS CLI, or the AWS API.

## Managing tags from the AWS Management Console
<a name="sq_tags_managing-console"></a>

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. In the navigation page, choose **AWS services**.

1. Choose an AWS service from the list, or enter the name of the service in the search box.

1. Choose a service that has a value in the **Applied quota value** column.

1. In the **Tags** section, choose **Manage tags**. This option is not available for quotas that don't have an applied quota value.

1. You can add or remove tags, or you can edit tag values for existing tags. Enter a name for the tag in **Key**. You can add an optional value for the tag in **Value**.

1. After making all of your changes to tags, choose **Save changes**.

If the operation is successful, you return to the quota details page where you can verify your changes. If the operation fails, follow the instructions in the error message to resolve it.

## Managing Service Quotas tags using the AWS CLI or API
<a name="sq_tags_managing-cli"></a>

To manage Service Quotas tags using the CLI or API, choose a management task and use the corresponding CLI command or API call. 


| Tag management task | CLI command | API call | 
| --- | --- | --- | 
| Add tags to applied quotas | `aws service-quotas [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/tag-resource.html)` | [`TagResource`](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_TagResource.html)<br /> | 
| View tags for an applied quota | `aws service-quotas [list-tags-for-resource](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-tags-for-resource.html)` | `[ListTagsForResource](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListTagsForResource.html)`<br /> | 
| Delete existing tag values for applied quotas | `aws service-quotas [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/untag-resource.html)` | `[UntagResource](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_UntagResource.html)`<br /> | 