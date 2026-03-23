# Define containment action preferences

Containment actions enable AWS Security Incident Response to execute rapid response measures during an active security incident. These actions help quickly mitigate the impact of security incidents in your environment.

###### Important

Security Incident Response doesn't enable containment capabilities by default. You must explicitly authorize containment actions through your containment preferences.

To authorize AWS Security Incident Response engineers to perform containment actions on your behalf, in addition to deploying an [AWS CloudFormation StackSet](working-with-stacksets.md "working-with-stacksets.md") that creates the required IAM roles, you must define your organization or account-level containment preferences. Account-level preferences supersede organization-level preferences.

**Prerequisites:** You must have permissions to create AWS Support cases.

**Containment options:**

- **Approval required** (default): Don't perform proactive containment of any resource without explicit authorization on a case-by-case basis.
- **Contain confirmed**: Perform proactive containment of a resource confirmed to be compromised.
- **Contain suspected**: Perform proactive containment of a resource with a high likelihood of having been compromised, based on analysis performed by AWS Security Incident Response engineering.

To define containment preferences:

1. [Create an AWS Support case](create-support-case.md "create-support-case.md") requesting to configure containment action preferences for Security Incident Response.
2. In your support case, specify:
   - Your AWS Organizations ID or specific account IDs where containment actions should be authorized
   - Your preferred containment option (Approval required, Contain confirmed, or Contain suspected).
   - The types of containment actions you want to authorize (such as EC2 instance isolation, credential rotation, or security group modifications)

3. AWS Support works with you to configure your containment preferences. You must deploy the necessary AWS CloudFormation StackSet that creates the required IAM roles. AWS Support can provide assistance, if needed.

When configured, AWS Security Incident Response executes the authorized containment actions during active security incidents to help protect your environment.

**Next steps:** After containment preferences are configured, you can monitor containment actions taken during incidents in the Security Incident Response console.
