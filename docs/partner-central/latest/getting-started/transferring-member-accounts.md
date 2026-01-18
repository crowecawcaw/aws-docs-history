# Transferring member accounts

This migration path moves individual member accounts from your existing AWS Organization to a new customer-owned organization, while maintaining billing responsibility through billing transfer.

**Prerequisites:**

- Customer needs a management account for their new organization
- List of member accounts to be transferred
- Documentation of any organizational dependencies within each member account to be transferred
  **Migration Steps:**

1. **Set up Customer's new Organization**

First, establish the destination for member accounts. The customer must either create a new AWS account or designate an existing account to serve as their management account. In the AWS Organizations console of this account, enable AWS Organizations and configure initial organization settings. This creates the target environment for the member accounts. 2. **Establish billing transfer**

Before moving any member accounts, set up billing transfer to ensure continuous billing responsibility. In AWS Partner Central, create a billing transfer from the customer's new management account to your Program Management Account (PMA). The customer must accept this transfer in their AWS Billing and Cost Management console. Wait for the billing transfer to become active on the first of the next month before proceeding with account migration. 3. **Prepare member account migration**

Review organization-level dependencies for the member accounts you plan to migrate. Remove or document any service control policies, resource sharing configurations, or delegated administrator settings that will need to be rebuilt in the new organization. Ensure you have a plan to reconstruct necessary configurations in the customer's organization. 4. **Transfer member accounts**

Once billing transfer is active, begin the account migration process. From the customer's new Organization, send invitations to each member account you want to transfer. Sign in to each member account to accept these invitations. Member accounts will then leave the legacy partner Organization and join the customer's Organization. Coordinate with the end customer to rebuild any necessary organizational configurations in their new environment.

###### Important

Ensure billing transfer is active before initiating any member account transfers. This maintains proper billing responsibility throughout the migration process.

###### Topics
