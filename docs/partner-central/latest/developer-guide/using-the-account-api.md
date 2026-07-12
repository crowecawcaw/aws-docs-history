The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Using the AWS Partner Central Account API

## Managing partner account

Partner accounts are registered and linked with an existing AWS account to provide a full IAM-based experience. This approach eliminates the need for user-level credentials, ensuring that all registrations and operations are managed through IAM entity within the AWS account. AWS Partner Central enables seamless integration with AWS services, and this model provides partner entity management, supports multiple catalogs, and establishes an AWS account-level entitlement system.

Partners can utilize the available partner account APIs to register, manage, and update their accounts:

### Partner Registration API

Partners can register their account using their AWS account for Partner Engagement. Using the Create API, partners will provide required alliance lead information, accept APN terms, and provide a unique legal name.

### Partner Profile API

Partners manage profiles containing company details (name, description, website, logo) with public/private visibility control, asynchronous validation, and status tracking allowing one update at a time.

### Domain Management API

Partners can register and verify business domains through email validation to establish organizational identity and associate employees' training and certifications.

### Partner Connection API

Partners connect their AWS accounts with other AWS accounts for various purposes, such as collaborating on co-selling with other partners, sharing AWS Marketplace Offers data between accounts, authorizing distributors/channel partners to distribute/re-sell their products, and more.

### Partner Verification API

Partner verification is a mandatory prerequisite for partner account registration. Before partners can create a partner account, they must complete business verification and identity verification processes. These verifications validate that the business is legally registered and confirm the identity of the person registering the AWS account.

###### Topics

- [Working with Partner Registration](working-with-partner-registration.md "working-with-partner-registration.md")
- [Working with Partner Profile](working-with-partner-profile.md "working-with-partner-profile.md")
- [Working with Domain Management](working-with-domain-management.md "working-with-domain-management.md")
- [Working with Partner Account Connections](working-with-account-connections.md "working-with-account-connections.md")
- [Working with Partner Verification](working-with-partner-verification.md "working-with-partner-verification.md")
