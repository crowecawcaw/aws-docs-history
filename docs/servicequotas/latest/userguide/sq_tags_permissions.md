# Enabling the required permissions for tagging Service Quotas

resources

You must configure permissions to allow your users or roles to manage tags in Service Quotas.
The permissions that are required to administer tags generally correspond to the API
operations for the task.

To allow IAM principles, such as roles or users, to use Service Quotas for tagging operations,
attach the [`ServiceQuotasReadOnlyAccess`AWS managed policy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ServiceQuotasReadOnlyAccess$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ServiceQuotasReadOnlyAccess$jsonEditor") to the
principals.

| Task                                        | Required permission                                                                           |
| ------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Add tags to applied quotas                  | `servicequotas:ListTagsForResource` `servicequotas:TagResource`                               |
| View tags for an applied quota              | `servicequotas:ListTagsForResource`                                                           |
| Remove existing tags from an applied quota  | `servicequotas:UntagResource`                                                                 |
| Edit existing tag values for applied quotas | `servicequotas:ListTagsForResource` `servicequotas:TagResource` `servicequotas:UntagResource` |
