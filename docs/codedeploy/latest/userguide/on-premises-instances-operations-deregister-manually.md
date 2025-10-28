# Manually deregister an

on-premises instance

Typically, you deregister an on-premises instance after you're no longer planning to
deploy to it. You use the AWS CLI to manually deregister on-premises instances.

Manually deregistering an on-premises instance does not uninstall the CodeDeploy agent. It does
not remove the configuration file from the instance. It does not delete the IAM user
associated with the instance. It does not remove any tags associated with the instance.

To automatically uninstall the CodeDeploy agent and remove the configuration file from the
on-premises instance, see [Automatically uninstall the
CodeDeploy agent and remove the configuration file from an on-premises instance](on-premises-instances-operations-uninstall-agent.md "on-premises-instances-operations-uninstall-agent.md").

To manually uninstall only the CodeDeploy agent, see [Managing CodeDeploy agent operations](codedeploy-agent-operations.md "codedeploy-agent-operations.md").

To manually delete the associated IAM user, see [Deleting an IAM user from your
AWS account](../../../IAM/latest/UserGuide/Using_DeletingUserFromAccount.md "../../../IAM/latest/UserGuide/Using_DeletingUserFromAccount.md").

To manually remove only the associated on-premises instance tags, see [Manually remove on-premises
instance tags from an on-premises instance](on-premises-instances-operations-remove-tags.md "on-premises-instances-operations-remove-tags.md").

- Call the [deregister-on-premises-instance](../../../cli/latest/reference/deploy/deregister-on-premises-instance.md "../../../cli/latest/reference/deploy/deregister-on-premises-instance.md") command, specifying the name
  that uniquely identifies the on-premises instance (with the `--instance-name`
  option):

```
aws deploy deregister-on-premises-instance --instance-name AssetTag12010298EX
```

After you deregister an on-premises instance:

    + It stops appearing in the console immediately.
    + You can create another instance with the same name immediately.
