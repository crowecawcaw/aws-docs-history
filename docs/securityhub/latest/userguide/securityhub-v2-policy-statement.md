# Creating the delegated administrator policy in Security Hub

The AWS organization management account can create a policy allowing the delegated administrator to configure Security Hub and perform specific actions in AWS Organizations.
The procedure in this topic describes how to create the policy.
When completing the procedure, you can allow Security Hub to create the policy for you or manually create the policy.
Allow Security Hub to create the policy unless you want to customize it for a particular use case.

Complete this procedure only if the organization management account enabled Security Hub and designated a delegated administrator, but skipped creating the policy during the enablement workflow.
For information about how to update this policy, see [Update a resource-based delegation policy with AWS Organizations](../../../organizations/latest/userguide/orgs-policy-delegate-update.md "../../../organizations/latest/userguide/orgs-policy-delegate-update.md") in the _AWS Organizations User Guide_.

###### Note

After you complete this procedure, the delegated administrator can create a policy to manage member accounts in your organization.
For more information, see [Creating a policy as the delegated administrator to manage member accounts](securityhub-v2-da-policy.md "securityhub-v2-da-policy.md").

###### To create the delegated administrator policy

1. Sign in to your AWS account with your organization management account credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the navigation pane, choose **General**.
3. For **Delegated administrator policy**, do one of the following:

   - Choose **Create policy**.
     Select the box under the policy statement to confirm that Security Hub automatically creates a delegation policy granting all required permission to the delegated administrator.
   - Open the policy.
     Choose **Copy and attach**.
     In the AWS Organizations console, under **Delegated administrator for AWS Organizations**, choose **Delegate**, and paste the resource policy in the delegation policy editor.
     Choose **Create Policy**.
     Open the tab where you are in the Security Hub console, and choose **Configure**.
