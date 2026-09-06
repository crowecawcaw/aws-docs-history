

# Service quotas
<a name="reference"></a>

The following table provides information about the service quotas for Tag Editor. 

These quotas are currently not adjustable using the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/resource-groups/quotas). Contact [Support](https://console.aws.amazon.com/support/home#/).


| Name | Default | 
| --- | --- | 
| Tags attached per resource | 50 user-defined tags (AWS generated tags don't count against this limit.) | 
| Tag key name | Minimum of 1, maximum 128 Unicode characters in UTF-8.<br />Allowed characters include letters, numbers, spaces, and the following characters:<br />`_ . : / = + - @`<br />Key names can't begin with `aws:` because that prefix is reserved for AWS use. Some AWS services have some additional character or length restrictions. For details, see the documentation for the specific service.  | 
| Tag values | Minimum of 0, maximum of 256 Unicode characters in UTF-8.<br />Allowed characters include letters, numbers, spaces, and the following characters:<br />`_ . : / = + - @` Some AWS services have some additional character or length restrictions. For details, see the documentation for the specific service.  | 
| Rate of calling the [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) API operation | Maximum of 15 calls per second | 
| Rate of calling the following API operations:+  [TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html) <br />+  [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html) <br />+  [GetTagKeys](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagKeys.html) <br />+  [GetTagValues](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagValues.html)  | Maximum of 5 calls per second | 