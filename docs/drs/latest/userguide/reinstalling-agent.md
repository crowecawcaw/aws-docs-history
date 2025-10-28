# Reinstalling the agent

To reinstall the AWS Replication Agent, download the latest version of the agent and
follow the installation instructions. You do not need to remove any previous versions prior to
reinstalling the agent.

- [Linux](linux-agent.md "linux-agent.md")
- [Windows](windows-agent.md "windows-agent.md")

###### Note

You must reinstall the agent to benefit from new features.

## Reinstalling the agent on a recovery instance

If you are reinstalling an agent on a recovery instance:

1. Select your recovery instance and choose **Disconnect from
   AWS** from the **Actions** drop-down
   menu.
2. When reinstalling the agent, include the **--install-as-recovery-instance** parameter.

Example:

```
chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init --install-as-recovery-instance s-abcd01234567890
```

###### Note

In order to reinstall the agent on a recovery instance, you need to provide the temporary
credentials for a role that has the [AWSElasticDisasterRecoveryAgentInstallationPolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.md "security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.md") policy.
