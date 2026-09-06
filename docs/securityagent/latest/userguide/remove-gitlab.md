

# Remove a GitLab integration
<a name="remove-gitlab"></a>

Remove a GitLab integration when you no longer need AWS Security Agent to access repositories from a specific GitLab account or group.

## Prerequisites for removal
<a name="_prerequisites_for_removal"></a>

Before removing a GitLab integration, ensure you have:
+ Checked which Agent Spaces have repositories connected from this integration
+ Understood the impact: Removing this integration will break repository connections for code review, penetration testing context, threat modeling, and automated remediation across all Agent Spaces using repositories from this integration

## Remove the integration from AWS Security Agent
<a name="_remove_the_integration_from_aws_security_agent"></a>

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Locate the GitLab integration you want to remove.

1. Select the integration by clicking on it.

1. Choose **Remove**.

1. Review the confirmation dialog and choose **Confirm removal**.

**Note**  
After removing the integration, you may also want to revoke the Personal Access Token in GitLab to prevent further access. Navigate to your GitLab user settings and delete or revoke the token.

The same process applies to GitLab Self-Managed integrations.