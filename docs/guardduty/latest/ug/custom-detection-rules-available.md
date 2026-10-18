

# Available Custom Detection Rules
<a name="custom-detection-rules-available"></a>

GuardDuty Custom Detection Rules offers a library of opt-in detections that target activity which might be routine in one environment but a sign of compromise in another. You can choose to enable these rules based on risks specific to your environment. To get the current list of available rules, use the [ListCustomDetectionRules](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCustomDetectionRules.html) API operation. For the finding types that each rule generates, see [Custom Detection Rules finding types](findings-custom-detection-rules.md).

**Note**  
The availability of individual rules depends on the availability of the corresponding AWS service and feature in each Region. For example, rules that target AWS Organizations or Amazon Simple Email Service are available only in Regions where those services operate. Similarly, rules that target Lambda function URLs or SageMaker AI notebook instances are available only in Regions where those features are supported.

## Viewing rule detection logic
<a name="custom-detection-rules-viewing-logic"></a>

Each rule defines specific conditions that determine when it fires. You can inspect the detection logic for any rule:
+ **Console** – In the GuardDuty console, navigate to **Custom Detection Rules**, and choose a rule name. The split panel displays the rule's detection logic on the **Details** tab.
+ **API** – Call the [GetCustomDetectionRule](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRule.html) operation. The response includes the rule's expression in the `Definition.Expression` field.

The following image shows the Custom Detection Rules catalog.

![Custom Detection Rules catalog listing available rules with columns for name, severity, and status, and property filter controls above the table.](https://docs.aws.amazon.com/guardduty/latest/ug/images/custom-detection-rules-rule-catalog.png)


The following image shows the rule details panel with the detection logic.

![Rule details split panel with the Details tab selected, showing the rule's SQL-based detection logic expression.](https://docs.aws.amazon.com/guardduty/latest/ug/images/custom-detection-rules-rule.png)


## Functions used in detection logic
<a name="custom-detection-rules-functions"></a>

Custom Detection Rules use SQL conditions. AWS CloudTrail rules evaluate AWS CloudTrail event fields, and some use specialized functions to inspect nested JSON structures within event fields like `requestParameters` and `responseElements`. Runtime Monitoring rules evaluate runtime event fields, and many use regular expression functions, mainly to match process command lines. The following table describes the functions that might appear in rule detection logic.

A rule that inspects a nested field depends on that field being present in the event. For more information about fields that AWS CloudTrail does not record, see [Redacted event fields](custom-detection-rules-how-it-works.md#custom-detection-rules-how-it-works-redacted-fields).


| Function | Returns | Description | 
| --- | --- | --- | 
| `get_json_object(json, path)` | String | Extracts a value from a JSON document using a dot-separated path (for example, `$.requestParameters.bucketName`). Returns the value as a string. | 
| `json_collect_values(json, path, field)` | Array | Navigates to an array within a JSON document and collects the specified field from each element. This function extracts a list of values from repeated structures like IAM policy statements or security group rules. | 
| `get_aws_principal(policy_json, effect)` | Array | Parses an IAM, Amazon S3, or Lambda resource policy and returns the AWS account principals from statements that match the specified effect (Allow or Deny). This function detects cross-account access in resource policies. | 
| `policy_has_public_principal(policy_json, effect)` | Boolean | Returns true when any statement with the specified effect grants access to a public principal (`"*"`). This function detects policies that allow public access. | 
| `RE2_FIND(input, pattern)` | Boolean | Returns true when the RE2 regular expression `pattern` matches any part of `input`. The match is case sensitive. Returns false when `input` is null. Runtime Monitoring rules use this function mainly to match process command lines. | 
| `IRE2_FIND(input, pattern)` | Boolean | Same as `RE2_FIND`, but the match is not case sensitive. | 

The GuardDuty security agent records a process's command-line arguments separated by null characters. Most Runtime Monitoring rules that match a command line first replace these separators with spaces, for example `RE2_FIND(REPLACE(process.cmd_line, '\u0000', ' '), pattern)`.

The detection logic SQL for Runtime Monitoring rules is an approximation of how GuardDuty detects activity, not the exact logic.