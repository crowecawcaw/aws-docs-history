

# Tag a CloudFront resource
<a name="tagging"></a>

Tags are words or phrases that you can use to identify and organize your AWS resources. You can add multiple tags to each resource, and each tag includes a key and a value that you define. For example, the key might be "domain" and the value might be "example.com". You can search and filter your resources based on the tags you add. For more information about use cases for tags, see [Common tagging strategies](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) in the Tagging AWS Resources and Tag Editor Guide.

You can use tags with CloudFront, such as the following examples: 
+ Enforce tag-based permissions on CloudFront distributions. For more information, see [ABAC with CloudFront](security_iam_service-with-iam.md#security_iam_service-with-iam-tags).
+ Track billing information in different categories. When you apply tags to CloudFront distributions or other AWS resources (such as Amazon EC2 instances or Amazon S3 buckets) and activate the tags, AWS generates a cost allocation report as a comma-separated value (CSV file) with your usage and costs aggregated by your active tags. 

  You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services. For more information about using tags for cost allocation, see [Using cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.

**Notes**  
You can tag distributions, but you can't tag origin access identities or invalidations.
[Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/tag-editor.html) and [Resource groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) aren't currently supported for CloudFront.
For the current maximum number of tags that you can add to a distribution, see [General quotas](cloudfront-limits.md#limits-general). 

**Contents**
+ [Tag restrictions](#tagging-restrictions)
+ [Tag your resources for billing](#tagging-billing)
+ [Add, edit, and delete tags](#tagging-add-edit-delete)
+ [Programmatic tagging](#tagging-related-information)

## Tag restrictions
<a name="tagging-restrictions"></a>

The following basic restrictions apply to tags:
+ For the maximum number of tags per distribution, see [General quotas](cloudfront-limits.md#limits-general).
+ Maximum key length – 128 Unicode characters
+ Maximum value length – 256 Unicode characters
+ Valid values for key and value – a-z, A-Z, 0-9, space, and the following characters: \_ . : / = \+ - and @
+ Tag keys and values are case sensitive
+ Don't use `aws:` as a prefix for keys. This prefix is reserved for AWS use.

## Tag your resources for billing
<a name="tagging-billing"></a>

You can use tags to organize your AWS bill to reflect your own cost structure. To do this, you must first activate tags for cost allocation in the Billing and Cost Management console. For more information about setting up a cost allocation report with tags, see [Monthly cost allocation report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html) in the AWS Billing User Guide. To see the cost of your combined resources, you can organize your billing information based on resources that have the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see [Using cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the AWS Billing User Guide.

**Note**  
If you've just enabled reporting, data for the current month is available for viewing after 24 hours.

## Add, edit, and delete tags
<a name="tagging-add-edit-delete"></a>

You can use the CloudFront console to manage tags for your CloudFront resources.<a name="tagging-add-edit-delete-procedure"></a>

**To add tags, edit, or delete tags for a resource**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. Navigate to your resource:
   +  **For a distribution:** Choose the ID for the distribution that you want to update. 
   +  **For a function:** Choose Functions, then choose the name of the function that you want to update. 
   +  **For a KeyValueStore:** Choose Functions, choose the KeyValueStore tab, then choose the name of the KeyValueStore that you want to update. 

1. Choose the **Tags** tab.

1. Choose **Manage tags**.

1. On the **Manage tags** page, you can do the following:
   + To add a tag, enter a key and, optionally, a value for the tag. Choose **Add new tag** to add more tags.
   + To edit a tag, change the tag’s key or its value, or both. You can delete the value for a tag, but the key is required.
   + To delete a tag, choose **Remove**.

1. Choose **Save changes**.

## Programmatic tagging
<a name="tagging-related-information"></a>

You can also use the CloudFront API, AWS Command Line Interface (AWS CLI), AWS SDKs, and AWS Tools for Windows PowerShell to apply tags. For more information, see the following topics:
+ CloudFront API operations:
  + [ListTagsForResource](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListTagsForResource.html) 
  + [TagResource](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TagResource.html) 
  + [UntagResource](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UntagResource.html) 
+ AWS CLI – See [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html) in the *AWS CLI Command Reference*
+ AWS SDKs – See the applicable SDK documentation on the [AWS Documentation](https://docs.aws.amazon.com/index.html) page
+ Tools for Windows PowerShell – See [Amazon CloudFront](https://docs.aws.amazon.com/powershell/latest/reference/items/CloudFront_cmdlets.html) in the [AWS Tools for PowerShell Cmdlet Reference](https://docs.aws.amazon.com/powershell/latest/reference/)