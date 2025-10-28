# Creating a custom data identifier

A _custom data identifier_ is a set of criteria that you define to
detect sensitive data in Amazon Simple Storage Service (Amazon S3) objects. When you create a custom data
identifier, you specify a regular expression (_regex_)
that defines a text pattern to match in an S3 object. You can also specify character
sequences and a proximity rule that refine the results. The character sequences can be:
_keywords_, which are words or phrases that must be
in proximity of text that matches the regex, or _ignore
words_, which are words or phrases to exclude from results. By using
custom data identifiers, you can supplement the [managed data identifiers](managed-data-identifiers.md "managed-data-identifiers.md") that Amazon Macie provides, and detect sensitive data
that reflects your organization's particular scenarios, intellectual property, or
proprietary data.

For example, many companies have a specific syntax for employee IDs. One such syntax
might be: a capital letter that indicates whether an employee is a full-time (_F_) or part-time (_P_)
employee, followed by a hyphen (–), followed by an eight-digit sequence that
identifies the employee. Examples are: _F–12345678_ for a full-time employee, and _P–87654321_ for a part-time employee. To detect employee IDs that
use this syntax, you might create a custom data identifier that specifies the following
regex: `[A-Z]-\d{8}`. To refine the analysis and avoid false positives, you
might also configure the identifier to use keywords (`employee` and
`employee ID`) and a maximum match distance of 20 characters. With these
criteria, results include text that matches the regex if the text occurs after the
keyword _employee_ or _employee
ID_ and all the text occurs within 20 characters of one of those
keywords.

For a demonstration of how keywords can help you find
sensitive data and avoid false positives, watch the following video:

In addition to detection criteria, you can optionally specify custom severity settings
for findings that a custom data identifier produces. Severity can be based on the number
of occurrences of text that match the identifier's detection criteria. If you don't
specify these settings, Macie automatically assigns the _Medium_ severity to all the findings that the identifier produces.
Severity doesn't change based on the number of occurrences of text that match the
identifier's detection criteria.

For detailed information about these and other settings, see [Configuration options for custom data identifiers](cdis-options.md "cdis-options.md").

###### To create a custom data identifier

You can create a custom data identifier by using the Amazon Macie console or the
Amazon Macie API.

Console
Follow these steps to create a custom data identifier by using the
Amazon Macie console.

###### To create a custom data identifier

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, under **Settings**,
   choose **Custom data identifiers**.
3. Choose **Create**.
4. For **Name**, enter a name for the custom data
   identifier. The name can contain as many as 128 characters.
5. For **Description**, optionally enter a brief
   description of the custom data identifier. The description can
   contain as many as 512 characters.

###### Note

Avoid including sensitive data in the name or description of a
custom data identifier. Other users of your account might be
able to access the name or description, depending on the actions
that they're allowed to perform in Macie. 6. For **Regular expression**, enter the regular
expression (_regex_) that defines
the text pattern to match. The regex can contain as many as 512
characters.

Macie supports a subset of the pattern syntax provided by the
[Perl Compatible Regular
Expressions (PCRE) library](https://www.pcre.org/ "https://www.pcre.org/"). For additional details and
tips, see [Detection criteria
for custom data identifiers](cdis-options.md#cdis-detection-criteria "cdis-options.md#cdis-detection-criteria"). 7. For **Keywords**, optionally enter as many as 50
character sequences (separated by commas) to define specific text
that must be in proximity of text that matches the regex
pattern.

Macie includes an occurrence in results only if the text matches
the regex pattern and the text is within the maximum match distance
of one of these keywords. Each keyword can contain 3–90 UTF-8
characters. Keywords aren't case sensitive. 8. For **Ignore words**, optionally enter as many as
10 character sequences (separated by commas) that define specific
text to exclude from results.

Macie excludes an occurrence from results if the text matches the
regex pattern but it contains one of these ignore words. Each ignore
word can contain 4–90 UTF-8 characters. Ignore words are case
sensitive. 9. For **Maximum match distance**, optionally enter
the maximum number of characters that can exist between the end of a
keyword and the end of text that matches the regex pattern.

Macie includes an occurrence in results only if the text matches
the regex pattern and the text is within this distance of a complete
keyword. The distance can be 1–300 characters. The default
distance is 50 characters. 10. For **Severity**, choose how to determine the
severity of sensitive data findings that the custom data identifier
produces:

    * To automatically assign the *Medium* severity to all findings, choose
     **Use Medium severity for any number of matches
     (default)**. With this option, Macie
     automatically assigns the *Medium* severity to a finding if the affected
     S3 object contains one or more occurrences of text that
     match the detection criteria.
    * To assign severity based on occurrences thresholds that
     you specify, choose **Use custom settings to
     determine severity**. Then use the
     **Occurrences threshold** and
     **Severity level** options to specify
     the minimum number of matches that must exist in an S3
     object to produce a finding with a selected severity.


    You can specify as many as three occurrences thresholds,
     one for each severity level that Macie supports: *Low* (least severe), *Medium*, or *High* (most severe). If you
     specify more than one, the thresholds must be in ascending
     order by severity, moving from *Low* to *High*. If an S3 object contains fewer
     occurrences than the lowest threshold, Macie doesn't create
     a finding.

11. (Optional) For **Tags**, choose **Add
    tag**, and then enter as many as 50 tags to assign to
    the custom data identifier.

A *tag* is a label that you define and assign to certain types of AWS resources. Each tag consists of a required tag key and an optional tag value. Tags can help you identify, categorize, and manage resources in different ways, such as by purpose, owner, environment, or other criteria. To learn more, see [Tagging Macie resources](tagging-resources.md "tagging-resources.md"). 12. (Optional) For **Evaluate**, enter up to 1,000
characters in the **Sample data** box, and then
choose **Test** to test the detection criteria.
Macie evaluates the sample data and reports the number of
occurrences of text that match the criteria. You can repeat this
step as many times as you like to refine and optimize the
criteria.

###### Note

We strongly recommend that you test and refine the detection criteria with sample
data. Because custom data identifiers are used by sensitive data
discovery jobs, you can't change a custom data identifier after
you create it. This helps ensure that you have an immutable history of sensitive data findings and discovery results. 13. When you finish, choose **Submit**.

Macie tests the settings and verifies that it can compile the regex. If
there's an issue with a setting or the regex, Macie displays an error that
describes the issue. After you address any issues, you can save the custom
data identifier.

API
To create a custom data identifier programmatically, use the [CreateCustomDataIdentifier](../APIReference/custom-data-identifiers.md "../APIReference/custom-data-identifiers.md") operation of the Amazon Macie API. Or,
if you're using the AWS Command Line Interface (AWS CLI), run the [create-custom-data-identifier](../../../cli/latest/reference/macie2/create-custom-data-identifier.md "../../../cli/latest/reference/macie2/create-custom-data-identifier.md") command.

###### Note

Before you create a custom data identifier, we strongly recommend that you test and
refine its detection criteria with sample data. Because custom data
identifiers are used by sensitive data discovery jobs, you can't change
a custom data identifier after you create it. This helps ensure that you have an immutable history of sensitive data findings and discovery results.

To test the criteria programmatically, you can use the [TestCustomDataIdentifier](../APIReference/custom-data-identifiers-test.md "../APIReference/custom-data-identifiers-test.md") operation of the Amazon Macie API.
This operation provides an environment for evaluating sample data with
detection criteria. If you're using the AWS CLI, you can run the [test-custom-data-identifier](../../../cli/latest/reference/macie2/test-custom-data-identifier.md "../../../cli/latest/reference/macie2/test-custom-data-identifier.md") command to test the
criteria.

When you're ready to create the custom data identifier, use the following
parameters to define its detection criteria:

- `regex` – Specify the regular expression
  (_regex_) that defines the text
  pattern to match. The regex can contain as many as 512
  characters.

Macie supports a subset of the pattern syntax provided by the
[Perl Compatible Regular
Expressions (PCRE) library](https://www.pcre.org/ "https://www.pcre.org/"). For additional details and
tips, see [Detection criteria
for custom data identifiers](cdis-options.md#cdis-detection-criteria "cdis-options.md#cdis-detection-criteria").

- `keywords` – Optionally specify 1–50
  character sequences (_keywords_)
  that must be in proximity of text that matches the regex
  pattern.

Macie includes an occurrence in results only if the text matches
the regex pattern and the text is within the maximum match distance
of one of these keywords. Each keyword can contain 3–90 UTF-8
characters. Keywords aren't case sensitive.

- `maximumMatchDistance` – Optionally specify the
  maximum number of characters that can exist between the end of a
  keyword and the end of text that matches the regex pattern. If
  you're using the AWS CLI, use the `maximum-match-distance`
  parameter to specify this value.

Macie includes an occurrence in results only if the text matches
the regex pattern and the text is within this distance of a complete
keyword. The distance can be 1–300 characters. The default
distance is 50 characters.

- `ignoreWords` – Optionally specify 1–10
  character sequences (_ignore
  words_) to exclude from results. If you're using the
  AWS CLI, use the `ignore-words` parameter to specify these
  character sequences.

Macie excludes an occurrence from results if the text matches the
regex pattern but it contains one of these ignore words. Each ignore
word can contain 4–90 UTF-8 characters. Ignore words are case
sensitive.

To specify the severity of sensitive data findings that the custom data
identifier produces, use the `severityLevels` parameter or, if
you're using the AWS CLI, the `severity-levels` parameter:

- To automatically assign the `MEDIUM` severity to all
  the findings, omit this parameter. Macie then uses the default
  setting. By default, Macie assigns the `MEDIUM` severity
  to a finding if the affected S3 object contains one or more
  occurrences of text that match the detection criteria.
- To assign severity based on occurrences thresholds that you
  specify, specify the minimum number of matches that must exist in an
  S3 object to produce a finding with a specified severity.

You can specify as many as three occurrences thresholds, one for
each severity level that Macie supports: `LOW` (least
severe), `MEDIUM`, or `HIGH` (most severe). If
you specify more than one, the thresholds must be in ascending order
by severity, moving from `LOW` to `HIGH`. If
an S3 object contains fewer occurrences than the lowest threshold,
Macie doesn't create a finding.

Use additional parameters to specify a name and other settings, such as
tags, for the custom data identifier. Avoid including sensitive data in
these settings. Other users of your account might be able to access these
values, depending on the actions that they're allowed to perform in
Macie.

When you submit your request, Macie tests the settings and verifies that
it can compile the regex. If there's an issue with a setting or the regex,
the request fails and Macie returns a message that describes the issue. If
the request succeeds, you receive output similar to the following:

```
`{
 "customDataIdentifierId": "393950aa-82ea-4bdc-8f7b-e5be3example"
}`
```

Where `customDataIdentifierId` specifies the unique identifier
(ID) for the custom data identifier that was created.

To subsequently retrieve and review the settings for the custom data
identifier, use the [GetCustomDataIdentifier](../APIReference/custom-data-identifiers-id.md "../APIReference/custom-data-identifiers-id.md") operation or, if you’re using the
AWS CLI, run the [get-custom-data-identifier](../../../cli/latest/reference/macie2/get-custom-data-identifier.md "../../../cli/latest/reference/macie2/get-custom-data-identifier.md") command. For the `id`
parameter, specify the custom data identifier's ID.

The following examples show how to use the AWS CLI to create a custom data
identifier. The examples create a custom data identifier that's designed to
detect employee IDs that use a specific syntax and are within proximity of a
specified keyword. The examples also define custom severity settings for
findings that the identifier produces.

This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 create-custom-data-identifier \
--name "`EmployeeIDs`" \
--regex "`[A-Z]-\d{8}`" \
--keywords '[`"employee","employee ID"`]' \
--maximum-match-distance `20` \
--severity-levels '[{"occurrencesThreshold":`1`,"severity":"`LOW`"},{"occurrencesThreshold":`50`,"severity":"`MEDIUM`"},{"occurrencesThreshold":`100`,"severity":"`HIGH`"}]' \
--description "`Detects employee IDs in proximity of a keyword.`" \
--tags '{"`Stack`":"`Production`"}'`
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 create-custom-data-identifier ^
--name "`EmployeeIDs`" ^
--regex "`[A-Z]-\d{8}`" ^
--keywords "[\"`employee`\",\"`employee ID`\"]" ^
--maximum-match-distance `20` ^
--severity-levels "[{\"occurrencesThreshold\":`1`,\"severity\":\"`LOW`\"},{\"occurrencesThreshold\":`50`,\"severity\":\"`MEDIUM`\"},{\"occurrencesThreshold\":`100`,\"severity\":\"`HIGH`\"}]" ^
--description "`Detects employee IDs in proximity of a keyword.`" ^
--tags={\"`Stack`\":\"`Production`\"}`
```

Where:

- `EmployeeIDs` is the name of
  the custom data identifier.
- `[A-Z]-\d{8}` is the regex
  for the text pattern to match.
- `employee` and
  `employee ID` are
  keywords that must be in proximity of text that matches the regex
  pattern.
- `20` is the maximum number
  of characters that can exist between the end of a keyword and the
  end of text that matches the regex pattern.
- `description` specifies a brief description of the
  custom data identifier.
- `severity-levels` defines custom occurrences thresholds
  for the severity of findings that the custom data identifier
  produces: `LOW` for
  1–49 occurrences;
  `MEDIUM` for 50–99
  occurrences; and, `HIGH` for
  100 or more occurrences.
- `Stack` is the tag key of
  the tag to assign to the custom data identifier.
  `Production` is the
  tag value for the specified tag key.

After you create the custom data identifier, you can [create and configure sensitive data discovery jobs](discovery-jobs-create.md "discovery-jobs-create.md") to use
it, or [add it to your settings for
automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md").
