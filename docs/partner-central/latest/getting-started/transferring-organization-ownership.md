# Transferring Organization ownership

This migration path transfers root account ownership of an existing AWS Organization to your customer while maintaining billing responsibility through billing transfer.

**Prerequisites:**

- Organization must be in all-features mode
- Customer must have an email for root account ownership
- Organization serves one customer's workloads
  **Migration Steps:**

To ensure continuous discount application throughout the migration process without any gaps, follow these steps:

1. **Define a new Partner Management Account (PMA)**

Create a new AWS account that will serve as your Partner Management Account and register this account as a PMA in Partner Central. This account will be responsible for the billing and payment for the customer organization. 2. **Identify the management account of the existing customer to migrate**

Identify the AWS account currently serving as the management account (legacy payer account) of the customer's organization that you wish to migrate to billing transfer. 3. **Establish a Partner Central channel relationship**

Create a channel relationship in Partner Central between your new Partner Management Account (from step 1) and the customer's legacy payer account (from step 2). As this organization contains your end customers workloads, you can add the account as an "end customer" relationship. 4. **Set up billing transfer**

From your new Partner Management Account, navigate to the AWS Billing and Cost Management console. Select Billing Transfers and create a new transfer by entering your customer's AWS management account ID. Your customer will receive an email notification and must accept the transfer in their AWS console. 5. **Wait for Billing Transfer to become effective**

Wait until the billing transfer becomes active, which occurs on the 1st day of the following month after acceptance. Do not proceed with the next steps until the billing transfer is active. 6. **Prepare the organization for transfer**

Update the management account's billing information in the AWS Billing and Cost Management console to reflect your customer's details. 7. **Transfer root account ownership**

Sign in to the Organization's root account and navigate to My Account in the AWS Management Console. Remove any partner MFA devices or other partner-specific security configurations. Update the root user email address to your customer's domain. The customer will receive an email to activate their root account access. Complete this step within 60 days of billing transfer going into effect. 8. **Verify transfer completion**

After the customer accepts ownership, verify that billing transfer remains active and your organization continues receiving invoices. The customer should now have full root access to manage their organization while billing responsibility remains with your organization through the established billing transfer.

###### Important

While full Organization transfer is the technically simplest path for migration, partners should be aware that this approach will expose their historical billing data to the new organization owner. This includes all billing information such as pricing, reserved instances, and saving plans that existed before the transfer of ownership.
