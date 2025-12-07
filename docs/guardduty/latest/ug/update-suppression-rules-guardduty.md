#

Updating suppression rules in GuardDuty

This section provides the steps to update a suppression rule in your AWS account in
a specific AWS Region.

You can update existing suppression rules from the **Suppression rules** page in the GuardDuty
console. GuardDuty supports updating the suppression filter description, rank and filter
criteria from the GuardDuty console or by using the GuardDuty CLI/API. Updating suppression
rule follows the same restrictions on the field values for description, rank and
criteria as [Creating suppression
rules](create-suppression-rules-guardduty.md "create-suppression-rules-guardduty.md").

If you're a member account, your administrator account can take this action on your behalf. For more
information, see [Administrator account and member
account relationships](administrator_member_relationships.md "administrator_member_relationships.md").

Choose your preferred access method to delete a suppression rule for GuardDuty findingtypes.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. On the **Suppression rules** page, select the suppression rule to update.
3. From the **Actions** dropdown, select **Update suppression rule**.
4. This opens the existing the suppression rule form.
5. Make changes to the **Description**, **Rank**
   and **Attributes** section as required.
6. Select **Update suppression rule** to update the Suppression rule.

API/CLI

###### To update a suppression rule using API:

1. You can update suppression rules through the UpdateFilter API. Only
   **description**, **rank** and
   **criteria** can be updated using the UpdateFilter API.
   All these three fields are optional.
2. To update an existing filter, you will need the name of the filter that you are planning to update.
3. If you want to update the existing criteria, create a JSON file with the updated criteria similar to how you first created the filter. An example criteria to suppress any unarchived low-severity findings that has a DNS request to the test.example.com domain. For medium severity findings, the input list will be ["4", "5", "7"]. For high severity findings, the input list will be ["6", "7", "8"]. For critical severity findings, the input list will be ["9", "10"]. You can also filter on the basis of any one value in the list. The following example adds a filter for low severity findings.

```

{
    "Criterion": {
        "service.action.dnsRequestAction.domain": {
            "Equals": [
                "test.example.com"
            ]
        },
        "severity": {
            "Equals": [
                "1",
                "2",
                "3"
            ]
        }
    }
}

```

For a list of JSON field names and their console equivalent see
[Property filters in GuardDuty](guardduty_filter-findings.md#filter_criteria "guardduty_filter-findings.md#filter_criteria").

To test your filter criteria, use the same JSON criterion in the
[ListFindings](../APIReference/API_ListFindings.md "../APIReference/API_ListFindings.md") API, and confirm that
the correct findings have been selected. To test your filter
criteria using AWS CLI follow the example using your own detectorId
and .json file.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```

aws guardduty list-detectors --region `us-east-1`

```

4. If you want to update the description, you can include the description parameter in the CLI call.
5. If you want to update the rank, you can include the rank parameter in the CLI call.
6. If you want to update from a suppression filter to a regular filter, using the
   action parameter and value as **ARCHIVE** in the CLI call.
7. Update your existing filter API or by using the AWS CLI following the example below with
   your own detector ID, a name for the suppression rule, and .json file.
8. The following is an example CLI that updates all the parameters described above.
   You can select the specific parameters to be updated for your use case from the command -

```

aws guardduty update-filter \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--region `us-east-1` \
--action `ARCHIVE` \
--rank `1` \
--description `"Updated description"` \
--finding-criteria `file://criteria.json`


```
