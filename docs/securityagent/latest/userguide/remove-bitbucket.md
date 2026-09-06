

# Remove a Bitbucket integration
<a name="remove-bitbucket"></a>

Remove a Bitbucket integration when you no longer need AWS Security Agent to access repositories from a specific Bitbucket workspace.

## Prerequisites for removal
<a name="_prerequisites_for_removal"></a>

Before removing a Bitbucket integration:
+ Check which Agent Spaces have repositories connected from this integration
+ Understand the impact: Removing will break code review, penetration testing context, threat modeling, and automated remediation for all connected repositories

## Step 1: Remove the integration from AWS Security Agent
<a name="_step_1_remove_the_integration_from_aws_security_agent"></a>

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Locate the Bitbucket integration you want to remove.

1. Select the integration.

1. Choose **Remove**.

1. Review the confirmation dialog and choose **Confirm removal**.

## Step 2: Uninstall the Forge app
<a name="_step_2_uninstall_the_forge_app"></a>

After removing the integration from AWS Security Agent, uninstall the Forge app from your Atlassian site:

1. In Bitbucket, navigate to **Workspace settings**.

1. Select **Forge Apps**.

1. Locate **Connect with AWS Security Agent**.

1. Choose **Uninstall**.

**Important**  
Removing the integration in the AWS Security Agent console does not uninstall the Forge app from your Atlassian site. If you plan to register the same Bitbucket workspace again, you must uninstall the Forge app first. Otherwise, the new installation can get stuck in a pending state.