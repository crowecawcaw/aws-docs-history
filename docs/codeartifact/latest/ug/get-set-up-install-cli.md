# Install or upgrade and then configure the

AWS CLI

To call CodeArtifact commands from the AWS Command Line Interface (AWS CLI) on a local development machine, you
must install the AWS CLI.

If you have an older version of the AWS CLI installed, you must upgrade it so the CodeArtifact
commands are available. CodeArtifact commands are available in the following AWS CLI
versions:

1. **AWS CLI 1:** 1.18.77 and newer
2. **AWS CLI 2:** 2.0.21 and newer
   To check the version, use the `aws --version` command.

###### To install and configure the AWS CLI

1. Install or upgrade the AWS CLI with the instructions in [Installing the
   AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md").
2. Configure the AWS CLI, with the **configure** command, as follows.

```
aws configure
```

When
prompted, specify the AWS access key and AWS secret access key of the IAM user
that you will use with CodeArtifact. When prompted for the default
AWS Region name, specify the Region where you will create the pipeline, such as
`us-east-2`. When prompted for the default output format, specify
`json`.

###### Important

When you configure the AWS CLI, you are prompted to specify an AWS Region. Choose
one of the supported Regions listed in [Region
and Endpoints](../../../general/latest/gr/codeartifact.md "../../../general/latest/gr/codeartifact.md") in the _AWS General Reference_.

For more information, see [Configuring the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") and [Managing access keys for
IAM users](../../../IAM/latest/UserGuide/ManagingCredentials.md "../../../IAM/latest/UserGuide/ManagingCredentials.md"). 3. To verify the installation or upgrade, call the following command from the
AWS CLI.

```
aws codeartifact help
```

If successful, this command displays a list of available CodeArtifact commands.
Next, you can create an IAM user and grant that user access to CodeArtifact. For more
information, see [Provision an IAM user](get-set-up-provision-user.md "get-set-up-provision-user.md").
