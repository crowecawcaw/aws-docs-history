# View shared model package

groups

After the resource owner completes the previous steps to create a resource
share and the consumer accepts the invitation for the share, the consumer can
view the shared model package groups using the AWS CLI or in the AWS RAM
console.

## AWS CLI

To view the model package groups shared, use the following command in the
model consumer account:

```
aws sagemaker list-model-package-groups --cross-account-filter-option CrossAccount
```

## AWS RAM console

In the AWS RAM console, the resource owner and consumer can view shared
model package groups. The resource owner can view the model package groups
shared with the consumer by following the steps in [Viewing
resource shares you created in AWS RAM](../../../ram/latest/userguide/working-with-sharing-view-rs.md "../../../ram/latest/userguide/working-with-sharing-view-rs.md"). The resource consumer can
view the model package groups shared by the owner by following the steps in
[Viewing
resource shares shared with you](../../../ram/latest/userguide/working-with-shared-view-rs.md "../../../ram/latest/userguide/working-with-shared-view-rs.md").
