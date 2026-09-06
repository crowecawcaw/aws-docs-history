

# Remove a Confluence integration
<a name="remove-confluence"></a>

Remove a Confluence integration when you no longer need AWS Security Agent to access documentation from a specific Confluence site.

## Prerequisites for removal
<a name="_prerequisites_for_removal"></a>

Before removing a Confluence integration:
+ Check which Agent Spaces have pages connected from this integration
+ Understand the impact: Removing will break documentation context for design reviews, penetration testing, and threat modeling across all Agent Spaces using content from this integration

## Step 1: Remove the integration from AWS Security Agent
<a name="_step_1_remove_the_integration_from_aws_security_agent"></a>

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Locate the Confluence integration you want to remove.

1. Select the integration.

1. Choose **Remove**.

1. Review the confirmation dialog and choose **Confirm removal**.

## Step 2: Uninstall the Forge app (optional)
<a name="_step_2_uninstall_the_forge_app_optional"></a>

After removing the integration from AWS Security Agent, you can optionally uninstall the Forge app from your Atlassian site:

1. In Confluence, navigate to **Confluence administration**.

1. Select **Apps**.

1. Locate **Connect with AWS Security Agent**.

1. Choose **Uninstall**.