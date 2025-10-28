# Account considerations

Choosing the right AWS account for your AWS Marketplace seller registration is an important decision that will support your marketplace business. Here are key considerations to help you make the best choice:

## Choosing your seller account

AWS Marketplace recommends using a new account to register as a seller. This account will become the seller of record for your products and will be used for reporting, disbursement, and communication from AWS Marketplace to you.

###### Important

Once you register as a seller and list a product, you can't change the account associated with your products. All AWS Marketplace interactions will be tied to the account you choose, so it's worth taking time to select the right one.

Using a new account offers several advantages:

- Clean separation between your AWS Marketplace business and other AWS activities
- Simplified billing and financial tracking
- Easier compliance and audit management
- Reduced risk of account-related issues affecting your marketplace business

You can have multiple seller accounts if your business requires it. Each seller account corresponds to a separate AWS account and operates independently of AWS Organizations. Some sellers use multiple accounts for business and financial reasons, such as operating in multiple territories, separating different business units, or meeting specific compliance requirements.

###### Note

Each seller account must have a unique legal business name during registration. However, multiple seller accounts can use the same display name. Keep in mind that each seller account maintains its own separate product catalog and requires independent management.

If you prefer to use an existing account, you can do so as long as it was created after September 27, 2017.

## Tax inheritance and entity considerations

If you're planning to use an AWS account that's part of an AWS Organizations organization, be aware of how tax inheritance settings can affect your AWS Marketplace seller registration.

###### Important

When the management account in an AWS Organizations organization enables tax inheritance, member accounts inherit the management account's billing address and legal entity information. This can create conflicts if your seller account needs to represent a different business entity than the management account.

Tax inheritance affects AWS Marketplace sellers because:

- The billing address determines your seller business location and must match the information you provide in the AWS Marketplace Management Portal.
- Member accounts inherit the management account's legal entity when tax inheritance is enabled.
- This inheritance can prevent you from accurately representing your business entity in different regions or countries.

### Recommendations for multi-entity businesses

If your management account represents a different business entity (for example, a US entity) than your intended seller account (for example, an Australian entity), we recommend one of the following approaches:

- **Use a standalone account:** Create a standalone AWS account that's not part of any organization for your AWS Marketplace seller registration.
- **Create a separate organization:** Set up a new AWS Organizations organization where all accounts represent the same business entity as your intended seller account.

This consideration is particularly important as AWS Marketplace continues to expand to new regions and marketplaces globally, including Korea, India, and other international markets.

###### Note

For more information about tax inheritance in AWS Organizations, see [Managing tax inheritance for linked accounts](../../../awsaccountbilling/latest/aboutv2/manage-account-payment.md#manage-account-tax-linked-accounts "../../../awsaccountbilling/latest/aboutv2/manage-account-payment.md#manage-account-tax-linked-accounts") in the _AWS Billing User Guide_.

## Setting up secure access

For security best practices, we recommend using AWS Identity and Access Management (IAM) roles to sign in to the AWS Marketplace Management Portal rather than using your root account credentials. For comprehensive security guidance, see [AWS Marketplace security](security.md "security.md").

You can also configure your account to allow multiple users with different permissions to access the AWS Marketplace Management Portal. For more information about setting up user access, see [Controlling access to
AWS Marketplace Management Portal](marketplace-management-portal-user-access.md "marketplace-management-portal-user-access.md").

## Setting up communications

The root/main email address for your AWS Marketplace seller account is critical for receiving essential communications, including important compliance notifications and urgent account updates. This email address must be regularly monitored by your AWS Marketplace team and cannot be an alias address, as certain AWS teams can only communicate with the registered root email address.

###### Important

Your root email address serves as the primary communication channel for critical AWS Marketplace business operations. Failure to monitor this email address could result in missed compliance deadlines, payment issues, or account suspension.

When setting up your seller account email address, ensure it meets these requirements:

- **Direct email address:** Must be a real email address, not an alias or distribution list, as certain AWS teams can only send emails to the registered root address
- **Regular monitoring:** Must be actively monitored by your AWS Marketplace team for time-sensitive communications
- **Organizational access:** Should be accessible by appropriate contacts within your organization who can respond to urgent matters
- **Business continuity:** Consider using a role-based email address (such as marketplace-team@yourcompany.com) rather than an individual's personal email to ensure continuity

## Ready to register?

Once you've selected your account, you can begin the seller registration process. For step-by-step registration instructions, see [Registration process](registration-process.md "registration-process.md").
