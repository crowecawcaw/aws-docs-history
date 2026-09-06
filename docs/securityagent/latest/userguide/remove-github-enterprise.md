

# Remove a GitHub Enterprise integration
<a name="remove-github-enterprise"></a>

Remove a GitHub Enterprise integration when you no longer need AWS Security Agent to access repositories from a specific GHE instance.

## Prerequisites for removal
<a name="_prerequisites_for_removal"></a>

Before removing a GHE integration:
+ Check which Agent Spaces have repositories connected from this integration
+ Understand the impact: Removing will break code review, penetration testing context, threat modeling, and automated remediation for all connected repositories

## Remove the integration
<a name="_remove_the_integration"></a>

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Locate the GitHub Enterprise integration you want to remove.

1. Select the integration.

1. Choose **Remove**.

1. Review the confirmation dialog and choose **Confirm removal**.

**Note**  
After removal, you may also want to revoke the OAuth application on your GHE instance. Navigate to your GHE organization settings and remove the authorized application.