

# Best practices
<a name="orgs_transfer_billing-best-practices"></a>

This page covers best practices for before you start using billing transfer, while you use it, and before you stop using it (if applicable).

**Important**  
We strongly recommend to download and back up all billing artifacts (invoices, credit memos, CUR files, CSV files from Cost Explorer and other billing and cost management pages as applicable) on the bill-source account (the account that transfer out its billing management), before establishing a billing transfer.

## Back up your billing data before billing transfer
<a name="orgs_transfer_billing-best-practices-rec"></a>

Before you proceed with transfer billing from your bill source account, we strongly recommend that you download and back up the following billing artifacts:
+ Invoices
+ Credit memos
+ AWS Cost and Usage Report files
+ CSV files exported from Cost Explorer
+ CSV files exported from other AWS Billing and Cost Management console pages

**Important**  
Downloading these billing artifacts helps ensure that you maintain access to your historical billing data after the billing transfer is complete.

## Prerequisites
<a name="orgs_transfer_billing-best-practices-prereq"></a>

There are three options to start using billing transfer:
+ Option 1: Set up billing transfer for externally owned organizations
+ Option 2: Create an AWS organization before setting up billing transfer
+ Option 3: Transfer ownership of an AWS organization before setting up billing transfer

### Option 1: Set up billing transfer for externally owned organizations
<a name="orgs_transfer_billing-best-practices-prereq-3"></a>

This option involves taking over billing responsibility through billing transfer from AWS Organizations owned by external parties (such as end customers, affiliates, or subsidiaries). You might send a billing transfer invite from your existing organization or create a new organization dedicated to billing and financial management to send invites from.

**Prerequisites**

To set up billing transfer you must meet this requirement:
+ The organizations sending and receiving the invites are on all-features mode

For Channel Partners, you should follow these best practices to comply with channel program terms:
+ The administrator of the organization accepting the invite has control over root account
+ Organizations who transfer away their billing serve one customer's workloads

This option is suitable for:

- Channel partners onboarding new end customers with existing AWS accounts

- Customers purchasing services directly from AWS who acquire new companies (such as private equity companies or enterprises expanding across subsidiaries and affiliates)

**Set up billing transfer**

In the AWS Billing and Cost Management console, choose **Preferences and Settings**, then **Billing Transfers**. Create a transfer from your bill transfer account to the existing management accounts that will become bill source accounts. If you're a channel partner, register your bill transfer account in Partner Central as a new Partner Management account before completing the transfer.

**Important**  
Before proceeding with billing transfer:  
Back up Cost Explorer data from bill source accounts, as they lose historical data visibility when billing transfer becomes active.  
Create new preferences after billing transfer is active, as existing preferences become unhealthy and stop receiving data. Disable the split cost allocation data functionality when creating preferences.

### Option 2: Create an AWS organization before setting up billing transfer
<a name="orgs_transfer_billing-best-practices-prereq-1"></a>

This process involves creating a new AWS Organizations, setting up billing transfer, and then migrating member accounts. This process is suitable if you support a single AWS organization and want to split into multiple AWS organizations. For example, you are a channel partner who consolidates multiple end customers into one AWS organizations (multi-tenant organization) and needs to provide them with dedicated AWS organizations; or you are a customer who consolidates multiple business units, affiliates, or subsidiaries into one AWS organizations.

**Benefits of organization migration**
+ Maintains billing privacy during migration
+ Provides flexible migration scheduling
+ Supports both single-tenant and multi-tenant AWS Organizations

Consider the following requirements before migrating:
+ You must rebuild organization-level configurations
+ You must identify and recreate organization-level dependencies
+ Migration takes longer than a full organization transfer

Follow these steps and review the considerations for each:

**Step 1: Create an AWS Organizations for each business unit or customer**

Create a new AWS account or designate an existing account as the management account for each business unit or customer you plan to move from your existing AWS Organizations.

**Note**  
If you're a channel partner, you might need to help your end customers create AWS Organizations. End customers must provide their own payment method.

For more information on how to create a management account for AWS Organizations, see [Tutorial: Creating and configuring an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html).

**Step 2: Set up billing transfer for the new management account**

Configure billing transfer between your existing management account and the newly created management account. The new AWS Organizations will transfer its bills to the existing organization.

**Important**  
The owner of the new AWS Organizations must accept the billing transfer invitation in their AWS Billing and Cost Management console. Wait for the billing transfer to become active on the date specified in the invitation before proceeding with account migration.

**Step 3: Prepare member account migration**

Review organization-level dependencies for the member accounts that you plan to migrate. Document or remove the following items that you'll need to rebuild in the new organization:
+ Service control policies
+ Resource sharing configurations
+ Delegated administrator settings

Create a plan to reconstruct these configurations in the end customer's or business unit's organization.

**Step 4: Move member accounts**

After billing transfer is active, begin the account migration.

From the new organization, send invitations to each member account you want to add. Sign in to each member account to accept these invitations. The member accounts then leave your current organization and join the new organization. Work with the new AWS Organizations owner to rebuild organizational configurations in the new environment.

For step-by-step instructions, see [Migrate an account to another organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_account_migration.html) in the AWS Organizations User Guide.

**Important**  
Member accounts migrating from the original AWS Organizations to the new organization lose access to their historical billing data. Back up all billing reports before proceeding with migration.  
Verify that billing transfer is active before starting any member account transfers to maintain proper billing responsibility throughout the migration process.

**Step 5: Assign root user access to the new organization owner**

Sign in to the organization's root account and navigate to **My Account** in the AWS Management Console. Update the root user email address to the new organization owner's email address and complete the email verification process. The new organization owner receives an email to activate their root account access. They must then:
+ Create new credentials
+ Set up MFA
+ Accept account ownership

During this process, remove any partner MFA devices and partner-specific security configurations.

**Note**  
This step is required only for channel partners and their reselling end customers. It's optional for customers purchasing services directly from AWS.

### Option 3: Transfer ownership of an AWS organization before setting up billing transfer
<a name="orgs_transfer_billing-best-practices-prereq-2"></a>

This option involves handing over account ownership by providing root credentials controls of an existing AWS Organizations to a new owner and then transferring billing responsibility through billing transfer.

You might send a billing transfer invite from your existing organization or create a new organization dedicated to billing and financial management to send invites from.

**Prerequisites**

Your organization must meet these requirements:
+ Organization is in all-features mode
+ Customer has an email address for root account ownership
+ Organization serves one customer's workloads
+ Both parties involved in the account ownership transfer must review and comply with the [AWS Account Assignment requirements](https://aws.amazon.com/legal/aws-account-assignment-requirements/)

**Benefits**

This approach provides:
+ Reduced operational effort because linked account migration isn't required
+ Reduced risk of breaking workloads due to incompatible policies

**Important**  
Historical billing data from the previous root owner remains available to the new root owner.  
Root access must be handed over after the payment of the previous billing cycle is settled.  
For example:  
Billing Transfer effective date: Oct 1st
Previous billing cycle closure: Oct 3rd (Sept invoice delivered)
Payment is settled: Oct 4th
Root access hand-over: Oct 5th
If you are expecting to receive credit memos (i.e., refunds) and you expect to no longer be able to access the account retrieve credit memos, we recommend to transfer root after 30-60 days from the Billing Transfer on-boarding.

This option is suitable for:

- Channel partners who currently own root access to their end customers' AWS Organizations for AWS payment obligations and want to return root ownership to end customers

- Customers purchasing services directly from AWS who maintain central controls over governance and security to protect negotiated discount terms from unauthorized parties (such as teams, business units, affiliates, or subsidiaries)

**Step 1: Create a billing management organization (optional)**

If you don't have a management account to use as the bill transfer account, create a new account and configure AWS Organizations as described in [Tutorial: Creating and configuring an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html).

**Note**  
As a best practice, use this account exclusively for billing and financial management.

**Step 2: Set up billing transfer**

Establish billing transfer with the existing AWS Organizations:

In the AWS Billing and Cost Management console, choose **Preferences and Settings**, then **Billing Transfers**. Create a transfer from your bill transfer account to the existing management accounts that will become bill source accounts. If you're a channel partner, register your bill transfer account in Partner Central as a new Partner Management account before completing the transfer.

**Important**  
Before proceeding:  
Wait for billing transfer to become active on the first day of the next month.  
Back up Cost Explorer data from bill source accounts, as they lose historical data visibility when billing transfer becomes active.  
Create new preferences after billing transfer is active, as existing preferences become unhealthy and stop receiving data. Disable the split cost allocation data functionality when creating preferences.

**Step 3: Prepare for root access transfer**

After billing transfer is active, prepare to transfer bill source account ownership:

In the AWS Billing and Cost Management console, update the organization's billing information with the new owner's details. Remove your payment method and update the billing address.

**Note**  
AWS uses the bill transfer account's billing information for invoice generation while billing transfer is active. However, you must update the bill source account's billing information to prevent charges if billing transfer is withdrawn.

**Step 4: Transfer root access**

Sign in to the organization's root account and navigate to **My Account** in the AWS Management Console. Update the root user email address to the new owner's email domain and complete email verification. The new owner receives an email to activate their root account access. They must create new credentials, set up MFA, and accept account ownership.

**Important**  
Before transferring root ownership:  
Remove any existing MFA devices and security configurations.  
Back up any billing information you need, including invoices, s, and Cost Explorer reports.  
Note that the new owner will have access to historical billing data. Contact AWS Support with questions about historical data visibility.  
To prevent new owner access to historical billing data, use Option A instead.

**Step 5: Verify the transfer**

After the new owner accepts ownership, verify that billing transfer remains active and your organization continues receiving invoices. The new owner now has full root access to manage their organization while billing responsibility remains with your organization through billing transfer.

## Withdrawing from billing transfer
<a name="orgs_transfer_billing-best-practices-offboard"></a>

Any account can withdraw from billing transfer. For more information, see [Withdrawing transfers](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/orgs_transfer_billing-stop-transfer.html).

**Important**  
Before withdrawing from billing transfer:  
Back up historical data from Cost Explorer, as bill source accounts lose access to their pro forma historical data after withdrawal.  
Prepare to create new preferences, as existing reports are marked as unhealthy and stop receiving data after withdrawal.

**Note**  
The bill transfer account maintains access to historical data for bill source accounts after withdrawal.