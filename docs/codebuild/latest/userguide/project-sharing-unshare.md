

# Unshare a shared project
<a name="project-sharing-unshare"></a>

An unshared project, including its builds, can be accessed only by its owner. If you unshare a project, any AWS account or user you previously shared it with cannot access the project or its builds.

To unshare a shared project that you own, you must remove it from the resource share. You can use the AWS CodeBuild console, AWS RAM console, or AWS CLI to do this.

**To unshare a shared project that you own (AWS RAM console)**  
See [Updating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.

**To unshare a shared project that you own (AWS CLI)**  
Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command.

 ** To unshare a project that you own (CodeBuild command)** 

Run the [delete-resource-policy](https://docs.aws.amazon.com/cli/latest/reference/codebuild/delete-resource-policy.html) command and specify the ARN of the project you want to unshare:

```
aws codebuild delete-resource-policy --resource-arn {{project-arn}}
```