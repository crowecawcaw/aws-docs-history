# Limitations

###### Note

In an IDC implementation, when a Amazon Q Business knowledge base is first created in Amazon Quick Suite, access to the knowledge base is automatically granted to users with access to the selected Amazon Q Business index. For additional users to have access to a knowledge base, the admin must configure user access in both the Amazon Q Business console and Amazon Quick Suite knowledge base permissions pages.

When using Amazon Q Business indexes in Amazon Quick Suite, be aware of the following limitations:

## General Limitations

- Amazon Q Business index knowledge bases cannot be changed like other knowledge bases in Amazon Quick Suite.
- Amazon Q Business index knowledge bases only support the docs types supported by Amazon Q Business.
- QApps, Actions, and Amazon Q Business chat guardrails are not included in the BYOI capability.
- Amazon Q Business indexes must be in the same AWS account and region as Amazon Quick Suite.

## IDC Implementation Limitations

- Both Amazon Quick Suite and Amazon Q Business must use the same instance of IAM Identity Center.

## Index Quotas

- You can connect up to two Amazon Q Business indexes per Region to Amazon Quick Suite in the current release.
- This quota cannot be increased.
- Once indexes are selected and saved in a Amazon Quick Suite instance, they cannot be directly unselected.
