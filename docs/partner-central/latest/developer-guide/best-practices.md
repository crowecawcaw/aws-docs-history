

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Best practices
<a name="best-practices"></a>

## Reacting to events
<a name="reacting-to-events"></a>

When handling events from AWS Partner Central API, ensure that your processing logic is idempotent to handle duplicate events. Instead of making immediate [GetOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetOpportunity.html) calls for each event, consider batching or selectively fetching details based on your application's needs. For uninterrupted operations, beware of [Quotas](quotas.md).

## Implementing optimistic locking
<a name="implementing-optimistic-locking"></a>

Optimistic locking prevents unintended data overrides during concurrent updates. Here's a typical scenario:

1. Partner retrieves an opportunity from their CRM system.

1. User `A` updates the opportunity on AWS Partner Central.

1. User `B` updates the same opportunity at the same time through the CRM integration.

1. If the data changes, the CRM system attempts to upload the data but returns a `ConflictException`.

1. User reviews the error and manually resolves conflicting data.

To avoid this scenario, all [UpdateOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UpdateOpportunity.html) requests must include the `LastModifiedDate` parameter, which you can obtain from previous [CreateOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateOpportunity.html), [UpdateOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UpdateOpportunity.html), and [GetOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetOpportunity.html) actions. The update succeeds only if `LastModifiedDate` matches our system. If it doesn't, you must fetch the latest `LastModifiedDate` using [GetOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetOpportunity.html) and reattempt the update.

## Synchronizing data between CRM and AWS Partner Central
<a name="synchronizing-data"></a>

It is essential to keep your system synced with the latest data from Partner Central. The following are two strategies to ensure your system reflects the latest data:

### Using events (recommended)
<a name="using-events"></a>

1. Load data using [ListOpportunities](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListOpportunities.html).

1. Subscribe to opportunity events.

1. Respond to new opportunities or changes.
   + When you receive `Opportunity Created`, `Opportunity Updated`, or `Engagement Invitation Accepted` events, use `GetOpportunity` to fetch the latest data.
   + When you receive `Engagement Invitation Rejected` events, remove the corresponding opportunities.

### Using ListOpportunities polling
<a name="using-listopportunities-polling"></a>

1. Load data using [ListOpportunities](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListOpportunities.html).

1. Choose a polling frequency, ensuring it is not too frequent to avoid exhausting your daily [ read quota](quotas.md).

1. Identify the latest `LastModifiedDate` from your stored data, ensuring it originates from AWS.

1. Use the timestamp in the `AfterLastModifiedDate` filter when calling [ListOpportunities](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListOpportunities.html).

   ```
   {
      "FilterList": [
          {
              "Name": "AfterLastModifiedDate",
              "ValueList": [ "2023-05-01T20:37:46Z" ] // Replace with actual timestamp of your last synced data
           }
      ]
   }
   ```

1. AWS will return opportunities created or updated after the value indicated on the timestamp.

1. Iterate over all returned pages using `NextToken`, and update your system's data using [GetOpportunity](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetOpportunity.html).

   ```
   {
      "NextToken": "AAMA-EFRSN...PZa942D",
      "FilterList": [
          {
              "Name": "AfterLastModifiedDate",
              "ValueList": [ "2023-05-01T20:37:46Z" ] // Replace with actual timestamp of your last synced data
           }
      ]
   }
   ```