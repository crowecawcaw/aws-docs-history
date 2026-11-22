

# Plan your Quick account structure and AWS Regions

This topic describes the recommended way to structure AWS Quick for your organization, how a single account operates across AWS Regions, and the role of your home Region.

**Topics**
+ [Recommended account structure](#recommended-account-structure)
+ [How a single account works across AWS Regions](#quick-across-regions)
+ [Your home Region](#home-region)

## Recommended account structure
<a name="recommended-account-structure"></a>

We recommend that you use a single AWS Quick account for your organization. A single account gives you one place to connect all of your apps and data, one place to manage users, and one place to manage fine-grained permissions. This makes it easier to apply consistent governance, share assets, and audit access across your organization.

To keep teams, projects, or business units separate within a single account, use namespaces. Namespaces provide logical isolation of users and resources while you maintain centralized account management. For more information, see [Supporting multitenancy with isolated namespaces](namespaces.md).

To keep Quick subscription creation centralized on your approved account, you can use service control policies in AWS Organizations. For more information, see [Using service control policies to restrict AWS Quick sign-up options](security-scp-admin.md).

## How a single account works across AWS Regions
<a name="quick-across-regions"></a>

AWS Quick is available in multiple AWS Regions. A single AWS Quick account spans all available AWS Quick Regions. After you sign up, you can create and use assets in any available AWS Quick Region, and those assets live in the Region where you create them. These assets include datasets, knowledge bases, agents, spaces, flows, and dashboards. Each AWS account can have one AWS Quick subscription, and that subscription can be used in multiple AWS Regions.

Capacity is managed separately in each Region. SPICE capacity and Quick Index capacity are allocated per AWS Region, so you provision capacity in each Region where you work with data.

## Your home Region
<a name="home-region"></a>

Your home Region is the AWS Region that you select when you set up your AWS Quick subscription. It is also called your account's identity Region, the Region that anchors your AWS Quick account identity and user sign-in. Your home Region must be a supported AWS Quick Region.

Your home Region also sets your default capacity behavior. AWS Quick automatically creates your index in your home Region with auto-scaling, and your Index capacity allocation is billed against your home Region. If you provision Index capacity in Regions beyond your home Region, that capacity is billed as overage.

For the list of supported Regions, and for how Amazon Q in Quick processes AI inference across Regions within your geography, see [AWS Regions and related information](regions.md) and [Cross-Region inference](regions.md#cross-region-inference).