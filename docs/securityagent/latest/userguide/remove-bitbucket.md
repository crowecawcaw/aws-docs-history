# Remove a Bitbucket integration

Remove a Bitbucket integration when you no longer need AWS Security Agent to access repositories from a specific Bitbucket workspace.

## Prerequisites for removal

Before removing a Bitbucket integration:

- Check which Agent Spaces have repositories connected from this integration
- Understand the impact: Removing will break code review, penetration testing context, threat modeling, and automated remediation for all connected repositories

## Step 1: Remove the integration from AWS Security Agent

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Locate the Bitbucket integration you want to remove.
3. Select the integration.
4. Choose **Remove**.
5. Review the confirmation dialog and choose **Confirm removal**.

## Step 2: Uninstall the Forge app

After removing the integration from AWS Security Agent, uninstall the Forge app from your Atlassian site:

1. In Bitbucket, navigate to **Workspace settings**.
2. Select **Forge Apps**.
3. Locate **Connect with AWS Security Agent**.
4. Choose **Uninstall**.

###### Important

###### Forge app is not uninstalled automatically

Removing the integration in the AWS Security Agent console does not uninstall the Forge app from your Atlassian site. If you plan to register the same Bitbucket workspace again, you must uninstall the Forge app first. Otherwise, the new installation can get stuck in a pending state.
