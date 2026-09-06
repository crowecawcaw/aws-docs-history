

# Enabling the required permissions for tagging Service Quotas resources
<a name="sq_tags_permissions"></a>

You must configure permissions to allow your users or roles to manage tags in Service Quotas. The permissions that are required to administer tags generally correspond to the API operations for the task.

To allow IAM principles, such as roles or users, to use Service Quotas for tagging operations, attach the [`ServiceQuotasReadOnlyAccess`AWS managed policy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ServiceQuotasReadOnlyAccess$jsonEditor) to the principals. 


| Task | Required permission | 
| --- | --- | 
| Add tags to applied quotas | `servicequotas:ListTagsForResource`<br />`servicequotas:TagResource`<br /> | 
| View tags for an applied quota | `servicequotas:ListTagsForResource`<br /> | 
| Remove existing tags from an applied quota | `servicequotas:UntagResource`<br /> | 
| Edit existing tag values for applied quotas | `servicequotas:ListTagsForResource`<br />`servicequotas:TagResource`<br />`servicequotas:UntagResource`<br /> | 