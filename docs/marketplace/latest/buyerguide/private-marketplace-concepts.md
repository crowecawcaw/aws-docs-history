# Private Marketplace concepts

This topic explains some of the key concepts for Private Marketplace.

## Experience

A Private Marketplace experience is a curated catalog of approved products with custom branding that allows you to control what users in your organization can procure from AWS Marketplace. To govern users, you associate the audience containing the user with a **Live** experience. Audiences can be the entire organization, organizational units (OUs), or accounts in your Organizations. You can create multiple experiences with specific procurement controls for different audiences.

### Experience status

The status of an experience determines if the experience is available to govern users. An experience can have two statuses:

- **Live –** The experience is active and will govern users in the audience that the experience is associated with. Admins can continue to make updates and manage products.
- **Not live –** The experience is created but not yet available to govern users. Admins can continue to make updates and configure settings. It can be set to **Live** when ready for users.

### Experience mode

The mode of an experience determines whether the experience can be updated and used to govern users. An experience can have two modes:

- **Active –** Active experiences can be updated and used to govern users. You can continue to make updates and manage products in active experiences.
  - When an active experience is **Live** and associated with an audience, all users in that audience will be governed by the experience.
  - When an active experience is **Not live**, it will not govern any users even when it is associated with an audience.

- **Archived –** Archived experiences cannot be modified and used to govern users. An archived experience has to be reactivated, if you want to use it again. Archiving an experience can be thought as soft deleting an experience and preventing active use with ability to reactivate and use it again, if required.

## Audience

Each hierarchical unit in Organizations — organization, organizational units (OUs), or accounts — can be an audience for an experience. You can think of audiences as nodes in the organization structure of Organizations hierarchy. Read more about [Organization structure](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#organization-structure "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#organization-structure") in the AWS Organizations user guide.

With Private Marketplace, you can provide specific procurement experiences to different audiences in your organization based on their business needs. You do this by associating an experience with an audience.

Experiences flow down through the audience hierarchy — when applied at a higher level, all lower levels inherit it automatically. To override an inherited experience, you can associate the audience at a lower level with a different experience.

## Associated audience

An experience can be directly associated with multiple audiences collectively termed as **associated audiences**.

When an experience is **Live**, it will govern the associated audiences. Users in the associated audiences will only be allowed to procure products approved in the experience. The associated audiences will not inherit any product approvals from experiences associated at a higher level in the organization hierarchy.

When an experience is **Not live**, it will not govern the associated audiences. The associated audiences will inherit product approvals from the first **Live** experience associated at a higher level in the organization hierarchy.

## Governing experience

An audience will only be governed by a single experience at a point in time. This is referred to as the **governing experience**. When an experience is governing an audience, users in that audience will only be allowed to procure products approved in the experience. The governing experience is determined by the status of the experience, its associated audiences, and the organization hierarchy.

The governing experience and its audience relationship can be **Associated** when an audience is directly associated with an experience and **Inherited** when it inherits from an experience at a higher level. Read more about [Governance hierarchy](#governance-hierarchy "#governance-hierarchy") to understand how experience inheritance works.

## Default governing experience

The default governing experience governs the entire organization, excluding organizational units and accounts that are directly associated with other **Live** experiences. It is recommended to configure a default governing experience to govern your entire organization. The default governing experience should be curated with products that you approve for all users in your organization.

To configure a default governing experience for your organization, create an experience, select the products that you approve for procurement in your organization, and associate your organization root as the audience for the experience. After the experience is set to **Live**, users in your organization will only be allowed to procure AWS Marketplace products that you approved in the default governing experience. For more information, see [Configuring Private Marketplace](configure-private-marketplace.md "configure-private-marketplace.md") for steps to create and configure an experience.

If you have organizational units (OUs) or accounts with specific procurement needs, you can create additional experiences with different sets of approved products and associate them to these audiences.

## Governance hierarchy

Private Marketplace provides hierarchical governance that is aligned with [Organizations hierarchy](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#organization-structure "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#organization-structure"). With Private Marketplace, you can create multiple experiences and associate them to your entire organization, AWS organizational units (OUs), or AWS accounts. This allows you to scale your procurement governance as your business needs evolve. If you update your organization hierarchy within Organizations, Private Marketplace updates the governance accordingly.

Here are the different levels of audience associations and the effect for each. Note that the status of an experience is also a factor to determine the governance. An experience will govern an audience only when it is set to **Live**. The effects described below assume a **Live** experience. When an experience associated with an audience is **Not live**, the audience inherits the **Live** experience at the next higher level.

- **Organization association –** When you associate an experience with the organization root, all OUs and accounts in the organization inherit the experience. All users in the organization will be governed by the experience and will only be allowed to procure products approved in the experience.
- **OU association –** When you associate an experience with a specific OU, it does not inherit experiences set at higher levels in the hierarchy. Accounts that are directly under that OU or any child OU inherit the experience associated with that OU. Users in accounts that are directly under that OU or any child OU will be governed by the experience and will only be allowed to procure products approved in the experience.
- **Account association –** When you associate an experience with a specific account, it does not inherit experiences set at higher levels in the hierarchy. Users in the account will be governed by the experience and will only be allowed to procure products approved in the experience.

In summary, the experience that is **Live** and closest to an account in the organization hierarchy takes effect and governs that account.

The following example explains how experiences in an organization govern different accounts:

- An organization has a default experience that is live and applies to the entire organization. All accounts within the organization are restricted to procuring only the products approved in this default experience.
- The finance department has its own unit experience that is live and associated with its Organizational Unit (OU). All accounts under this OU are limited to procuring only the products approved in the finance unit experience. They cannot access products available in the default experience.
- An individual account, let's call it account A, has its own experience that is live and specifically associated with it. Users in account A can only procure products approved in the account A experience.
- Another department, marketing, has a unit experience created but not yet live. It is associated with the marketing department's OU. However, since this experience is not live, the accounts under the marketing OU continue to be governed by the default experience. They can only procure products approved in the default experience, not those in the marketing unit experience, which is not live.

## Managed products

As an administrator, you can approve or decline products from experiences in your organization. These are referred to as managed products. A product could be approved in one of your experiences to allow a subset of users to procure the product. The same product could be denied in another experience to not allow a different set of users from procuring it.

Private Marketplace provides multiple ways to manage products and visualize the product availability in experiences. See the following topics for more details:

- [View governance details and manage products](view-governance-details.md "view-governance-details.md")
- [Managing products in an experience](manage-experiences.md#manage-products-in-an-experience "manage-experiences.md#manage-products-in-an-experience")
- [Approval status of a product in experiences](approval-status-of-a-product-in-experience.md "approval-status-of-a-product-in-experience.md")
