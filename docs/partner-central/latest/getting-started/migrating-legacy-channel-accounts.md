# Migrating legacy channel accounts

This guide explains how AWS Channel Partners can migrate their existing channel end customers in partner-controlled AWS Organizations to billing transfer, enabling customers to maintain independent AWS Organizations while partners retain billing responsibility.

Channel Partners have two options to migrate existing end customer accounts to billing transfer:

## Full Organization Transfer

Transfer your existing AWS Organization to customer ownership while maintaining billing responsibility through billing transfer. This process involves transferring root account ownership to the customer after establishing billing transfer, preserving all existing organization configurations and service integrations.

**Benefits:**

- Maintains all existing organization configurations
- Minimizes technical complexity and migration time
- Preserves service dependencies and integrations

**Important Considerations:**

- Best suited for single-tenant organizations
- Historical billing data becomes visible to the customer
- Partner must set up billing transfer before transferring root ownership

## Member Account Transfer

Move individual member accounts from your existing AWS Organization to a new customer-owned Organization. This process involves creating a new Organization for the customer, establishing billing transfer, then migrating member accounts.

**Benefits:**

- Maintains billing privacy throughout migration
- Provides flexibility in migration scheduling
- Works for both single-tenant and multi-tenant organizations

**Important Considerations:**

- Requires rebuilding Organization-level configurations
- Organization-level dependencies must be identified and recreated
- Longer migration timeline than full organization transfer

###### Topics

- [Transferring Organization ownership](transferring-organization-ownership.md "transferring-organization-ownership.md")
- [Transferring member accounts](transferring-member-accounts.md "transferring-member-accounts.md")
