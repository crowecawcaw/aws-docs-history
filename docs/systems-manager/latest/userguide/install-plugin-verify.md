AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Verify the Session Manager plugin installation

Run the following commands to verify that the Session Manager plugin installed
successfully.

```
session-manager-plugin
```

If the installation was successful, the following message is returned.

```
The Session Manager plugin is installed successfully. Use the AWS CLI to start a session.
```

You can also test the installation by running the [start-session](../../../cli/latest/reference/ssm/start-session.md "../../../cli/latest/reference/ssm/start-session.md")
command in the the [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") (AWS CLI).
In the following command, replace `instance-id` with
your own information.

```
aws ssm start-session --target `instance-id`
```

This command will work only if you have installed and configured the AWS CLI,
and if your Session Manager administrator has granted you the necessary IAM
permissions to access the target managed node using Session Manager.
