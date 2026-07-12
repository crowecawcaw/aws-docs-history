The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Best practices

## Reacting to events

When handling events from AWS Partner Central API, ensure that your processing logic is
idempotent to handle duplicate events. Instead of making immediate [GetOpportunity](../APIReference/API_GetOpportunity.md "../APIReference/API_GetOpportunity.md") calls for each event, consider batching or selectively
fetching details based on your application's needs. For uninterrupted operations, beware
of [Quotas](quotas.md "quotas.md").

## Implementing optimistic locking

Optimistic locking prevents unintended data overrides during concurrent updates.
Here's a typical scenario:

1. Partner retrieves an opportunity from their CRM system.
2. User `A` updates the opportunity on AWS Partner Central.
3. User `B` updates the same opportunity at the same time through the
   CRM integration.
4. If the data changes, the CRM system attempts to upload the data but returns a
   `ConflictException`.
5. User reviews the error and manually resolves conflicting data.

To avoid this scenario, all [UpdateOpportunity](../APIReference/API_UpdateOpportunity.md "../APIReference/API_UpdateOpportunity.md") requests must include the `LastModifiedDate`
parameter, which you can obtain from previous [CreateOpportunity](../APIReference/API_CreateOpportunity.md "../APIReference/API_CreateOpportunity.md"), [UpdateOpportunity](../APIReference/API_UpdateOpportunity.md "../APIReference/API_UpdateOpportunity.md"), and [GetOpportunity](../APIReference/API_GetOpportunity.md "../APIReference/API_GetOpportunity.md") actions. The update succeeds only if
`LastModifiedDate` matches our system. If it doesn't, you must fetch the
latest `LastModifiedDate` using [GetOpportunity](../APIReference/API_GetOpportunity.md "../APIReference/API_GetOpportunity.md") and reattempt the update.

## Synchronizing data between CRM and AWS Partner Central

It is essential to keep your system synced with the latest data from Partner Central.
The following are two strategies to ensure your system reflects the latest data:

### Using events (recommended)

1. Load data using [ListOpportunities](../APIReference/API_ListOpportunities.md "../APIReference/API_ListOpportunities.md").
2. Subscribe to opportunity events.
3. Respond to new opportunities or changes.

   - When you receive `Opportunity Created`, `Opportunity
  Updated`, or `Engagement Invitation Accepted` events,
     use `GetOpportunity` to fetch the latest data.
   - When you receive `Engagement Invitation Rejected`
     events, remove the corresponding opportunities.

### Using ListOpportunities polling

1. Load data using [ListOpportunities](../APIReference/API_ListOpportunities.md "../APIReference/API_ListOpportunities.md").
2. Choose a polling frequency, ensuring it is not too frequent to avoid
   exhausting your daily [read quota](quotas.md "quotas.md").
3. Identify the latest `LastModifiedDate` from your stored data,
   ensuring it originates from AWS.
4. Use the timestamp in the `AfterLastModifiedDate` filter when
   calling [ListOpportunities](../APIReference/API_ListOpportunities.md "../APIReference/API_ListOpportunities.md").

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

5. AWS will return opportunities created or updated after the value
   indicated on the timestamp.
6. Iterate over all returned pages using `NextToken`, and update
   your system's data using [GetOpportunity](../APIReference/API_GetOpportunity.md "../APIReference/API_GetOpportunity.md").

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
