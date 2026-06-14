# Remove a GitHub Enterprise Server integration

Remove a GitHub Enterprise Server integration when you no longer need AWS Security Agent to access repositories from a specific GHES instance.

## Prerequisites for removal

Before removing a GHES integration:

- Check which Agent Spaces have repositories connected from this integration
- Understand the impact: Removing will break code review, penetration testing context, threat modeling, and automated remediation for all connected repositories

## Remove the integration

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Locate the GitHub Enterprise Server integration you want to remove.
3. Select the integration.
4. Choose **Remove**.
5. Review the confirmation dialog and choose **Confirm removal**.

###### Note

After removal, you may also want to revoke the OAuth application on your GHES instance. Navigate to your GHES organization settings and remove the authorized application.
