# Changing your private marketplace

status

After you are satisfied with the experience's product list, the marketplace's branding
settings, and the associated account groups, then you can make your private marketplace live.
From the **AWS Private Marketplace** administrator's page, select
**Experience** in the left navigation pane, then select the experience you
want to enable. On the **Settings** tab, you can change the private
marketplace status between **Live** (enabled) and **Not
live** (disabled).

When your private marketplace is live, end users can buy only the products that you have
approved. When your private marketplace is disabled, you retain the list of products. However,
disabling a private marketplace removes the restriction from users in your AWS Organizations
organization. As a result, they can subscribe to any products in the public AWS Marketplace.

Making a private marketplace live does not disrupt active Amazon Machine Images (AMIs)
running on Amazon Elastic Compute Cloud (Amazon EC2) instances. As a best practice, ensure that all AWS Marketplace products
currently in use across your organization are included in your private marketplace. It's also
a best practice to have a plan in place to discontinue use of unapproved products before
making the private marketplace live. After the private marketplace is live, all new
subscriptions or renewals are governed by the products approved in the private marketplace
catalog.
