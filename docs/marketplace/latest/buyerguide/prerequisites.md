

# Prerequisites
<a name="prerequisites"></a>

To use Private Marketplace, you need one or more AWS accounts managed in AWS Organizations with all features enabled.
+ Create an organization using [Tutorial: Creating and configuring an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html).
+ If you have an existing organization with only consolidated billing feature, enable all features using [Enabling all features for an organization with Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html).

## Integration with AWS Organizations
<a name="integration-with-aws-organizations"></a>

Before you can start creating Private Marketplace experiences and using them to control what your users can purchase from AWS Marketplace, you must enable trusted access in Organizations and create a service-linked role.

### Trusted access in AWS Organizations
<a name="trusted-access-in-aws-organizations"></a>

You must enable trusted access in Organizations to make Private Marketplace a trusted service that can perform tasks in your organization and its accounts on your behalf. For more information, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).

Trusted access in Organizations is essential for Private Marketplace to keep the governance in sync with changes in your Organizations structure. If you disable trusted access, it turns off Private Marketplace governance completely. All your audiences will be disassociated from Private Marketplace experiences, and all users in your organization will be able to procure any product from AWS Marketplace.

**Important**  
We **strongly recommend** enabling trusted access using AWS Marketplace console which will also create the required service-linked role. If you enable trusted access using the Organizations console or API, it will not create the service-linked role. You must first create the service-linked role using AWS Identity and Access Management (IAM).
Do not disable trusted access unless you are certain that you do not require Private Marketplace governance for your entire organization. There are less disruptive ways to turn off or update governance for parts of your organization. For more information, see [Updating experience configuration](manage-experiences.md#update-experience-configuration) and [Managing audience associations for an experience](manage-experiences.md#manage-audience-associations-for-an-experience).

### Service-linked role for Private Marketplace
<a name="service-linked-role-for-private-marketplace"></a>

You must create the `AWSServiceRoleForPrivateMarketplaceAdmin` service-linked role in the management account. It includes the permissions that are required to access data from Organizations and manage Private Marketplace resources on your behalf. For more information about the service-linked role, see [Using roles to configure Private Marketplace in AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/using-service-linked-roles-private-marketplace.html).

**Note**  
If you have been using Private Marketplace without Organizations integration or using it to govern individual accounts that are not in Organizations, you will not be able to use the new features launched since February 16, 2024.  
To use the latest features, an administrator in the Organizations management account must create an integration for Private Marketplace. This is a prerequisite to use the AWS Marketplace console for managing Private Marketplace. The website for managing Private Marketplace will be deprecated on March 17, 2026. The integration is also required to use the features for organizational unit (OU) support and user request notifications noted in the following topics:  
[AWS Marketplace now supports managing Private Marketplace catalogs for organizational units](https://aws.amazon.com/about-aws/whats-new/2024/02/aws-marketplace-private-marketplace-catalogs-organizational-units/)
[AWS Marketplace now supports notifications for Private Marketplace](https://aws.amazon.com/about-aws/whats-new/2024/10/aws-marketplace-notifications-private-marketplace/)