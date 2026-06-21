# Governance

Control procurement approvals and product visibility with buyer groups, policies, and segments.

## Groups and auto-approval

You can create buyer groups within your storefront to organize users and configure
automatic approval rules for procurement requests. Groups determine which approval
policies apply to different sets of buyers.

### What are groups?

A group is a collection of buyers who share the same procurement rules. For
example, you might create groups for:

- Engineering department (auto-approve requests from trusted domains)
- Procurement team (manual approval for all requests)
- Auto-approved (buyers whose requests were automatically approved)

### To create a group

1. Open the storefront and choose the **Governance** tab.
2. Choose **Groups**.
3. Choose **Add Group**.
4. Enter the **Group name** and optional
   **Description**.
5. Choose **Save**.

### Auto-Approval Settings

Auto-Approval is governed by the **Auto-Approval Settings** panel. Turn on **Enable Auto-Approval**, then add up to 20 **Trusted Email Domains**. Users who sign up with an email in a trusted domain are added to the Auto-approved group, and admins receive an email notification. Choose **Save Settings**.

For example, if you add `example.com` as a trusted email domain, any user who signs up with an `@example.com` address is automatically approved.

### To add members to a group

1. In the **Groups** section, choose the
   group.
2. Choose **Add Members**.
3. Search for and choose buyers by email or name.
4. Choose **Save**.

### Auto-approval workflow

When auto-approval is enabled:

1. A user signs up for the storefront.
2. The system checks whether the user's email domain matches one of the
   **Trusted Email Domains**.
3. If the domain matches, the user is added to the **Auto-approved**
   group automatically.
4. Admins receive an email notification when a user is
   auto-approved.
5. If the domain does not match, the request routes to the assigned
   approver or follows the configured policy.

### Notes

- A buyer can belong to only one group at a time.
- Buyers not assigned to any group follow the storefront's default
  governance policy.
- Group assignments can be changed at any time. Changes apply to future
  requests only.
- You can manage up to 20 **Trusted Email Domains** per storefront.

### Related topics

- [Policies](#policies "#policies")
- [Segments](#segments "#segments")
- [Governance: User management](#user-management "#user-management")

## Policies

Governance policies define the rules that control how procurement requests are
approved on your storefront. Policies set approval chains and conditions
that determine whether a request requires manual review.

### What is a policy?

A policy is a set of rules that evaluate incoming Buy With AWS requests and
determine the approval path. Policies can be applied to specific segments or to the
entire storefront as a default.

### To create a policy

1. Open the storefront and choose the **Governance** tab.
2. Choose **Policies**.
3. Choose **Create Policy**.
4. In the dialog, use the enable/disable toggle in the header to control whether the policy is active. Configure the following fields:

   - **Name** - A descriptive name
     for the policy
   - **Action** - Choose an action from the Select action dropdown
   - **Which segments will this apply to?** - A multi-select to choose the segments this policy applies to
   - **What order amount should trigger the action?** - Choose Any amount, Orders above, or Orders below
   - **Add a message** - Optional, up to 500 characters

5. Choose **Create**.

### Policy assignment

Policies apply to segments through the **Which segments will this apply to?** multi-select inside the dialog.

### Default policy

If no policy applies to a product's segments, the storefront's default policy applies.
To set the default:

1. In the **Policies** section, find the policy
   you want as default.
2. Choose the actions menu and choose **Set as
   Default**.

### Policy evaluation order

1. The system identifies the segments that contain the requested product.
2. The system applies the policies assigned to those segments.
3. The configured action is executed.

### Notes

- A policy applies to the segments selected in the **Which segments will this apply to?** multi-select.
- Policies evaluate per-request.
- Changing a policy affects future requests only. In-progress requests
  follow the policy that was active at submission time.

### Related topics

- [Groups and auto-approval](#groups-and-auto-approval "#groups-and-auto-approval")
- [Segments](#segments "#segments")
- [Governance: User management](#user-management "#user-management")

## Segments

Segments allow you to define subsets of your storefront's product catalog that are
visible to specific groups of buyers. Use segments to create tailored browsing
experiences where different buyer groups see different products.

### What is a segment?

A segment is a filter that controls product visibility per buyer group. For
example:

- "Enterprise" segment shows only enterprise-tier products
- "SMB" segment shows starter and mid-tier products
- "Security" segment shows only security-category products

### To create a segment

1. Open the storefront and choose the **Governance** tab.
2. Choose **Segments**.
3. Choose **Create Segment**.
4. Configure the segment criteria:

   - **Name** - A descriptive name for the segment
   - **Type** - Choose a type from the dropdown

5. Choose **Create**.

### To assign a segment to a group

1. In the **Segments** section, choose the
   segment.
2. Choose **Assign to Group**.
3. Choose the buyer group(s) that should see this segment's products.
4. Choose **Save**.

### How segments affect the buyer experience

- Buyers in a group with an assigned segment see only the products in that
  segment when browsing the storefront.
- Buyers not assigned to any segment see the full product catalog.
- Segments filter the catalog view only. They do not prevent buyers from
  accessing product URLs directly.

### Notes

- A group can be assigned one segment. To show multiple segments to a group,
  combine the products into a single segment.
- Segments do not affect product availability in AWS Marketplace. They
  control visibility within the storefront only.
- Changes to segment assignments take effect immediately.

### Related topics

- [Groups and auto-approval](#groups-and-auto-approval "#groups-and-auto-approval")
- [Policies](#policies "#policies")
- Categories and badges

## Governance: User management

You can manage buyer access to your storefront at the governance level. This includes
adding buyers, assigning them to groups, and controlling their visibility and approval
settings.

### Adding buyers

Buyers are added to your storefront's governance system when they:

- Are manually added by an admin
- Submit a storefront access request (if enabled)
- Are imported via a buyer list

#### To manually add a buyer

1. Open the storefront and choose the **Governance** tab.
2. Choose **Users**.
3. Choose **Add User**.
4. Complete the following fields:

   - **Title**
   - **Email**
   - **First Name**
   - **Last Name**
   - **Company**
   - **Group** - The Group dropdown defaults to Public.
   - **Status**
   - **Approval Required** (checkbox)

5. Choose **Add User**.

### Viewing and managing buyers

The Users section displays all buyers with access to your storefront:

| Column  | Description                           |
| ------- | ------------------------------------- |
| Name    | Buyer's display name                  |
| Email   | Buyer's email address                 |
| Group   | Assigned governance group             |
| Segment | Product segment visible to this buyer |
| Status  | Active or inactive                    |
| Added   | Date the buyer was added              |

#### To edit a buyer's group assignment

1. In the **Users** list, locate the
   buyer.
2. Choose the **Group** dropdown for that
   buyer.
3. Choose the new group.
4. The change is saved automatically.

#### To remove a buyer

1. In the **Users** list, locate the
   buyer.
2. Choose the actions menu and choose **Remove**.
3. Confirm the removal.

The buyer loses access to governance-controlled features (auto-approval,
segments) but can still browse the public storefront.

### Bulk operations

For storefronts with many buyers, you can:

- **Import buyers** via CSV (email and group
  assignment)
- **Export buyer list** as CSV for offline
  review

### Notes

- Governance user management is separate from team member management. Team
  members manage the storefront; governance users are the buyers who use
  it.
- Removing a buyer from governance does not block them from visiting the
  storefront URL. It removes them from group policies and segment
  restrictions.

### Related topics

- [Groups and auto-approval](#groups-and-auto-approval "#groups-and-auto-approval")
- [Segments](#segments "#segments")
- [Policies](#policies "#policies")
- RBAC and custom roles
