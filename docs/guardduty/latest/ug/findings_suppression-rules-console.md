# Creating suppression rules in

GuardDuty

A suppression rule is a set of criteria that includes using filter attributes and
providing values for which you don't want GuardDuty to generate a finding type. The
finding types that match this criteria are automatically archived. To reduce noise, the
suppressed findings are not sent to any of the AWS services with which you may
integrate. For more information about common use cases for creating suppression rules,
see [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md").

You can visualize, create, and manage suppression rules by using the GuardDuty console.
Suppression rules are generated in the same manner as filters, and your existing saved
filters can be used as suppression rules. For more information about creating filters,
see [Filtering findings in GuardDuty](guardduty_filter-findings.md "guardduty_filter-findings.md").

Choose your preferred access method to create a suppression rule for GuardDuty finding
types.

Console

###### To create a

suppression rule using the console:

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. On the **Findings** page,
   the **Create suppression rule** feature remains grayed out unless you add at least
   one filter criterion. Because suppression rules are applied to
   active, ongoing findings, make sure that the **Status** menu is set to
   **Current**.
3. To add one or more filter criteria, follow steps 3 through 7 in [Adding filters on Findings page](guardduty_filter-findings.md#guardduty-add-filters-findings-page "guardduty_filter-findings.md#guardduty-add-filters-findings-page"), and then continue with the following steps.
4. After you have added the filter criteria and confirmed that the
   filtered findings meet your requirements, choose
   **Create suppression rule**.
5. Enter a **Name** for the suppression rule.The name must be 3-64 characters. Valid characters
   are a-z, A-Z, 0-9, period (.), hyphen (-), and underscore (\_).
6. The **Description** is optional.
   If you enter a description, it can have up to 512 characters.
7. Choose **Create**.

You can also create a suppression rule from an existing saved filter. For
more information about creating filters, see [Filtering findings in GuardDuty](guardduty_filter-findings.md "guardduty_filter-findings.md").

###### To create a

suppression rule from a saved filter:

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. On the **Findings** page, from the **Saved rules**
   menu, select a saved filter set rule. This will automatically display the filter set and findings
   that match the criteria.
3. You can also add more filter criteria to this saved rule. If you don't need additional
   filter criteria, skip this step.

To add one or more additional filter criteria, follow steps 2 through the end of the preceding
procedure - [To create a suppression rule using the console](#findings_suppression-rules-create-console "#findings_suppression-rules-create-console"). 4. If you don't need to add additional filter criteria to the saved rule, follow
steps 4 through the end of the preceding procedure - [To create a suppression rule using the console](#findings_suppression-rules-create-console "#findings_suppression-rules-create-console").

API/CLI

###### To create a suppression rule using API:

1. You can create suppression rules through the [CreateFilter](../APIReference/API_CreateFilter.md "../APIReference/API_CreateFilter.md") API. To do so, specify
   the filter criteria in a JSON file following the format of the
   example detailed below. The below example will suppress any
   unarchived low-severity findings that has a DNS request to the
   `test.example.com` domain. For medium severity findings, the input
   list will be `["4", "5", "7"]`. For high severity
   findings, the input list will be `["6", "7", "8"]`. For
   critical severity findings, the input list will be `["9", "10"]`. You
   can also filter on the basis of any one value in the list.

The following example adds a filter for low severity findings.

```
{
    "Criterion": {
        "service.archived": {
            "Eq": [
                "false"
            ]
        },
        "service.action.dnsRequestAction.domain": {
            "Eq": [
                "test.example.com"
            ]
        },
        "severity": {
            "Eq": [
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
aws guardduty list-findings --detector-id `12abc34d567e8fa901bc2d34e56789f0` --finding-criteria file://`criteria.json`
```

2. Upload your filter to be used as suppression rule with the [CreateFilter](../APIReference/API_CreateFilter.md "../APIReference/API_CreateFilter.md") API or by using the
   AWS CLI following the example below with your own detector ID, a
   name for the suppression rule, and .json file.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty create-filter --action ARCHIVE --detector-id `12abc34d567e8fa901bc2d34e56789f0` --name `yourfiltername` --finding-criteria file://`criteria.json`

```

You can view a list of your filters programmatically with the [ListFilter](../APIReference/API_ListFilter.md "../APIReference/API_ListFilter.md") API. You can view the details of
an individual filter by supplying the filter name to the [GetFilter](../APIReference/API_GetFilter.md "../APIReference/API_GetFilter.md") API. Update filters using [UpdateFilter](../APIReference/API_UpdateFilter.md "../APIReference/API_UpdateFilter.md") or delete them with the [DeleteFilter](../APIReference/API_DeleteFilter.md "../APIReference/API_DeleteFilter.md") API.
