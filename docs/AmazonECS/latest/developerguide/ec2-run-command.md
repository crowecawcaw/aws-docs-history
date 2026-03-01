# Managing Amazon ECS container instances remotely using AWS Systems Manager

You can use the Run Command capability in AWS Systems Manager (Systems Manager) to securely and remotely
manage the configuration of your Amazon ECS container instances. Run Command provides a simple
way to perform common administrative tasks without logging on locally to the instance. You
can manage configuration changes across your clusters by simultaneously executing commands
on multiple container instances. Run Command reports the status and results of each
command.

Here are some examples of the types of tasks you can perform with Run Command:

- Install or uninstall packages.
- Perform security updates.
- Clean up Docker images.
- Stop or start services.
- View system resources.
- View log files.
- Perform file operations.
  For more information about Run Command, see [AWS Systems Manager Run Command](../../../systems-manager/latest/userguide/run-command.md "../../../systems-manager/latest/userguide/run-command.md") in the
  _AWS Systems Manager User Guide_.

The following are prequisites to using Systems Manager with Amazon ECS.

1. You must grant the container instance role (**ecsInstanceRole**) permissions
   to access the Systems Manager APIs. You can do this by assigning the
   **AmazonSSMManagedInstanceCore** to the
   `ecsInstanceRole` role. For information about how to attach a
   policy to a role, see [Update permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the _AWS Identity and Access Management User Guide_
2. Verify that SSM Agent is installed on your container instances. For more
   information, see [Manually installing and uninstalling SSM Agent on EC2 instances for Linux](../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-linux.md").
   After you attach Systems Manager managed policies to your `ecsInstanceRole` and
   verify that AWS Systems Manager Agent (SSM Agent) is installed on your container instances, you
   can start using Run Command to send commands to your container instances. For
   information about running commands and shell scripts on your instances and viewing the
   resulting output, see [Running Commands Using
   Systems Manager Run Command](../../../systems-manager/latest/userguide/run-command.md "../../../systems-manager/latest/userguide/run-command.md") and [Run Command Walkthroughs](../../../systems-manager/latest/userguide/run-command-walkthroughs.md "../../../systems-manager/latest/userguide/run-command-walkthroughs.md")
   in the _AWS Systems Manager User Guide_.

A common use case is to update container instance software with Run Command. You can
follow the procedues in the AWS Systems Manager User Guide with the following parameters.

| Parameter            | Value                           |
| -------------------- | ------------------------------- |
| **Command document** | `AWS-RunShellScript`            |
| **Command**          | ``<br>`$` `yum update -y`<br>`` |
| **Target instances** | Your container instances        |
