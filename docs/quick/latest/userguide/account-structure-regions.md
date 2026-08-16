# Plan your Quick account structure and AWS Regions

This topic describes the recommended way to structure Amazon Quick for your organization,
how a single account operates across AWS Regions, and the role of your home
Region.

###### Topics

- [Recommended account structure](#recommended-account-structure "#recommended-account-structure")
- [How a single account works across AWS Regions](#quick-across-regions "#quick-across-regions")
- [Your home Region](#home-region "#home-region")

## Recommended account structure

We recommend that you use a single Amazon Quick account for your organization. A single
account gives you one place to connect all of your apps and data, one place to manage
users, and one place to manage fine-grained permissions. This makes it easier to apply
consistent governance, share assets, and audit access across your organization.

To keep teams, projects, or business units separate within a single account, use
namespaces. Namespaces provide logical isolation of users and resources while you
maintain centralized account management. For more information, see [Supporting multitenancy with isolated namespaces](namespaces.md "namespaces.md").

To keep Quick subscription creation centralized on your approved account,
you can use service control policies in AWS Organizations. For more information, see [Using service control policies to restrict Amazon Quick sign-up options](security-scp-admin.md "security-scp-admin.md").

## How a single account works across AWS Regions

Amazon Quick is available in multiple AWS Regions. A single Amazon Quick account
spans all available Amazon Quick Regions. After you sign up, you can create and use
assets in any available Amazon Quick Region, and those assets live in the Region where
you create them. These assets include datasets, knowledge bases, agents, spaces, flows,
and dashboards. Each AWS account can have one Amazon Quick subscription, and that
subscription can be used in multiple AWS Regions.

Capacity is managed separately in each Region. SPICE capacity and Quick
Index capacity are allocated per AWS Region, so you provision capacity in each Region
where you work with data.

## Your home Region

Your home Region is the AWS Region that you select when you set up your
Amazon Quick subscription. It is also called your account's identity Region, the Region
that anchors your Amazon Quick account identity and user sign-in. Your home Region must
be a supported Amazon Quick Region.

Your home Region also sets your default capacity behavior. Amazon Quick automatically
creates your index in your home Region with auto-scaling, and your Index capacity
allocation is billed against your home Region. If you provision Index capacity in Regions
beyond your home Region, that capacity is billed as overage.

For the list of supported Regions, and for how Amazon Q in Quick processes AI inference across
Regions within your geography, see [AWS Regions, websites, IP address ranges, and endpoints](regions.md "regions.md") and
[Cross-Region inference for Australia, Japan, Europe, and the United States](regions.md#cross-region-inference "regions.md#cross-region-inference").
