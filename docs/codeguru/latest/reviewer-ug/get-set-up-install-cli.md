As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Install or upgrade and then configure the

AWS CLI

To call Amazon CodeGuru Reviewer commands from the AWS Command Line Interface (AWS CLI) on a local development machine, you
must install the AWS CLI.

###### Note

You cannot create a repository association for a GitHub repository using the AWS CLI. You
can use the AWS CLI to create a repository association for all other supported repository
types. For more information, see [Working with repository associations in
Amazon CodeGuru Reviewer](working-with-repositories.md "working-with-repositories.md").

If you have an older version of the AWS CLI installed, we recommend you upgrade it so the
CodeGuru Reviewer commands are available. To check the version, use the `aws --version`
command.

###### To install and configure the AWS CLI

1. Follow the instructions in [Getting started with the
   AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") to install or upgrade the AWS CLI.
2. To configure the AWS CLI, see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the
   _AWS Command Line Interface User Guide_.

###### Important

When you configure the AWS CLI, you are prompted to specify an AWS Region. Choose
one of the supported Regions listed in [Amazon CodeGuru Reviewer endpoints and quotas](../../../general/latest/gr/codeguru-reviewer.md "../../../general/latest/gr/codeguru-reviewer.md")
in the _AWS General Reference_. 3. To verify the installation or upgrade, call the following command from the
AWS CLI.

```
aws codeguru-reviewer help
```

If successful, this command displays a list of available CodeGuru Reviewer commands.
