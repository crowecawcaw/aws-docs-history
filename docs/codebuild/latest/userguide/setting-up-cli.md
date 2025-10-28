# Interact with CodeBuild using the AWS CLI

If you follow the steps in [Getting started using the
console](getting-started-overview.md#getting-started "getting-started-overview.md#getting-started") to access AWS CodeBuild for the first time, you
most likely do not need the information in this topic. However, as you continue using
CodeBuild, you might want to do things such as allow users to use the AWS CLI to interact with
CodeBuild instead of (or in addition to) the CodeBuild console, the CodePipeline console, or the
AWS SDKs.

To install and configure the AWS CLI, see [Getting Set Up with the
AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md") in the _AWS Command Line Interface User Guide_.

After installing the AWS CLI, complete the following tasks:

1. Run the following command to confirm whether your installation of the AWS CLI
   supports CodeBuild:

```
aws codebuild list-builds
```

If successful, information similar to the following will appear in the
output:

```
{
  "ids": []
}
```

The empty square brackets indicate that you have not yet run any
builds. 2. If an error is output, you must uninstall your current version of the AWS CLI
and then install the latest version. For more information, see [Uninstalling the AWS CLI](../../../cli/latest/userguide/cli-uninstall.md "../../../cli/latest/userguide/cli-uninstall.md") and
[Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") in
the _AWS Command Line Interface User Guide_.
