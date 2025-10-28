# Analyzing findings from automated sensitive data discovery

When Amazon Macie performs automated sensitive data discovery, it creates a sensitive data finding for each Amazon Simple Storage Service
(Amazon S3) object that it finds sensitive data in. A _sensitive data
finding_ is a detailed report of sensitive data that Macie found in an S3 object. A
finding doesn't include the sensitive data that Macie found. Instead, it provides information
that you can use for further investigation and remediation as necessary.

Each sensitive data finding provides a severity rating and details such as:

- The date and time when Macie found the sensitive data.
- The category and types of sensitive data that Macie found.
- The number of occurrences of each type of sensitive data that Macie found.
- How Macie found the sensitive data, automated sensitive data discovery or a sensitive data discovery job.
- The name, public access settings, encryption type, and other information about the
  affected S3 bucket and object.
  Depending on the affected S3 object's file type or storage format, the details can also
  include the location of as many as 15 occurrences of the sensitive data that Macie found.

Macie stores sensitive data findings for 90 days. You can access them by using the Amazon Macie
console or the Amazon Macie API. You can also monitor and process findings by using other
applications, services, and systems. For more information, see [Reviewing and analyzing findings](findings.md "findings.md").

###### To analyze findings produced by automated sensitive data discovery

To identify and analyze findings that Macie created while performing automated sensitive data discovery, you can
filter your findings. With filters, you use specific attributes of findings to build custom
views and queries for findings. To filter findings, you can use the Amazon Macie console or submit
queries programmatically using the Amazon Macie API. For more information, see [Filtering findings](findings-filter-overview.md "findings-filter-overview.md").

###### Note

If your account is part of an organization that centrally manages multiple Macie accounts,
only the Macie administrator for your organization has direct access to findings that automated sensitive data discovery
produces for accounts in your organization. If you have a member account and want to review the
findings for your account, contact your Macie administrator.

Console
Follow these steps to identify and analyze the findings by using the Amazon Macie
console.

###### To analyze findings produced by automated discovery

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Findings**.
3. To display findings that were suppressed by a [suppression rule](findings-suppression.md "findings-suppression.md"), change the **Finding status** setting. Choose
   **All** to display both suppressed and unsuppressed findings, or choose
   **Archived** to display only suppressed findings. To then hide suppressed
   findings again, choose **Current**.
4. Place your cursor in the **Filter criteria** box. In the list of
   fields that appears, choose **Origin type**.

This field specifies how Macie found the sensitive data that produced a finding,
automated sensitive data discovery or a sensitive data discovery job. To find this field in the list of filter
fields, you can browse the complete list, or enter part of the field's name to narrow the
list of fields. 5. Select **AUTOMATED_SENSITIVE_DATA_DISCOVERY** as the value for the
field, and then choose **Apply**. Macie applies the filter criteria and
adds the condition to a filter token in the **Filter criteria** box. 6. To refine the results, add filter conditions for additional fields—for example,
**Created at** for the time range when a finding was created, **S3
bucket name** for the name of an affected bucket, or **Sensitive data
detection type** for the type of sensitive that was detected and produced a
finding.

If you want to subsequently use this set of conditions again, you can save it as a filter
rule. To do this, choose **Save rule** in the **Filter
criteria** box. Then enter a name and, optionally, a description for the rule. When
you finish, choose **Save**.

API
To identify and analyze the findings programmatically, specify filter criteria in queries
that you submit using the [ListFindings](../APIReference/findings.md "../APIReference/findings.md") or [GetFindingStatistics](../APIReference/findings-statistics.md "../APIReference/findings-statistics.md") operation of the Amazon Macie API. The
**ListFindings** operation returns an array of finding IDs, one ID for each
finding that matches the filter criteria. You can then use those IDs to retrieve the details
of each finding. The **GetFindingStatistics** operation returns aggregated
statistical data about all the findings that match the filter criteria, grouped by a field
that you specify in your request. For more information about filtering findings
programmatically, see [Filtering findings](findings-filter-overview.md "findings-filter-overview.md").

In the filter criteria, include a condition for the `originType` field. This
field specifies how Macie found the sensitive data that produced a finding, automated sensitive data discovery or a
sensitive data discovery job. If automated sensitive data discovery produced a finding, the value for this field is
`AUTOMATED_SENSITIVE_DATA_DISCOVERY`.

To identify and analyze the findings by using the AWS Command Line Interface (AWS CLI), run the [list-findings](../../../cli/latest/reference/macie2/list-findings.md "../../../cli/latest/reference/macie2/list-findings.md") or [get-finding-statistics](../../../cli/latest/reference/macie2/get-finding-statistics.md "../../../cli/latest/reference/macie2/get-finding-statistics.md") command. The following examples use the
**list-findings** command to retrieve finding IDs for all high-severity
findings that automated sensitive data discovery produced in the current AWS Region.

This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 list-findings \
--finding-criteria '{"criterion":{"classificationDetails.originType":{"eq":["AUTOMATED_SENSITIVE_DATA_DISCOVERY"]},"`severity.description`":{"`eq`":["`High`"]}}}'`
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 list-findings ^
--finding-criteria={\"criterion\":{\"classificationDetails.originType\":{\"eq\":[\"AUTOMATED_SENSITIVE_DATA_DISCOVERY\"]},\"`severity.description`\":{\"`eq`\":[\"`High`\"]}}}`
```

Where:

- `classificationDetails.originType` specifies the JSON name of the
  **Origin type** field, and:
  - `eq` specifies the _equals_
    operator.
  - `AUTOMATED_SENSITIVE_DATA_DISCOVERY` is an enumerated value for the
    field.

- `severity.description` specifies the JSON name of
  the **Severity** field, and:
  - `eq` specifies the _equals_ operator.
  - `High` is an enumerated value for the
    field.

If the request succeeds, Macie returns a `findingIds` array. The array lists
the unique identifier for each finding that matches the filter criteria, as shown in the
following example.

```
`{
 "findingIds": [
 "1f1c2d74db5d8caa76859ec52example",
 "6cfa9ac820dd6d55cad30d851example",
 "702a6fd8750e567d1a3a63138example",
 "826e94e2a820312f9f964cf60example",
 "274511c3fdcd87010a19a3a42example"
 ]
}`
```

If no findings match the filter criteria, Macie returns an empty `findingIds`
array.

```
`{
 "findingIds": []
}`
```
