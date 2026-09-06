

# Authorization based on AWS IoT SiteWise tags
<a name="security_iam_service-with-iam-tags"></a>

You can attach tags to AWS IoT SiteWise resources or pass tags in a request to AWS IoT SiteWise. To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys. For more information about tagging AWS IoT SiteWise resources, see [Tag your AWS IoT SiteWise resources](tag-resources.md).

To view an example identity-based policy for limiting access to a resource based on the tags on that resource, see [View AWS IoT SiteWise assets based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-asset-tags).