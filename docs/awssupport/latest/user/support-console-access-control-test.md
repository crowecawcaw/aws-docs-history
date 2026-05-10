# Testing Support Center Console API calls

To validate that your IAM policies are correctly configured for Support Center Console API
operations, open the [AWS Support Center Console](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support") to generate
recent API calls.

To check for missing IAM permissions, complete the following steps:

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail](https://console.aws.amazon.com/cloudtrail "https://console.aws.amazon.com/cloudtrail").
2. Check the AWS Region dropdown to make sure that you're in the **US East (N. Virginia)** Region.
3. In the navigation pane, choose **Event history**.
4. Filter by event source **support-console.amazonaws.com**.
5. Match the event names to the list of `support-console:*` operations in [Adding IAM policies for the Support Center Console API operations](support-console-access-control.md "support-console-access-control.md") (for example,
   `GetAccountState`).
6. Open the matching events and check for an `additionalEventData` field
   containing an `authZHeader` entry. If present, your IAM policy is missing the
   permission listed in that entry.
7. Add the specific `support-console` permission to your IAM policy. You can
   grant access to all operations using `support-console:*`, or select individual
   operations for fine-grained control. For the full list of operations, see [Adding IAM policies for the Support Center Console API operations](support-console-access-control.md "support-console-access-control.md").
8. To verify the fix, revisit the AWS Support Center Console to generate new API calls, then repeat
   steps 1–6. Make sure that the new events no longer contain an `additionalEventData`
   field.
