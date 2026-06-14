# Remove a Confluence integration

Remove a Confluence integration when you no longer need AWS Security Agent to access documentation from a specific Confluence site.

## Prerequisites for removal

Before removing a Confluence integration:

- Check which Agent Spaces have pages connected from this integration
- Understand the impact: Removing will break documentation context for design reviews, penetration testing, and threat modeling across all Agent Spaces using content from this integration

## Step 1: Remove the integration from AWS Security Agent

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Locate the Confluence integration you want to remove.
3. Select the integration.
4. Choose **Remove**.
5. Review the confirmation dialog and choose **Confirm removal**.

## Step 2: Uninstall the Forge app (optional)

After removing the integration from AWS Security Agent, you can optionally uninstall the Forge app from your Atlassian site:

1. In Confluence, navigate to **Confluence administration**.
2. Select **Apps**.
3. Locate **Connect with AWS Security Agent**.
4. Choose **Uninstall**.
