# Co-selling and partners

Manage co-selling opportunities and channel partner selling authorizations.

## Managing co-selling opportunities

You can track, update, and manage your co-selling opportunities from the Co-Selling
Opportunities page. The page provides a pipeline view of all opportunities.

### To view opportunities

1. In your connected account, choose **Co-Selling Opportunities**.
2. The opportunities table displays the following columns:

   - Source
   - Status
   - Stage
   - Opportunity ID
   - Customer Company Name
   - Project Title

3. Use the All Opportunities dropdown to filter; the Source column shows
   whether an opportunity is AWS-originated or partner-originated.
4. The following filters are available:

   - Search
   - All Opportunities dropdown
   - Sync
   - Refresh

5. Status values are: Pending Submission, Submitted, and Approved.

### To view additional details

The opportunity detail view includes:

- **Activity history** - Timeline of stage
  changes and updates
- **AWS feedback** - Comments or guidance from
  AWS (for accepted opportunities)
- **Related offers** - Private offers created
  for this opportunity
- **Contacts** - Customer and AWS contacts
  associated

### Opportunity pipeline

The pipeline summary at the top of the Co-Selling Opportunities page shows the
following cards:

- All Opportunities
- AWS Originated
- Partner Originated
- Estimated pipeline revenue
- WIN rate
- Validation rate

### Notes

- Opportunities synced with ACE follow AWS co-selling program rules. See
  your partner agreement for eligibility requirements.
- Received opportunities (from AWS) may include referral benefits or
  technical support offers.
- Archiving an opportunity removes it from the active view but retains it
  for reporting.

### Related topics

- Creating co-selling opportunities
- AWS ACE connector
- Co-selling automation

## Selling Authorizations

Selling authorizations allow you to authorize channel partners to resell your products
through their own storefronts or directly to their buyers via Channel Partner Private
Offers (CPPO).

### To view selling authorizations

1. In your connected account, choose **Selling
   Authorizations**.
2. The list displays:

   - Authorization ID
   - Partner name and AWS Account ID
   - Product name
   - Status (Active, Expired, Revoked)
   - Authorization date
   - Expiration date

### To create a selling authorization

1. Choose **Create Authorization**.
2. Complete the form:

   - **Partner AWS Account ID** - The
     reseller's 12-digit AWS account ID
   - **Product** - Select the product to
     authorize for resale
   - **Pricing** - Set the wholesale price
     or discount for the partner
   - **Duration** - How long the
     authorization is valid
   - **Terms** - Any additional resale
     terms or restrictions

3. Choose **Create**.

The partner receives notification and can begin creating CPPOs for your
product.

### Managing authorizations

- **Revoke** - Cancel an active authorization.
  The partner can no longer create new CPPOs, but existing agreements remain
  active.
- **Extend** - Extend the expiration date of an
  authorization.
- **Edit** - Modify pricing or terms (applies
  to future CPPOs only).

### Notes

- Selling authorizations are managed through the AWS Marketplace Catalog API.
  Ensure your connected account has the required permissions.
- For more information about how CPPO works, see [Channel Partner Private Offers](../userguide/channel-partner-offers.md "../userguide/channel-partner-offers.md") in the AWS Marketplace Seller
  Guide.

### Related topics

- Creating offers
- Connecting your AWS Marketplace account
