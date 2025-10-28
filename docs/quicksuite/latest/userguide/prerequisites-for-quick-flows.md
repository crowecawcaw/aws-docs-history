# Prerequisites for Quick Flows

Before you can create and use Amazon Quick Flows, you need to ensure that your Amazon Quick Suite administrator has completed the following prerequisites.

## Administrator setup requirements

Your Quick Suite administrator must complete the following tasks before you can create and use Quick Flows:

- Set up and configure Quick Suite for your organization.
- (Optional) Restrict access to flows for select users using custom permissions.

For information about how to set up Quick Suite, see [Setting up and signing into Amazon Quick Suite](setting-up.md "setting-up.md").

## Required permissions

Permissions to create, run, share, and govern flows are a result of user subscriptions and any configured custom permissions. Learn more about Quick Suite subscriptions in [Managing Quick Suite
subscriptions](managing-subscriptions.md "managing-subscriptions.md").

For more information about user roles and permissions in Quick Suite, see [Managing user access inside Amazon Quick Suite](managing-users.md "managing-users.md").

## Amazon Bedrock model access

Quick Flows uses Amazon Bedrock models for AI reasoning capabilities in General knowledge step. Your administrator must:

- Enable access in custom permissions for output refinement in flows using Bedrock models.

For information about managing Amazon Bedrock model access for Quick Flows, see [Using response preferences in General knowledge step](using-response-preferences-in-general-knowledge-step.md "using-response-preferences-in-general-knowledge-step.md").

## Action connector prerequisites

To use action connectors in your flows, your administrator must:

- Enable the specific action connectors that your organization needs.
- Configure authentication for each connector (2-legged OAuth or 3-legged OAuth).
- Grant appropriate permissions to users who need to use specific connectors.

For more information about action connector prerequisites and configuration, see [Action steps in flows](action-steps-in-flows.md "action-steps-in-flows.md").

## Quick Suite integration prerequisites

If you plan to use Amazon Quick Sight integration in your flows, your administrator must:

- Set up and configure Amazon Quick Sight for your organization.
- Enable Amazon Quick Sight integration for Quick Flows.
- Grant appropriate permissions to users who need to access Amazon Quick Sight dashboards and visualizations.

For more information about Amazon Quick Sight integration with Quick Flows, see [Amazon Quick Sight steps in flows](amazon-quick-sight-steps-in-flows.md "amazon-quick-sight-steps-in-flows.md").

## Browser requirements

Amazon Quick Flows supports the following web browsers:

- Google Chrome (latest three versions)
- Mozilla Firefox (latest three versions)
- Microsoft Edge (latest three versions)
- Apple Safari (latest three versions)

For the best experience, we recommend using the latest version of Google Chrome or Mozilla Firefox.

## Availability in AWS Regions

Quick Flows is available in all four regions with Quick Suite:

- US East (N. Virginia)
- US West (Oregon)
- Europe (Dublin)
- Asia Pacific (Sydney)

## Next steps

After ensuring that all prerequisites are met, you can:

- Learn about the key concepts in Quick Flows. See [Terminology and key concepts](terminology-and-key-concepts.md "terminology-and-key-concepts.md").
- Create your first flow. See [Creating flows](creating-flows.md "creating-flows.md").
- Explore advanced features and capabilities. See [Editing flows](editing-flows.md "editing-flows.md").
