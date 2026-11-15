

# Getting started with an AI coding agent
<a name="getting-started-agent"></a>

The `aws-emulator` skill teaches your AI coding agent how to work with AWS Emulator. With the skill, your agent can do the following for you:
+ Install the emulator, using the Linux package or Docker, depending on your operating system
+ Start the emulator, and point the AWS CLI or your AWS SDK at it
+ Fix connection, certificate, and signing errors
+ Check whether your project is expected to work on the emulator. For more information, see [Checking whether your project works with AWS Emulator](check-project.md).

The skill uses the same steps that this guide describes for the Linux package and Docker paths. Before your agent writes outside its working folders, such as when it runs `sudo` or edits your shell profile, it asks you first.

## To install the skill
<a name="getting-started-agent-install"></a>

1. Check that you have the AWS CLI version 2.35.0 or later.

   ```
   aws --version
   ```

1. Install the skill. The following command installs it for all the AI coding agents that the AWS CLI finds on your machine, such as Kiro, Cursor, and Claude Code.

   ```
   aws agent-toolkit add-skill --skill-name aws-emulator --region us-east-1
   ```

   For more information, see [Managing skills with the AWS CLI](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html) in the *Agent Toolkit for AWS User Guide*.

1. Ask your agent to set up the emulator. For example, ask "Install AWS Emulator and point my project at it."