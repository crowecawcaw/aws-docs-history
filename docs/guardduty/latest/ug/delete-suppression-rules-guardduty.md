# Deleting suppression rules in

GuardDuty

This section provides the steps to delete a suppression rule in your AWS account in
a specific AWS Region.

You may want to delete a suppression rule that no longer depicts an expected behavior
in your environment. You no longer want to suppress the associated finding type so that
GuardDuty can generate a finding type.

If you're a member account, your administrator account can take this action on your behalf. For more
information, see [Administrator account and member
account relationships](administrator_member_relationships.md "administrator_member_relationships.md").

Choose your preferred access method to delete a suppression rule for GuardDuty finding
types.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. On the **Findings** page, choose
   **Suppress Findings** to open the suppression
   rule panel.
3. From the **Saved rules** drop down, choose a
   saved filter.
4. Choose **Delete rule**.

API/CLI
Run the [DeleteFilter](../APIReference/API_DeleteFilter.md "../APIReference/API_DeleteFilter.md") API. Specify the filter name
and the associated detector ID for the particular Region.

Alternatively, you can use the following AWS CLI example by replacing the
values formatted in `red`:

```
aws guardduty delete-filter --region `us-east-1` --detector-id `12abc34d567e8fa901bc2d34e56789f0` --filter-name `filterName`
```

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.
