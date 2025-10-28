# Unshare a shared project

An unshared project, including its builds, can be accessed only by its owner. If you
unshare a project, any AWS account or user you previously shared it with cannot access
the project or its builds.

To unshare a shared project that you own, you must remove it from the resource share.
You can use the AWS CodeBuild console, AWS RAM console, or AWS CLI to do this.

###### To unshare a shared project that you own (AWS RAM console)

See [Updating a resource share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To unshare a shared project that you own (AWS CLI)

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

**To unshare project that you own (CodeBuild command)**

Run the [delete-resource-policy](../../../cli/latest/reference/codebuild/delete-resource-policy.md "../../../cli/latest/reference/codebuild/delete-resource-policy.md") command and specify the ARN of the project you want
to unshare:

```
aws codebuild delete-resource-policy --resource-arn `project-arn`
```
