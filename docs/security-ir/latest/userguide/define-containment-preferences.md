# Define Containment Action Preferences

Containment actions enable Security Incident Response to execute rapid response measures during an active security incident, such as isolating compromised hosts or rotating credentials. These actions help quickly mitigate the impact of security incidents in your environment.

###### Important

Security Incident Response does not enable containment capabilities by default. You must explicitly authorize containment actions through your containment preferences.

To authorize Security Incident Response engineers to perform containment actions on your behalf, you must define your organization or account-level containment preferences. Account-level preferences supersede organization-level preferences.

**Prerequisites:** You must have permissions to create AWS Support cases.

**Containment options:**

- **Approval required** (default): Do not perform proactive containment of any resource without explicit authorization on a case-by-case basis.
- **Contain confirmed**: Perform proactive containment of a resource confirmed to be compromised.
- **Contain suspected**: Perform proactive containment of a resource with a high likelihood of having been compromised, based on analysis performed by AWS Security Incident Response engineering.

To define containment preferences:

1. [Create an AWS Support case](create-support-case.md "create-support-case.md") requesting to configure containment action preferences for Security Incident Response.
2. In your support case, specify:
   - Your AWS Organization ID or specific account IDs where containment actions should be authorized
   - Your preferred containment option (no containment, containment with approval, or automatic containment)
   - The types of containment actions you want to authorize (such as EC2 instance isolation, credential rotation, or security group modifications)

3. AWS Support will work with you to configure your containment preferences. You will need to deploy the necessary AWS CloudFormation StackSet that creates the required IAM roles. AWS Support can provide assistance if needed.

Once configured, Security Incident Response can execute the authorized containment actions during active security incidents to help protect your environment.

**Next steps:** After containment preferences are configured, you can monitor containment actions taken during incidents in the Security Incident Response console.
