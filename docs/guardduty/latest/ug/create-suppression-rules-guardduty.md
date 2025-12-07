# Creating suppression rules in

GuardDuty

A suppression rule is a set of criteria that includes using filter attributes and
providing values for which you don't want GuardDuty to generate a finding type. The
finding types that match this criteria are automatically archived. To reduce noise, the
suppressed findings are not sent to any of the AWS services with which you may
integrate. For more information about common use cases for creating suppression rules,
see [Suppression rules](findings_suppression-rule.md "findings_suppression-rule.md").

You can visualize, create, and manage suppression rules by using the **Suppression rules** page
in the GuardDuty console. Suppression rules can also be generated from your existing saved filters.
For more information about creating filters, see
[Filtering findings in GuardDuty](guardduty_filter-findings.md "guardduty_filter-findings.md").

The filter criteria can include an exact match using **Equals** and
**NotEquals** operators, a **wildcard match** using
the **Matches** and **NotMatches** operators or
**comparison match** using **GreaterThan**,
**GreaterThanEquals**, **LessThan** and **LessThanEquals**
operators. More information on the available operators can be found in the
[Conditions](../APIReference/API_Condition.md "../APIReference/API_Condition.md") page.

Choose your preferred access method to create a suppression rule for GuardDuty finding
types.

Console

###### To create a

suppression rule using the console:

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. On the **Suppression rules** page, click on the **Create suppression rule**
   to open the **Create suppression rule** form.
3. Enter a **Name** for the suppression rule. The name must be 3-64 characters.
   Valid characters are a-z, A-Z, 0-9, period (.), hyphen (-), and underscore (\_).
4. The **Description** is optional. If you enter a description, it can have up
   to 512 characters. Valid characters are a-z, A-Z, 0-9, period (.), hyphen (-), colon (:),
   brackets({}()[]), forward slash (/), and space.
5. The **Rank** is optional. It can be a numerical value from 1 up to the total
   count of filters and suppression rules, plus 1.
6. Under the **Attributes** section, select a **Key** and an
   **Operator** from the drop-down.
7. Enter the value either “string” or “date” from the datepicker based on the selected key.
   If it is a string value, type the text and press enter. Multiple values can be added in case of
   string values.
8. Additional criteria can be added by selecting **Add Criteria** to add another
   set of **Key**, and **Value(s)**.
9. Select **Create suppression rule** to create and save the suppression rule.

You can also create a suppression rule from an existing saved filter. For
more information about creating filters, see [Filtering findings in GuardDuty](guardduty_filter-findings.md "guardduty_filter-findings.md").

###### To create a

suppression rule from a saved filter:

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. On the **Findings** page, from the **Saved rules**
   menu, select a saved filter set rule. This will automatically display the filter set and findings
   that match the criteria.
3. You can also add more filter criteria to this saved rule. If you don't need additional
   filter criteria, skip this step. To add one or more filter criteria, follow steps 3
   through 7 in [Adding filters on Findings page](guardduty_filter-findings.md#guardduty-add-filters-findings-page "guardduty_filter-findings.md#guardduty-add-filters-findings-page"), and then continue with the following steps.
4. After you have added the filter criteria and confirmed that the
   filtered findings meet your requirements, choose
   **Create suppression rule**.
5. Enter a **Name** for the suppression rule.The name must be 3-64 characters. Valid characters
   are a-z, A-Z, 0-9, period (.), hyphen (-), and underscore (\_).
6. The **Description** is optional.
   If you enter a description, it can have up to 512 characters.
7. Choose **Create**.
8. If you don't need to add additional filter criteria to the saved rule, follow steps 4 through 7 to create the filter.

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

The following example adds a filter for low severity findings for lambda functions
with function name prefix "MyFunc" and function tag with prefix not as "TestTag"

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

You can create suppression rules using wildcard characters \* and ? . Wildcards in filters
are supported using **Matches** and **NotMatches**
operators only. To match any number of characters, you can use \* in the attribute value
and to match a single character, you can use ? in the attribute value. Filters support a
maximum of 5 attributes under a single wildcard condition and a maximum of 5 wildcard
character within a single attribute. The following example adds a filter for Lambda name
matching the prefix “MyFunc" but not Lambda functions with tags with "TestTag" as prefix
followed by 0-2 characters.

```

{
    "Criterion": {
        "resource.lambdaDetails.functionName": {
            "Matches": [
                "MyFunc*"
            ]
        },
        "resource.lambdaDetails.tags.key": {
            "NotMatches": [
                "TestTag??"
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
aws guardduty list-detector
```

```

aws guardduty list-findings \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--region `us-east-1` \
--finding-criteria file://`criteria.json`

```

###### Note

Wildcards matching are not available for ListFindings and
GetFindingsStatistics. Criteria containing wildcards cannot
be validated using ListFindings and GetFindingsStatistics. 2. Upload your filter to be used as suppression rule with the [CreateFilter](../APIReference/API_CreateFilter.md "../APIReference/API_CreateFilter.md") API or by using the
AWS CLI following the example below with your own detector ID, a
name for the suppression rule, and .json file.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```

aws guardduty create-filter \
--detector-id `12abc34d567e8fa901bc2d34e56789f0` \
--region `us-east-1` \
--action ARCHIVE \
--name `yourfiltername` \
--finding-criteria file://`criteria.json`

```

You can view a list of your filters programmatically with the [ListFilter](../APIReference/API_ListFilter.md "../APIReference/API_ListFilter.md") API. You can view the details of
an individual filter by supplying the filter name to the [GetFilter](../APIReference/API_GetFilter.md "../APIReference/API_GetFilter.md") API. Update filters using [UpdateFilter](../APIReference/API_UpdateFilter.md "../APIReference/API_UpdateFilter.md") or delete them with the [DeleteFilter](../APIReference/API_DeleteFilter.md "../APIReference/API_DeleteFilter.md") API.
