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
2. On the **Suppression rules** page, select the suppression rule to delete.
3. From the **Actions** dropdown, select **Delete suppression rule**.
4. It prompts a confirmation pop-up. Select **Delete** to proceed with the deletion.
   Or select **Cancel** to cancel the operation.

API/CLI
Run the [DeleteFilter](../APIReference/API_DeleteFilter.md "../APIReference/API_DeleteFilter.md") API. Specify the filter name
and the associated detector ID for the particular Region.

Alternatively, you can use the following AWS CLI example by replacing the
values formatted in `red`:

```

aws guardduty delete-filter \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--filter-name `filterName` \
--region `us-east-1`

```

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.
