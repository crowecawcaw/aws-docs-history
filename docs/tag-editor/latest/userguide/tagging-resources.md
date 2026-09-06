

# Managing tags with Tag Editor
<a name="tagging-resources"></a>

After you [find resources](find-resources-to-tag.md) that you want to tag, you can add, remove, and edit the tags for some or all of your search results. Tag Editor shows you any tags that are attached to resources. It also shows you whether those tags were added in Tag Editor, by the resource's service console, or by using the API.

**Important**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.

**Other ways to manage your tags**  
This topic discusses tagging resources by using Tag Editor in the AWS Management Console. However, you can also manage the tags on your AWS resources by using the following tools:  
You can type or script commands at your shell prompt by using the [`resourcegroupstaggingapi` commands](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html#cli-aws-resourcegroupstaggingapi) in the AWS Command Line Interface (AWS CLI).
You can create and run PowerShell scripts by using the [AWS Resource Groups Tagging API](https://docs.aws.amazon.com/powershell/latest/reference/items/ResourceGroupsTaggingAPI_cmdlets.html) in the AWS Tools for PowerShell Core.
You can create and run programs with any of the available [AWS SDKs](https://docs.aws.amazon.com/index.html#sdks) by using the [Resource groups tagging APIs](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/), such as the [tagging APIs for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html) or the [tagging APIs for Java](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/ResourceGroupsTaggingAPI.html).

When you add, remove, or edit existing tags, you're changing tags only on those resources that you select in the results of your **Find resources to tag** query. You can select up to 500 resources on which to manage tags.