# Unshare a shared report group

An unshared report group, including its reports and their test case results, can be
accessed only by its owner. If you unshare a report group, any AWS account or user you
previously shared it with cannot access the report group, its reports, or the results of
test cases in the reports.

To unshare a shared report group that you own, you must remove it from the resource
share. You can use the AWS RAM console or AWS CLI to do this.

###### To unshare a shared report group that you own (AWS RAM console)

See [Updating a resource share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To unshare a shared report group that you own (AWS RAM command)

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

**To unshare report group that you own CodeBuild command)**

Run the [delete-resource-policy](../../../cli/latest/reference/codebuild/delete-resource-policy.md "../../../cli/latest/reference/codebuild/delete-resource-policy.md") command and specify the ARN of the report group you
want to unshare:

```
aws codebuild delete-resource-policy --resource-arn `report-group-arn`
```
