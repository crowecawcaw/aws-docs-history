

# Removing tags
<a name="tagging-remove"></a>

 You can remove tags from Amazon Inspector resources. These resources include suppression rules and CIS scan configurations. Tags help you categorize AWS resources based on specific criteria. This topic describes how to remove tags from Amazon Inspector resources. 

## Removing tags from Amazon Inspector resources
<a name="w2aac50c13b5"></a>

 You can remove tags from [suppression rules](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-supression-rules.html) and [CIS scan configurations](https://docs.aws.amazon.com/inspector/latest/user/scanning-cis-create-cis-scan-configuration.html). The following procedures describe how to remove tags in the console and with the Amazon Inspector API. 

### Removing tags in the console
<a name="w2aac50c13b5b5"></a>

 You can remove tags from Amazon Inspector resources in the console. 

**Removing tags from suppression rules**  
 You can remove a tag from a suppression rule by editing the suppression rule to no longer include the tag. For more information, see [Editing a suppression rule](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-supression-rules.html#findings-managing-supression-rules-change). 

**Removing tags from a CIS scan configuration**  
 You can remove a tag from a CIS scan configuration by editing the CIS scan configuration to no longer include the tag. For more information, see [Editing a CIS scan configuration](https://docs.aws.amazon.com/inspector/latest/user/scanning-cis-view-edit-cis-scan-configuration.html). 

### Removing tags with the Amazon Inspector API
<a name="w2aac50c13b5b7"></a>

 You can remove a tag from an Amazon Inspector resource with the Amazon Inspector API. 

**Removing tags from Amazon Inspector resources**  
 Use the `[UntagResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UntagResource.html)` API to remove tags from Amazon Inspector resources. 

 The following snippet shows an example of how to remove tag from an Amazon Inspector resource using `UntagResource`. You must include the ARN of the resource and key for tag in the command. The following example uses an empty resource ARN for a suppression filter. The key is `CostAllocation`. For information about resource types for Amazon Inspector, see [Actions, resources, and condition keys for Amazon Inspector2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoninspector2.html#amazoninspector2-resources-for-iam-policies) in the *Service Authorization Reference*. 

```
aws inspector2 untag-resource \ 
--resource-arn "{{arn:${Partition}:inspector2:${Region}:${Account}:owner/${OwnerId}/cis-configuration/${CISScanConfigurationId}}}" \ 
--tag-keys CostAllocation \
--region us-west-2
```